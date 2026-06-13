# Python 阶段 3 测试题

> 阶段：Python 面向对象与异步基础
>
> 要求：不要查资料，凭自己的理解回答。可以按题号作答，概念题不用很长，但要说清楚；代码题要写完整，**注意缩进**，并且**严格按要求的字段名和输出格式**来写。
>
> 难度说明：标了 ⭐ 的是常规题，标了 🔥 的是**拔高题**（答错不影响过关判断，但能帮我看出你的深度）。

---

## 一、class / __init__ / self 基础

### 1. ⭐ 请解释下面这段代码，并和 JS 做对比

```python
class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")


user = User("Kai")
user.say_hello()
```

请回答：

```text
class 是做什么的？
__init__ 类似 JS 里的什么？
self 类似 JS 里的什么？
self.name = name 这一行在做什么？
```

---

### 2. 🔥 执行顺序题

当 Python 执行到 `user = User("Kai")` 这一行时，背后发生了什么？

请按你的理解，把「创建对象」到「say_hello 打印出来」之间发生的步骤大致写出来。

提示：可以从「`User("Kai")` 触发了哪个方法」「`"Kai"` 传给了谁」「`self` 是谁」这几个角度说。

---

## 二、属性与方法（含深入）

### 3. ⭐ 属性和方法有什么区别？

下面代码里，哪个是属性、哪个是方法？

```python
record = LearningRecord("Kai", "Python 阶段 3")
print(record.name)
print(record.summary())
```

---

### 4. 🔥 类属性 vs 实例属性

下面代码会打印出什么？请逐行写出输出，并解释**为什么**。

```python
class Agent:
    species = "AI"          # 写在 class 下面、方法外面

    def __init__(self, name):
        self.name = name     # 写在 __init__ 里面


a = Agent("助手A")
b = Agent("助手B")

print(a.species)
print(b.species)
print(a.name)
print(b.name)
```

请回答：

```text
a.species:
b.species:
a.name:
b.name:
为什么 species 不用写在 __init__ 里也能访问？
```

---

### 5. ⭐ 找错题：忘记 self

下面代码有什么问题？会发生什么？正确应该怎么写？

```python
class User:
    def __init__(name):
        name = name
```

---

## 三、dict 和 class 的区别

### 6. ⭐ 什么时候用 dict，什么时候用 class？

下面两种写法都能表示一个 Agent：

```python
# 写法一
agent = {
    "name": "学习助手",
    "tools": ["读取文件", "保存记录"]
}

# 写法二
class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.tools = []

    def run(self, user_input):
        return f"{self.name} 收到任务：{user_input}"
```

请回答：

```text
dict 更适合做什么？
class 比 dict 多了什么能力？
在 Agent 应用里，这两种你觉得分别会用在什么地方？
```

---

## 四、@dataclass

### 7. ⭐ @dataclass 的作用

```python
from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


message = Message(role="user", content="你好")
```

请回答：

```text
@dataclass 帮你省掉了哪段你本来要手写的代码？
如果不用 @dataclass，上面这个类的 __init__ 你会怎么写？
```

---

### 8. 🔥 什么时候**不**适合用 dataclass？

`dataclass` 主要适合「以存数据为主」的类。

请你想一想：如果一个类**行为很多、逻辑很复杂**（比如一个真正会调模型、调工具、管理对话状态的 Agent），用普通 class 还是 dataclass 更合适？为什么？

---

## 五、类型提示

### 9. ⭐ + 🔥 类型提示

```python
def build_message(name: str, stage: str) -> str:
    return f"{name} 正在学习 {stage}"
```

请回答：

```text
name: str 是什么意思？
-> str 是什么意思？
（拔高）如果我故意传一个数字 build_message(123, 456)，Python 在运行时会报错吗？为什么？
类型提示和 TypeScript 的类型检查，最大的区别是什么？
```

---

## 六、async / await 核心

### 10. 🔥 协程对象题

```python
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "数据加载完成"


x = fetch_data()
print(x)
```

请回答：

```text
async def 定义出来的是「普通函数」还是别的东西？
x = fetch_data() 之后，x 是「字符串 数据加载完成」吗？如果不是，x 大概是什么？
要拿到 "数据加载完成" 这个真正的结果，应该怎么写？
```

---

### 11. ⭐ await 是做什么的？它类似 JS 里的什么？

---

### 12. ⭐ 顶层 await 问题

为什么下面这样直接写会出问题？正确应该怎么写（写出修正后的完整结构）？

```python
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "ok"


result = await fetch_data()   # 这一行
print(result)
```

---

## 七、asyncio.sleep vs time.sleep（深入）

### 13. 🔥 阻塞 vs 非阻塞

```python
# A 写法
import time
time.sleep(1)

# B 写法
import asyncio
await asyncio.sleep(1)
```

