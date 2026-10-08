---
pageClass: mechanism-map-page
outline: false
---

# 一项 REQ 的阶段地图

[文档地图](/document-map/)说明材料放在哪里；这里按产生和使用它们的阶段查阅。每一步先列输入、输出，再说明安排原因与偏差处理。

图中的橙色支路表示：验证发现问题后，先调查、修复，再开启新一轮完整验证。

<picture class="stage-map-picture">
  <source media="(max-width: 1399px)" srcset="/images/req-stage-map-mobile.svg">
  <img src="/images/req-stage-map.svg" alt="一项 REQ 的阶段地图：虚线分出 S0 至 S5 的谋划阶段，以及 S6 至 S9 的实施与验证阶段。S5 向上审查 S3 契约与 S4 任务，并追溯需求和设计。S7 验证通过后进入 S10 验收与 S11 人的决定；发现问题时进入 S8 调查、S9 修复，再返回新一轮 S7。">
</picture>

外层虚线把 **S0～S5 的谋划**与 **S6～S9 的实施、验证和修复**分开；S10～S11 是交付核对与人的决定。S5 指向 S3、S4 的底色框，表示先核对契约和任务，同时沿它们追溯需求与设计。

## 按阶段查找

- [S0～S2：确定承诺与设计](/mechanism/intent)——需求、绑定关系、架构与场景。
- [S3～S5：安排工作](/mechanism/plan)——契约、任务与计划审查。
- [S6～S7：完成并检查](/mechanism/build-and-check)——共同版本与完整验证。
- [S8～S9：调查与修复](/mechanism/investigate-and-repair)——根因、修复与重新验证。
- [S10～S11：验收与决定](/mechanism/release)——验收、审计与人的发布决定。

需求、设计、契约和报告通常在项目的 `docs/` 下；当前绑定、阶段和证据引用在 `.claude/loop-state.json` 中。可按阶段进入上面的文章。

阶段怎样真正向前推进，见[谁推动阶段，凭什么继续](./progression)。工作途中暂停、改变承诺，或准备开始下一项 REQ，见[暂停、修订与下一项需求](./lifecycle)。

## 发现偏差，从哪里查起

先确定**哪里不符合预期**，再查相关产物及其上游输入。输入正确而产物有误，从产生该产物的环节处理；输入已经有误，则继续向上查。

例如，取消订单后页面仍显示“处理中”：S7 记录实际结果，S8 调查是代码没执行约定、约定写错了，还是最初的需求有误。实现缺陷走 S9，规格问题走设计与契约返工，需求问题由人确认修订。团队按正式路径处理，运行机制登记阶段变化。

<details class="stage-map-index">
<summary>查看文字版阶段与产物索引</summary>

| 阶段 | 这一步留下的主要事实 | 想查什么，从哪里开始 |
| --- | --- | --- |
| [S0 需求](/mechanism/intent#s0) | 人确认并锁定的 `docs/requirements/REQ-{id}.md` | 本次究竟答应改变什么、怎样算成功 |
| [S1 绑定](/mechanism/intent#s1) | `.claude/loop-state.json` 中的唯一 REQ 绑定、基线指纹、开发分支与发布上游 | 这轮实际获准处理哪份 REQ |
| [S2 设计](/mechanism/intent#s2) | `docs/architecture/ARCHITECTURE-*.md`；必要时更新模块场景与故事 | 谁负责什么，正常与拒绝情形如何设计 |
| [S3 契约](/mechanism/plan#s3) | `docs/dev/contracts/CONTRACTS-*.md` 与 FE、BE、SYNC 契约 | 各部分对同一行为是否有一致约定 |
| [S4 任务](/mechanism/plan#s4) | `docs/dev/tasks/TASK-*.md` 与当前 REQ 的整体派发计划 | 谁做哪项工作，依赖谁，凭什么算完成 |
| [S5 计划审查](/mechanism/plan#s5) | 独立审查结论与锁定的执行批次 | 规格链和任务计划是否已经被另一方检查 |
| [S6 构建](/mechanism/build-and-check#s6) | 已提交、已集成的代码和测试，以及任务交付记录 | 某项工作只是报告完成，还是已进入共同版本 |
| [S7 完整验证](/mechanism/build-and-check#s7) | 本轮验证计划、逐项结果；通过时形成完整验证通过记录，发现阻断问题时形成发现批次 | 哪些承诺已有当前版本的证据，哪些问题尚未解决 |
| [S8 调查](/mechanism/investigate-and-repair#s8) | 调查案例、因果解释与获准执行的修复约定 | 问题因何产生，影响多大，应该在哪一层修 |
| [S9 修复](/mechanism/investigate-and-repair#s9) | 修复结果、影响清单、定向复验和返回完整验证的交接 | 原问题是否已修，哪些旧证据需要重新取得 |
| [S10 验收与审计](/mechanism/release#s10) | `docs/reports/acceptance/ACC-*.md`、发布审计、剩余风险与发布就绪材料 | 需求是否兑现，系统整体是否仍可安全交付 |
| [S11 人的决定](/mechanism/release#s11) | 明确的人类决定及其固定去向 | 是批准、搁置、驳回哪一类问题，还是中止 |

</details>

关于需求、进度和模块设计这三类记录的区别，另见[《一项工作，为什么有三份记录》](/mechanism/req-identity)。
