#!/usr/bin/env python3
"""Validate the default project-local verified capability registry."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
from typing import Any


ALLOWED_COMPONENT_STATUS = {
    "verified",
    "active_with_regression",
    "validation_only",
    "planned",
    "blocked",
    "rejected",
    "superseded",
}
ALLOWED_RECIPE_STATUS = {"verified", "validation_only", "planned", "superseded"}
ALLOWED_POLICY_STATUS = {"verified", "validation_only", "planned", "superseded"}
HARD_UNAVAILABLE_DEPENDENCY_STATUS = {"blocked", "rejected", "superseded"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def resolve_local(root: Path, raw: str, label: str) -> Path:
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f"{label}_PATH_EMPTY")
    candidate = (root / raw).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"{label}_OUTSIDE_PROJECT:{raw}") from exc
    if not candidate.is_file():
        raise ValueError(f"{label}_MISSING:{raw}")
    return candidate


def python_symbol_digest(path: Path, symbols: list[str]) -> str:
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(path))
    nodes: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            nodes[node.name] = node
    material: list[str] = []
    for name in symbols:
        node = nodes.get(name)
        if node is None or not hasattr(node, "end_lineno"):
            raise ValueError(f"PYTHON_SYMBOL_MISSING:{path.name}:{name}")
        segment = ast.get_source_segment(text, node)
        if segment is None:
            raise ValueError(f"PYTHON_SYMBOL_SOURCE_UNAVAILABLE:{path.name}:{name}")
        material.append(f"{name}\n{segment.replace(chr(13) + chr(10), chr(10))}")
    return sha256_bytes(("\n\n".join(material) + "\n").encode("utf-8"))


def validate_artifact(root: Path, component_id: str, artifact: dict[str, Any]) -> None:
    kind = artifact.get("kind")
    raw_path = artifact.get("path")
    expected = str(artifact.get("sha256", "")).upper()
    if len(expected) != 64 or any(ch not in "0123456789ABCDEF" for ch in expected):
        raise ValueError(f"ARTIFACT_HASH_INVALID:{component_id}:{raw_path}")
    path = resolve_local(root, raw_path, f"ARTIFACT:{component_id}")
    if kind == "file":
        actual = sha256_bytes(path.read_bytes())
    elif kind == "python_symbols":
        symbols = artifact.get("symbols")
        if not isinstance(symbols, list) or not symbols or any(not isinstance(x, str) or not x for x in symbols):
            raise ValueError(f"PYTHON_SYMBOL_LIST_INVALID:{component_id}:{raw_path}")
        if len(symbols) != len(set(symbols)):
            raise ValueError(f"PYTHON_SYMBOL_LIST_DUPLICATE:{component_id}:{raw_path}")
        actual = python_symbol_digest(path, symbols)
    else:
        raise ValueError(f"ARTIFACT_KIND_INVALID:{component_id}:{kind}")
    if actual != expected:
        raise ValueError(f"ARTIFACT_FINGERPRINT_MISMATCH:{component_id}:{raw_path}:{actual}")


def require_text(record: dict[str, Any], field: str, prefix: str) -> None:
    value = record.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{prefix}_{field.upper()}_MISSING")


def require_string_list(record: dict[str, Any], field: str, prefix: str, allow_empty: bool = False) -> list[str]:
    value = record.get(field)
    if not isinstance(value, list) or (not allow_empty and not value):
        raise ValueError(f"{prefix}_{field.upper()}_INVALID")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{prefix}_{field.upper()}_INVALID")
    if len(value) != len(set(value)):
        raise ValueError(f"{prefix}_{field.upper()}_DUPLICATE")
    return value


def detect_cycles(components: dict[str, dict[str, Any]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(component_id: str) -> None:
        if component_id in visiting:
            raise ValueError(f"COMPONENT_DEPENDENCY_CYCLE:{component_id}")
        if component_id in visited:
            return
        visiting.add(component_id)
        for dependency in components[component_id].get("dependencies", []):
            visit(dependency)
        visiting.remove(component_id)
        visited.add(component_id)

    for component_id in components:
        visit(component_id)


def validate(root: Path, registry_path: Path) -> dict[str, Any]:
    data = json.loads(registry_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("COMPONENT_REGISTRY_SCHEMA_INVALID")
    if data.get("status") != "active":
        raise ValueError("COMPONENT_REGISTRY_NOT_ACTIVE")
    require_text(data, "loop_id", "REGISTRY")

    component_rows = data.get("components")
    policy_rows = data.get("acceptance_policies", [])
    recipe_rows = data.get("recipes", [])
    if not isinstance(component_rows, list) or not component_rows:
        raise ValueError("COMPONENTS_INVALID")
    if not isinstance(policy_rows, list) or not isinstance(recipe_rows, list):
        raise ValueError("POLICIES_OR_RECIPES_INVALID")

    all_ids: set[str] = set()
    components: dict[str, dict[str, Any]] = {}
    policies: dict[str, dict[str, Any]] = {}

    for row in component_rows:
        if not isinstance(row, dict):
            raise ValueError("COMPONENT_ROW_INVALID")
        require_text(row, "id", "COMPONENT")
        component_id = row["id"]
        if component_id in all_ids:
            raise ValueError(f"REGISTRY_ID_DUPLICATE:{component_id}")
        all_ids.add(component_id)
        components[component_id] = row
        require_text(row, "type", f"COMPONENT:{component_id}")
        status = row.get("status")
        if status not in ALLOWED_COMPONENT_STATUS:
            raise ValueError(f"COMPONENT_STATUS_INVALID:{component_id}:{status}")
        dependencies = require_string_list(row, "dependencies", f"COMPONENT:{component_id}", allow_empty=True)
        if component_id in dependencies:
            raise ValueError(f"COMPONENT_SELF_DEPENDENCY:{component_id}")
        if "entry" in row:
            resolve_local(root, row["entry"], f"COMPONENT_ENTRY:{component_id}")
        if status == "verified":
            if row.get("frozen") is not True:
                raise ValueError(f"VERIFIED_COMPONENT_NOT_FROZEN:{component_id}")
            for field in ("accepted_scope", "reuse_rule", "invalidated_by"):
                require_text(row, field, f"VERIFIED_COMPONENT:{component_id}")
            require_string_list(row, "evidence", f"VERIFIED_COMPONENT:{component_id}")
            if "entry" not in row and "contract_version" not in row:
                raise ValueError(f"VERIFIED_COMPONENT_HAS_NO_ENTRY_OR_CONTRACT:{component_id}")
        artifacts = row.get("artifacts", [])
        if not isinstance(artifacts, list):
            raise ValueError(f"COMPONENT_ARTIFACTS_INVALID:{component_id}")
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                raise ValueError(f"COMPONENT_ARTIFACT_ROW_INVALID:{component_id}")
            validate_artifact(root, component_id, artifact)

    for row in policy_rows:
        if not isinstance(row, dict):
            raise ValueError("POLICY_ROW_INVALID")
        require_text(row, "id", "POLICY")
        policy_id = row["id"]
        if policy_id in all_ids:
            raise ValueError(f"REGISTRY_ID_DUPLICATE:{policy_id}")
        all_ids.add(policy_id)
        policies[policy_id] = row
        status = row.get("status")
        if status not in ALLOWED_POLICY_STATUS:
            raise ValueError(f"POLICY_STATUS_INVALID:{policy_id}:{status}")
        if "contract" in row:
            resolve_local(root, row["contract"], f"POLICY_CONTRACT:{policy_id}")
        if status == "verified":
            require_string_list(row, "evidence", f"VERIFIED_POLICY:{policy_id}")
            if "contract" not in row and "contract_version" not in row:
                raise ValueError(f"VERIFIED_POLICY_HAS_NO_CONTRACT:{policy_id}")

    for component_id, row in components.items():
        for dependency in row.get("dependencies", []):
            if dependency not in components:
                raise ValueError(f"COMPONENT_DEPENDENCY_MISSING:{component_id}:{dependency}")
            dependency_status = components[dependency]["status"]
            if dependency_status in HARD_UNAVAILABLE_DEPENDENCY_STATUS:
                raise ValueError(f"COMPONENT_DEPENDENCY_UNAVAILABLE:{component_id}:{dependency}:{dependency_status}")
            if dependency_status == "planned" and row["status"] != "planned":
                raise ValueError(f"COMPONENT_DEPENDENCY_UNAVAILABLE:{component_id}:{dependency}:{dependency_status}")
            if row["status"] == "verified" and (
                dependency_status != "verified" or components[dependency].get("frozen") is not True
            ):
                raise ValueError(f"VERIFIED_COMPONENT_DEPENDS_ON_UNVERIFIED:{component_id}:{dependency}")

    detect_cycles(components)

    for row in recipe_rows:
        if not isinstance(row, dict):
            raise ValueError("RECIPE_ROW_INVALID")
        require_text(row, "id", "RECIPE")
        recipe_id = row["id"]
        if recipe_id in all_ids:
            raise ValueError(f"REGISTRY_ID_DUPLICATE:{recipe_id}")
        all_ids.add(recipe_id)
        status = row.get("status")
        if status not in ALLOWED_RECIPE_STATUS:
            raise ValueError(f"RECIPE_STATUS_INVALID:{recipe_id}:{status}")
        component_ids = require_string_list(row, "components", f"RECIPE:{recipe_id}")
        policy_ids = require_string_list(row, "acceptance_policies", f"RECIPE:{recipe_id}", allow_empty=True)
        for component_id in component_ids:
            if component_id not in components:
                raise ValueError(f"RECIPE_COMPONENT_MISSING:{recipe_id}:{component_id}")
        for policy_id in policy_ids:
            if policy_id not in policies:
                raise ValueError(f"RECIPE_POLICY_MISSING:{recipe_id}:{policy_id}")
        if status == "verified":
            require_string_list(row, "evidence", f"VERIFIED_RECIPE:{recipe_id}")
            for component_id in component_ids:
                component = components[component_id]
                if component["status"] != "verified" or component.get("frozen") is not True:
                    raise ValueError(f"VERIFIED_RECIPE_USES_UNVERIFIED_COMPONENT:{recipe_id}:{component_id}")
            for policy_id in policy_ids:
                if policies[policy_id]["status"] != "verified":
                    raise ValueError(f"VERIFIED_RECIPE_USES_UNVERIFIED_POLICY:{recipe_id}:{policy_id}")

    return {
        "status": "PASS",
        "loop_id": data["loop_id"],
        "components": len(components),
        "verified_components": sum(1 for row in components.values() if row["status"] == "verified"),
        "policies": len(policies),
        "recipes": len(recipe_rows),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="Project root")
    parser.add_argument(
        "--registry",
        default=".project-reasoning/COMPONENTS.json",
        help="Registry path relative to project root",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        raise SystemExit(f"PROJECT_ROOT_MISSING:{root}")
    registry_path = resolve_local(root, args.registry, "COMPONENT_REGISTRY")
    try:
        result = validate(root, registry_path)
    except (ValueError, json.JSONDecodeError, UnicodeError, SyntaxError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
