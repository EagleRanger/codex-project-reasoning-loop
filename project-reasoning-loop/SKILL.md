---
name: project-reasoning-loop
description: Establish and run durable global-to-project reasoning loops for long-running or multi-session work without duplicating native Codex project, chat, task-status, or approval state. Use when Codex needs to create or resume one named loop per actual project entity, coordinate several task chats that share a project, read referenced task context, protect a verified workflow from stale routes, use local evidence before token-expensive quality review, preserve recoverable run state, prevent recurrence of validated mistakes, or return evidence-backed reasoning candidates for cross-project review. Do not use the full loop for trivial one-step requests.
---

# Project Reasoning Loop

Build continuity from reviewable project artifacts while reusing native Codex project and task state. Keep the global Loop limited to cross-project methods. Let one named project-specific Loop per actual project entity perform the real iteration, optimization, validation, recovery, and feedback extraction. Keep project facts local, link to native task evidence instead of copying it, and return only evidence-backed reasoning candidates for global review.

## Select the operating mode

Choose the lightest mode that controls the actual risk.

- **Light**: localized, reversible, well-specified change. Read current state and relevant lessons; execute; verify.
- **Standard**: normal feature, bug, or multi-file iteration. Run the pre-task check, work in checkpoints, then update state and lessons.
- **Full**: architecture change, destructive or external side effect, high uncertainty, milestone review, or work spanning multiple systems. Add explicit assumptions, impact analysis, rollback, decision record, and post-task review.

State the selected mode in one sentence. Do not turn small work into ceremony.

## Use a two-level loop architecture

- **Global loop (`project-reasoning-loop`)**: owns only reusable cross-project methods for framing, evidence, validation, recovery, workflow replacement, and experience review. Never store or advance a concrete project's actual state here.
- **Project-specific loop**: performs the actual project iteration and optimization; owns that project's objective, authority chain, current phase, active workflow, rejected routes, run state, decisions, lessons, evidence, and candidate feedback extraction.

Use the direction of flow explicitly: global methods are localized by a project Loop; project evidence is abstracted into candidates and returned for global review. Do not let the global Loop execute or maintain the project on behalf of its project-specific Loop.

For substantial Standard or Full work, identify or establish a stable named project-specific loop before implementation. A project loop is a local governance contract, not necessarily another installed Skill. Never create a project-local copy of this global Skill.

Skip a dedicated project loop for one-step, low-risk work with no meaningful resume or recovery need.

## Coordinate with native Codex project and task management

Map the native structure before creating project-loop artifacts:

- A **Codex project** organizes shared folders, instructions, sources, and related task chats.
- A **task/chat** owns one distinct outcome, its transcript, current turn state, tool activity, and user interaction.
- A **project-specific loop** spans the actual project entity across related task chats and stores only durable project semantics that native task history does not reliably expose as current executable truth.

Do not create a new loop merely because the sidebar contains another task. Reuse one loop when several tasks share the same project root, objective, authorities, and production workflow. Treat scheduled or recurring execution tasks as run lanes of the owning project, not independent project loops.

Native Codex state is authoritative for task transcript, live status, current approvals, tool results, and task identity. The project loop is authoritative for project objective, authority map, phase, active workflow, blocked routes, acceptance evidence, recovery state, durable decisions, validated lessons, and global candidates. Link native task IDs or evidence locations; do not paste full transcripts, commentary streams, or duplicate progress logs into project records.

Read [references/native-codex-coordination.md](references/native-codex-coordination.md) before reorganizing several Codex tasks, creating loops for an existing project collection, or tuning Auto-review volume.

## Initialize project artifacts

Use `.project-reasoning/` as the default project-local source of truth. If it does not exist and the task is long-running, run:

```powershell
python <skill-dir>/scripts/init_project.py --root <project-root> --loop-id <stable-project-loop-id>
```

The initializer creates only missing files. Never overwrite existing project records.

Use these artifacts:

- `PROJECT_LOOP.md`: project-loop identity, scope, authority map, global input boundary, execution/recovery contract, and global feedback boundary.
- `STATE.md`: recoverable project truth and next checkpoint; never a duplicate of native task status or transcript.
- `DECISIONS.md`: durable decisions, alternatives, and reversal conditions.
- `LESSONS.md`: concrete events and validated project lessons.
- `GLOBAL_CANDIDATES.md`: proposals for transferable reasoning methods; never an automatic global memory.

Read [references/project-loop-contract.md](references/project-loop-contract.md) before establishing or substantially changing a project loop. Read [references/validation-review-policy.md](references/validation-review-policy.md) when a project uses automated model review, has costly validation, or needs a review-budget policy. Read [references/artifact-schema.md](references/artifact-schema.md) before creating or substantially editing records. Read [references/promotion-policy.md](references/promotion-policy.md) before proposing or promoting a cross-project lesson.

