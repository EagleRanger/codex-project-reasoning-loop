# Release notes

## v1.4.0 - 2026-10-25

### 中文更新说明

本版保留“总方法 ↔ 分项目改进”以及具体项目内部“项目＋执行”的分层结构，重点把已有原则接到方法选择、实际调用、验收和恢复入口，不另建任务系统或内部管理岗位。

- **适用方法召回：** 按实际对象、操作、已验范围与失效条件选择方法；区分未找到、误匹配、读到未采用、调用失败和获准例外。发现结果不等于运行许可。
- **验收依据校准：** 对分类、摘要和代理指标，先核原始证据与区分性反例，再信任测试结果；实现通过、实际效果和用户认可分开记录。
- **超长上下文减负：** 主入口改为按需引用；保留旧引用地址，增加精简读取视图的来源、遗漏和回退边界。文件体量、实际读取量和自然效果分别说明。
- **交接结算与行动续接：** 发送、接收和压缩恢复均核对最新结案、撤回及替代；旧批注不重派，结果不明先对账。说明进度、结束阶段或完成子任务不自动等于总目标完成。
- **按完整交付评价优化：** 同等验收下比较总耗时、等待、协调与返工，不能用更少调用或 token 单独证明提速。
- **兼容性：** Skill 名称、项目记录格式及既有验证器保持兼容；不要求安装新服务，不绑定特定模型或本机项目注册表。

本次包含结构与既有验证器回归，以及隔离的合成情境检查。它们不能证明所有模型都会正确采用方法，也不构成自然业务提速、零返工或零误调用的保证。具体结果与边界见本版 Release。

### English summary

- Preserves the global/project feedback cycle and each project's strategy/run separation.
- Connects applicable-method discovery to real entrypoints, current authority and observable adoption stages.
- Calibrates classifier, summary and proxy-based acceptance against source evidence and a discriminating counterexample.
- Adds closure-aware handoffs, reliable continuation and compact read-view boundaries for very long histories.
- Uses progressive disclosure while retaining existing reference paths and record/validator compatibility.
- Evaluates delivery optimizations by comparable elapsed time, waiting, rework and quality, not token count alone.

No live installation, business workflow, account configuration, scheduler or external project is changed by downloading this release.

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
