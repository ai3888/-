// 在 x.com 的页面里执行这段代码（列表、账号主页、搜索结果都行），返回这个页面上最近的帖子（JSON 文字）。
// 给 DeepSeek 用：用 ego 浏览器打开页面后，在页面里执行整段代码，把返回的文字原样存成文件。详见 x_task.md。
// 代码会自己往下翻几屏，只读页面，不点任何按钮。点赞、转发、回复、浏览数取自按钮的无障碍标签，界面是中文还是英文都能认。
(async () => {
  const HOURS = 30;                // 只要最近多少小时内发的帖子（每天跑一次，多留几个小时余量）
  const MAX_SCROLLS_LIST = 15;     // 列表里账号多、帖子多，多翻几屏
  const MAX_SCROLLS_OTHER = 3;     // 账号主页和搜索结果

  const cutoff = Date.now() - HOURS * 3600 * 1000;
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const articles = () => document.querySelectorAll('article[data-testid="tweet"]');
  const loggedIn = () => !!document.querySelector(
    '[data-testid="SideNav_AccountSwitcher_Button"], [data-testid="AppTabBar_Profile_Link"]');

  // "1234 Likes. Like"、"1,234 次查看"、"1.2万" 这类文字里取出数字
  const num = (s) => {
    const m = String(s || '').match(/(\d[\d,，]*(?:\.\d+)?)\s*(万|亿|[KMB](?![a-z]))?/i);
    if (!m) return 0;
    const unit = { '万': 1e4, '亿': 1e8, k: 1e3, m: 1e6, b: 1e9 }[(m[2] || '').toLowerCase()] || 1;
    return Math.round(parseFloat(m[1].replace(/[,，]/g, '')) * unit);
  };
  const clip = (s, n) => (s || '').replace(/\s+/g, ' ').trim().slice(0, n);

  const parse = (art) => {
    const time = art.querySelector('time[datetime]');
    const link = time && time.closest('a[href*="/status/"]');  // 广告没有发布时间，会在这里被跳过
    const m = link && (link.getAttribute('href') || '').match(/^\/([^/?#]+)\/status\/(\d+)/);
    if (!m) return null;
    let text = '', quoted = '', textEl = null;
    for (const t of art.querySelectorAll('[data-testid="tweetText"]')) {
      const box = t.closest('div[role="link"]');            // 引用的帖子包在一个可点击的框里
      if (box && art.contains(box)) quoted = quoted || t.innerText;
      else if (!textEl) { textEl = t; text = t.innerText; }
    }
    const label = (sel) => (art.querySelector(sel) || { getAttribute: () => '' }).getAttribute('aria-label');
    const links = textEl ? [...textEl.querySelectorAll('a[href^="http"]')].map((a) => clip(a.innerText, 120)) : [];
    const nameBox = art.querySelector('[data-testid="User-Name"]');
    const context = art.querySelector('[data-testid="socialContext"]');
    const card = art.querySelector('[data-testid="card.wrapper"]');
    return {
      id: m[2],
      url: `https://x.com/${m[1]}/status/${m[2]}`,
      author: m[1],
      name: nameBox ? clip(nameBox.innerText.split('\n')[0], 80) : '',
      time: time.getAttribute('datetime'),
      text: (text || '').trim().slice(0, 1500),
      likes: num(label('[data-testid="like"], [data-testid="unlike"]')),
      reposts: num(label('[data-testid="retweet"], [data-testid="unretweet"]')),
      replies: num(label('[data-testid="reply"]')),
      views: num(label('a[href$="/analytics"]')),
      context: context ? clip(context.innerText, 80) : '',   // 比如「某某 转帖了」「已置顶」
      quoted: clip(quoted, 500),
      card: card ? clip(card.innerText, 200) : '',
      links: links.filter(Boolean),
    };
  };

  // 等帖子加载出来（最多 15 秒）
  for (let i = 0; i < 30 && !articles().length; i++) await sleep(500);

  const maxScrolls = location.pathname.includes('/lists/') ? MAX_SCROLLS_LIST : MAX_SCROLLS_OTHER;
  const seen = new Map();
  for (let i = 0; ; i++) {
    let fresh = 0;
    for (const art of articles()) {
      const p = parse(art);
      if (!p || seen.has(p.id)) continue;
      seen.set(p.id, p);
      if (Date.parse(p.time) >= cutoff) fresh++;
    }
    // 这一屏没有新的近期帖子，再往下只会更旧（第一屏可能只有置顶的旧帖，所以至少翻一次）
    if (i >= maxScrolls || (fresh === 0 && (i > 0 || seen.size >= 5))) break;
    const before = articles().length && articles()[articles().length - 1];
    window.scrollBy(0, window.innerHeight * 2);
    for (let j = 0; j < 10; j++) {                            // 等新帖子加载（最多 5 秒）
      await sleep(500);
      const all = articles();
      if (all.length && all[all.length - 1] !== before) break;
    }
  }

  const posts = [...seen.values()].filter((p) => Date.parse(p.time) >= cutoff);
  return JSON.stringify({
    page: location.href,
    collected_at: new Date().toISOString(),
    logged_in: loggedIn(),
    hours: HOURS,
    found_on_page: seen.size,
    posts,
  }, null, 1);
})();
