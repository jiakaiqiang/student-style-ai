# 学习记忆 / Learning Memory

> 这个文件用于把本项目中的学习上下文保存到仓库中，方便后续换环境后继续学习。
>
> 使用方式：新环境中打开本仓库后，先阅读本文件和 `CLAUDE.md`，再继续作为一对一 Agent 应用开发学习老师跟进。

---

## 1. 学习者背景

- 学习者是一名前端开发者。
- 目标是从前端开发转向 Agent / LLM 应用开发。
- 当前学习路线从 Python 开始，再逐步进入 API、LLM SDK、工具调用、RAG、Agent 工作流与完整项目实践。

---

## 2. 教学方式约定

请按照一对一老师方式推进：

1. 每个阶段先输出学习文档。
2. 学习者学习完成后会说：`我学习完了`。
3. 然后出阶段测试题。
4. 学习者回答后，需要分析：
   - 已掌握知识点；
   - 薄弱点；
   - 常见误区；
   - 是否通过当前阶段；
   - 是否可以进入下一阶段。
5. 如果没有掌握，不要急着进入下一阶段，先给补强讲解和练习。
6. 直到判断阶段能力掌握，再继续推进 Agent 学习路线。

---

## 3. 当前学习路线

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

## 4. 已生成学习文档

当前项目中已有：

- `python-stage-01-basics.md` — 阶段 1：Python 基础入门
- `python-stage-02-scripting.md` — 阶段 2：Python 进阶与脚本能力
- `python-stage-02-assessment.md` — 阶段 2 测试题
- `python-stage-03-oop-async.md` — 阶段 3：Python 面向对象与异步基础
- `python-stage-03-oop-async-advanced.md` — 阶段 3：Python 面向对象与异步编程全面深入版
- `python-stage-03-assessment-advanced.md` — 阶段 3 测试题
- `python-stage-04-api-backend.md` — 阶段 4：API 使用与后端服务基础

---

## 5. 阶段 1：Python 基础

状态：已通过，属于基础通过。

已掌握：

- Python 基础类型：`str`、`int`、`float`、`bool`、`None`。
- Python `True` / `False` / `None` 对应 JS 的 `true` / `false` / `null`。
- Python 变量不使用 `let` / `const` / `var`。
- `list` 类似 JS 数组。
- `dict` 类似 JS 对象 / key-value 数据。
- `def` 用于定义函数。
- `return` 用于返回函数结果。
- `json.dumps()` 将 Python 对象转 JSON 字符串。
- `json.loads()` 将 JSON 字符串转 Python 对象。
- 初步理解 Agent 应用中 JSON 用于结构化用户输入、模型输出、工具参数、API 结果和状态记录。

阶段 1 暴露过的问题：

- 曾把 Python 缩进主要理解为函数代码块，需要持续强化：Python 中 `if` / `for` / `while` / `def` / `class` / `with` / `try` 等代码块都依赖缩进。
- 曾把 list 描述为“链式数据”，需要更准确理解为“有顺序的数据集合”。
- 输出结果的精确性需要加强，例如 `print()` 通常一行输出一次。
- JSON 参数位置曾写错，如把 `ensure_ascii=False`、`indent=2` 放到 `print()` 上。
- 小编码题最初出现过 dict 逗号、字段、布尔值、JSON 解析字段访问等问题，后续已补强。

阶段 1 判断：通过，但后续继续关注缩进和代码精确性。

---

## 6. 阶段 2：Python 进阶与脚本能力

状态：概念通过，条件通过进入阶段 3，但缩进问题仍需持续关注。

已学习内容：

- 文件读写：`open()`、`with`、`r` / `w` / `a` 模式、`encoding="utf-8"`。
- JSON 文件操作：`json.dump()` / `json.load()`。
- JSON 字符串和文件方法区别：
  - `json.dumps()`：Python 对象 -> JSON 字符串
  - `json.loads()`：JSON 字符串 -> Python 对象
  - `json.dump()`：Python 对象 -> JSON 文件
  - `json.load()`：JSON 文件 -> Python 对象
