#!/usr/bin/env python3
"""AI 资讯雷达：从各个免费来源抓取最新的 AI 内容，去重、算热度，生成每天给 GPT 读的「日报素材」。

流程里不调用任何付费模型：抓取、去重、排序全部由代码完成，挑选和写日报交给 ChatGPT 里的 GPT。
来源在 ai_news.toml 里配置，给 GPT 的写作说明在 ai_news_guide.md 里。只依赖 Python 3.11+ 标准库。

用法：
    python ai_news.py              # 抓取并生成 reports/ai-news/日期.md 和 latest.md
    python ai_news.py --dry-run    # 只打印素材，不写文件
    python ai_news.py --check      # 检查每个来源能不能用，不写文件"""

from __future__ import annotations

import argparse
import email.utils
import gzip
import html
import json
import math
import os
import re
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "news"
NOW = datetime.now(timezone.utc)
BEIJING = timezone(timedelta(hours=8))
TODAY = NOW.astimezone(BEIJING).date()  # 日报按北京时间算日期

# 有些网站会拦截不像浏览器的请求
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
MAX_BYTES = 20 * 1024 * 1024
NETWORK_ERRORS = (urllib.error.URLError, TimeoutError, ConnectionError, ET.ParseError,
                  ValueError, KeyError, TypeError, IndexError, AttributeError, gzip.BadGzipFile)
SUMMARY_CHARS = 1500


# ---------------------------------------------------------------- 网络

def http_get(url, headers=None, data=None, retries=2, timeout=30):
    """发请求，返回字节。被限流或服务器出错时等一会儿再试。"""
    req = urllib.request.Request(url, data=data, headers={
        "User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9", **(headers or {})})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read(MAX_BYTES)
            return gzip.decompress(body) if body[:2] == b"\x1f\x8b" else body  # 少数网站不管请求头，总是压缩
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or attempt == retries:
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt == retries:
                raise
        time.sleep(5 * (attempt + 1))


def get_json(url, **kw):
    return json.loads(http_get(url, **kw))


def post_json(url, body, headers, timeout=120):
    return get_json(url, data=json.dumps(body).encode(), retries=0, timeout=timeout,
                    headers={"Content-Type": "application/json", **headers})


def describe_error(e):
    """把异常变成一句人能看懂的话。不会带上 Key。"""
    if isinstance(e, urllib.error.HTTPError):
        msg = ""
        try:
            body = json.loads(e.read()[:4000])
            err = body.get("error") if isinstance(body, dict) else None
            msg = err.get("message", "") if isinstance(err, dict) else str(err or "")
        except (ValueError, OSError):
            pass
        return f"HTTP {e.code}" + (f"：{msg[:150]}" if msg else "")
    if isinstance(e, urllib.error.URLError):
        return f"连不上：{e.reason}"
    return str(e)[:200] or type(e).__name__


# ---------------------------------------------------------------- 文本和时间

def clean_text(s, limit=SUMMARY_CHARS):
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", s or "", flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return " ".join(html.unescape(s).split())[:limit]


def parse_time(s):
    """RSS 的时间（RFC 822）和 Atom / JSON 的时间（ISO 8601）都认，统一成 UTC。"""
    if not s:
        return None
    s = s.strip()
    try:
        dt = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError, IndexError):
        dt = None
    if dt is None:
        try:
            dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def make_item(source, id, title, url, published, summary="", metrics=None, **extra):
    """所有来源统一成这个格式，后面的筛选和 GPT 只认这一种。"""
    item = {
        "source": source,
        "id": id,
        "title": " ".join((title or "").split()),
        "url": url,
        "published": published,
        "summary": clean_text(summary),
        "metrics": metrics or {},
    }
    extra = {k: v for k, v in extra.items() if v}
    if extra:
        item["extra"] = extra
    return item


# ---------------------------------------------------------------- RSS / Atom

def local(tag):
    return tag.rsplit("}", 1)[-1]


def kids(el, name):
    return [c for c in el if local(c.tag) == name]


def first_text(el, *names):
    """按顺序找第一个有内容的子元素，不管命名空间。"""
    for name in names:
        for c in kids(el, name):
            t = "".join(c.itertext()).strip()
            if t:
                return t
    return ""


def deep_text(el, name):
    for c in el.iter():
        if c is not el and local(c.tag) == name:
            t = "".join(c.itertext()).strip()
            if t:
                return t
    return ""


