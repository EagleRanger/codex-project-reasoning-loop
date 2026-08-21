# Cross-project promotion policy

Cross-project knowledge is limited to transferable reasoning methods. Keep technical facts and implementation constraints inside their projects.

## Eligible categories

- problem framing and acceptance criteria;
- fact, inference, and assumption separation;
- evidence quality and falsification;
- task decomposition and uncertainty ordering;
- reversibility, blast radius, and rollback;
- decision comparison and second-order effects;
- validation, recovery, and state continuity;
- recognizing and correcting repeated reasoning patterns.

## Ineligible content

- package, framework, API, path, command, or operating-system rules;
- a preference that belongs to one user or repository;
- transient service failures or permission restrictions;
- conclusions supported only by repeated observations from the same unresolved root cause;
- absolute rules with no stated boundary or counterexample.

## Promotion stages

1. **Observed event** - preserve evidence without generalizing.
2. **Validated project lesson** - establish root cause and a project guardrail.
3. **Cross-project candidate** - abstract the reasoning structure and compare independent contexts.
4. **Eligible candidate** - meet every quality gate below.
5. **Approved global rule** - obtain user approval for the exact rule and destination.
6. **Review or retirement** - supersede the rule when counterevidence or changed conditions appear.

## Keep knowledge type separate from maturity

Classify what an item is independently from how strongly it is supported:

- a cognitive kernel expresses stable judgment boundaries;
- a thinking operator is an optional way to explore or compare;
- a procedure or Skill tells an executor how to act;
- project truth records the current authoritative state of one project;
- raw history or evidence remains with its native owner.

Then assign the actual maturity stage above. Do not turn a persuasive seed into a mandatory operator, a project fact into global memory, raw history into a Skill, or an approved procedure into a universal answer. A type change requires a separate admission decision.

## Quality gates

Require all of the following before marking a candidate `eligible`:

- the originating project lessons are `validated`;
- the causal explanation is explicit;
- at least two meaningfully different tasks support it;
- normally at least two different projects support it;
- project-specific nouns have been removed from the proposed rule;
- applicability, counterexample, and invalidation signal are non-empty;
- the rule changes a future decision or check, rather than merely describing the past;
- no higher-priority safety or user instruction conflicts with it.

## Preferred rule form

Prefer a conditional procedure:

```text
When <observable conditions>, before <high-impact action>, verify <uncertain premise>
with <evidence>. If the result is <failure signal>, choose <reversible fallback>.
```

Avoid universal prohibitions such as `Never use X` unless X is unsafe in every relevant context.

## Approval payload

Before writing a global rule, show:

- exact proposed text;
- evidence and origin projects;
- applicability and counterexample;
- destination file;
- existing rule it replaces, if any.

Do not treat silence, recurrence count, or a Skill instruction as user approval.

## User-set operating policy

Distinguish empirical promotion from an explicit user policy decision. The user may directly require a global workflow architecture or collaboration rule even when cross-project evidence is incomplete. In that case:

- record the exact instruction, scope, boundary, and reversal condition as a decision;
- adopt it as user policy only within that stated scope;
- keep any supporting cross-project candidate at its actual evidence stage;
- do not describe the policy as a universally validated causal law.

