# Phase 20 — Repository CI & Runtime Safety Gate

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 20 — Repository CI & Runtime Safety Gate
**By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-30
**Status:** BUILD_READY — READY FOR CODEX REVIEW

---

## Section A — Purpose

Phase 20 installs a GitHub Actions CI workflow that runs three static safety
checks on every push and pull request. No workflows are executed. No external
services are contacted. No credentials are written or read.

This gate enforces three repo-level safety invariants automatically:

| Invariant | Enforced By |
|-----------|-------------|
| All JSON files in the repo are valid (parseable) | `scripts/validate_json.py` |
| No hardcoded API keys, tokens, or passwords exist | `scripts/check_no_secrets.py` |
| No n8n workflow has `active: true` | `scripts/check_n8n_workflows.py` |

---

## Section B — Files Created

| File | Role |
|------|------|
| `.github/workflows/repo-safety-check.yml` | GitHub Actions workflow — triggers all three checks |
| `scripts/validate_json.py` | Recursively validates every `.json` file in the repo |
| `scripts/check_no_secrets.py` | Scans all text files for secret credential patterns |
| `scripts/check_n8n_workflows.py` | Checks all n8n workflow JSONs for `active: true` |
| `docs/PHASE_20_CI_SAFETY_GATE.md` | This document |
| `handoff/PHASE_20_HANDOFF.md` | Phase 20 handoff for Codex review |

---

## Section C — GitHub Actions Workflow

**File:** `.github/workflows/repo-safety-check.yml`

**Triggers:**
- `push` — any branch
- `pull_request` — any branch
- `workflow_dispatch` — manual trigger from GitHub UI

**Runner:** `ubuntu-latest`

**Python version:** 3.11

**Steps:**
1. Checkout repository (`actions/checkout@v4`)
2. Set up Python 3.11 (`actions/setup-python@v5`)
3. Run `python scripts/validate_json.py`
4. Run `python scripts/check_no_secrets.py`
5. Run `python scripts/check_n8n_workflows.py`

All steps are independent. If any step exits with code 1, the CI job fails
and GitHub blocks the merge (when branch protection rules are enabled).

**No secrets, tokens, or environment variables are required by the workflow.**

---

## Section D — Script: validate_json.py

**Purpose:** Validate that every `.json` file in the repository can be parsed
without error. A malformed JSON file could indicate a corrupted schema,
broken workflow export, or accidental edit.

**Behavior:**
- Recursively walks the repository from the root
- Skips `.git`, `node_modules`, `__pycache__`, `.venv`, `venv`
- Attempts `json.loads()` on each `.json` file
- Reports PASS or FAIL per file with line/column information on parse errors
- Exits 0 if all files valid; exits 1 if any file fails

**Local test result (2026-05-30):**
- Files checked: 36
- PASS: 36 / FAIL: 0
- Exit code: 0

---

## Section E — Script: check_no_secrets.py

**Purpose:** Scan all text files for patterns that indicate hardcoded credentials.
Catches accidental commits of API keys, tokens, or passwords before they
reach the remote repository.

**Policy:** `REPLACE_WITH_*` placeholder strings are explicitly allowed.
They are stubs, not real credentials. The patterns only match actual
credential format lengths and character sets.

**Patterns checked (11 total):**

| Pattern | Detects |
|---------|---------|
| `sk-ant-api\d{2}-...{90,}` | Anthropic API key |
| `sk-[A-Za-z0-9]{48,}` | OpenAI API key |
| `ghp_[A-Za-z0-9]{36}` | GitHub Personal Access Token |
| `github_pat_[A-Za-z0-9_]{82}` | GitHub Fine-grained PAT |
| `AKIA[0-9A-Z]{16}` | AWS Access Key ID |
| `-----BEGIN.*PRIVATE KEY-----` | PEM private key block |
| `eyJhbGciOiJ...` (JWT format) | JSON Web Token |
| `[0-9]{9,10}:[A-Za-z0-9_-]{35}` | Telegram bot token |
| `"private_key": "-----BEGIN` | Google service account key |
| `xox[bprs]-...` | Slack OAuth token |
| `EAA[A-Za-z0-9]{80,}` | Meta/Facebook access token |

**Skipped:** Binary files, `.git/`, `node_modules/`, image/font/archive extensions.

**Matched value handling:** When a hit is found, only the first 8 characters
of the matched value are shown in the report (truncated with `...`) so that
logs do not echo real credentials.

**Local test result (2026-05-30):**
- Files scanned: 304
- Findings: 2 (both in `.env` — gitignored, not committed)
- `.env` is listed in `.gitignore` and will not be present in CI
- **CI result on GitHub will be: CLEAN / exit 0**

---

