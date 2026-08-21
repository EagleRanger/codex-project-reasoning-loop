# Codex Project Reasoning Loop

A public Codex Skill for durable, evidence-driven iteration across long-running projects and multiple task chats.

这是一个面向 Codex 长周期项目的公开 Skill。它把“跨项目通用推理方法”和“单个项目的可执行事实”分成两层，同时复用 Codex 原生项目、任务、审批和自动化状态，避免建立第二套重复任务系统。

## Why this exists

Long-running agent projects usually fail in predictable ways:

- a new task chat cannot tell which workflow is currently authoritative;
- historical discussion is mistaken for current executable truth;
- rejected approaches silently return after context loss;
- one project's technical workaround is promoted into a global rule;
- the same unchanged context is repeatedly sent through expensive model review;
- task transcripts, project state, and approval state are duplicated across files.

This Skill addresses those failures with a two-level reasoning architecture and an explicit boundary with native Codex state.

Its defining separation is: **the global Loop manages only cross-project methods; each project-specific Loop performs the actual project iteration and extracts feedback candidates; native Codex manages live task state.**

## Architecture

```text
Native Codex project and task layer
  owns transcripts, live task state, approvals, tools, and schedules;
  uses 【项目】 strategy tasks and 【执行】 run tasks as separate work surfaces
                         |
                         | reference, do not duplicate
                         v
Project-specific loop
  coordinates the task lanes and performs project iteration; owns objective,
  authority map, phase, active workflow, blocked routes, recovery state,
  acceptance evidence, decisions, and validated lessons
                         |
                         | submit evidence-backed candidates
                         v
Global project-reasoning-loop Skill
  owns only reusable cross-project methods for framing, evidence,
  validation, recovery, review budgeting, and experience promotion;
  never owns or updates a concrete project's actual state
```

The central rule is **one fact, one owner**. Native Codex remains the source of truth for live task execution. The project loop stores only durable project semantics that must survive across task chats.

## Core ideas

1. **One actual project, one project loop.** Development, review, investigation, and scheduled runs reuse the same loop when they share an objective, authority chain, production workflow, and recovery state.
2. **Global methods, project execution.** The global Loop manages only cross-project methods. Each project-specific Loop applies those methods to actual iteration, validation, recovery, and project-level feedback extraction.
3. **Read referenced context before reconstructing it.** When a user points to another task or conversation, read the original relevant turns and then the project's current authority files.
4. **Use the lightest safe governance mode.** Light, Standard, and Full modes prevent both under-governance and unnecessary ceremony.
5. **Validate locally before spending model attention.** Deterministic gates run first; model review receives only material deltas and unresolved risks.
6. **Promotion requires evidence and review.** A repeated observation is not a global rule. Require verified causality, independent contexts, applicability, a counterexample, an invalidation signal, and explicit approval.
7. **Records must earn persistence.** Keep cheaply derivable facts with their authoritative source; persist only durable decisions, caveats, recovery truth, validated lessons, and evidence-backed candidates.
8. **Tool success is not outcome evidence.** External or user-visible acceptance must be verified directly.
9. **Separate strategy from operation.** `【项目】` researches, validates, diagnoses, and maintains canonical strategy; `【执行】` runs one approved workflow and returns evidence. Both use the same project loop.
10. **Bound multi-agent work.** Parallelize only independent or disjoint work, keep one canonical writer, serialize shared resources, and use compact handoff packets.
11. **Freeze accepted capabilities and compose them.** When a capability is independently accepted, give it a stable component ID, protected fingerprint, dependencies, evidence, reuse scope, and invalidation rule. Improve it through a new candidate ID and atomic recipe switch instead of silently editing it or rebuilding a parallel route.
12. **Crystallize reasoning before execution.** Explore freely in the project lane, then pass only verified facts, settled decisions, open design space, assumptions, boundaries, acceptance evidence, and reopen conditions to the execution lane.
13. **Gate before mutation and accept evidence-backed no-action.** Reject stale authority or evidence before the first durable effect; a bounded no-op or negative result is valid when scope and non-mutation are proved.
14. **Converge with a baseline pass and an exception pass.** Freeze items that pass, repair only the observed failure subset once, and reopen the baseline only when failures are systemic.
15. **Keep context hot, warm, and cold.** Resume from a minimal current-truth bundle, retrieve decisions and evidence by relevance, and preserve raw history for audit without loading it by default.
16. **Prove recovery before archive or deletion.** Compact recall-first and precision-second, preserve the prior state and hash, then pass an eight-question hot-only recovery gate. Structural success is not semantic recovery.

