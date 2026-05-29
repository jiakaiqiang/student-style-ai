# Agent 应用开发学习路线：阶段 2 — Python 进阶与脚本能力

> 学习对象：有前端开发经验，正在从 Python 基础进入 Agent 应用开发。
>
> 当前阶段目标：从“会写基础语法”进入“能写小脚本”，为后续调用模型 API、读写文件、管理状态、封装工具函数打基础。

---

## 0. 学习方式

你先学习本文件，并完成最后的练习。

当你学习完成后，直接告诉我：

```text
我学习完了
```

然后我会给你出阶段 2 测试题。你回答后，我会分析你的掌握情况，并判断是否进入阶段 3。

---

## 1. 为什么 Agent 开发需要脚本能力？

真实的 Agent 应用不只是和大模型聊天，它通常还要：

- 读取用户文件；
- 保存任务状态；
- 读取配置；
- 调用 HTTP API；
- 调用模型接口；
- 处理错误；
- 把逻辑封装成工具函数；
- 把结果保存为 JSON。

例如：

```text
用户上传简历
Python 读取文件
调用模型分析简历
生成学习计划
保存学习记录
下一次继续读取学习状态
```

所以这一阶段重点不是复杂算法，而是掌握“脚本式开发能力”。

---

## 2. 文件读写

### 2.1 写入文件

```python
content = "我正在学习 Python，为 Agent 应用开发做准备。"

with open("learning.txt", "w", encoding="utf-8") as file:
    file.write(content)
```

解释：

```python
open("learning.txt", "w", encoding="utf-8")
```

含义：

```text
learning.txt       文件名
w                  写入模式，会覆盖原内容
encoding="utf-8"   使用 UTF-8 编码，支持中文
```

`with` 的作用是：文件使用完成后自动关闭。

---

### 2.2 读取文件

```python
with open("learning.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

解释：

```text
r          read，读取模式
file.read 读取整个文件内容
```

---

### 2.3 追加文件

```python
with open("learning.txt", "a", encoding="utf-8") as file:
    file.write("\n今天学习了文件读写。")
```

解释：

```text
a          append，追加模式
```

追加模式不会覆盖原来的内容。

---

## 3. JSON 文件读写

阶段 1 学过：

```python
json.dumps()
json.loads()
```

这一阶段要再学两个：

```python
json.dump()
json.load()
```

记忆方法：

```text
带 s 的处理字符串：dumps / loads
不带 s 的处理文件：dump / load
```

---

### 3.1 Python 对象写入 JSON 文件

```python
import json

record = {
    "name": "Kai",
    "stage": "Python 阶段 2",
    "completed": False,
    "topics": ["文件读写", "异常处理", "HTTP 请求"]
}

with open("record.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False, indent=2)
```

这里使用的是：

```python
json.dump(record, file, ensure_ascii=False, indent=2)
```

意思是：把 Python 对象 `record` 直接写入 JSON 文件。

---

### 3.2 从 JSON 文件读取 Python 对象

```python
import json

with open("record.json", "r", encoding="utf-8") as file:
    record = json.load(file)

print(record["stage"])
```

这里使用的是：

```python
json.load(file)
```

意思是：从 JSON 文件读取内容，并解析成 Python 对象。

---

## 4. dumps / loads / dump / load 对比

| 方法 | 作用 | 操作对象 |
|---|---|---|
| `json.dumps()` | Python 对象转 JSON 字符串 | 字符串 |
| `json.loads()` | JSON 字符串转 Python 对象 | 字符串 |
| `json.dump()` | Python 对象写入 JSON 文件 | 文件 |
| `json.load()` | JSON 文件读取成 Python 对象 | 文件 |

示例：

```python
import json

user = {"name": "Kai"}

# Python 对象 -> JSON 字符串
json_text = json.dumps(user, ensure_ascii=False, indent=2)

# JSON 字符串 -> Python 对象
parsed_user = json.loads(json_text)

# Python 对象 -> JSON 文件
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, ensure_ascii=False, indent=2)

