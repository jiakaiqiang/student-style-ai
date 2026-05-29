# Agent 应用开发学习路线：阶段 1 — Python 基础入门

> 学习对象：有前端开发经验，目标转向 Agent / LLM 应用开发。
>
> 当前阶段目标：先建立 Python 编程基础，为后续学习 API 调用、数据处理、异步编程、LLM SDK、工具调用、Agent 框架打基础。

---

## 0. 学习方式说明

接下来我会作为你的一对一 Agent 学习老师，按照下面流程推进：

1. 我给你一份阶段学习文档。
2. 你按照文档学习和练习。
3. 当你告诉我「我学习完了」时，我会给你出题。
4. 你回答后，我会分析：
   - 哪些知识已经掌握；
   - 哪些地方理解不清；
   - 哪些地方容易和前端思维混淆；
   - 是否可以进入下一阶段。
5. 如果没有掌握，我会继续补充讲解和练习。
6. 当我判断你已经掌握该阶段，再进入下一阶段。

---

## 1. 为什么 Agent 应用开发要先学 Python？

虽然前端开发者可以用 JavaScript / TypeScript 开发 AI 应用，但 Python 仍然非常重要，因为：

1. 大量 AI / LLM / Agent 生态首先支持 Python。
   - LangChain
   - LlamaIndex
   - OpenAI SDK
   - Anthropic SDK
   - MCP / 工具调用相关示例
   - 数据处理、向量数据库、RAG 示例

2. Python 更适合快速写脚本和实验。
   - 读取文件
   - 处理 JSON
   - 请求 API
   - 调用模型
   - 组织工具函数
   - 快速验证 Agent 思路

3. 后续 Agent 应用经常需要后端能力。
   你作为前端开发者，已经具备 UI、交互、组件化、状态管理经验。补上 Python 后，可以逐步具备：
   - 后端接口开发；
   - AI 服务封装；
   - 自动化脚本；
   - LLM 工具调用；
   - 多步骤 Agent 工作流开发。

---

## 2. 本阶段学习目标

完成本阶段后，你应该能够：

- 理解 Python 文件如何运行；
- 掌握变量、数据类型、条件判断、循环；
- 掌握 list、dict、tuple、set 的基础用法；
- 会写函数；
- 能理解 Python 和 JavaScript 的主要差异；
- 能写一个简单的命令行小程序；
- 能读写 JSON 数据，为后续 Agent 工具输入输出做准备。

---

## 3. Python 和 JavaScript 的核心区别

你是前端开发者，所以可以先用 JavaScript 对比 Python。

### 3.1 变量声明

JavaScript：

```js
const name = "Kai"
let age = 25
```

Python：

```python
name = "Kai"
age = 25
```

Python 不需要 `let`、`const`、`var`。

---

### 3.2 代码块

JavaScript 使用 `{}`：

```js
if (age >= 18) {
  console.log("adult")
}
```

Python 使用缩进：

```python
if age >= 18:
    print("adult")
```

重点：Python 对缩进非常敏感。一般使用 4 个空格。

---

### 3.3 输出内容

JavaScript：

```js
console.log("hello")
```

Python：

```python
print("hello")
```

---

### 3.4 注释

JavaScript：

```js
// 单行注释
```

Python：

```python
# 单行注释
```

---

## 4. Python 基础语法

### 4.1 基础数据类型

```python
name = "Alice"      # str 字符串
age = 20            # int 整数
height = 1.68       # float 小数
is_student = True   # bool 布尔值
nothing = None      # 空值
```

对应 JS：

```js
const name = "Alice"
const age = 20
const height = 1.68
const isStudent = true
const nothing = null
```

注意：

- Python 布尔值是 `True` / `False`，首字母大写。
- Python 空值是 `None`，不是 `null`。

---

### 4.2 字符串

```python
name = "Alice"
message = "Hello, " + name
print(message)
```

推荐使用 f-string：

```python
name = "Alice"
age = 20
print(f"My name is {name}, I am {age} years old")
```

类似 JS 模板字符串：

```js
console.log(`My name is ${name}, I am ${age} years old`)
```

---

### 4.3 条件判断

```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

注意：

- Python 用 `elif`，不是 `else if`。
- 条件后面要有冒号 `:`。
- 代码块靠缩进。

---

### 4.4 循环

#### for 循环

```python
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)
```

类似 JS：

```js
for (const name of names) {
  console.log(name)
}
```

#### range

```python
for i in range(5):
    print(i)
```

输出：

```text
0
1
2
3
4
```

#### while 循环

```python
count = 0

while count < 3:
    print(count)
    count += 1
```

---

## 5. 常用数据结构

### 5.1 list 列表

类似 JS 数组。

```python
skills = ["HTML", "CSS", "JavaScript"]

print(skills[0])
skills.append("Python")
print(skills)
```

常用操作：

```python
skills = ["HTML", "CSS"]

