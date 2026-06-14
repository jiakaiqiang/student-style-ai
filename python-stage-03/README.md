# Python 阶段 3：面向对象与异步基础

## 文件结构

```text
python-stage-03/
├── README.md                          # 本文件：阶段 3 总览
├── learning-doc.md                    # 学习文档
├── assessment.py                      # 正式测试题（20 题，可执行）
├── assessment-answer.py               # 测试题参考答案
├── practice/                          # 动手练习
│   ├── README.md                      # 练习说明
│   ├── exercise_01_class.py           # 练习 1：class / __init__ / self
│   ├── exercise_02_dataclass.py       # 练习 2：@dataclass
│   ├── exercise_03_async.py           # 练习 3：async / await / gather
│   └── exercise_04_fix_bug.py         # 练习 4：调试题
├── retest.py                          # 复测题（可执行）
└── retest-answer.py                   # 复测题参考答案
```

## 学习流程

1. **学习文档**：阅读 `learning-doc.md`
2. **动手练习**：完成 `practice/` 下的 4 个练习
3. **正式测试**：完成 `assessment.py` 中的 20 题
4. **复测**（如果需要）：完成 `retest.py`

## 缩进规则（重要）

```text
顶层代码：0 个空格
函数/类/方法体：4 个空格
同一代码块：缩进必须一致
```

## 学习目标

- class / __init__ / self
- 属性和方法
- dict vs class
- @dataclass
- 类型提示
- async def / await
- asyncio.run() / asyncio.gather()
- 异步 Agent 基础结构
