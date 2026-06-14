# Agent 应用开发学习路线：阶段 3 — Python 面向对象与异步基础

> 学习对象：有前端开发经验，已学习 Python 基础与脚本能力。
>
> 当前阶段目标：理解 Python 面向对象和异步编程基础，为后续学习 LLM SDK、工具封装、Agent 工作流、并发 API 调用打基础。

---

## 0. 学习方式

你先学习本文件，并完成最后的练习。

当你学习完成后，直接告诉我：

```text
我学习完了
```

然后我会给你出阶段 3 测试题。你回答后，我会分析你的掌握情况，并判断是否进入阶段 4。

---

## 1. 为什么 Agent 开发需要面向对象和异步？

真实 Agent 应用中，经常会出现这些对象：

- 用户 User
- 消息 Message
- 工具 Tool
- 任务 Task
- Agent
- 对话 Session
- 配置 Config
- 模型客户端 ModelClient

这些对象通常都有自己的数据和行为。

例如一个 Agent 可能需要：

```text
保存名字
保存可用工具列表
接收用户输入
调用模型
调用工具
返回结果
```

这就很适合用 class 表达。

同时，Agent 经常要调用外部服务：

- 模型 API
- 搜索 API
- 数据库
- 文件系统
- 工具服务

这些操作可能比较慢，所以需要异步编程来提高效率。

---

## 2. 面向对象基础：class

JavaScript 中你可能写过：

```js
class User {
  constructor(name) {
    this.name = name
  }

  sayHello() {
    console.log(`Hello, ${this.name}`)
  }
}
```

Python 中类似：

```python
class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")


user = User("Kai")
user.say_hello()
```

输出：

```text
Hello, Kai
```

---

## 3. __init__ 是什么？

```python
def __init__(self, name):
    self.name = name
```

`__init__` 是初始化方法。创建对象时会自动执行。

例如：

```python
user = User("Kai")
```

会自动调用：

```python
__init__(self, "Kai")
```

你可以把它类比成 JavaScript 的：

```js
constructor(name) {}
```

---

## 4. self 是什么？

`self` 表示当前对象本身。

```python
class User:
    def __init__(self, name):
        self.name = name
```

这里：

```python
self.name = name
```

意思是：把传进来的 `name` 保存到当前对象的 `name` 属性上。

类似 JS：

```js
this.name = name
```

所以可以简单记：

```text
Python self 类似 JavaScript this
```

注意：Python 类方法第一个参数通常都要写 `self`。

---

## 5. 属性和方法

```python
class LearningRecord:
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage

    def summary(self):
        return f"{self.name} 正在学习 {self.stage}"


record = LearningRecord("Kai", "Python 阶段 3")
print(record.name)
print(record.summary())
```

输出：

```text
Kai
Kai 正在学习 Python 阶段 3
```

说明：

```text
record.name 是属性
record.summary() 是方法
```

---

## 6. 用 class 表示 Agent

一个简单 Agent 可以这样表示：

```python
class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.tools = []

    def add_tool(self, tool_name):
        self.tools.append(tool_name)

    def list_tools(self):
        return self.tools

    def run(self, user_input):
        return f"{self.name} 收到任务：{user_input}"


agent = SimpleAgent("学习助手")
agent.add_tool("读取文件")
agent.add_tool("保存记录")

print(agent.list_tools())
print(agent.run("帮我学习 Python"))
```

输出：

```text
['读取文件', '保存记录']
学习助手 收到任务：帮我学习 Python
```

---

## 7. 类和 dict 的区别

你之前学过 dict：

```python
agent = {
    "name": "学习助手",
    "tools": ["读取文件", "保存记录"]
}
```

dict 适合保存数据。

class 不仅能保存数据，还能保存行为：

```python
class SimpleAgent:
    def run(self, user_input):
        ...
```

对比：

| 类型 | 适合做什么 |
|---|---|
| dict | 保存结构化数据 |
| class | 同时组织数据和行为 |

Agent 应用里，两者都会用。

---

## 8. dataclass 简介

如果一个类主要用来存数据，可以用 `dataclass` 简化。

```python
from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


message = Message(role="user", content="你好")
print(message.role)
print(message.content)
```

这比手写 `__init__` 简洁。

等价于你不用自己写：

```python
def __init__(self, role, content):
    self.role = role
    self.content = content
```

在 Agent 应用中，Message 很常见：

```python
Message(role="user", content="帮我总结这个文件")
Message(role="assistant", content="好的，我来处理")
```

---

## 9. 类型提示基础

Python 可以写类型提示：

```python
def add(a: int, b: int) -> int:
    return a + b
```

含义：

```text
a 是 int
b 是 int
返回值是 int
```

类型提示不会像 TypeScript 那样在运行前强制检查，但它可以：

- 提升可读性；
- 帮助 IDE 提示；
- 方便后续维护；
- 让 Agent 工具参数更清晰。

示例：

```python
def build_message(name: str, stage: str) -> str:
    return f"{name} 正在学习 {stage}"
```

---

## 10. 异步编程 async / await

你作为前端开发者，应该熟悉 JS 的：

```js
async function fetchData() {
  const response = await fetch(url)
  return await response.json()
}
```

Python 也有类似语法：

```python
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "数据加载完成"


async def main():
    result = await fetch_data()
    print(result)


asyncio.run(main())
```

输出：

```text
数据加载完成
```

---

## 11. async def 是什么？

```python
async def fetch_data():
    ...
```