def parse_feed(data):
    """RSS 2.0、RSS 1.0 和 Atom 都能解析，返回条目列表。"""
    root = ET.fromstring(data)
    entries = []
    for el in root.iter():
        if local(el.tag) not in ("item", "entry"):
            continue
        link = ""
        for node in kids(el, "link"):
            href = node.get("href")
            if href is None:  # RSS：链接写在文本里
                link = link or (node.text or "").strip()
            elif node.get("rel", "alternate") == "alternate":  # Atom：链接写在属性里
                link = link or href
        author = kids(el, "author")
        desc = first_text(el, "description", "summary")
        body = first_text(el, "encoded", "content")
        # 有的 Newsletter 的 description 只是一句副标题，这时改用正文
        summary = desc if len(clean_text(desc)) >= 200 or not body else body
        entries.append({
            "el": el,
            "id": first_text(el, "guid", "id"),
            "title": clean_text(first_text(el, "title"), 300),
            "url": link,
            "published": parse_time(first_text(el, "pubDate", "published", "date", "updated")),
            "summary": clean_text(summary or deep_text(el, "description")),
            "author": (first_text(author[0], "name") if author else "") or first_text(el, "creator", "author"),
        })
    return entries


# ---------------------------------------------------------------- 各个来源
# 每个函数返回 (条目列表, 备注)。出错直接抛异常，由 run_source 统一记录。

def fetch_hf_papers(cfg, since):
    """按日期取每天的榜单（今天往前，天数和时间窗口一致）。榜单本身就是「最近的」，不再按时间过滤。"""
    days = max(1, math.ceil((NOW - since).total_seconds() / 86400))
    dates = [(NOW - timedelta(days=n)).date().isoformat() for n in range(days)]
    items, seen = [], set()
    for day in dates:
        try:
            data = get_json(f"https://huggingface.co/api/daily_papers?date={day}&limit=100")
        except urllib.error.HTTPError as e:
            if e.code in (400, 404):  # 当天的榜单还没出来
                continue
            raise
        for d in data:
            p = d.get("paper") or {}
            pid = p.get("id") or d.get("id")
            if not pid or pid in seen:
                continue
            seen.add(pid)
            items.append(make_item(
                "hf_papers", f"arxiv:{pid}", d.get("title") or p.get("title"), f"https://huggingface.co/papers/{pid}",
                parse_time(p.get("submittedOnDailyAt") or d.get("publishedAt") or p.get("publishedAt")),
                p.get("summary") or d.get("summary"),
                {"upvotes": p.get("upvotes", 0), "comments": d.get("numComments", 0)},
                arxiv=f"https://arxiv.org/abs/{pid}", github=p.get("githubRepo"), date=day))
    return items, f"{dates[-1]} 到 {dates[0]} 的榜单"


def fetch_arxiv(cfg, since):
    """官方 RSS 每天给出当天公布的那一批论文，所以不再按时间过滤。"""
    cats = cfg.get("categories") or ["cs.AI", "cs.CL", "cs.LG"]
    entries = parse_feed(http_get("https://rss.arxiv.org/rss/" + "+".join(cats)))
    items, updates = [], 0
    for e in entries:
        if first_text(e["el"], "announce_type") not in ("", "new", "cross"):
            updates += 1  # replace / replace-cross：旧论文出了新版本
            continue
        m = re.search(r"\d{4}\.\d{4,5}", e["id"] + " " + e["url"])
        if not m:
            continue
        abstract = re.sub(r"^.*?Abstract:\s*", "", e["summary"], count=1, flags=re.S)
        cats_of = [c.text.strip() for c in kids(e["el"], "category") if c.text]
        items.append(make_item("arxiv", f"arxiv:{m.group(0)}", e["title"], f"https://arxiv.org/abs/{m.group(0)}",
                               e["published"], abstract, categories=cats_of))
    return items, "当天公布的一批" + (f"，另有 {updates} 篇是旧论文的新版本，已跳过" if updates else "")


def keyword_matcher(words):
    parts = [rf"(?<![a-z0-9]){re.escape(w)}s?(?![a-z0-9])" if len(w) <= 4 else re.escape(w) for w in words]
    if not parts:
        return lambda text: True
    rx = re.compile("|".join(parts), re.I)
    return lambda text: bool(rx.search(text or ""))


def fetch_hackernews(cfg, since):
    min_points = cfg.get("min_points", 50)
    params = urllib.parse.urlencode({
        "tags": "story",
        "hitsPerPage": 1000,
        "numericFilters": f"created_at_i>{int(since.timestamp())},points>={min_points}",
    })
    hits = get_json(f"https://hn.algolia.com/api/v1/search_by_date?{params}")["hits"]
    match = keyword_matcher(cfg.get("keywords", []))
    items = []
    for h in hits:
        title = h.get("title") or ""
        if cfg.get("ai_only", True) and not match(title):
            continue
        discussion = f"https://news.ycombinator.com/item?id={h['objectID']}"
        items.append(make_item(
            "hackernews", f"hn:{h['objectID']}", title, h.get("url") or discussion,
            datetime.fromtimestamp(h["created_at_i"], timezone.utc), h.get("story_text") or "",
            {"points": h.get("points", 0), "comments": h.get("num_comments", 0)}, discussion=discussion))
    return items, f"{min_points} 分以上共 {len(hits)} 条，其中 AI 相关 {len(items)} 条"


