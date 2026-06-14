# Python 阶段 3 正式测试题 - 参考答案
#
# 注意：这是参考答案，你的答案可能和这个不完全一样，只要核心理解正确即可。

# ============================================================================
# 一、class / __init__ / self 基础
# ============================================================================

# 1. ⭐ 请解释下面这段代码，并和 JS 做对比

# 答：class 是做什么的？
# 定义一个类（模板），用来创建对象。类似 JS 的 class。

# 答：__init__ 类似 JS 里的什么？
# 类似 JS 的 constructor，用来初始化对象。

# 答：self 类似 JS 里的什么？
# 类似 JS 的 this，代表当前对象实例。

# 答：self.name = name 这一行在做什么？
# 把传入的参数 name 保存到对象的 name 属性上。


# 2. 🔥 执行顺序题
# 答：
# 1. Python 看到 User("Kai")，调用 User 类
# 2. 触发 __init__ 方法，self 指向新创建的对象
# 3. "Kai" 作为 name 参数传入
# 4. self.name = name 把 "Kai" 保存到对象的 name 属性上
# 5. 对象创建完成，赋值给变量 user
# 6. user.say_hello() 调用对象的 say_hello 方法
# 7. 方法内部通过 self.name 读取到 "Kai"
# 8. 打印 "Hello, Kai"


# ============================================================================
# 二、属性与方法（含深入）
# ============================================================================

# 3. ⭐ 属性和方法有什么区别？
# 答：
# record.name 是属性，直接访问对象存储的数据
# record.summary() 是方法，调用一个函数，可以执行逻辑和返回计算结果


# 4. 🔥 类属性 vs 实例属性
# 答：a.species: AI
# 答：b.species: AI
# 答：a.name: 助手A
# 答：b.name: 助手B
# 答：为什么 species 不用写在 __init__ 里也能访问？
# 因为 species 是类属性，定义在类的顶层，被所有实例共享。
# name 是实例属性，每个实例有自己独立的值。


# 5. ⭐ 找错题：忘记 self
# 答：问题是什么？
# __init__ 方法的第一个参数必须是 self，这里漏了。

# 答：会发生什么？
# 运行时会报错：TypeError: __init__() takes 1 positional argument but 2 were given
# 因为 Python 会自动把对象实例作为第一个参数传进来。

# 答：正确写法：
# def __init__(self, name):
#     self.name = name


# ============================================================================
# 三、dict 和 class 的区别
# ============================================================================

# 6. ⭐ 什么时候用 dict，什么时候用 class？
# 答：dict 更适合做什么？
# 适合存储临时数据、配置、JSON 数据等，结构简单、灵活、不需要方法的场景。

# 答：class 比 dict 多了什么能力？
# 可以定义方法（行为），可以用 __init__ 初始化，可以用类型提示，代码更结构化和可维护。

# 答：在 Agent 应用里，这两种你觉得分别会用在什么地方？
# dict：存储 API 响应数据、配置参数、工具调用参数等
# class：定义 Agent 类、Message 类、Tool 类等，封装行为和状态


# ============================================================================
# 四、@dataclass
# ============================================================================

# 7. ⭐ @dataclass 的作用
# 答：@dataclass 帮你省掉了哪段你本来要手写的代码？
# 自动生成 __init__ 方法，不用手动写 self.role = role, self.content = content

# 答：如果不用 @dataclass，Message 类的 __init__ 你会怎么写？
# def __init__(self, role: str, content: str):
#     self.role = role
#     self.content = content


# 8. 🔥 什么时候**不**适合用 dataclass？
# 答：
# 用普通 class 更合适。
# dataclass 适合「数据容器」，主要用来存数据。
# 如果类有复杂的初始化逻辑、很多方法、内部状态管理，用普通 class 更灵活。


# ============================================================================
# 五、类型提示
# ============================================================================

# 9. ⭐ + 🔥 类型提示
# 答：name: str 是什么意思？
# 类型提示，表示 name 参数期望是 str 类型。

# 答：-> str 是什么意思？
# 返回值类型提示，表示这个函数返回 str 类型。

# 答（拔高）：如果我故意传一个数字 build_message(123, 456)，Python 在运行时会报错吗？为什么？
# 不会报错。Python 的类型提示只是「提示」，不强制检查。
# 代码会继续运行，只是 f-string 会把 123 和 456 转成字符串。
# 需要用 mypy 这样的工具才能在运行前检查类型。

# 答：类型提示和 TypeScript 的类型检查，最大的区别是什么？
# Python 类型提示是可选的，运行时不检查，主要用于 IDE 提示和静态检查工具。
# TypeScript 类型检查是强制的，编译时就会报错，运行时就是 JavaScript 了。


# ============================================================================
# 六、async / await 核心
# ============================================================================

# 10. 🔥 协程对象题
# 答：async def 定义出来的是「普通函数」还是别的东西？
# 是协程函数（coroutine function），调用它会返回一个协程对象，不会立即执行。

# 答：x = fetch_data() 之后，x 是「字符串 数据加载完成」吗？如果不是，x 大概是什么？
# 不是字符串，x 是一个协程对象（coroutine object）。

# 答：要拿到 "数据加载完成" 这个真正的结果，应该怎么写？
# 在异步函数里用 await：
# async def main():
#     x = await fetch_data()
#     print(x)
# asyncio.run(main())


# 11. ⭐ await 是做什么的？它类似 JS 里的什么？
# 答：
# await 用来等待一个异步操作完成，拿到真正的结果。
# 类似 JS 的 await，用法和作用基本一样。


# 12. ⭐ 顶层 await 问题
# 答：为什么会出问题？
# Python 不允许在顶层（非异步函数里）直接用 await。
# await 只能在 async def 定义的异步函数内部使用。

