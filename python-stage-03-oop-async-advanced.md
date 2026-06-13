# Agent 应用开发学习路线：阶段 3 — Python 面向对象与异步编程（全面深入版）

> **学习对象**：有前端开发经验，已掌握 Python 基础与脚本能力。
>
> **当前阶段目标**：深入理解 Python 面向对象和异步编程，掌握 Agent 应用开发中的核心模式和最佳实践。

---

## 目录

### 第一部分：面向对象编程深入
1. 类的构造：`__init__` vs `__new__`
2. 属性管理：`@property`、getter/setter
3. 方法类型：实例方法、`@staticmethod`、`@classmethod`
4. 继承与多态：`super()`、方法重写、MRO
5. `@dataclass` 高级特性
6. 类型系统：`TypedDict`、`Protocol`、`Literal`、泛型
7. 抽象基类与接口设计

### 第二部分：异步编程深入
8. Event Loop 与协程原理
9. `coroutine` vs `Task` vs `Future`
10. 任务管理：`create_task()`、`gather()`、`wait()`
11. 超时与取消机制
12. 异步上下文管理器 `async with`
13. 异步迭代器 `async for`
14. 异步生成器与流式处理
15. 错误处理与异常传播

### 第三部分：Agent 应用实战模式
16. Agent 架构设计模式
17. 工具系统设计
18. 并发调用与性能优化
19. 状态管理与会话持久化

---

## 第一部分：面向对象编程深入

---

## 1. 类的构造：`__init__` vs `__new__`

### 1.1 `__init__` — 初始化方法

你已经熟悉 `__init__`，它类似 JS 的 `constructor`：

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.tools = []
```

`__init__` 在对象**已经创建后**被调用，用于初始化对象的属性。

### 1.2 `__new__` — 对象创建方法

`__new__` 是真正创建对象的方法，在 `__init__` 之前调用：

```python
class Agent:
    def __new__(cls, name):
        print(f"__new__ 被调用，创建对象")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print(f"__init__ 被调用，初始化对象")
        self.name = name

agent = Agent("Bot")
```

输出：
```text
__new__ 被调用，创建对象
__init__ 被调用，初始化对象
```

### 1.3 Agent 场景：单例模式

在 Agent 应用中，有时需要确保某个类只有一个实例（例如全局配置、模型客户端）：

```python
class ModelClient:
    _instance = None
    
    def __new__(cls, api_key):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, api_key):
        self.api_key = api_key

# 无论创建多少次，都是同一个对象
client1 = ModelClient("key1")
client2 = ModelClient("key2")
print(client1 is client2)  # True
```

**实际应用**：避免重复创建昂贵的资源（HTTP 连接池、数据库连接）。

---

## 2. 属性管理：`@property`

### 2.1 为什么需要 property？

直接访问属性可能不安全：

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.max_tokens = 1000

agent = Agent("Bot")
agent.max_tokens = -500  # 不合理的值，但没有校验
```

### 2.2 使用 `@property` 添加校验

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self._max_tokens = 1000  # 私有属性
    
    @property
    def max_tokens(self):
        """获取 max_tokens"""
        return self._max_tokens
    
    @max_tokens.setter
    def max_tokens(self, value):
        """设置 max_tokens，带校验"""
        if value < 0:
            raise ValueError("max_tokens 不能为负数")
        self._max_tokens = value

agent = Agent("Bot")
print(agent.max_tokens)  # 1000
agent.max_tokens = 2000  # 正常
agent.max_tokens = -500  # 抛出 ValueError
```

### 2.3 Agent 场景：计算属性

```python
class Agent:
    def __init__(self, name):
        self.name = name
        self.tools = []
    
    @property
    def tool_count(self):
        """动态计算工具数量"""
        return len(self.tools)
    
    @property
    def status(self):
        """根据状态计算描述"""
        if not self.tools:
            return "未配置工具"
        return f"已配置 {self.tool_count} 个工具"

agent = Agent("Bot")
print(agent.status)  # 未配置工具
agent.tools.append("search")
print(agent.status)  # 已配置 1 个工具
```

**前端类比**：类似 Vue 的 `computed` 或 React 的派生状态。

---

## 3. 方法类型：实例方法、`@staticmethod`、`@classmethod`

### 3.1 实例方法（Instance Method）

最常见的方法，第一个参数是 `self`：

```python
class Agent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"我是 {self.name}"
```

### 3.2 静态方法（`@staticmethod`）

不需要访问实例或类，只是逻辑上属于这个类：

```python
class Agent:
    @staticmethod
    def validate_name(name):
        """校验名称格式，不需要访问实例"""
        if not name or len(name) < 2:
            raise ValueError("名称至少 2 个字符")
        return True

# 可以直接通过类调用
Agent.validate_name("Bot")  # True
Agent.validate_name("A")    # ValueError
```

### 3.3 类方法（`@classmethod`）

第一个参数是 `cls`（类本身），常用于工厂方法：

```python
class Agent:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    @classmethod
    def create_default(cls):
        """工厂方法：创建默认配置的 Agent"""
        return cls(name="DefaultBot", model="gpt-4")
    
    @classmethod
    def from_config(cls, config_dict):
        """工厂方法：从配置字典创建"""
        return cls(
            name=config_dict["name"],
            model=config_dict["model"]
        )