def fetch_openrouter(cfg, since):
    models = get_json("https://openrouter.ai/api/v1/models")["data"]
    items = [
        make_item("openrouter", f"openrouter:{m['id']}", m.get("name") or m["id"], f"https://openrouter.ai/{m['id']}",
                  datetime.fromtimestamp(m["created"], timezone.utc), m.get("description") or "",
                  {"context_length": m.get("context_length")}, pricing=m.get("pricing"))
        for m in models if m.get("created")
    ]
    return items, f"平台上共 {len(models)} 个模型"


CHANNEL_ID = re.compile(r"UC[\w-]{22}")
CHANNEL_ID_PATTERNS = [
    r'<link rel="canonical" href="https://www\.youtube\.com/channel/(UC[\w-]{22})"',
    r'"externalId":"(UC[\w-]{22})"',
    r'itemprop="identifier" content="(UC[\w-]{22})"',
]


def resolve_channel(handle, cache):
    """@handle 换成 UC 开头的频道 ID（RSS 只认 ID）。查到的会缓存起来，下次不用再查。"""
    if CHANNEL_ID.fullmatch(handle):
        return handle
    if handle in cache:
        return cache[handle]
    path = handle if handle.startswith("@") else "@" + handle
    page = http_get(f"https://www.youtube.com/{urllib.parse.quote(path, safe='@')}",
                    headers={"Cookie": "SOCS=CAI"}).decode("utf-8", "replace")  # 跳过欧盟的 cookie 同意页
    for pat in CHANNEL_ID_PATTERNS:
        if m := re.search(pat, page):
            cache[handle] = m.group(1)
            return m.group(1)
    raise ValueError("页面里找不到频道 ID，检查一下 handle 是否写对")


