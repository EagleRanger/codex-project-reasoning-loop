#!/usr/bin/env python3
"""Create missing project-reasoning artifacts without overwriting user files."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


TEMPLATES = {
    "STATE.md": """# Project State

Updated: YYYY-MM-DD

## Objective

## Current truth

## Active work

## Risks and blockers

## Rejected approaches

## Next checkpoint
""",
    "DECISIONS.md": """# Decisions

Append durable decisions using the schema in the project-reasoning-loop Skill.
""",
    "LESSONS.md": """# Project Lessons

Record concrete events and validated project lessons. Do not place global rules here.
""",
    "GLOBAL_CANDIDATES.md": """# Cross-Project Reasoning Candidates

These are proposals only. Promotion requires evidence, boundary analysis, and user approval.
""",
}


def project_loop_template(loop_id: str) -> str:
    return f"""# Project Loop Contract

**Loop ID:** {loop_id}
**Status:** active
**Global loop:** project-reasoning-loop
**Updated:** {date.today().isoformat()}

## Identity and scope

- Native Codex project or local-folder identity:
- Related task/chat lanes and distinct outcomes:
- Objective:
- Acceptance evidence:
- Non-goals:

## Authority map

- Current user objective or project contract:
- Roadmap or phase plan:
- Active workflow or implementation pointer:
- Current evidence and run records:

## Inbound from global loop

- Applied or localized methods:
- Relevant methods rejected and why:

## Execution and recovery

- Local validation gates and evidence limits:
- Quality-review triggers and maximum scope:
- Review-policy version, budget, receipt, invalidation, and stop conditions:
- Current side-effect authority and shared-resource ownership:
- Irreversible-action containment and unknown-run reconciliation:
- Rollback and recovery:
- Per-run manifest policy:

## Outbound to global loop

- Candidate queue: `.project-reasoning/GLOBAL_CANDIDATES.md`
- Project-specific content that must remain local:

## Current phase and next checkpoint

- Current phase:
- Next falsifiable checkpoint:
- Pass/fail signal:
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument(
        "--loop-id",
        help="Stable project-specific loop identifier (defaults to <root-name>-project-loop)",
    )
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    target = root / ".project-reasoning"
    target.mkdir(parents=True, exist_ok=True)
    loop_id = args.loop_id or f"{root.name}-project-loop"
    templates = {"PROJECT_LOOP.md": project_loop_template(loop_id), **TEMPLATES}

    created: list[str] = []
    preserved: list[str] = []
    for name, content in templates.items():
        path = target / name
        if path.exists():
            preserved.append(name)
            continue
        path.write_text(content, encoding="utf-8", newline="\n")
        created.append(name)

    print(f"Project reasoning directory: {target}")
    print("Created: " + (", ".join(created) if created else "none"))
    print("Preserved: " + (", ".join(preserved) if preserved else "none"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

