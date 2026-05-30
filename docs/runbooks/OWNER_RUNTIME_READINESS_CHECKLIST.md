# Owner Runtime Readiness Checklist — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness)
Type: Owner-Facing Checklist
Audience: Owner (Bo Bao) — not for agents

---

## Purpose

This checklist must be completed before any runtime action (sandbox import, sandbox execution, or production runtime). It ensures the repository and environment are in a verified, safe state before proceeding.

**This checklist does not authorize any runtime action.** Authorization requires the Owner to explicitly write an approval phrase (see Section G below).

---

## A — Repo State Checks

Run these commands before any runtime action:

| Check | Command | Required Result |
|-------|---------|----------------|
| Branch is main | `git branch --show-current` | `main` |
| Working tree is clean | `git status --short` | No output (clean) |
| HEAD equals origin/main | `git log -1 --oneline` and compare to GitHub | Hashes match |
| No uncommitted changes | `git diff --stat` | No output |

**If any check fails:** Stop. Do not proceed. Contact Builder to resolve.

---

## B — Latest Phase Handoff Exists

| Check | Location | Required |
|-------|---------|---------|
| Latest phase handoff file exists | `handoff/PHASE_[XX]_HANDOFF.md` | YES |
| Handoff confirms no workflow JSON modified | Handoff file — "Files NOT Modified" section | YES |
| Handoff confirms no secrets added | Handoff file — validation table | YES |
| Handoff confirms no `"active": true` introduced | Handoff file — validation table | YES |

---

## C — Codex PASS or Owner Direct Review Exists for Previous Phase

| Check | Where to Find | Required |
|-------|--------------|---------|
| Previous phase has Codex PASS or Owner direct review | Phase handoff + PHASE_LOG.md | YES |
| PASS is for the specific phase being acted upon or prior phase | Phase handoff | YES |
| No BLOCK or outstanding REVIEW_FAIL on relevant files | Phase handoff | YES |

---

## D — No Secrets in Repo

| Check | Method | Required Result |
|-------|--------|----------------|
| CI secret scan passing | GitHub Actions tab — `repo-safety-check.yml` | All checks PASS |
| No API keys in new files | Manual review or `scripts/check_no_secrets.py` | CLEAN |
| No `.env` committed | `git status` | `.env` not listed |
| All credentials are `REPLACE_WITH_*` placeholders | Review workflow JSON files | YES |

---

## E — Workflow JSON Safety Checks

| Check | Method | Required Result |
|-------|--------|----------------|
| All workflow JSON files have `"active": false` | `scripts/check_n8n_workflows.py` or manual check | All `active: false` |
| No `"active": true` anywhere in repo | `scripts/check_n8n_workflows.py` | 0 violations |
| All workflow JSON files are valid JSON | `scripts/validate_json.py` | All PASS |
| Workflow JSON files are importable (Phase 14 PASS) | `logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md` | PASS recorded |

---

## F — Approval Gate Documentation Check

| Check | Where to Find | Required |
|-------|--------------|---------|
| Approval gate document exists | `docs/governance/OWNER_APPROVAL_GATE.md` | YES |
| Relevant gate for this action is defined (Gate 5 for import, Gate 6 for execution) | `docs/governance/OWNER_APPROVAL_GATE.md` | YES |
| Per-workflow runbook or evidence pack exists for this workflow | `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` | YES |

---

## G — Sandbox / Test Data Confirmation

| Check | Required |
|-------|---------|
| Test data is dummy/sandbox — not real customer data | YES |
| No real customer names, phones, emails, or IDs will be used | YES |
| No real Zalo/Facebook/Instagram/TikTok credentials will be configured | YES |
| No real OpenAI / image generation API key will be used for the test | YES |
| No real Google Sheets or Drive will receive test output | YES |
| n8n instance is confirmed as sandbox/test — NOT production | YES |

---

## H — Output Safety Confirmation

| Check | Required |
|-------|---------|
| No real customer messages will be sent during this test | YES |
| No social media posts will be published during this test | YES |
| No ad campaign or budget will be committed during this test | YES |
| No comment replies will be posted during this test | YES |
| All publish/send/reply nodes are NoOp stubs in the workflow | YES |

