#!/usr/bin/env python3
"""
Phase 20 — Repository CI & Runtime Safety Gate
FnB OS V1 / Vị Cuốn Growth OS

Scans all text files in the repository for patterns that indicate hardcoded
API keys, tokens, or passwords.

POLICY:
- REPLACE_WITH_* placeholder strings are explicitly ALLOWED — they are stubs.
- This script detects actual credential values, not placeholder markers.
- Binary files are skipped automatically.

SAFETY: Static analysis only. No external services contacted. No credentials
        are written or transmitted.

Usage:   python scripts/check_no_secrets.py
Exit:    0 = no secrets found, 1 = potential secrets detected
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

# Directories to skip
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}

# File extensions that are unlikely to contain secrets as text
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".woff", ".woff2",
    ".ttf", ".eot", ".otf", ".mp4", ".mp3", ".wav", ".pdf", ".zip",
    ".tar", ".gz", ".bz2", ".7z", ".bin", ".exe", ".dll", ".so",
    ".pyc", ".pyo",
}

# Secret patterns — each entry: (label, compiled_regex)
# These patterns match real credential formats.
# REPLACE_WITH_* placeholders will not match because they lack the required
# character sequences and lengths.
SECRET_PATTERNS = [
    (
        "Anthropic API key (sk-ant-api)",
        re.compile(r"sk-ant-api\d{2}-[A-Za-z0-9\-_]{90,}"),
    ),
    (
        "OpenAI API key (sk-... 48+ chars)",
        re.compile(r"\bsk-[A-Za-z0-9]{48,}\b"),
    ),
    (
        "GitHub Personal Access Token (ghp_)",
        re.compile(r"ghp_[A-Za-z0-9]{36}"),
    ),
    (
        "GitHub Fine-grained PAT (github_pat_)",
        re.compile(r"github_pat_[A-Za-z0-9_]{82}"),
    ),
    (
        "AWS Access Key ID (AKIA...)",
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ),
    (
        "PEM private key block",
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ),
    (
        "JWT token (eyJhbGciO...)",
        re.compile(
            r"eyJhbGciOiJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+"
        ),
    ),
    (
        "Telegram bot token (digits:chars)",
        re.compile(r"\b[0-9]{9,10}:[A-Za-z0-9_\-]{35}\b"),
    ),
    (
        "Google service account private key",
        re.compile(r'"private_key"\s*:\s*"-----BEGIN'),
    ),
    (
        "Slack bot/user OAuth token (xox[bprs]-)",
        re.compile(r"xox[bprs]-[0-9A-Za-z\-]{10,}"),
    ),
    (
        "Meta/Facebook access token (EAAG/EAA pattern 80+ chars)",
        re.compile(r"EAA[A-Za-z0-9]{80,}"),
    ),
]


def is_binary(path: Path) -> bool:
    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True
    try:
        chunk = path.read_bytes()[:8192]
        # Presence of null bytes strongly indicates binary content
        return b"\x00" in chunk
    except OSError:
        return True


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    """Return list of (line_number, label, matched_text) for each hit."""
    if is_binary(path):
        return []
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    hits = []
    for lineno, line in enumerate(content.splitlines(), start=1):
        for label, pattern in SECRET_PATTERNS:
            match = pattern.search(line)
            if match:
                # Truncate the matched value so logs don't echo real credentials
                matched = match.group(0)
                safe_preview = matched[:8] + "..." if len(matched) > 8 else matched
                hits.append((lineno, label, safe_preview))
    return hits


def main() -> int:
    print()
    print("=" * 64)
    print("  FnB OS V1 -- Phase 20 Secret Scanner")
    print("  STATIC ANALYSIS ONLY -- No external services contacted")
    print("=" * 64)
    print(f"  Root         : {ROOT}")
    print(f"  Patterns     : {len(SECRET_PATTERNS)}")
    print(f"  Policy       : REPLACE_WITH_* placeholders are ALLOWED")
    print()

    total_files = 0
    total_hits = 0
    findings: list[tuple[Path, list[tuple[int, str, str]]]] = []

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for filename in sorted(filenames):
            path = Path(dirpath) / filename
            hits = scan_file(path)
            total_files += 1
            if hits:
                total_hits += len(hits)
                findings.append((path, hits))

    print("-" * 64 + " Results")

    if not findings:
        print("  [CLEAN] No secret patterns detected.")
        print()
    else:
        for path, hits in findings:
            rel = path.relative_to(ROOT)
            print(f"  [HIT]   {rel}")
            for lineno, label, preview in hits:
                print(f"          -> line {lineno}: {label}  [{preview}]")
        print()

    print("-" * 64 + " Summary")
    print(f"  Files scanned  : {total_files}")
    print(f"  Patterns used  : {len(SECRET_PATTERNS)}")
    print(f"  Findings       : {total_hits}")

    if total_hits == 0:
        print("  Result         : CLEAN -- safe for commit")
        print()
        print("  NOTE: REPLACE_WITH_* placeholders were not flagged (policy).")
        print("        Static scan only -- no external services contacted.")
        print()
        return 0
    else:
        print("  Result         : SECRETS DETECTED — review and remove before commit")
        print()
        print("  ACTION REQUIRED:")
        print("    Remove or replace each detected value with a REPLACE_WITH_* placeholder.")
        print("    Do NOT commit real credentials to this repository.")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
