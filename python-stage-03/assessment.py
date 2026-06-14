# Python 阶段 3 正式测试题
#
# 说明：
# - 共 20 题，包含概念题、拔高题（🔥）、调试题、编码题
# - 概念题在注释中回答（用 # 答：... 的格式）
# - 编码题直接在指定位置写代码
# - 完成后运行 python assessment.py 检查代码题是否能跑通
# - ⭐ 标记的是常规题，🔥 标记的是拔高题
#
# 重要提醒：
# 1. 顶层代码 0 个空格，函数/类体 4 个空格
# 2. f-string 是 {x} 不是 ${x}
# 3. 字段名、输出格式严格按要求
# 4. asyncio.gather 结果顺序按传入顺序，不是完成顺序

# ============================================================================
# 一、class / __init__ / self 基础
# ============================================================================

# 1. ⭐ 请解释下面这段代码，并和 JS 做对比
"""
class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}")


user = User("Kai")
user.say_hello()
"""

# 答：class 是做什么的？
#

# 答：__init__ 类似 JS 里的什么？
#

# 答：self 类似 JS 里的什么？
#

# 答：self.name = name 这一行在做什么？
#


# 2. 🔥 执行顺序题
# 当 Python 执行到 user = User("Kai") 这一行时，背后发生了什么？
# 请按你的理解，把「创建对象」到「say_hello 打印出来」之间发生的步骤大致写出来。
#
# 答：
#


# ============================================================================
# 二、属性与方法（含深入）
# ============================================================================

# 3. ⭐ 属性和方法有什么区别？
# 下面代码里，哪个是属性、哪个是方法？
"""
record = LearningRecord("Kai", "Python 阶段 3")
print(record.name)
print(record.summary())
"""
# 答：
#


# 4. 🔥 类属性 vs 实例属性
# 下面代码会打印出什么？请逐行写出输出，并解释为什么。
"""
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
"""
# 答：a.species:
# 答：b.species:
# 答：a.name:
# 答：b.name:
# 答：为什么 species 不用写在 __init__ 里也能访问？
#


# 5. ⭐ 找错题：忘记 self
# 下面代码有什么问题？会发生什么？正确应该怎么写？
"""
class User:
    def __init__(name):
        name = name
"""
# 答：问题是什么？
#

# 答：会发生什么？
#

# 答：正确写法：
#


# ============================================================================
# 三、dict 和 class 的区别
# ============================================================================

# 6. ⭐ 什么时候用 dict，什么时候用 class？
# 答：dict 更适合做什么？
#

# 答：class 比 dict 多了什么能力？
#

# 答：在 Agent 应用里，这两种你觉得分别会用在什么地方？
#


# ============================================================================
# 四、@dataclass
# ============================================================================

# 7. ⭐ @dataclass 的作用
# 答：@dataclass 帮你省掉了哪段你本来要手写的代码？
#

# 答：如果不用 @dataclass，Message 类的 __init__ 你会怎么写？
#


# 8. 🔥 什么时候**不**适合用 dataclass？
# 答：如果一个类行为很多、逻辑很复杂（比如一个真正会调模型、调工具、管理对话状态的 Agent），
#     用普通 class 还是 dataclass 更合适？为什么？
#


# ============================================================================
# 五、类型提示
# ============================================================================

# 9. ⭐ + 🔥 类型提示
"""
def build_message(name: str, stage: str) -> str:
    return f"{name} 正在学习 {stage}"
"""
# 答：name: str 是什么意思？
#

# 答：-> str 是什么意思？
#

# 答（拔高）：如果我故意传一个数字 build_message(123, 456)，Python 在运行时会报错吗？为什么？
#

# 答：类型提示和 TypeScript 的类型检查，最大的区别是什么？
#


# ============================================================================
# 六、async / await 核心
# ============================================================================

# 10. 🔥 协程对象题
"""
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "数据加载完成"


x = fetch_data()
print(x)
"""
# 答：async def 定义出来的是「普通函数」还是别的东西？
#

# 答：x = fetch_data() 之后，x 是「字符串 数据加载完成」吗？如果不是，x 大概是什么？
#

# 答：要拿到 "数据加载完成" 这个真正的结果，应该怎么写？
#


# 11. ⭐ await 是做什么的？它类似 JS 里的什么？
# 答：
#


# 12. ⭐ 顶层 await 问题
# 为什么下面这样直接写会出问题？正确应该怎么写（写出修正后的完整结构）？
"""
import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return "ok"


result = await fetch_data()   # 这一行
print(result)
"""
# 答：为什么会出问题？
#

# 答：正确写法（写出完整代码结构）：
#


# ============================================================================
# 七、asyncio.sleep vs time.sleep（深入）
# ============================================================================

