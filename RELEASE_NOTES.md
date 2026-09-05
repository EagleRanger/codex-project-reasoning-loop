# Release notes

## v1.3.0 - 2026-09-06

- Adds a generative main-contradiction method: identify the relation that most enables or suppresses the desired possibility, preserve effective parts, rewrite the blocking mechanism, and revise from positive and negative feedback.
- Connects exploration, testing, evidence admission, retrieval, reuse, and revision through existing project authorities instead of creating another memory database.
- Makes task continuation explicit: questions, corrections, compatible additions, and local pauses steer an active outcome rather than silently cancelling it; phases and partial outputs are not completion.
- Gives current authority and the latest applicable correction priority while retaining older failures and counterexamples as relevance-triggered evidence.
- Clarifies bounded model and agent routing: host policy chooses the worker, while permissions, acceptance evidence, and completion criteria remain unchanged.
- Adds `continuity-and-learning.md` and updates context compaction, task handoffs, contracts, agent metadata, and public documentation.

## v1.2.0 - 2026-08-31

- Makes the two-level architecture explicitly bidirectional: global methods are localized by each project, and validated project lessons return only as redacted candidates for global review.
- Makes the internal Project/strategy and Execution/run split explicit for each concrete project: both lanes share one project Loop, while execution remains bounded and returns evidence to the project lane.
- Optimizes long-running, very large projects and long context histories through hot/warm/cold context layers, lane-specific compact recovery packets, semantic recovery gates, and receipt invalidation after material change.
- Separates structural validity, observed real effect, and user acceptance into independent claim dimensions; one passing dimension no longer implies the others.
- Requires mutable authority and workflow pointers to resolve against their current owner at validation time; historical identifiers remain frozen fixtures only when declared as such.
- Invalidates recovery and compaction receipts when objective, authority, active workflow, permissions, or acceptance semantics materially change.
- Requires execution feedback to pass through project-local admission before it can become a project lesson or cross-project candidate.
- Strengthens the public privacy boundary: concrete project names, paths, task IDs, account data, private URLs, logs, hashes, and implementation incidents remain outside the reusable Skill.
- Updates the project contract, artifact schemas, promotion policy, handoffs, context lifecycle, and public documentation to reflect the current total-to-project-to-total improvement cycle.

## v1.1.0 - 2026-08-22

- Adds an Explore-Crystallize-Execute-Reflect cycle without creating a second task or conversation store.
- Adds compact reasoning-source, settled-decision, open-design-space, assumption, and reopen fields to task handoffs.
- Requires admission gates before the first governed mutation and recognizes evidence-backed no-action or zero-change outcomes.
- Adds bounded evidence settlement for asynchronous terminal signals and a two-pass baseline/exception convergence method.
- Separates knowledge type from evidence maturity so project facts, thinking operators, Skills, and raw history do not promote by category confusion.
- Adds a record admission test that rejects duplicate, cheaply derivable, transient, or weakly evidenced project records.
- Requires scheduled reviews to propose evidence-backed improvements without manufacturing lessons or automatically rewriting global rules.
- Separates `【项目】` strategy/validation tasks from `【执行】` production/run tasks while keeping one project loop.
- Adds compact project-to-execution and execution-to-project handoff contracts, single-writer governance, and bounded multi-agent rules.
- Adds hot/warm/cold context lifecycle governance for long-running projects.
- Adds recall-first and precision-first compaction, compaction receipts, and an eight-question hot-only recovery gate.
- Separates reversible task archive from dependency-checked, restore-tested, explicitly authorized physical deletion.
- Adds a read-only context-bundle audit script; size and file-count thresholds remain review triggers rather than mutation authority.
- Credits OpenAI Codex for AI-assisted architecture synthesis, drafting, implementation support, validation design, and documentation organization.

## v1.0.0 - 2026-08-09

Initial public release.

- Adds the global-to-project reasoning-loop architecture.
- Defines the boundary between native Codex task state and durable project state.
- Adds Light, Standard, and Full governance modes.
- Adds project initialization and structured-record validation scripts.
- Adds workflow-replacement, recovery, and real-run guardrails.
- Adds local-first review, review-key caching, and model-review budgets.
- Adds evidence-gated cross-project lesson promotion.
- Includes bilingual public documentation and explicit risk boundaries.
