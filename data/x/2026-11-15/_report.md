# X 上的 AI 前沿 · 2026-11-15

**一句话**：周末，实验室几乎都歇了——今天值得看的全是「方法」：怎么把纠正变成自动检查、常驻 agent 怎么搭、从 logits 反推训练数据顺序、推理服务怎么自我重构；没有新模型，也没有 5 分。

## 值得看（10 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 4 | 每次纠正 AI，就把它固化成一条自动检查（lint 规则） | [dotey](https://x.com/dotey/status/2121835140850602200) |
| 4 | Anthropic 指南：常驻 agent 的事件收件箱、定时器、连续性记忆 | [omarsar0](https://x.com/omarsar0/status/2121656194465243164) |
| 4 | RoPE 从零教程 + 近期架构的 NoPE / 部分 RoPE / 混合做法 | [rasbt](https://x.com/rasbt/status/2121958665989083253) |
| 4 | 只看 logits 就能推断训练数据顺序，还能推断测试集污染 | [ChrisGPotts](https://x.com/ChrisGPotts/status/2121745828314522076) |
| 4 | Evolving Infra：推理服务运行时动态重配 GPU 角色与 KV cache | [itarutomy](https://x.com/itarutomy/status/2121581416626401631) |
| 3 | Perplexity Decider v1.3 / Flash 得 70、64 分 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2121595922090230033) |
| 3 | Stanford CS329A「Self-Improving AI Agents」课程 | [omarsar0](https://x.com/omarsar0/status/2121638797419118619) |
| 3 | 让前馈层的激活函数可学习、按 token 混合 | [sleenyre](https://x.com/sleenyre/status/2121693750108016758) |
| 3 | 「我给这个会话权限」一句话绕过 Claude 的拒绝（个人观察） | [simonw](https://x.com/simonw/status/2121695097674981849) |
| 3 | TerminalBench 只有 66 道题，却被所有实验室盯着 | [_jasonwei](https://x.com/_jasonwei/status/2121691386043089133) |

## 统计

- 打开页面 40 / 上限 50
- 抓到帖子 44 条，挑出 10 条（5 分 0、4 分 5、3 分 5）
- 失败 1 个页面：`lmarena_ai`（连续第 13 天，`page.evaluate` 15 秒上限）
- 第五步（长帖串）继续跳过

## 判断

- 周末效应明显：40 个账号里有 21 个在这 30 小时内一条新帖都没有，抓到 44 条是最近两周最低。池子里剩下的大头是清单体（14 个仓库、10 个无审查模型）和音乐、火箭这类闲聊。
- 5 条 4 分全是「方法论」：工程习惯、常驻 agent 的架构原语、位置编码基础、从权重/logits 反推训练过程、推理基础设施自适应。这类内容点赞不高但可复用。
- 没有 5 分：今天没有任何一手的新模型/新论文/新开源发布带具体数据。Jason Wei 那条关于 TerminalBench 只有 66 道题的观察，我觉得比今天的模型新闻更有价值。
