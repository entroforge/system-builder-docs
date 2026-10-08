---
pageClass: document-map-page
---

# `control/`：工作按什么边界推进

`docs/control/` 定义阶段怎样变化、哪些操作受到保护。日常看当前位置与缺项，核对精确规则时查下面的文件。

| 文件 | 各自负责什么 |
| --- | --- |
| `agent-protocol.md` | S0～S11 的阶段协议：每一步要求的输入、产物、检查与返回路径 |
| `loop-definition.json` | 工作状态与合法迁移的机器定义 |
| `hook-policy.json` | 工具操作触发的保护策略与执行边界 |
| `protected-commands.json` | 受保护的命令类别，例如发布相关的 Git 操作 |

这里保存**推进规则**，`docs/` 外的 `.claude/loop-state.json` 保存**当前进度与事实**。

`.claude/bin/loop-harness` 执行校验与登记，Hook 在工具操作前后触发检查并反馈。AI 按技能和角色方法工作，程序按这里的定义核对推进条件。

实际交接过程见[谁推动阶段](../mechanism/progression)。各类工作的工程约束在 [`rules/`](./rules)，操作说明在 [`guides/`](./guides)。
