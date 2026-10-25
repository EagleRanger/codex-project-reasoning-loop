# Record Lifecycle

Read initialization only for a missing or substantially changed project contract; admission before durable writes; promotion only for cross-project candidates. These are distinct triggers, not a mandatory sequence.

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

Read [references/project-loop-contract.md](project-loop-contract.md) before establishing or substantially changing a project loop. Read [references/validation-review-policy.md](validation-review-policy.md) when a project uses automated model review, has costly validation, or needs a review-budget policy. Read [references/artifact-schema.md](artifact-schema.md) before creating or substantially editing records. Read [references/promotion-policy.md](promotion-policy.md) before proposing or promoting a cross-project lesson.

## Run the record admission test

Run this test before creating or materially updating any durable project record. Decide the resulting action; do not create a separate admission log unless the decision itself changes future work.

1. **Owner**: identify the authoritative owner. If the item is a live task status, transcript, approval, tool result, source file, configuration value, or ordinary run log, keep it with its native owner and store only a stable pointer when needed.
2. **Derivability**: ask whether the item can be read cheaply and reliably from a current authoritative source. If yes, retrieve it live; record only the pointer plus a non-obvious decision, caveat, exception, or recovery consequence.
3. **Future decision value**: require the item to change a future action, prevent a validated recurrence, preserve authority or recovery truth, or explain a durable decision. Reject transient narration and facts that do not affect later behavior.
4. **Evidence maturity**: separate observation, inference, and assumption. An unverified event may be recorded as `investigating`, but only an observed failure with useful causal evidence may nominate a project guardrail or cross-project candidate.
5. **Scope and duplication**: update or supersede an existing record instead of adding a near-duplicate. Keep project-specific content in the project; send only abstract reasoning candidates to global review.
6. **Minimum necessary evidence**: retain the smallest redacted evidence that supports the claim. Do not copy full chats, raw traces, secrets, personal data, or large logs into project records.

Choose one result: **reject**, **link to authority**, **merge or update**, or **record**. A scheduled review must not manufacture lessons from repository scanning, treat the absence of recent failures as proof of improvement, or promote a candidate without the normal evidence and approval guardrails.


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

- Remove concrete project names, local paths, task IDs, account data, private URLs, raw logs, unique hashes, and implementation incidents before a project candidate leaves its project boundary.
An explicit user instruction may set a global operating policy without pretending that the policy is an empirically proven cross-project lesson. Record its source, scope, boundary, and reversal condition as a decision. Continue to label the supporting project candidate by its actual evidence stage.
