# 练习 2：@dataclass + 类型提示
#
# 要求：
# 1. 从 dataclasses 导入 dataclass；
# 2. 用 @dataclass 定义 ToolResult，字段（注意类型提示）：
#    - tool_name: str
#    - success: bool
#    - output: str
# 3. 定义一个普通函数 format_result(result: ToolResult) -> str，
#    返回这一行：
#    [{tool_name}] 成功={success} 输出={output}
# 4. 创建 ToolResult(tool_name="file_reader", success=True, output="读取了 3 行")，
#    print(format_result(...)) 打印出来。
#
# 期望输出（必须完全一致）：
# [file_reader] 成功=True 输出=读取了 3 行

# 在下面开始写：

from dataclasses import dataclass

@dataclass
class ToolResult:
    tool_name:str
    success:bool
    output:str

def format_result(result:ToolResult)->str:
    return f"[{result.tool_name}] 成功={result.success} 输出={result.output}"


data= ToolResult(tool_name='file_reader',success=True,output="读取了 3 行")
print(format_result(data))