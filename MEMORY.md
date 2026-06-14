# 学习记忆汇总 / Learning Memory Consolidated

> 本文件整合了项目学习进度的所有关键记忆，用于跨环境、跨会话继续学习。
>
> **使用方式：** 新环境打开本仓库后，先阅读本文件和 `CLAUDE.md` / `LEARNING_MEMORY.md`，再作为一对一 Agent 应用开发学习老师继续推进。

---

## 学习者背景

- **身份：** 前端开发者
- **目标：** 从前端开发转向 Agent / LLM 应用开发
- **学习路线：** 从 Python 开始，逐步进入 API、LLM SDK、工具调用、RAG、Agent 工作流与完整项目实战

---

## 教学方式约定

按照一对一老师模式推进：

1. 每个阶段先输出学习文档；
2. 学习者学完后会说：`我学习完了`；
3. 出阶段测试题；
4. 学习者回答后，分析：
   - 已掌握知识点
   - 薄弱点
   - 常见误区
   - 是否通过当前阶段
   - 是否可以进入下一阶段
5. 如果没有掌握，先给补强讲解和练习，不要急着进入下一阶段；
6. 直到判断阶段能力掌握，再继续推进 Agent 学习路线。

---

## 学习路线

1. Python 基础
2. Python 进阶与脚本能力
3. Python 面向对象与异步基础
4. API 使用与后端服务基础
5. LLM SDK 使用
6. 工具调用与结构化输出
7. RAG / 数据检索基础
8. Agent 工作流与多步骤任务执行
9. Agent 应用项目实战

---

## 已生成学习文档

| 文档 | 说明 |
|---|---|
| `python-stage-01-basics.md` / `.html` | 阶段 1：Python 基础入门 |
| `python-stage-02-scripting.md` / `.html` | 阶段 2：Python 进阶与脚本能力 |
| `python-stage-02-assessment.md` / `.html` | 阶段 2 测试题 |
| `python-stage-03-oop-async.md` / `.html` | 阶段 3：Python 面向对象与异步基础 |
| `python-stage-03-assessment.md` / `.html` | 阶段 3 测试题 |
| `python-stage-03-practice/` | 阶段 3 动手练习（4 个 .py 文件） |

**文档输出约定（2026-06-08 起）：**
- 每篇学习文档和测试题都产出 **md + html 双份**；
- HTML 采用 ChatGPT 文档阅读风格：居中单栏、清爽排版、深色代码块（语言标签 + 复制按钮）、highlight.js 语法高亮、跟随系统深浅色；
- **不保留转换脚本在仓库中**；批量转换时用临时方式完成。

---

## 阶段 1：Python 基础

**状态：** ✅ 已通过（基础通过，后续继续关注缩进和代码精确性）

**测试日期：** 2026-05-29

### 已掌握

- Python 基础类型：`str`、`int`、`float`、`bool`、`None`
- Python `True` / `False` / `None` 对应 JS 的 `true` / `false` / `null`
- Python 变量不使用 `let` / `const` / `var`，动态类型
- `list` 类似 JS 数组
- `dict` 类似 JS 对象 / key-value 数据
- `def` 定义函数，`return` 返回函数结果
- `json.dumps()` 将 Python 对象转 JSON 字符串
- `json.loads()` 将 JSON 字符串转 Python 对象
- 初步理解 Agent 应用中 JSON 用于结构化用户输入、模型输出、工具参数、API 结果和状态记录

### 暴露过的问题

- 曾把 Python 缩进主要理解为函数代码块，需要持续强化：Python 中 `if` / `for` / `while` / `def` / `class` / `with` / `try` 等代码块都依赖缩进
- 曾把 list 描述为"链式数据"，更准确是"有顺序的数据集合"
- 输出结果精确性需要加强，例如 `print()` 通常一行输出一次
- JSON 参数位置曾写错，如把 `ensure_ascii=False`、`indent=2` 放到 `print()` 上
- 小编码题最初出现过 dict 逗号、字段、布尔值、JSON 解析字段访问等问题，后续已补强
- **顶层代码缩进问题：** 顶层代码被意外缩进，会导致 `IndentationError: unexpected indent`

### 判断

通过，但后续继续关注缩进和代码精确性。

---

## 阶段 2：Python 进阶与脚本能力

**状态：** ✅ 概念通过，条件通过进入阶段 3（缩进问题仍需持续关注）

