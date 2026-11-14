# AI 日报素材 · 2026-11-14

> 生成于 2026-11-14 10:40（北京时间）。30/40 个来源抓取成功，失败：油管 @AndrejKarpathy、油管 @TwoMinutePapers、油管 @YannicKilcher、油管 @aiexplained-official、油管 @DwarkeshPatel、油管 @MachineLearningStreetTalk、油管 @LatentSpacePod、油管 @GoogleDeepMind、油管 @OpenAI、油管 @anthropic-ai。本次候选：热议话题 2 个、高热度单条讨论 8 条、新东西 20 条、论文 12 篇。

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

#### 1. 关键词：chatgpt / wallet / lets — 3 个来源：OpenAI、TechCrunch AI、The Verge AI

- [Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) — 来源：OpenAI（发布于 11-13 23:00）
  - 简介：Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.
- [ChatGPT’s new Wallet lets AI agents shop and check out for you](https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/) — 来源：TechCrunch AI（发布于 11-14 00:00）
  - 简介：ChatGPT Wallet lets AI agents shop and check out on users' behalf, starting with a limited rollout to U.S. Pro subscribers.
- [ChatGPT Wallet lets OpenAI’s Dots agents make purchases for you](https://www.theverge.com/ai-artificial-intelligence/1033425/openai-chatgpt-wallet) — 来源：The Verge AI（发布于 11-14 04:45）
  - 简介：After launching its Dots AI agents platform earlier this year, OpenAI is launching a wallet for the agents. ChatGPT Wallet is rolling out starting today for ChatGPT Pro subscribers in the US aged 18 a

#### 2. 关键词：Building strong safety evaluations — 2 个来源：Anthropic 工程博客、Anthropic 研究

- [Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations) — 来源：Anthropic 工程博客、Anthropic 研究（发布于 11-13 08:00）
  - 简介：Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.

### 只在一个地方出现、但很热的讨论（Hacker News，按分数排序）

- [Nvidia employees petition to bring back Jensen Huang](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/) — 来源：Hacker News（HN 792 分，652 条评论，发布于 11-13 10:16）
  - HN 讨论：https://news.ycombinator.com/item?id=50477231
- [Elevated errors on claude.ai, Claude Code, and platform.claude.com](https://status.claude.com/incidents/nn11wk485zfn) — 来源：Hacker News（HN 484 分，383 条评论，发布于 11-13 18:18）
  - HN 讨论：https://news.ycombinator.com/item?id=50481187
- [AI is destroying the trust between writers and readers](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/) — 来源：Hacker News（HN 314 分，195 条评论，发布于 11-13 19:13）
  - HN 讨论：https://news.ycombinator.com/item?id=50481870
- [$11.4M in Nvidia hardware vanishes during shipment from CA to TX](https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas) — 来源：Hacker News（HN 299 分，168 条评论，发布于 11-14 02:40）
  - HN 讨论：https://news.ycombinator.com/item?id=50487864
- [AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths) — 来源：Hacker News（HN 337 分，93 条评论，发布于 11-14 01:30）
  - HN 讨论：https://news.ycombinator.com/item?id=50486748
- [Brave Search API now accepts agentic payments via the x402 protocol](https://brave.com/blog/search-api-agentic-payments/) — 来源：Hacker News（HN 256 分，148 条评论，发布于 11-13 11:08）
  - HN 讨论：https://news.ycombinator.com/item?id=50477649
- [Claude Is Down](https://status.claude.com/history) — 来源：Hacker News（HN 197 分，172 条评论，发布于 11-13 18:20）
  - HN 讨论：https://news.ycombinator.com/item?id=50481220
- [Why is Google cutting off Search from AI-free schools? Here are some theories](https://text.npr.org/nx-s1-6029408) — 来源：Hacker News（HN 166 分，166 条评论，发布于 11-13 23:29）
  - HN 讨论：https://news.ycombinator.com/item?id=50484960

## 素材二：新东西

### 官方发布

- [Advancing science & engineering with Antigravity’s /teamwork](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/) — 来源：Google Research（发布于 11-14 04:47）
  - 简介：Education Innovation
- [Build a Robot Pick-and-Place Simulation with SimReady Assets](https://huggingface.co/blog/nvidia/simready-assets-robot-pick-and-place) — 来源：Hugging Face 博客（发布于 11-14 02:00）
- [XYBench: Helping with the problem behind the question](https://huggingface.co/blog/allenai/xybench) — 来源：Hugging Face 博客（发布于 11-14 01:02）
- [Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet) — 来源：OpenAI（发布于 11-13 23:00）
  - 简介：Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.
- [llama.cpp v1.0.0 : A stronger foundation for the local AI ecosystem](https://huggingface.co/blog/ggml-org/llama-cpp-v1) — 来源：Hugging Face 博客（发布于 11-13 22:05）
- [An update on our recent security incident](https://cursor.com/blog/security-incident-update) — 来源：Cursor（发布于 11-13 20:00）
- [Shield helps technicians hand off legacy portal work with OpenAI](https://openai.com/business/customer-stories/shield) — 来源：OpenAI（发布于 11-13 16:00）
  - 简介：Shield uses OpenAI to help IT technicians hand off work in legacy portals. Its Forge agents navigate systems so technicians can focus on issues needing their judgment.
- [Building strong safety evaluations](https://www.anthropic.com/research/building-strong-safety-evaluations) — 来源：Anthropic 工程博客、Anthropic 研究（发布于 11-13 08:00）
  - 简介：Recommendations for designing, running, and reporting safety evaluations, based on our own experiences.
- [The Claude Tag guide for startups](https://claude.com/resources/articles/claude-tag-guide-for-startups) — 来源：Claude 博客（发布于 11-13 08:00）
  - 简介：How leading startups use Claude Tag to ship faster and scale operations
- [Building always-on agents](https://claude.com/resources/articles/building-always-on-agents) — 来源：Claude 博客（发布于 11-13 08:00）
  - 简介：Always-on agents run indefinitely, deciding how and when to act across many sessions. This guide walks through their core primitives and how they fit together.

### 新上线的模型（OpenRouter）

今天没有。

### 开源项目和 Skill（GitHub 项目雷达 2026-11-14，已按涨星速度等打过分）

- [openfilm/openfilm](https://github.com/openfilm/openfilm) — ⭐ 6,629（每天 +165.7 星，按总星数平均） · 创建 40 天 · TypeScript · MIT · 30 位贡献者 · 雷达评分 100（潜力股）
  - 简介：The open source AI video agent: turns any coding agent into a video agent, with an editor to change anything it makes.
- [affaan-m/ECC](https://github.com/affaan-m/ECC) — ⭐ 302,498（每天 +441.0 星） · 创建 300 天 · JavaScript · MIT · 478 位贡献者 · 雷达评分 100（值得关注）
  - 简介：The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — ⭐ 263,234（每天 +242.0 星） · 创建 479 天 · Python · MIT · 6355 位贡献者 · 雷达评分 100（值得关注）
  - 简介：The agent that grows with you
- [ollama/ollama](https://github.com/ollama/ollama) — ⭐ 186,903（每天 +79.0 星） · 创建 1236 天 · Go · MIT · 630 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models.
- [open-webui/open-webui](https://github.com/open-webui/open-webui) — ⭐ 158,593（每天 +80.0 星） · 创建 1134 天 · Svelte · NOASSERTION · 893 位贡献者 · 雷达评分 100（值得关注）
  - 简介：User-friendly AI Interface (Supports Ollama, OpenAI API, ...)
- [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) — ⭐ 147,317（每天 +511.0 星） · 创建 224 天 · Python · Apache-2.0 · 414 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.
- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) — ⭐ 113,721（每天 +290.0 星） · 创建 256 天 · TypeScript · MIT · 264 位贡献者 · 雷达评分 100（值得关注）
  - 简介：The open-source app everyone uses to manage agents at work
- [Tencent/WeKnora](https://github.com/Tencent/WeKnora) — ⭐ 37,400（每天 +71.0 星） · 创建 479 天 · Go · NOASSERTION · 378 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Open-source LLM knowledge platform: turn raw documents into a queryable RAG, an autonomous reasoning agent, and a self-maintaining Wiki.
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) — ⭐ 30,121（每天 +251.0 星） · 创建 506 天 · TypeScript · Apache-2.0 · 647 位贡献者 · 雷达评分 100（值得关注）
  - 简介：An open-source AI coding agent that lives in your terminal.
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) — ⭐ 60,190（每天 +204.0 星） · 创建 302 天 · JavaScript · MIT · 64 位贡献者 · 雷达评分 100（值得关注）
  - 简介：Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

### 新工具（Show HN：作者自己发出来的新项目）

今天没有。

## 素材三：论文（HF 每日论文，社区投票精选，按点赞数排序）

- [SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](https://huggingface.co/papers/2611.15777) — 来源：HF 每日论文（78 人点赞，2 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/holdrain/SO-Arena
  - 简介：System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the breadth of model capabilities and the reliability of their decisions. We introduce SO-Arena, a benchmark characterizing the capability spectrum and decision reliability of System One models across 11 doma
- [BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model](https://huggingface.co/papers/2611.14815) — 来源：HF 每日论文（46 人点赞，1 条评论，发布于 11-13 08:00）
  - 简介：Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and vehicles can be occluded. Prior work therefore conditions video generation on layouts that specify vehicle motion, providing control over surrounding vehicles but requiring their future trajectories a
- [PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://huggingface.co/papers/2611.16748) — 来源：HF 每日论文（42 人点赞，3 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/DAGroup-PKU/PhysLoop
  - 简介：Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. Large language models (LLMs) possess physical knowledge, but struggle to reliably guide video generation models in producing their training videos. We present PhysLoop, a unified harness designed to s
- [G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation](https://huggingface.co/papers/2611.13004) — 来源：HF 每日论文（41 人点赞，2 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/DAGroup-PKU/G-STAR
  - 简介：Discrete autoregressive models offer a scalable framework for image generation. However, they face a fundamental trade-off: long token sequences preserve representation quality but slow generation, while aggressive spatial compression reduces representation capacity. Based on product quantization, we show that, under a fixed nominal information budget, group size should scale quadratically with the per-axis spatial compression factor. Building on this principle, we propose GSTAR, a spatial--grou
- [Duo: A Reciprocal World Model for Full-Duplex Interaction](https://huggingface.co/papers/2611.15131) — 来源：HF 每日论文（37 人点赞，1 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/inclusionAI/Duo
  - 简介：In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time. The RWM treats intelligence and physical reality as equally fundamental to what constitutes a world. Existing world models largely focus on simulating the latter, leaving reasoning and decision-making as external controls rather than intrinsic parts of the world itself. In RWM, we identify two equally fu
- [Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://huggingface.co/papers/2611.15844) — 来源：HF 每日论文（30 人点赞，1 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/OpenVisionBanana/OpenVisionBanana
  - 简介：Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present Open Vision Banana (OVB), a fully open and reproducible recipe for converting pretrained generators into unified multi-task perception systems. Our analyses identify the design choices that matter most for generalization
- [Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://huggingface.co/papers/2611.17167) — 来源：HF 每日论文（29 人点赞，2 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/ZJU-REAL/decision-agents
  - 简介：Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges
- [Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://huggingface.co/papers/2611.17060) — 来源：HF 每日论文（26 人点赞，1 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/Ropedia/Ropedia-Xperience-2
  - 简介：Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two complementary resources: demonstrations of human behavior that supervise how tasks are performed, and interactive environments in which policies can be rolled out, evaluated, and improved in closed loop. Language models have adv
- [On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://huggingface.co/papers/2611.05984) — 来源：HF 每日论文（26 人点赞，2 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/aHapBean/SimpleHC
  - 简介：Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler, more efficient designs. We find that learned read/write gating without mixing and unconstrained mixing with fixed gates form two effective interaction groups: either alone achieves performance compa
- [TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://huggingface.co/papers/2611.17331) — 来源：HF 每日论文（21 人点赞，1 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/NVlabs/DVSM
  - 简介：Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the 
- [WorldDraft: If Code Builds the World, Can Video Models Just Render It?](https://huggingface.co/papers/2611.16217) — 来源：HF 每日论文（14 人点赞，2 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/KevinHuge/WorldDraft
  - 简介：Multimodal coding agents decouple 4D world construction from visual generation, repurposing video models from world generators toward generative renderers. This division of labor raises a fundamental question: if code builds the world, can video models just render it? A reliable generative renderer hinges on two complementary criteria: (i) world preservation, retaining prescribed 4D kinematics and camera paths; and (ii) visual realization, persistently binding text-specified target attributes ov
- [Factored One-sided Adam-Moment for Practical and Scalable SOAP](https://huggingface.co/papers/2611.16905) — 来源：HF 每日论文（12 人点赞，1 条评论，发布于 11-13 08:00）
  - 代码：https://github.com/naver-ai/foam
  - 简介：Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state memory and eigendecomposition overhead. We ask whether the benefits of SOAP can be retained at nearly the efficiency of AdamW. In this paper, we answer yes with a lightweight SOAP variant, Factored One-sided Adam-Moment (FOA

## 附：博客和 Newsletter 的其他新文章

- [Amazon has a plan to index the world’s online shopping data](https://www.theverge.com/tech/1033697/amazon-world-product-graph-ai-search) — 来源：The Verge AI（发布于 11-14 07:49）
  - 简介：Amazon has plans to build a vault of data on every product sold anywhere on the internet, even products Amazon doesn't sell, and make the information 
- [Jensen Huang’s departure blasts big hole in AI startup funding, VCs and founders say](https://techcrunch.com/2026/11/13/jensen-huangs-departure-blasts-big-hole-in-ai-startup-funding-vcs-and-founders-say/) — 来源：TechCrunch AI（发布于 11-14 06:43）
  - 简介：Nvidia poured tens of billions into AI startups under Huang. Without him at the helm, founders and VCs are bracing for smaller checks and lower valuat
- [AI agent startup LangChain hits $3B valuation](https://techcrunch.com/2026/11/13/ai-agent-startup-langchain-hits-3b-valuation/) — 来源：TechCrunch AI（发布于 11-14 03:37）
  - 简介：LangChain now claims 7,000 customers of its model and platform agnostic agent management tool LangSmith.
- [Export-banned Nvidia chips are behind China’s most powerful AI models — uh-oh, Jensen!](https://techcrunch.com/2026/11/13/export-banned-nvidia-chips-are-behind-chinas-most-powerful-ai-models-uh-oh-jensen/) — 来源：TechCrunch AI（发布于 11-14 02:40）
  - 简介：New research shows the most advanced AI models from China were trained on banned Nvidia chips.
- [The unfolding Jensen Huang scandal: a timeline](https://techcrunch.com/2026/11/13/nvidia-ceo-jensen-huangs-affair-with-alleged-chinese-spy-a-timeline/) — 来源：TechCrunch AI（发布于 11-13 23:58）
  - 简介：Jensen Huang has resigned from Nvidia following an affair, which could have ramifications for national security as the U.S. and China race to develop 
- [What’s really at stake in the Jensen Huang saga](https://www.theverge.com/podcast/1032866/jensen-huang-nvidia-china-trump-vergecast) — 来源：The Verge AI（发布于 11-13 22:47）
  - 简介：One part of the saga surrounding Nvidia CEO Jensen Huang ended on Thursday, when Huang resigned from his position at the top of AI's most important co
- [ElevenLabs’ new app combines meeting note-taking and dictation for teams](https://techcrunch.com/2026/11/13/elevenlabs-new-app-combines-meeting-note-taking-and-dictation-for-teams/) — 来源：TechCrunch AI（发布于 11-13 22:44）
  - 简介：ElevenAI is a new meeting notetaker and dictation app aimed at teams and enterprises.
- [Claude’s Duet agent is a little neurotic and surprisingly helpful](https://www.theverge.com/ai-artificial-intelligence/1032518/claude-duet-ai-agent-hands-on) — 来源：The Verge AI（发布于 11-13 22:00）
  - 简介：Normally, the products I test don't offer to help me write up my experience with them. Duet is different. Claude Duet is Anthropic's AI agent for cons
- [Israel’s VCs see opportunity for challengers in Nvidia’s turmoil](https://techcrunch.com/2026/11/13/israels-vcs-see-opportunity-for-challengers-in-nvidias-turmoil/) — 来源：TechCrunch AI（发布于 11-13 20:52）
  - 简介：Given Nvidia’s stronghold on AI and its importance in Israel, many in the country's startup ecosystem are worried about the impact of his departure.
- [Jensen Huang didn’t show confidence in his successor, report says](https://techcrunch.com/2026/11/13/jensen-huang-didnt-show-confidence-in-his-successor-report-says/) — 来源：TechCrunch AI（发布于 11-13 20:28）
  - 简介：Huang described Kress as a "deer in the headlights" during a meeting in summer.
- [Let’s talk about Jensen Huang’s many affairs!](https://www.theverge.com/ai-artificial-intelligence/1032339/lets-talk-about-the-nvidia-shitshow) — 来源：The Verge AI（发布于 11-13 20:00）
  - 简介：Usually, we'd be offering to answer your questions about a news event, but honestly we don't really have any answers about what the hell is going on o
- [［AINews］ Jensen Huang resigns after 33 years leading NVIDIA](https://latent.space/p/ainews-jensen-huang-resigns-after-33-years-leading-nvidia/) — 来源：Latent Space（含每天的 AINews：汇总推特、Reddit、Discord 的讨论）（发布于 11-13 17:04）
  - 简介：Congrats to Gemini 4 Hydrogen on their launch and it seems Anthropic’s IPO is well under way, but today’s headline was only ever going to be about one
- [黄仁勋辞职，英伟达33年首换帅，市值蒸发超3万亿](https://www.qbitai.com/2026/11/509995.html) — 来源：量子位（发布于 11-13 17:02）
  - 简介：一个时代结束了
- [MEET2027含金量再加码：AI4S/量子计算/AI Infra…第二批嘉宾强势来袭！](https://www.qbitai.com/2026/11/509827.html) — 来源：量子位（发布于 11-13 15:51）
  - 简介：12.9 北京，来MEET2027现场
- [中国AI突破复杂肺癌诊疗！中美医疗圈集体坐不住了](https://www.qbitai.com/2026/11/509796.html) — 来源：量子位（发布于 11-13 15:43）
  - 简介：250名国内顶尖三甲医院医生联合评测
