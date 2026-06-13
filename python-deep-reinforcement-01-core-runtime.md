# Python 深度强化第 1 课：运行模型、变量、类型、对象与精确性

这一课不讲新框架，只解决一个核心问题：你写的 Python 代码到底是如何被解释器执行的。

如果这一层不稳，后面写 FastAPI、LLM SDK、Agent 工具都会出现低级但致命的问题，比如：

- 模块名拼错；
- 大小写写错；
- `true` 和 `True` 混用；
- 类和对象分不清；
- 字段声明和赋值分不清；
- 代码看起来像那么回事，但运行直接失败。

这类问题不是“小粗心”。在工程里，它们会导致服务无法启动、接口不可用、部署失败。

---

## 1. Python 代码是从上到下执行的

示例：

```python
print("A")
print("B")
print("C")
```

执行顺序是：

```text
A
B
C
```

Python 不会先看你后面有没有定义某个变量，再回头帮你补。执行到哪一行，就要求那一行依赖的名字已经存在。

错误示例：

```python
print(name)

name = "Alice"
```

这会报错，因为执行 `print(name)` 时，`name` 还没有被定义。

正确示例：

```python
name = "Alice"

print(name)
```

---

## 2. Python 对大小写敏感

这三个名字在 Python 里完全不同：

```python
name
Name
NAME
```

所以：

```python
HTTPException
HttpException
httpexception
```

也是三个不同的名字。

FastAPI 中正确的是：

```python
from fastapi import HTTPException
```

如果写成：

```python
from fastapi import HttpException
```

Python 会去 `fastapi` 模块里找一个叫 `HttpException` 的对象。找不到就报错。

结论：

```text
大小写不是风格问题，是名字是否存在的问题。
```

---

## 3. Python 的布尔值和空值

Python 使用：

```python
True
False
None
```

JavaScript 使用：

```javascript
true
false
null
```

错误示例：

```python
accepted = true
```

Python 会把 `true` 当成一个变量名去找。如果没有定义过 `true`，就会报错。

正确示例：

```python
accepted = True
```

结论：

```text
Python 不是 JavaScript。
Python 的内置常量首字母大写：True、False、None。
```

---

## 4. import 是加载模块和名字

示例：

```python
from fastapi import FastAPI, HTTPException
```

这句话的意思是：

```text
从 fastapi 模块中取出 FastAPI 和 HTTPException 这两个名字。
```

模块名必须正确：

```python
fastapi
```

不是：

```python
faseapi
```

名字也必须正确：

```python
HTTPException
```

不是：

```python
HttpException
```

工程要求：

```text
import 写错，程序通常直接启动失败。
```

---

## 5. 变量是名字绑定，不是盒子

示例：

```python
age = 18
```

可以理解为：

```text
名字 age 绑定到对象 18。
```

再看：

```python
age = 18
age = 20
```

这不是把盒子里的值从 18 改成 20，而是让名字 `age` 重新绑定到另一个对象。

对初学阶段，你可以暂时理解为“变量保存值”，但后面理解对象、引用、可变类型时，必须知道 Python 更准确的模型是：

```text
变量名 -> 对象
```

---

## 6. 类型会影响运行行为

示例：

```python
print(1 + 2)
```

输出：

```text
3
```

示例：

```python
print("1" + "2")
```

输出：

```text
12
```

看起来都是 `+`，但因为类型不同，行为不同。

所以 API 中的字段类型不是装饰：

```python
class UserRequest(BaseModel):
    age: int
```

这表示 `age` 应该是整数。如果传错类型，Pydantic / FastAPI 会进行校验。

---

## 7. 定义类和创建对象不是一回事

定义类：

```python
class User:
    def __init__(self, name: str):
        self.name = name
```

这只是定义了一种对象结构。

创建对象：

```python
user = User("Alice")
```

这才是真正创建一个对象。

类像“模板”，对象像“根据模板做出来的具体实例”。

前端类比：

```javascript
class User {
  constructor(name) {
    this.name = name
  }
}

const user = new User("Alice")
```

Python 不写 `new`：

```python
user = User("Alice")
```

---

## 8. BaseModel 中的字段声明不是赋值

示例：

```python
from pydantic import BaseModel


class UserRequest(BaseModel):
    user_id: str
    age: int
```

这里的：

```python
user_id: str
age: int
```

不是在赋具体值，而是在声明字段和类型规则。

真正赋值发生在创建对象时：

```python
user = UserRequest(user_id="u_001", age=20)
```

结论：

```text
class 里声明结构。
创建对象时传入具体数据。
```

---

## 9. 可运行代码的最低标准

下面这段代码不能通过工程标准：

```python
from faseapi import FastAPI,HttpException
```

原因：

- `faseapi` 拼错；
- `HttpException` 大小写错；
- 缺少空格虽然不一定报错，但风格差。

工程标准写法：

```python
from fastapi import FastAPI, HTTPException
```

以后判断代码不能只问“意思是不是对”，要问：

```text
这段代码能不能运行？
导入是否正确？
大小写是否正确？
字段名是否正确？
返回值是否符合 response_model？
```

---

## 10. 本课你必须掌握

学完这一课，你必须能回答：

1. 为什么 Python 创建对象不用 `new`？
2. 为什么 `True` 可以，`true` 不可以？
3. 为什么 `HTTPException` 不能写成 `HttpException`？
4. `class UserRequest(BaseModel)` 是什么意思？
5. `user_id: str` 是赋值吗？
6. `UserRequest(user_id=\"u_001\")` 是定义类还是创建对象？
7. 为什么 import 拼写错误会导致程序不能启动？
8. 为什么代码“看起来懂了”不等于“工程上合格”？

---

## 11. 学完后的动作

学完后只说：

```text
我学习完了
```

然后我会出第 1 课测试题。测试题会严格检查概念、代码阅读、错误定位和小编码能力。
