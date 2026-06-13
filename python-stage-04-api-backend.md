# 阶段 4：API 使用与后端服务基础

这一阶段的目标不是把你训练成传统后端工程师，而是让你具备开发 Agent / LLM 应用时最常用的 API 和服务能力。

你需要能看懂一个 API 怎么被调用，也能自己写一个简单后端接口。后续做 LLM SDK、工具调用、RAG、Agent 工作流时，几乎都会用到这些能力。

---

## 1. 为什么 Agent 开发需要 API 和后端基础

前端开发中，你经常会这样调用接口：

```js
const response = await fetch("/api/user")
const data = await response.json()
```

Agent 应用里也一样，只是调用方可能变成：

- Python 后端调用 LLM API；
- Agent 调用外部工具 API；
- 前端调用你写的 Agent 服务；
- 一个工具函数调用数据库、搜索服务、向量数据库或第三方平台；
- 多个服务之间传递结构化 JSON。

所以你要掌握三件事：

1. 如何理解 HTTP API；
2. 如何用 Python 调用 API；
3. 如何用 Python 写一个 API 服务。

---

## 2. HTTP 请求与响应

一个 HTTP 请求通常包含：

- URL：请求地址，例如 `https://api.example.com/users`
- Method：请求方法，例如 `GET`、`POST`、`PUT`、`DELETE`
- Headers：请求头，例如认证信息、内容类型
- Query Params：查询参数，例如 `?page=1&limit=10`
- Body：请求体，通常是 JSON

一个 HTTP 响应通常包含：

- Status Code：状态码，例如 `200`、`400`、`401`、`404`、`500`
- Headers：响应头
- Body：响应体，通常是 JSON

常见状态码：

| 状态码 | 含义 |
| --- | --- |
| `200` | 请求成功 |
| `201` | 创建成功 |
| `400` | 请求参数错误 |
| `401` | 未认证，例如 API Key 错误 |
| `403` | 没有权限 |
| `404` | 资源不存在 |
| `422` | 请求格式不符合数据模型，FastAPI 常见 |
| `500` | 服务内部错误 |

---

## 3. GET 和 POST 的区别

`GET` 常用于读取数据：

```text
GET /users/1
GET /search?q=python
```

特点：

- 通常没有请求体；
- 参数常放在 URL 查询参数里；
- 用于获取资源。

`POST` 常用于创建数据或提交复杂输入：

```text
POST /tasks
POST /chat
POST /agent/run
```

特点：

- 通常有 JSON 请求体；
- 用于提交结构化数据；
- Agent 应用中非常常见。

示例请求体：

```json
{
  "message": "帮我总结这段文本",
  "temperature": 0.7
}
```

---

## 4. 用 requests 调用 API

阶段 2 中你已经接触过 `requests`。这里把它放到 API 语境里重新理解。

GET 示例：

```python
import requests

response = requests.get("https://api.example.com/users/1")

print(response.status_code)
print(response.json())
```

POST 示例：

```python
import requests

payload = {
    "message": "hello",
    "user_id": "u_001"
}

response = requests.post(
    "https://api.example.com/chat",
    json=payload
)

print(response.status_code)
print(response.json())
```

重点：

- `json=payload` 会把 Python dict 作为 JSON 请求体发送；
- `response.json()` 会把 JSON 响应体解析成 Python 对象；
- `response.status_code` 用于判断请求是否成功。

---

## 5. API Key 与环境变量

调用真实服务时，经常需要 API Key。

不要这样写：

```python
api_key = "sk-xxxx"
```

应该使用环境变量：

```python
import os

api_key = os.getenv("MY_API_KEY")
```

请求时放到 headers：

```python
import os
import requests

api_key = os.getenv("MY_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://api.example.com/me",
    headers=headers
)

print(response.status_code)
print(response.json())
```

Agent 开发中，LLM API Key、数据库连接信息、第三方工具密钥都不应该写死在代码里。

---

## 6. 后端服务是什么

后端服务可以理解为：一组可被外部调用的函数，只是这些函数通过 HTTP 暴露出来。

普通 Python 函数：

```python
def add(a: int, b: int) -> int:
    return a + b
```

API 接口：

```text
POST /add
```

请求体：

```json
{
  "a": 1,
  "b": 2
}
```

响应体：

```json
{
  "result": 3
}
```

你可以把 API 理解成：

```text
HTTP 版本的函数调用
```

这对 Agent 工具调用非常重要，因为很多工具本质上就是“可被模型或系统调用的函数”。

---

## 7. FastAPI 入门

FastAPI 是 Python 中常用的 Web API 框架。它适合写结构清晰、类型友好、文档自动生成的 API 服务。

最小示例：

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello api"}
```

保存为 `main.py` 后，可以运行：

```bash
uvicorn main:app --reload
```

含义：

- `main`：文件名 `main.py`
- `app`：文件里的 FastAPI 实例
- `--reload`：代码修改后自动重启，适合开发环境

浏览器访问：

```text
http://127.0.0.1:8000
```

自动文档：

```text
http://127.0.0.1:8000/docs
```

---

## 8. 路径参数

路径参数来自 URL 路径。

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Alice"
    }
```

访问：

```text
GET /users/1
```

返回：

```json
{
  "user_id": 1,
  "name": "Alice"
}
```

注意：`user_id: int` 表示 FastAPI 会尝试把路径里的值转换成整数。

---

## 9. 查询参数

查询参数来自 URL 的 `?` 后面。

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
def search(q: str, limit: int = 10):
    return {
        "query": q,
        "limit": limit,
        "items": []
    }
