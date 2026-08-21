from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("validate_component_registry.py")
SPEC = importlib.util.spec_from_file_location("validate_component_registry", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


class ComponentRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "artifact.txt").write_bytes(b"accepted\n")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_registry(self, data: dict) -> Path:
        path = self.root / "COMPONENTS.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def base_registry(self) -> dict:
        return {
            "schema_version": 1,
            "status": "active",
            "loop_id": "test-loop",
            "components": [
                {
                    "id": "COMP-V1",
                    "type": "test",
                    "status": "verified",
                    "frozen": True,
                    "entry": "artifact.txt",
                    "dependencies": [],
                    "accepted_scope": "accepted bytes",
                    "reuse_rule": "reuse unchanged",
                    "invalidated_by": "fingerprint drift",
                    "evidence": ["TEST-EVIDENCE"],
                    "artifacts": [
                        {
                            "kind": "file",
                            "path": "artifact.txt",
                            "sha256": digest(b"accepted\n"),
                        }
                    ],
                }
            ],
            "acceptance_policies": [
                {
                    "id": "POLICY-V1",
                    "status": "verified",
                    "contract_version": "v1",
                    "evidence": ["TEST-POLICY"],
                }
            ],
            "recipes": [
                {
                    "id": "RECIPE-V1",
                    "status": "verified",
                    "components": ["COMP-V1"],
                    "acceptance_policies": ["POLICY-V1"],
                    "evidence": ["TEST-RECIPE"],
                }
            ],
        }

    def test_verified_recipe_passes(self) -> None:
        result = MODULE.validate(self.root, self.write_registry(self.base_registry()))
        self.assertEqual(result["status"], "PASS")

    def test_fingerprint_drift_blocks_reuse(self) -> None:
        registry = self.write_registry(self.base_registry())
        (self.root / "artifact.txt").write_bytes(b"changed\n")
        with self.assertRaisesRegex(ValueError, "ARTIFACT_FINGERPRINT_MISMATCH"):
            MODULE.validate(self.root, registry)

    def test_verified_recipe_rejects_validation_only_component(self) -> None:
        data = self.base_registry()
        data["components"][0]["status"] = "validation_only"
        data["components"][0]["frozen"] = False
        with self.assertRaisesRegex(ValueError, "VERIFIED_RECIPE_USES_UNVERIFIED_COMPONENT"):
            MODULE.validate(self.root, self.write_registry(data))

    def test_planned_chain_may_describe_future_composition(self) -> None:
        data = self.base_registry()
        data["components"] = [
            {
                "id": "PLAN-A",
                "type": "test",
                "status": "planned",
                "frozen": False,
                "dependencies": [],
                "artifacts": [],
            },
            {
                "id": "PLAN-B",
                "type": "test",
                "status": "planned",
                "frozen": False,
                "dependencies": ["PLAN-A"],
                "artifacts": [],
            },
        ]
        data["acceptance_policies"] = []
        data["recipes"] = [
            {
                "id": "PLAN-RECIPE",
                "status": "planned",
                "components": ["PLAN-A", "PLAN-B"],
                "acceptance_policies": [],
            }
        ]
        result = MODULE.validate(self.root, self.write_registry(data))
        self.assertEqual(result["verified_components"], 0)


if __name__ == "__main__":
    unittest.main()
