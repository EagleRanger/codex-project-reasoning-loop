#!/usr/bin/env python3
"""Read-only structural audit for declared project context bundles."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


RAW_TRANSCRIPT_MARKERS = (
    "TRANSCRIPT START",
    "TRANSCRIPT DELTA START",
    '"response_item"',
    '"event_msg"',
    "tool exec result:",
)


def safe_relative_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"hot/retrieval path must be project-relative: {value}")
    return path


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Context bundle JSON file")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat size/count review warnings as failures.",
    )
    args = parser.parse_args()

    config_path = Path(args.config).expanduser().resolve()
    data = json.loads(config_path.read_text(encoding="utf-8"))
    thresholds = data["thresholds"]
    errors: list[str] = []
    warnings: list[str] = []
    rows: list[dict[str, object]] = []

    seen_loops: set[str] = set()
    for project in data["projects"]:
        loop_id = project["loop_id"]
        if loop_id in seen_loops:
            errors.append(f"duplicate loop_id: {loop_id}")
        seen_loops.add(loop_id)

        root = Path(project["root"]).expanduser()
        if not root.exists():
            errors.append(f"{loop_id}: missing root {root}")
            continue

        hot_files = project["hot_files"]
        if len(hot_files) > thresholds["hot_bundle_review_files"]:
            warnings.append(
                f"{loop_id}: hot bundle has {len(hot_files)} files "
                f"> {thresholds['hot_bundle_review_files']}"
            )

        total_bytes = 0
        file_rows: list[dict[str, object]] = []
        normalized: set[str] = set()
        for relative_value in hot_files:
            try:
                relative = safe_relative_path(relative_value)
            except ValueError as exc:
                errors.append(f"{loop_id}: {exc}")
                continue

            normalized_value = relative.as_posix().lower()
            if normalized_value in normalized:
                errors.append(f"{loop_id}: duplicate hot file {relative_value}")
                continue
            normalized.add(normalized_value)

            path = root / relative
            if not path.is_file():
                errors.append(f"{loop_id}: missing hot file {path}")
                continue

            raw = path.read_bytes()
            total_bytes += len(raw)
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                errors.append(f"{loop_id}: hot file is not UTF-8 text {path}")
                continue

            markers = [marker for marker in RAW_TRANSCRIPT_MARKERS if marker in text]
            if markers:
                errors.append(
                    f"{loop_id}: raw transcript/tool output marker in hot file "
                    f"{relative_value}: {', '.join(markers)}"
                )
            if len(raw) > thresholds["hot_file_review_bytes"]:
                warnings.append(
                    f"{loop_id}: {relative_value} is {len(raw)} bytes "
                    f"> {thresholds['hot_file_review_bytes']}"
                )
            file_rows.append(
                {
                    "path": relative.as_posix(),
                    "bytes": len(raw),
                    "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
                }
            )

        for relative_value in project.get("retrieval_only", []):
            try:
                relative = safe_relative_path(relative_value)
            except ValueError as exc:
                errors.append(f"{loop_id}: {exc}")
                continue
            if not (root / relative).is_file():
                errors.append(f"{loop_id}: missing retrieval-only file {root / relative}")

        if total_bytes > thresholds["hot_bundle_review_bytes"]:
            warnings.append(
                f"{loop_id}: hot bundle is {total_bytes} bytes "
                f"> {thresholds['hot_bundle_review_bytes']}"
            )
        rows.append(
            {
                "loop_id": loop_id,
                "root": str(root),
                "hot_file_count": len(file_rows),
                "hot_bytes": total_bytes,
                "hot_files": file_rows,
            }
        )

    result = {
        "schema_version": 1,
        "policy_id": data.get("policy_id"),
        "status": "fail" if errors or (args.strict and warnings) else "pass",
        "projects": rows,
        "warnings": warnings,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["status"] == "fail" else 0


if __name__ == "__main__":
    sys.exit(main())