# 使用工厂方法
agent1 = Agent.create_default()
agent2 = Agent.from_config({"name": "Bot", "model": "claude-3"})
```

### 3.4 Agent 场景对比

| 方法类型 | 使用场景 | Agent 应用示例 |
|---------|---------|---------------|
| 实例方法 | 需要访问实例数据 | `agent.run(input)` |
| 静态方法 | 工具函数，不依赖实例 | `Agent.validate_prompt(text)` |
| 类方法 | 创建实例的不同方式 | `Agent.from_config(dict)` |

---

## 4. 继承与多态

### 4.1 基础继承

```python
class BaseAgent:
    def __init__(self, name):
        self.name = name
    
    def run(self, input_text):
        return f"{self.name} 处理：{input_text}"

class SearchAgent(BaseAgent):
    def __init__(self, name, search_engine):
        super().__init__(name)  # 调用父类的 __init__
        self.search_engine = search_engine
    
    def search(self, query):
        return f"使用 {self.search_engine} 搜索：{query}"

agent = SearchAgent("搜索助手", "Google")
print(agent.run("任务"))      # 继承自父类
print(agent.search("Python"))  # 子类新增方法
```

### 4.2 方法重写（Override）

```python
class BaseAgent:
    def run(self, input_text):
        return f"基础处理：{input_text}"

class SmartAgent(BaseAgent):
    def run(self, input_text):
        # 重写父类方法
        result = super().run(input_text)  # 可选：调用父类方法
        return f"智能增强 -> {result}"

agent = SmartAgent("Bot")
print(agent.run("任务"))  # 智能增强 -> 基础处理：任务
```

### 4.3 Agent 场景：工具基类

```python
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """工具抽象基类"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, **kwargs):
        """子类必须实现此方法"""
        pass

class SearchTool(BaseTool):
    async def execute(self, query: str):
        # 实现具体搜索逻辑
        return f"搜索结果：{query}"

class CalculatorTool(BaseTool):
    async def execute(self, expression: str):
        return f"计算结果：{eval(expression)}"
```

**实际应用**：统一工具接口，Agent 可以用相同方式调用不同工具。

---

## 4. 继承与多态

### 4.1 基础继承

```python
class BaseAgent:
    def __init__(self, name):
        self.name = name
    
    def run(self, input_text):
        return f"{self.name} 处理：{input_text}"

class SearchAgent(BaseAgent):
    def __init__(self, name, search_engine):
        super().__init__(name)  # 调用父类的 __init__
        self.search_engine = search_engine
    
    def search(self, query):
        return f"使用 {self.search_engine} 搜索：{query}"

agent = SearchAgent("搜索助手", "Google")
print(agent.run("任务"))      # 继承自父类
print(agent.search("Python"))  # 子类新增方法
```

### 4.2 方法重写（Override）

```python
class BaseAgent:
    def run(self, input_text):
        return f"基础处理：{input_text}"

class SmartAgent(BaseAgent):
    def run(self, input_text):
        # 重写父类方法
        result = super().run(input_text)  # 可选：调用父类方法
        return f"智能增强 -> {result}"

agent = SmartAgent("Bot")
print(agent.run("任务"))  # 智能增强 -> 基础处理：任务
```

### 4.3 Agent 场景：工具基类

```python
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """工具抽象基类"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def execute(self, **kwargs):
        """子类必须实现此方法"""
        pass

class SearchTool(BaseTool):
    async def execute(self, query: str):
        # 实现具体搜索逻辑
        return f"搜索结果：{query}"

class CalculatorTool(BaseTool):
    async def execute(self, expression: str):
        return f"计算结果：{eval(expression)}"
```

**实际应用**：统一工具接口，Agent 可以用相同方式调用不同工具。

---

## 5. `@dataclass` 高级特性

### 5.1 基础回顾

```python
from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str
```

### 5.2 `field()` — 自定义字段行为

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Agent:
    name: str
    tools: List[str] = field(default_factory=list)  # 默认空列表
    max_tokens: int = field(default=1000)
    api_key: str = field(repr=False)  # 不在 repr 中显示

agent = Agent(name="Bot", api_key="secret")
print(agent)  # Agent(name='Bot', tools=[], max_tokens=1000)
```

**注意**：不要用 `tools: List[str] = []`，这会导致所有实例共享同一个列表！

### 5.3 `__post_init__` — 初始化后处理

```python
@dataclass
class Agent:
    name: str
    model: str
    
    def __post_init__(self):
        """在 __init__ 之后自动调用"""
        if not self.name:
            raise ValueError("name 不能为空")
        self.name = self.name.strip()
        print(f"Agent {self.name} 初始化完成")

agent = Agent(name="  Bot  ", model="gpt-4")
# 输出：Agent Bot 初始化完成
print(agent.name)  # "Bot"（已去除空格）
```

### 5.4 `frozen=True` — 不可变对象

