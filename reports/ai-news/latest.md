# AI 日报素材 · 2026-10-29

> 生成于 2026-10-29 07:11（北京时间）。30/40 个来源抓取成功，失败：油管 @AndrejKarpathy、油管 @TwoMinutePapers、油管 @YannicKilcher、油管 @aiexplained-official、油管 @DwarkeshPatel、油管 @MachineLearningStreetTalk、油管 @LatentSpacePod、油管 @GoogleDeepMind、油管 @OpenAI、油管 @anthropic-ai。本次候选：热议话题 3 个、高热度单条讨论 8 条、新东西 21 条、论文 12 篇。

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

#### 1. 关键词：gemini / gemini 4 / carbon — 4 个来源：Google DeepMind、Hacker News、TechCrunch AI、The Verge AI

- [Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) — 来源：Hacker News（HN 736 分，599 条评论，发布于 10-29 01:01）
  - HN 讨论：https://news.ycombinator.com/item?id=50276792
- [Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/) — 来源：Google DeepMind（发布于 10-29 01:00）
- [Google expands AI Search ads globally as core ad growth slows](https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/) — 来源：TechCrunch AI（发布于 10-29 05:48）
  - 简介：The announcement came alongside parent company Alphabet's third-quarter earnings report, which saw revenue grow 25% year over year to $127.6 billion.