**测试日期：** 2026-05-29

### 已学习内容

- 文件读写：`open()`、`with`、`r` / `w` / `a` 模式、`encoding="utf-8"`
- JSON 文件操作：`json.dump()` / `json.load()` vs `json.dumps()` / `json.loads()`
  - `json.dumps()`：Python 对象 -> JSON 字符串
  - `json.loads()`：JSON 字符串 -> Python 对象
  - `json.dump()`：Python 对象 -> JSON 文件
  - `json.load()`：JSON 文件 -> Python 对象
- `pathlib.Path` 路径处理
- `mkdir(exist_ok=True)` 创建文件夹
- `data_dir / "file.json"` 拼接路径
- `try...except` 异常处理
- `save_record()`、`load_record()`、`main()` 函数模块化
- `requests.get()` / `requests.post()` HTTP 请求基础
- `response.status_code`、`response.json()`
- `json=payload` 表示以 JSON 请求体发送 Python dict
- `os.getenv()` 读取环境变量
- API Key 不应写死在代码中，避免泄露并方便部署

### 测评表现

- 文件读写、JSON 四方法、异常处理、HTTP 请求、环境变量等概念回答较好
- 能从 Agent 工具封装角度理解函数模块化
- 理解 `requests` 和前端 `fetch()` 的相似点

### 暴露过的问题

- 曾把 `encoding="utf-8"` 写成 `encoding="ftf-8"`
- 曾说 `Path("data")` 是创建文件夹，更准确说法是：它创建路径对象，真正创建文件夹的是 `mkdir()`
- POST 请求中曾说"jsons 实例"，应表达为 JSON 请求体 / payload
- 小编码题第一次没有完全按需求实现：
  - 使用 `current_stage` 而不是 `stage`
  - 缺少 `target`
  - 文件路径不是 `data/stage_02_record.json`
  - 输出没有按要求打印 `stage` 和 `target`
- **后续修正了字段、路径和输出，但多次出现顶层代码前面多空格的问题**

### 重点提醒

```text
顶层代码：0 个空格
函数内部：4 个空格
同一代码块：缩进必须一致
```

顶层代码包括：

```python
import json
from pathlib import Path

def main():
    ...

main()
```

---

## 阶段 3：Python 面向对象与异步基础

**状态：** 🔄 动手练习已完成并 review（2026-06-14），待正式测试

**已学习文件：**
- `python-stage-03-oop-async.md` / `.html`（学习文档）
- `python-stage-03-assessment.md` / `.html`（测试题，共 20 题）
- `python-stage-03-practice/` 四个动手练习

### 阶段 3 学习重点

- `class`、`__init__`、`self`
- 属性和方法
- `dict` 和 `class` 的区别
- `@dataclass`
- 类型提示
- `async def`、`await`
- `asyncio.run()`、`asyncio.gather()`
- 异步 Agent 的基础结构

### 动手练习 review 结果（2026-06-14）

完成了四个练习：

| 练习 | 内容 | 结果 |
|---|---|---|
| `exercise_01_class.py` | class / `__init__` / self / 方法 | ✅ 通过 |
| `exercise_02_dataclass.py` | @dataclass / 类型提示 | ❌ 有 bug |
| `exercise_03_async.py` | async / await / gather / 并发 | ⚠️ 代码能跑，预测错一个 |
| `exercise_04_fix_bug.py` | 调试题 | ✅ 通过 |

#### 练习 1：class — ✅ 通过

输出正确：

```text
工具 file_reader：读取文件内容
file_reader 收到参数：notes.txt
```

`__init__`、`self`、方法都写对了，缩进也对。

#### 练习 2：dataclass — ❌ 有一个真 bug

**实际输出：**

```text
[file_reader] 成功=$True 输出=读取了 3 行
```

**期望输出：**

```text
[file_reader] 成功=True 输出=读取了 3 行
```

**Bug：** 第 29 行 f-string 里用了 `${result.success}`，多了一个 `$`。这是**前端 JS 模板字符串习惯漏过来了**：

- JS：`` `${x}` ``
- Python f-string：`f"{x}"`（不用 `$`）

**另外：** 第 24-26 行 dataclass 字段后面加了分号 `;`（如 `tool_name: str;`），Python 不需要分号，虽然不报错但不是 Python 写法。

#### 练习 3：async — ⚠️ 代码能跑，但预测错了一个

**实际输出：**

