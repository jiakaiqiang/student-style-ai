# Python 后端 RAG + Agent + MCP + Skill 最小闭环 Demo

这个 demo 用于实战学习：

- 后端：FastAPI
- Agent：LangChain `create_agent`
- 模型：Ollama 本地模型
- RAG：LangChain `InMemoryVectorStore` + Ollama Embeddings
- MCP：`mcp.server.fastmcp.FastMCP`
- Skill：一个可复用的 Python 学习建议函数，并通过 MCP 暴露给 Agent

## 1. 闭环结构

```text
用户 HTTP 请求
  -> FastAPI /ask
  -> LangChain Agent
  -> MCP Client
  -> MCP Server Tools
     -> rag_search: 本地知识库检索
     -> learning_skill: 学习闭环建议
  -> Agent 汇总工具结果
  -> FastAPI 返回答案
```

## 2. 准备 Ollama

先启动 Ollama，然后拉取模型：

```powershell
ollama pull llama3.1
ollama pull nomic-embed-text
```

如果机器配置较低，可以换小模型：

```powershell
$env:OLLAMA_CHAT_MODEL="qwen2.5:3b"
ollama pull qwen2.5:3b
```

## 3. 安装依赖

在项目根目录运行：

```powershell
cd d:\demo\agentlearn-other
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .\rag_mcp_skill_demo\requirements.txt
```

## 4. 启动后端

```powershell
uvicorn rag_mcp_skill_demo.backend:app --reload --port 8000
```

打开健康检查：

```text
http://127.0.0.1:8000/health
```

FastAPI 自动文档：

```text
http://127.0.0.1:8000/docs
```

## 5. 发送请求

PowerShell 示例：

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri http://127.0.0.1:8000/ask `
  -ContentType "application/json" `
  -Body '{"question":"RAG、Agent、MCP 和 Skill 是怎么形成闭环的？"}'
```

CLI 示例：

```powershell
python -m rag_mcp_skill_demo.client_cli "我该怎么学习 LangChain Agent？"
```

## 6. 建议你动手改的地方

1. 修改 `data/knowledge.md`，添加你自己的知识点。
2. 修改 `mcp_server.py` 中的 `chunk_size` 和 `chunk_overlap`，观察检索质量变化。
3. 修改 `/ask` 的问题，让 Agent 同时调用 `rag_search` 和 `learning_skill`。
4. 增加一个新的 MCP tool，例如 `python_quiz_skill(topic: str)`。
5. 把 `InMemoryVectorStore` 替换成 Chroma、Qdrant 或 pgvector。

## 7. 文件说明

- `backend.py`：FastAPI 后端和 LangChain Agent。
- `mcp_server.py`：MCP server，暴露 RAG 工具和 Skill 工具。
- `data/knowledge.md`：最小知识库。
- `client_cli.py`：命令行测试客户端。
- `requirements.txt`：依赖列表。

## 8. 常见问题

### 依赖报错：找不到 langchain_mcp_adapters

运行：

```powershell
pip install -r .\rag_mcp_skill_demo\requirements.txt
```

### Ollama 连接失败

确认 Ollama 正在运行：

```powershell
ollama list
```

确认模型已下载：

```powershell
ollama pull llama3.1
ollama pull nomic-embed-text
```

### 第一次请求很慢

正常。第一次请求会：

1. 启动 MCP 子进程。
2. 加载知识库。
3. 调用 Embedding 模型构建内存向量索引。
4. 调用 Chat 模型生成答案。