def fetch_youtube(handle, cache):
    cid = resolve_channel(handle, cache)
    entries = parse_feed(http_get(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"))
    items = []
    for e in entries:
        vid = first_text(e["el"], "videoId")
        if not vid:
            continue
        stats = next((x for x in e["el"].iter() if local(x.tag) == "statistics"), None)
        views = stats.get("views") if stats is not None else None
        items.append(make_item(
            "youtube", f"yt:{vid}", e["title"], f"https://www.youtube.com/watch?v={vid}", e["published"], e["summary"],
            {"views": int(views) if views and views.isdigit() else None}, channel=e["author"] or handle))
    return items, ""


def fetch_feed(feed):
    urls = feed["url"] if isinstance(feed["url"], list) else [feed["url"]]
    errors = []
    for url in urls:
        try:
            entries = parse_feed(http_get(url))
        except NETWORK_ERRORS as e:
            errors.append(describe_error(e))
            continue
        items = [make_item("feed", f"url:{e['url'] or e['id']}", e["title"], e["url"], e["published"], e["summary"],
                           feed=feed["name"], kind=feed.get("kind", "newsletter"), author=e["author"])
                 for e in entries if e["url"] or e["id"]]
        return items, "" if url == urls[0] else f"主地址失败（{errors[0]}），用的备用地址"
    raise ValueError("；".join(errors))


# ---------------------------------------------------------------- 运行

def run_source(name, fn, since):
    """跑一个来源。since 为 None 表示不按时间过滤。返回 (最近的条目, 状态)。"""
    print(f"[抓取] {name}", file=sys.stderr)
    try:
        items, note = fn()
    except NETWORK_ERRORS as e:
        print(f"  失败：{describe_error(e)}", file=sys.stderr)
        return [], {"name": name, "ok": False, "error": describe_error(e)}
    recent = [i for i in items if since is None or i["published"] is None or i["published"] >= since]
    dated = [i for i in items if i["published"]]
    latest = max(dated, key=lambda i: i["published"]) if dated else (items[0] if items else None)
    status = {"name": name, "ok": True, "total": len(items), "recent": len(recent), "note": note,
              "window_hours": None if since is None else round((NOW - since).total_seconds() / 3600)}
    if latest:
        status["latest"] = {"title": latest["title"],
                            "date": latest["published"].date().isoformat() if latest["published"] else ""}
    print(f"  共 {len(items)} 条，最近的 {len(recent)} 条", file=sys.stderr)
    return recent, status


def build_jobs(cfg, cache):
    """返回 [(显示名, 抓取函数, 时间窗口起点或 None)]。"""
    hours = cfg.get("fetch", {}).get("lookback_hours", 48)
    since = NOW - timedelta(hours=hours)

    def section(key):
        sec = cfg.get(key)
        return sec if sec and sec.get("enabled", True) else None

    jobs = []
    if (c := section("hf_papers")) is not None:
        jobs.append(("HF 每日论文", lambda c=c: fetch_hf_papers(c, since), None))
    if (c := section("arxiv")) is not None:
        jobs.append(("arXiv 新论文", lambda c=c: fetch_arxiv(c, since), None))
    if (c := section("hackernews")) is not None:
        jobs.append(("Hacker News", lambda c=c: fetch_hackernews(c, since), since))
    if (c := section("openrouter")) is not None:
        jobs.append(("OpenRouter 新模型", lambda c=c: fetch_openrouter(c, since), since))
    for feed in cfg.get("feeds", []):
        if feed.get("enabled", True):
            feed_since = NOW - timedelta(hours=feed.get("lookback_hours", hours))
            jobs.append((feed["name"], lambda feed=feed: fetch_feed(feed), feed_since))
    if (yt := section("youtube")) is not None:
        yt_since = NOW - timedelta(hours=yt.get("lookback_hours", hours))
        for ch in yt.get("channels", []):
            jobs.append((f"油管 {ch}", lambda ch=ch: fetch_youtube(ch, cache), yt_since))
    return jobs


# ---------------------------------------------------------------- 日报素材（给 GPT 读）

SOURCE_NAMES = {"hf_papers": "HF 每日论文", "arxiv": "arXiv", "hackernews": "Hacker News", "openrouter": "OpenRouter"}


def source_label(item):
    extra = item.get("extra", {})
    if item["source"] == "feed":
        return extra.get("feed", "博客")
    if item["source"] == "youtube":
        return f"油管 {extra.get('channel', '')}".strip()
    return SOURCE_NAMES.get(item["source"], item["source"])


def canonical_key(item):
    """同一篇论文、同一个网址只算一条：论文统一成 arXiv 编号，网址去掉 www 和跟踪参数。"""
    if item["id"].startswith("arxiv:"):
        return item["id"]
    url = item.get("url") or ""
    if m := re.search(r"(?:arxiv\.org/(?:abs|pdf)|huggingface\.co/papers)/(\d{4}\.\d{4,5})", url):
        return f"arxiv:{m.group(1)}"
    if not url.startswith("http"):
        return item["id"]
    parts = urllib.parse.urlsplit(url)
    query = urllib.parse.urlencode([(k, v) for k, v in urllib.parse.parse_qsl(parts.query)
                                    if not k.startswith("utm_") and k not in ("ref", "source")])
    return parts.netloc.lower().removeprefix("www.") + parts.path.rstrip("/") + (f"?{query}" if query else "")


def merge_items(items):
    """不同来源指向同一个东西时合并成一条，记下所有来源（比如 HN 上在讨论 OpenAI 博客里的同一篇文章）。"""
    merged = {}
    for it in items:
        key = canonical_key(it)
        if key not in merged:
            merged[key] = {**it, "key": key, "sources": [source_label(it)],
                           "metrics": dict(it["metrics"]), "extra": dict(it.get("extra", {}))}
            continue
        m = merged[key]
        if m["source"] == "hackernews" and it["source"] != "hackernews":  # 标题和链接优先用原始出处的
            m.update(title=it["title"], url=it["url"], source=it["source"])
        if it["published"] and (not m["published"] or it["published"] < m["published"]):
            m["published"] = it["published"]  # 发布时间取最早的，方便判断是不是刚冒出来
        if (label := source_label(it)) not in m["sources"]:
            m["sources"].append(label)
        for k, v in it["metrics"].items():
            if isinstance(v, (int, float)) and v > (m["metrics"].get(k) or 0):
                m["metrics"][k] = v
        for k, v in it.get("extra", {}).items():
            m["extra"].setdefault(k, v)
        if len(it["summary"]) > len(m["summary"]):
            m["summary"] = it["summary"]
    return list(merged.values())


STOPWORDS = set("""
a an the and or but of to in on at by for from with without into onto over under about after before between
during via vs than then this that these those it its is are was were be been being am do does did done has have
had having can could will would should may might must not no yes all any some more most less very just only also
even still yet so too as if when where why how what which who whose while until up down out off new now today
week weeks year years day days time first last next one two three own same other another your you we our us my
me he she they them their his her ask show hn launch launches launched introducing announcing announces announced
release released releases update updates updated using use uses used make makes made build builds building built
get gets got way ways thing things here there based part ai ais llm llms model models agent agents agentic open
source data paper papers learning machine deep language large video videos news ainews podcast episode inside
better best good great big small fast faster free tool tools app apps system systems work works working people
company companies don doesn isn can't won't i'm we're you're dont doesnt isnt really why's what's it's
""".split())
TERM_TOKEN = re.compile(r"[a-z][a-z0-9]*(?:[.\-+][a-z0-9]+)*|\d+(?:\.\d+)*")
VERSION = re.compile(r"v?\d+(?:\.\d+)*[a-z]?")


def title_terms(title):
    """标题里的关键词，名字后面跟版本号的连起来算，比如 gemini 4、qwen 3.5。中文标题里的英文名也能认出来。"""
    toks = TERM_TOKEN.findall(title.lower())
    terms = set()
    for i, t in enumerate(toks):
        if t in STOPWORDS or VERSION.fullmatch(t) or len(t) < 3:
            continue
        terms.add(t)
        if i + 1 < len(toks) and VERSION.fullmatch(toks[i + 1]):
            terms.add(f"{t} {toks[i + 1]}")
    return terms


def heat(e):
    m = e["metrics"]
    return (m.get("points") or 0) + (m.get("comments") or 0)


def hot_topics(entries, limit):
    """借鉴 TrendRadar：同一件事在越多不同来源出现，说明讨论越广。

    论文标题术语太多，不参与关键词匹配；论文只有在被别处直接链接时（网址合并）才算多来源。
    """
    pool = [e for e in entries if e["source"] not in ("hf_papers", "arxiv")]
    by_term = {}
    for e in pool:
        for t in title_terms(e["title"]):
            by_term.setdefault(t, {})[e["key"]] = e
    too_common = max(6, len(pool) * 0.15)  # 出现得太多的词（比如 openai）说明不了是同一件事
    scored = []
    for term, group in by_term.items():
        sources = {s for e in group.values() for s in e["sources"]}
        if len(sources) >= 2 and len(group) <= too_common:
            scored.append((len(sources), sum(heat(e) for e in group.values()), term, group))
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)

    clusters = []
    for _, _, term, group in scored:
        keys = set(group)
        for c in clusters:
            if keys <= c["entries"].keys() or len(keys & c["entries"].keys()) / len(keys | c["entries"].keys()) >= 0.5:
                c["terms"].append(term)
                c["entries"].update(group)
                break
        else:
            clusters.append({"terms": [term], "entries": dict(group)})
    # 网址相同、本身就来自多个来源的条目（比如 HN 在讨论某篇官方博客），也单独算一个话题
    clustered = {k for c in clusters for k in c["entries"]}
    for e in entries:
        if len(e["sources"]) >= 2 and e["key"] not in clustered:
            clusters.append({"terms": [e["title"]], "entries": {e["key"]: e}})
    for c in clusters:
        c["sources"] = sorted({s for e in c["entries"].values() for s in e["sources"]})
        c["heat"] = sum(heat(e) for e in c["entries"].values())
    clusters.sort(key=lambda c: (len(c["sources"]), c["heat"]), reverse=True)
    return clusters[:limit]


def md_title(s):
    return (s or "（无标题）").replace("[", "［").replace("]", "］")


def fmt_entry(e, summary_chars=300):
    m = e["metrics"]
    facts = []
    if m.get("points"):
        facts.append(f"HN {m['points']} 分")
    if m.get("upvotes"):
        facts.append(f"{m['upvotes']} 人点赞")
    if m.get("comments"):
        facts.append(f"{m['comments']} 条评论")
    if m.get("views"):
        facts.append(f"播放 {m['views']:,}")
    if e["published"]:
        facts.append(f"发布于 {e['published'].astimezone(BEIJING):%m-%d %H:%M}")
    lines = [f"- [{md_title(e['title'])}]({e['url']}) — 来源：{'、'.join(e['sources'])}"
             + (f"（{'，'.join(facts)}）" if facts else "")]
    extra = e.get("extra", {})
    if (disc := extra.get("discussion")) and disc != e["url"]:
        lines.append(f"  - HN 讨论：{disc}")
    if extra.get("github"):
        lines.append(f"  - 代码：{extra['github']}")
    if e["summary"]:
        lines.append(f"  - 简介：{e['summary'][:summary_chars]}")
    return lines


def fmt_model(e):
    pricing = e.get("extra", {}).get("pricing") or {}

    def per_million(v):
        try:
            x = float(v) * 1e6
        except (TypeError, ValueError):
            return "未知"
        return "免费" if x == 0 else f"${x:g}"

    ctx = e["metrics"].get("context_length")
    facts = [f"上线于 {e['published'].astimezone(BEIJING):%m-%d}"] if e["published"] else []
    if ctx:
        facts.append(f"上下文 {ctx:,} token")
    if pricing:
        facts.append(f"每百万 token 输入 {per_million(pricing.get('prompt'))}、输出 {per_million(pricing.get('completion'))}")
    lines = [f"- [{md_title(e['title'])}]({e['url']}) — {'，'.join(facts)}"]
    if e["summary"]:
        lines.append(f"  - 简介：{e['summary'][:300]}")
    return lines


def fmt_repo(r):
    rate = f"每天 +{r.get('stars_per_day')} 星" + ("" if r.get("growth_basis") == "recent" else "，按总星数平均")
    facts = [f"⭐ {r.get('stars', 0):,}（{rate}）", f"创建 {r.get('age_days')} 天"]
    facts += [x for x in (r.get("language"), r.get("license")) if x]
    if r.get("contributors") is not None:
        facts.append(f"{r['contributors']} 位贡献者")
    tier_name = {"potential": "潜力股", "watch": "值得关注"}.get(r.get("tier"), "")
    facts.append(f"雷达评分 {r.get('score')}" + (f"（{tier_name}）" if tier_name else ""))
    lines = [f"- [{r['name']}]({r['url']}) — {' · '.join(facts)}"]
    if r.get("description"):
        lines.append(f"  - 简介：{r['description'][:300]}")
    if r.get("flags"):
        lines.append(f"  - 风险：{'；'.join(r['flags'])}")
    return lines


def read_guide():
    """写作说明放在素材最前面；开头给人看的引用说明去掉。"""
    path = ROOT / "ai_news_guide.md"
    if not path.exists():
        return ""
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(line for line in lines if not line.startswith(">")).strip()


def build_digest(cfg, items, statuses, radar, seen):
    """返回 (素材 Markdown, 放进素材的条目 key)。"""
    dcfg = cfg.get("digest", {})
    cooldown = dcfg.get("cooldown_days", 7)
    recent_cut = (TODAY - timedelta(days=cooldown)).isoformat()
    # 前几天的素材里已经出现过的不再放；今天早些时候跑过的不算（同一天重跑结果不变）
    entries = [e for e in merge_items(items)
               if not (recent_cut <= seen.get(e["key"], "") < TODAY.isoformat())]
    used = set()

    def take(es):
        used.update(e["key"] for e in es)
        return es

    clusters = hot_topics(entries, dcfg.get("max_hot_topics", 10))
    for c in clusters:
        take(list(c["entries"].values()))
    in_clusters = set(used)
    singles = take(sorted((e for e in entries if e["source"] == "hackernews" and e["key"] not in in_clusters
                           and not e["title"].lower().startswith("show hn")),
                          key=heat, reverse=True)[: dcfg.get("max_hot_single", 8)])
    limit = dcfg.get("max_per_section", 10)
    official = take(sorted((e for e in entries if e.get("extra", {}).get("kind") == "official"),
                           key=lambda e: e["published"] or NOW, reverse=True)[:limit])
    models = take(sorted((e for e in entries if e["source"] == "openrouter"),
                         key=lambda e: e["published"] or NOW, reverse=True)[:limit])
    show_hn = take(sorted((e for e in entries if e["source"] == "hackernews"
                           and e["title"].lower().startswith("show hn")), key=heat, reverse=True)[:limit])
    papers = take(sorted((e for e in entries if e["source"] == "hf_papers"),
                         key=lambda e: (e["metrics"].get("upvotes") or 0, bool(e.get("extra", {}).get("github"))),
                         reverse=True)[: dcfg.get("max_papers", 12)])
    others = take(sorted((e for e in entries if e["source"] == "feed" and e["key"] not in used
                          and e.get("extra", {}).get("kind") != "official"),
                         key=lambda e: e["published"] or NOW, reverse=True)[:15])
    repos = radar.get("items", [])[:limit]

    ok = [s for s in statuses if s["ok"]]
    failed = [s["name"] for s in statuses if not s["ok"]]
    out = [f"# AI 日报素材 · {TODAY}", "",
           f"> 生成于 {NOW.astimezone(BEIJING):%Y-%m-%d %H:%M}（北京时间）。{len(ok)}/{len(statuses)} 个来源抓取成功"
           + (f"，失败：{'、'.join(failed)}" if failed else "") + "。"
           f"本次候选：热议话题 {len(clusters)} 个、高热度单条讨论 {len(singles)} 条、"
           f"新东西 {len(official) + len(models) + len(repos) + len(show_hn)} 条、论文 {len(papers)} 篇。", ""]
    if guide := read_guide():
        out += [guide, "", "---", ""]

    out += ["# 今日素材", "", "## 素材一：大家都在讨论的", "",
            "### 多个来源同时提到的话题", "",
            "按「出现在几个不同来源」排序，来源越多说明讨论越广。关键词是程序自动找的，可能把不相关的内容归到一起，请自己判断。", ""]
    if not clusters:
        out += ["今天没有多个来源同时提到的话题。", ""]
    for i, c in enumerate(clusters, 1):
        out += [f"#### {i}. 关键词：{' / '.join(c['terms'][:3])} — {len(c['sources'])} 个来源：{'、'.join(c['sources'])}", ""]
        for e in sorted(c["entries"].values(), key=heat, reverse=True)[:6]:
            out += fmt_entry(e, 200)
        out += [""]
    out += ["### 只在一个地方出现、但很热的讨论（Hacker News，按分数排序）", ""]
    for e in singles:
        out += fmt_entry(e, 200)
    out += ["", "## 素材二：新东西", "", "### 官方发布", ""]
    for e in official or []:
        out += fmt_entry(e)
    if not official:
        out += ["今天没有。"]
    out += ["", "### 新上线的模型（OpenRouter）", ""]
    for e in models:
        out += fmt_model(e)
    if not models:
        out += ["今天没有。"]
    out += ["", f"### 开源项目和 Skill（GitHub 项目雷达 {radar.get('date', '')}，已按涨星速度等打过分）", ""]
    for r in repos:
        out += fmt_repo(r)
    if not repos:
        out += ["今天没有。"]
    out += ["", "### 新工具（Show HN：作者自己发出来的新项目）", ""]
    for e in show_hn:
        out += fmt_entry(e, 200)
    if not show_hn:
        out += ["今天没有。"]
    out += ["", "## 素材三：论文（HF 每日论文，社区投票精选，按点赞数排序）", ""]
    for e in papers:
        out += fmt_entry(e, 500)
    if not papers:
        out += ["今天没有。"]
    out += ["", "## 附：博客和 Newsletter 的其他新文章", ""]
    for e in others:
        out += fmt_entry(e, 150)
    if not others:
        out += ["今天没有。"]
    return "\n".join(out) + "\n", used


# ---------------------------------------------------------------- Gemini 检查（--check）
# 流程本身不调用任何付费模型。Gemini 只用来看油管视频，目前账号被 Google 限制，先保留检查，解封了马上能知道

def pick_gemini_model(names):
    """没指定模型时，挑版本最新的正式版 Flash-Lite（免费额度最宽松）。"""
    def version(n):
        m = re.match(r"gemini-(\d+(?:\.\d+)?)", n)
        return float(m.group(1)) if m else 0.0
    skip = ("preview", "exp", "tts", "image", "audio", "live", "latest")
    cands = [n for n in names if "flash-lite" in n and not any(s in n for s in skip)]
    cands = cands or [n for n in names if "flash" in n and not any(s in n for s in skip)]
    return max(cands, key=version) if cands else None


def gemini_generate(key, model, parts):
    out = post_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                    {"contents": [{"parts": parts}]}, {"x-goog-api-key": key})
    return "".join(p.get("text", "") for p in out["candidates"][0]["content"]["parts"]).strip()


