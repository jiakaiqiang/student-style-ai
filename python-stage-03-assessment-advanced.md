# 阶段 3 深度测试题 — Python 面向对象与异步编程

> **测试说明**：
> - 本测试共 18 题，分为 4 个部分
> - 请认真作答，展示你对概念的深度理解
> - 编码题请严格按要求实现，注意缩进、字段名、类型提示

---

## 第一部分：概念理解题（10 题）

### Q1. `__init__` vs `__new__`

请回答：
1. `__new__` 和 `__init__` 的调用顺序是什么？
2. `__new__` 的返回值是什么？`__init__` 的返回值是什么？
3. 为什么单例模式要重写 `__new__` 而不是 `__init__`？
4. 在 Agent 应用中，哪些对象适合用单例模式？为什么？

---

### Q2. `@property` 的作用

请回答：
1. `@property` 和直接访问属性（如 `self.name`）有什么区别？
2. 什么时候应该用 `@property` 而不是普通属性？
3. 在 Agent 中，给出 2 个适合用 `@property` 的场景。

---

### Q3. 方法类型对比

有以下代码：

```python
class Agent:
    @staticmethod
    def validate_input(text):
        return len(text) > 0
    
    @classmethod
    def from_config(cls, config):
        return cls(config["name"])
    
    def run(self, input):
        return f"处理：{input}"
```

请回答：
1. 这三种方法分别在什么场景下使用？
2. 为什么 `validate_input` 用 `@staticmethod` 而不是实例方法？
3. 为什么 `from_config` 用 `@classmethod` 而不是 `@staticmethod`？

---

### Q4. `@dataclass` 高级特性

请回答：
1. 为什么不能写 `tools: List[str] = []`，必须用 `field(default_factory=list)`？
2. `frozen=True` 的作用是什么？在 Agent 应用中哪些数据应该是 frozen 的？
3. `slots=True` 的作用是什么？什么场景下应该使用？
4. `__post_init__` 在什么时候被调用？适合做什么事情？

---

### Q5. `Protocol` vs 抽象基类

请回答：
1. `Protocol` 和 `ABC`（抽象基类）有什么区别？
2. 什么时候用 `Protocol`，什么时候用 `ABC`？
3. 在 Agent 工具系统中，你会选择哪一个？为什么？

---

### Q6. Event Loop 原理

请回答：
1. Event Loop 的作用是什么？
2. `asyncio.run(main())` 做了哪些事情？
3. 为什么不能在普通 Python 文件顶层直接写 `await fetch_data()`？
4. 前端的 Event Loop 和 Python 的 Event Loop 有什么相似之处？

---

### Q7. `coroutine` vs `Task`

请回答：
1. 调用 `async def fetch()` 返回的是什么？它会立即执行吗？
2. `asyncio.create_task()` 做了什么？Task 会立即开始执行吗？
3. 以下两段代码的执行时间有什么区别？为什么？

```python
# 代码 A
result1 = await fetch("A")
result2 = await fetch("B")

# 代码 B
task1 = asyncio.create_task(fetch("A"))
task2 = asyncio.create_task(fetch("B"))
result1 = await task1
result2 = await task2
```

---

### Q8. `gather()` vs `wait()`

请回答：
1. `asyncio.gather()` 和 `asyncio.wait()` 的主要区别是什么？
2. 什么场景下应该用 `gather()`？什么场景下应该用 `wait()`？
3. `gather()` 的 `return_exceptions=True` 参数有什么作用？

---

### Q9. 异步上下文管理器

请回答：
1. `async with` 和普通 `with` 的区别是什么？
2. 为什么 HTTP 客户端（如 aiohttp）要用 `async with` 而不是普通 `with`？
3. 在 Agent 应用中，哪些资源应该用 `async with` 管理？

---

### Q10. 异步生成器

请回答：
1. 异步生成器和普通生成器的区别是什么？
2. 为什么 LLM 流式输出要用异步生成器而不是普通函数？
3. `async for` 和普通 `for` 的区别是什么？

---

## 第二部分：代码分析题（5 题）

### Q11. 找出所有错误

以下代码有 **5 个错误**，请找出并说明如何修改：

```python
from dataclasses import dataclass
import asyncio

@dataclass
class Agent:
    name: str
    tools: list = []
    
    def __post_init__():
        print(f"Agent {name} 初始化")
    
    async def call_tool(tool_name, input):
        result = asyncio.sleep(1)
        return f"工具 {tool_name} 结果"
    
    async def run(self, user_input):
        results = await asyncio.gather(
            self.call_tool("search", user_input),
            self.call_tool("calc", "1+1")
        )
        return results

agent = Agent("Bot")
asyncio.run(agent.run("hello"))
```

---

### Q12. 性能问题分析

以下代码有性能问题，请回答：

```python
async def process_queries(queries: List[str]):
    results = []
    for query in queries:
        result = await call_api(query)
        results.append(result)
    return results
```

1. 这段代码的性能问题是什么？
2. 如果有 10 个 query，每个 API 调用耗时 1 秒，总耗时是多少？
3. 如何优化？优化后总耗时是多少？
4. 写出优化后的代码。

---

### Q13. 异常处理问题

以下代码的异常处理有什么问题？

```python
async def call_multiple_tools(user_input: str):
    try:
        results = await asyncio.gather(
            search_tool.execute(query=user_input),
            calculator_tool.execute(expression="1/0"),
            weather_tool.execute(city="北京")
        )
        return results
    except Exception as e:
        return "工具调用失败"
```

