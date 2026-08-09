#!/usr/bin/env python3
"""Validate structured project lesson and global-candidate Markdown records."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


HEADING_RE = re.compile(r"^## ((?:LES|GRC)-\d{8}-\d{3}):\s+(.+)$", re.MULTILINE)
FIELD_RE = re.compile(r"^\*\*([^*]+):\*\*\s*(.*)$", re.MULTILINE)

REQUIRED = {
    "LES": {
        "fields": {"Scope", "Status", "Tags", "Date"},
        "sections": {
            "Observation",
            "Prior assumption",
            "Root cause",
            "Evidence",
            "Project guardrail",
            "Applicability",
            "Counterexample",
        },
    },
    "GRC": {
        "fields": {
            "Status",
            "Tags",
            "Date",
            "Origin-Projects",
            "Origin-Lessons",
        },
        "sections": {
            "Reasoning failure",
            "Proposed reasoning rule",
            "Evidence",
            "Applicability",
            "Counterexample",
            "Invalidation signal",
        },
    },
}

PROJECT_LOOP_FIELDS = {"Loop ID", "Status", "Global loop", "Updated"}
PROJECT_LOOP_SECTIONS = {
    "Identity and scope",
    "Authority map",
    "Inbound from global loop",
    "Execution and recovery",
    "Outbound to global loop",
    "Current phase and next checkpoint",
}


def split_entries(text: str) -> list[tuple[str, str, str]]:
    matches = list(HEADING_RE.finditer(text))
    entries: list[tuple[str, str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        entries.append((match.group(1), match.group(2), text[match.end() : end]))
    return entries


def validate_entry(entry_id: str, title: str, body: str) -> list[str]:
    kind = entry_id[:3]
    spec = REQUIRED[kind]
    fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(body)}
    sections = {
        match.strip()
        for match in re.findall(r"^###\s+(.+?)\s*$", body, flags=re.MULTILINE)
    }
    errors: list[str] = []

    if not title.strip():
        errors.append(f"{entry_id}: title is empty")
    for field in sorted(spec["fields"] - fields.keys()):
        errors.append(f"{entry_id}: missing field {field}")
    for field in sorted(spec["fields"] & fields.keys()):
        if not fields[field]:
            errors.append(f"{entry_id}: empty field {field}")
    for section in sorted(spec["sections"] - sections):
        errors.append(f"{entry_id}: missing section {section}")

    if kind == "GRC" and fields.get("Status") in {"eligible", "approved"}:
        projects = [
            item.strip()
            for item in fields.get("Origin-Projects", "").split(",")
            if item.strip()
        ]
        if len(set(projects)) < 2:
            errors.append(
                f"{entry_id}: eligible/approved candidate needs at least two origin projects"
            )

    return errors


def validate_project_loop(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    fields = {key.strip(): value.strip() for key, value in FIELD_RE.findall(text)}
    sections = {
        match.strip()
        for match in re.findall(r"^##\s+(.+?)\s*$", text, flags=re.MULTILINE)
    }
    errors: list[str] = []
    for field in sorted(PROJECT_LOOP_FIELDS - fields.keys()):
        errors.append(f"PROJECT_LOOP.md: missing field {field}")
    for field in sorted(PROJECT_LOOP_FIELDS & fields.keys()):
        if not fields[field]:
            errors.append(f"PROJECT_LOOP.md: empty field {field}")
    for section in sorted(PROJECT_LOOP_SECTIONS - sections):
        errors.append(f"PROJECT_LOOP.md: missing section {section}")
    if fields.get("Status") not in {"active", "paused", "retired"}:
        errors.append("PROJECT_LOOP.md: Status must be active, paused, or retired")
    if fields.get("Global loop") != "project-reasoning-loop":
        errors.append("PROJECT_LOOP.md: Global loop must be project-reasoning-loop")
    if fields.get("Updated") == "YYYY-MM-DD":
        errors.append("PROJECT_LOOP.md: Updated is still a placeholder")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root")
    parser.add_argument(
        "--require-project-loop",
        action="store_true",
        help="Require and validate PROJECT_LOOP.md",
    )
    args = parser.parse_args()

    base = Path(args.root).expanduser().resolve() / ".project-reasoning"
    files = [base / "LESSONS.md", base / "GLOBAL_CANDIDATES.md"]
    errors: list[str] = []
    record_count = 0

    project_loop_path = base / "PROJECT_LOOP.md"
    if project_loop_path.exists():
        errors.extend(validate_project_loop(project_loop_path))
    elif args.require_project_loop:
        errors.append(f"missing file: {project_loop_path}")

    for path in files:
        if not path.exists():
            errors.append(f"missing file: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        entries = split_entries(text)
        record_count += len(entries)
        seen: set[str] = set()
        for entry_id, title, body in entries:
            if entry_id in seen:
                errors.append(f"{path.name}: duplicate id {entry_id}")
            seen.add(entry_id)
            errors.extend(validate_entry(entry_id, title, body))

    if errors:
        print(f"Validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {record_count} structured record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