def check_gemini():
    """返回 [(检查项, 结果)]：Key 本身，以及能不能直接看油管视频。"""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        return [("Gemini", "⏳ 还没配置（仓库 Secrets 里添加 GEMINI_API_KEY）")]
    try:
        models = get_json("https://generativelanguage.googleapis.com/v1beta/models?pageSize=1000",
                          headers={"x-goog-api-key": key}, retries=0).get("models", [])
    except NETWORK_ERRORS as e:
        return [("Gemini", f"❌ Key 不能用：{describe_error(e)}")]
    names = [m["name"].removeprefix("models/") for m in models
             if "generateContent" in m.get("supportedGenerationMethods", [])]
    print("[Gemini] 这个 Key 能用的模型：" + ", ".join(names))
    model = os.environ.get("GEMINI_MODEL") or pick_gemini_model(names)
    if not model:
        return [("Gemini", "⚠️ Key 有效，但没找到 Flash 系列模型")]
    rows = []
    try:
        gemini_generate(key, model, [{"text": "只回复：好"}])
        rows.append(("Gemini", f"✅ 可用，已成功调用 {model}"))
    except NETWORK_ERRORS as e:
        return [("Gemini", f"⚠️ Key 有效，但调用 {model} 失败：{describe_error(e)}")]
    # 用油管第一个视频（19 秒）测试 Gemini 能不能直接看油管链接
    try:
        reply = gemini_generate(key, model, [
            {"file_data": {"file_uri": "https://www.youtube.com/watch?v=jNQXAC9IVRw"}},
            {"text": "用一句中文描述这个视频的内容。"},
        ])
        rows.append(("Gemini 看油管视频", f"✅ 可以。测试视频的描述：{clean_text(reply, 80)}"))
    except NETWORK_ERRORS as e:
        rows.append(("Gemini 看油管视频", f"❌ {describe_error(e)}"))
    return rows


