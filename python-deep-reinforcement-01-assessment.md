# Python 深度强化第 1 课测试：运行模型、变量、类型、对象与精确性

本测试用于检查你是否真正掌握第 1 课的核心内容。回答时不要只写“大概意思”，要精确说明运行行为、错误原因、大小写、字段声明、对象创建和导入名称。

---

## 1. 执行顺序

Python 代码为什么是“从上到下执行”？

下面代码会不会报错？为什么？

```python
print(name)
name = "Alice"
```

---

## 2. 布尔值大小写

为什么 `True` 可以，`true` 不可以？

这和 JavaScript 有什么区别？

---

## 3. import 精确性

下面导入有什么问题？请写出正确版本。

```python
from faseapi import FastAPI,HttpException
```

---

## 4. BaseModel 字段声明

解释这段代码里每一行的作用：

```python
from pydantic import BaseModel

class UserRequest(BaseModel):
    user_id: str
    age: int
```

重点说明：

- `class UserRequest(BaseModel)` 是什么意思？
- `user_id: str` 是不是赋值？
- `age: int` 在运行和校验中有什么作用？

---

## 5. 定义类 vs 创建对象

下面这句是在“定义类”还是“创建对象”？为什么？

```python
user = UserRequest(user_id="u_001", age=20)
```

---

## 6. 大小写敏感

`HTTPException` 为什么不能写成 `HttpException`？

这只是代码风格问题吗？如果写错，工程上会有什么后果？

---

## 7. 类型影响运行行为

下面两段代码输出分别是什么？为什么？

```python
print(1 + 2)
print("1" + "2")
```

---

## 8. 小编码题

写一段可以运行的 Python 代码，要求：

- 从 `pydantic` 导入 `BaseModel`
- 定义 `TaskRequest`
- 字段包括：
  - `task_id: str`
  - `title: str`
  - `completed: bool`
- 创建一个对象：
  - `task_id` 为 `"t_001"`
  - `title` 为 `"learn python"`
  - `completed` 为 `False`
- 打印这个对象

要求：

- 顶层代码必须 0 个空格缩进
- 类内部字段必须 4 个空格缩进
- `BaseModel`、`False`、字段名必须大小写完全正确
- 代码必须能真实运行

