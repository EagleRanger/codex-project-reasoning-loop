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
  owns transcripts, live task state, approvals, tools, and schedules
                         |
                         | reference, do not duplicate
                         v
Project-specific loop
  performs actual project iteration and optimization; owns objective,
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
7. **Tool success is not outcome evidence.** External or user-visible acceptance must be verified directly.

## Repository layout

```text
project-reasoning-loop/
  SKILL.md
  agents/openai.yaml
  references/
    artifact-schema.md
    native-codex-coordination.md
    project-loop-contract.md
    promotion-policy.md
    validation-review-policy.md
  scripts/
    init_project.py
    validate_records.py
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
- Cross-project candidates never promote themselves into global rules.
- The full loop is intentionally skipped for trivial one-step tasks.
- A stale or over-detailed project state can create more cost than it saves; keep `STATE.md` compact and retrieve lessons by relevance.

## 中文要点

- 一个真实项目只建立一个项目循环；开发、检查和定时执行只是不同任务通道。
- Codex 原生任务负责对话、实时状态、审批和工具活动；项目循环不重复保存这些内容。
- 总 Loop 只管理跨项目方法，不保存或推进任何具体项目的实际状态。
- 下位项目 Loop 负责实际项目迭代优化、验证、恢复和反馈提炼，并保存长期目标、权威链、当前阶段、活动工作流、禁止路线与验收证据。
- 项目技术经验先留在项目内；只有经过因果验证和独立场景比较的推理方法，才可提交为跨项目候选。
- 先做本地确定性验证，再把实质变化和未解决风险交给模型审查。
- 任何公开发布、删除、部署或真实外部操作仍需当前明确授权。

## License

MIT License. See `LICENSE`.
