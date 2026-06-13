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

## 7. 当前阶段：阶段 3 — Python 面向对象与异步基础

当前应学习文件：

```text
python-stage-03-oop-async.md
```

阶段 3 学习重点：

- `class`
- `__init__`
- `self`
- 属性和方法
- `dict` 和 `class` 的区别
- `@dataclass`
- 类型提示
- `async def`
- `await`
- `asyncio.run()`
- `asyncio.gather()`
- 异步 Agent 的基础结构

学习者学完后会说：

```text
我学习完了
```

之后需要出阶段 3 测试题，并继续分析学习结果。

---

## 8. 教学提醒

后续教学要继续关注：

1. Python 缩进纪律；
2. 是否严格按需求实现字段名、文件名、输出格式；
3. 是否能把前端经验迁移到 Python，例如：
   - `self` 类似 JS `this`；
   - `__init__` 类似 JS `constructor`；
   - Python `async/await` 类似 JS `async/await`；
   - `requests` 类似前端 `fetch`。
4. 逐步把每个 Python 能力映射到 Agent 应用场景。

---

## 9. 文档输出约定（md + html 双份）

从 2026-06-08 起，学习文档和测试题采用 **md + html 双份**：

- 继续维护 `.md`（方便编辑和 diff）；
- 每篇额外导出一份同名 `.html`，风格参考 ChatGPT 页面的**文档阅读风格**：
  - 居中单栏、清爽排版、深色代码块（带语言标签 + 复制按钮）；
  - 语法高亮用 highlight.js CDN，离线自动降级为深色纯文本块；
  - 跟随系统深/浅色（`prefers-color-scheme`）。
- 已生成 HTML：`python-stage-01-basics`、`python-stage-02-scripting`、`python-stage-02-assessment`、`python-stage-03-oop-async`、`python-stage-03-assessment`。
- 用户**不希望仓库里保留转换脚本**：批量转换时用一次性临时方式完成（装到临时目录、跑完即删）。
- 新增文档时，记得同步产出 `.html`。
