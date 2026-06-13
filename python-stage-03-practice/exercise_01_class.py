# 练习 1：用 class 封装一个工具（class / __init__ / self / 方法）
#
# 要求（严格按字段名和输出格式）：
# 1. 定义 Tool 类；
# 2. __init__ 接收两个参数：name、description，保存到对象属性上；
# 3. 定义方法 describe()，返回这一行（用 f-string）：
#    工具 {name}：{description}
# 4. 定义方法 run(self, arg)，返回这一行：
#    {name} 收到参数：{arg}
# 5. 创建 Tool("file_reader", "读取文件内容")，
#    先 print(工具.describe())，再 print(工具.run("notes.txt"))
#
# 期望输出（必须完全一致）：
# 工具 file_reader：读取文件内容
# file_reader 收到参数：notes.txt

# 在下面开始写：

class Tool:
    def __init__(self,name,description):
        self.name = name
        self.description = description
    def describe(self):
        return f"工具 {self.name}：{self.description}"

    def run(self, arg):
        return f"{self.name} 收到参数：{arg}"
tool = Tool("file_reader", "读取文件内容")
print(tool.describe())
print(tool.run("notes.txt"))