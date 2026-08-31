# Artifact schema

Use one project-local directory: `.project-reasoning/`.

## Contents

- [`PROJECT_LOOP.md`](#project_loopmd)
- [`STATE.md`](#statemd)
- [Optional per-run record](#optional-per-run-record)
- [`DECISIONS.md`](#decisionsmd)
- [`LESSONS.md`](#lessonsmd)
- [`GLOBAL_CANDIDATES.md`](#global_candidatesmd)
- [Record quality](#record-quality)

### `PROJECT_LOOP.md`

Use this as the canonical project-specific loop contract for substantial multi-session work.

```markdown
# Project Loop Contract

**Loop ID:** stable-project-loop-id
**Status:** active | paused | retired
**Global loop:** project-reasoning-loop
**Updated:** YYYY-MM-DD

## Identity and scope
- Native Codex project or local-folder identity and related task/chat lanes.
- Objective and acceptance evidence.
- Non-goals and project boundary.

## Authority map
- Current user objective or project contract.
- Roadmap or phase plan.
- Active workflow or implementation pointer, when applicable.
- Current state, evidence, decisions, lessons, and run records.

## Task lanes and handoff
- Project/strategy lane and its canonical write ownership.
- Execution/run lane and its permitted run scope.
- Explore, Crystallize, Execute, and Reflect phase ownership plus the crystallization-gate rule.
- Project-to-execution packet and execution-to-project feedback locations.
- Parallel-safe work, serialized resources, and escalation path.

## Inbound from global loop
- Reviewed methods applied or localized.
- Relevant methods rejected for this project and why.

## Execution and recovery
- Local validation gates and their evidence limits.
- Quality-review triggers, scope budget, review-policy version, review receipt, invalidation, and stop conditions.
- Current side-effect authority, irreversible-action containment, unknown-run reconciliation, rollback, and run-manifest policy.
- Structural-validity, observed-effect, and user-acceptance conclusions, each with its own evidence limit.
- Mutable authority and workflow pointers plus the conditions that invalidate prior validation or recovery receipts.

## Outbound to global loop
- Candidate queue and prohibited project-specific content.
- Project-local admission owner and maturity required before an outbound candidate may be proposed.
- Redaction boundary for project names, paths, task IDs, accounts, private URLs, logs, hashes, and implementation incidents.

## Current phase and next checkpoint
- Current phase, smallest falsifiable next action, and pass/fail signal.
```

### `STATE.md`

Keep this file short enough to read at every substantial resume.

```markdown
# Project State

Updated: YYYY-MM-DD

## Objective
Concrete outcome and acceptance evidence.

## Current truth
- Verified facts only.

## Active work
- Current checkpoint and affected area.

## Risks and blockers
- Risk, evidence, and owner or unblock condition.

## Rejected approaches
- Approach - reason - reconsider when.

## Next checkpoint
- Smallest next action and its pass/fail signal.
```

### Optional per-run record

Use `.project-reasoning/runs/<run-id>.md` only when the run has external effects, recovery value, or a governed handoff. Keep live progress in the native task.

```markdown
# Execution Run

**Run ID:** stable-run-id
**Handoff ID:** HO-...
**Project loop:** stable-project-loop-id
**Workflow identity:** immutable version
**Owner:** execution task or agent identity
**Terminal status:** pending | running | succeeded | failed | interrupted | unknown

## Authority and scope
- Reasoning source, current authority, settled decisions, open design space, assumptions to test, target, inputs, permitted actions, and invalidation.

## Acceptance and stop conditions
- Direct evidence contract, deadline or budget, containment, and rollback.

## Result and feedback
- Separate structural-validity, observed-effect, and user-acceptance conclusions; use `not_applicable` or `unverified` instead of inferring a pass.
- Outcome type, observed facts, evidence pointers, evidence-settlement state, mutation or non-mutation evidence, deviations, cleanup, unresolved questions, and optional proposed follow-up.
```

The execution lane may create and finalize its own run record. The project lane alone decides what enters canonical state, decisions, lessons, or global candidates.

### `DECISIONS.md`

Append decisions that constrain future work.

```markdown
## DEC-YYYYMMDD-NNN: Short title

**Status:** active | superseded | reversed
**Scope:** project | subsystem
**Tags:** comma-separated
**Date:** YYYY-MM-DD

### Context
What decision was required.

### Decision
What was selected.

### Alternatives
What was rejected and why.

### Evidence
Tests, observations, or constraints supporting the decision.

### Revisit when
Specific invalidation or reversal conditions.
```

### `LESSONS.md`

Use entries for concrete events and validated project lessons.

```markdown
## LES-YYYYMMDD-NNN: Short title

**Scope:** event | project
**Status:** observed | investigating | validated | superseded | rejected
**Tags:** comma-separated
**Date:** YYYY-MM-DD

### Observation
What happened, without interpretation.

### Prior assumption
What was believed before the evidence appeared.

### Root cause
Verified cause, or `Unverified` while investigating.

### Evidence
Reproduction, test, log reference, or comparison.

### Project guardrail
Conditional prevention step for this project, or `None` for an unresolved event.

### Applicability
Where this lesson applies.

### Counterexample
When following the guardrail would be wrong.
```

### `GLOBAL_CANDIDATES.md`

Store proposals only. A candidate is not a global rule.

```markdown
## GRC-YYYYMMDD-NNN: Short title

**Status:** proposed | eligible | approved | rejected | superseded
**Tags:** comma-separated reasoning categories
**Date:** YYYY-MM-DD
**Origin-Projects:** project-a, project-b
**Origin-Lessons:** LES-..., LES-...

### Reasoning failure
The transferable failure in framing, assumptions, evidence, decomposition, risk, validation, or recovery.

### Proposed reasoning rule
A conditional question or procedure independent of project technology.

### Evidence
How independent contexts support the abstraction.

### Applicability
Conditions under which the rule should be consulted.

### Counterexample
Conditions under which the rule would mislead.

### Invalidation signal
Evidence that should cause review or retirement.
```

## Record quality

- Before any durable write, apply the Skill's record admission test and choose: reject, link to authority, merge or update, or record. Do not add a second log merely to prove the test ran.
- Keep facts with their authoritative owner. If a source file, configuration, native Codex task, or ordinary run log can answer the question cheaply and reliably, store a stable pointer plus only the non-obvious decision, caveat, exception, or recovery consequence.
- Require future decision value: a record must change later action, preserve authority or recovery truth, explain a durable decision, or prevent a validated recurrence.
- Separate observation, inference, and assumption. Repository scanning alone cannot nominate a pitfall; unverified events remain `investigating` and cannot supply a validated guardrail.
- Prefer links or compact evidence summaries over pasted logs.
- Redact credentials, personal data, private URLs, and unnecessary file contents.
- Update an existing entry instead of creating a duplicate.
- Use tags for retrieval; examples: `assumption`, `evidence`, `scope`, `rollback`, `validation`, `decomposition`, `recovery`.
- Preserve rejected and superseded records so future work can understand why a rule is inactive.
- Keep `PROJECT_LOOP.md` as the canonical contract. Optional machine-readable indexes must point back to it and be checked for consistency rather than becoming an independent source of truth.
- Keep exploratory dialogue with its native task. When an idea must survive across sessions, store only a source pointer and the minimum decision-relevant definition, scope, counterexample, unresolved question, and maturity; do not create a second conversation archive.
- When automated model review is enabled, keep its review key and unresolved findings in a compact project-local receipt or state file; do not require the reviewer to reconstruct them from full chat history.