```python
@dataclass(frozen=True)
class Message:
    role: str
    content: str

msg = Message(role="user", content="Hello")
msg.content = "Hi"  # 抛出 FrozenInstanceError
```

**Agent 场景**：消息历史记录应该是不可变的，防止意外修改。

### 5.5 `slots=True` — 内存优化

```python
@dataclass(slots=True)
class Message:
    role: str
    content: str
```

**效果**：减少内存占用，提升属性访问速度。适合创建大量实例的场景（如消息列表）。

---

## 6. 类型系统深入

### 6.1 基础类型提示

```python
def process(name: str, age: int) -> str:
    return f"{name} is {age}"
```

### 6.2 `Optional` 和 `Union`

```python
from typing import Optional, Union

def get_agent(name: Optional[str] = None) -> Optional[Agent]:
    """返回值可能是 Agent 或 None"""
    if name:
        return Agent(name)
    return None

def process(value: Union[str, int]) -> str:
    """参数可以是 str 或 int"""
    return str(value)
```

### 6.3 `Literal` — 限定具体值

```python
from typing import Literal

def create_message(role: Literal["user", "assistant", "system"], content: str):
    """role 只能是这三个值之一"""
    return {"role": role, "content": content}

create_message("user", "Hello")      # ✅
create_message("admin", "Hello")     # ❌ 类型检查器会报错
```

### 6.4 `TypedDict` — 结构化字典

```python
from typing import TypedDict

class MessageDict(TypedDict):
    role: str
    content: str
    timestamp: int

def save_message(msg: MessageDict):
    print(msg["role"])

# 使用
msg: MessageDict = {
    "role": "user",
    "content": "Hello",
    "timestamp": 1234567890
}
save_message(msg)
```

**Agent 场景**：API 响应、配置文件、JSON 数据结构。

### 6.5 `Protocol` — 结构化类型（鸭子类型）

```python
from typing import Protocol

class Runnable(Protocol):
    """定义接口：任何有 run 方法的对象"""
    def run(self, input: str) -> str:
        ...

class Agent:
    def run(self, input: str) -> str:
        return f"处理：{input}"

class Tool:
    def run(self, input: str) -> str:
        return f"执行：{input}"

def execute(obj: Runnable, input: str):
    """接受任何实现了 run 方法的对象"""
    return obj.run(input)

execute(Agent(), "task")  # ✅
execute(Tool(), "task")   # ✅
```

**前端类比**：类似 TypeScript 的 `interface`。

---

## 第二部分：异步编程深入

---

## 7. Event Loop 与协程原理

### 7.1 什么是 Event Loop？

Event Loop（事件循环）是异步编程的核心，负责调度和执行异步任务。

**前端类比**：类似浏览器的事件循环，处理 `setTimeout`、`Promise`、用户事件等。

```python
import asyncio

async def task():
    print("任务开始")
    await asyncio.sleep(1)
    print("任务结束")

# asyncio.run() 会创建 event loop 并运行
asyncio.run(task())
```

### 7.2 协程（Coroutine）是什么？

```python
async def fetch_data():
    await asyncio.sleep(1)
    return "data"

# 调用 async 函数不会立即执行，而是返回一个协程对象
coro = fetch_data()
print(type(coro))  # <class 'coroutine'>

# 必须用 await 或 asyncio.run() 来执行
result = asyncio.run(coro)
```

### 7.3 协程的生命周期

```python
import asyncio

async def demo():
    print("1. 协程开始")
    await asyncio.sleep(1)
    print("2. 等待结束")
    return "完成"

async def main():
    print("创建协程")
    coro = demo()  # 此时还没执行
    
    print("开始执行")
    result = await coro  # 这里才真正执行
    
    print(f"结果：{result}")

asyncio.run(main())
```

输出：
```text
创建协程
开始执行
1. 协程开始
2. 等待结束
结果：完成
```

### 7.4 Agent 场景

```python
async def call_llm_api(prompt: str):
    """模拟调用 LLM API"""
    await asyncio.sleep(1)  # 模拟网络延迟
    return f"LLM 回复：{prompt}"

# 创建协程但不立即执行，可以批量管理
tasks = [call_llm_api(f"问题{i}") for i in range(3)]
```

---

## 8. `coroutine` vs `Task` vs `Future`

### 8.1 Coroutine（协程）

```python
async def fetch():
    return "data"

coro = fetch()  # 协程对象，还未执行
```

### 8.2 Task（任务）

Task 是协程的包装，可以被 event loop 调度：

```python
import asyncio

async def fetch(name):
    await asyncio.sleep(1)
    return f"{name} 完成"

async def main():
    # 创建 Task，立即开始在后台执行
    task1 = asyncio.create_task(fetch("任务1"))
    task2 = asyncio.create_task(fetch("任务2"))
    
    print("任务已创建，开始等待")
    
    # 等待任务完成
    result1 = await task1
    result2 = await task2
    
    print(result1, result2)

asyncio.run(main())
```

### 8.3 `create_task()` vs `gather()`

**`create_task()`**：立即开始执行，返回 Task 对象，可以单独控制。

