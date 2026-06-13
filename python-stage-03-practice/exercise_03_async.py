# 练习 3：异步 + 并发 + 耗时预测
#
# 要求：
# 1. import asyncio；
# 2. 定义异步函数 call_tool(name, delay)：
#    - await asyncio.sleep(delay) 模拟耗时；
#    - 返回字符串：{name} 完成
# 3. 定义 async def main()：
#    - 用 asyncio.gather 并发执行：
#      call_tool("搜索", 2)、call_tool("读文件", 1)、call_tool("写报告", 3)
#    - print 结果列表；
# 4. 用 asyncio.run(main()) 启动。
#
# ── 运行之前，先回答下面两个预测（写在注释里）──
#
# 预测 1：这个程序总耗时大约几秒？
# 你的答案：3
#
# 预测 2：打印出来的列表顺序是什么？
# 你的答案：搜索 读文件 写报告
#
# 写完预测再运行，对照是否和你想的一致。

# 在下面开始写：
import asyncio

async def call_tool(name,delay):
        await asyncio.sleep(delay)
        return f"{name} 完成"
async def main():
    list =  asyncio.gather(call_tool("搜索",2),call_tool("读文件",1),call_tool("写报告",3))
    print(await list) # 这里问什么要用await  asyncio.gather返回的是一个协程对象 需要await才能得到结果

asyncio.run(main())
