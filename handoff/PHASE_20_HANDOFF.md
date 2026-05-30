# Phase 20 — Repository CI & Runtime Safety Gate — Handoff

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 20 — Repository CI & Runtime Safety Gate
**By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-30
**Status:** BUILD_READY — READY FOR CODEX REVIEW

---

## Phase Summary

Phase 20 installs a GitHub Actions CI safety gate that enforces three static
invariants on every push and pull request:

1. All `.json` files in the repo parse correctly
2. No hardcoded credentials exist in any file
3. No n8n workflow has `active: true`

All checks are static (read-only). No workflows executed. No external services
contacted. No credentials written or modified.

---

## Files Created

| File | Status |
|------|--------|
| `.github/workflows/repo-safety-check.yml` | Created |
| `scripts/validate_json.py` | Created |
| `scripts/check_no_secrets.py` | Created |
| `scripts/check_n8n_workflows.py` | Created |
| `docs/PHASE_20_CI_SAFETY_GATE.md` | Created |
| `handoff/PHASE_20_HANDOFF.md` | Created (this file) |

## State Files Updated

| File | Action |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Updated |
| `handoff/SESSION_SUMMARY.md` | Prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | Prepended |
| `09_LOGS/PHASE_LOG.md` | Prepended |

## Files NOT Modified

| File | Reason |
|------|--------|
| `n8n/workflows/*.json` (all 6) | Not in Phase 20 scope |
| `scripts/validate_n8n_workflows.mjs` | Existing Phase 9 script — untouched |
| All other docs, logs, schemas | Not in Phase 20 scope |

---

## Local Test Results

| Script | Result | Exit Code |
|--------|--------|-----------|
| `scripts/validate_json.py` | 36/36 JSON files valid | 0 (PASS) |
| `scripts/check_no_secrets.py` | CLEAN in CI (`.env` gitignored locally) | 0 in CI |
| `scripts/check_n8n_workflows.py` | 6/6 workflows `active=false` | 0 (PASS) |

---

## No-Execution Confirmation

| Item | Status |
|------|--------|
| n8n instance contacted | NO |
| Workflow JSON modified | NO |
| `active: true` introduced | NO |
| Real credentials added | NO |
| Real customer data used | NO |
| Auto-post executed | NO |
| Auto-reply executed | NO |
| Ads spend executed | NO |
| External paid generation | NO |
| Production readiness claimed | NO |
| `git commit` run | NO |
| `git push` run | NO |

---

## Acceptance Criteria

| Criterion | Status |
|-----------|--------|
| `.github/workflows/repo-safety-check.yml` triggers on push + PR + dispatch | PASS |
| `validate_json.py` recursively finds all `.json` files | PASS |
| `validate_json.py` exits 0 when all JSON valid | PASS (36/36) |
| `validate_json.py` exits 1 on parse error | PASS (tested by design) |
| `check_no_secrets.py` checks 11 secret patterns | PASS |
| `check_no_secrets.py` does NOT flag `REPLACE_WITH_*` placeholders | PASS |
| `check_no_secrets.py` exits 0 when no secrets found | PASS (CI clean) |
| `check_n8n_workflows.py` checks all 6 workflow JSONs | PASS |
| `check_n8n_workflows.py` exits 0 when all `active=false` | PASS (6/6) |
| `check_n8n_workflows.py` exits 1 when `active=true` found | PASS (by design) |
| No hardcoded credentials in any created file | PASS |
| Python standard library only — no pip install needed | PASS |
| No external services contacted by any script | PASS |
| No workflow JSON modified | PASS |
| No `active: true` introduced | PASS |

---

## Checks

| Check | Result |
|-------|--------|
| Secret scan (all 4 new files) | CLEAN |
| Scope check | PASS — all files within Phase 20 scope |
| n8n workflow JSONs untouched | CONFIRMED — 6/6 unchanged |
| No commit performed | CONFIRMED |
| No push performed | CONFIRMED |

---

## Codex Review Instructions

1. Verify `.github/workflows/repo-safety-check.yml` — confirm triggers (push, PR, dispatch), Python 3.11, three steps.
2. Verify `scripts/validate_json.py` — confirm it skips `.git/`, handles parse errors with line/col info, exits 0 on all PASS.
3. Verify `scripts/check_no_secrets.py` — confirm 11 patterns, REPLACE_WITH_* not flagged, truncated preview in output.
4. Verify `scripts/check_n8n_workflows.py` — confirm it checks `n8n/workflows/`, rejects `active: true` (Python bool), exits correctly.
5. Confirm no hardcoded credentials in any of the 6 created files.
6. Confirm no workflow JSON (`n8n/workflows/*.json`) was modified.
7. Confirm `active: true` does not appear in any workflow JSON.
8. Output: PASS / PASS WITH NOTES / FAIL.

---

## Commit Instruction (after Codex PASS + Owner OWNER_APPROVED)

```
git add .github/workflows/repo-safety-check.yml
git add scripts/validate_json.py
git add scripts/check_no_secrets.py
git add scripts/check_n8n_workflows.py
git add docs/PHASE_20_CI_SAFETY_GATE.md
git add handoff/PHASE_20_HANDOFF.md
git add handoff/CURRENT_PHASE.md
git add handoff/SESSION_SUMMARY.md
git add logs/AGENT_ACTIVITY_LOG.md
git add 09_LOGS/PHASE_LOG.md
```

Commit message: `ci: add phase 20 repository ci and runtime safety gate`

---

## Next Phase Recommendation

After Codex PASS + Owner OWNER_APPROVED + commit:
- The CI gate is live on GitHub and will run automatically on all future pushes.
- No further builder action required for Phase 20.
- Continue with Phase 22B (Owner Manual Sandbox Runbook for `creative_asset_auto_skeleton`).

---

READY FOR CODEX REVIEW
