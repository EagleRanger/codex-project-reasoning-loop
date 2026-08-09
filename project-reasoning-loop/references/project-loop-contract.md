# Project-loop contract

Use a project-specific loop to connect the global reasoning method to one project's executable truth. Keep the contract proportional to risk.

## Minimum contract

Define:

1. a stable loop ID and project boundary;
2. native project or folder identity, related task lanes, and the actual project entity they share;
3. objective, non-goals, and acceptance evidence;
4. an authority map with one navigation entry;
5. current phase and smallest falsifiable checkpoint;
6. inbound global methods that were applied, localized, or rejected;
7. validation, recovery, rollback, and shared-resource ownership;
8. local validation gates, quality-review escalation triggers, and review stop conditions;
9. an outbound queue for abstract reasoning candidates;
10. content that must remain project-local.

The project loop performs the actual project iteration and owns project facts. The global loop owns only reusable cross-project reasoning methods. Project feedback moves upward only as abstract candidates. Do not let either layer impersonate the other.

Native Codex project and task management owns container membership, transcripts, live task state, approvals, and tool activity. Reference those facts instead of copying them into the loop.

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
- statuses that separate production, validation, rejected, and superseded routes;
- negative checks that block stale or rejected entrypoints;
- a per-run execution manifest with owner, target, inputs, active workflow, evidence, rollback, and final status;
- serialized ownership for shared external state unless concurrency safety is proved;
- versioned candidate replacement followed by an atomic active-pointer switch;
- a local-first review policy with a compact review key or receipt, bounded model-review scope, and an explicit escalation reason.

Do not impose one high-governance file hierarchy on every project. Require the semantic contract and controls only where their risk is present.

## Validation and review boundary

Local validation and model review are complementary:

- local gates cheaply prove syntax, structure, invariants, known regressions, and repeatable state checks;
- targeted model review examines the remaining semantic delta and decision risk;
- real-world acceptance proves the requested external or user-visible outcome.

A passing local gate never proves more than its stated coverage. A model review should not re-read passing evidence unless it challenges the conclusion. Deep review is mandatory when the project's escalation triggers fire, even if local checks pass.

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

Lower layers may explain or challenge higher layers with evidence, but they do not silently overwrite them.

## Feedback to the global loop

Keep project technology, commands, paths, handles, versions, hashes, and transient failures local. Return only a candidate that:

- has a verified causal explanation;
- changes a future reasoning decision;
- removes project-specific nouns;
- states applicability, counterexample, and invalidation signal;
- remains a proposal until the global maintenance task reviews it.
