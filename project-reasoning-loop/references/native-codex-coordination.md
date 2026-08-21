# Native Codex coordination

Use Codex project and task management as the transport and live-state layer. Add a project-specific loop only for durable project semantics that would otherwise be scattered across chats or stale files.

## One fact, one owner

| Information | Authoritative owner | Project-loop treatment |
|---|---|---|
| Task transcript and user messages | Native task/chat | Store only task ID and a short relevance pointer |
| Live turn, tool, approval, and interruption status | Native task/runtime | Read live; do not mirror in `STATE.md` |
| Project folders and shared instructions | Native project plus `AGENTS.md` | Reference them in the authority map |
| Scheduled-task timing and binding | Native automation | Reference automation ID; do not copy its schedule |
| Project objective and acceptance contract | Project loop | Store canonically |
| Current phase, active workflow, blocked routes, and recovery state | Project loop | Store canonically and validate |
| Durable decisions and validated lessons | Project loop | Store compact records with evidence links |
| Cross-project reasoning candidates | Project loop candidate queue | Keep proposed until global review |

If the native layer already provides a fact, link it instead of reproducing it. If the project loop needs a stable snapshot, record the minimum derived conclusion plus its task ID, timestamp, and evidence pointer.

## Map projects, tasks, and run lanes

Use this default mapping:

```text
Codex project or shared project folder
└── one actual project entity and one project-specific loop
    ├── 【项目】 task/chat: strategy, research, validation, diagnosis, canonical decisions
    ├── 【执行】 task/chat: scheduled or concrete production run and feedback
    └── optional bounded sub-agents: independent evidence or disjoint work only
```

Create separate project loops only when objectives, authorities, production workflows, risk boundaries, or recovery states are materially independent. A separate sidebar title alone is not enough.

Task labels describe responsibility, not authority. `【项目】` is the project-loop steward and canonical writer. `【执行】` follows one approved handoff and returns evidence; it cannot silently change the active workflow or project strategy. Both labels reuse the same project loop and native Codex remains authoritative for each task's live state.

When a task mixes strategy testing and real execution, stop before side effects and split it at the handoff boundary. Keep candidate testing isolated, then issue a compact project-to-execution packet. Return a compact execution-to-project packet after the run. See `task-lane-handoff.md`.

Native multi-agent work is most useful for independent questions, disjoint write scopes, and separate verification. Do not parallelize shared GUI state, external accounts, the same production entrypoint, or overlapping files. Parent-mediated synthesis and append-only run outputs are safer than assuming peer agents share current state.

For a broad craft area such as presentations, distinguish the reusable production method from a concrete deliverable. Keep shared craft guidance in the applicable Skill or project instructions; keep deliverable-specific decisions and evidence with the actual project. Do not build another umbrella loop that repeats both.

## Resume without replay

On resume:

1. read native task status and the current user instruction;
2. read the project-loop contract and compact project state;
3. retrieve only relevant decisions, lessons, and referenced task turns;
4. continue from the next falsifiable checkpoint.

Do not summarize the entire task transcript into `STATE.md`. Do not copy every tool event into a project ledger. Preserve only conclusions needed to make the next project decision safely.

## Separate quality review from Auto-review

Quality review evaluates whether project work is correct and complete. It may use local gates, targeted model review, deep review, and review receipts.

Codex Auto-review evaluates whether an eligible sandbox-boundary escalation should run. It does not grant new permissions and does not replace project acceptance. It normally triggers only when a tool or command requests access outside the active sandbox or policy.

To reduce Auto-review volume safely:

- first identify repeated, legitimate boundary crossings from retained session evidence;
- prefer work inside the project's existing writable roots;
- propose only narrow additional writable roots for intentional neighboring project or scratch locations;
- propose precise command-prefix rules for repeated safe commands, never broad interpreter or network prefixes;
- keep destructive, secret-bearing, external, or unusual actions reviewable;
- require explicit user authorization before changing permissions or review policy.

Reducing quality-review rounds does not reduce Auto-review traffic unless it also removes unnecessary boundary-crossing actions. Measure the two systems separately.