# JSON 文件 -> Python 对象
with open("user.json", "r", encoding="utf-8") as file:
    loaded_user = json.load(file)
```

---

## 5. 路径处理：pathlib

在 Python 中，推荐用 `pathlib` 处理路径。

```python
from pathlib import Path

file_path = Path("record.json")

print(file_path.exists())
print(file_path.name)
print(file_path.suffix)
```

解释：

```text
exists()   判断路径是否存在
name       文件名
suffix     文件后缀
```

---

### 5.1 创建文件夹

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
```

解释：

```python
exist_ok=True
```

表示如果 `data` 文件夹已经存在，不要报错。

---

### 5.2 拼接路径

```python
from pathlib import Path

data_dir = Path("data")
file_path = data_dir / "record.json"

print(file_path)
```

推荐这样写：

```python
data_dir / "record.json"
```

不要优先手写：

```python
"data/record.json"
```

因为不同操作系统的路径分隔符可能不同，用 `Path` 更安全。

---

## 6. 异常处理

真实程序里，经常会出现错误：

- 文件不存在；
- JSON 格式错误；
- API 请求失败；
- 环境变量不存在；
- 用户传入参数错误。

Python 用 `try...except` 处理错误。

---

### 6.1 文件不存在

```python
try:
    with open("not_exists.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("文件不存在，请检查文件路径。")
```

如果文件不存在，程序不会直接崩溃，而是进入 `except FileNotFoundError`。

---

### 6.2 数字转换失败

```python
try:
    number = int("abc")
    print(number)

except ValueError:
    print("转换数字失败。")
```

---

### 6.3 捕获通用错误

```python
try:
    result = 10 / 0
    print(result)

except Exception as error:
    print("程序出错了：", error)
```

`Exception` 可以捕获大多数错误。

但以后写项目时，优先捕获具体错误类型，例如：

```python
FileNotFoundError
ValueError
KeyError
```

---

## 7. 函数模块化

不要把所有代码都堆在一起。真实项目里要拆成函数。

### 7.1 保存函数

```python
import json


def save_record(record, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(record, file, ensure_ascii=False, indent=2)
```

---

### 7.2 读取函数

```python
import json


def load_record(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)
```

---

### 7.3 主流程函数

```python
def main():
    record = {
        "name": "Kai",
        "stage": "Python 阶段 2"
    }

    save_record(record, "record.json")
    loaded_record = load_record("record.json")
    print(loaded_record["stage"])


main()
```

为什么要拆函数？

```text
逻辑更清晰
可以复用
方便测试
以后可以封装成 Agent 工具
```

---

## 8. HTTP 请求基础

Agent 应用经常需要调用 API，比如：

- 模型 API；
- 搜索 API；
- 天气 API；
- 数据库接口；
- 企业内部接口。

Python 常用 `requests` 发送 HTTP 请求。

安装：

```bash
pip install requests
```

---

### 8.1 GET 请求

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())
```

解释：

```text
requests.get()       发送 GET 请求
response.status_code HTTP 状态码
response.json()      把返回的 JSON 解析成 Python 对象
```

---

### 8.2 带参数的 GET 请求

```python
import requests

params = {
    "q": "python agent development"
}

response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)

data = response.json()

print(data["total_count"])
```

类似前端：

```js
fetch("/api/search?q=python")
```

---

### 8.3 POST 请求

```python
import requests

payload = {
    "name": "Kai",
    "stage": "Python"
}

response = requests.post("https://httpbin.org/post", json=payload)

print(response.status_code)
print(response.json())
```

这里：

```python
json=payload
```

表示把 Python dict 作为 JSON 请求体发送。

类似前端：

```js
fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(payload)
})
```

---

## 9. 环境变量

Agent 应用经常需要 API Key，例如：

```text
ANTHROPIC_API_KEY
OPENAI_API_KEY
SEARCH_API_KEY
DATABASE_URL
```

这些不要直接写在代码里。

错误示例：

```python
api_key = "sk-xxxxxx"
```

正确方式：

```python
import os

