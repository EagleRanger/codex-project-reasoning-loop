# Context lifecycle and recoverable compaction

Use this policy when a project is long-lived enough that default context loading becomes slow, noisy, or prone to restoring stale routes. The objective is reliable orientation with less default context, while preserving the evidence needed to correct a bad summary.

## Three context layers

### Hot: read on every resume

Keep only the semantics required for the next safe decision:

- current user instruction and applicable project rules;
- project-loop identity, objective, authorities, and acceptance contract;
- active workflow, recipe, or component composition;
- accepted baseline and its evidence pointer;
- mutable and frozen scope;
- blocked, rejected, or superseded routes;
- unresolved risks, permission boundaries, and next checkpoint.

Hot context is a current-truth index, not a narrative history. Retain a tombstone or `superseded_by` pointer for a route whose disappearance could let it silently return.

### Warm: retrieve by relevance

Keep decisions, lessons, components, handoff packets, run receipts, and validation evidence outside the default bundle. Retrieve them only when the current objective, object, version, failure type, tag, contradiction, or evidence pointer requires them.

### Cold: preserve without default loading

Keep native task transcripts, raw logs, old state, screenshots, and historical artifacts with their native owner or in an auditable cold store. The project loop keeps pointers, not copied transcripts.

## Decide whether to continue or split a task

- Continue the same task while one explicit outcome remains active. A user correction inside that outcome does not require a second writing chain.
- Start another task when the outcome, deliverable, or fact owner is materially independent. Pass a crystallized recovery packet instead of copying the old transcript.
- Project/strategy and execution/run tasks may be separate work surfaces, but they share one project loop and one active authority chain.
- Keep one writer for any shared file, GUI, external account, production entrypoint, or canonical project record.

## Compact in two passes

### Pass 1: recall first

Extract the current objective, latest user corrections, settled decisions, authorities, accepted baseline, open work, blocked routes, risks, permission boundaries, evidence pointers, and next checkpoint. Temporary duplication is safer than prematurely deleting a correction.

### Pass 2: precision second

Remove repeated explanation, transient progress narration, regenerable tool output, superseded intermediate drafts, and background that changes no future decision. Preserve source, time, applicability, counterexample, invalidation signal, conflict, and replacement chain.

Compaction changes the default loading set; it does not erase source evidence. Before rewriting the only hot state, preserve the old version in cold storage and record its SHA-256.

## Record a compaction receipt

For a material change in recovery semantics, create a receipt such as `.project-reasoning/context/history/CTX-YYYYMMDD-<slug>.md` containing:

- source task or file identity, time range, and pre-compaction hash;
- cold-copy path and hash;
- retained current facts, user corrections, decisions, risks, blocked routes, and evidence pointers;
- categories removed from the hot set;
- conflicts, replacement links, and unresolved claims;
- new hot files and hashes;
- recovery-test result, time, and rollback location.

## Run the eight-question recovery gate

Give the evaluator only the proposed hot context and require correct answers to:

1. What is the single current objective?
2. Which files, versions, or systems are authoritative?
3. What workflow, recipe, or composition is active?
4. Which baseline has been accepted?
5. Which routes are blocked, rejected, or superseded?
6. What may change, and what must remain frozen?
7. What risks and permission boundaries remain?
8. What is the next checkpoint and its pass/fail signal?

Any missing or contradictory answer makes the compaction `candidate_failed`. Restore the prior hot state, repair the semantics, and test again. Hashes and parser success prove structure, not orientation.

## Archive and deletion states

Use a staged lifecycle:

1. `active`: current work with a passing hot recovery path;
2. `reference`: completed outcome that still has dependencies or correction value;
3. `archived`: reversible UI/archive state while source evidence remains intact;
4. `deletion_candidate`: no active entry or inbound dependency, with verified cold copy and restore drill;
5. `deleted`: executed only after fresh authorization for the exact objects and followed by residual-pointer checks.

Before archive or deletion, verify task ID, title, first effective objective, latest effective objective, project root, inbound references, cold-copy hash, and restore path. Time, sidebar position, similar titles, size, or aggregate token count are not sufficient identity or deletion evidence.

## Optional bundle configuration

The read-only audit script accepts JSON shaped like:

```json
{
  "schema_version": 1,
  "policy_id": "context-lifecycle-v1",
  "thresholds": {
    "hot_file_review_bytes": 32768,
    "hot_bundle_review_bytes": 65536,
    "hot_bundle_review_files": 4
  },
  "projects": [
    {
      "loop_id": "example-project-loop",
      "root": "C:/path/to/project",
      "hot_files": [
        ".project-reasoning/PROJECT_LOOP.md",
        ".project-reasoning/STATE.md"
      ],
      "retrieval_only": [
        ".project-reasoning/DECISIONS.md",
        ".project-reasoning/LESSONS.md"
      ]
    }
  ]
}
```

Thresholds are review triggers. `--strict` may turn warnings into audit failures for a project that deliberately chooses that policy, but it still cannot authorize mutation, archive, or deletion.
