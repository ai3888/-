# AI 日报素材 · 2026-11-07

> 生成于 2026-11-07 10:20（北京时间）。30/40 个来源抓取成功，失败：油管 @AndrejKarpathy、油管 @TwoMinutePapers、油管 @YannicKilcher、油管 @aiexplained-official、油管 @DwarkeshPatel、油管 @MachineLearningStreetTalk、油管 @LatentSpacePod、油管 @GoogleDeepMind、油管 @OpenAI、油管 @anthropic-ai。本次候选：热议话题 4 个、高热度单条讨论 8 条、新东西 17 条、论文 12 篇。

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

#### 1. 关键词：anthropic / ipo / valuation — 3 个来源：Hacker News、TechCrunch AI、The Verge AI

- [Anthropic IPO buyers see valuation as low as $1.1T](https://www.bloomberg.com/news/articles/2026-11-06/anthropic-ipo-valuation-expectations-pressured-after-ai-rout) — 来源：Hacker News（HN 235 分，493 条评论，发布于 11-07 00:54）
  - HN 讨论：https://news.ycombinator.com/item?id=50394906
  - 简介：https://epyhia.com/anthropic-ipo-valuation-talks-drop-to-1-3...
- [Major Investors Are Skeptical Anthropic IPO Can Achieve $1.5T Valuation](https://www.wsj.com/finance/major-investors-are-skeptical-anthropic-ipo-can-achieve-1-5-trillion-valuation-ca965d8b’) — 来源：Hacker News（HN 90 分，106 条评论，发布于 11-06 08:31）
  - HN 讨论：https://news.ycombinator.com/item?id=50386597
- [Anthropic IPO valuation talks drop to $1.3T](https://epyhia.com/anthropic-ipo-valuation-talks-drop-to-1-3-trillion-as-major-investors) — 来源：Hacker News（HN 93 分，1 条评论，发布于 11-07 01:21）
  - HN 讨论：https://news.ycombinator.com/item?id=50395318
- [OpenAI reportedly raises an additional $11 billion at a $1.25 trillion valuation](https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/) — 来源：TechCrunch AI（发布于 11-07 06:53）
  - 简介：OpenAI has reportedly raised an additional $11 billion as part of a funding round that hasn't closed yet but is expected to in the coming weeks.
- [Ramp data shows AI spending stalling just as Anthropic nears its IPO](https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/) — 来源：TechCrunch AI（发布于 11-06 23:54）
  - 简介：AI usage keeps climbing, but spending has stalled. Price cuts and smarter cost controls among the biggest spenders could challenge investor assumptions about AI hypergrowth.
- [OpenAI valued at $1.25 trillion, as rival Anthropic nears its IPO](https://www.theverge.com/ai-artificial-intelligence/1029380/openai-1-25-trillion-investment-valuation) — 来源：The Verge AI（发布于 11-07 07:46）
  - 简介：OpenAI is now valued at $1.25 trillion in a new round of funding that has raised another $11 billion, according to Bloomberg. That would make it one of the world's most valuable companies, not long af

#### 2. 关键词：The components of agent memory — 2 个来源：Anthropic 工程博客、Anthropic 研究

- [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) — 来源：Anthropic 工程博客、Anthropic 研究（发布于 11-06 08:00）
  - 简介：For Claude to learn from experience, it has to decide what’s worth remembering before it knows what’s next. Here’s how “dreaming” helps it organize memory and correct mistakes.

#### 3. 关键词：spaces / meta / muse — 2 个来源：TechCrunch AI、The Verge AI

- [Meta introduces Spaces, a new way to collaborate with your Muse agent](https://techcrunch.com/2026/11/06/meta-introduces-spaces-a-new-way-to-collaborate-with-your-muse-agent/) — 来源：TechCrunch AI（发布于 11-07 02:44）
  - 简介：Meta's Muse agents continue to get new features and integrations. Spaces promises to be a new way to interact with the AI helpers.
- [Meta’s Muse AI can create custom ‘spaces’ for the version of the app you need right now](https://www.theverge.com/tech/1028871/meta-muse-ai-spaces) — 来源：The Verge AI（发布于 11-07 02:10）
  - 简介：Meta will now allow you to build customized, app-like experiences within Muse. The new feature, called "spaces," allows its AI assistant to build things like a shopping hub, school dashboard, music tr

#### 4. 关键词：amazon / alexa / text — 2 个来源：TechCrunch AI、The Verge AI

- [After blocking Muse, Amazon now lets users text Alexa to help them shop](https://techcrunch.com/2026/11/06/after-blocking-muse-amazon-now-lets-users-text-alexa-to-help-them-shop/) — 来源：TechCrunch AI（发布于 11-06 22:10）
  - 简介：Amazon said that the feature will roll out to millions of users in coming weeks.
- [Amazon will let you text Alexa your shopping list](https://www.theverge.com/tech/1028587/amazon-alexa-shopping-ai-text-orders) — 来源：The Verge AI（发布于 11-06 22:00）
  - 简介：Amazon is adding a new feature to Alexa for Shopping that allows customers to purchase items by texting the AI shopping assistant. Users can describe the products they're looking to buy and/or provide

### 只在一个地方出现、但很热的讨论（Hacker News，按分数排序）

- [Cuban: Facebook knowingly runs AI deepfake scam ads; docs say $16B fraud revenue](https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html) — 来源：Hacker News（HN 496 分，222 条评论，发布于 11-06 07:09）
  - HN 讨论：https://news.ycombinator.com/item?id=50385870
- [AI is dramatically accelerating AI research](https://www.planned-obsolescence.org/p/ai-is-dramatically-accelerating-ai) — 来源：Hacker News（HN 208 分，158 条评论，发布于 11-07 04:27）
  - HN 讨论：https://news.ycombinator.com/item?id=50397994
- [I struggle to believe that AI R&D is ingenious](https://www.lesswrong.com/posts/DALNiKBjMGMF8grme/arjun-panickssery-s-shortform?commentId=fJtaHHHfx45tD7BSL) — 来源：Hacker News（HN 180 分，184 条评论，发布于 11-06 13:19）
  - HN 讨论：https://news.ycombinator.com/item?id=50388513
- [Rune: A native GPU-rendered Rust UI framework for macOS, Windows, Linux and web](https://github.com/anomalyco/rune) — 来源：Hacker News（HN 155 分，112 条评论，发布于 11-07 00:31）
  - HN 讨论：https://news.ycombinator.com/item?id=50394569
- [University libraries are being swarmed by AI bots, putting public access at risk](https://www.cbc.ca/news/world/university-libraries-ai-data-scraping-bots-9.7408287) — 来源：Hacker News（HN 125 分，56 条评论，发布于 11-06 22:13）
  - HN 讨论：https://news.ycombinator.com/item?id=50392499
- [Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3](https://github.com/rivet-dev/rivet) — 来源：Hacker News（HN 118 分，58 条评论，发布于 11-06 01:17）
  - HN 讨论：https://news.ycombinator.com/item?id=50381687
  - 简介：Hey HN, this is Nathan and Nicholas from Rivet ( https://rivet.dev ) – a fast, high-density, and scalable orchestrator for agentic workloads using the actor model. Rather than running a heavyweight sa
- [Nvidia Kubernetes Engine (NVKE)](https://github.com/dsx-ai-factory/nvke) — 来源：Hacker News（HN 122 分，27 条评论，发布于 11-06 11:16）
  - HN 讨论：https://news.ycombinator.com/item?id=50387738
- [Closed AI models dominate the price-performance frontier](https://village.dev/blog/closed-ai-models-now-dominate-the-price-performance-frontier/) — 来源：Hacker News（HN 76 分，72 条评论，发布于 11-06 10:49）
  - HN 讨论：https://news.ycombinator.com/item?id=50387546

## 素材二：新东西

### 官方发布

- [ToyBlocks: A controlled world for robot learning and evaluation](https://huggingface.co/blog/allenai/toyblocks) — 来源：Hugging Face 博客（发布于 11-06 22:00）
- [Partnering with Hacktron to find vulnerabilities in OpenAI’s systems](https://openai.com/index/partnering-with-hacktron) — 来源：OpenAI（发布于 11-06 16:00）
  - 简介：OpenAI is partnering with Hacktron to find vulnerabilities, test connections with third-party services, and strengthen defenses with frontier AI.
- [Measuring how AI agents handle everyday wet-lab science](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science) — 来源：OpenAI（发布于 11-06 08:00）
  - 简介：OpenAI introduces BioBasicsBench, a 100-task benchmark measuring how well AI agents interpret raw experimental data and handle everyday wet-lab science.
- [Egyptian and Nigerian English join the Open ASR Leaderboard](https://huggingface.co/blog/open-asr-leaderboard-liva) — 来源：Hugging Face 博客（发布于 11-06 08:00）
- [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) — 来源：Anthropic 工程博客、Anthropic 研究（发布于 11-06 08:00）
  - 简介：For Claude to learn from experience, it has to decide what’s worth remembering before it knows what’s next. Here’s how “dreaming” helps it organize memory and correct mistakes.
- [Teaching AI to build scientific models](https://www.anthropic.com/research/teaching-ai-to-build-scientific-models) — 来源：Anthropic 研究（发布于 11-06 08:00）
  - 简介：In this guest post, Jakob Macke, Daniel Gedon, and Stefan Wahl discuss how AI is starting to change the scientific modeling process, from construction to interpretation.

### 新上线的模型（OpenRouter）

- [LiquidAI: LFM3-1.7B](https://openrouter.ai/liquid/lfm-3-1.7b) — 上线于 11-07，上下文 262,144 token，每百万 token 输入 $0.08、输出 $0.2
  - 简介：A compact 1.7B-parameter text model with a 256K-token context, post-trained for agents, tool calling, and structured outputs. It reasons before it answers. Prompts and outputs may be retained and used...

### 开源项目和 Skill（GitHub 项目雷达 2026-11-07，已按涨星速度等打过分）

- [nightly-labs/openbot](https://github.com/nightly-labs/openbot) — ⭐ 6,072（每天 +70.6 星，按总星数平均） · 创建 86 天 · TypeScript · NOASSERTION · 43 位贡献者 · 雷达评分 100（潜力股）
  - 简介：A local-first desktop workspace for persistent AI teammates. Run Codex, Claude, and Grok with dedicated workspaces, task queues, file sharing, browser control, and agent-to-agent collaboration.
- [yikart/AiToEarn](https://github.com/yikart/AiToEarn) — ⭐ 27,383（每天 +58.0 星） · 创建 620 天 · TypeScript · MIT · 30 位贡献者 · 雷达评分 98（值得关注）
  - 简介：Let's use AI to Earn!
- [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) — ⭐ 35,167（每天 +136.0 星） · 创建 85 天 · TypeScript · MIT · 60 位贡献者 · 雷达评分 96（潜力股）
  - 简介：为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) — ⭐ 7,096（每天 +92.0 星） · 创建 85 天 · TypeScript · MIT · 76 位贡献者 · 雷达评分 96（潜力股）
  - 简介：DSH's officially top-recommended TUI plugin — high performance, low overhead, cute pixel whale, smooth mouse interaction. One-command install via npm. / DSH 官方首推的 TUI 插件，高性能低占用，可爱像素鲸鱼，流畅鼠标交互，npm 一键安装
- [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) — ⭐ 9,697（每天 +61.0 星） · 创建 39 天 · TypeScript · MIT · 25 位贡献者 · 雷达评分 95（潜力股）
  - 简介：一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。
- [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) — ⭐ 79,063（每天 +51.0 星） · 创建 708 天 · Jupyter Notebook · MIT · 118 位贡献者 · 雷达评分 95（值得关注）
  - 简介：18 Lessons to Get Started Building AI Agents
- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) — ⭐ 20,937（每天 +131.0 星） · 创建 281 天 · TypeScript · MIT · 6 位贡献者 · 雷达评分 95（值得关注）
  - 简介：短剧、漫剧制作工具 Toonflow：开源 AI 视频创作平台，集成剧本创作、智能分镜、角色与场景资产管理、图像生成和视频生成。融合无限画布、AI Agent 与可视化工作流，支持本地部署、自选模型、跨平台客户端、MCP 与插件扩展。Open-source AI short drama and motion comic creation tool with an infinite canvas, AI agents, storyboarding, image and video generation. Self-hosted and extensible, with a canvas-base
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) — ⭐ 46,308（每天 +75.0 星） · 创建 351 天 · Python · Apache-2.0 · 45 位贡献者 · 雷达评分 95（值得关注）
  - 简介：Official, Anthropic-managed directory of high quality Claude Code Plugins.
- [storytold/wordcraft](https://github.com/storytold/wordcraft) — ⭐ 17,481（每天 +68.0 星） · 创建 30 天 · Rust · Apache-2.0 · 253 位贡献者 · 雷达评分 95（潜力股）
  - 简介：An open-source, clean-room reimplementation of Microsoft Word in pure Rust
- [jackwener/OpenCLI](https://github.com/jackwener/OpenCLI) — ⭐ 30,941（每天 +32.0 星） · 创建 237 天 · JavaScript · Apache-2.0 · 269 位贡献者 · 雷达评分 95（值得关注）
  - 简介：Make Any Website into CLI & Use your logged-in browser by AI agent.

### 新工具（Show HN：作者自己发出来的新项目）

今天没有。

## 素材三：论文（HF 每日论文，社区投票精选，按点赞数排序）

- [VFlash: Fast, Accurate Visual Planning via Flash Primitive Decoding](https://huggingface.co/papers/2611.08449) — 来源：HF 每日论文（95 人点赞，1 条评论，发布于 11-06 08:00）
  - 简介：Models for physical AI tasks, such as robotics and autonomous driving, need not reason solely in language. They can use visual plans--points, bounding boxes, and trajectories--to represent spatial goals and anticipate motion. However, autoregressive vision-language models generate these plans one coordinate token at a time, making richer predictions increasingly costly. We introduce VFlash, a method for fast, accurate visual planning through Flash Primitive Decoding. VFlash exploits the known st
- [SLA: Scaling Spatial-Language-Action Model via Continual Pre-training](https://huggingface.co/papers/2611.08373) — 来源：HF 每日论文（88 人点赞，2 条评论，发布于 11-06 08:00）
  - 简介：Reliable robotic manipulation requires both semantic understanding and precise control in three-dimensional space. However, vision-language-action (VLA) foundations largely inherit visual representations from 2D vision-language pre-training, while spatial supervision is often introduced only during task-specific adaptation. Developing spatial understanding as a transferable foundation-model capability therefore calls for learning from broader robot experience. We present SLA, a Spatial-Language-
- [Harness-S: Learning from Sibling Harnesses for Generalizable Agent Training](https://huggingface.co/papers/2611.04277) — 来源：HF 每日论文（54 人点赞，4 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/DeepExperience/Harness-S
  - 简介：Harness evolution from a common base exhibits Locality, Complementarity, and Nonstationarity: variants repair different failures, and their utility changes as the policy learns. Rather than seeking a universally superior harness, we introduce Harness-S to selectively rescue failures of a base execution system through sibling harnesses and transfer the resulting capabilities into a single policy that remains effective under the original harness. Directional Harness Evolution develops specialized 
- [Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand](https://huggingface.co/papers/2611.00883) — 来源：HF 每日论文（50 人点赞，3 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/George-Ling3/BestRand
  - 简介：Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small benchmark subset that closely matches full-benchmark results. To quantify estimation error, we derive an accurate analytical approximation to the error distribution when estimating full-benchmark scores from a subset, showing that most subsets yield small errors, while a few produce much larger errors, resulting in a long-tailed distribution. This means random sampling alone can 
- [WeLM-Image: A Unified Image Generation Model towards Visual Intelligence](https://huggingface.co/papers/2611.07392) — 来源：HF 每日论文（39 人点赞，1 条评论，发布于 11-06 08:00）
  - 简介：We present WeLM-Image, a unified image foundation model that integrates multimodal understanding into text-to-image generation, instruction-guided editing, and multi-reference synthesis. Designed for single-GPU deployment in WeChat's large-scale consumer applications, the model processes text, reference images, and target latents as one interleaved sequence. A Mixture-of-Transformers (MoT) backbone combines shared attention with independent understanding and generation parameters to limit optimi
- [TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing](https://huggingface.co/papers/2611.06741) — 来源：HF 每日论文（37 人点赞，3 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/Lyricccco/tailsteer
  - 简介：Strong single-turn editing performance does not guarantee reliable multi-turn interaction: as edited outputs are repeatedly reused, small unintended changes can accumulate into severe visual drift. This long-term drift is often mitigated through training on multi-turn data or cross-turn rollouts, potentially altering pretrained priors, or through specialized inference-time mechanisms that are difficult to scale to foundation models. We introduce TailSteer, a final-stage training framework that i
- [EvoMemState: Evolving Memory State for Personal Agents](https://huggingface.co/papers/2611.03743) — 来源：HF 每日论文（20 人点赞，4 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/XMUDeepLIT/EvoMemState
  - 简介：Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain memories as independent facts. This fact-centric paradigm may overlook how new facts update, constrain, or conflict with earlier ones, while leaving their applicability, role, and priority for the current request implicit
- [Towards Foundation Decision Models: Drex](https://huggingface.co/papers/2611.07854) — 来源：HF 每日论文（18 人点赞，3 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/nace-ai/drex-decision-models
  - 简介：Autoregressive approaches with large language models, such as long chain-of-thought reasoning, have become the default for new AI applications because they reach higher accuracy on a wide range of tasks. In production, however, they give inconsistent answers, require parsing of outputs, and add cost and latency. Decision models address this: given a question and a set of options supplied by the user, they return a probability distribution over the options without autoregressive decoding. We pres
- [VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents](https://huggingface.co/papers/2611.04894) — 来源：HF 每日论文（17 人点赞，2 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/antins-labs/VisSearch-Bench-v1
  - 简介：Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking it to other findings during search. Visually intensive tasks require agents to com
- [Open-HumanScale: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://huggingface.co/papers/2611.06817) — 来源：HF 每日论文（15 人点赞，2 条评论，发布于 11-06 08:00）
  - 简介：Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanScale, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanScale-50K---a curated egocentric video corpus densely annotated with hand motion and natural language. Leveraging this corpus, we systematically investigate pu
- [On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer](https://huggingface.co/papers/2611.06976) — 来源：HF 每日论文（12 人点赞，2 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/zhenyi4/platour
  - 简介：Prefill-to-Autoregressive Cross-model Transfer (PACT), a form of latent communication between language models, combines a larger model's prompt representations with a smaller model's efficient generation, offering a promising way to balance capability and inference cost. However, existing systems provide limited support for independently evaluating large-small model collaboration, and improved task performance alone does not establish whether the receiver benefits from the sender's information. 
- [EDGAR: Efficient Diffusion-Driven Gaussian Avatar Refinement via Synthetic Failure](https://huggingface.co/papers/2611.07909) — 来源：HF 每日论文（10 人点赞，2 条评论，发布于 11-06 08:00）
  - 代码：https://github.com/kwanyun/edgar-code
  - 简介：Recent advances in Gaussian splatting have enabled efficient and photorealistic head avatar reconstruction, yet monocular video-based or image-based methods still suffer from under-constrained geometry and texture, leading to artifacts such as blurring, stretching, and temporal instability. We present EDGAR (Efficient Diffusion-Driven Gaussian Avatar Refinement), a conditional diffusion framework designed to enhance the quality of Gaussian avatars by correcting artifacts while preserving identit

## 附：博客和 Newsletter 的其他新文章

- [Crusoe sells troubled Wyoming data center project to Google](https://techcrunch.com/2026/11/06/crusoe-sells-troubled-wyoming-data-center-project-to-google/) — 来源：TechCrunch AI（发布于 11-07 09:40）
  - 简介：The deal highlights the challenges of developing massive AI data centers.
- [China reportedly recruited AI exec to spy on Jensen Huang](https://www.theverge.com/tech/1029338/nvidia-ceo-jensen-huang-china-spy) — 来源：The Verge AI（发布于 11-07 07:00）
  - 简介：China's intelligence agency recruited Megaspeed executive Alice Huang to spy on Nvidia CEO Jensen Huang, according to The New York Times. The Ministry
- [All the latest updates on AI data centers](https://www.theverge.com/ai-artificial-intelligence/902546/data-centers-ai-energy-power-grids-controversy) — 来源：The Verge AI（发布于 11-07 04:02）
  - 简介：Massive new data centers are the physical foundation for tech companies’ hopes and dreams for AI. But the rush to expand warehouses full of energy-hun
- [Hundreds of Artex AI hacking tools found publicly exposed to the web](https://techcrunch.com/2026/11/06/hundreds-of-artex-ai-hacking-tools-found-publicly-exposed-to-the-web/) — 来源：TechCrunch AI（发布于 11-07 02:44）
  - 简介：Security researchers found hundreds of servers hosting the penetration testing tool Artex exposed to the internet, allowing anyone access to the hacki
- [How a Blue Wave midterm might reshape the AI industry](https://techcrunch.com/podcast/how-a-blue-wave-midterm-might-reshape-the-ai-industry/) — 来源：TechCrunch AI（发布于 11-07 02:00）
  - 简介：Democrats’ historic victories in this week’s U.S. midterm elections could also transform the tech industry. The public voted on 41 data center-related
- [After the midterms, is the AI industry in for a rough two years?](https://techcrunch.com/video/after-the-midterms-is-the-ai-industry-in-for-a-rough-two-years/) — 来源：TechCrunch AI（发布于 11-07 01:23）
  - 简介：Democrats’ historic victories in this week’s U.S. midterm elections could also transform the tech industry. The public voted on 41 data center-related
- [AI is the new dating dealbreaker](https://www.theverge.com/ai-artificial-intelligence/1028609/ai-dating-feelings-doomers-singularity) — 来源：The Verge AI（发布于 11-07 01:00）
  - 简介：When Irene moved to San Francisco last year, she started using dating apps as a way to meet new people, get to know her new city, and connect with oth
- [Big Tech lost big in the 2026 election](https://www.theverge.com/podcast/1028731/2026-midterms-tech-ai-vergecast) — 来源：The Verge AI（发布于 11-07 00:38）
  - 简介：On Tuesday, millions of American voters went to the polls and voted overwhelmingly for Democrats and against AI. The fight against Big Tech is about t
- [How Akai and Moog are embracing vibe-coded mods](https://www.theverge.com/tech/1028720/vibe-coding-open-source-inmusic-akai) — 来源：The Verge AI（发布于 11-07 00:34）
  - 简介：inMusic, the parent company of Akai, Moog, Native Instruments, and more, has decided to embrace the modding community. In an interview with The Verge,
- [Controlling Biology - Fabian Theis, Helmholtz Munich](https://latent.space/p/controlling-biology-fabian-theis-helmholtz-munich/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 11-06 23:10）
  - 简介：Fabian Theis has been one of the key players in the various iterations of the Virtual Cell concept and initiatives. It is not hyperbole at all to say 
- [Underdog shows off a 32MB speech model in new demo](https://techcrunch.com/2026/11/06/underdog-shows-off-a-32mb-speech-model-in-new-demo/) — 来源：TechCrunch AI（发布于 11-06 21:02）
  - 简介：Despite its small size, Underdog's new model can generate both speech and music.
- [Physicl raises $10M to make the digital world real enough for robots](https://techcrunch.com/2026/11/06/physicl-raises-10m-to-make-the-digital-world-real-enough-for-robots/) — 来源：TechCrunch AI（发布于 11-06 21:00）
  - 简介：Physicl is trying to solve the sim-to-real gap with a pipeline originally built to market goods online.
- [Protesters break into Microsoft data center site in Amsterdam](https://www.theverge.com/news/1028549/protesters-microsoft-data-center-site-amsterdam) — 来源：The Verge AI（发布于 11-06 19:55）
  - 简介：Protesters have broken into a construction site of a new Microsoft data center in Amsterdam this morning. Members of the Geef Tegengas group helped or
- [［AINews］ Inkling 2 Small: 17A-594B trained in 68 hours on 12T tokens, beating Muse Spark](https://latent.space/p/ainews-inkling-2-small-17a-594b-trained-in-68-hours-on-12t-tokens-beating-muse-spark/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 11-06 18:35）
  - 简介：Build AI systems with context graphs and agentic memory. Join Andrew Ng and AI engineers at NODES 2026 for 100+ live technical sessions . Free, online
- [I watched a humanoid robot clean my apartment. It felt like a taste of the future.](https://www.technologyreview.com/2026/11/06/1148090/i-watched-a-humanoid-robot-clean-my-apartment-it-felt-like-a-taste-of-the-future/) — 来源：MIT 科技评论 AI（发布于 11-06 18:00）
  - 简介：I’m not the sort of person who typically pays for a house cleaner. I’m too frugal, and I kind of enjoy putting on a podcast and going to town on my tu