- `pathlib.Path` 路径处理。
- `mkdir(exist_ok=True)` 创建文件夹。
- `data_dir / "file.json"` 拼接路径。
- `try...except` 异常处理。
- `save_record()`、`load_record()`、`main()` 函数模块化。
- `requests.get()` / `requests.post()` HTTP 请求基础。
- `response.status_code`、`response.json()`。
- `json=payload` 表示以 JSON 请求体发送 Python dict。
- `os.getenv()` 读取环境变量。
- API Key 不应写死在代码中，避免泄露并方便部署。

阶段 2 测评表现：

- 文件读写、JSON 四方法、异常处理、HTTP 请求、环境变量等概念回答较好。
- 能从 Agent 工具封装角度理解函数模块化。
- 理解 `requests` 和前端 `fetch()` 的相似点。

阶段 2 暴露过的问题：

- 曾把 `encoding="utf-8"` 写成 `encoding="ftf-8"`。
- 曾说 `Path("data")` 是创建文件夹，更准确说法是：它创建路径对象，真正创建文件夹的是 `mkdir()`。
- POST 请求中曾说“jsons 实例”，应表达为 JSON 请求体 / payload。
- 小编码题第一次没有完全按需求实现：
  - 使用 `current_stage` 而不是 `stage`；
  - 缺少 `target`；
  - 文件路径不是 `data/stage_02_record.json`；
  - 输出没有按要求打印 `stage` 和 `target`。
- 后续修正了字段、路径和输出，但多次出现顶层代码前面多空格的问题。

当前重点提醒：

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

## 7. 阶段 3：Python 面向对象与异步编程（全面深入版）

**状态**：已通过。

已学习文件：

```text
python-stage-03-oop-async-advanced.md
```

阶段 3 学习重点（全面版）：

**面向对象部分：**
- `__init__` vs `__new__`（单例模式）
- `@property`（计算属性、参数校验）
- `@staticmethod`、`@classmethod`（方法类型）
- 继承、`super()`、方法重写
- `@dataclass` 高级特性：`field()`、`__post_init__`、`frozen`、`slots`
- 类型系统：`TypedDict`、`Protocol`、`Literal`、`Union`、`Optional`
- 抽象基类 `ABC`

**异步编程部分：**
- Event Loop 与协程原理
- `coroutine` vs `Task` vs `Future`
- `asyncio.create_task()` vs `asyncio.gather()` vs `asyncio.wait()`
- 超时控制：`asyncio.wait_for()`
- 异步上下文管理器：`async with`
- 异步迭代器：`async for`
- 异步生成器
- 错误处理与异常传播
- 并发控制：`Semaphore`

**Agent 应用实战：**
- Agent 架构设计模式
- 工具系统设计
- 并发调用与性能优化
- 状态管理与会话持久化

测试题文件：

```text
python-stage-03-assessment-advanced.md
```

测试题包含：
- 概念理解题（10 题）
- 代码分析题（5 题）
- 设计题（2 题）
- 综合编码题（1 题）

阶段 3 判断：通过，可以进入阶段 4。

---

## 2026-06-02 update: Python deep reinforcement lesson 1 assessment

User submitted answers for `python-deep-reinforcement-01-assessment.md`.

Assessment result: not passed yet. Broad concepts are mostly understood, but engineering precision is still insufficient.

Observed strengths:
- Understands that Python executes statements from top to bottom.
- Understands that names must exist before they are used.
- Understands `True` vs `true` at a basic level.
- Understands that `user_id: str` is a field/type declaration, not value assignment.
- Understands the difference between defining a class and creating an object.
- Understands that `+` behaves differently for numbers and strings.
- Small coding exercise structure is mostly runnable.

Observed issues:
- Wrote `hTTPException` instead of `HTTPException`; this is still incorrect and would break import/runtime behavior.
- Described `class UserRequest(BaseModel)` imprecisely as using BaseModel "parameters"; should be explained as inheritance from `BaseModel`.
- Wrote `Userrequest` instead of `UserRequest` in explanation; case precision still needs reinforcement.
- In the coding exercise, used title `"learn Python"` instead of required `"learn python"`. Field values must match requirements exactly.
- Needs stricter attention to exact imports, capitalization, required literal values, and API/schema naming.

Next action:
- Do not advance to lesson 2 yet.
- Give a short targeted reinforcement exercise focused on import precision, case sensitivity, exact requirement matching, and BaseModel inheritance.

2026-06-02 follow-up reinforcement result: still not passed.