---

## I — Rollback and Fallback Note

| Check | Required |
|-------|---------|
| Rollback procedure exists (`docs/governance/OWNER_APPROVAL_GATE.md` Gate 10) | YES |
| Owner knows which git commit to roll back to if needed | YES — record here: `__________________________` |
| Fallback: stop n8n execution panel immediately if unexpected behavior occurs | YES |

---

## J — Evidence Capture Plan

| Check | Required |
|-------|---------|
| Evidence log template exists for this workflow | YES — confirm path: `__________________________` |
| Screenshot naming convention is documented in the runbook | YES |
| Evidence folder exists (or Owner will create it) | YES |
| Owner has time to capture screenshots during the session | YES |

---

## K — Owner Explicit Approval Required

**Before any runtime action, the Owner must write one of these exact phrases** (or an equivalent explicit approval) in the session, command record, or evidence log. Copy and fill in the blanks:

### For Sandbox Import Only

```
APPROVED FOR SANDBOX IMPORT ONLY — [workflow name] — [date]
```

Example:
```
APPROVED FOR SANDBOX IMPORT ONLY — creative_asset_auto_skeleton — 2026-05-30
```

### For Sandbox Manual Execution Only

```
APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow name] — [date]
```

Example:
```
APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — creative_asset_auto_skeleton — 2026-05-30
```

> **Note:** This is a separate approval from sandbox import. Import approval does NOT authorize execution.

### For Production Runtime Only

```
APPROVED FOR PRODUCTION RUNTIME ONLY — [workflow name] — [date]
```

Example:
```
APPROVED FOR PRODUCTION RUNTIME ONLY — content_auto_skeleton — 2026-06-15
```

> **Note:** This is a separate approval from all sandbox approvals. Sandbox PASS does NOT imply production approval.

---

## L — Final Pre-Action Sign-Off

| # | Item | Owner Confirms |
|---|------|---------------|
| L-01 | All Section A repo state checks PASS | ☐ |
| L-02 | Latest phase handoff exists and confirms no secrets/active=true | ☐ |
| L-03 | Previous phase Codex PASS or Owner direct review confirmed | ☐ |
| L-04 | No secrets in repo — CI passing | ☐ |
| L-05 | All workflow JSON `active: false` | ☐ |
| L-06 | Approval gate document confirms this action is gated | ☐ |
| L-07 | Test data is dummy only — no real customer data | ☐ |
| L-08 | n8n instance confirmed as sandbox/test | ☐ |
| L-09 | No real output (post/reply/ads) will occur | ☐ |
| L-10 | Rollback procedure known | ☐ |
| L-11 | Evidence capture plan ready | ☐ |
| L-12 | Explicit approval phrase written above (Section K) | ☐ |

**Owner Sign-Off:**

```
Owner: Bo Bao
Date: ________________
Action approved: ________________
Approval phrase written: ________________
```

---

## What Happens if a Check Fails

| Failure | Action |
|---------|--------|
| Repo not clean | Stop. Do not proceed. Fix uncommitted changes or stale state first. |
| Phase handoff missing | Stop. Request Builder create the handoff before proceeding. |
| Secret found in repo | Stop immediately. Do not import or execute. Contact Builder to remove secret and re-run CI. |
| `"active": true` found | Stop immediately. Do not import. Contact Builder to fix before proceeding. |
| n8n instance is production | Stop immediately. Confirm sandbox instance URL before proceeding. |
| Real credentials in n8n | Stop. Remove real credentials from n8n Settings before proceeding. |

---

## Related Documents

- [SANDBOX_RUNBOOK_INDEX.md](SANDBOX_RUNBOOK_INDEX.md) — which workflows have runbooks
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — import step-by-step
- [RUNTIME_APPROVAL_DECISION_TREE.md](RUNTIME_APPROVAL_DECISION_TREE.md) — decision tree for approvals
- [docs/governance/OWNER_APPROVAL_GATE.md](../governance/OWNER_APPROVAL_GATE.md) — formal gate definitions

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This checklist is documentation-only. Completing this checklist does not authorize runtime action — explicit Owner approval phrase is required.*
