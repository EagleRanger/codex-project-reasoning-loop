# Task lanes and handoff

Use two native task labels inside one project-specific loop when research, strategy, validation, and real execution otherwise interfere with each other.

## Lane contract

### Project/strategy lane (`【项目】`)

Own:

- project framing, research, assumptions, and strategy;
- isolated idea tests and candidate workflow validation;
- root-cause analysis of execution feedback;
- active workflow selection and replacement approval;
- canonical `PROJECT_LOOP.md`, `STATE.md`, decisions, lessons, and global candidates.

Do not use this lane as the routine scheduled operator. A project-lane experiment remains `validation_only` until a separate real-run handoff names the accepted workflow and authority.

### Execution/run lane (`【执行】`)

Own:

- one scheduled or concrete production objective;
- current run authority, target, inputs, and stop conditions;
- verified active workflow execution;
- direct evidence, terminal status, cleanup, containment, and feedback.

Do not choose a new strategy, widen permissions, change risk or resource limits, activate a candidate workflow, revive a blocked route, or modify global rules. Use only pre-approved recovery actions. Return any required production-logic change to the project lane.

## Project-to-execution packet

Provide the minimum sufficient packet:

```markdown
**Project loop:** stable-loop-id
**Handoff ID:** HO-YYYYMMDD-NNN
**Reasoning source:** native task or artifact pointer
**Active workflow:** immutable identity or version
**Objective:** one bounded outcome
**Authority:** current instruction, contract, or automation binding
**Settled decisions:** choices the run must not reopen
**Open design space:** bounded executor discretion
**Assumptions to test:** falsifiable unknowns
**Inputs and target:** exact scope
**Permitted actions:** explicit boundary
**Acceptance evidence:** observable pass criteria
**Stop conditions:** failure, uncertainty, deadline, or budget
**Rollback or containment:** required safe response
**Report destination:** native task and optional run-record path
**Invalid or reopen when:** authority, input, workflow, target, evidence contract, or stated premise changes
```

Do not copy full project history. Link the current contract and only the relevant decision or lesson.

## Execution-to-project packet

Return:

```markdown
**Run ID:** stable unique run identity
**Handoff ID:** originating handoff
**Workflow identity:** actually resolved version
**Terminal status:** succeeded | failed | interrupted | unknown
**Outcome:** changed | no_action | blocked_before_mutation | effect_unknown
**Observed facts:** direct observations only
**Evidence:** compact pointers, hashes, checks, screenshots, or external-state references
**Evidence settled:** yes | no, plus any pending asynchronous source
**Structural validity:** passed | failed | not_applicable, with evidence limit
**Observed effect:** passed | failed | unverified | not_applicable
**User acceptance:** accepted | rejected | pending | not_applicable
**Deviations:** difference from the packet or `None`
**Containment and cleanup:** completed actions and remaining exposure
**Unresolved questions:** facts the execution lane could not establish
**Proposed follow-up:** optional hypothesis, clearly not an approved strategy
```

The project lane applies the record admission test, diagnoses causes, and decides whether to repair, validate a new candidate, change strategy, or leave the result as a transient run event.

Execution output may nominate a follow-up, but only the project lane may admit it as a project lesson or create a redacted cross-project candidate. The global maintenance task receives candidates, never raw execution packets.

## Multi-agent rules

- Give each agent one bounded responsibility and non-overlapping write scope.
- Let the parent or project lane synthesize; do not require peer-to-peer shared state.
- Use stable task, handoff, run, workflow, and evidence identities.
- Prefer append-only per-run output for concurrent evidence collection and one canonical writer for governance files.
- Bound concurrency, elapsed time, review rounds, and model cost. Stop repeated or decision-irrelevant work.
- Serialize GUI, account, and production resources unless concurrency safety is directly proven.