```python
async def main():
    task = asyncio.create_task(fetch("A"))
    # 可以在这里做其他事情
    await asyncio.sleep(0.5)
    # 然后等待任务
    result = await task
```

**`gather()`**：批量等待多个协程，返回结果列表。

```python
async def main():
    results = await asyncio.gather(
        fetch("A"),
        fetch("B"),
        fetch("C")
    )
    print(results)  # ['A 完成', 'B 完成', 'C 完成']
```

### 8.4 Agent 场景：并发调用多个工具

```python
async def call_tool(tool_name: str, input: str):
    await asyncio.sleep(1)
    return f"{tool_name} 结果：{input}"

async def agent_run(user_input: str):
    # 同时调用搜索、计算、天气三个工具
    results = await asyncio.gather(
        call_tool("search", user_input),
        call_tool("calculator", "1+1"),
        call_tool("weather", "北京")
    )
    return results

# 总耗时约 1 秒，而非 3 秒
```

### 8.5 Future（了解即可）

Future 是更底层的对象，通常不直接使用。Task 是 Future 的子类。

---

## 9. 超时与取消机制

### 9.1 `asyncio.wait_for()` — 超时控制

```python
import asyncio

async def slow_task():
    await asyncio.sleep(5)
    return "完成"

async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("任务超时")

asyncio.run(main())  # 输出：任务超时
```

### 9.2 Agent 场景：API 调用超时

```python
async def call_llm_with_timeout(prompt: str, timeout: float = 30.0):
    """调用 LLM，带超时保护"""
    try:
        result = await asyncio.wait_for(
            call_llm_api(prompt),
            timeout=timeout
        )
        return result
    except asyncio.TimeoutError:
        return "API 调用超时，请重试"
```

### 9.3 `asyncio.wait()` — 灵活的等待

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成"

async def main():
    tasks = [
        asyncio.create_task(task("A", 1)),
        asyncio.create_task(task("B", 2)),
        asyncio.create_task(task("C", 3))
    ]
    
    # 等待第一个完成
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    
    print(f"第一个完成：{done.pop().result()}")
    
    # 取消剩余任务
    for task in pending:
        task.cancel()

asyncio.run(main())
```

### 9.4 取消任务

```python
async def long_task():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("任务被取消")
        raise  # 重新抛出，让调用者知道

async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(1)
    task.cancel()  # 取消任务
    
    try:
        await task
    except asyncio.CancelledError:
        print("确认任务已取消")

asyncio.run(main())
```

---

## 10. 异步上下文管理器 `async with`

### 10.1 同步上下文管理器回顾

你已经学过 `with` 用于文件操作：

```python
with open("file.txt", "r") as f:
    content = f.read()
# 文件自动关闭
```

### 10.2 异步上下文管理器

```python
import asyncio
import aiofiles

async def read_file():
    async with aiofiles.open("file.txt", "r") as f:
        content = await f.read()
        return content
```

### 10.3 自定义异步上下文管理器

```python
class AsyncDatabaseConnection:
    async def __aenter__(self):
        print("连接数据库")
        await asyncio.sleep(0.1)  # 模拟连接
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("关闭数据库连接")
        await asyncio.sleep(0.1)  # 模拟关闭
    
    async def query(self, sql):
        return f"查询结果：{sql}"

async def main():
    async with AsyncDatabaseConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(result)
    # 自动关闭连接

asyncio.run(main())
```

### 10.4 Agent 场景：HTTP 客户端

```python
import aiohttp

async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
    # session 自动关闭，连接池自动清理
```

**实际应用**：
- HTTP 客户端（aiohttp）
- 数据库连接（asyncpg、motor）
- 文件操作（aiofiles）
- 资源锁（asyncio.Lock）

---

## 11. 异步迭代器 `async for`

### 11.1 同步迭代器回顾

```python
for item in [1, 2, 3]:
    print(item)
```

### 11.2 异步迭代器

```python
import asyncio

class AsyncRange:
    def __init__(self, count):
        self.count = count
        self.current = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current < self.count:
            await asyncio.sleep(0.1)  # 模拟异步操作
            self.current += 1
            return self.current
        raise StopAsyncIteration

async def main():
    async for num in AsyncRange(3):
        print(num)

asyncio.run(main())
```

输出：
```text
1
2
3
```

### 11.3 Agent 场景：流式响应

```python
class StreamingLLMResponse:
    """模拟 LLM 流式输出"""
    def __init__(self, text):
        self.words = text.split()
        self.index = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.index < len(self.words):
            await asyncio.sleep(0.1)  # 模拟网络延迟
            word = self.words[self.index]
            self.index += 1
            return word
        raise StopAsyncIteration

async def stream_response():
    response = StreamingLLMResponse("Hello world from LLM")
    async for word in response:
        print(word, end=" ", flush=True)
    print()

asyncio.run(stream_response())
```

**实际应用**：
- OpenAI/Anthropic 流式 API
- 数据库游标
- 消息队列消费者
- WebSocket 消息流

---

## 12. 异步生成器

### 12.1 同步生成器回顾

```python
def count_up(n):
    for i in range(n):
        yield i