## Repository layout

```text
project-reasoning-loop/
  SKILL.md
  agents/openai.yaml
  references/
    artifact-schema.md
    native-codex-coordination.md
    project-loop-contract.md
    reasoning-execution-cycle.md
    component-registry.md
    context-lifecycle.md
    promotion-policy.md
    task-lane-handoff.md
    validation-review-policy.md
  scripts/
    init_project.py
    validate_records.py
    validate_component_registry.py
    test_validate_component_registry.py
    audit_context_lifecycle.py
```

## Installation

Clone this repository and copy the inner `project-reasoning-loop` folder into your Codex skills directory.

Windows PowerShell:

```powershell
git clone https://github.com/EagleRanger/codex-project-reasoning-loop.git
Copy-Item -Recurse -Force `
  .\codex-project-reasoning-loop\project-reasoning-loop `
  "$env:USERPROFILE\.codex\skills\project-reasoning-loop"
```

macOS or Linux:

```bash
git clone https://github.com/EagleRanger/codex-project-reasoning-loop.git
cp -R ./codex-project-reasoning-loop/project-reasoning-loop \
  ~/.codex/skills/project-reasoning-loop
```

Start a new Codex task after installation so the Skill list is refreshed.

## Quick start

Ask Codex to use the Skill:

```text
Use $project-reasoning-loop to establish a durable loop for this project.
Keep native Codex task state authoritative and use Standard mode unless risk requires otherwise.
```

Or initialize the default project records directly:

```powershell
python project-reasoning-loop/scripts/init_project.py `
  --root <project-root> `
  --loop-id <stable-project-loop-id>
```

This creates missing files only:

- `.project-reasoning/PROJECT_LOOP.md`
- `.project-reasoning/STATE.md`
- `.project-reasoning/DECISIONS.md`
- `.project-reasoning/LESSONS.md`
- `.project-reasoning/GLOBAL_CANDIDATES.md`

Validate the records with:

```powershell
python project-reasoning-loop/scripts/validate_records.py `
  --root <project-root> `
  --require-project-loop
```

Projects that reuse independently accepted capabilities may also keep `.project-reasoning/COMPONENTS.json` and validate it before development or execution:

```powershell
python project-reasoning-loop/scripts/validate_component_registry.py `
  --root <project-root>
```

Only `verified + frozen` components may enter a verified production recipe. A fingerprint mismatch, unavailable dependency, or validation-only component in a verified recipe blocks reuse.

Long-running projects may also declare hot and retrieval-only context bundles and run a read-only audit:

```powershell
python project-reasoning-loop/scripts/audit_context_lifecycle.py `
  --config <context-projects.json>
```

The audit checks structure, declared files, size triggers, and accidental raw-transcript material. It does not prove semantic recovery or authorize compaction, archive, or deletion. See `references/context-lifecycle.md` for the two-pass compaction receipt and eight-question recovery gate.

## Example project boundary

```markdown
# Project Loop Contract

**Loop ID:** example-product-project-loop
**Status:** active
**Global loop:** project-reasoning-loop
**Updated:** 2026-08-09

## Identity and scope

- Objective: deliver the named product milestone.
- Acceptance evidence: direct tests and user-visible verification.
- Related task lanes: development, review, and scheduled execution.

## Authority map

- Current user instruction.
- Active project contract and workflow pointer.
- Current evidence, decisions, lessons, and recovery state.
```

