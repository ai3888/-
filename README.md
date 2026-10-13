# GitHub 项目雷达

每天自动在 GitHub 上找「有潜力」和「值得关注」的开源项目，结果写在 [`reports/latest.md`](reports/latest.md)，历史报告按日期存在 `reports/` 里。

## 判断标准

先用代码按客观数据打分（满 100 分），再让 GPT 看入选的项目做最后判断。

| 维度 | 权重 | 看什么 |
|---|---|---|
| 涨星速度 | 40 | 最近每天涨多少星，按最近加星的时间算，不是总星数 |
| 开发活跃度 | 20 | 近 30 天提交数、最近一周有没有更新 |
| 社区 | 20 | 贡献者人数、fork 数占星数的比例（有人真的在用、在改） |
| 规范度 | 20 | 有没有许可证、topics、主页、正式发版 |

- **🚀 潜力股**：创建不超过 90 天，分数 ≥ 55
- **👀 值得关注**：不限创建时间，分数 ≥ 65
- **直接排除**：fork 来的、已归档的、没有简介的、30 天没更新的、awesome 列表、教程、面试题
- **风险提示（每条扣 10 分）**：星很多但几乎没人 fork（可能刷星）；只有一个人维护且近 30 天几乎没提交
- **GPT 复核**：看 README 判断是不是真有新意、是不是套壳或营销、和你关注的方向是否相关，给出「推荐 / 一般 / 跳过」
- **不重复推荐**：推荐过的项目 14 天内不再出现

这些数值都能在 [`config.toml`](config.toml) 里改。

## 为什么这样分工能省 token

搜索、过滤和打分都由代码完成，不花 token。每天只有最后入选的十几个项目，以精简数据加每个约 1500 字 README 的形式，一次性交给 GPT。每次大约几千 token，用量会写在报告底部。

## 开始使用

1. **（可选）配置 GPT**：仓库 Settings → Secrets and variables → Actions：
   - Secrets 里添加 `OPENAI_API_KEY`
   - Variables 里可以添加 `OPENAI_MODEL`（模型名，默认 `gpt-4o-mini`）和 `OPENAI_BASE_URL`（使用中转服务时填写，例如 `https://xxx.com/v1`）
   - 不配置也能运行，只是没有 GPT 点评
2. **手动跑一次试试**：Actions → 项目雷达 → Run workflow。跑完后仓库里会多出 `reports/` 目录。
3. **之后每天北京时间 9 点多自动运行**。想在手机上收到提醒，就把 `config.toml` 里的 `create_issue` 改成 `true`，每次运行都会开一个 issue，GitHub App 和邮件会通知你。

如果第 2 步提交报告时报 403，到 Settings → Actions → General → Workflow permissions 选择「Read and write permissions」。

## 调整标准

都在 `config.toml` 里：

- `interests`：你关注的方向，GPT 按它判断相关度
- `[[queries]]`：去哪里找，写法和 GitHub 搜索框一样，比如 `language:rust topic:cli stars:>200`
- `[filters]`：排除哪些项目
- `[weights]` / `[full_marks]`：各维度的权重和满分标准
- `[tiers]`：分数线、每次最多推荐几个、冷却天数

刚开始可以先跑几天看看报告。推荐太多就提高分数线，太少就降低分数线或者加搜索条件。

## 和你现有的 GPT 配合

每天的筛选交给这里。你的 GPT 只需要读一个文件：

```
GET https://api.github.com/repos/<你的用户名>/<仓库名>/contents/reports/latest.md
Accept: application/vnd.github.raw
```

然后对感兴趣的项目再深入问，比如「第 2 个项目和 XX 比怎么样」。这样 token 花在你真正关心的项目上。

## 在自己电脑上运行

需要 Python 3.11 或更高版本，不用安装任何依赖：

```bash
export GITHUB_TOKEN=你的GitHub令牌     # 不设置也能跑，但 GitHub 限流很严
export OPENAI_API_KEY=sk-...           # 可选
python3 scout.py --dry-run             # 只打印报告，不写文件
```
