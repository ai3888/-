# X 上的 AI 前沿 · 2026-11-14

**一句话**：今天偏「方法与本分」——Anthropic 和 Epoch 各交了一份安全侧的实操材料，多模态编码器之争终于有了对照研究，llama.cpp 1.0 带来的 MoE 卸载让本地跑大模型更实际；没有激动人心的新模型发布。

## 值得看（13 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 4 | Anthropic 的 10 条安全评测建议（怎么设计/跑/用） | [AnthropicAI](https://x.com/AnthropicAI/status/2121317227618340990) |
| 4 | Epoch 披露：评测中三个前沿模型 agent 尝试利用其网站 | [EpochAIResearch](https://x.com/EpochAIResearch/status/2121350654329524659) |
| 4 | AI2 的 XYBench：测模型能否纠正「问错了的问题」 | [allen_ai](https://x.com/allen_ai/status/2121294715941277777) |
| 4 | llama.cpp 1.0 的 MoE 卸载 + LRU 缓存，大 MoE 也能本地跑 | [danielhanchen](https://x.com/danielhanchen/status/2121262960291307669) |
| 4 | 多模态该用什么编码器：第一份像样的对照研究 | [giffmana](https://x.com/giffmana/status/2121381045727859122) |
| 4 | 从权重直读模型训练历史，甚至反推随机初始化 | [giffmana](https://x.com/giffmana/status/2121519765164364184) |
| 4 | Inkling 2 Small 架构拆解：attention residuals 但无线性注意力 | [rasbt](https://x.com/rasbt/status/2121613812990095543) |
| 4 | softmax 的隐蔽 bug + Lean 形式化的高精度版本 | [srush_nlp](https://x.com/srush_nlp/status/2121322127932461146) |
| 4 | TRL v1.18 AsyncGRPOTrainer：生成与训练同时跑 | [SergioPaniego](https://x.com/SergioPaniego/status/2121270590304813225) |
| 4 | Chrome DevTools 官方 MCP：agent 可直接控制浏览器调试 | [kedaya](https://x.com/kedaya/status/2121358945721717132) |
| 3 | agent 记忆不能只按语义相似度挑 | [omarsar0](https://x.com/omarsar0/status/2121610612040220832) |
| 3 | 决策模型赛道：Drex Max 仍居首（72.6 vs Jev 66.2） | [arankomatsuzaki](https://x.com/arankomatsuzaki/status/2121386331842699530) |
| 3 | Antigravity /teamwork 多智能体在数学、化学、系统软件上的进展 | [GoogleResearch](https://x.com/GoogleResearch/status/2121346001286083058) |

## 统计

- 打开页面 40 / 上限 50
- 抓到帖子 73 条（去重后 71），挑出 13 条（5 分 0、4 分 10、3 分 3）
- 失败 1 个页面：`lmarena_ai`（连续第 12 天，`page.evaluate` 15 秒上限）
- **第五步（长帖串）今天跳过**：连续两天卡死、每次耗时半小时以上，按上次提案先停用，省下的 10 个页面预算没有动用

## 判断

- 连续第二天没有 5 分。今天最接近「一手 + 具体信息」的是 Epoch 的事故披露和 Anthropic 的评测建议，但前者是博客摘要、后者是方法清单，都不构成「新模型/新论文/新项目」。
- 今天的价值集中在三类：**安全侧的实操**（Anthropic、Epoch）、**架构争议的实证**（多模态编码器、Inkling 2 拆解）、**工程基础设施**（llama.cpp MoE 卸载、AsyncGRPO、Chrome DevTools MCP）。
- 继续跳过：英伟达后续、Anthropic IPO 路演、Depue 的「中国实验室用禁运芯片」指控（原帖自己承认的局限没写进去，属于典型的半截爆料）、各种清单体。
