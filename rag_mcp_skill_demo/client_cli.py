"""Small CLI client for the backend.

用法：

    python -m rag_mcp_skill_demo.client_cli "RAG 和 MCP 怎么配合？"

延伸知识点：
- 后端 demo 最好同时提供 HTTP API 和一个最小客户端。
- 客户端可以帮助你快速验证接口，不必每次都打开 Postman。
"""

from __future__ import annotations

import sys

import requests


def main() -> None:
    question = " ".join(sys.argv[1:]).strip()
    if not question:
        question = "RAG、Agent、MCP、Skill 在这个 demo 中如何形成闭环？"

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question},
        timeout=120,
    )
    response.raise_for_status()
    print(response.json()["answer"])


if __name__ == "__main__":
    main()