## Section F — Script: check_n8n_workflows.py

**Purpose:** Verify that no n8n workflow JSON file in `n8n/workflows/` has
`"active": true`. An active workflow auto-executes in n8n. This invariant
must never be violated for skeleton files.

**Behavior:**
- Reads every `.json` file in `n8n/workflows/`
- Parses the JSON and checks the `active` field
- PASS if `active` is `false`, absent, or any non-`true` value
- FAIL if `active` is exactly `true` (Python boolean `True`)
- Additional advisory warning if workflow name does not contain `[SKELETON]`
- Exits 0 if all workflows safe; exits 1 if any have `active: true`

**Local test result (2026-05-30):**
- Files checked: 6
- PASS: 6 / FAIL: 0
- All 6 workflows confirmed `active=false`
- Exit code: 0

---

## Section G — Safety Confirmations

| Check | Status |
|-------|--------|
| Workflow JSON modified | NO |
| `active: true` introduced | NO |
| Real credentials added | NO |
| Real customer data | NO |
| Workflow execution performed | NO |
| Auto-post | NO |
| Auto-reply | NO |
| Ads spend | NO |
| External paid generation | NO |
| Production readiness claimed | NO |
| Secret scan (scripts themselves) | CLEAN |
| n8n instance contacted | NO |

---

## Section H — Local Test Results Summary

| Script | Files Checked | PASS | FAIL | Exit Code | CI Expectation |
|--------|--------------|------|------|-----------|----------------|
| validate_json.py | 36 JSON files | 36 | 0 | 0 | PASS |
| check_no_secrets.py | 304 files | — | .env (gitignored) | 1 locally | PASS (0) in CI |
| check_n8n_workflows.py | 6 n8n workflows | 6 | 0 | 0 | PASS |

**Note on check_no_secrets.py local result:**
The `.env` file on the local machine contains real Telegram/JWT tokens for
development use. This file is listed in `.gitignore` (lines 2–4) and is
never committed to the repository. GitHub Actions runs on a clean checkout
that does not include `.env`. The CI check will pass with exit 0.

---

## Section I — Explicit Non-Goals

| Non-Goal | Reason |
|----------|--------|
| Does not execute n8n workflows | Static check only |
| Does not connect to any external API | No credentials needed |
| Does not modify any existing JSON | Read-only |
| Does not claim production readiness | Repo safety gate only |
| Does not replace Phase 14/16/17 sandbox execution | Separate process |
| Does not activate any workflow | Activation is Owner-only in n8n |
| Does not auto-commit or auto-push | No commit/push in CI |
| Does not scan for logic errors in workflow JSON | Structural check only |

---

## Section J — Phase Connections

| Phase | Result |
|-------|--------|
| Phase 8 — n8n Workflow Skeletons | DONE (`ad867b3`) |
| Phase 9 — n8n Import Validation Pack | DONE (`56ed0c3`) |
| Phase 14 — Sandbox Import Dry-Run | PASS (`86099bb`) |
| Phase 16 — Sandbox Runtime Validation Plan | DONE (`82a3ce3`) |
| Phase 17 — Sandbox Test Data + Evidence Pack | DONE (`ac91976`) |
| Phase 19 — Owner Manual Sandbox Execution Instructions | DONE (`f04edba`) |
| Phase 20A — Manual Sandbox Evidence Capture Pack | DONE (`f505dae`) |
| Phase 20B — Owner Manual Sandbox Runbook | DONE (`fb33e8c`) |
| Phase 20C — Owner Evidence Submission | PASS (`50df2af`) |
| Phase 21 — Sandbox Manual Execution Expansion Plan | DONE (`07ef58b`) |
| Phase 22A — Creative Asset Sandbox Evidence Pack | PACK_READY |
| **Phase 20 CI — Repository CI & Runtime Safety Gate** | **BUILD_READY** |

---

## Section K — Codex Review Checklist

| Item | Verify |
|------|--------|
| CR-01 | `.github/workflows/repo-safety-check.yml` triggers on push + PR + dispatch |
| CR-02 | `validate_json.py` recursively finds all `.json`, exits 0 on all PASS |
| CR-03 | `check_no_secrets.py` has 11 patterns, REPLACE_WITH_* not flagged |
| CR-04 | `check_n8n_workflows.py` checks `active` field, exits 1 on `active: true` |
| CR-05 | No hardcoded credentials in any of the 4 new files |
| CR-06 | No `active: true` introduced in any n8n workflow JSON |
| CR-07 | No external services contacted by any script |
| CR-08 | All scripts exit with correct codes (0 = pass, 1 = fail) |
| CR-09 | Python standard library only — no pip installs required |
| CR-10 | No workflow JSON modified |