New observed issues:
- In text, wrote `HTTPExeption` instead of `HTTPException`; the missing `c` shows spelling precision is still unstable.
- Incorrectly said `BaseModel` is provided by FastAPI. Correct source is Pydantic: `from pydantic import BaseModel`.
- Corrected code omitted the required `BaseModel` import.
- Kept class name as `taskrequest`; should use PascalCase `TaskRequest` for a class, and this matters for name consistency.
- Indentation in the class body was not consistently 4 spaces.

Next action:
- Continue lesson 1 reinforcement.
- Drill minimal runnable snippets requiring exact imports, PascalCase class names, Pydantic BaseModel, bool literals vs type declarations, and 4-space indentation.

## 8. 当前阶段：阶段 4 — API 使用与后端服务基础

**状态**：已进入阶段 4，已提供学习文档，等待学习者完成。

当前应学习文件：

```text
python-stage-04-api-backend.md
```

阶段 4 学习重点：

- HTTP 请求与响应模型
- REST API 基础设计
- FastAPI 后端服务入门
- Pydantic 数据校验
- 路由、请求体、查询参数、路径参数
- 状态码与错误处理
- 前后端调用链路
- API Key 与环境变量
- 为后续 LLM SDK、工具调用和 Agent 服务封装打基础

学习者学完后会说：

```text
我学习完了
```

阶段 4 巩固情况：

- 学习者已经能写出 FastAPI 请求/响应模型、POST 路由、请求对象读取和错误返回的大体结构。
- 最新巩固题仍出现精确性问题：
  - `fastapi` 写成 `faseapi`；
  - `HTTPException` 写成 `HttpException`。
- 这说明概念基本理解，但代码精确性仍不足。进入 LLM SDK 前，需要暂停路线，先做更深入、更全面、更实战的 Python 一对一强化。

当前安排：

```text
暂停阶段 5：LLM SDK 使用
先进入 Python 深度强化训练
```

新增训练文档：

- `python-deep-reinforcement-roadmap.md` — Python 深度强化总路线
- `python-deep-reinforcement-01-core-runtime.md` — 第 1 课：Python 运行模型、变量、类型、对象与精确性

强化重点：

- Python import 与模块名精确性；
- 大小写敏感；
- 函数、类、对象、实例化；
- dict、dataclass、BaseModel 的选择；
- 异常处理与错误传播；
- FastAPI 请求/响应模型；
- 代码是否能真实运行，而不是只表达大概意思；
- 从前端迁移到 Python 时必须纠正的习惯。

---

## 9. 教学提醒

后续教学要继续关注：

1. Python 缩进纪律；
2. 是否严格按需求实现字段名、文件名、输出格式；
3. 是否能把前端经验迁移到 Python，例如：
   - `self` 类似 JS `this`；
   - `__init__` 类似 JS `constructor`；
   - Python `async/await` 类似 JS `async/await`；
   - `requests` 类似前端 `fetch`。
4. 逐步把每个 Python 能力映射到 Agent 应用场景。

教学风格更新：

1. 用户要求更严格、更专业、更实战的一对一教学；
2. 不要总是说“好”，不要过度鼓励；
3. 需要主动提出问题让用户回答；
4. 对答案要直接指出错误、风险和工程后果；
5. 不要因为概念大体正确就放过拼写、大小写、导入、字段名、返回格式等基础错误；
6. 进入 LLM SDK 前必须先补足 Python 精确性和实战编码能力。

---

## 10. 文档输出约定（md + html 双份）

从 2026-06-08 起，学习文档和测试题采用 **md + html 双份**：

- 继续维护 `.md`（方便编辑和 diff）；
- 每篇额外导出一份同名 `.html`，风格参考 ChatGPT 页面的**文档阅读风格**：
  - 居中单栏、清爽排版、深色代码块（带语言标签 + 复制按钮）；
  - 语法高亮用 highlight.js CDN，离线自动降级为深色纯文本块；
  - 跟随系统深/浅色（`prefers-color-scheme`）。
- 已生成 HTML：`python-stage-01-basics`、`python-stage-02-scripting`、`python-stage-02-assessment`、`python-stage-03-oop-async`、`python-stage-03-assessment`。
- 用户**不希望仓库里保留转换脚本**：批量转换时用一次性临时方式完成（装到临时目录、跑完即删）。
- 新增文档时，记得同步产出 `.html`。
