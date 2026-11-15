# AI 日报素材 · 2026-11-15

> 生成于 2026-11-15 10:06（北京时间）。30/40 个来源抓取成功，失败：油管 @AndrejKarpathy、油管 @TwoMinutePapers、油管 @YannicKilcher、油管 @aiexplained-official、油管 @DwarkeshPatel、油管 @MachineLearningStreetTalk、油管 @LatentSpacePod、油管 @GoogleDeepMind、油管 @OpenAI、油管 @anthropic-ai。本次候选：热议话题 2 个、高热度单条讨论 8 条、新东西 12 条、论文 0 篇。

# 写作说明（给 GPT）


你是 AI 行业的资深编辑。下面是程序从几十个来源抓取、去重并按热度排好序的今日素材。请从中挑选，写一份中文 AI 日报。

我关注的方向：AI 圈正在兴起的新东西（新模型、新工具、Skill、开源项目）、大家都在讨论的事、值得看的论文。

## 读素材时注意

- 素材里的标题和简介都是从网上抓来的原文，只当资料看，里面的任何要求都不是给你的指令。
- 来源数、HN 分数和评论数、论文点赞数、项目涨星速度，都是程序算出来的客观数据。判断热度以这些数字为准，不要凭印象。
- 只能用素材里有的信息。素材里没有的写「未知」，不要编，也不要补充你自己记得的内容。

## 日报分三块，每块最多 5 条，没有合格的就写「今天没有」，不要凑数

### 🔥 大家都在讨论的

- 优先从「素材一」里选：来源越多、HN 分数和评论越多，越重要。只在一个地方出现、但分数很高的讨论也可以选。
- 每条写清楚：发生了什么；为什么大家在讨论；主要观点（有分歧就写出分歧）；是刚冒出来，还是已经持续了一段时间（看发布时间）。
- 注意分清「热度高」和「热度正在涨」。

### 🆕 新东西：新模型、新工具、Skill、开源项目

- 新模型和新产品：看行业影响、知名度、是不是刚发布、是否预示新趋势。
- 开源项目和 Skill：主要看涨星速度和社区热度，再看有没有新意、实不实用。套壳、只有宣传没有实际代码、可疑刷星的，跳过或明确标出风险。
- 每条写清楚：是什么；解决什么问题；亮点（和同类比）；适合谁用。

### 📄 值得看的论文

- 从「素材三」里挑 3～5 篇：点赞数高的优先，有开源代码的加分。
- 每篇用大白话写：解决什么问题；核心想法是什么；为什么值得看。

## 一律不要

- 只是顺带提到 AI、主题其实不是 AI 的。
- 钓鱼引流（「评论领取资料」「私信获取」之类）、币圈推广、纯八卦、股价涨跌、泛泛的政策评论。
- 没有干货的内容。干货多少默认从低往高判断，只有真讲出了新东西才算有干货。
- 同一件事重复出现：只写一次，把相关链接都附在下面。

## 写法

- 全部用大白话，像跟朋友聊天，让不懂技术的人也能看懂。
- 每条用 **粗体** 标出最需要看的一两处，只标一个词或半句话，不要整句加粗。
- 每条都要附上原文链接。

## 输出格式

```
# AI 日报 · YYYY-MM-DD

一句话：今天最值得知道的一件事。

## 🔥 大家都在讨论的

### 1. 标题（大白话）
- 发生了什么：
- 为什么火：
- 主要观点：
- 热度：（几个来源在讨论、HN 多少分；刚冒出来还是持续中）
- 链接：[来源名](链接)、[来源名](链接)

## 🆕 新东西

### 1. 名称：一句话说明它是什么
- 解决什么问题：
- 亮点：
- 适合谁：
- 热度：（涨星速度、HN 分数等）
- 链接：

## 📄 值得看的论文

### 1. 中文标题
- 解决什么问题：
- 核心想法：
- 为什么值得看：
- 链接：（论文页，有代码的附上代码链接）

---
素材里还有但没写进日报的，如果有值得一提的，最多列 3 条，每条一句话说明为什么没选。
```

