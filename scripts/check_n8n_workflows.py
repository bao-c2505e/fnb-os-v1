#!/usr/bin/env python3
"""
Phase 20 — Repository CI & Runtime Safety Gate
FnB OS V1 / Vị Cuốn Growth OS

Checks every n8n workflow JSON file in n8n/workflows/ to ensure that
the `active` field is NOT set to true.

RULE: All workflow skeleton files MUST have active=false (or active absent).
      active=true would allow n8n to execute the workflow automatically,
      which is forbidden for all skeleton files in this repository.

SAFETY: Static analysis only. No workflows executed. No n8n instance contacted.
        No credentials read or modified.

Usage:   python scripts/check_n8n_workflows.py
Exit:    0 = all workflows safe (active != true), 1 = active=true detected
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WORKFLOW_DIR = ROOT / "n8n" / "workflows"


def check_workflow(path: Path) -> tuple[bool, str]:
    """
    Returns (safe, detail).
    safe=True means the file does NOT have active=true.
    """
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return False, f"Read error: {exc}"

    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        return False, f"JSON parse error at line {exc.lineno}: {exc.msg}"

    active_value = data.get("active")

    if active_value is True:
        return False, f"FAIL — active=true detected. Workflow would auto-execute in n8n."

    if active_value is False:
        detail = "active=false (correct)"
    elif active_value is None:
        detail = "active field absent (safe — n8n defaults to inactive)"
    else:
        detail = f"active={json.dumps(active_value)} (non-boolean — safe, but review)"

    # Additional check: name should contain [SKELETON] as a safety label
    name = data.get("name", "")
    if name and "[SKELETON]" not in name:
        detail += f" | WARNING: name '{name}' does not contain [SKELETON]"

    return True, detail


def main() -> int:
    print()
    print("=" * 64)
    print("  FnB OS V1 -- Phase 20 n8n Workflow Safety Check")
    print("  STATIC ANALYSIS ONLY -- No n8n instance contacted")
    print("=" * 64)
    print(f"  Workflow dir : {WORKFLOW_DIR}")
    print()

    if not WORKFLOW_DIR.exists():
        print(f"  WARNING: Workflow directory not found: {WORKFLOW_DIR}")
        print("  No workflow files to check.")
        print()
        print("─── Summary ─────────────────────────────────────────────────────")
        print("  Files checked : 0")
        print("  Result        : PASS (no workflow directory — nothing to fail)")
        print()
        return 0

    workflow_files = sorted(WORKFLOW_DIR.glob("*.json"))

    if not workflow_files:
        print("  No .json files found in n8n/workflows/.")
        print()
        print("─── Summary ─────────────────────────────────────────────────────")
        print("  Files checked : 0")
        print("  Result        : PASS (no workflow files — nothing to fail)")
        print()
        return 0

    print(f"  Found {len(workflow_files)} workflow file(s). Checking active field...\n")
    print("-" * 64 + " Results")

    pass_count = 0
    fail_count = 0
    failures = []

    for path in workflow_files:
        rel = path.relative_to(ROOT)
        safe, detail = check_workflow(path)
        if safe:
            pass_count += 1
            print(f"  [PASS]  {rel}")
            print(f"          -> {detail}")
        else:
            fail_count += 1
            failures.append((rel, detail))
            print(f"  [FAIL]  {rel}")
            print(f"          -> {detail}")

    print()
    print("-" * 64 + " Summary")
    print(f"  Files checked : {len(workflow_files)}")
    print(f"  PASS          : {pass_count}")
    print(f"  FAIL          : {fail_count}")

    if fail_count == 0:
        print("  Result        : ALL PASS -- no active=true detected")
        print()
        print("  NOTE: All skeleton workflows confirmed inactive.")
        print("        Static check only -- no n8n instance contacted.")
        print()
        return 0
    else:
        print("  Result        : ACTIVE WORKFLOWS DETECTED — MUST FIX BEFORE COMMIT")
        print()
        print("  CRITICAL: The following workflows have active=true:")
        for rel, detail in failures:
            print(f"    - {rel}: {detail}")
        print()
        print("  ACTION REQUIRED:")
        print('    Set "active": false in each listed workflow file.')
        print("    Never commit a workflow with active=true to this repository.")
        print("    Activating workflows must only be done in n8n with Owner approval.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
