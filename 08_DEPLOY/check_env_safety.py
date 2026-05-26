"""
check_env_safety.py — FnB OS V1 environment safety checker.

Checks that the environment is configured safely before any workflow runs.
Never prints secret values — only variable names and PASS/WARN/FAIL status.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_FILE = os.path.join(ROOT, ".env")
EXAMPLE_FILE = os.path.join(ROOT, ".env.example")
GITIGNORE_FILE = os.path.join(ROOT, ".gitignore")
CLAUDE_ENV_FILE = os.path.join(ROOT, ".claude", ".env")

REQUIRED_VARS = [
    "PROJECT_NAME",
    "DEFAULT_BRAND",
    "ENVIRONMENT",
    "OPENAI_API_KEY",
    "OPENAI_DEFAULT_MODEL",
    "GEMINI_API_KEY",
    "GEMINI_MODEL",
    "GOOGLE_DRIVE_ROOT_FOLDER_ID",
    "GOOGLE_SHEET_CONTROL_CENTER_ID",
    "TELEGRAM_BOT_TOKEN",
    "TELEGRAM_CHAT_ID",
    "N8N_BASE_URL",
    "N8N_API_KEY",
    "GITHUB_TOKEN",
    "AUTO_PUBLISH_ENABLED",
    "HUMAN_APPROVAL_REQUIRED",
]

PLACEHOLDER_MARKERS = [
    "PASTE_YOUR_",
    "YOUR_",
    "FILL_",
    "<",
    "TODO",
]

PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


def status_line(label, result, detail=""):
    icon = {"PASS": "[+]", "WARN": "[!]", "FAIL": "[X]"}.get(result, "   ")
    line = f"  {icon} {result:<4}  {label}"
    if detail:
        line += f"  ({detail})"
    print(line)
    return result


def load_env_vars(filepath):
    """Parse key=value pairs from a .env file without using python-dotenv."""
    pairs = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, val = line.partition("=")
                pairs[key.strip()] = val.strip()
    return pairs


def is_placeholder(val):
    return any(marker in val for marker in PLACEHOLDER_MARKERS) or val == ""


def check_gitignore_blocks_env(gitignore_path):
    """Return True if .gitignore has a line that would block .env."""
    with open(gitignore_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines()]
    return ".env" in lines or ".env.*" in lines


def main():
    results = []
    print()
    print("=" * 60)
    print("  FnB OS V1 — Environment Safety Check")
    print("=" * 60)
    print()

    # 1. Root .env exists
    print("[ File Checks ]")
    if os.path.isfile(ENV_FILE):
        results.append(status_line("Root .env exists", PASS))
    else:
        results.append(status_line("Root .env exists", FAIL, "create from .env.example"))

    # 2. .env.example exists
    if os.path.isfile(EXAMPLE_FILE):
        results.append(status_line(".env.example exists", PASS))
    else:
        results.append(status_line(".env.example exists", FAIL, "missing from repo"))

    # 3. .gitignore exists
    if os.path.isfile(GITIGNORE_FILE):
        results.append(status_line(".gitignore exists", PASS))
    else:
        results.append(status_line(".gitignore exists", FAIL, "repo has no .gitignore"))

    # 4. .gitignore blocks .env
    if os.path.isfile(GITIGNORE_FILE):
        if check_gitignore_blocks_env(GITIGNORE_FILE):
            results.append(status_line(".env ignored by Git", PASS))
        else:
            results.append(status_line(".env ignored by Git", FAIL, "add .env to .gitignore NOW"))
    else:
        results.append(status_line(".env ignored by Git", FAIL, "no .gitignore found"))

    # 5. .claude/.env check — warn if exists, DO NOT read values
    print()
    print("[ Security Checks ]")
    if os.path.isfile(CLAUDE_ENV_FILE):
        results.append(status_line(
            ".claude/.env detected",
            WARN,
            "SECURITY RISK — delete this file, secrets belong only in root .env"
        ))
    else:
        results.append(status_line(".claude/.env not present", PASS, "good"))

    # 6. Variable presence and placeholder check (no values printed)
    if os.path.isfile(ENV_FILE):
        print()
        print("[ Variable Checks — names only, no values printed ]")
        env_vars = load_env_vars(ENV_FILE)

        filled = []
        still_placeholder = []
        missing = []

        for var in REQUIRED_VARS:
            if var not in env_vars:
                missing.append(var)
            elif is_placeholder(env_vars[var]):
                still_placeholder.append(var)
            else:
                filled.append(var)

        # AUTO_PUBLISH_ENABLED must be false
        auto_publish = env_vars.get("AUTO_PUBLISH_ENABLED", "").lower()
        if auto_publish == "false":
            results.append(status_line("AUTO_PUBLISH_ENABLED=false", PASS))
        elif auto_publish == "true":
            results.append(status_line("AUTO_PUBLISH_ENABLED", FAIL, "must be false — auto-publish is DISABLED in Phase 0"))
        else:
            results.append(status_line("AUTO_PUBLISH_ENABLED", WARN, f"unexpected value, expected 'false'"))

        # HUMAN_APPROVAL_REQUIRED must be true
        human_approval = env_vars.get("HUMAN_APPROVAL_REQUIRED", "").lower()
        if human_approval == "true":
            results.append(status_line("HUMAN_APPROVAL_REQUIRED=true", PASS))
        elif human_approval == "false":
            results.append(status_line("HUMAN_APPROVAL_REQUIRED", FAIL, "must be true — human approval cannot be bypassed"))
        else:
            results.append(status_line("HUMAN_APPROVAL_REQUIRED", WARN, f"unexpected value, expected 'true'"))

        print()
        print("  Variable fill status:")
        for var in REQUIRED_VARS:
            if var in missing:
                status_line(var, FAIL, "missing from .env")
            elif var in still_placeholder:
                status_line(var, WARN, "still placeholder — fill before Phase 1")
            else:
                status_line(var, PASS, "filled")

    # Summary
    print()
    print("=" * 60)
    fail_count = sum(1 for r in results if r == FAIL)
    warn_count = sum(1 for r in results if r == WARN)
    pass_count = sum(1 for r in results if r == PASS)

    print(f"  Summary: {pass_count} PASS  |  {warn_count} WARN  |  {fail_count} FAIL")

    if fail_count > 0:
        print()
        print("  [X] FAILED -- fix all FAIL items before proceeding to Phase 1.")
        sys.exit(1)
    elif warn_count > 0:
        print()
        print("  [!] WARNINGS present -- fill placeholder values before Phase 1.")
        sys.exit(0)
    else:
        print()
        print("  [+] All checks passed. Ready for Phase 1 after filling real values.")
        sys.exit(0)


if __name__ == "__main__":
    main()