See `references/artifact-schema.md` for complete schemas.

## Governance modes

- **Light:** localized, reversible, well-specified work.
- **Standard:** normal feature, bug, or multi-file iteration.
- **Full:** architecture change, high uncertainty, destructive or external effects, workflow replacement, or milestone acceptance.

Use the lightest mode that controls the real risk.

## Review and token discipline

This Skill separates two different mechanisms:

- **Project quality review:** local deterministic gates, targeted model review, and deep model review.
- **Codex Auto-review:** native sandbox-boundary approval. Project review receipts must never bypass it.

An unchanged review key with no open finding should not trigger another quality-model review. However, lower token use alone is not success; compare escaped defects and unresolved risk as well.

## Risk boundaries

- The Skill does not grant permissions or authorize external side effects.
- Historical approval does not authorize a new real-world run.
- Local checks do not prove an external or user-visible result unless their coverage actually observes it.
- Project records must not copy secrets, full transcripts, personal data, or unnecessary raw logs.
- Repository scanning or the absence of recent failures cannot by itself create a validated lesson.
- Cross-project candidates never promote themselves into global rules.
- The full loop is intentionally skipped for trivial one-step tasks.
- A stale or over-detailed project state can create more cost than it saves; keep `STATE.md` compact and retrieve lessons by relevance.

## 中文要点

- 一个真实项目只建立一个项目循环；开发、检查和定时执行只是不同任务通道。
- `【项目】`负责研究、策略、隔离测试、根因分析和项目权威更新；`【执行】`负责按已批准版本完成具体运行、留证、清理和问题反馈。
- 两个标签是任务职责而不是新项目；它们必须共享同一个下位 Loop，并通过精简交接包传递目标和证据。
- Codex 原生任务负责对话、实时状态、审批和工具活动；项目循环不重复保存这些内容。
- 总 Loop 只管理跨项目方法，不保存或推进任何具体项目的实际状态。
- 下位项目 Loop 负责实际项目迭代优化、验证、恢复和反馈提炼，并保存长期目标、权威链、当前阶段、活动工作流、禁止路线与验收证据。
- 已独立验收的能力应登记为稳定组件并冻结，通过配方组合复用；改变行为时建立新ID/版本并独立验收，禁止静默改写旧组件或为同一能力另造平行入口。
- 开放式探索先在项目通道形成认知，再经过结晶门转成精简执行契约；执行端不重放整段历史，也不把旧答案当默认结论。
- 拒绝性门禁必须位于第一笔持久写入或真实副作用之前；有证据的无动作与零变更负结果也是正式终态。
- 同类大范围任务优先首轮统一基线、冻结通过项，次轮只修失败子集；局部缺陷不得自动触发全量重做。
- 长期项目把上下文分为热、温、冷三层：热层只保留恢复真值，温层按目标和证据指针补读，冷层保全原始对话、日志和旧状态但默认不加载。
- 上下文压缩先召回后精炼，保存旧状态和哈希，并通过只给热层的八问恢复测试；文件存在和脚本通过不能代替语义恢复。
- 归档与物理删除是不同动作。删除必须核对准确任务身份、入向依赖、冷备份和恢复演练，并取得针对准确对象的新授权。
- 项目技术经验先留在项目内；只有经过因果验证和独立场景比较的推理方法，才可提交为跨项目候选。
- 先做本地确定性验证，再把实质变化和未解决风险交给模型审查。
- 任何公开发布、删除、部署或真实外部操作仍需当前明确授权。

## Contributors and attribution

- **Project direction, acceptance decisions, and release ownership:** EagleRanger
- **AI collaboration:** OpenAI Codex — architecture synthesis, Skill drafting, implementation assistance, validation design, and documentation organization

The repository remains reviewable human-owned work: Codex assistance does not replace the project owner's decisions, authorization, or responsibility for public release.

## License

MIT License. See `LICENSE`.