```

访问：

```text
GET /search?q=python&limit=5
```

返回：

```json
{
  "query": "python",
  "limit": 5,
  "items": []
}
```

如果参数有默认值，例如 `limit: int = 10`，调用时可以不传。

---

## 10. 请求体与 Pydantic

POST 请求通常需要请求体。FastAPI 使用 Pydantic 定义请求体结构。

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "user_id": request.user_id,
        "reply": f"收到：{request.message}"
    }
```

请求：

```json
{
  "user_id": "u_001",
  "message": "你好"
}
```

响应：

```json
{
  "user_id": "u_001",
  "reply": "收到：你好"
}
```

Pydantic 的作用：

- 定义字段名；
- 定义字段类型；
- 自动校验请求体；
- 自动生成 API 文档；
- 让接口输入更清晰。

---

## 11. 响应模型

除了请求体，响应体也可以定义结构。

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    user_id: str
    reply: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return {
        "user_id": request.user_id,
        "reply": f"收到：{request.message}"
    }
```

`response_model` 的好处：

- 明确响应格式；
- 帮你过滤多余字段；
- 自动生成更准确的接口文档；
- 后续前端或 Agent 调用时更容易对接。

---

## 12. 错误处理

当请求不合法时，不应该只返回普通字符串，而应该返回明确的 HTTP 错误。

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str


users = {
    1: User(id=1, name="Alice"),
    2: User(id=2, name="Bob")
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = users.get(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
```

访问不存在的用户：

```text
GET /users/999
```

响应状态码是 `404`，而不是 `200`。

这很重要，因为调用方通常通过状态码判断是否成功。

---

## 13. 前端如何调用你的 FastAPI 服务

前端调用方式和你熟悉的接口调用一样。

```js
const response = await fetch("http://127.0.0.1:8000/chat", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    user_id: "u_001",
    message: "你好"
  })
})

const data = await response.json()
console.log(data.reply)
```

这就是前端和 Python 后端之间的基本连接方式。

后续做 Agent 应用时，经常会变成：

```text
前端页面 -> FastAPI 后端 -> LLM SDK -> 工具函数 / 数据库 / RAG -> 返回结果
```

---

## 14. 同步接口与异步接口

FastAPI 支持普通函数：

```python
@app.get("/sync")
def sync_api():
    return {"mode": "sync"}
```

也支持异步函数：

```python
@app.get("/async")
async def async_api():
    return {"mode": "async"}
```

什么时候用 `async def`？

- 调用异步 LLM SDK；
- 调用异步 HTTP 客户端；
- 操作异步数据库；
- 需要并发等待多个 I/O 任务。

什么时候普通 `def` 就够？

- 简单计算；
- 读取本地小数据；
- 初学阶段写普通示例；
- 没有异步依赖。

不要为了“看起来高级”强行使用异步。后续进入 LLM SDK 和 Agent 工作流时，再逐步增加异步使用。

---

## 15. 一个 Agent 服务雏形

下面是一个非常简化的 Agent API 雏形。

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class AgentRequest(BaseModel):
    user_id: str
    task: str


class AgentResponse(BaseModel):
    user_id: str
    result: str
    used_tool: bool


def run_agent_task(task: str) -> str:
    return f"任务已接收：{task}"


@app.post("/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest):
    result = run_agent_task(request.task)

    return AgentResponse(
        user_id=request.user_id,
        result=result,
        used_tool=False
    )
```

这个例子虽然没有真正调用 LLM，但结构已经接近真实 Agent 服务：

- `AgentRequest` 定义用户输入；
- `run_agent_task()` 表示核心 Agent 逻辑；
- `/agent/run` 对外暴露服务；
- `AgentResponse` 定义稳定输出格式。

后续阶段会把 `run_agent_task()` 替换成真实 LLM SDK 调用、工具调用、RAG 和多步骤工作流。

---

## 16. 本阶段你需要掌握什么

完成本阶段后，你应该能做到：

1. 解释 HTTP 请求由哪些部分组成；
2. 区分 GET 和 POST；
3. 理解状态码的作用；
4. 用 `requests` 调用一个 JSON API；
5. 使用环境变量读取 API Key；
6. 用 FastAPI 写一个简单 GET 接口；
7. 用 FastAPI 写一个带请求体的 POST 接口；
8. 用 Pydantic 定义请求和响应结构；
9. 用 `HTTPException` 返回明确错误；
10. 说清楚 API 服务和 Agent 工具/Agent 后端之间的关系。

---

## 17. 小练习

请你自己写一个文件：

```text
stage_04_api_demo.py
```

要求：

1. 使用 FastAPI 创建 `app`；
2. 定义一个 `TaskRequest`，字段包括：
   - `user_id: str`
   - `title: str`
   - `priority: int`
3. 定义一个 `TaskResponse`，字段包括：
   - `user_id: str`
   - `summary: str`
   - `accepted: bool`
4. 创建一个 POST 接口：

```text
POST /tasks/analyze
```

5. 如果 `priority` 小于 1 或大于 5，返回 `400` 错误；
6. 正常情况下返回：

```json
{
  "user_id": "用户 id",
  "summary": "任务 标题 的优先级是 priority",
  "accepted": true
}
```

缩进提醒：

```text
顶层 import、class、app、函数定义：0 个空格
class 内部字段：4 个空格
函数内部代码：4 个空格
if 内部代码：8 个空格
```

---

## 18. 学完后的下一步

你学完本阶段后，对我说：

```text
我学习完了
```

然后我会给你阶段 4 测试题。测试通过后，我们进入阶段 5：LLM SDK 使用。
