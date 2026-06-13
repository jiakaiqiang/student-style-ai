"""FastAPI backend that drives a LangChain agent with Ollama and MCP tools.

启动命令：

    uvicorn rag_mcp_skill_demo.backend:app --reload --port 8000

请求示例：

    POST http://127.0.0.1:8000/ask
    {"question": "RAG、Agent、MCP 和 skill 是怎么闭环的？"}

学习重点：
1. FastAPI 提供后端 HTTP 接口。
2. LangChain create_agent 创建会用工具的 Agent。
3. ChatOllama 连接本地 Ollama chat 模型。
4. langchain-mcp-adapters 把 MCP tools 转成 LangChain tools。
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent
MCP_SERVER_FILE = BASE_DIR / "mcp_server.py"

# 延伸知识点：
# - 默认模型名可以按你的 Ollama 本地模型调整。
# - 例如：llama3.1、qwen2.5:7b、qwen2.5:3b、mistral 等。
# - temperature 越低，输出越稳定；越高，表达越发散。
OLLAMA_CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.1")

SYSTEM_PROMPT = """你是一个 Python 后端、RAG、Agent、MCP、Skill 学习教练。

回答要求：
1. 优先调用可用工具获取上下文，尤其是涉及 RAG、Agent、MCP、Skill 概念时。
2. 回答要面向实战学习，解释清楚“输入 -> 处理 -> 输出”。
3. 如果工具返回了资料，请用自己的话总结，不要机械复制。
4. 如果用户问如何继续学习，请调用 learning_skill 给出练习闭环。
"""

app = FastAPI(title="RAG Agent MCP Skill Demo")


class AskRequest(BaseModel):
    """HTTP request body for /ask.

    延伸知识点：
    - Pydantic 负责请求数据校验。
    - 后端 API 不要直接接收裸 dict，显式 schema 更容易维护和生成文档。
    """

    question: str = Field(..., min_length=1, description="用户问题")


class AskResponse(BaseModel):
    """HTTP response body for /ask."""

    answer: str
    model: str


def mcp_config() -> dict[str, Any]:
    """Return MCP server config consumed by MultiServerMCPClient.

    延伸知识点：
    - 这里使用 stdio transport，后端会自动启动 mcp_server.py。
    - 多个 MCP server 可以同时注册，例如 filesystem、database、browser。
    - MCP 让工具边界更清楚：后端不需要知道工具内部怎么实现。
    """

    return {
        "rag_skill": {
            "command": sys.executable,
            "args": [str(MCP_SERVER_FILE)],
            "transport": "stdio",
        }
    }


async def run_agent(question: str) -> str:
    """Create tools from MCP, run the LangChain agent, and return final text.

    延伸知识点：
    - 为了让 demo 更容易理解，这里每次请求都创建一次 MCP client 和 agent。
    - 生产环境可以在应用启动时缓存 agent/tools，降低延迟。
    - Agent 的中间工具调用可以接入 LangSmith 或日志系统做可观测性。
    """

    client = MultiServerMCPClient(mcp_config())
    tools = await client.get_tools()

    model = ChatOllama(model=OLLAMA_CHAT_MODEL, temperature=0)
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": question}]}
    )

    # create_agent 返回的是消息列表，最后一条通常就是最终回答。
    final_message = result["messages"][-1]
    content = getattr(final_message, "content", str(final_message))
    return content if isinstance(content, str) else str(content)


@app.get("/health")
async def health() -> dict[str, str]:
    """Simple health check.

    延伸知识点：
    - 健康检查接口适合给 Docker、Kubernetes、负载均衡器探活。
    - 这里不检查 Ollama，是为了保持 health 轻量。
    """

    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
async def ask(payload: AskRequest) -> AskResponse:
    """Ask the agent a question and get a learning-oriented answer."""

    answer = await run_agent(payload.question)
    return AskResponse(answer=answer, model=OLLAMA_CHAT_MODEL)
