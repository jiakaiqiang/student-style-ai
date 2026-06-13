"""MCP server: exposes RAG and skill tools to the LangChain agent.

运行方式通常不是你手动启动，而是由 backend.py 通过 stdio 自动拉起：

    python rag_mcp_skill_demo/mcp_server.py

学习重点：
1. MCP server 是“工具提供方”。
2. Agent/backend 是“工具消费方”。
3. 工具内部可以是 RAG、数据库查询、业务规则、工作流、文件读写等。
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from mcp.server.fastmcp import FastMCP


BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_FILE = BASE_DIR / "data" / "knowledge.md"

# 延伸知识点：
# - Chat 模型和 Embedding 模型最好分开配置。
# - Chat 模型擅长生成文字，Embedding 模型擅长表达“语义相似度”。
# - Ollama 默认服务地址通常是 http://localhost:11434。
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

mcp = FastMCP("rag-mcp-skill-demo")


@lru_cache(maxsize=1)
def build_vector_store() -> InMemoryVectorStore:
    """Build an in-memory vector store from the local Markdown knowledge file.

    延伸知识点：
    - 真实项目中通常会把向量写入 Chroma、Milvus、Qdrant、pgvector 等持久化数据库。
    - 教学 demo 用 InMemoryVectorStore 更直观：每次启动重新构建，少一个外部依赖。
    - lru_cache 让本进程只构建一次索引，避免每次工具调用都重复向量化。
    """

    raw_text = KNOWLEDGE_FILE.read_text(encoding="utf-8")

    # Document 是 LangChain 对“带元数据文本”的统一表示。
    # metadata 可以保存来源、标题、页码、业务 id，方便回答时引用出处。
    document = Document(
        page_content=raw_text,
        metadata={"source": str(KNOWLEDGE_FILE.name)},
    )

    # RecursiveCharacterTextSplitter 会优先按段落、换行、句子边界切分。
    # chunk_size 太小：上下文不完整；太大：召回不精准、token 成本更高。
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=450,
        chunk_overlap=80,
    )
    chunks = splitter.split_documents([document])

    embeddings = OllamaEmbeddings(model=OLLAMA_EMBED_MODEL)
    return InMemoryVectorStore.from_documents(chunks, embeddings)


@mcp.tool()
def rag_search(query: str, k: int = 3) -> str:
    """Search the local Python agent knowledge base.

    Args:
        query: 用户问题或检索关键词。
        k: 返回最相似的片段数量，默认 3 条。

    延伸知识点：
    - 这个函数是一个 MCP Tool，Agent 可以决定什么时候调用它。
    - RAG 工具最好返回“可引用的原文片段”，不要在工具里过度生成。
    - 最终组织语言的工作交给 Agent/LLM，更容易保持职责清晰。
    """

    vector_store = build_vector_store()
    docs = vector_store.similarity_search(query, k=max(1, min(k, 5)))

    if not docs:
        return "没有检索到相关资料。"

    lines: list[str] = []
    for index, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        lines.append(f"[片段 {index} | 来源: {source}]\n{doc.page_content}")

    return "\n\n---\n\n".join(lines)


@mcp.tool()
def learning_skill(topic: str, level: str = "beginner") -> str:
    """Return a structured learning path for one backend/RAG/Agent/MCP topic.

    Args:
        topic: 想学习的主题，例如 RAG、Agent、MCP、Ollama、LangChain Tool。
        level: 学习者水平，例如 beginner、intermediate、advanced。

    延伸知识点：
    - Skill 不一定要调用大模型，也可以是确定性函数。
    - 稳定的 skill 更容易测试、复用和上线。
    - 当 skill 被 MCP 化以后，任何支持 MCP 的客户端都可以调用它。
    """

    normalized_level = level.lower().strip() or "beginner"
    return (
        f"学习主题: {topic}\n"
        f"学习阶段: {normalized_level}\n\n"
        "建议闭环:\n"
        "1. 先用自己的话解释这个概念，写下 3 个关键词。\n"
        "2. 阅读 demo 中对应代码注释，找到输入、处理、输出三件事。\n"
        "3. 改一个小参数并运行，例如 chunk_size、k、模型名称。\n"
        "4. 观察结果变化，记录为什么会变化。\n"
        "5. 给这个模块新增一个最小测试或一个新工具。\n\n"
        "练习任务:\n"
        f"- 为 `{topic}` 补充一段知识库文本。\n"
        "- 重新提问，观察 RAG 是否能召回你新增的内容。\n"
        "- 尝试让 Agent 同时调用 rag_search 和 learning_skill。"
    )


if __name__ == "__main__":
    # stdio 是最适合本地 demo 的 MCP transport：
    # backend 会把 MCP server 当成一个子进程启动，通过标准输入输出通信。
    mcp.run(transport="stdio")