for num in count_up(3):
    print(num)
```

### 12.2 异步生成器

```python
import asyncio

async def async_count_up(n):
    for i in range(n):
        await asyncio.sleep(0.1)
        yield i

async def main():
    async for num in async_count_up(3):
        print(num)

asyncio.run(main())
```

### 12.3 Agent 场景：分批处理大数据

```python
async def fetch_users_batch(batch_size: int = 100):
    """模拟分批从数据库获取用户"""
    total = 1000
    for offset in range(0, total, batch_size):
        await asyncio.sleep(0.1)  # 模拟数据库查询
        batch = [f"user_{i}" for i in range(offset, min(offset + batch_size, total))]
        yield batch

async def process_all_users():
    async for batch in fetch_users_batch(100):
        print(f"处理 {len(batch)} 个用户")
        # 处理这一批用户

asyncio.run(process_all_users())
```

### 12.4 实际应用：LLM 流式输出处理

```python
async def stream_llm_tokens(prompt: str):
    """模拟 LLM 流式返回 token"""
    tokens = ["Hello", " ", "world", "!", " ", "How", " ", "are", " ", "you", "?"]
    for token in tokens:
        await asyncio.sleep(0.05)
        yield token

async def collect_stream():
    full_text = ""
    async for token in stream_llm_tokens("Hi"):
        print(token, end="", flush=True)
        full_text += token
    print(f"\n完整文本：{full_text}")

asyncio.run(collect_stream())
```

---

## 13. 错误处理与异常传播

### 13.1 异步函数中的异常

```python
import asyncio

async def risky_task():
    await asyncio.sleep(1)
    raise ValueError("出错了")

async def main():
    try:
        await risky_task()
    except ValueError as e:
        print(f"捕获异常：{e}")

asyncio.run(main())
```

### 13.2 `gather()` 中的异常处理

默认情况下，`gather()` 遇到异常会立即抛出：

```python
async def task(name, should_fail=False):
    await asyncio.sleep(1)
    if should_fail:
        raise ValueError(f"{name} 失败")
    return f"{name} 成功"

async def main():
    try:
        results = await asyncio.gather(
            task("A"),
            task("B", should_fail=True),
            task("C")
        )
    except ValueError as e:
        print(f"捕获异常：{e}")

asyncio.run(main())
```

### 13.3 `return_exceptions=True` — 收集异常

```python
async def main():
    results = await asyncio.gather(
        task("A"),
        task("B", should_fail=True),
        task("C"),
        return_exceptions=True  # 不抛出，而是返回异常对象
    )
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"任务 {i} 失败：{result}")
        else:
            print(f"任务 {i} 成功：{result}")

asyncio.run(main())
```

输出：
```text
任务 0 成功：A 成功
任务 1 失败：B 失败
任务 2 成功：C 成功
```

### 13.4 Agent 场景：工具调用容错

```python
async def call_tool_safe(tool_name: str, input: str):
    """安全调用工具，捕获异常"""
    try:
        result = await call_tool(tool_name, input)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}

async def agent_run_with_fallback(user_input: str):
    results = await asyncio.gather(
        call_tool_safe("search", user_input),
        call_tool_safe("calculator", "1+1"),
        call_tool_safe("weather", "北京")
    )
    
    # 过滤成功的结果
    successful = [r["result"] for r in results if r["success"]]
    return successful
```

---

## 13. 错误处理与异常传播

### 13.1 异步函数中的异常

```python
import asyncio

async def risky_task():
    await asyncio.sleep(1)
    raise ValueError("出错了")

async def main():
    try:
        await risky_task()
    except ValueError as e:
        print(f"捕获异常：{e}")

asyncio.run(main())
```

### 13.2 `gather()` 中的异常处理

默认情况下，`gather()` 遇到异常会立即抛出：

```python
async def task(name, should_fail=False):
    await asyncio.sleep(1)
    if should_fail:
        raise ValueError(f"{name} 失败")
    return f"{name} 成功"

async def main():
    try:
        results = await asyncio.gather(
            task("A"),
            task("B", should_fail=True),
            task("C")
        )
    except ValueError as e:
        print(f"捕获异常：{e}")

asyncio.run(main())
```

### 13.3 `return_exceptions=True` — 收集异常

```python
async def main():
    results = await asyncio.gather(
        task("A"),
        task("B", should_fail=True),
        task("C"),
        return_exceptions=True  # 不抛出，而是返回异常对象
    )
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"任务 {i} 失败：{result}")
        else:
            print(f"任务 {i} 成功：{result}")

asyncio.run(main())
```

### 13.4 Agent 场景：工具调用容错

```python
async def call_tool_safe(tool_name: str, input: str):
    """安全调用工具，捕获异常"""
    try:
        result = await call_tool(tool_name, input)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

---

## 第三部分：Agent 应用实战模式

---

## 14. Agent 架构设计模式

### 14.1 基础 Agent 架构

