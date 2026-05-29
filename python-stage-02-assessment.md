# Python 阶段 2 测试题

> 阶段：Python 进阶与脚本能力
>
> 要求：不要查资料，直接根据自己的理解回答。可以按题号回答，不需要特别长，但代码题要尽量写完整。

---

## 一、文件读写基础

### 1. 请解释下面代码是什么意思：

```python
with open("learning.txt", "w", encoding="utf-8") as file:
    file.write("我正在学习 Python")
```

你需要说明：

```text
with open 是做什么的？
"w" 是什么意思？
encoding="utf-8" 是做什么的？
file.write() 是做什么的？
```

---

### 2. 下面三种文件模式分别是什么意思？

```python
"r"
"w"
"a"
```

请回答：

```text
"r":
"w":
"a":
```

---

## 二、JSON 文件题

### 3. 请解释下面 4 个方法的区别：

```python
json.dumps()
json.loads()
json.dump()
json.load()
```

请按下面格式回答：

```text
json.dumps():
json.loads():
json.dump():
json.load():
```

提示：重点区分 **字符串** 和 **文件**。

---

### 4. 下面代码中，哪一行是把 Python 对象写入 JSON 文件？

```python
import json

record = {
    "name": "Kai",
    "stage": "Python 阶段 2"
}

with open("record.json", "w", encoding="utf-8") as file:
    json.dump(record, file, ensure_ascii=False, indent=2)
```

请指出是哪一行，并解释这行代码的作用。

---

## 三、路径处理题

### 5. 请解释下面代码：

```python
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "stage_02_record.json"
```

你需要说明：

```text
Path("data") 是什么？
mkdir(exist_ok=True) 是什么？
data_dir / "stage_02_record.json" 是什么？
```

---

## 四、异常处理题

### 6. 请解释下面代码的执行逻辑：

```python
try:
    with open("not_exists.txt", "r", encoding="utf-8") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("文件不存在")
```

你需要回答：

1. 如果文件存在，会发生什么？
2. 如果文件不存在，会发生什么？
3. 为什么 Agent 应用开发中需要异常处理？

---

## 五、函数模块化题

### 7. 为什么下面这种写法更适合以后做 Agent 应用？

```python
def save_record(record, file_path):
    ...

def load_record(file_path):
    ...

def main():
    ...
```

请你结合以下角度回答：

- 代码清晰度
- 复用
- 测试
- Agent 工具封装

---

## 六、HTTP 请求题

### 8. 请解释下面代码：

```python
import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())
```

你需要回答：

```text
requests.get() 是做什么的？
response.status_code 是什么？
response.json() 是什么？
它和前端 fetch 有什么相似点？
```

---

### 9. 请解释下面 POST 请求：

```python
payload = {
    "name": "Kai",
    "stage": "Python"
}

response = requests.post("https://httpbin.org/post", json=payload)
```

这里的：

```python
json=payload
```

是什么意思？  
它类似前端 `fetch` 里的什么写法？

---

## 七、环境变量题

### 10. 为什么 Agent 应用里的 API Key 不应该直接写死在代码里？

例如不推荐这样写：

```python
api_key = "sk-xxxxxx"
```

请说明原因，并写出 Python 中读取环境变量的代码：

```python
import os

...
```

---

## 八、小编码题

### 11. 请写一段完整 Python 代码，要求：

1. 导入 `json`
2. 从 `pathlib` 导入 `Path`
3. 定义函数 `save_record(record, file_path)`
4. 定义函数 `load_record(file_path)`
5. 在 `main()` 中：
   - 创建 `data` 文件夹
   - 定义 `learning_record` 字典，包含：
     - `name`
     - `role`
     - `target`
     - `stage`
     - `completed`
     - `topics`
   - 把它保存到：

```text
data/stage_02_record.json
```

   - 再从文件读取回来
   - 打印：

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

## 回答格式

请按下面格式回答：

```text
1. ...
2. ...
3. ...
...
11. ...
```

回答完成后，我会分析你的学习结果，并判断你是否通过 **Python 阶段 2**。