请回答：

```text
A 和 B 都是「等 1 秒」，它们最大的区别是什么？
如果在一个异步程序里误用了 time.sleep(1)，会带来什么问题？
```

---

## 八、并发 asyncio.gather（深入）

### 14. 🔥 耗时推理题

```python
import asyncio


async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} 完成"


async def main():
    results = await asyncio.gather(
        task("A", 3),
        task("B", 1),
        task("C", 2)
    )
    print(results)


asyncio.run(main())
```

请回答：

```text
这段程序大约总共耗时几秒？为什么？（不是 3+1+2）
results 列表里元素的顺序，是按「完成快慢」排，还是按「传入顺序」排？
如果把 asyncio.gather 换成下面这样依次 await，总耗时会变成几秒？
    a = await task("A", 3)
    b = await task("B", 1)
    c = await task("C", 2)
```

---

### 15. 🔥 拔高：异步 ≠ 并行

很多人以为「异步 = 多核同时跑、什么都更快」。

请回答：

```text
asyncio 适合「等 IO 的慢操作（调 API、读文件、查数据库）」还是「纯计算的 CPU 密集任务（比如算 1 亿次循环）」？
为什么 asyncio 对纯 CPU 计算几乎没有加速效果？
（用你自己的话说，能说到「单线程 / 一个时间只跑一段代码 / 趁着等待去干别的」这个意思就算到位）
```

---

## 九、调试题

### 16. 🔥 找出下面异步代码的 bug

下面这段代码想打印「模型回复：已处理 学习 Python」，但实际打印出来不对。请指出问题在哪，并给出修正后的代码。

```python
import asyncio


class AsyncAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型回复：已处理 {prompt}"

    async def run(self, user_input):
        result = self.call_model(user_input)     # 这里
        return f"{self.name}: {result}"


async def main():
    agent = AsyncAgent("学习助手")
    print(await agent.run("学习 Python"))


asyncio.run(main())
```

---

## 十、Agent 应用映射

### 17. ⭐ 连线题（用文字回答即可）

请说明下面每个 Python 能力，在 Agent 应用里大概对应什么用途：

```text
class：
__init__：
self：
方法（method）：
@dataclass：
类型提示：
async / await：
asyncio.gather：
```

并补充回答一句：**为什么 Agent 开发经常需要异步？**

---

## 十一、编码题（注意缩进 + 严格按字段名/输出）

### 18. ⭐ 练习 1：学习记录类

要求：

1. 定义 `LearningRecord` 类；
2. `__init__` 接收三个参数：`name`、`stage`、`target`，并保存到对象属性上；
3. 定义 `summary()` 方法，返回**这一行**（注意标点和文字，用 f-string 拼）：

```text
{name} 正在学习 {stage}，目标是 {target}
```

4. 创建一个 `LearningRecord("Kai", "Python 阶段 3", "Agent developer")`，并 `print(记录.summary())`。

---

### 19. ⭐ 练习 2：Message dataclass

要求：

1. 从 `dataclasses` 导入 `dataclass`；
2. 用 `@dataclass` 定义 `Message`，字段：
   - `role: str`
   - `content: str`
3. 创建：

```python
Message(role="user", content="我正在学习 Agent 开发")
```

4. 分别 `print` 出它的 `role` 和 `content`。

---

### 20. ⭐ + 🔥 练习 3：异步 Agent（综合题）

要求严格按下面规格实现：

1. `import asyncio`；
2. 定义 `AsyncLearningAgent` 类；
3. `__init__(self, name)`：把 `name` 存到 `self.name`；
4. 异步方法 `call_model(self, prompt)`：
   - 用 `await asyncio.sleep(1)` 模拟调模型；
   - 返回字符串：`模型已处理：{prompt}`
5. 异步方法 `run(self, user_input)`：
   - 内部 `await self.call_model(user_input)` 拿到结果 `reply`；
   - 返回字符串：`{self.name} -> {reply}`
6. 定义 `async def main()`：
   - 创建 `AsyncLearningAgent("学习助手")`；
   - `await agent.run("学习 async")`；
   - 把结果 `print` 出来；
7. 最后用 `asyncio.run(main())` 启动。

期望输出（你要保证你的代码能打印出**完全一样**的这一行）：

```text
学习助手 -> 模型已处理：学习 async
```

参考骨架（只是结构提示，字段和返回值要按上面要求写）：

```python
import asyncio


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

## 回答格式

请按题号回答，例如：

```text
1. ...
2. ...
...
20.
（贴完整代码）
```

提交后我会按这几个维度分析：

- 已掌握知识点；
- 薄弱点 / 误区；
- 缩进与「严格按需求实现」的纪律；
- 是否通过阶段 3；
- 是否可以进入 **阶段 4：API 使用与后端服务基础**。
