# Verified capability module registry

Use a component registry only when a project has capabilities that are independently accepted and reused across phases, workflows, or run lanes. The registry prevents later work from silently rewriting accepted behavior or rebuilding a parallel route.

## Core model

Keep one project-local `.project-reasoning/COMPONENTS.json` as the machine authority for module identity and status. The project contract explains how the registry is used; it does not copy component status, hashes, evidence, or dependencies.

Each component defines:

- a stable `id`, `type`, and lifecycle `status`;
- one `entry` or `contract_version`;
- `accepted_scope`: what direct evidence actually proved;
- `dependencies`: other registered modules required at runtime;
- `evidence`: compact local pointers supporting acceptance;
- `reuse_rule`: when later work must call the module instead of rebuilding it;
- `invalidated_by`: conditions that require a new validation decision;
- optional protected `artifacts` with deterministic fingerprints.

Use lifecycle states deliberately:

- `verified`: independently accepted and frozen for its stated scope;
- `active_with_regression`: usable only under the named regression or containment;
- `validation_only`: candidate or experiment; never an implicit production dependency;
- `planned`: accepted need without an implementation;
- `blocked` or `rejected`: unavailable to normal composition;
- `superseded`: historical identity replaced by another named module.

## Freeze and replacement

Freezing protects the accepted scope, not every future use case.

1. Reuse a verified module unchanged when the requested capability is inside its accepted scope.
2. Compose it behind a new outer adapter when the new phase only changes dispatch, inputs, or presentation.
3. Create a new module ID when implementation or accepted semantics must change.
4. Validate the candidate independently while retaining the verified module as rollback.
5. Switch a production recipe only after all dependencies and acceptance policies are independently accepted.
6. Preserve rejected and superseded identities so old entrypoints can be blocked deterministically.

Never refresh a protected hash merely to make a validator pass. Explain the change, decide whether the old module remains valid, and either restore it or promote a new identity.

## Artifact fingerprints

The default validator supports:

- `file`: SHA-256 over the entire file;
- `python_symbols`: SHA-256 over the exact source of named top-level Python functions or classes, in listed order.

Use a whole-file lock for small, cohesive modules. Use symbol locks only when a verified capability remains embedded in a larger legacy Python file and unrelated changes should not invalidate it. Include every helper whose behavior is part of the accepted scope; a symbol lock is not proof of dependencies that were omitted.

## Composition rules

- A `verified` component must be frozen, have evidence, accepted scope, reuse rule, and invalidation signals.
- A verified component may depend only on other verified, frozen components.
- A verified production recipe may contain only verified, frozen components and verified acceptance policies.
- Policies, executable components, volatile run state, and explanatory documents remain separate types.
- A project with no accepted implementation may register planned components; it must not manufacture `verified` status from architecture notes or tool installation.

Run:

```powershell
python <skill-dir>/scripts/validate_component_registry.py --root <project-root>
```

The validator checks structure, IDs, dependencies, cycles, production composition, local evidence pointers, and protected artifact fingerprints. Project-specific runtime gates may add stricter checks but should reference the same registry instead of creating another component ledger.
