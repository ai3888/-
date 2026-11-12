# X 上的 AI 前沿 · 2026-11-12

**一句话**：Google 一天发了两样东西（AlphaGenome 2 和首个决策模型 Gemini Decision 1），Anthropic 的产品线被评测数据反复拿来比对；真正有技术含量的是「细胞级基因模型」和「决策 API 的定价结构」，而不是社交媒体上刷屏的英伟达人事变动。

## 值得看（12 条）

| 分 | 内容 | 链接 |
|---|---|---|
| 5 | AlphaGenome 2：细胞级基因模型，1 亿+ 图谱 / 68 组织，可现场吸收新实验数据 | [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2120532824465805749) |
| 4 | Fable 5.2 登顶 AA-Robotics，首个靠纯视频完成「量箱子」的模型 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120698177016005029) |
| 4 | VIALS-AA：拿掉工具，强模型不如弱模型带工具；工具让均分 25%→47% | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120664556972257506) |
| 4 | 每美元智能：升档比拉满 effort 更划算 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120672485167497335) |
| 4 | Gemini Decision 1：Google 首个决策模型，Decision Index 66 分 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120582049522127205) |
| 4 | Gemini Decisions API：只给判断，$0.10/百万输入、输出免费 | [dotey](https://x.com/dotey/status/2120647659388031454) |
| 4 | Unsloth Dynamic V3.1：同尺寸 +5~10% 准确率，12GB 可跑 | [danielhanchen](https://x.com/danielhanchen/status/2120544760041730294) |
| 4 | Continual-ARC：三个主流 agent 都不会真正从经验学习 | [omarsar0](https://x.com/omarsar0/status/2120638750740844672) |
| 3 | Gemini 4 Carbon 在机器人实验室待了 7 小时 33 分，把夹爪弄坏 | [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2120729548719309223) |
| 3 | 可穿戴信号 →「可辅导的健康年龄」+ 12 周习惯模拟 | [GoogleResearch](https://x.com/GoogleResearch/status/2120613625186673087) |
| 3 | GR00T 2 实拍：自主做完化学实验并自己清理，不剪辑不加速 | [DrJimFan](https://x.com/DrJimFan/status/2120540201994846253) |
| 3 | AutoE2E：8000 万参数的开源端到端自动驾驶模型 | [ShinpeiKato](https://x.com/ShinpeiKato/status/2120498703828242816) |

## 统计

- 打开页面 42 / 上限 50
- 抓到帖子 72 条，挑出 12 条（5 分 1、4 分 7、3 分 4）
- 失败 1 个页面：`lmarena_ai`（连续第 10 天，`page.evaluate` 15 秒上限）
- 中途出过一次事故：首轮抓取卡在第 8 个页面近 50 分钟，我终止进程后用断点续跑完成，已抓到的 5 个页面没有重复打开

## 判断

- 今天社交层面最大的新闻是英伟达 CEO 变动（Jensen Huang 辞任、CFO 临时接任）和 Anthropic 的 IPO 时间表，但这两件事都没有技术信息、也不属于你配置的五个关注方向，所以我**没有收进 `_picks.json`**，只在报告里记一笔。
- AlphaGenome 2 给 5 分是因为它同时具备：一手发布、具体数据规模（1 亿+ 图谱、68 组织）、明确的方法改进（细胞级而非组织级）、可用的开放入口（API + Colab）。
- 今天 Artificial Analysis 发了 7 条评测数据，其中 4 条进了列表——这类「同一个机构把同一批模型翻来覆去测」的内容，信息密度确实高，但要注意它们的自家基准有立场。
