---
pageClass: document-map-page
---

# `rules/`：反复适用的工程约束

`docs/rules/` 保存跨阶段反复使用的规则。`control/` 定义工作状态和操作边界；这里说明遇到某类工作时，文档、代码和协作要遵守什么条件。入口 `README.md` 区分始终适用与按情境启用的规则。

## 常用的共同约束

| 文件 | 管什么 |
| --- | --- |
| `communication.md` | 协作、证据、升级问题时怎样沟通 |
| `naming.md` | 需求、合同、任务、分支等怎样命名 |
| `change-control.md` | 已确认的需求或设计需要改变时怎样留下决定 |
| `git-branch-release.md` | 分支、worktree、合并与发布边界 |
| `security.md` | 代码、配置、数据与权限的安全要求 |

## 按工作内容查的规则

| 文件 | 遇到什么时查 |
| --- | --- |
| `api-design.md`、`shared-model-contracts.md` | 接口、共享数据形状和各部分的消费关系 |
| `state-machine.md`、`error-handling.md` | 状态转换、错误与恢复行为 |
| `scenario-model.md`、`ui-prototype.md` | 模块场景、原型、故事、动线的覆盖 |
| `design-foundation.md` | 产品整体视觉语言与体验设计的形成和沿用 |
| `dispatch-plan.md` | 多项任务的依赖和整体派发计划 |
| `bugfix-review.md`、`capture-provenance.md` | 缺陷修复、观察材料的来源与可信度 |
| `release-architecture-audit.md` | 发布前的系统级风险检查 |

遇到具体工作，按上表查相应规则。规则怎样体现在产物中，可回看 [`design/`](./design)、[`dev/`](./dev) 或 [`reports/`](./reports)。