表示定义一个异步函数。

异步函数调用后不会立即得到普通结果，而是得到一个可等待对象，需要用：

```python
await fetch_data()
```

等待它完成。

---

## 12. await 是什么？

```python
result = await fetch_data()
```

`await` 表示等待异步任务完成，并拿到结果。

它类似 JS 里的：

```js
const result = await fetchData()
```

---

## 13. asyncio.sleep 和 time.sleep 的区别

同步阻塞：

```python
import time

time.sleep(1)
print("完成")
```

`time.sleep(1)` 会阻塞整个程序。

异步等待：

```python
import asyncio

await asyncio.sleep(1)
```

`asyncio.sleep(1)` 是非阻塞等待，适合异步任务。

---

## 14. 并发执行多个任务

Agent 可能需要同时做多个慢操作，例如：

- 查天气；
- 搜索资料；
- 读取数据库；
- 调用多个 API。

Python 可以用 `asyncio.gather()` 并发执行：

```python
import asyncio


async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成"


async def main():
    results = await asyncio.gather(
        task("任务 A", 2),
        task("任务 B", 1),
        task("任务 C", 3)
    )

    print(results)


asyncio.run(main())
```

输出大概是：

```text
['任务 A 完成', '任务 B 完成', '任务 C 完成']
```

虽然任务 C 等 3 秒，但三个任务是同时开始的，总耗时约 3 秒，而不是 2 + 1 + 3 = 6 秒。

---

## 15. 异步 Agent 示例

```python
import asyncio


class AsyncAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型回复：已处理 {prompt}"

    async def run(self, user_input):
        result = await self.call_model(user_input)
        return f"{self.name}: {result}"


async def main():
    agent = AsyncAgent("学习助手")
    result = await agent.run("学习 Python async")
    print(result)


asyncio.run(main())
```

这里：

```python
async def call_model(...)
```

模拟调用模型 API。

真实项目里，这里会替换成：

```python
await client.messages.create(...)
```

或者其他异步 SDK 调用。

---

## 16. 常见错误

### 16.1 忘记 self

错误：

```python
class User:
    def __init__(name):
        name = name
```

正确：

```python
class User:
    def __init__(self, name):
        self.name = name
```

---

### 16.2 忘记 await

错误：

```python
result = fetch_data()
print(result)
```

这可能打印出 coroutine 对象，而不是实际结果。

正确：

```python
result = await fetch_data()
print(result)
```

---

### 16.3 顶层直接 await

普通 Python 文件里不能直接：

```python
result = await fetch_data()
```

通常要写：

```python
async def main():
    result = await fetch_data()

asyncio.run(main())
```

---

## 17. Agent 应用中的对应关系

| Python 能力 | Agent 应用中的作用 |
|---|---|
| class | 表示 Agent、Tool、Task、Message 等对象 |
| __init__ | 初始化对象状态 |
| self | 访问当前对象的数据和方法 |
| 方法 | 表示对象能做的动作 |
| dataclass | 简洁定义消息、配置、任务等数据结构 |
| 类型提示 | 让工具参数和返回值更清晰 |
| async/await | 调用模型 API、工具 API、数据库等慢操作 |
| asyncio.gather | 并发执行多个外部调用 |

---

## 18. 阶段 3 自查清单

学习完成后，你应该能回答：

1. `class` 是做什么的？
2. `__init__` 类似 JavaScript 中的什么？
3. `self` 类似 JavaScript 中的什么？
4. 属性和方法有什么区别？
5. dict 和 class 的区别是什么？
6. `@dataclass` 适合什么场景？
7. 类型提示有什么用？
8. `async def` 是什么？
9. `await` 是什么？
10. `asyncio.gather()` 适合什么场景？
11. 为什么 Agent 开发经常需要异步？

---

## 19. 阶段 3 练习

请你学习后完成下面练习。

### 练习 1：定义一个学习记录类

要求：

1. 定义 `LearningRecord` 类；
2. `__init__` 接收：
   - `name`
   - `stage`
   - `target`
3. 保存到对象属性上；
4. 定义 `summary()` 方法，返回：

```text
你的名字 正在学习 Python 阶段 3，目标是 Agent developer
```

---

### 练习 2：定义 Message dataclass

要求：

1. 使用 `@dataclass`
2. 定义 `Message`
3. 包含：
   - `role: str`
   - `content: str`
4. 创建一个用户消息：

```python
Message(role="user", content="我正在学习 Agent 开发")
```

---

### 练习 3：异步 Agent

要求：

1. 定义 `AsyncLearningAgent` 类；
2. `__init__` 接收 `name`；
3. 定义异步方法 `call_model(prompt)`；
4. 在 `call_model` 中使用 `await asyncio.sleep(1)` 模拟模型调用；
5. 返回：

```text
模型已处理：你的输入
```

6. 定义异步方法 `run(user_input)`；
7. 在 `run` 中 `await self.call_model(user_input)`；
8. 用 `asyncio.run(main())` 运行。

参考结构：

```python
import asyncio
from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


class AsyncLearningAgent:
    def __init__(self, name):
        ...

    async def call_model(self, prompt):
        ...

    async def run(self, user_input):
        ...


async def main():
    ...


asyncio.run(main())
```

---

## 20. 学完后告诉我

学习完成后，直接回复：

```text
我学习完了
```

然后我会给你出阶段 3 测试题，并根据你的答案判断是否进入：

```text
阶段 4：API 使用与后端服务基础
```