# 13. 🔥 阻塞 vs 非阻塞
# 答：time.sleep(1) 和 await asyncio.sleep(1) 都是「等 1 秒」，它们最大的区别是什么？
#

# 答：如果在一个异步程序里误用了 time.sleep(1)，会带来什么问题？
#


# ============================================================================
# 八、并发 asyncio.gather（深入）
# ============================================================================

# 14. 🔥 耗时推理题
"""
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
"""
# 答：这段程序大约总共耗时几秒？为什么？
#

# 答：results 列表里元素的顺序，是按「完成快慢」排，还是按「传入顺序」排？
#

# 答：如果把 asyncio.gather 换成依次 await，总耗时会变成几秒？
#     a = await task("A", 3)
#     b = await task("B", 1)
#     c = await task("C", 2)
#


# 15. 🔥 拔高：异步 ≠ 并行
# 答：asyncio 适合「等 IO 的慢操作（调 API、读文件、查数据库）」还是「纯计算的 CPU 密集任务（比如算 1 亿次循环）」？
#

# 答：为什么 asyncio 对纯 CPU 计算几乎没有加速效果？
#


# ============================================================================
# 九、调试题
# ============================================================================

# 16. 🔥 找出下面异步代码的 bug
# 下面这段代码想打印「学习助手: 模型回复：已处理 学习 Python」，但实际打印出来不对。
# 请指出问题在哪，并在下面写出修正后的代码。
"""
import asyncio


class AsyncAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型回复：已处理 {prompt}"

    async def run(self, user_input):
        result = self.call_model(user_input)     # 这里有问题
        return f"{self.name}: {result}"


async def main():
    agent = AsyncAgent("学习助手")
    print(await agent.run("学习 Python"))


asyncio.run(main())
"""
# 答：问题在哪？
#

# 修正后的代码（写在下面，确保能运行）：
# import asyncio
#
#


# ============================================================================
# 十、Agent 应用映射
# ============================================================================

# 17. ⭐ 连线题（用文字回答即可）
# 答：class 在 Agent 应用里对应什么用途？
#

# 答：__init__ 在 Agent 应用里对应什么用途？
#

# 答：self 在 Agent 应用里对应什么用途？
#

# 答：方法（method）在 Agent 应用里对应什么用途？
#

# 答：@dataclass 在 Agent 应用里对应什么用途？
#

# 答：类型提示在 Agent 应用里对应什么用途？
#

# 答：async / await 在 Agent 应用里对应什么用途？
#

# 答：asyncio.gather 在 Agent 应用里对应什么用途？
#

# 答：为什么 Agent 开发经常需要异步？
#


# ============================================================================
# 十一、编码题（可运行部分）
# ============================================================================

print("=" * 60)
print("编码题测试")
print("=" * 60)

# 18. ⭐ 练习 1：学习记录类
# 要求：
# 1. 定义 LearningRecord 类
# 2. __init__ 接收三个参数：name、stage、target，并保存到对象属性上
# 3. 定义 summary() 方法，返回这一行（注意标点和文字，用 f-string 拼）：
#    {name} 正在学习 {stage}，目标是 {target}
# 4. 创建一个 LearningRecord("Kai", "Python 阶段 3", "Agent developer")，并 print(记录.summary())
#
# 期望输出：
# Kai 正在学习 Python 阶段 3，目标是 Agent developer

print("\n题目 18：学习记录类")

# 在下面写代码：


# 19. ⭐ 练习 2：Message dataclass
# 要求：
# 1. 从 dataclasses 导入 dataclass
# 2. 用 @dataclass 定义 Message，字段：
#    - role: str
#    - content: str
# 3. 创建 Message(role="user", content="我正在学习 Agent 开发")
# 4. 分别 print 出它的 role 和 content
#
# 期望输出：
# user
# 我正在学习 Agent 开发

print("\n题目 19：Message dataclass")

# 在下面写代码：


# 20. ⭐ + 🔥 练习 3：异步 Agent（综合题）
# 要求严格按下面规格实现：
# 1. import asyncio
# 2. 定义 AsyncLearningAgent 类
# 3. __init__(self, name)：把 name 存到 self.name
# 4. 异步方法 call_model(self, prompt)：
#    - 用 await asyncio.sleep(1) 模拟调模型
#    - 返回字符串：模型已处理：{prompt}
# 5. 异步方法 run(self, user_input)：
#    - 内部 await self.call_model(user_input) 拿到结果 reply
#    - 返回字符串：{self.name} -> {reply}
# 6. 定义 async def main()：
#    - 创建 AsyncLearningAgent("学习助手")
#    - await agent.run("学习 async")
#    - 把结果 print 出来
# 7. 最后用 asyncio.run(main()) 启动
#
# 期望输出：
# 学习助手 -> 模型已处理：学习 async

print("\n题目 20：异步 Agent")

# 在下面写代码：
