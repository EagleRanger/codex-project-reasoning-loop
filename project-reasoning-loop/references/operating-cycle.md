# Operating Cycle

Read only the applicable section when planning substantial work, moving from exploration into execution, or finalizing a checkpoint. Light work does not require the full cycle. This file owns operating-cycle rules; linked references supply specialized contracts.

## Select the operating mode

Choose the lightest mode that controls the actual risk.

- **Light**: localized, reversible, well-specified change. Read current state and relevant lessons; execute; verify.
- **Standard**: normal feature, bug, or multi-file iteration. Run the pre-task check, work in checkpoints, then update state and lessons.
- **Full**: architecture change, destructive or external side effect, high uncertainty, milestone review, or work spanning multiple systems. Add explicit assumptions, impact analysis, rollback, decision record, and post-task review.

State the selected mode in one sentence. Do not turn small work into ceremony.

## Separate cognitive phases from governance modes

Treat task phase and risk mode as independent controls. `Explore`, `Crystallize`, `Execute`, and `Reflect` describe what kind of thinking is happening; Light, Standard, and Full describe how much governance the risk requires.

- **Explore** in the project/strategy lane. Preserve the current question, verified facts, user boundaries, and unresolved contradictions. Consult prior models as hypotheses, not default answers; exclude stale conclusions, unrelated Skills, and execution detail that would anchor the search prematurely.
- **Crystallize** in the project/strategy lane. Convert the useful reasoning into a compact contract: objective, evidence, settled decisions, open design space, assumptions to test, protected boundaries, acceptance evidence, and conditions that reopen discussion.
- **Execute** in the execution/run lane. Follow the crystallized contract and active workflow. Do not replay the full exploratory dialogue or reopen a settled decision unless its stated invalidation signal appears.
- **Reflect** in the project/strategy lane. Compare observed effects with the contract, separate event from diagnosis, and admit only decision-relevant lessons or cross-project candidates.

The project lane may contain all three non-execution phases. Create an optional dedicated exploration task only when uninterrupted conceptual development would otherwise pollute project governance; it still shares the same project loop and has no separate authority. Do not create a new `Cognitive Workspace` or duplicate conversation archive by default.

Require a crystallization gate before an exploratory result can authorize real execution. Read [references/reasoning-execution-cycle.md](reasoning-execution-cycle.md) when a task moves from open-ended reasoning into implementation, when long context is over-anchoring later work, or when knowledge type and evidence maturity are being confused.

## Pre-task loop

1. Read applicable `AGENTS.md` instructions first.
2. Complete any referenced-task context ingress described above.
3. Read `PROJECT_LOOP.md` and follow its authority map. For substantial Standard or Full work, establish the project loop first if it is missing.
4. Classify the current task as project/strategy, execution/run, or an unsplit mixed task. Split mixed research and real execution before side effects; load the applicable handoff packet.
5. Read `STATE.md`; read only the decisions and lessons relevant to the current module, tags, failure class, or decision type.
6. Select applicable reviewed global methods, localize them to project facts, and record why a seemingly relevant method does not apply when that decision matters later.
   When the method entrypoint is unknown or a route was corrected, use [method discovery and adoption](continuity-and-learning.md#find-and-adopt-an-applicable-method). Reuse unchanged known entrypoints instead of running discovery on every turn.
7. Separate:
   - objective and acceptance evidence;
   - constraints and non-goals;
   - observed facts;
   - inferences;
   - unverified assumptions.
8. Identify historical guardrails and blocked routes. Do not treat an unresolved observation as a rule or a rejected workflow as an available fallback.
9. For Standard or Full mode, assess affected files/systems, reversibility, user-owned work, validation, rollback, and shared-resource ownership.
10. Ask for direction only when a missing choice materially changes the outcome or when new authority is required.

Output a compact pre-task note: mode, project-loop identity, task lane, objective, handoff identity when applicable, acceptance evidence, relevant lessons, blocked routes, main uncertainty, and next checkpoint.

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
6. Run the record admission test before writing. Record only failures that carry durable diagnostic value; do not log every nonzero exit code.
7. When the user corrects the approach, capture the corrected premise and why the former premise failed.
8. If the project has multiple workflow versions, use its declared active workflow; invoke candidates only in validation mode.
9. For real external side effects or shared applications, establish run ownership and a per-run manifest before acting; serialize access unless the project has proved concurrency safe.
10. Run the project's cheapest decisive local gates before requesting model review. Escalate only the unresolved semantic or risk-bearing delta.

When acceptance relies on classification, a summary or a proxy, first use [acceptance calibration](validation-review-policy.md#calibrate-the-acceptance-basis). Preserve accepted work; recheck only changed objects and affected relationships, widening when a shared source or global invariant changes. Do not interpret a review-round limit as permission to stop unfinished in-scope repair.

Historical design discussion, a prior run authorization, or access to a logged-in session does not authorize a new real side effect. Confirm current authority from the current instruction and project contract.

Do not commit, push, deploy, publish, delete, or alter global rules unless the user requested or approved that action.

## Post-task loop

1. Verify the requested outcome with direct evidence. Tool success alone is not outcome evidence.
2. Finalize any execution manifest and reconcile it with observed external state. In an execution lane, return the compact execution-to-project packet and stop before changing canonical strategy.
3. Apply the record admission test to every proposed durable write.
4. In the project lane, triage returned execution evidence and update `PROJECT_LOOP.md` only when its phase, authority map, task-lane contract, active-workflow pointer, or input/output boundary changed.
5. Update `STATE.md` with what is now true, remaining risks, blockers, and the next checkpoint. Keep it concise.
6. Add or update a `LESSONS.md` entry only when evidence supports a useful event or project lesson.
7. Record a decision when future work needs to know why an alternative was selected or rejected.
8. Consider a cross-project candidate only after abstracting away project technology and implementation names.
9. Run the standard validator when this Skill's default project-loop contract is used:

```powershell
python <skill-dir>/scripts/validate_records.py --root <project-root> --require-project-loop
```

Add `--require-task-lanes` when the project uses separate project/strategy and execution/run tasks.

If the project declares hot and retrieval-only context bundles, also run:

```powershell
python <skill-dir>/scripts/audit_context_lifecycle.py --config <context-projects.json>
```

Treat size and file-count findings as review warnings unless the project explicitly enables strict audit. Never treat audit success as permission to archive or delete native tasks.

If the project already has an equivalent custom contract and its own loop assertion, run the base record validator without `--require-project-loop` plus the project's own assertion. Do not duplicate a second canonical loop file merely to satisfy this validator.

10. Report newly recorded lessons and candidates. Never claim a candidate has become global unless the user approved a specific global change.
