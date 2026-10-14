#!/usr/bin/env python3
"""AI 资讯雷达 · 接入层：从各个免费来源抓取最新的 AI 内容，整理成统一格式。

目前只做「接入」这一步。后面的去重筛选、Gemini 初筛、GPT 判断和日报，都建立在这份数据上。
来源在 ai_news.toml 里配置。只依赖 Python 3.11+ 标准库，不需要 pip install。

用法：
    python ai_news.py            # 抓取所有来源，存到 data/news/raw/日期.json
    python ai_news.py --check    # 检查每个来源和 API Key 能不能用，不写文件
"""

from __future__ import annotations

import argparse
import email.utils
import gzip
import html
import json
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
TODAY = NOW.date()

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
    data = get_json("https://huggingface.co/api/daily_papers?limit=100")
    items = []
    for d in data:
        p = d.get("paper") or {}
        pid = p.get("id") or d.get("id")
        if not pid:
            continue
        items.append(make_item(
            "hf_papers", f"arxiv:{pid}", d.get("title") or p.get("title"), f"https://huggingface.co/papers/{pid}",
            parse_time(d.get("publishedAt") or p.get("publishedAt")), p.get("summary") or d.get("summary"),
            {"upvotes": p.get("upvotes", 0), "comments": d.get("numComments", 0)},
            arxiv=f"https://arxiv.org/abs/{pid}", github=p.get("githubRepo")))
    return items, ""


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
    return items, f"另有 {updates} 篇是旧论文的新版本，已跳过" if updates else ""


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
                           feed=feed["name"], author=e["author"])
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
        jobs.append(("HF 每日论文", lambda c=c: fetch_hf_papers(c, since), since))
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


# ---------------------------------------------------------------- API Key 检查（--check）

def check_openai():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        return "⏳ 还没配置（仓库 Secrets 里添加 OPENAI_API_KEY）"
    base = (os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("OPENAI_MODEL") or "gpt-4o-mini"
    auth = {"Authorization": f"Bearer {key}"}
    try:
        ids = sorted(m.get("id", "") for m in get_json(f"{base}/models", headers=auth, retries=0).get("data", []))
        print("[OpenAI] 这个 Key 能用的 GPT 模型：" + (", ".join(i for i in ids if i.startswith("gpt")) or "（无）"))
    except NETWORK_ERRORS as e:
        return f"❌ Key 不能用：{describe_error(e)}"
    # 查模型列表不要钱，但看不出有没有充值，所以再发一句很短的话试试（不到 0.001 美分）
    try:
        post_json(f"{base}/chat/completions", {"model": model, "messages": [{"role": "user", "content": "只回复：好"}]}, auth)
    except NETWORK_ERRORS as e:
        return f"⚠️ Key 有效，但调用 {model} 失败：{describe_error(e)}（如果提示额度不足，需要先在 OpenAI 后台充值）"
    return f"✅ 可用，已成功调用 {model}"


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
        window = "当天这批" if s["window_hours"] is None else f"{s['window_hours']} 小时内"
        state = "✅ 正常" if s["recent"] else ("⚠️ 能连上，但这段时间没有新内容" if s["total"] else "⚠️ 能连上，但一条都没有")
        lines.append(f"| {s['name']} | {state} | {window} {s['recent']} 条 | {newest} | {cell(s.get('note'), 120)} |")
    ok = sum(1 for s in statuses if s["ok"])
    lines += ["", f"共 {len(statuses)} 个来源：{ok} 个能用，{len(statuses) - ok} 个失败。", ""]
    lines += ["## API Key", "", "| 检查项 | 结果 |", "|---|---|"]
    lines += [f"| {name} | {cell(result, 300)} |" for name, result in key_rows]
    lines += ["", "<sub>✅ 正常；⚠️ 能连上但最近没新内容（博客更新慢是正常的）；❌ 连不上，需要换地址或换方法。"
              "检查 Key 时各发了一句很短的测试，费用不到 0.001 美分。</sub>", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser(description="AI 资讯雷达 · 接入层")
    ap.add_argument("--config", default=str(ROOT / "ai_news.toml"))
    ap.add_argument("--check", action="store_true", help="只检查每个来源和 API Key 能不能用，不写文件")
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
        report = render_check(statuses, [("OpenAI", check_openai()), *check_gemini()])
        print("\n" + report)
        if summary := os.environ.get("GITHUB_STEP_SUMMARY"):  # 显示在 GitHub Actions 运行页面上
            with open(summary, "a", encoding="utf-8") as f:
                f.write(report)
        return

    out = DATA / "raw" / f"{TODAY}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {"fetched_at": NOW.isoformat(), "sources": statuses, "items": items}
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1, default=lambda o: o.isoformat()) + "\n",
                   encoding="utf-8")
    cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    ok = sum(1 for s in statuses if s["ok"])
    print(f"[完成] {ok}/{len(statuses)} 个来源成功，共 {len(items)} 条，存到 {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
