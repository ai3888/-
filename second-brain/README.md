# 第二大脑

把你和各个 AI 的聊天记录存成一个属于自己的记忆库：每段对话都存下来，按主题整理成分支，再写一份「关于我」。换一个 AI、或者用 API 接新模型时，先让它读 `memory/index.md`，它就知道你是谁、聊过什么，不用你从头解释。

记忆库就是一堆 Markdown 文件，不绑定任何一家 AI，谁都能读。

## ⚠️ 只能放在私有仓库

记忆库里是你全部的私人聊天。这个文件夹所在的「项目雷达」仓库是**公开的**，所以：

- 这里只放代码。`memory/` 和 `inbox/` 在这个仓库里被 `.gitignore` 忽略，不会被提交
- 真正使用时，新建一个**私有**仓库，把这个文件夹里的全部文件（包括 `.github` 和 `inbox`）放到新仓库的根目录。自带的 GitHub Actions 发现仓库是公开的会直接停下，不会处理任何聊天记录

## 怎么运作

```
inbox/                    ← 你放进来的导出文件
  │  python memory.py import inbox
  ▼
memory/conversations/     每段对话一个 Markdown（原文，按来源和月份分文件夹）
  │  python memory.py organize   GPT 给每段对话写一句话摘要和要点、归到分支、记下关于你的信息
  ▼
memory/index.md           入口：给 AI 的说明 + 关于我 + 所有分支（每个附一句话）
memory/profile.md         关于我：基本情况、在做的事、常用工具、偏好、目标、不喜欢的
memory/branches/          每个分支一个文件：分支总结 + 每段对话的摘要和原文链接
```

AI 读的时候一层层往下：先读 `index.md`（几千字），需要细节再读某个分支，还要更细才读原文。token 只花在用得上的地方。

## 开始使用

1. **新建私有仓库**：GitHub 右上角 + → New repository，名字比如 `memory`，一定选 **Private**。把这个文件夹里的文件放进去（也可以让 Claude 帮你建好）
2. **配置模型**（和项目雷达一样）：新仓库 Settings → Secrets and variables → Actions
   - Secrets 里添加 `OPENAI_API_KEY`
   - Variables 里可以添加 `OPENAI_MODEL`（默认 `gpt-4o-mini`）和 `OPENAI_BASE_URL`（用中转或国内模型时填）
   - 不配置也能用，只存原文，不整理分支
3. **导出聊天记录**：

   | 来源 | 怎么导出 | 放进 inbox 的文件 |
   |---|---|---|
   | ChatGPT | Settings → Data controls → Export data，邮件里下载 zip | zip，或者里面的 `conversations.json` |
   | Claude | Settings → Privacy → Export data，邮件里下载 zip | zip，或者里面的 `conversations.json` |
   | 自己用 API 聊的 | 存成 OpenAI 消息格式（见下方） | `.json` 或 `.jsonl` |
   | 其他 AI（DeepSeek、Kimi、豆包……） | 把对话复制下来 | 一段对话一个 `.md` 或 `.txt`，第一行 `# 标题` |

4. **上传**：打开新仓库的 `inbox` 文件夹 → Add file → Upload files。网页上传单个文件最大 25MB，导出的 zip 太大时，解压后只把 `conversations.json` 重新压缩成 zip 再传（纯文字压缩后会小很多）
5. **等几分钟**：Actions 自动导入、整理，原文件删掉，结果提交到 `memory/`。第一次对话多的话，每次最多整理 300 段，剩下的每天凌晨接着整理，也可以在 Actions 页面手动点 Run workflow

以后定期（比如每月）再导出一次、上传一次就行。导出文件里是全部历史，已经存过的会自动跳过；之前的对话后来又聊了新内容，会更新原文并重新整理。

## 让 AI 读你的记忆

- **能调用网络 API 的**（GPTs 的 Action、Agent、自己写的程序）：建一个只读 token：GitHub 头像 → Settings → Developer settings → Fine-grained tokens → Generate new token，Repository access 只选这个私有仓库，Permissions 里 Contents 选 Read-only。然后：

  ```
  GET https://api.github.com/repos/<你的用户名>/<仓库名>/contents/memory/index.md
  Authorization: Bearer <token>
  Accept: application/vnd.github.raw
  ```

  分支和原文同理，把路径换成 `memory/` 加上 `index.md` 里的链接。
- **ChatGPT / Claude 的项目（Projects）**：把 `index.md` 和 `profile.md` 上传成项目文件。
- **任何 AI，复制粘贴**：`python memory.py context 关键词`，会打印 `index.md` 加上和关键词相关的分支，贴到对话开头。
- **用 API 接新模型**：把 `index.md` 的内容放进 system prompt。

token 就是你全部记忆的钥匙：只给只读权限、只选这一个仓库，不要贴到公开的地方。

## 自己用 API 聊天的记录格式

```json
[
  {
    "id": "可选，同一段对话保持不变，再导入时会更新原来那段",
    "title": "标题",
    "messages": [
      {"role": "user", "content": "……"},
      {"role": "assistant", "content": "……"}
    ]
  }
]
```

`.jsonl` 每行一段也可以。

## 在自己电脑上运行

需要 Python 3.11 或更高版本，不用安装任何依赖：

```bash
export OPENAI_API_KEY=sk-...                       # 可选，不设置就只存原文
python3 memory.py import ~/Downloads/chatgpt.zip   # 也可以是文件夹
python3 memory.py organize
python3 memory.py context 投资 美股 > 给AI的背景.txt
```

## 说明

- 整理时，对话内容会发给你配置的模型服务。不想发出去就不配置 key，只存原文。
- ChatGPT、Claude 的网页版和 App 没有提供读取聊天记录的接口，没法每聊一句就自动存进来，目前只能定期导出。
- 分支的大类在 `memory.toml` 的 `suggested_branches` 里改。改完想把所有对话重新归类：`python memory.py organize --redo`。
- 认不出来的导出文件会在运行日志里提示，原文件留在 `inbox/` 不删。
