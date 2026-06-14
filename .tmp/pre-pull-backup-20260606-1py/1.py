from dataclasses import dataclass


class user :
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("User created:", self.name)
    def sayHello(self):
        print(f"Hello, I'm, {self.name}")

user =  user("Joe", 20)
user.sayHello()


class LearningRecord :
    def __init(self, name,stage,target):
        self.name = name
        self.stage = stage
        self.target = target
    def summary(self):
        print(f"{self.name} 正在学习 {self.stage} ,目标是 {self.target}")

learnData = LearningRecord("Joe", "Python阶段3", "Agent developer")

@dataclass
class Message(object):
   role:str
   content:str

Message(role="user", content="我正在学习 Agent 开发")

class AsyncLearningAgent:
    def __init(self, name):
        self.name = name
    async def call_model(prompt):
             await asyncio.sleep(1)
             return f"模型已处理：{prompt}"
async def main():

    agent = AsyncLearningAgent("Joe")
    result =  await agent.call_model("我正在学习 Agent 3")
    print(result)
asyncio.run(main())



import asyncio
from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


class AsyncLearningAgent:
    def __init__(self, name):
        self.name = name

    async def call_model(self, prompt):
        await asyncio.sleep(1)
        return f"模型已处理：{prompt}"


    async def run(self, user_input):
        result =  await self.call_model(user_input)
        return result


async def main():
    agent =  AsyncLearningAgent("Joe")
    result = await agent.run("我正在学习 Agent 3")
    print(result)

asyncio.run(main())






