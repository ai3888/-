# X 上的 AI 前沿 · 2026-11-04

**一句话**：今天没有「必读」级别的发布，主线分成三股——让模型自己干活的实操（Mistral 133 个 agent 打 CVE、OpenAI 用 Astra 一周做硬件原型）、把记忆和 harness 拆出来单独优化、以及几个新的评测暴露「该停不停」这类笨问题。

## 值得看（14 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 4 | Anthropic FlashProve：用密码学证明回复真出自某个模型 | [AnthropicAI](https://x.com/AnthropicAI/status/2117710942826123294) |
| 4 | 133 个 agent 在 Django CVE 上 triage→复现→打补丁 | [MistralAI](https://x.com/MistralAI/status/2117925908572991748) |
| 4 | GPT-6 Astra 一周设计出 Codex 原型硬件（外壳/电路/软件） | [OpenAI](https://x.com/OpenAI/status/2117692477947641954) |
| 4 | NVIDIA：频繁上下文压缩几乎不伤长序列准确率 | [omarsar0](https://x.com/omarsar0/status/2117956281910829083) |
| 4 | Living Brain：记忆从模型剥离，多处共用，LoCoMo 92.2% | [omarsar0](https://x.com/omarsar0/status/2117983990099452018) |
| 4 | harness 优化：成本偏好只放在搜索最后一步 | [omarsar0](https://x.com/omarsar0/status/2117738094069944347) |
| 4 | Revolut 把 2000 名工程师切到自托管 GLM | [omarsar0](https://x.com/omarsar0/status/2117709046291517443) |
| 4 | AI2 StateBench：状态追踪 4 个难度等级 | [allen_ai](https://x.com/allen_ai/status/2117670296647823731) |
| 4 | 10 月 10 个开放 LLM 架构盘点（Open October） | [rasbt](https://x.com/rasbt/status/2117637894315626719) |
| 4 | 字节 Recycler：隐藏状态回收做零成本潜推理 | [JohnCLangford](https://x.com/JohnCLangford/status/2117758072693150152) |
| 4 | DR Pixel：不靠 OCR 的 deep research agent，27B 追平 GPT-5.4 | [Hughie_Hu43](https://x.com/Hughie_Hu43/status/2117609678985392209) |
| 4 | TQ_L 量化比上一版更接近 BF16，只多 0.2GB | [coffeecup2020](https://x.com/coffeecup2020/status/2117601437202989238) |
| 4 | AA-Robotics：「任务做完不知道停」，Opus 5.5 多推 22 分钟 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2117786852375814228) |
| 3 | 腾讯 Hy4 发布，官方称将开源权重 | [testingcatalog](https://x.com/testingcatalog/status/2117885727354548370) |

## 统计

- 打开页面 45 / 上限 50
- 抓到帖子 84 条，挑出 14 条（5 分 0、4 分 13、3 分 1）
- 失败 1 个页面：`lmarena_ai`（连续第 6 天，`page.evaluate` 15 秒上限）
- 另两个页面首轮 `goto` 超时（`EpochAIResearch`、`ArtificialAnlys`），重试后成功，其中 Epoch 今天没有 30 小时内的新帖

## 判断

- 今天**没有给 5 分**：最接近的是 Mistral 的 CVE 演示和 Anthropic 的 FlashProve，但前者是演示不是发布、后者没给数字和可用产物，按标准都停在 4 分。
- 一天里 5 条来自同一个账号（omarsar0）容易让人觉得偏食，但内容确实各不相同（论文、产品、工程实践、行业数据），我按内容收、没按人头配额。
- 「agent 干完活不知道停」这条（AA-Robotics）我觉得比很多模型发布更有信息量，因为它指向的是 harness 设计而不是模型能力。
