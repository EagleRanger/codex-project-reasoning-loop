# Project-loop contract

Use a project-specific loop to connect the global reasoning method to one project's executable truth. Keep the contract proportional to risk.

## Minimum contract

Define:

1. a stable loop ID and project boundary;
2. native project or folder identity, `【项目】` strategy lanes, `【执行】` run lanes, and the actual project entity they share;
3. objective, non-goals, and acceptance evidence;
4. an authority map with one navigation entry;
5. current phase and smallest falsifiable checkpoint;
6. inbound global methods that were applied, localized, or rejected;
7. validation, recovery, rollback, and shared-resource ownership;
8. local validation gates, quality-review escalation triggers, and review stop conditions;
9. an outbound queue for abstract reasoning candidates;
10. project-to-execution and execution-to-project handoff boundaries, including canonical write ownership;
11. content that must remain project-local.
12. the cognitive phase model and crystallization gate used when open-ended reasoning becomes execution.
13. independent claim dimensions for structural validity, observed effect, and user acceptance when applicable.
14. project-local admission and redaction before any lesson becomes an outbound cross-project candidate.
15. continuation rules for questions, corrections, additions, local pauses, and whole-task replacement.

The project loop performs the actual project iteration and owns project facts. The global loop owns only reusable cross-project reasoning methods. Project feedback moves upward only as abstract candidates. Do not let either layer impersonate the other.

## Global-project improvement cycle

Use this loop:

```text
reviewed global method
-> project localization and bounded execution
-> project-local evidence, diagnosis, decision, and validated lesson
-> redacted cross-project candidate
-> global comparison, review, approval, and versioned method update
```

The downward path carries methods and questions. The upward path carries only admitted reasoning candidates, never raw project state or execution authority.

Native Codex project and task management owns container membership, transcripts, live task state, approvals, and tool activity. Reference those facts instead of copying them into the loop.

The `【项目】` lane owns strategy, isolated validation, root-cause analysis, active-workflow decisions, and canonical project records. The `【执行】` lane owns one bounded run, direct evidence, cleanup, and feedback. A task title alone grants no authority. Both lanes must resolve the same loop ID, and a candidate must cross an explicit handoff before real execution.

Within the project lane, distinguish `Explore`, `Crystallize`, and `Reflect`; reserve `Execute` for the execution lane. Keep those phases separate from Light, Standard, and Full risk modes. The crystallization gate passes only the current problem, verified facts, settled decisions, open design space, falsifiable assumptions, protected boundaries, acceptance evidence, and reopen conditions. The exploratory transcript remains with its native task.

## Scale by risk

### Lean project loop

Use for ordinary multi-session work:

- `PROJECT_LOOP.md` as the navigation and boundary contract;
- `STATE.md`, `DECISIONS.md`, `LESSONS.md`, and `GLOBAL_CANDIDATES.md`;
- direct validation commands and a clear next checkpoint.

### Governed project loop

Add these controls when the project has external side effects, shared applications, expensive recovery, multiple workflow versions, or stale routes that can still execute:

- a machine-readable index that points to the canonical contract;
- a workflow registry with one active verified identity;
- a component registry when independently accepted capabilities are reused across phases;
- frozen module identities, accepted scopes, dependencies, evidence, invalidation signals, and versioned replacement rules;
- statuses that separate production, validation, rejected, and superseded routes;
- negative checks that block stale or rejected entrypoints;
- a per-run execution manifest with owner, target, inputs, active workflow, evidence, rollback, and final status;
- a versioned project-to-execution packet and a compact execution-to-project result for every governed real run;
- pre-mutation admission gates that reject stale identity, authority, evidence, or dependencies before the first durable or external effect;
- serialized ownership for shared external state unless concurrency safety is proved;
- versioned candidate replacement followed by an atomic active-pointer switch;
- production compositions that reject unverified dependencies and fingerprint drift in protected accepted artifacts;
- a local-first review policy with a compact review key or receipt, bounded model-review scope, and an explicit escalation reason.
- a bounded convergence rule that freezes accepted items and limits later passes to the observed failure subset when the work is homogeneous.

Do not impose one high-governance file hierarchy on every project. Require the semantic contract and controls only where their risk is present.

## Validation and review boundary

Local validation and model review are complementary:

- local gates cheaply prove syntax, structure, invariants, known regressions, and repeatable state checks;
- targeted model review examines the remaining semantic delta and decision risk;
- real-world acceptance proves the requested external or user-visible outcome.


Record structural validity, observed effect, and user acceptance as separate conclusions whenever they apply. Do not use a structural validator, tool exit, or completed process to claim a real effect or accepted outcome that it did not observe.
A passing local gate never proves more than its stated coverage. A model review should not re-read passing evidence unless it challenges the conclusion. Deep review is mandatory when the project's escalation triggers fire, even if local checks pass.

Tool termination, cause settlement, external effect, and final acceptance are distinct boundaries. When an external system writes late evidence, use a bounded read-only settlement check before classification. A justified no-action or negative result is acceptable when its scope, decisive gate, non-mutation evidence, and next legal condition are explicit.

Historical discussion establishes intent and design history, not current authorization for a new external side effect. The project contract must define who can authorize a real run, how irreversible actions are contained or compensated, and how an `unknown` run is reconciled before retry.

## Context ingress

When the user references another task or conversation:

1. read the original task turns rather than relying on its title or summary;
2. extract the user's objective, corrections, explicit boundaries, and unresolved questions;
3. read the referenced project's current authority files and evidence;
4. treat conversation content as intent and history, and project artifacts as current executable state;
5. surface conflicts and inaccessible context instead of silently choosing one.

## Authority precedence

Use this default unless the project defines a stricter safe order:

```text
current explicit user instruction
-> explicit project objective or contract
-> current direct evidence
-> declared active project authorities and workflow
-> current state and decisions
-> validated lessons
-> older conversations, logs, comments, and inactive scripts
```

Use the latest applicable correction within the active objective. Older conclusions remain retrievable evidence, but they do not regain authority merely because they are more detailed.

Lower layers may explain or challenge higher layers with evidence, but they do not silently overwrite them.

## Feedback to the global loop

Keep project technology, commands, paths, handles, versions, hashes, and transient failures local. Return only a candidate that:

- has a verified causal explanation;
- changes a future reasoning decision;
- removes project-specific nouns;
- states applicability, counterexample, and invalidation signal;
- remains a proposal until the global maintenance task reviews it.
- has passed project-local record admission and lesson validation before global review;
- carries only the minimum redacted evidence needed to evaluate the reasoning claim.