```python
from dataclasses import dataclass, field
from typing import List, Optional, Protocol
import asyncio

@dataclass
class Message:
    role: str
    content: str

class Tool(Protocol):
    """工具接口"""
    name: str
    description: str
    
    async def execute(self, **kwargs) -> str:
        ...

class Agent:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.tools: List[Tool] = []
        self.messages: List[Message] = []
    
    def register_tool(self, tool: Tool):
        """注册工具"""
        self.tools.append(tool)
    
    async def call_llm(self, prompt: str) -> str:
        """调用 LLM"""
        await asyncio.sleep(1)  # 模拟 API 调用
        return f"LLM 回复：{prompt}"
    
    async def run(self, user_input: str) -> str:
        """运行 Agent"""
        # 1. 保存用户消息
        self.messages.append(Message(role="user", content=user_input))
        
        # 2. 调用 LLM
        response = await self.call_llm(user_input)
        
        # 3. 保存助手消息
        self.messages.append(Message(role="assistant", content=response))
        
        return response
```

### 14.2 带工具调用的 Agent

```python
@dataclass
class ToolCall:
    tool_name: str
    arguments: dict
    result: Optional[str] = None

class AdvancedAgent(Agent):
    async def run(self, user_input: str) -> str:
        self.messages.append(Message(role="user", content=user_input))
        
        # 1. LLM 决定是否需要调用工具
        llm_response = await self.call_llm(user_input)
        
        # 2. 解析工具调用（简化示例）
        if "search:" in llm_response:
            query = llm_response.split("search:")[1].strip()
            tool_result = await self._call_tool("search", {"query": query})
            
            # 3. 将工具结果返回给 LLM
            final_response = await self.call_llm(f"工具结果：{tool_result}")
            self.messages.append(Message(role="assistant", content=final_response))
            return final_response
        
        self.messages.append(Message(role="assistant", content=llm_response))
        return llm_response
    
    async def _call_tool(self, tool_name: str, args: dict) -> str:
        for tool in self.tools:
            if tool.name == tool_name:
                return await tool.execute(**args)
        raise ValueError(f"工具 {tool_name} 不存在")
```

---

## 15. 工具系统设计

### 15.1 工具基类

```python
from abc import ABC, abstractmethod
from typing import Any, Dict
from dataclasses import dataclass

@dataclass
class ToolParameter:
    name: str
    type: str
    description: str
    required: bool = True

class BaseTool(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def get_parameters(self) -> List[ToolParameter]:
        """返回工具参数定义"""
        pass
    
    @abstractmethod
    async def execute(self, **kwargs) -> Any:
        """执行工具"""
        pass
    
    def to_schema(self) -> Dict:
        """转换为 LLM 工具调用的 schema"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": {
                "type": "object",
                "properties": {
                    p.name: {"type": p.type, "description": p.description}
                    for p in self.get_parameters()
                },
                "required": [p.name for p in self.get_parameters() if p.required]
            }
        }
```

### 15.2 具体工具实现

```python
class SearchTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="search",
            description="搜索互联网信息"
        )
    
    def get_parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(name="query", type="string", description="搜索关键词")
        ]
    
    async def execute(self, query: str) -> str:
        await asyncio.sleep(0.5)  # 模拟网络请求
        return f"搜索结果：关于 {query} 的信息..."

class CalculatorTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="执行数学计算"
        )
    
    def get_parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(name="expression", type="string", description="数学表达式")
        ]
    
    async def execute(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"计算结果：{result}"
        except Exception as e:
            return f"计算错误：{e}"
```

---

## 16. 并发调用与性能优化

### 16.1 并发调用多个工具

```python
class ParallelAgent:
    async def run_parallel_tools(self, user_input: str):
        """并发调用多个工具"""
        results = await asyncio.gather(
            self.search_tool.execute(query=user_input),
            self.calculator_tool.execute(expression="1+1"),
            self.weather_tool.execute(city="北京"),
            return_exceptions=True
        )
        
        # 过滤成功的结果
        successful = [r for r in results if not isinstance(r, Exception)]
        return successful
```

### 16.2 使用 `create_task()` 提前启动

```python
async def optimized_run(self, user_input: str):
    # 立即启动耗时任务
    search_task = asyncio.create_task(self.search_tool.execute(query=user_input))
    
    # 在等待搜索的同时做其他事情
    await self.log_request(user_input)
    await self.update_metrics()
    
    # 现在等待搜索结果
    search_result = await search_task
    return search_result
```

### 16.3 限制并发数量

```python
import asyncio
from asyncio import Semaphore

class RateLimitedAgent:
    def __init__(self, max_concurrent: int = 5):
        self.semaphore = Semaphore(max_concurrent)
    
    async def call_tool_with_limit(self, tool, **kwargs):
        async with self.semaphore:
            return await tool.execute(**kwargs)
    
    async def batch_process(self, queries: List[str]):
        tasks = [
            self.call_tool_with_limit(self.search_tool, query=q)
            for q in queries
        ]
        return await asyncio.gather(*tasks)
```

### 16.4 缓存优化

