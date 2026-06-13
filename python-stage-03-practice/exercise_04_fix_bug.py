# 练习 4：调试题 —— 先预测，再运行，再修复
#
# 下面这段代码是「故意写坏的」，里面有 2 个 bug。
#
# 步骤（严格按顺序，这是练「精通」的关键）：
# 1. 不要运行！先读代码，把你预测的问题写在下面的「预测」注释里；
# 2. 运行它，对照实际报错/输出和你的预测是否一致；
# 3. 修复代码，让它打印出：
#    学习助手 -> 模型回复：已处理 学习 async
#
# ── 你的预测（运行前填写）──
# 预测 bug 1：   name 赋值的时候没有写self
# 预测 bug 2： run前端 不用async
# 预测运行后会发生什么：
# 学习助手 -> 模型回复：已处理 学习 async
# ── 下面是故意写坏的代码 ──

import asyncio


class AsyncAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型回复：已处理 {prompt}"

    async def run(self, user_input):
        reply = await self.call_model(user_input) #这里为啥要await
        return f"{self.name} -> {reply}"


async def main():
    agent =  AsyncAgent("学习助手")  
    print(agent.run("学习 async"))


asyncio.run(main())
