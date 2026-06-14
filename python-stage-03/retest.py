# Python 阶段 3 复测题
#
# 说明：
# - 如果正式测试没通过，用这套题进行针对性复测
# - 题目更简洁，聚焦核心概念和常见错误点
# - 完成后运行 python retest.py 检查代码题是否能跑通

# ============================================================================
# 一、核心概念快速检查
# ============================================================================

# 1. self 和 __init__ 的作用
# 用一句话解释：
# 答：self 是什么？
#

# 答：__init__ 在什么时候被调用？
#


# 2. 属性 vs 方法
"""
agent.name          # A
agent.run()         # B
"""
# 答：A 是属性还是方法？
#

# 答：B 是属性还是方法？
#


# 3. dict vs class
# 答：如果只是存储配置数据（比如 {"model": "gpt-4", "temperature": 0.7}），用 dict 还是 class？
#

# 答：如果需要定义行为（比如 Agent 有 run() 方法），用 dict 还是 class？
#


# ============================================================================
# 二、异步核心
# ============================================================================

# 4. 协程对象识别
"""
async def fetch():
    return "ok"

x = fetch()
"""
# 答：x 是字符串 "ok" 吗？如果不是，x 是什么？
#

# 答：要拿到 "ok"，应该怎么写？
#


# 5. await 的位置
"""
async def task_a():
    await asyncio.sleep(1)
    return "A"

async def task_b():
    result = task_a()    # 这一行
    return result
"""
# 答：task_b 里调用 task_a() 这一行，缺了什么？
#

# 答：正确写法是什么？
#


# 6. gather 的顺序
"""
results = await asyncio.gather(
    task("X", 5),
    task("Y", 1),
    task("Z", 3)
)
"""
# 答：results 里的顺序是 ['Y 完成', 'Z 完成', 'X 完成']（按完成快慢），还是 ['X 完成', 'Y 完成', 'Z 完成']（按传入顺序）？
#


# ============================================================================
# 三、常见错误识别
# ============================================================================

# 7. 找错：忘记 self
"""
class Tool:
    def __init__(name):
        self.name = name
"""
# 答：这段代码有什么问题？
#


# 8. 找错：f-string 语法
"""
name = "Kai"
print(f"Hello, ${name}")
"""
# 答：这段代码有什么问题？（提示：这是 JS 习惯带过来的）
#


# 9. 找错：缺少 await
"""
async def main():
    agent = AsyncAgent("助手")
    print(agent.run("任务"))
"""
# 答：这段代码会打印出什么？（不是期望的结果）
#

# 答：正确应该怎么写？
#


# ============================================================================
# 四、编码题
# ============================================================================

print("=" * 60)
print("复测编码题")
print("=" * 60)

# 10. 简单 class
# 要求：
# 1. 定义 Tool 类
# 2. __init__ 接收 name 参数，保存到 self.name
# 3. 定义 use() 方法，返回字符串：使用工具：{self.name}
# 4. 创建 Tool("搜索")，print(工具.use())
#
# 期望输出：
# 使用工具：搜索

print("\n题目 10：简单 class")

# 在下面写代码：


# 11. dataclass
# 要求：
# 1. 从 dataclasses 导入 dataclass
# 2. 用 @dataclass 定义 Task，字段：title: str, done: bool
# 3. 创建 Task(title="学习 Python", done=True)
# 4. print 出 title 和 done
#
# 期望输出：
# 学习 Python
# True

print("\n题目 11：dataclass")

# 在下面写代码：


# 12. 异步函数
# 要求：
# 1. import asyncio
# 2. 定义 async def greet(name)：
#    - await asyncio.sleep(0.5)
#    - 返回字符串：Hello, {name}
# 3. 定义 async def main()：
#    - await greet("Kai")
#    - 把结果 print 出来
# 4. asyncio.run(main())
#
# 期望输出：
# Hello, Kai

print("\n题目 12：异步函数")

# 在下面写代码：