```python
from functools import lru_cache
from typing import Dict

class CachedAgent:
    def __init__(self):
        self.cache: Dict[str, Any] = {}
    
    async def call_with_cache(self, tool_name: str, **kwargs):
        cache_key = f"{tool_name}:{str(kwargs)}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        result = await self.tools[tool_name].execute(**kwargs)
        self.cache[cache_key] = result
        return result
```

---

## 17. 状态管理与会话持久化

### 17.1 会话状态管理

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
from datetime import datetime

@dataclass
class Session:
    session_id: str
    user_id: str
    messages: List[Message] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    
    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))
    
    def get_history(self, last_n: int = 10) -> List[Message]:
        return self.messages[-last_n:]

class StatefulAgent:
    def __init__(self):
        self.sessions: Dict[str, Session] = {}
    
    def get_or_create_session(self, session_id: str, user_id: str) -> Session:
        if session_id not in self.sessions:
            self.sessions[session_id] = Session(
                session_id=session_id,
                user_id=user_id
            )
        return self.sessions[session_id]
    
    async def run(self, session_id: str, user_id: str, user_input: str) -> str:
        session = self.get_or_create_session(session_id, user_id)
        session.add_message("user", user_input)
        
        # 使用历史消息调用 LLM
        history = session.get_history()
        response = await self.call_llm_with_history(history)
        
        session.add_message("assistant", response)
        return response
```

### 17.2 持久化到文件

```python
import json
from pathlib import Path

class PersistentAgent(StatefulAgent):
    def __init__(self, storage_dir: str = "data/sessions"):
        super().__init__()
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def save_session(self, session_id: str):
        session = self.sessions[session_id]
        file_path = self.storage_dir / f"{session_id}.json"
        
        data = {
            "session_id": session.session_id,
            "user_id": session.user_id,
            "messages": [
                {"role": m.role, "content": m.content}
                for m in session.messages
            ],
            "context": session.context,
            "created_at": session.created_at.isoformat()
        }
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_session(self, session_id: str) -> Optional[Session]:
        file_path = self.storage_dir / f"{session_id}.json"
        
        if not file_path.exists():
            return None
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        session = Session(
            session_id=data["session_id"],
            user_id=data["user_id"],
            context=data["context"]
        )
        
        for msg in data["messages"]:
            session.add_message(msg["role"], msg["content"])
        
        return session
```

---

## 18. 完整示例：生产级 Agent

```python
import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Protocol
from abc import ABC, abstractmethod
import json
from pathlib import Path

# ============ 消息和会话 ============

@dataclass
class Message:
    role: str
    content: str

@dataclass
class Session:
    session_id: str
    messages: List[Message] = field(default_factory=list)
    
    def add_message(self, role: str, content: str):
        self.messages.append(Message(role=role, content=content))

# ============ 工具系统 ============

class Tool(Protocol):
    name: str
    description: str
    
    async def execute(self, **kwargs) -> str:
        ...

class SearchTool:
    name = "search"
    description = "搜索互联网信息"
    
    async def execute(self, query: str) -> str:
        await asyncio.sleep(0.5)
        return f"搜索结果：{query}"