# 答：正确写法（写出完整代码结构）：
# import asyncio
#
# async def fetch_data():
#     await asyncio.sleep(1)
#     return "ok"
#
# async def main():
#     result = await fetch_data()
#     print(result)
#
# asyncio.run(main())


# ============================================================================
# 七、asyncio.sleep vs time.sleep（深入）
# ============================================================================

# 13. 🔥 阻塞 vs 非阻塞
# 答：time.sleep(1) 和 await asyncio.sleep(1) 都是「等 1 秒」，它们最大的区别是什么？
# time.sleep(1) 是阻塞的，整个程序卡住 1 秒，什么都不能干。
# await asyncio.sleep(1) 是非阻塞的，等待期间可以切换去执行其他异步任务。

# 答：如果在一个异步程序里误用了 time.sleep(1)，会带来什么问题？
# 会阻塞整个事件循环，其他异步任务也被卡住，失去了异步的意义。


# ============================================================================
# 八、并发 asyncio.gather（深入）
# ============================================================================

# 14. 🔥 耗时推理题
# 答：这段程序大约总共耗时几秒？为什么？
# 约 3 秒。因为三个任务并发执行，总耗时取决于最慢的那个（task A 需要 3 秒）。

# 答：results 列表里元素的顺序，是按「完成快慢」排，还是按「传入顺序」排？
# 按传入顺序排。gather 会等所有任务完成，然后按传入顺序返回结果。
# 所以是 ['A 完成', 'B 完成', 'C 完成']，不是 ['B 完成', 'C 完成', 'A 完成']。

# 答：如果把 asyncio.gather 换成依次 await，总耗时会变成几秒？
# 3 + 1 + 2 = 6 秒。因为变成了串行执行，A 跑完才跑 B，B 跑完才跑 C。


# 15. 🔥 拔高：异步 ≠ 并行
# 答：asyncio 适合「等 IO 的慢操作（调 API、读文件、查数据库）」还是「纯计算的 CPU 密集任务（比如算 1 亿次循环）」？
# 适合等 IO 的慢操作。

# 答：为什么 asyncio 对纯 CPU 计算几乎没有加速效果？
# asyncio 是单线程的，同一时间只能执行一段代码，靠「在等待时切换任务」来提高效率。
# 纯 CPU 计算没有等待时间，一直在占用 CPU，切换也没意义。
# 要加速 CPU 密集任务需要用多进程（multiprocessing）。


# ============================================================================
# 九、调试题
# ============================================================================

# 16. 🔥 找出下面异步代码的 bug
# 答：问题在哪？
# async def run 方法里，调用 self.call_model(user_input) 时忘了加 await。
# 导致 result 是一个协程对象，不是字符串。

# 修正后的代码：
import asyncio


class AsyncAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型回复：已处理 {prompt}"

    async def run(self, user_input):
        result = await self.call_model(user_input)  # 加上 await
        return f"{self.name}: {result}"


async def main():
    agent = AsyncAgent("学习助手")
    print(await agent.run("学习 Python"))


# asyncio.run(main())  # 取消注释可以运行


# ============================================================================
# 十、Agent 应用映射
# ============================================================================

# 17. ⭐ 连线题
# 答：class 在 Agent 应用里对应什么用途？
# 定义 Agent、Tool、Message 等核心组件的结构。

# 答：__init__ 在 Agent 应用里对应什么用途？
# 初始化 Agent 的配置、模型、工具列表、会话状态等。

# 答：self 在 Agent 应用里对应什么用途？
# 访问 Agent 对象自身的状态和方法，比如 self.tools、self.call_model()。

# 答：方法（method）在 Agent 应用里对应什么用途？
# 封装 Agent 的行为，比如 run()、call_tool()、save_history() 等。

# 答：@dataclass 在 Agent 应用里对应什么用途？
# 定义数据结构，比如 Message、ToolCall、ToolResult 等。

# 答：类型提示在 Agent 应用里对应什么用途？
# 让 IDE 提示更准确，让代码更易读，方便团队协作和类型检查。

# 答：async / await 在 Agent 应用里对应什么用途？
# 调用 LLM API、调用外部工具时不阻塞，可以并发处理多个请求。

# 答：asyncio.gather 在 Agent 应用里对应什么用途？
# 并发调用多个工具、同时查询多个数据源，提高 Agent 响应速度。

# 答：为什么 Agent 开发经常需要异步？
# Agent 需要调用 LLM API、调用外部工具、查询数据库等 IO 操作，
# 这些操作很慢，用异步可以在等待时处理其他任务，提高效率和并发能力。


# ============================================================================
# 十一、编码题（可运行部分）
# ============================================================================

print("=" * 60)
print("编码题测试 - 参考答案")
print("=" * 60)

# 18. ⭐ 练习 1：学习记录类
print("\n题目 18：学习记录类")


class LearningRecord:
    def __init__(self, name, stage, target):
        self.name = name
        self.stage = stage
        self.target = target

    def summary(self):
        return f"{self.name} 正在学习 {self.stage}，目标是 {self.target}"


record = LearningRecord("Kai", "Python 阶段 3", "Agent developer")
print(record.summary())


# 19. ⭐ 练习 2：Message dataclass
print("\n题目 19：Message dataclass")

from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


msg = Message(role="user", content="我正在学习 Agent 开发")
print(msg.role)
print(msg.content)


# 20. ⭐ + 🔥 练习 3：异步 Agent（综合题）
print("\n题目 20：异步 Agent")


class AsyncLearningAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型已处理：{prompt}"

    async def run(self, user_input):
        reply = await self.call_model(user_input)
        return f"{self.name} -> {reply}"


async def main():
    agent = AsyncLearningAgent("学习助手")
    result = await agent.run("学习 async")
    print(result)


asyncio.run(main())
