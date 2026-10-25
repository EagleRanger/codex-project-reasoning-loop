# Local validation and model-review policy

Use this policy to reduce repeated quality-review token consumption without reducing outcome assurance. It does not govern Codex Auto-review for sandbox-boundary approvals; see [native-codex-coordination.md](native-codex-coordination.md).

## Core rule

Validate locally first, then spend model attention only on the unresolved semantic or risk-bearing delta. Optimize total verification cost, not token count in isolation.

## Calibrate the acceptance basis

Use this check when the conclusion depends on a classifier, generated summary or proxy metric. Before counting passing tests, inspect the original evidence and one relevant counterexample that would distinguish the desired result from a plausible wrong answer. Confirm that the test's expected outcome matches the user's actual acceptance contract. Directly observable, low-risk edits do not require an additional model reviewer.

For example, an announcement that an event will happen is not evidence that it happened; an average image brightness can be nonzero while the meaningful content region is absent. These are synthetic illustrations, not claims about a particular project. Check the actual object, time, scope and visible result, rather than a convenient aggregate.

Keep implementation validity, observed effect and user acceptance independent. A large passing suite can reproduce the same wrong premise as the implementation. Preserve necessary raw evidence and distinguish contradictory cases before trusting generated labels. Do not replay a successful real action merely to produce a fresh test artifact.

## Evidence ladder

### Tier 0: no-quality-review skip

Skip automated quality-model review when all of the following are true:

- there is no material change to behavior, contract, risk boundary, or active workflow;
- the review key matches a previously accepted receipt;
- no unresolved finding or failed gate has changed state;
- no explicit user or project milestone requires review.

### Tier 1: local deterministic validation

Run the narrowest applicable checks first:

- schema, format, parse, type, and configuration validation;
- changed-file and changed-symbol scope checks;
- unit, regression, invariant, and negative blocked-route tests;
- artifact-pointer, state, and manifest consistency checks;
- reproducible read-only inspection of external state where available.

Record what each gate proves and what it cannot prove. Do not upload or summarize passing raw logs to a model unless a later contradiction makes them relevant.

### Tier 2: targeted model review

Provide only a compact delta packet:

- objective and acceptance contract;
- material changes and affected authorities;
- relevant validated guardrails;
- local-gate summary, failures, and uncertainty;
- unresolved findings and exact review question.

Ask for findings, evidence gaps, and required next checks. Do not ask for a fresh project summary.

### Tier 3: deep model review

Escalate when any of these apply:

- architecture, public contract, security, privacy, or permission boundary changed;
- destructive or external side effects are possible;
- an active verified workflow is being replaced;
- local gates disagree, are incomplete for the main risk, or repeatedly fail without diagnosis;
- milestone or release acceptance is being claimed;
- the user explicitly requests deep review.

Deep review may widen context, but it must still name the risk and stop condition.

## Review key and receipt

Derive a local review key from the material change-set identity, acceptance-contract version, relevant validator versions, unresolved-finding set, and review-policy version. Do not include secrets or raw sensitive content.

Store a compact receipt containing:

- review key and time;
- review tier and escalation reason;
- reviewer, model, and prompt-policy identity;
- reviewed scope;
- local-gate summary;
- finding IDs and resolution state;
- result: accepted, changes required, blocked, or invalidated.

An unchanged key with no open finding is a cache hit and should not trigger a new model review.

The project review policy must say which reviewer, model, or prompt-policy changes invalidate an accepted receipt. Record those identities for audit, but do not automatically re-review unchanged work after every tool or model update unless the assurance policy requires it.

## Budget and stop conditions

Use a soft budget rather than pretending exact token usage is always observable. Declare:

- maximum automatic model-review rounds per checkpoint;
- maximum context scope for targeted review, expressed in project-observable units such as changed files, artifacts, findings, or a bounded delta packet;
- conditions that permit widening the scope;
- the person or loop that owns unresolved findings.

Stop reviewing when acceptance evidence is complete, when the same key already passed, or when another round would contain no new evidence. If the budget is exhausted with unresolved high-risk findings, block the claim or request direction; do not silently accept it.

## Cost metrics

Track locally observable proxies:

- automatic review invocations;
- cache hits and skipped reviews;
- targeted versus deep review rounds;
- files or artifacts included in the delta packet;
- repeated findings without new evidence;
- defects caught locally versus by model review versus real acceptance.

Use these metrics to tune gates and triggers. Do not call the optimization successful merely because fewer reviews ran; compare escaped defects and unresolved risk too.

For a proposed delivery optimization, compare comparable tasks under the same acceptance contract: end-to-end elapsed time, preparation and reading, tool waiting, coordination and review, rework, and final quality. Include worker startup and handoff overhead when evaluating parallelism. State differences in input, environment and actual provider/model; do not assume a configuration changed an already-running agent.

Distinguish cached input, uncached input and output when usage is observable. Cumulative input is neither current context size nor a bill. No reliable baseline means an observation or hypothesis, not a savings claim. Reuse existing natural-task receipts instead of adding calls or business runs just to populate metrics.

A limit on repeated model review stops redundant review, not unfinished authorized diagnosis, bounded repair or required acceptance. Preserve the task's real deadline, budget and safety constraints; hand back only for new authority, a material user choice, a genuine external dependency or verified inability to continue.