class CalculatorTool:
    name = "calculator"
    description = "执行数学计算"
    
    async def execute(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"计算结果：{result}"
        except Exception as e:
            return f"错误：{e}"

# ============ Agent ============

class ProductionAgent:
    def __init__(self, name: str, storage_dir: str = "data"):
        self.name = name
        self.tools: Dict[str, Tool] = {}
        self.sessions: Dict[str, Session] = {}
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
    
    def register_tool(self, tool: Tool):
        self.tools[tool.name] = tool
    
    async def call_llm(self, messages: List[Message]) -> str:
        """模拟 LLM 调用"""
        await asyncio.sleep(1)
        last_msg = messages[-1].content
        return f"LLM 处理：{last_msg}"
    
    async def call_tool(self, tool_name: str, **kwargs) -> str:
        if tool_name not in self.tools:
            raise ValueError(f"工具 {tool_name} 不存在")
        return await self.tools[tool_name].execute(**kwargs)
    
    def get_or_create_session(self, session_id: str) -> Session:
        if session_id not in self.sessions:
            # 尝试从磁盘加载
            loaded = self._load_session(session_id)
            if loaded:
                self.sessions[session_id] = loaded
            else:
                self.sessions[session_id] = Session(session_id=session_id)
        return self.sessions[session_id]
    
    async def run(self, session_id: str, user_input: str) -> str:
        session = self.get_or_create_session(session_id)
        session.add_message("user", user_input)
        
        # 调用 LLM
        response = await self.call_llm(session.messages)
        session.add_message("assistant", response)
        
        # 保存会话
        self._save_session(session)
        
        return response
    
    def _save_session(self, session: Session):
        file_path = self.storage_dir / f"{session.session_id}.json"
        data = {
            "session_id": session.session_id,
            "messages": [{"role": m.role, "content": m.content} for m in session.messages]
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _load_session(self, session_id: str) -> Optional[Session]:
        file_path = self.storage_dir / f"{session_id}.json"
        if not file_path.exists():
            return None
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        session = Session(session_id=data["session_id"])
        for msg in data["messages"]:
            session.add_message(msg["role"], msg["content"])
        return session

# ============ 使用示例 ============

async def main():
    agent = ProductionAgent("助手")
    agent.register_tool(SearchTool())
    agent.register_tool(CalculatorTool())
    
    response = await agent.run("session_001", "你好")
    print(response)

asyncio.run(main())
```

---

## 19. 知识点总结

### 19.1 面向对象核心概念

| 概念 | 作用 | Agent 应用场景 |
|------|------|---------------|
| `__init__` vs `__new__` | 对象创建与初始化 | 单例模式（全局配置、客户端） |
| `@property` | 属性访问控制 | 计算属性、参数校验 |
| `@staticmethod` | 工具函数 | 数据验证、格式转换 |
| `@classmethod` | 工厂方法 | 从配置创建 Agent |
| 继承与 `super()` | 代码复用 | 工具基类、Agent 基类 |
| `@dataclass` | 数据类 | Message、Session、Config |
| `field()` | 字段配置 | 默认值、私有字段 |
| `frozen=True` | 不可变对象 | 消息历史、配置 |
| `slots=True` | 内存优化 | 大量实例场景 |
| `Protocol` | 接口定义 | 工具接口、可运行对象 |
| `TypedDict` | 结构化字典 | API 响应、JSON 数据 |
| `Literal` | 值限定 | 角色类型、状态枚举 |

### 19.2 异步编程核心概念

| 概念 | 作用 | Agent 应用场景 |
|------|------|---------------|
| `async def` | 定义异步函数 | API 调用、工具执行 |
| `await` | 等待异步结果 | 等待 LLM 响应 |
| `asyncio.run()` | 启动事件循环 | 程序入口 |
| `asyncio.create_task()` | 创建后台任务 | 提前启动耗时操作 |
| `asyncio.gather()` | 并发执行 | 同时调用多个工具 |
| `asyncio.wait()` | 灵活等待 | 超时控制、部分完成 |
| `asyncio.wait_for()` | 超时控制 | API 调用超时保护 |
| `async with` | 异步上下文管理 | HTTP 客户端、数据库连接 |
| `async for` | 异步迭代 | 流式响应、分批处理 |
| 异步生成器 | 流式数据 | LLM 流式输出 |
| `return_exceptions=True` | 异常收集 | 工具调用容错 |
| `Semaphore` | 并发限制 | 速率限制、资源控制 |

### 19.3 设计模式

| 模式 | 实现方式 | 使用场景 |
|------|---------|---------|
| 单例模式 | `__new__` | 全局配置、客户端 |
| 工厂模式 | `@classmethod` | 多种创建方式 |
| 策略模式 | `Protocol` | 可插拔工具 |
| 模板模式 | 抽象基类 | 工具基类 |
| 装饰器模式 | `@property` | 属性增强 |

---

## 20. 学习检查清单

学完本文档后，你应该能够：

### 面向对象部分
- [ ] 解释 `__init__` 和 `__new__` 的区别，并实现单例模式
- [ ] 使用 `@property` 实现计算属性和参数校验
- [ ] 区分实例方法、`@staticmethod`、`@classmethod` 的使用场景
- [ ] 使用继承和 `super()` 实现工具基类
- [ ] 使用 `@dataclass` 的高级特性：`field()`、`__post_init__`、`frozen`、`slots`
- [ ] 使用 `Protocol` 定义接口
- [ ] 使用 `TypedDict` 和 `Literal` 进行类型约束

### 异步编程部分
- [ ] 理解 Event Loop 和协程的工作原理
- [ ] 区分 `coroutine`、`Task`、`Future`
- [ ] 选择合适的并发方式：`create_task()` vs `gather()` vs `wait()`
- [ ] 使用 `wait_for()` 实现超时控制
- [ ] 使用 `async with` 管理资源
- [ ] 使用 `async for` 处理流式数据
- [ ] 实现异步生成器
- [ ] 处理异步代码中的异常
- [ ] 使用 `Semaphore` 限制并发数量

### Agent 应用部分
- [ ] 设计 Agent 基础架构
- [ ] 实现工具系统（基类、具体工具、schema）
- [ ] 实现并发工具调用
- [ ] 实现会话状态管理
- [ ] 实现会话持久化

---

## 21. 学完后的下一步

当你学习完成后，请回复：

```text
我学习完了
```

我会给你出一套**深度测试题**，包括：

1. **概念理解题**（10 题）：检验你对核心概念的理解深度
2. **代码分析题**（5 题）：分析代码问题，说明如何改进
3. **设计题**（2 题）：设计一个完整的 Agent 组件
4. **编码题**（1 题）：实现一个生产级的 Agent 功能

测试题会覆盖：
- `__new__` 单例模式
- `@property` 和计算属性
- `Protocol` 接口设计
- `@dataclass` 高级特性
- Event Loop 原理
- `create_task()` vs `gather()`
- 异步上下文管理器
- 异步生成器
- 错误处理策略
- Agent 架构设计

通过测试后，你将进入：

```text
阶段 4：API 使用与后端服务基础
```

---

**祝学习顺利！记得严格按照要求实现代码，注意缩进和字段名的精确性。**