- [As AI agents reshape the web, Google opens Gemini and Search to more apps](https://techcrunch.com/2026/10/28/as-ai-agents-reshape-the-web-google-opens-gemini-and-search-to-more-apps/) — 来源：TechCrunch AI（发布于 10-29 01:00）
  - 简介：A new developer platform will let businesses bring their services to Google's AI experiences, potentially changing how consumers discover and use apps.
- [Google launches Gemini 4 Carbon with a ‘significant leap’ in cybersecurity](https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier) — 来源：The Verge AI（发布于 10-29 04:03）
  - 简介：Google has released its latest frontier model, Gemini 4 Carbon, offering "significant gains" in coding, agentic tasks, and cybersecurity. In an announcement on Wednesday, Google highlights Carbon's to

#### 2. 关键词：transcription / nvidia — 3 个来源：Hacker News、Hugging Face 博客、TechCrunch AI

- [NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) — 来源：Hacker News、Hugging Face 博客（HN 101 分，17 条评论，发布于 10-28 22:58）
  - HN 讨论：https://news.ycombinator.com/item?id=50275128
- [Voice AI in vogue: Nvidia releases new open transcription model](https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/) — 来源：TechCrunch AI（发布于 10-28 23:00）
  - 简介：Nvidia just released a free speech-to-text model that can transcribe up to 40 languages, but it only works on recordings, not live audio, so it’s a big step for meeting and medical transcription tools

#### 3. 关键词：autofill / chrome / gmail — 2 个来源：TechCrunch AI、The Verge AI

- [Chrome’s AI-powered Autofill can now dig through your Gmail to fill out forms](https://techcrunch.com/2026/10/28/chromes-ai-powered-autofill-can-now-dig-through-your-gmail-to-fill-out-forms/) — 来源：TechCrunch AI（发布于 10-29 01:00）
  - 简介：The autofill update lets Chrome pull flight confirmations, tracking info, order details, and other information from your inbox, with your permission.
- [Chrome’s enhanced autofill can now pull info from Gmail to help you fill out forms](https://www.theverge.com/tech/1020626/chrome-enhanced-autofill-gmail-forms-gemini-personal-intelligence) — 来源：The Verge AI（发布于 10-29 01:00）
  - 简介：Following improvements made to Chrome's enhanced autofill last year that included your name, passport number, email address, and physical addresses sourced from your Google Accounts and services like 

### 只在一个地方出现、但很热的讨论（Hacker News，按分数排序）

- [Kentucky man becomes the first humanist granted religious exemption from AI](https://religionnews.com/2026/10/26/in-a-first-a-humanist-granted-a-religious-exemption-from-using-ai/) — 来源：Hacker News（HN 403 分，448 条评论，发布于 10-28 21:41）
  - HN 讨论：https://news.ycombinator.com/item?id=50273396
- [Survival LLM: AI assistant and emergency library that runs on your own computer](https://www.brangus.io/survival-llm) — 来源：Hacker News（HN 514 分，193 条评论，发布于 10-28 03:55）
  - HN 讨论：https://news.ycombinator.com/item?id=50264853
- [Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/) — 来源：Hacker News（HN 224 分，90 条评论，发布于 10-29 05:03）
  - HN 讨论：https://news.ycombinator.com/item?id=50280864
- [Dayjob: Tax – evaluating AI agents on 50 professional tax assignments](https://surgehq.ai/blog/dayjob-tax) — 来源：Hacker News（HN 177 分，107 条评论，发布于 10-28 23:46）
  - HN 讨论：https://news.ycombinator.com/item?id=50275626
- [The Agent SDK](https://cursor.com/blog/agent-sdk) — 来源：Hacker News（HN 85 分，106 条评论，发布于 10-28 22:02）
  - HN 讨论：https://news.ycombinator.com/item?id=50273731
- [Google AI gets cagey when asked who won the 2020 elections](https://arstechnica.com/ai/2026/10/google-ai-gets-cagey-when-asked-who-won-the-2020-elections/) — 来源：Hacker News（HN 113 分，55 条评论，发布于 10-29 04:10）
  - HN 讨论：https://news.ycombinator.com/item?id=50280178
- [Valve Responds to Developers Fearing AI Slop and Clones](https://www.invenglobal.com/articles/27761/valve-responds-to-developers-fearing-ai-slop-and-clones) — 来源：Hacker News（HN 65 分，76 条评论，发布于 10-28 21:27）
  - HN 讨论：https://news.ycombinator.com/item?id=50273192
- [Harvey raised 500M for legal AI, I built the same and open sourced it](https://github.com/thomasunise/casecite) — 来源：Hacker News（HN 68 分，37 条评论，发布于 10-28 21:56）
  - HN 讨论：https://news.ycombinator.com/item?id=50273623

## 素材二：新东西

### 官方发布

- [Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/) — 来源：Google DeepMind（发布于 10-29 01:00）
- [NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary) — 来源：Hacker News、Hugging Face 博客（HN 101 分，17 条评论，发布于 10-28 22:58）
  - HN 讨论：https://news.ycombinator.com/item?id=50275128
- [OpenAI and ServiceNow expand partnership across enterprise workflows](https://openai.com/index/openai-servicenow-partnership-expansion) — 来源：OpenAI（发布于 10-28 21:15）
  - 简介：OpenAI and ServiceNow expand their partnership to bring OpenAI models and agents into ServiceNow and ServiceNow workflows into ChatGPT and Codex.
- [The future of the firm](https://openai.com/index/the-future-of-the-firm) — 来源：OpenAI（发布于 10-28 18:00）
  - 简介：How AI might enter the org chart—beneath, beside, and between us.
- [Legora is building the agentic operating system for legal work](https://openai.com/index/legora) — 来源：OpenAI（发布于 10-28 17:30）
  - 简介：See how Legora uses OpenAI models, ChatGPT, and Codex to accelerate legal workflows, expand contract analysis, and free lawyers to focus on higher-value work.
- [AI for Science expands to foundations and research institutions](https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions) — 来源：Anthropic 新闻（发布于 10-28 08:00）
  - 简介：We’re highlighting 20 scientific foundations, institutions, and research groups from around the world that we’ve partnered with in an expansion of our AI for Science program.
- [Smart reports, surveys, and pooled group budgets for Claude Enterprise](https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets) — 来源：Claude 博客（发布于 10-28 08:00）
  - 简介：In many organizations, members have identified the unique work that Claude can unlock. The next step is expanding that work to every team.
- [Introducing artifacts for legal work](https://claude.com/resources/articles/introducing-artifacts-for-legal-work) — 来源：Claude 博客（发布于 10-28 08:00）
  - 简介：Claude for Legal now includes ready-to-use artifacts for legal work that teams can adapt with their own data and connectors, and share across the business.
- [IDC brings Quanta into Claude and adopts Claude across the company](https://claude.com/resources/articles/idc-brings-quanta-into-claude-and-adopts-claude-across-the-company) — 来源：Claude 博客（发布于 10-28 08:00）
  - 简介：IDC integrated Claude as part of its Quanta platform, and it has rolled Claude out across its own business
- [Manage costs and demonstrate ROI for Claude Code on Google Cloud](https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud) — 来源：Claude 博客（发布于 10-27 08:00）
  - 简介：Best practices for managing costs and measuring return on investment for Claude Code on Google Cloud.

### 新上线的模型（OpenRouter）

- [Particle AI: Particle-1](https://openrouter.ai/particle-ai/particle-1) — 上线于 10-29，上下文 1,048,576 token，每百万 token 输入 $0.25、输出 $1
  - 简介：Particle-1 is a token-efficient agentic coding model from Particle AI, post-trained on DeepSeek V4.1 Flash. It is suited for software engineering work such as terminal workflows, codebase changes, and data...

### 开源项目和 Skill（GitHub 项目雷达 2026-10-29，已按涨星速度等打过分）

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) — ⭐ 264,763（每天 +1123.0 星） · 创建 76 天 · TypeScript · MIT · 66 位贡献者 · 雷达评分 100（潜力股）
  - 简介：DeepSeek Harness: Everything is a Plugin.
- [storytold/photocraft](https://github.com/storytold/photocraft) — ⭐ 74,393（每天 +486.0 星） · 创建 28 天 · Rust · Apache-2.0 · 461 位贡献者 · 雷达评分 100（潜力股）
  - 简介：PhotoCraft: An open-source, photo editor written by scratch in pure Rust
- [storytold/pdfcraft](https://github.com/storytold/pdfcraft) — ⭐ 18,444（每天 +212.0 星） · 创建 28 天 · Rust · Apache-2.0 · 322 位贡献者 · 雷达评分 100（潜力股）
  - 简介：PdfCraft: An open-source PDF reader and editor written by scratch in pure Rust
- [storytold/filmcraft](https://github.com/storytold/filmcraft) — ⭐ 16,724（每天 +155.0 星） · 创建 28 天 · Rust · Apache-2.0 · 136 位贡献者 · 雷达评分 100（潜力股）
  - 简介：FilmCraft: An open-source, nonlinear video editor written by scratch in pure Rust
- [storytold/lightcraft](https://github.com/storytold/lightcraft) — ⭐ 14,978（每天 +114.0 星） · 创建 28 天 · Rust · Apache-2.0 · 213 位贡献者 · 雷达评分 100（潜力股）
  - 简介：LightCraft: An open-source non-destructive photo editor written by scratch in pure Rust
- [storytold/vectorcraft](https://github.com/storytold/vectorcraft) — ⭐ 10,933（每天 +81.0 星） · 创建 28 天 · Rust · Apache-2.0 · 197 位贡献者 · 雷达评分 100（潜力股）
  - 简介：VectorCraft: An open-source, vector art tool written by scratch in pure Rust
- [storytold/effectcraft](https://github.com/storytold/effectcraft) — ⭐ 8,090（每天 +54.0 星） · 创建 27 天 · Rust · Apache-2.0 · 118 位贡献者 · 雷达评分 100（潜力股）
  - 简介：EffectCraft: An open-source motion graphics and compositing tool written by scratch in pure Rust
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — ⭐ 7,639（每天 +262.0 星） · 创建 72 天 · TypeScript · MIT · 46 位贡献者 · 雷达评分 100（潜力股）
  - 简介：Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided before it happens and recorded after. Bring any AG-UI agent.
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) — ⭐ 6,670（每天 +56.0 星） · 创建 31 天 · Swift · MIT · 39 位贡献者 · 雷达评分 100（潜力股）
  - 简介：A tiny friend in your Mac's notch and on your iPhone that keeps an eye on your AI coding agents: Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more. Approve from the notch or your Lock Screen.
- [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) — ⭐ 6,581（每天 +814.0 星） · 创建 78 天 · TypeScript · Apache-2.0 · 176 位贡献者 · 雷达评分 100（潜力股）
  - 简介：Open-source Grok Bot alternative with a virtual machine that bots can use

### 新工具（Show HN：作者自己发出来的新项目）

今天没有。

## 素材三：论文（HF 每日论文，社区投票精选，按点赞数排序）

- [ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence](https://huggingface.co/papers/2610.34283) — 来源：HF 每日论文（344 人点赞，1 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/yihaohu0118/ChronoReplay
  - 简介：Training a spatial VLM to answer which side an object lies on does not require it to preserve the metric displacement that determines that answer, while supervision for a distance estimate may leave categorical relations largely unconstrained. When post-training emphasizes one readout, improvements can therefore concentrate on that interface while transfer to others remains weak or even degrades; we call this observed specialization interface lock-in. ChronoReplay addresses it by replaying heter
- [Multiscale Policy Optimization for Long-Horizon LLM Agents](https://huggingface.co/papers/2610.35013) — 来源：HF 每日论文（342 人点赞，3 条评论，发布于 10-28 08:00）
  - 简介：Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale Policy Optimization (MPO), combining Multiscale Advantage Estimation (MAE) and turn-level importance sampling to align credit assignment and policy updates at the turn scale. Extensive experiments ac
- [The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://huggingface.co/papers/2610.36077) — 来源：HF 每日论文（311 人点赞，2 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/InfRec-Cardinal/The-Trinity
  - 简介：Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with growing task diversity and complexity. A key insight is that tasks with different modalities and surface forms can share the same underlying capability requirements. We therefore introduce The Trinity, a recursive self-
- [VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://huggingface.co/papers/2610.35864) — 来源：HF 每日论文（171 人点赞，1 条评论，发布于 10-28 08:00）
  - 简介：Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-drive
- [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://huggingface.co/papers/2610.37381) — 来源：HF 每日论文（135 人点赞，1 条评论，发布于 10-28 08:00）
  - 简介：Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation. The module learns 
- [Hy-Nomas: Towards Free-form Interactive World Generation](https://huggingface.co/papers/2610.36729) — 来源：HF 每日论文（104 人点赞，1 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/Tencent-Hunyuan/Hy-Nomas
  - 简介：Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interaction turns. It generates variable-length segments conditioned on current inputs and cached history. Our central design aligns structured video captions with action-aware causal attention: descriptive 
- [Memory Tax: Dissecting the Net Value of Agent Memory](https://huggingface.co/papers/2610.34073) — 来源：HF 每日论文（100 人点赞，3 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/hexuan21/MemoryTax
  - 简介：Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in many cases, indicating a negative net value. Taking RAG as a reference, we dissect the net value of memory into the gains and losses over direct retrieval, termed memory benefit and memory tax. These ga
- [Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?](https://huggingface.co/papers/2610.37662) — 来源：HF 每日论文（81 人点赞，1 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/hustvl/FVQ
  - 简介：Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic fidelity of discrete visual tokens and positioning continuous visual representations as an intrinsic upper bound. Using multimodal understanding as a proxy for semantic fidelity, we revisit this assum
- [HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://huggingface.co/papers/2610.24520) — 来源：HF 每日论文（78 人点赞，5 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/LUMIA-Group/habit-bench
  - 简介：In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or when it applies. Retaining past interactions alone does not ensure that agents can infer habits and apply them appropriately. We introduce HABIT-Bench to evaluate how well agent memory systems infer habi
- [Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?](https://huggingface.co/papers/2610.32046) — 来源：HF 每日论文（72 人点赞，2 条评论，发布于 10-28 08:00）
  - 代码：https://github.com/yepengliu/TTME
  - 简介：Recent test-time training (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cost for online weight updates during the discovery process, making computational efficiency an important consideration when scaling to larger models. This motivates us to explore an efficient test-time adaptation method for scientific discovery. We introd
- [Representation Redistribution in Sparse Autoencoders](https://huggingface.co/papers/2610.21240) — 来源：HF 每日论文（56 人点赞，2 条评论，发布于 10-27 08:00）
  - 代码：https://github.com/OpenSAE/Redistribution-Sensitivity-Score
  - 简介：Sparse autoencoders (SAEs) decompose language model activations into sparse features, but prompt transformations designed to preserve the underlying request can redistribute activity across them. A feature change observed on one transformed prompt need not recur, and even a recurring change need not affect a downstream computation. We introduce the redistribution sensitivity score (RSS), which identifies large feature responses that recur in a consistent direction, and evaluate the resulting sup
- [Rollback: Experience Backtracking in World Models for Policy Improvement](https://huggingface.co/papers/2610.36068) — 来源：HF 每日论文（50 人点赞，1 条评论，发布于 10-28 08:00）
  - 简介：Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies. However, existing world-model-based methods largely treat world models as forward-only surrogates of the physical environment, leaving untapped a capability no physical environment affords: rewinding to past decision points to explore counterfactual futures. We introduce Rollback, a policy improvement paradigm that turns world models from passive simulators into counterfact

## 附：博客和 Newsletter 的其他新文章

- [Adam Mosseri says negativity around AI is ‘going to get worse’](https://www.theverge.com/ai-artificial-intelligence/1021644/adam-mosseri-instagram-ai-negativity) — 来源：The Verge AI（发布于 10-29 07:05）
  - 简介：Asked about AI and the trend of college students booing tech CEOs at graduation ceremonies, Instagram head Adam Mosseri acknowledged in an interview t
- [Microsoft just shared Azure’s actual revenue in dollars: $33.2 billion](https://techcrunch.com/2026/10/28/microsoft-just-shared-azures-actual-revenue-in-dollars-33-2-billion/) — 来源：TechCrunch AI（发布于 10-29 05:58）
  - 简介：Microsoft has never disclosed Azure's quarterly revenue in dollars. But for the first time, we can see just how close it is getting to besting the big
- [Microsoft recorded $10 billion in revenue from OpenAI](https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/) — 来源：TechCrunch AI（发布于 10-29 05:34）
  - 简介：Microsoft said it made $10 billion in revenue from commercial arrangements with OpenAI, including revenue-sharing payments, in the quarter ending Sept
- [Akai is embracing vibe-coded mods with an open-source MPC](https://www.theverge.com/gadgets/1021405/akai-open-source-mpc-sample-key) — 来源：The Verge AI（发布于 10-29 05:34）
  - 简介：The MPC Sample Key isn't even formally announced yet, but Akai is already showing off what the modding community is cooking up through vibe coding. Ak
- [Microsoft hits 10 quarters of record-breaking revenue in a row](https://techcrunch.com/2026/10/28/microsoft-hits-10-quarters-of-record-breaking-revenue-in-a-row/) — 来源：TechCrunch AI（发布于 10-29 05:25）
  - 简介：Whatever the future of AI might be, the current situation is still very good for Microsoft. The tech giant reported yet another record for quarterly r
- [Creating AI value with enterprise context](https://www.technologyreview.com/2026/10/28/1147709/creating-ai-value-with-enterprise-context/) — 来源：MIT 科技评论 AI（发布于 10-29 04:32）
  - 简介：Across a business, any number of AI platforms, systems, and tools may be at work simultaneously—for example, AI-powered customer platforms, conversati
- [Why Agents Love Supabase](https://latent.space/p/supabase/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 10-29 03:48）
  - 简介：I first met Paul Copplestone and Ant Wilson in Singapore, shortly after they finished YC as the hottest startup of YC S20 . Six years later, we finall
- [Anthropic just launched tools to show companies what their AI spending is buying](https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/) — 来源：TechCrunch AI（发布于 10-29 03:19）
  - 简介：The frontier lab is lifting the curtain on how users spend money on its models ahead of a planned IPO.
- [Wiz’s CTO on PHP2Shell and the coming ‘vulnpocalypse’](https://techcrunch.com/video/wizs-cto-on-php2shell-and-the-coming-vulnpocalypse/) — 来源：TechCrunch AI（发布于 10-29 03:05）
  - 简介：The PHP scare may have faded from your feed, but the cleanup is far from over. Last week, two critical bugs in the open source language behind roughly
- [The ‘Vulnpocalypse’ is coming for the internet’s aging code, says Wiz’s CTO](https://techcrunch.com/podcast/the-vulnpocalypse-is-coming-for-the-internets-aging-code-says-wizs-cto/) — 来源：TechCrunch AI（发布于 10-29 02:50）
  - 简介：The PHP scare may have faded from your feed, but the cleanup is far from over. Last week, two critical bugs in the open source language behind roughly
- [Microsoft is ending Copilot support on smart TVs](https://www.theverge.com/tech/1021143/microsoft-lg-samsung-copilot-ai-assistant-smart-tvs-ending) — 来源：The Verge AI（发布于 10-29 02:36）
  - 简介：Nearly two years after LG and Samsung announced at CES 2025 that their latest smart TVs would include access to Microsoft's Copilot, the company is en
- [Meta says it’ll probably delay its controversial new business terms again](https://www.theverge.com/tech/1020769/meta-updated-business-terms-delay-indefinitely) — 来源：The Verge AI（发布于 10-29 00:15）
  - 简介：Meta says it may push the implementation of its new business terms past November 20th as it faces backlash from publishers over concerns about AI trai
- [AI execs may be too out of touch to build for the general public](https://techcrunch.com/2026/10/28/ai-execs-may-be-too-out-of-touch-to-build-for-the-general-public/) — 来源：TechCrunch AI（发布于 10-28 23:53）
  - 简介：Tech leaders are flaunting how out of touch they are when they brag about using AI to connect with their families.
- [South Korea’s financial industry hit by fresh wave of cyberattacks](https://techcrunch.com/2026/10/28/south-koreas-financial-industry-hit-by-fresh-wave-of-cyberattacks/) — 来源：TechCrunch AI（发布于 10-28 23:41）
  - 简介：South Korea’s financial institutions have been hit by another wave of cyberattacks, highlighting the growing risk of AI-driven hacking in Asia.
- [xAI is buying out homeowners who promise not to sue over data center noise](https://www.theverge.com/ai-artificial-intelligence/1020596/xai-mississippi-neighborhood-data-center-lawsuit) — 来源：The Verge AI（发布于 10-28 22:44）
  - 简介：A subsidiary of Elon Musk's xAI is offering to buy up homes in a Mississippi neighborhood, as long as residents don't join a lawsuit targeting the com
