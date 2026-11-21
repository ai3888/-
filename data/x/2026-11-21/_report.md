# X 上的 AI 前沿 · 2026-11-21

**一句话**：OpenAI 一天甩出三份硬材料（AI 参与提出药物机制假设、反蒸馏研究、药物化学基准），Thinking Machines 的 Inkling 2 Mini 把「开放权重 + 小激活」推到新位置；另外今天有一条关于黎曼假设的爆炸性传闻，但我不建议当事实看。

## 值得看（13 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | GPT-Rosalind 提出药物方向：恢复胆固醇运输阻止神经元退化，小鼠实验支持 | [OpenAI](https://x.com/OpenAI/status/2123899406550528422) |
| 4 | Inkling 2 Mini：26B/5.4B 激活，超过 5~6 倍大的开放模型 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123877871316087012) |
| 4 | OpenAI 反蒸馏研究：能力能被复制但安全措施不能 | [OpenAI](https://x.com/OpenAI/status/2123862344422088794) |
| 4 | MedChemBench：药物化学推理新基准 | [OpenAI](https://x.com/OpenAI/status/2123856316187975756) |
| 4 | Drex Router 实测：1:19 vs 2:42、$0.57 vs $0.91 | [arankomatsuzaki](https://x.com/arankomatsuzaki/status/2123891222326739264) |
| 4 | AA-Robotics 新维度：Astra 只用 92 条指令，少 75% | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2123866468156854664) |
| 4 | 腾讯 Hy4 系统卡带第三方失控风险评估 | [NeelNanda5](https://x.com/NeelNanda5/status/2123889182301139248) |
| 4 | 自我改进 harness 的反直觉结论：改 prompt 掉分，改代码升分 | [tdualdir](https://x.com/tdualdir/status/2124054720222535986) |
| 4 | Jeveration：78ms 一次前向直接出 512×512 图 | [carol00892](https://x.com/carol00892/status/2123808797009543293) |
| 4 | ERMoE：MoE 不需要学 router，用正交本征基直接对齐 | [peony__snow](https://x.com/peony__snow/status/2123740591981052199) |
| 4 | SMELT：对齐 FLOPs/参数/KV cache 后，循环 Transformer 到底有没有用 | [peony__snow](https://x.com/peony__snow/status/2123708176319279467) |
| 4 | Inkling 2 Mini 本地跑：16GB 内存、DeepSWE 48.2% | [UnslothAI](https://x.com/UnslothAI/status/2123873656069877899) |
| 4 | harness 是训练设置的一部分，模型吸收不了它 | [rasbt](https://x.com/rasbt/status/2123853084216455549) |

## 统计

- 打开页面 40 / 上限 50
- 抓到帖子 102 条，挑出 13 条（5 分 1、4 分 12、3 分 0）
- 失败 1 个页面：`lmarena_ai`（连续第 19 天，`page.evaluate` 15 秒上限）
- 第五步（长帖串）继续跳过

## 判断

- **关于「黎曼假设被解决」的传闻**：今天多条帖子在传「Anthropic 的数学家 @__alpoge__ 用 Claude 证出黎曼假设」，fchollet、reach_vb、DrJimFan 都在转。我**没有把它写进 `_picks.json`**——目前只有当事人一句「我认为我找到了证明」，没有论文、没有同行复核，正是 `x_task.md` 里点名要排除的「说不出来源的重磅爆料」。这类消息如果之后被证实，值得单独拿出来讲；现在按传闻处理。
- 今天真正扎实的是 OpenAI 那三条：一条是 AI 参与提出机制假设并有小鼠数据，一条是反蒸馏这种很少公开的安全工作，一条是领域基准。三条都有一手材料和具体内容。
- Inkling 2 Mini 值得留意：26B 总参、5.4B 激活就能压过 27B~33B 的开放模型，说明「小激活 + 循环结构」这条路开始出成果。