```text
['搜索 完成', '读文件 完成', '写报告 完成']
```

**预测 1（总耗时 3 秒）：** ✅ 对。三个任务并发，最慢的是「写报告」3 秒，所以总共约 3 秒，不是 2+1+3=6。

**预测 2（顺序 `读文件 搜索 写报告`）：** ❌ 错。用户按「谁先完成」来排了，但 `asyncio.gather` 返回的列表**永远按传入顺序**排，不按完成快慢排。实际是 `搜索 读文件 写报告`（传入顺序）。

**记住这个区分：** **谁先跑完**和**结果顺序**是两回事。gather 会等所有任务都完成，再按传入顺序把结果摆好。

**其他问题：**
1. 第 31 行变量名用了 `list`，这会盖掉 Python 内置的 `list`。换个名字，比如 `results`。
2. 第 28-29 行 `call_tool` 函数体缩进了 **8 个空格**，应该是 **4 个**。

第 32 行注释问得很好——`asyncio.gather(...)` 返回的确实是一个可等待对象，要 `await` 才能拿到结果列表，理解对了。

#### 练习 4：调试题 — ✅ 修对了

预测的两个 bug 都对：
- bug 1：`self.name = name` 漏了 `self`（原坏代码里是 `name = name`）
- bug 2：`run` 里少了 `await`（原坏代码 `result = self.call_model(...)` 没 await，结果是协程对象不是字符串）

修成 `reply = await self.call_model(user_input)` 后，输出正确：

```text
学习助手 -> 模型回复：已处理 学习 async
```

注释里问「这里为啥要 await」——因为 `call_model` 是 `async def`，直接调用只会得到一个**协程对象**，加 `await` 才会真正执行它并拿到 return 的字符串。理解对了。

### 暴露的主要问题

#### 1. 前端习惯误用

- **练习 2：f-string 里用了 `${x}`（JS 模板字符串语法），应该是 `{x}`**
- **dataclass 字段后面加了分号 `;`（Python 不需要）**

#### 2. `asyncio.gather` 结果顺序误解

- 练习 3 预测结果会按「完成快慢」排序
- 实际 `gather` 返回的列表**永远按传入顺序**，不是完成顺序

#### 3. 缩进问题持续出现

- 练习 3 函数体缩进了 8 个空格，应该是 4 个
- 这是从阶段 1、阶段 2 一直跟踪的纪律问题

#### 4. 变量名覆盖内置名

- 练习 3 用了 `list` 作为变量名，覆盖了 Python 内置的 `list`

### 掌握情况（很好）

- `self`、`await`、协程对象、并发耗时计算等核心概念理解正确
- 能预测和修复异步代码的 bug（练习 4 全对）
- 注释显示对「为什么要 await」有清晰认知

### 下一步

用户被建议修正练习 2、3 的问题后，进入正式的阶段 3 测试题 `python-stage-03-assessment.md`（20 道题，包含概念题、拔高题、调试题、编码题）。

---

## 持续关注的重点模式

### 1. 缩进纪律（从阶段 1 至今）

```text
顶层代码：0 个空格
函数/类/方法体：4 个空格
同一代码块：缩进必须一致
```

**历史问题：**
- 阶段 1：顶层代码被意外缩进
- 阶段 2：顶层 import、def、main() 前多空格
- 阶段 3：函数体缩进 8 个空格

### 2. 前端习惯迁移到 Python

**已发现的迁移问题：**
- `self` 类似 JS `this` ✅（这个映射是对的）
- `__init__` 类似 JS `constructor` ✅（这个映射是对的）
- Python `async/await` 类似 JS `async/await` ✅（这个映射是对的）
- `requests` 类似前端 `fetch` ✅（这个映射是对的）
- ❌ f-string 里用 `${x}`（应该是 `{x}`，不用 `$`）
- ❌ 语句/字段后面加分号 `;`（Python 不需要）

### 3. 严格按需求实现

**历史问题：**
- 阶段 2：字段名、文件名、输出格式未按要求实现

**教学提醒：** 逐步把每个 Python 能力映射到 Agent 应用场景。

---

## Git 提交记录

- `fe01d40` — Add agent learning materials and memory
- `22e5c03` — chore(learning): add python practice files
- `bb54ba6` — chore(learning): add stage 3 practice, html docs and rag mcp demo
- `1face6f` — docs(learning): add stage 3 practice review to memory

---

**最后更新：** 2026-06-14
