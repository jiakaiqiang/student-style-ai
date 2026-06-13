# 参考答案说明

这个文件包含所有练习题的参考答案。

**重要提醒**：先自己独立完成练习，卡住了再看答案！

---

## 题 1：变量与 f-string

```python
name = "张三"
age = 25
print(f"我叫 {name}，今年 {age} 岁")
```

**关键点**：
- f-string 格式：`f"文本 {变量}"`
- 注意 `f` 前缀不能省

---

## 题 2：列表基本操作

```python
fruits = ["apple", "banana", "cherry"]

# 1. 在末尾加一个 "orange"
fruits.append("orange")

# 2. 打印列表的长度
print(len(fruits))

# 3. 用 for 循环逐行打印每个水果
for fruit in fruits:
    print(fruit)
```

**关键点**：
- `append()` 在末尾添加元素
- `len()` 获取长度
- `for` 循环语法：`for 变量 in 列表:` 注意冒号
- 循环体缩进 4 个空格

---

## 题 3：字典 + 循环

```python
ages = {"小明": 18, "小红": 22, "小刚": 30}

# 1. 打印小红的年龄
print(ages["小红"])

# 2. 用 for 循环，按 名字: 年龄 的格式逐行打印所有人
for name, age in ages.items():
    print(f"{name}: {age}")

# 3. 把小明的年龄改成 19，再打印小明的年龄
ages["小明"] = 19
print(ages["小明"])
```

**关键点**：
- 字典访问：`dict[key]`
- 遍历字典：`for key, value in dict.items()`
- 修改值：直接赋值 `dict[key] = 新值`

---

## 题 4：函数 def

```python
def add(a, b=10):
    return a + b

# 调用测试
print(add(3, 5))   # 输出 8
print(add(3))      # 输出 13（使用默认值 b=10）
```

**关键点**：
- 函数定义：`def 函数名(参数):` 注意冒号
- 函数体缩进 4 个空格
- 默认参数写法：`参数名=默认值`
- 有默认值的参数必须放在没有默认值的参数后面

---

## 题 5：列表推导式

```python
nums = [1, 2, 3, 4, 5, 6]

# 1. 得到每个数的平方
squares = [x * x for x in nums]
print(squares)  # [1, 4, 9, 16, 25, 36]

# 2. 只保留偶数
evens = [x for x in nums if x % 2 == 0]
print(evens)  # [2, 4, 6]
```

**关键点**：
- 基本语法：`[表达式 for 变量 in 列表]`
- 带过滤：`[表达式 for 变量 in 列表 if 条件]`
- `%` 是取余运算符，`x % 2 == 0` 判断偶数
- 这就是 JS 里的 `nums.map(x => x * x)` 和 `nums.filter(x => x % 2 === 0)` 的 Python 写法

---

## 常见错误示例

### ❌ 错误 1：忘记冒号

```python
# 错误
def add(a, b)
    return a + b

# 正确
def add(a, b):
    return a + b
```

### ❌ 错误 2：缩进不一致

```python
# 错误
def add(a, b):
  return a + b  # 2 个空格

for i in range(5):
    print(i)  # 4 个空格
```

**正确做法**：统一用 4 个空格缩进。

### ❌ 错误 3：用 JS 语法

```python
# 错误
if x === 5 && y > 10:
    print("ok")

# 正确
if x == 5 and y > 10:
    print("ok")
```

Python 用 `==`、`and`、`or`、`not`，不是 `===`、`&&`、`||`、`!`。

---

## 进阶任务参考答案

### 进阶 1：统计字母出现次数

```python
def count_letters(text):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts

# 测试
result = count_letters("hello")
print(result)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

更简洁的写法（用 `get` 方法）：

```python
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts
```

### 进阶 2：奇数的平方

```python
def odd_squares(nums):
    return [x * x for x in nums if x % 2 == 1]

# 测试
print(odd_squares([1, 2, 3, 4, 5, 6]))  # [1, 9, 25]
```

### 进阶 3：年龄最大的人

```python
def oldest_person(people):
    oldest = people[0]
    for person in people:
        if person["age"] > oldest["age"]:
            oldest = person
    return oldest["name"]

# 测试
people = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 22}
]
print(oldest_person(people))  # Bob
```

更简洁的写法（用 `max` 函数）：

```python
def oldest_person(people):
    return max(people, key=lambda p: p["age"])["name"]
```
