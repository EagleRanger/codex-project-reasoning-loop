---
name: project-reasoning-loop
description: Maintain recoverable project continuity across tasks, corrections and long runs. Use for project recovery, bounded handoffs, workflow replacement, context compaction and evidence-based learning; skip full governance for one-step work.
---

# Project Reasoning Loop

Build continuity from reviewable project artifacts while reusing native Codex project and task state. Keep the global Loop limited to cross-project methods. Let one named project-specific Loop per actual project entity perform the real iteration, optimization, validation, recovery, and feedback extraction. Keep project facts local, link to native task evidence instead of copying it, and return only evidence-backed reasoning candidates for global review.

## Select the operating mode

Choose Light for localized reversible work, Standard for normal iteration, Full for architecture, high uncertainty or consequential effects. Scale governance to risk, not task length. Read [mode and operating cycle](references/operating-cycle.md#select-the-operating-mode) for the applicable mode; do not load every phase for a small change.

## Start from the main contradiction

For complex work, identify the relationship that most strongly decides whether the desired new possibility can survive. Do not reduce this to a fixed checklist.

1. Name the desired new possibility or capability.
2. Identify the people, rules, interfaces, resources, habits, or stale assumptions that enable or suppress it.
3. Find the smallest relationship whose change would materially alter the outcome.
4. Preserve the parts already producing value; rewrite only the blocking mechanism first.
5. Test the direct effect and use both positive and negative feedback to revise the explanation.

A useful summary states the main contradiction, the effective adjustment, the direct observed effect, and the unresolved uncertainty. It does not claim a universal law from one successful case.

Use an experience cycle through the project's existing authorities: **explore -> test -> admit -> retrieve -> reuse -> revise**. Retrieve prior successes, counterexamples, and failed routes by the current goal and failure class. Keep them as evidence pointers with scope and invalidation conditions, not as a second memory database. Read [references/continuity-and-learning.md](references/continuity-and-learning.md) when continuity, corrections, or local experience are central to the task.

## Use a two-level loop architecture

- **Global loop (`project-reasoning-loop`)**: owns only reusable cross-project methods for framing, evidence, validation, recovery, workflow replacement, and experience review. Never store or advance a concrete project's actual state here.
- **Project-specific loop**: performs the actual project iteration and optimization; owns that project's objective, authority chain, current phase, active workflow, rejected routes, run state, decisions, lessons, evidence, and candidate feedback extraction.

Use the direction of flow explicitly: global methods are localized by a project Loop; project evidence is abstracted into candidates and returned for global review. Do not let the global Loop execute or maintain the project on behalf of its project-specific Loop.

For substantial Standard or Full work, identify or establish a stable named project-specific loop before implementation. A project loop is a local governance contract, not necessarily another installed Skill. Never create a project-local copy of this global Skill.

Skip a dedicated project loop for one-step, low-risk work with no meaningful resume or recovery need.

## Run the bidirectional improvement cycle

Use the two levels as a controlled improvement loop, not a one-way template hierarchy:

1. The global Loop supplies reviewed cross-project methods and admission questions.
2. A project-specific Loop localizes only the methods that fit its objective, risks, authorities, and evidence.
3. The project runs, validates, recovers, and records project-local decisions and lessons without changing the global Skill.
4. A validated project lesson may be abstracted into a redacted cross-project candidate.
5. The global maintenance task compares independent contexts, reviews boundaries and counterexamples, obtains any required approval, and only then updates the global method.

The global Loop never pulls raw project state upward, and an execution task never promotes its own finding directly. Every upward change passes project-local admission first, then global review.

## Coordinate with native Codex project and task management

Map the native structure before creating project-loop artifacts:

- A **Codex project** organizes shared folders, instructions, sources, and related task chats.
- A **task/chat** owns one distinct outcome, its transcript, current turn state, tool activity, and user interaction.
- A **project-specific loop** spans the actual project entity across related task chats and stores only durable project semantics that native task history does not reliably expose as current executable truth.

Do not create a new loop merely because the sidebar contains another task. Reuse one loop when several tasks share the same project root, objective, authorities, and production workflow. Treat scheduled or recurring execution tasks as run lanes of the owning project, not independent project loops.

Native Codex state is authoritative for task transcript, live status, current approvals, tool results, and task identity. The project loop is authoritative for project objective, authority map, phase, active workflow, blocked routes, acceptance evidence, recovery state, durable decisions, validated lessons, and global candidates. Link native task IDs or evidence locations; do not paste full transcripts, commentary streams, or duplicate progress logs into project records.

Treat a new message as steering, not automatic cancellation. A question may be answered and the active outcome then resumed; a correction replaces only the affected assumption or step; a local pause stops only its named branch. Drop the prior objective only when the user cancels it, replaces it with an incompatible objective, pauses the whole task, or a real authority/choice/dependency boundary requires return to the user. A tool result, partial deliverable, status report, or finished phase is not task completion while authorized work and a safe next step remain.

Read [references/native-codex-coordination.md](references/native-codex-coordination.md) before reorganizing several Codex tasks, creating loops for an existing project collection, or tuning Auto-review volume.

## Separate project and execution task lanes

Project and run lanes share one loop and its authority. A task title does not grant strategy or production permission. Before splitting lanes, scheduling a run or issuing a production handoff, read [lane ownership and handoffs](references/production-lifecycle.md#separate-project-and-execution-task-lanes).

## Separate cognitive phases from governance modes

Explore/Crystallize/Execute/Reflect describe thinking; Light/Standard/Full describe risk. Before exploration becomes real execution, settle its bounded contract using [phase rules](references/operating-cycle.md#separate-cognitive-phases-from-governance-modes). Exploration alone does not authorize production.

## Bound multi-agent work

Treat native tasks and sub-agents as isolated work surfaces, not additional authorities.

- Delegate only independent, well-defined work with a concrete output, evidence requirement, write scope, and stop condition.
- Parallelize read-only investigation, disjoint implementation slices, or independent verification only when this materially reduces elapsed time or catches a named risk.
- Serialize shared desktop applications, external accounts, production entrypoints, and overlapping file writes unless the project has proved concurrency safe.
- Keep the project/strategy lane or current parent as the synthesizer. Pass compact evidence packets instead of replaying every worker trace into every agent.
- Do not assume peer agents share a reliable message bus or current state. Use parent-mediated handoff or project-owned append-only run artifacts with explicit ownership.
- Set a concurrency and review budget. Prefer one local batch operation over many agents when it is cheaper and equally decisive; stop fan-out when results repeat, conflict without new evidence, or no longer change the decision.
- Never use multi-agent fan-out merely because the capability exists. Respect the host's current delegation policy and the user's authority.
- Model or agent selection never changes permissions, evidence standards, or completion criteria. Follow the host project's current routing policy, give workers compact evidence-bearing packets, reuse the original worker for bounded repair when context continuity matters, and add independent review only for a named risk.

## Initialize project artifacts

Reuse the existing project loop. Before creating or substantially changing its artifacts, read [initialization](references/record-lifecycle.md#initialize-project-artifacts); never overwrite existing records. One native task does not imply one new project loop.

## Govern context lifecycle and compaction

Treat context selection as a recovery problem, not a race to create the shortest summary.

- **Hot context** contains only the current instruction, applicable project rules, project contract, compact current truth, active workflow or recipe, accepted baseline, blocked routes, authority boundary, unresolved risks, and next checkpoint.
- **Warm context** contains decisions, lessons, component records, handoffs, receipts, and validation evidence retrieved only by current objective, object, version, failure class, tag, or evidence pointer.
- **Cold context** preserves native transcripts, raw logs, old state, screenshots, and historical artifacts for audit and correction without loading them by default.

Compact in two passes: recall-first extraction of current truth and user corrections, then precision-first removal of duplication and cheaply regenerable narration. Preserve the old hot state and its hash before rewriting it. A structural check is not recovery proof: test the new hot bundle without replaying full history and require correct answers for objective, authorities, active workflow, accepted baseline, blocked routes, mutable and frozen scope, permissions and risks, and the next pass/fail checkpoint.

Archive only after a replacement recovery path passes. Physical deletion is a separate, explicitly authorized action that requires exact semantic identity, dependency checks, a verified cold copy, and a restore drill. Size, token count, age, or process memory may trigger review but never authorize compaction, archive, or deletion by themselves.

Read [references/context-lifecycle.md](references/context-lifecycle.md) before materially compacting project state, splitting a long-running task, archiving a source task, or proposing deletion. If a project declares a context-bundle config, use `scripts/audit_context_lifecycle.py` for a read-only structural audit; its pass result does not replace the semantic recovery test.

Invalidate a prior compaction or recovery receipt when the objective, authority chain, active workflow, permissions, accepted baseline, or acceptance semantics materially change. Apply the single [receipt invalidation and retest rule](references/context-lifecycle.md#invalidate-stale-recovery-receipts); do not infer a lighter gate merely because a changed authority or workflow is described briefly.

## Run the record admission test

Before durable writes, check owner, derivability, future decision value, evidence maturity, duplication and minimum evidence using [record admission](references/record-lifecycle.md#run-the-record-admission-test). Prefer an authoritative pointer or updating an existing record to another log.

## Separate conclusion dimensions

Do not collapse different kinds of evidence into one overall `PASS`.

- **Structural validity**: files, schemas, identities, links, and declared relationships are internally consistent.
- **Observed effect**: the requested behavior or external state change was directly observed.
- **User acceptance**: the user reviewed and accepted the relevant outcome when acceptance is part of the contract.

Report each applicable dimension independently. A structural pass does not imply real effect, and an observed effect does not imply user acceptance.

## Resolve mutable authority at validation time

Resolve current authority, workflow, target, and dependency pointers from their authoritative owner when the check runs. Do not hard-code a value that is expected to change.
Use a historical identifier only as an explicitly frozen fixture with a stated purpose. A current-pointer test and a frozen-fixture test are different claims and must not impersonate each other.

## Ingest referenced tasks and conversations first

When the user points to another Codex task, project, or conversation as the source of intent:

1. Locate and read that task's original turns from the start of the referenced topic through its latest correction or decision. Paginate when needed, but do not load unrelated task history merely because it exists.
2. Read the associated project's current authority files and relevant state, decisions, lessons, and change artifacts.
3. Treat the conversation as evidence of user intent, corrections, and historical reasoning; treat current project artifacts and direct observations as evidence of present state.
4. Resolve conflict by current user instruction, explicit project objective or contract, current direct evidence, active project authorities, then older chat or logs.
5. State what could not be accessed instead of silently reconstructing missing context.

Default to the latest applicable correction and current authority. Load older error paths only when they explain a present contradiction, constrain a safe action, or provide a needed counterexample. A handoff that may change execution should point to the relevant original span and require the receiver to verify through the latest correction instead of trusting a title or compressed preview.

## Pre-task loop

Recover the current objective and latest correction, authority map, active workflow, accepted baseline, blocked routes, mutable/frozen scope, risks and next checkpoint. Read only relevant state and experience; follow [pre-task checks](references/operating-cycle.md#pre-task-loop) for substantial work. Referenced user intent must be read through its latest applicable correction.

Before choosing a route, match the actual object and operation to the project's current accepted method. A task title, working directory, generic error word, or search miss does not establish method ownership or permission. Follow [method discovery and adoption](references/continuity-and-learning.md#find-and-adopt-an-applicable-method) when the entrypoint is unknown or a previous route failed.

## During-task loop

Work through falsifiable checkpoints; preserve accepted work, classify failures, and continue authorized work until the outcome is verified or a real boundary blocks it. Apply the [during-task rules](references/operating-cycle.md#during-task-loop) to the affected scope; a partial result is not completion.

## Put decision gates before mutation

Resolve target identity, authority, freshness and scope before a governed effect; safe no-action is valid. Apply [mutation and asynchronous settlement gates](references/production-lifecycle.md#put-decision-gates-before-mutation) before acting; never repeat an action just to obtain evidence.

## Govern workflow replacement and real runs

Use one current accepted production identity; candidates and superseded routes cannot silently run. Before replacement or a real run read [production lifecycle](references/production-lifecycle.md#govern-workflow-replacement-and-real-runs). Reconcile unknown prior effects before reusing a target.

## Converge verified capability modules

Reuse accepted components within their verified scope. Before modularization, composition or a change to a frozen component, read [component lifecycle](references/production-lifecycle.md#converge-verified-capability-modules); stale or rejected dependencies invalidate reuse.

## Converge broad work without reopening accepted scope

Freeze accepted items and repair only failures and affected invariants. For sufficiently similar batches read [two-pass conditions and exceptions](references/production-lifecycle.md#converge-broad-work-without-reopening-accepted-scope); systemic defects require reassessing the baseline.

## Use a local-first quality-review ladder

Run decisive local checks first, then review only unresolved semantic or risk-bearing changes. Before costly/model review read [review triggers and unchanged-evidence skips](references/production-lifecycle.md#use-a-local-first-quality-review-ladder). Quality receipts never replace native approval; do not weaken required acceptance to save tokens.

When a conclusion depends on classification, summarization or a proxy metric, calibrate the acceptance basis against original evidence and a discriminating counterexample before trusting the tests. Read [acceptance calibration](references/validation-review-policy.md#calibrate-the-acceptance-basis) for that risk; simple directly observable edits need no extra review ceremony.

## Post-task loop

Verify the user-visible outcome, settle any run, and preserve the next recoverable state. Use [closure and validators](references/operating-cycle.md#post-task-loop) when closing a governed checkpoint. Record only information that passes admission; structural success is not production acceptance.

## Distinguish lesson scopes

Keep observed events, validated project lessons and cross-project candidates distinct. Read [lesson scopes](references/record-lifecycle.md#distinguish-lesson-scopes) when classifying or abstracting experience; one incident is not a global rule.

## Global promotion guardrail

Projects return redacted candidates, not raw state or automatic policy changes. Before promotion read [evidence and approval requirements](references/record-lifecycle.md#global-promotion-guardrail). Explicit user policy remains distinct from an empirically validated lesson.

## Keep the system lean

- Do not read all historical records on every task; retrieve by tags and relevance.
- Do not persist facts that remain cheaply derivable from their authoritative source; store a pointer and only the non-obvious decision or caveat.
- Do not send unchanged history, passing local evidence, or resolved findings back through model review. Prefer a compact delta packet and review receipt.
- Treat Markdown artifacts as the source of truth. Any index or database must be rebuildable from them.
- Do not duplicate the same rule across multiple files.
- Do not preserve screenshots, logs, or secrets longer than necessary; retain minimal redacted evidence.
- Do not modify this Skill from its own observations. Propose Skill changes separately and validate them before adoption.

Compare optimizations at the same acceptance level using elapsed time, waiting, rework and quality; fewer calls or tokens alone do not prove improvement. Keep source size, actual model input and natural-task effect as separate observations. See [cost and delivery metrics](references/validation-review-policy.md#cost-metrics).

## Keep execution and maintenance separate

- Treat projects that consume this Skill as read-only clients of the installed Skill.
- A project task may apply the workflow, update its own `.project-reasoning/` records, and propose a Skill improvement, but it must not edit, reinstall, or repair the global Skill.
- Route proposed Skill changes to the designated maintenance task. Apply them there only after reviewing project evidence and validating the revised Skill.
- If the Skill is absent from an already-open task's available list, follow the project's durable `AGENTS.md` fallback for that task and report the availability issue to the maintenance task; do not silently create a project-local fork.
