# Production Lifecycle

Read only the relevant section for production handoff, governed mutation, workflow replacement, accepted component reuse, batch convergence, or costly quality review. Ordinary local edits do not activate every production control.

## Separate project and execution task lanes

Use task lanes as role boundaries inside one actual project's loop, not as new projects or new sources of truth. A title label is a routing hint; current user intent, the project contract, and direct evidence remain authoritative.

For long-running or very large projects, use this as the default internal management split. The project lane keeps strategy and durable truth; the execution lane consumes a compact handoff for one approved run. Keep their default context bundles separate so execution detail does not flood project strategy and stale strategy history does not anchor routine runs.

- **Project/strategy lane (`【项目】`)**: research project-wide rules, test ideas in isolated `validation_only` mode, diagnose execution feedback, choose strategy, approve workflow replacement, and maintain canonical project state, decisions, lessons, and candidate feedback.
- **Execution/run lane (`【执行】`)**: perform a bounded scheduled or concrete production run against one active approved workflow, preserve current authority and stop conditions, collect direct evidence, contain failure, finalize the run result, and return structured feedback.

Both lanes must resolve to the same project-loop ID. Do not create a second loop, copy canonical state into the execution task, or let the execution lane silently change strategy, risk limits, active workflow identity, blocked routes, or global rules. An execution agent may perform bounded diagnosis needed to classify and contain the current failure; any change to production logic returns to the project lane for decision and validation.

Keep tests and real execution separate. The project lane may explore candidates only against isolated inputs or explicit validation targets. Moving a candidate into a real run requires an explicit project-to-execution packet containing the loop ID, active workflow identity, objective, current authority, inputs and target, permitted actions, acceptance evidence, stop conditions, rollback or containment, report destination, and invalidation condition.

The execution lane returns an execution-to-project packet containing the run ID, workflow identity, observed facts, evidence pointers, terminal status, deviations, containment or cleanup, unresolved questions, and any proposed follow-up. It must distinguish observation from diagnosis and must not present a strategy recommendation as an approved rule.

The project lane is the single writer for canonical governance records. The execution lane owns only its native live task state and, where recovery value justifies it, a per-run record. The project lane admits, merges, or rejects returned information using the record admission test.

Read [references/task-lane-handoff.md](task-lane-handoff.md) before splitting an existing task, configuring a scheduled execution lane, or coordinating multiple agents around one project.

## Put decision gates before mutation

- Order the path as `candidate -> current admission -> action object -> durable or external effect`. A rejection gate after an order, file mutation, message, or external action was already created is cleanup evidence, not proof that no side effect occurred.
- Resolve identity, authority, freshness, scope, dependency, and risk gates before the first governed mutation. Keep reduction or containment actions separately authorized where requiring a new increase-risk gate would be unsafe.
- Treat a bounded `no_action`, `blocked_before_mutation`, or zero-candidate result as a valid terminal outcome when the evaluated scope, decisive gate, non-mutation evidence, and next legal condition are recorded. Never force work merely to prove that a workflow can act.
- Do not equate the first terminal signal with settled evidence. When a tool, log, UI, or external system writes cause or effect asynchronously, perform one bounded, read-only settlement check before classification. The settlement check must not repeat the action or consume another attempt.

## Govern workflow replacement and real runs

Use these controls only where a project has persistent executable workflows, external side effects, or expensive recovery:

- Keep one declared active production workflow and explicit statuses such as `verified`, `validation_only`, `rejected`, and `superseded`.
- Make blocked or rejected routes unenforceable through the normal entrypoint; documentation alone is not a sufficient guard when stale code can still run.
- Give a replacement a new identity. Validate it independently, then switch the active identity atomically after complete acceptance evidence; do not overwrite the verified baseline in place.
- Freeze a verified baseline while a candidate is under test unless direct counterevidence requires a repair.
- Create a non-reusable execution manifest for each real run when run identity matters. Record objective, authority, inputs, target, owner, active workflow, acceptance evidence, rollback, and final status.
- Require the execution lane to resolve the manifest's loop and workflow identities before acting. A missing, stale, or mismatched handoff blocks the real run and returns to the project lane.
- Finalize manifests as succeeded, failed, interrupted, or unknown. A crash, timeout, missing callback, or process exit must never remain recorded as success.
- Reconcile an `unknown` run against external state before another real run can reuse the same target. For an irreversible action, require explicit current authorization plus a pre-check and an acceptable containment or compensation plan; otherwise block the action.
- Treat static checks and unit tests as gate evidence, not as proof that the real user-visible or external-state outcome occurred.
- After an active-workflow switch, assert that the registry, normal entrypoint, and runtime resolution all identify the same version before declaring the switch complete.

## Converge verified capability modules

When a long project repeatedly reuses independently accepted capabilities, represent those capabilities as project-local modules instead of rebuilding them inside every new phase.

- Give each accepted capability one stable module ID, one authoritative entry, an explicit accepted scope, dependencies, evidence, invalidation signals, and a reuse rule.
- Mark a module `verified` and freeze its accepted implementation or contract only after direct acceptance evidence. A later phase composes it; it does not silently edit it.
- Build a changed candidate under a new ID or version, keep the verified module available as rollback, validate the candidate independently, then switch the active composition only after the normal promotion gate.
- Let production recipes compose only independently accepted modules and verified acceptance policies. A verified module must not secretly depend on a rejected, planned, or validation-only component.
- Keep policies, executable modules, run state, and explanatory documents as different types. Documentation may explain the registry but must not become a second manually maintained status source.
- Before starting a new implementation, resolve the requested capability against the registry. Reuse or extend an accepted module when its scope applies; record why it does not apply before creating a parallel route.
- Protect accepted artifacts with a deterministic fingerprint when practical. A fingerprint mismatch invalidates reuse until the change is explained and revalidated; it is never silently refreshed.

Read [references/component-registry.md](component-registry.md) before modularizing an existing project, freezing accepted components, or composing several project capabilities. Use `scripts/validate_component_registry.py` when the project adopts the default registry schema.

## Converge broad work without reopening accepted scope

For a broad set of sufficiently similar items, use a bounded two-pass convergence pattern when the project can define a stable baseline and item-level acceptance:

1. Inventory the current scope dynamically and apply the verified baseline, template, or recipe once.
2. Freeze items that pass their acceptance checks.
3. Rework only the observed failure subset once, then re-check both that subset and the global invariants.
4. Route any remaining failures to review instead of automatically starting a third pass or regenerating the full set.

Do not use this pattern when items require materially different strategies, when the first-pass failures reveal a systemic defect in the baseline, or when a safety-critical acceptance policy requires more rounds. In those cases invalidate the baseline, create a new versioned candidate, and repeat from an explicitly new identity. A local defect must not silently reopen already accepted items.

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