## Ingest referenced tasks and conversations first

When the user points to another Codex task, project, or conversation as the source of intent:

1. Locate and read that task's original turns from the start of the referenced topic through its latest correction or decision. Paginate when needed, but do not load unrelated task history merely because it exists.
2. Read the associated project's current authority files and relevant state, decisions, lessons, and change artifacts.
3. Treat the conversation as evidence of user intent, corrections, and historical reasoning; treat current project artifacts and direct observations as evidence of present state.
4. Resolve conflict by current user instruction, explicit project objective or contract, current direct evidence, active project authorities, then older chat or logs.
5. State what could not be accessed instead of silently reconstructing missing context.

## Pre-task loop

1. Read applicable `AGENTS.md` instructions first.
2. Complete any referenced-task context ingress described above.
3. Read `PROJECT_LOOP.md` and follow its authority map. For substantial Standard or Full work, establish the project loop first if it is missing.
4. Read `STATE.md`; read only the decisions and lessons relevant to the current module, tags, failure class, or decision type.
5. Select applicable reviewed global methods, localize them to project facts, and record why a seemingly relevant method does not apply when that decision matters later.
6. Separate:
   - objective and acceptance evidence;
   - constraints and non-goals;
   - observed facts;
   - inferences;
   - unverified assumptions.
7. Identify historical guardrails and blocked routes. Do not treat an unresolved observation as a rule or a rejected workflow as an available fallback.
8. For Standard or Full mode, assess affected files/systems, reversibility, user-owned work, validation, rollback, and shared-resource ownership.
9. Ask for direction only when a missing choice materially changes the outcome or when new authority is required.

Output a compact pre-task note: mode, project-loop identity, objective, acceptance evidence, relevant lessons, blocked routes, main uncertainty, and next checkpoint.

## During-task loop

1. Work in the smallest checkpoint that can disprove the current approach.
2. Validate the highest-risk assumption before scaling or performing broad mechanical work.
3. Preserve user changes and inspect current state before editing.
4. After each meaningful checkpoint, compare observed results with the acceptance evidence.
5. Classify failures before recording them:
   - expected negative test or search miss;
   - environment, permission, or transient failure;
   - execution mistake;
   - design or reasoning mistake.
6. Record only failures that carry durable diagnostic value. Do not log every nonzero exit code.
7. When the user corrects the approach, capture the corrected premise and why the former premise failed.
8. If the project has multiple workflow versions, use its declared active workflow; invoke candidates only in validation mode.
9. For real external side effects or shared applications, establish run ownership and a per-run manifest before acting; serialize access unless the project has proved concurrency safe.
10. Run the project's cheapest decisive local gates before requesting model review. Escalate only the unresolved semantic or risk-bearing delta.

Historical design discussion, a prior run authorization, or access to a logged-in session does not authorize a new real side effect. Confirm current authority from the current instruction and project contract.

Do not commit, push, deploy, publish, delete, or alter global rules unless the user requested or approved that action.

## Govern workflow replacement and real runs

Use these controls only where a project has persistent executable workflows, external side effects, or expensive recovery:

- Keep one declared active production workflow and explicit statuses such as `verified`, `validation_only`, `rejected`, and `superseded`.
- Make blocked or rejected routes unenforceable through the normal entrypoint; documentation alone is not a sufficient guard when stale code can still run.
- Give a replacement a new identity. Validate it independently, then switch the active identity atomically after complete acceptance evidence; do not overwrite the verified baseline in place.
- Freeze a verified baseline while a candidate is under test unless direct counterevidence requires a repair.
- Create a non-reusable execution manifest for each real run when run identity matters. Record objective, authority, inputs, target, owner, active workflow, acceptance evidence, rollback, and final status.
- Finalize manifests as succeeded, failed, interrupted, or unknown. A crash, timeout, missing callback, or process exit must never remain recorded as success.
- Reconcile an `unknown` run against external state before another real run can reuse the same target. For an irreversible action, require explicit current authorization plus a pre-check and an acceptable containment or compensation plan; otherwise block the action.
- Treat static checks and unit tests as gate evidence, not as proof that the real user-visible or external-state outcome occurred.
- After an active-workflow switch, assert that the registry, normal entrypoint, and runtime resolution all identify the same version before declaring the switch complete.

## Use a local-first quality-review ladder

The purpose of quality review is risk reduction, not repeated narration of unchanged context. This ladder is separate from Codex Auto-review at the sandbox boundary.

1. **Local gate**: run deterministic, offline, or machine-checkable validations over the changed scope first. Examples include schema checks, invariant assertions, blocked-route scans, targeted tests, diff checks, and artifact consistency checks.
2. **Targeted model review**: review only the material delta, affected contract, failed or uncertain local evidence, and relevant guardrails.
3. **Deep model review**: use for architecture or contract changes, security or privacy impact, destructive or external side effects, replacement of an active verified workflow, unresolved contradictions, milestone acceptance, or an explicit user request.