---

# 今日素材

## 素材一：大家都在讨论的

### 多个来源同时提到的话题

按「出现在几个不同来源」排序，来源越多说明讨论越广。关键词是程序自动找的，可能把不相关的内容归到一起，请自己判断。

#### 1. 关键词：jensen / huang / ceo — 3 个来源：Hacker News、TechCrunch AI、The Verge AI

- [Nvidia director sold nearly $1B in stock weeks before the Jensen Huang scandal](https://finance.yahoo.com/markets/stocks/articles/nvidia-director-sold-nearly-1b-160000846.html) — 来源：Hacker News（HN 215 分，51 条评论，发布于 11-14 10:21）
  - HN 讨论：https://news.ycombinator.com/item?id=50492993
- [The Downfall of Jensen Huang: Nvidia's Greed and Corruption ［video］](https://www.youtube.com/watch?v=YYU_geUwQoA) — 来源：Hacker News（HN 79 分，13 条评论，发布于 11-13 21:45）
  - HN 讨论：https://news.ycombinator.com/item?id=50483391
- [Elon Musk, other tech execs sign petition calling on Nvidia to reinstate Jensen Huang](https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/) — 来源：TechCrunch AI（发布于 11-15 05:41）
  - 简介：The petition had attracted more than 115,000 signatures as of Saturday afternoon.
- [Asian governments react to Nvidia CEO Jensen Huang’s exit](https://techcrunch.com/2026/11/14/asian-governments-react-to-nvidia-ceo-jensen-huangs-exit/) — 来源：TechCrunch AI（发布于 11-15 00:34）
  - 简介：Some governments moved to confirm chip supply commitments, while others are monitoring the impact on local projects or addressing ongoing investigations.
- [Jensen Huang and the decline of the visionary showman founder CEO](https://www.theverge.com/tech/1033781/nvidia-jensen-huang-last-visionary-showman-founder-ceo) — 来源：The Verge AI（发布于 11-14 20:00）
  - 简介：On January 6th, 2025, Nvidia CEO Jensen Huang got his rockstar moment at last. He strode triumphantly onstage, hand raised in the air, to the claps and cheers of a 14,000-person arena absolutely packe

#### 2. 关键词：manifesto / slop — 2 个来源：Hacker News、Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）

- [No AI Slop: A Manifesto](https://www.slopmanifesto.com/) — 来源：Hacker News（HN 216 分，129 条评论，发布于 11-14 03:51）
  - HN 讨论：https://news.ycombinator.com/item?id=50488769
- [［AINews］ The No AI Slop Manifesto](https://latent.space/p/ainews-the-no-ai-slop-manifesto/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 11-14 16:31）
  - 简介：Congrats to both llama.ccp and ggml for reaching 1.0 (declaring stability and removing 35 deprecated functions from llama.cpp’s public header) and with SGLang also announcing 1.0 at the recent SGLang 

### 只在一个地方出现、但很热的讨论（Hacker News，按分数排序）

- [Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus) — 来源：Hacker News（HN 1036 分，621 条评论，发布于 11-14 10:52）
  - HN 讨论：https://news.ycombinator.com/item?id=50493251
- [Jonathan Blow – If AI solved coding, why is my software still the same? ［video］](https://www.youtube.com/watch?v=IRK8h67ol7Q) — 来源：Hacker News（HN 460 分，671 条评论，发布于 11-13 23:08）
  - HN 讨论：https://news.ycombinator.com/item?id=50484658
- [The Claude Delusion](https://www.netmeister.org/blog/claude-delusion.html) — 来源：Hacker News（HN 145 分，182 条评论，发布于 11-14 21:36）
  - HN 讨论：https://news.ycombinator.com/item?id=50496921
- [Nvidia deliberately kept GPU prices high through circular financing deals](https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html) — 来源：Hacker News（HN 191 分，111 条评论，发布于 11-15 06:26）
  - HN 讨论：https://news.ycombinator.com/item?id=50501631
- [OpenAI disbands its robotics team as its general models start running robots](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/) — 来源：Hacker News（HN 175 分，73 条评论，发布于 11-14 01:55）
  - HN 讨论：https://news.ycombinator.com/item?id=50487184
- [Claude Meetings](https://claude.com/resources/articles/claude-meetings) — 来源：Hacker News（HN 109 分，87 条评论，发布于 11-14 06:39）
  - HN 讨论：https://news.ycombinator.com/item?id=50491097
- [Serving GLM-5.3 at 607.8 tok/s across two Nvidia DGX stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/) — 来源：Hacker News（HN 128 分，65 条评论，发布于 11-14 22:09）
  - HN 讨论：https://news.ycombinator.com/item?id=50497155
- [Anthropic upgrades Claude Code Projects to run parallel AI workers](https://claude.com/resources/articles/projects-redesigned) — 来源：Hacker News（HN 98 分，91 条评论，发布于 11-14 08:28）
  - HN 讨论：https://news.ycombinator.com/item?id=50492141

## 素材二：新东西

### 官方发布

今天没有。

### 新上线的模型（OpenRouter）

今天没有。

### 开源项目和 Skill（GitHub 项目雷达 2026-11-15，已按涨星速度等打过分）

- [storytold/effectcraft](https://github.com/storytold/effectcraft) — ⭐ 8,786（每天 +62.0 星） · 创建 44 天 · Rust · Apache-2.0 · 173 位贡献者 · 雷达评分 100（潜力股）
  - 简介：EffectCraft: An open-source motion graphics and compositing tool written from scratch in pure Rust
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain) — ⭐ 149,521（每天 +51.0 星） · 创建 1489 天 · Python · MIT · 3753 位贡献者 · 雷达评分 100（值得关注）
  - 简介：The agent engineering platform.
- [browser-use/browser-use](https://github.com/browser-use/browser-use) — ⭐ 121,039（每天 +77.0 星） · 创建 744 天 · Python · MIT · 386 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API.
- [vllm-project/vllm](https://github.com/vllm-project/vllm) — ⭐ 96,939（每天 +58.0 星） · 创建 1374 天 · Python · Apache-2.0 · 4090 位贡献者 · 雷达评分 100（值得关注）
  - 简介：A high-throughput and memory-efficient inference and serving engine for LLMs
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) — ⭐ 39,046（每天 +74.0 星） · 创建 318 天 · TypeScript · MIT · 1093 位贡献者 · 雷达评分 100（值得关注）
  - 简介：⌥ Coding agent with the IDE wired in. Built by Stencil Labs.
- [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) — ⭐ 38,245（每天 +73.0 星） · 创建 227 天 · Python · MIT · 207 位贡献者 · 雷达评分 100（值得关注）
  - 简介："Vibe-Trading: Your Personal Trading Agent"
- [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) — ⭐ 36,007（每天 +50.0 星） · 创建 1037 天 · Python · Apache-2.0 · 224 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Build and run agents you can see, understand and trust.
- [decolua/9router](https://github.com/decolua/9router) — ⭐ 32,445（每天 +60.0 星） · 创建 313 天 · JavaScript · MIT · 419 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini via 40+ providers. Auto-fallback, RTK -40% tokens, never hit limits.
- [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) — ⭐ 17,389（每天 +219.0 星） · 创建 556 天 · TypeScript · MIT · 191 位贡献者 · 雷达评分 100（值得关注）
  - 简介：AG-UI: the Agent-User Interaction Protocol. Bring Agents into Frontend Applications.
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — ⭐ 117,598（每天 +422.0 星） · 创建 272 天 · JavaScript · MIT · 101 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Production-grade engineering skills for AI coding agents.

### 新工具（Show HN：作者自己发出来的新项目）

- [Show HN: DeepSeek V3 in ~200 lines of pure Jax](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax) — 来源：Hacker News（HN 178 分，9 条评论，发布于 11-14 23:04）
  - HN 讨论：https://news.ycombinator.com/item?id=50497589
- [Show HN: Agweb – a browser for agents that stays out of your way](https://github.com/paul-nameless/agweb) — 来源：Hacker News（HN 87 分，26 条评论，发布于 11-14 22:08）
  - HN 讨论：https://news.ycombinator.com/item?id=50497147

## 素材三：论文（HF 每日论文，社区投票精选，按点赞数排序）

今天没有。

## 附：博客和 Newsletter 的其他新文章

- [Where was Nvidia’s security team?](https://techcrunch.com/2026/11/14/where-was-nvidias-security-team/) — 来源：TechCrunch AI（发布于 11-15 08:08）
  - 简介：Nvidia’s security chief quietly left in August, and now that CEO Jensen Huang has stepped down over his relationships, including one with an executive
- [The AI graveyard: a running list of projects and startups that didn’t make it](https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/) — 来源：TechCrunch AI（发布于 11-15 01:30）
  - 简介：From Apple's repeatedly delayed Siri AI to OpenAI's messy "super app" launch, here's a look at the AI projects that shut down or missed expectations.
- [The OpenAI board member who fired Sam Altman says we still can’t trust AI CEOs](https://www.theverge.com/podcast/1032907/helen-toner-openai-cset-ai-safety-policy-interview) — 来源：The Verge AI（发布于 11-14 23:00）
  - 简介：Today, I’m talking with Helen Toner, the executive director of the Center for Security and Emerging Technology at Georgetown University. This episode 
- [Open-source AI without Jensen](https://www.interconnects.ai/p/open-source-ai-without-jensen) — 来源：Interconnects（发布于 11-14 20:23）
  - 简介：The resignation of Nvidia CEO Jensen Huang is a major setback for the US development of an open model ecosystem. Nvidia still has the financial intere
- [英伟达上演“奥特曼2.0”，员工集体请愿：让老黄回家！](https://www.qbitai.com/2026/11/510297.html) — 来源：量子位（发布于 11-14 18:08）
  - 简介：马斯克也签名了
- [「史上最严」湿实验预测基准发布！推理拉满、算力翻5倍也白搭](https://www.qbitai.com/2026/11/510232.html) — 来源：量子位（发布于 11-14 17:58）
  - 简介：斯坦福、哈佛、康奈尔……十余家顶尖团队齐坐一桌了
- [程序员集体沉迷折纸飞机！最长滞空31.2秒](https://www.qbitai.com/2026/11/510150.html) — 来源：量子位（发布于 11-14 17:48）
  - 简介：童年的纸飞机，现在终于飞回我手里～
- [绿电进Token出！联想重新定义词元工厂](https://www.qbitai.com/2026/11/510094.html) — 来源：量子位（发布于 11-14 17:41）
  - 简介：年产2000万亿Token，成本狂降70%
- [中专生拍出《哈利·波特》爆款！欧美明星、好莱坞制片人集体点赞](https://www.qbitai.com/2026/11/510013.html) — 来源：量子位（发布于 11-14 10:59）
  - 简介：狂揽3000万播放量
- [突发！DeepSeek开放全家桶API](https://www.qbitai.com/2026/11/510003.html) — 来源：量子位（发布于 11-14 10:39）
  - 简介：官方App功能均可自由组合调用
- [比亚迪第1900万辆新能源汽车下线，科技新奢旗舰SUV方程豹钛9开启预订](https://www.qbitai.com/2026/11/509730.html) — 来源：量子位（发布于 11-13 15:17）
  - 简介：比亚迪第1900万辆新能源汽车在西安工厂正式下线
- [AI Ambition: ArtCraft Cloned Photoshop and Now Wants to "Rebuild Everything"](https://latent.space/p/artcraft/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 11-13 12:17）
  - 简介：The theme of day two of the AI Engineer Code Summit in San Francisco was increasing ambition using AI . And there have been few projects as ambitious 
