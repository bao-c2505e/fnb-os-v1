#!/usr/bin/env python3
"""
Phase 20 — Repository CI & Runtime Safety Gate
FnB OS V1 / Vị Cuốn Growth OS

Validates that every .json file in the repository can be parsed without error.

SAFETY: Static analysis only. No workflows executed. No external services contacted.

Usage:   python scripts/validate_json.py
Exit:    0 = all JSON files valid, 1 = one or more files failed to parse
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Directories to skip entirely
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def find_json_files(root: Path) -> list[Path]:
    results = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune skip dirs in-place so os.walk doesn't descend into them
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in filenames:
            if filename.endswith(".json"):
                results.append(Path(dirpath) / filename)
    return sorted(results)


def validate_file(path: Path) -> tuple[bool, str]:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return False, f"Encoding error: {exc}"
    except OSError as exc:
        return False, f"Read error: {exc}"

    try:
        json.loads(content)
        return True, ""
    except json.JSONDecodeError as exc:
        return False, f"JSON parse error at line {exc.lineno}, col {exc.colno}: {exc.msg}"


def main() -> int:
    print()
    print("=" * 64)
    print("  FnB OS V1 -- Phase 20 JSON Validator")
    print("  STATIC ANALYSIS ONLY -- No workflows executed")
    print("=" * 64)
    print(f"  Root: {ROOT}")
    print()

    json_files = find_json_files(ROOT)

    if not json_files:
        print("  No .json files found in repository.")
        print()
        return 0

    print(f"  Found {len(json_files)} JSON file(s). Validating...\n")
    print("-" * 64 + " Results")

    pass_count = 0
    fail_count = 0
    failures = []

    for path in json_files:
        rel = path.relative_to(ROOT)
        ok, detail = validate_file(path)
        if ok:
            pass_count += 1
            print(f"  [PASS]  {rel}")
        else:
            fail_count += 1
            failures.append((rel, detail))
            print(f"  [FAIL]  {rel}")
            print(f"          -> {detail}")

    print()
    print("-" * 64 + " Summary")
    print(f"  Files checked : {len(json_files)}")
    print(f"  PASS          : {pass_count}")
    print(f"  FAIL          : {fail_count}")

    if fail_count == 0:
        print("  Overall       : ALL PASS")
        print()
        print("  NOTE: Static parse validation only.")
        print("        No workflows executed. No external services contacted.")
        print()
        return 0
    else:
        print("  Overall       : FAILURES FOUND -- review details above")
        print()
        print("  Failed files:")
        for rel, detail in failures:
            print(f"    - {rel}: {detail}")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
