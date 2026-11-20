# X 上的 AI 前沿 · 2026-11-20

**一句话**：没有大模型发布，今天的好东西都在「怎么把事做对」——936 个 agent 自主产出的论文被系统审稿、Claude Code 团队重做代码审查、GUARD 解自我改进的遗忘问题、模型路由把成本砍到十分之一。

## 值得看（11 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 4 | 936 个 AI 自主做研究产出 936 篇论文：更严谨、但更不新颖 | [dotey](https://x.com/dotey/status/2123671858541187164) |
| 4 | Claude Code 团队如何重做代码审查（从人情互审到自动化） | [dotey](https://x.com/dotey/status/2123555597387813050) |
| 4 | Gemini 4 三代定位：Carbon 最贵最强物理，但长程任务不如 Neon/Hydrogen | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123513872095269336) |
| 4 | GUARD：冻结基础模型、只更新外围，治自我改进的遗忘与记忆污染 | [omarsar0](https://x.com/omarsar0/status/2123420538030957015) |
| 4 | Meta：用 agent 从自己的代码库自动构造编码评测 | [omarsar0](https://x.com/omarsar0/status/2123767076745818281) |
| 4 | Marin Mochi 技术报告：潜空间 MoE + 额外 RMSNorm，附 57 个 checkpoint | [rasbt](https://x.com/rasbt/status/2123433827234111659) |
| 4 | 腾讯 Hy4 旗舰开放权重：770B/49B、FP8 权重 786GB | [MiaAI_lab](https://x.com/MiaAI_lab/status/2123703921134747902) |
| 4 | Drex Router：按难度路由模型，做小游戏 $1.26 vs $13.44 | [testingcatalog](https://x.com/testingcatalog/status/2123531678878400758) |
| 4 | epiplexity：按泛化目标挑选与生成训练数据 | [ellensu35](https://x.com/ellensu35/status/2123440617560973468) |
| 4 | JEPA4R：在点云潜空间规划，Cube-Single 78.4% vs 46.8% | [HaoTang_ai](https://x.com/HaoTang_ai/status/2123542255487295814) |
| 3 | 实测反调：GPT-6.2 Sol 复杂编码还不如 Opus 5.5 | [dotey](https://x.com/dotey/status/2123676175021281770) |

## 统计

- 打开页面 40 / 上限 50
- 抓到帖子 93 条（去重 89），挑出 11 条（5 分 0、4 分 10、3 分 1）
- 失败 1 个页面：`lmarena_ai`（连续第 18 天，`page.evaluate` 15 秒上限）
- 第五步（长帖串）继续跳过

## 判断

- 今天没有 5 分：没有任何实验室发布带具体数字的新模型/论文；最接近的是 936-agent 实验（一手但作者是转述）和 Claude Code 的审查流程（一手但无量化）。
- 今天的主题其实是**「评估与流程」**：怎么给 agent 产出的研究打分、怎么从自己代码库造评测、怎么用路由把成本打下来、怎么让自我改进不遗忘。模型能力没大变化，但把这些做对能直接换来十倍成本差。
- 继续跳过：Anthropic 上市首日（$97.17 收盘）和 GPT-6.2 的口水战（只留了 dotey 那条有具体对比的实测）。
