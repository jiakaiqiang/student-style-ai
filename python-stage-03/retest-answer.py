# Python 阶段 3 复测题 - 参考答案

# ============================================================================
# 一、核心概念快速检查
# ============================================================================

# 1. self 和 __init__ 的作用
# 答：self 是什么？
# self 代表对象实例本身，类似 JS 的 this。

# 答：__init__ 在什么时候被调用？
# 创建对象时自动调用，用来初始化对象的属性。


# 2. 属性 vs 方法
# 答：A 是属性还是方法？
# 属性

# 答：B 是属性还是方法？
# 方法


# 3. dict vs class
# 答：如果只是存储配置数据（比如 {"model": "gpt-4", "temperature": 0.7}），用 dict 还是 class？
# 用 dict

# 答：如果需要定义行为（比如 Agent 有 run() 方法），用 dict 还是 class？
# 用 class


# ============================================================================
# 二、异步核心
# ============================================================================

# 4. 协程对象识别
# 答：x 是字符串 "ok" 吗？如果不是，x 是什么？
# 不是字符串，x 是一个协程对象（coroutine object）。

# 答：要拿到 "ok"，应该怎么写？
# 在异步函数里用 await：x = await fetch()


# 5. await 的位置
# 答：task_b 里调用 task_a() 这一行，缺了什么？
# 缺了 await

# 答：正确写法是什么？
# result = await task_a()


# 6. gather 的顺序
# 答：results 里的顺序是 ['Y 完成', 'Z 完成', 'X 完成']（按完成快慢），还是 ['X 完成', 'Y 完成', 'Z 完成']（按传入顺序）？
# ['X 完成', 'Y 完成', 'Z 完成']（按传入顺序）


# ============================================================================
# 三、常见错误识别
# ============================================================================

# 7. 找错：忘记 self
# 答：这段代码有什么问题？
# __init__ 的第一个参数必须是 self，这里漏了。
# 正确写法：def __init__(self, name):


# 8. 找错：f-string 语法
# 答：这段代码有什么问题？（提示：这是 JS 习惯带过来的）
# Python f-string 不需要 $，应该是 f"Hello, {name}"，不是 f"Hello, ${name}"


# 9. 找错：缺少 await
# 答：这段代码会打印出什么？（不是期望的结果）
# 会打印出协程对象，类似：<coroutine object AsyncAgent.run at 0x...>

# 答：正确应该怎么写？
# print(await agent.run("任务"))


# ============================================================================
# 四、编码题
# ============================================================================

print("=" * 60)
print("复测编码题 - 参考答案")
print("=" * 60)

# 10. 简单 class
print("\n题目 10：简单 class")


class Tool:
    def __init__(self, name):
        self.name = name

    def use(self):
        return f"使用工具：{self.name}"


tool = Tool("搜索")
print(tool.use())


# 11. dataclass
print("\n题目 11：dataclass")

from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool


task = Task(title="学习 Python", done=True)
print(task.title)
print(task.done)


# 12. 异步函数
print("\n题目 12：异步函数")

import asyncio


async def greet(name):
    await asyncio.sleep(0.5)
    return f"Hello, {name}"


async def main():
    result = await greet("Kai")
    print(result)


asyncio.run(main())