def cell(s, limit=60):
    s = clean_text(str(s or ""), limit)
    return s.replace("|", "／") or "—"


def render_check(statuses, key_rows):
    lines = [f"# AI 资讯雷达 · 接入检查（{NOW:%Y-%m-%d %H:%M} UTC）", "",
             "## 数据来源", "",
             "| 来源 | 状态 | 最近新内容 | 最新一条 | 备注 |", "|---|---|---|---|---|"]
    for s in statuses:
        if not s["ok"]:
            lines.append(f"| {s['name']} | ❌ 失败 | — | — | {cell(s['error'], 120)} |")
            continue
        latest = s.get("latest") or {}
        newest = f"{latest.get('date', '')} {cell(latest.get('title'), 50)}" if latest else "—"
        window = "本次" if s["window_hours"] is None else f"{s['window_hours']} 小时内"
        state = "✅ 正常" if s["recent"] else ("⚠️ 能连上，但这段时间没有新内容" if s["total"] else "⚠️ 能连上，但一条都没有")
        lines.append(f"| {s['name']} | {state} | {window} {s['recent']} 条 | {newest} | {cell(s.get('note'), 120)} |")
    ok = sum(1 for s in statuses if s["ok"])
    lines += ["", f"共 {len(statuses)} 个来源：{ok} 个能用，{len(statuses) - ok} 个失败。", ""]
    lines += ["## Gemini（看油管视频用，可选）", "", "| 检查项 | 结果 |", "|---|---|"]
    lines += [f"| {name} | {cell(result, 300)} |" for name, result in key_rows]
    lines += ["", "<sub>✅ 正常；⚠️ 能连上但最近没新内容（博客更新慢是正常的）；❌ 连不上，需要换地址或换方法。"
              "检查 Gemini 时发了一句很短的测试，用的是免费额度。</sub>", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description="AI 资讯雷达：生成每天给 GPT 读的日报素材")
    ap.add_argument("--config", default=str(ROOT / "ai_news.toml"))
    ap.add_argument("--check", action="store_true", help="只检查每个来源能不能用，不写文件")
    ap.add_argument("--dry-run", action="store_true", help="只打印素材，不写文件")
    args = ap.parse_args()

    with open(args.config, "rb") as f:
        cfg = tomllib.load(f)
    cache_path = DATA / "youtube_channels.json"
    cache = json.loads(cache_path.read_text()) if cache_path.exists() else {}

    items, statuses = [], []
    for name, fn, since in build_jobs(cfg, cache):
        got, status = run_source(name, fn, since)
        items += got
        statuses.append(status)

    if args.check:
        report = render_check(statuses, check_gemini())
        print("\n" + report)
        if summary := os.environ.get("GITHUB_STEP_SUMMARY"):  # 显示在 GitHub Actions 运行页面上
            with open(summary, "a", encoding="utf-8") as f:
                f.write(report)
        return

    radar_path = ROOT / "data" / "radar_latest.json"
    radar = json.loads(radar_path.read_text(encoding="utf-8")) if radar_path.exists() else {}
    seen_path = DATA / "seen.json"
    seen = json.loads(seen_path.read_text(encoding="utf-8")) if seen_path.exists() else {}
    digest, used = build_digest(cfg, items, statuses, radar, seen)
    if args.dry_run:
        print(digest)
        print(f"[素材] {len(digest):,} 字", file=sys.stderr)
        return

    reports = ROOT / "reports" / "ai-news"
    reports.mkdir(parents=True, exist_ok=True)
    (reports / f"{TODAY}.md").write_text(digest, encoding="utf-8")
    (reports / "latest.md").write_text(digest, encoding="utf-8")
    for key in used:
        seen.setdefault(key, TODAY.isoformat())
    keep_after = (TODAY - timedelta(days=30)).isoformat()
    DATA.mkdir(parents=True, exist_ok=True)
    seen_path.write_text(json.dumps({k: v for k, v in sorted(seen.items()) if v >= keep_after},
                                    ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")

    raw = DATA / "raw" / f"{TODAY}.json"  # 原始数据只留在本地排查用，不提交（见 .gitignore）
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(json.dumps({"fetched_at": NOW.isoformat(), "sources": statuses, "items": items},
                              ensure_ascii=False, indent=1, default=lambda o: o.isoformat()) + "\n", encoding="utf-8")
    ok = sum(1 for s in statuses if s["ok"])
    print(f"[完成] {ok}/{len(statuses)} 个来源成功，抓到 {len(items)} 条，素材 {len(digest):,} 字："
          f"{(reports / 'latest.md').relative_to(ROOT)}")

if __name__ == "__main__":
    main()