1. 如果 calculator_tool 抛出异常，会发生什么？
2. 这种处理方式有什么问题？
3. 如何改进，让其他工具的结果仍然能返回？

---

### Q14. 资源泄漏问题

以下代码有资源泄漏风险，请回答：

```python
async def fetch_data(url: str):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    data = await response.json()
    return data
```

1. 这段代码的问题是什么？
2. 在什么情况下会发生资源泄漏？
3. 如何修复？

---

### Q15. 并发控制问题

以下代码可能导致 API 速率限制，请回答：

```python
async def process_all(items: List[str]):
    tasks = [call_api(item) for item in items]
    return await asyncio.gather(*tasks)
```

1. 如果 items 有 1000 个，会发生什么问题？
2. 如何限制并发数量为 10？
3. 写出改进后的代码。

---

## 第三部分：设计题（2 题）

### Q16. 设计工具系统

请设计一个完整的工具系统，要求：

1. 定义工具基类（使用 `Protocol` 或 `ABC`，说明你的选择理由）
2. 工具必须包含：
   - `name`：工具名称
   - `description`：工具描述
   - `execute(**kwargs)`：异步执行方法
   - `to_schema()`：返回 LLM 可用的工具 schema
3. 实现两个具体工具：
   - `SearchTool`：接收 `query: str`，返回搜索结果
   - `WeatherTool`：接收 `city: str`，返回天气信息
4. 实现 `ToolRegistry` 类，用于注册和管理工具
5. 所有代码要有类型提示

请写出完整代码。

---

### Q17. 设计会话管理系统

请设计一个会话管理系统，要求：

1. 使用 `@dataclass` 定义 `Message` 类：
   - `role: str`（使用 `Literal` 限定为 "user" | "assistant" | "system"）
   - `content: str`
   - `timestamp: float`（使用 `field(default_factory=...)` 自动生成）

2. 使用 `@dataclass` 定义 `Session` 类：
   - `session_id: str`
   - `user_id: str`
   - `messages: List[Message]`（默认空列表）
   - `context: Dict[str, Any]`（默认空字典）
   - 方法 `add_message(role, content)`：添加消息
   - 方法 `get_recent_messages(n: int)`：获取最近 n 条消息
   - 使用 `@property` 实现 `message_count`：返回消息总数

3. 实现 `SessionManager` 类：
   - 管理多个会话
   - 方法 `create_session(session_id, user_id)`：创建会话
   - 方法 `get_session(session_id)`：获取会话
   - 方法 `save_session(session_id, file_path)`：保存到 JSON 文件
   - 方法 `load_session(file_path)`：从 JSON 文件加载

4. 所有代码要有完整的类型提示

请写出完整代码。

---

## 第四部分：综合编码题（1 题）

### Q18. 实现生产级 Agent

请实现一个完整的 Agent 系统，文件名：`production_agent.py`

**要求：**

#### 1. 工具系统

定义工具基类 `BaseTool`（使用 `ABC`）：
- 属性：`name: str`、`description: str`
- 抽象方法：`async def execute(self, **kwargs) -> str`
- 方法：`to_schema() -> Dict`（返回工具的 JSON schema）

实现三个具体工具：
- `SearchTool`：参数 `query: str`，模拟搜索（sleep 0.5 秒）
- `CalculatorTool`：参数 `expression: str`，执行计算（使用 `eval`，要捕获异常）
- `WeatherTool`：参数 `city: str`，模拟查天气（sleep 0.3 秒）

#### 2. 消息和会话

使用 `@dataclass` 定义：
- `Message`：`role: str`、`content: str`
- `Session`：`session_id: str`、`messages: List[Message]`（默认空列表）

#### 3. Agent 类

实现 `ProductionAgent` 类：

**属性：**
- `name: str`
- `tools: Dict[str, BaseTool]`（工具字典）
- `sessions: Dict[str, Session]`（会话字典）
- `max_concurrent_tools: int`（最大并发工具数，默认 3）

**方法：**
- `register_tool(self, tool: BaseTool)`：注册工具
- `async def call_llm(self, messages: List[Message]) -> str`：模拟 LLM 调用（sleep 1 秒，返回简单响应）
- `async def call_tool_safe(self, tool_name: str, **kwargs) -> Dict`：安全调用工具，返回 `{"success": bool, "result": str, "error": str}`
- `async def call_tools_parallel(self, tool_calls: List[Dict]) -> List[Dict]`：并发调用多个工具，使用 `Semaphore` 限制并发数
- `def get_or_create_session(self, session_id: str) -> Session`：获取或创建会话
- `async def run(self, session_id: str, user_input: str) -> str`：运行 Agent

#### 4. 主函数

实现 `async def main()`：
1. 创建 Agent
2. 注册三个工具
3. 创建会话并运行两次对话
4. 打印结果

#### 5. 代码规范

- 所有函数和方法要有类型提示
- 顶层代码 0 个空格，函数内部 4 个空格
- 使用 `asyncio.run(main())` 启动

**提示：**
- `call_tools_parallel` 中使用 `asyncio.Semaphore` 限制并发
- 工具调用要用 `return_exceptions=True` 或 `try-except` 保证容错
- Session 的 messages 要用 `field(default_factory=list)`

请写出完整的 `production_agent.py` 文件内容。

---

## 测试完成后

请把你的答案发给我，我会分析：
1. 概念理解的深度和准确性
2. 代码质量和规范性
3. 设计能力和架构思维
4. 是否可以进入阶段 4

祝你测试顺利！