skills.append("JavaScript")     # 追加
skills.remove("CSS")            # 删除指定值
print(len(skills))               # 长度
print("HTML" in skills)         # 判断是否存在
```

---

### 5.2 dict 字典

类似 JS 对象。

```python
user = {
    "name": "Alice",
    "age": 20,
    "role": "frontend developer"
}

print(user["name"])
print(user.get("email"))
```

修改：

```python
user["age"] = 21
user["city"] = "Shanghai"
```

遍历：

```python
for key, value in user.items():
    print(key, value)
```

---

### 5.3 tuple 元组

不可修改的列表。

```python
point = (10, 20)
print(point[0])
```

---

### 5.4 set 集合

用于去重和集合判断。

```python
tags = {"python", "agent", "python"}
print(tags)
```

输出只会保留一个 `python`。

---

## 6. 函数

JavaScript：

```js
function add(a, b) {
  return a + b
}
```

Python：

```python
def add(a, b):
    return a + b

result = add(1, 2)
print(result)
```

带默认参数：

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Alice")
```

---

## 7. 模块和导入

Python 可以把代码拆成多个文件。

假设有 `utils.py`：

```python
def format_name(name):
    return name.strip().title()
```

在 `main.py` 里使用：

```python
from utils import format_name

print(format_name(" alice "))
```

类似前端中的：

```js
import { formatName } from "./utils"
```

---

## 8. JSON 处理：Agent 开发非常重要

Agent 应用中，经常会处理结构化数据，例如：

- 模型返回的 JSON；
- 工具调用参数；
- API 请求结果；
- 用户配置；
- 对话历史。

Python 处理 JSON：

```python
import json

user = {
    "name": "Alice",
    "skills": ["frontend", "python"]
}

json_text = json.dumps(user, ensure_ascii=False, indent=2)
print(json_text)

parsed_user = json.loads(json_text)
print(parsed_user["name"])
```

重点：

- `json.dumps()`：Python 对象转 JSON 字符串。
- `json.loads()`：JSON 字符串转 Python 对象。

---

## 9. 文件读写

读取文件：

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

写入文件：

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python")
```

读写 JSON 文件：

```python
import json

user = {
    "name": "Alice",
    "role": "frontend developer"
}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=2)

with open("user.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["name"])
```

---

## 10. 小练习

请你完成下面练习。可以新建一个 `stage_01_python_basics.py` 文件来写。

### 练习 1：个人信息输出

定义变量：

- name
- role
- years_of_experience
- target

然后用 f-string 输出一句话，例如：

```text
我是 Kai，一名前端开发者，有 3 年经验，正在学习 Agent 应用开发。
```

---

### 练习 2：技能列表

定义一个列表：

```python
skills = ["HTML", "CSS", "JavaScript"]
```

然后：

1. 添加 `Python`；
2. 判断 `Python` 是否在列表中；
3. 遍历输出每个技能。

---

### 练习 3：用户字典

定义一个字典：

```python
profile = {
    "name": "Kai",
    "role": "frontend developer",
    "learning": "Python"
}
```

然后：

1. 输出 `name`；
2. 新增字段 `target`，值为 `Agent developer`；
3. 遍历输出所有 key 和 value。

---

### 练习 4：函数

写一个函数：

```python
def build_learning_message(name, topic):
    ...
```

调用后返回：

```text
Kai 正在学习 Python，为 Agent 应用开发做准备。
```

---

### 练习 5：JSON

创建一个 Python 字典：

```python
learning_record = {
    "name": "Kai",
    "current_stage": "Python 基础",
    "completed": False,
    "topics": ["变量", "条件判断", "循环", "函数", "JSON"]
}
```

要求：

1. 转成 JSON 字符串并打印；
2. 再从 JSON 字符串解析回 Python 字典；
3. 输出 `current_stage`。

---

## 11. 阶段自查清单

学习完成后，请确认自己是否能回答：

- Python 代码块为什么依赖缩进？
- `list` 和 `dict` 分别对应前端里的什么概念？
- `json.dumps` 和 `json.loads` 的区别是什么？
- `def` 是做什么的？
- Python 中的 `None`、`True`、`False` 和 JS 中的哪些值类似？
- 为什么 Agent 应用开发中 JSON 很重要？

---

## 12. 你学习完后要做什么？

当你学完这份文档，并完成练习后，直接告诉我：

```text
我学习完了
```

然后我会给你出一组测试题，包括：

1. 基础概念题；
2. Python 和 JavaScript 对比题；
3. 代码阅读题；
4. 小编码题；
5. Agent 应用场景理解题。

你回答之后，我会根据你的答案给出学习分析，并决定：

- 是否通过阶段 1；
- 是否需要补强某些知识点；
- 是否进入阶段 2：Python 进阶与脚本能力。
