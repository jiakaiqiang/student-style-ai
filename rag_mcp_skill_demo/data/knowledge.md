# Python Agent 学习小知识库

## RAG 是什么

RAG 的全称是 Retrieval-Augmented Generation，中文常翻译为“检索增强生成”。
它的核心思想是：不要只依赖大模型参数中的记忆，而是在回答问题前，先从外部知识库中检索相关资料，
再把检索结果作为上下文交给大模型生成答案。

一个最小 RAG 流程通常包含：

1. 文档加载：读取 Markdown、PDF、网页、数据库记录等资料。
2. 文档切分：把长文档拆成较短的 chunk，方便向量化和召回。
3. 向量化：使用 Embedding 模型把文本转换为向量。
4. 向量存储：把向量和原文保存到向量数据库或内存索引。
5. 检索：根据用户问题查找最相似的 chunk。
6. 生成：把检索到的内容交给 LLM，生成最终答案。

## Agent 是什么

Agent 可以理解为“会使用工具的大模型应用”。
普通 LLM 调用通常是：用户提问，模型直接回答。
Agent 调用则是：用户提问，模型先判断是否需要工具，必要时调用检索、计算器、数据库、MCP 工具等，
再根据工具结果继续推理并回答。

Agent 的关键学习点：

1. 模型负责推理和决策。
2. Tool 负责执行确定性的外部动作。
3. Prompt 负责约束角色、边界和输出风格。
4. Trace 或日志负责观察 Agent 的中间过程。

## MCP 是什么

MCP 的全称是 Model Context Protocol。
它是一种让模型应用连接外部工具和上下文服务的协议。
可以把 MCP server 理解为“工具提供方”，把 LangChain 后端理解为“工具使用方”。

在这个 demo 中：

1. MCP server 暴露 `rag_search` 工具，用于查询本地知识库。
2. MCP server 暴露 `learning_skill` 工具，用于生成结构化学习建议。
3. LangChain agent 通过 MCP adapter 获取这些工具。
4. FastAPI 后端提供 HTTP 接口，把用户问题交给 Agent。

## Skill 是什么

这里的 skill 指一个可复用的任务能力，不一定必须是大模型。
在工程里，skill 常常是一个普通 Python 函数、一个工作流、一个 prompt 模板，或者一个外部服务。

好 skill 的特点：

1. 输入清晰：例如 topic、level、goal。
2. 输出稳定：例如固定返回学习步骤、注意事项、练习任务。
3. 可被工具化：可以包装为 LangChain Tool、MCP Tool、HTTP API。
4. 可测试：即使不用大模型，也能验证输入输出是否合理。

## Ollama 在本 demo 中的角色

Ollama 负责本地运行模型。
本 demo 使用两类模型：

1. Chat 模型：例如 `llama3.1`，负责 Agent 推理和最终回答。
2. Embedding 模型：例如 `nomic-embed-text`，负责把知识库文本变成向量。

如果你的机器性能有限，可以换成更小的 chat 模型，例如 `qwen2.5:3b`。
Embedding 模型通常比 Chat 模型更轻量。