api_key = os.getenv("ANTHROPIC_API_KEY")

if api_key is None:
    print("缺少 ANTHROPIC_API_KEY 环境变量")
else:
    print("已读取 API Key")
```

原因：

- 避免泄露密钥；
- 不同环境可以使用不同配置；
- 代码可以安全提交到仓库。

---

## 10. 命令行参数

运行脚本时可以传参数：

```bash
python app.py Kai
```

Python 读取参数：

```python
import sys

name = sys.argv[1]

print(f"你好，{name}")
```

`sys.argv` 是一个列表：

```text
sys.argv[0]  脚本文件名，例如 app.py
sys.argv[1]  第一个参数，例如 Kai
```

更安全的写法：

```python
import sys

if len(sys.argv) < 2:
    print("请传入你的名字")
else:
    name = sys.argv[1]
    print(f"你好，{name}")
```

---

## 11. 完整示例：学习记录脚本

```python
import json
from pathlib import Path


def save_record(record, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(record, file, ensure_ascii=False, indent=2)


def load_record(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    file_path = data_dir / "learning_record.json"

    record = {
        "name": "Kai",
        "role": "frontend developer",
        "target": "Agent developer",
        "stage": "Python 阶段 2",
        "completed": False,
        "topics": ["文件读写", "JSON 文件", "异常处理", "路径处理"]
    }

    save_record(record, file_path)

    loaded_record = load_record(file_path)

    print("学习记录已保存")
    print(loaded_record["stage"])


main()
```

你要理解：

```text
save_record() 负责保存 JSON 文件
load_record() 负责读取 JSON 文件
main() 负责组织主流程
Path("data") 表示 data 文件夹
data_dir.mkdir(exist_ok=True) 创建文件夹
file_path = data_dir / "learning_record.json" 拼接路径
```

---

## 12. Agent 应用中的对应关系

| Python 能力 | Agent 应用中的作用 |
|---|---|
| 文件读写 | 读取用户上传文件、保存模型结果 |
| JSON 文件 | 保存任务状态、学习记录、工具结果 |
| pathlib | 管理项目文件路径 |
| try/except | 处理文件不存在、API 失败、模型返回异常 |
| requests | 调用外部 API 或模型 API |
| os.getenv | 安全读取 API Key |
| 函数封装 | 封装 Agent 工具 |
| 命令行参数 | 写可执行脚本和工具 |

---

## 13. 阶段 2 自查清单

学习完成后，你应该能回答：

1. `with open(..., "w")` 是什么意思？
2. `"r"`、`"w"`、`"a"` 分别是什么模式？
3. `json.dumps()` 和 `json.dump()` 的区别是什么？
4. `json.loads()` 和 `json.load()` 的区别是什么？
5. `Path("data")` 是做什么的？
6. `mkdir(exist_ok=True)` 有什么用？
7. 为什么 Agent 应用要处理异常？
8. 为什么 API Key 不应该写死在代码里？
9. `requests.get()` 和前端 `fetch()` 有什么相似点？
10. 为什么要把代码拆成 `save_record()`、`load_record()`、`main()`？

---

## 14. 阶段 2 练习

请你学习后完成下面练习。

要求：

1. 导入 `json`
2. 导入 `Path`
3. 创建 `data` 文件夹
4. 创建一个学习记录字典 `learning_record`
5. 字典里包含：
   - `name`
   - `role`
   - `target`
   - `stage`
   - `completed`
   - `topics`
6. 把它保存到：

```text
data/stage_02_record.json
```

7. 再从这个 JSON 文件读取回来
8. 打印：

```text
当前阶段：Python 阶段 2
学习目标：Agent developer
```

参考结构：

```python
import json
from pathlib import Path


def save_record(record, file_path):
    ...


def load_record(file_path):
    ...


def main():
    ...


main()
```

---

## 15. 学完后告诉我

学习完成后，直接回复：

```text
我学习完了
```

然后我会给你出阶段 2 测试题，并根据你的答案判断是否进入：

```text
阶段 3：Python 面向对象与异步基础
```