Do not trigger another quality-model review when the material change set, acceptance contract, validator versions, unresolved findings, and review-policy version are unchanged. Record a compact review receipt or equivalent state so a quality reviewer can skip an identical review key. Store reviewer, model, and prompt-policy identity in the receipt; let the project policy state which identity changes invalidate prior acceptance instead of forcing every tool update to re-review unchanged work.

Each governed project must declare:

- local validation gates and which risks each gate can and cannot prove;
- model-review escalation triggers and maximum review scope;
- a quantified soft review budget expressed as automatic rounds per checkpoint and maximum delta scope when exact token accounting is unavailable;
- stop conditions, unresolved-finding ownership, and when a new evidence delta permits another round.

If the same review failure recurs without new evidence, diagnose the validation or design loop instead of resubmitting the same context. Never weaken safety-critical review solely to save tokens.

Codex Auto-review is not this quality-review ladder. It reviews eligible requests to cross the sandbox boundary. Do not cache, bypass, or replace native approval decisions with project receipts. Reduce unnecessary Auto-review traffic by keeping safe work inside the declared project roots and, only with explicit user authorization, proposing narrowly scoped writable roots or command-prefix rules. Never broaden permissions merely to reduce review volume.

## Post-task loop

1. Verify the requested outcome with direct evidence. Tool success alone is not outcome evidence.
2. Finalize any execution manifest and reconcile it with observed external state.
3. Update `PROJECT_LOOP.md` only when its phase, authority map, active-workflow pointer, or input/output boundary changed.
4. Update `STATE.md` with what is now true, remaining risks, blockers, and the next checkpoint. Keep it concise.
5. Add or update a `LESSONS.md` entry only when evidence supports a useful event or project lesson.
6. Record a decision when future work needs to know why an alternative was selected or rejected.
7. Consider a cross-project candidate only after abstracting away project technology and implementation names.
8. Run the standard validator when this Skill's default project-loop contract is used:

```powershell
python <skill-dir>/scripts/validate_records.py --root <project-root> --require-project-loop
```

If the project already has an equivalent custom contract and its own loop assertion, run the base record validator without `--require-project-loop` plus the project's own assertion. Do not duplicate a second canonical loop file merely to satisfy this validator.

9. Report newly recorded lessons and candidates. Never claim a candidate has become global unless the user approved a specific global change.

## Distinguish lesson scopes

- **Event**: what happened in one task, with evidence and current diagnosis.
- **Project lesson**: a validated technical or workflow constraint for this project.
- **Cross-project candidate**: a conditional reasoning method about framing, assumptions, evidence, decomposition, risk, validation, or recovery.

Convert specifics into reasoning structure before proposing transfer:

```text
specific failure -> verified project lesson -> abstract reasoning error
-> compare independent contexts -> define boundary and counterexample
-> user-reviewed cross-project rule
```

Never promote package-manager choices, paths, APIs, framework conventions, or version-specific fixes into global reasoning rules.

## Global promotion guardrail

Global promotion is a proposal-and-review operation, not an automatic threshold action.

- Require a verified causal explanation, not mere recurrence.
- Require evidence from at least two meaningfully different tasks; normally require two different projects.
- State applicability, counterexample, and invalidation signal.
- Prefer a conditional question or procedure over an absolute prohibition.
- Show the exact proposed rule and destination to the user before writing outside the project.
- Keep rejected and superseded candidates reviewable.

An explicit user instruction may set a global operating policy without pretending that the policy is an empirically proven cross-project lesson. Record its source, scope, boundary, and reversal condition as a decision. Continue to label the supporting project candidate by its actual evidence stage.

## Keep the system lean

- Do not read all historical records on every task; retrieve by tags and relevance.
- Do not send unchanged history, passing local evidence, or resolved findings back through model review. Prefer a compact delta packet and review receipt.
- Treat Markdown artifacts as the source of truth. Any index or database must be rebuildable from them.
- Do not duplicate the same rule across multiple files.
- Do not preserve screenshots, logs, or secrets longer than necessary; retain minimal redacted evidence.
- Do not modify this Skill from its own observations. Propose Skill changes separately and validate them before adoption.

## Keep execution and maintenance separate

- Treat projects that consume this Skill as read-only clients of the installed Skill.
- A project task may apply the workflow, update its own `.project-reasoning/` records, and propose a Skill improvement, but it must not edit, reinstall, or repair the global Skill.
- Route proposed Skill changes to the designated maintenance task. Apply them there only after reviewing project evidence and validating the revised Skill.
- If the Skill is absent from an already-open task's available list, follow the project's durable `AGENTS.md` fallback for that task and report the availability issue to the maintenance task; do not silently create a project-local fork.
