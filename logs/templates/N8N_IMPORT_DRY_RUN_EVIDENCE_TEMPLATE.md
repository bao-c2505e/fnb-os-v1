# n8n Import Dry-Run Evidence Template

**Template Version:** 1.0 — 2026-05-28
**Usage:** Copy this file to `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_[MODULE]-[DATE].md` and fill all [FILL] fields.
**Scope:** Generic — reusable for any module or phase, not only Phase 8.

> Do NOT fill this template directly. Copy it first.
> Evidence result defaults to NOT_RUN until the session is completed.

---

## Section 1 — Evidence Log Metadata

| Field | Value |
|-------|-------|
| Evidence Log ID | `EV-[MODULE]-[DATE]-[SEQ]` (e.g. `EV-CONTENT-AUTO-20260529-001`) |
| Module / Phase | [FILL: e.g. Phase 8 — Content Auto Skeleton] |
| Repo | [FILL: e.g. `https://github.com/bao-c2505e/fnb-os-v1`] |
| Log Created By | [FILL: Agent or human] |
| Log Created Date | [FILL: YYYY-MM-DD] |
| Log Filled By | [FILL: Owner / Operator name] |
| Log Fill Date | [FILL: YYYY-MM-DD] |
| Session Type | [FILL: Import Dry-Run / Smoke Test / Full Activation / Other] |
| Session Duration | [FILL] |

---

## Section 2 — Repo State at Time of Session

| Field | Value |
|-------|-------|
| Branch | [FILL: e.g. `main`] |
| HEAD commit | [FILL: run `git log --oneline -1`] |
| Working tree state | [FILL: Clean / Modified — describe] |
| Relevant file commit | [FILL: commit hash where workflow file was last modified] |

---

## Section 3 — Workflow(s) Under Test

| # | File Path | Expected Workflow Name | Expected Node Count | Status |
|---|-----------|----------------------|-------------------|--------|
| 1 | [FILL] | [FILL] | [FILL] | [FILL: IMPORTED / FAILED / SKIPPED] |
| 2 | [FILL] | [FILL] | [FILL] | [FILL] |

*Add rows as needed.*

---

## Section 4 — Target Environment

| Field | Value |
|-------|-------|
| n8n Instance Type | [FILL: Local / Docker / Cloud] |
| n8n Instance URL | [FILL: e.g. `http://localhost:5678` — no production URLs] |
| n8n Version | [FILL] |
| Host OS | [FILL] |
| Node.js Version | [FILL] |
| Static Validator Run | [FILL: PASS / BLOCKED_BY_ENVIRONMENT / SKIPPED] |
| Import Method | [FILL: n8n UI Import / CLI] |
| Is Production Instance | [FILL: YES / NO — must be NO for dry-run] |

---

## Section 5 — Pre-Session Checklist

| # | Pre-Condition | Status | Notes |
|---|--------------|--------|-------|
| P-01 | Static validator passed (`node scripts/validate_n8n_workflows.mjs` exits 0) | [FILL: PASS / BLOCKED / SKIPPED] | [FILL] |
| P-02 | n8n instance confirmed local (not production) | [FILL: PASS / BLOCKED] | [FILL] |
| P-03 | n8n accessible in browser | [FILL: PASS / BLOCKED] | [FILL] |
| P-04 | Workflow file(s) confirmed present on disk | [FILL: PASS / BLOCKED] | [FILL] |
| P-05 | No real credentials will be entered | [FILL: CONFIRMED] | [FILL] |
| P-06 | Operator has read import procedure doc | [FILL: CONFIRMED / NOT READ] | [FILL] |

---

## Section 6 — Per-Workflow Import Observations

*Duplicate this block for each workflow under test.*

### [Workflow Name]

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n matches expected | [Expected name] | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible | Yes | [FILL] | [FILL] |
| Node count visible | [Expected count] | [FILL] | [FILL] |
| Error Trigger node visible | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

*Add module-specific risk checks below if applicable (e.g. for ads, CRM, inbox, publishing workflows):*

| High-Risk Check | Expected | Observed | Pass? |
|----------------|----------|----------|-------|
| [FILL: e.g. No Ads API node visible] | [FILL] | [FILL] | [FILL] |
| [FILL: e.g. No messaging API node visible] | [FILL] | [FILL] | [FILL] |
| [FILL: e.g. All publish nodes are NoOp stubs] | [FILL] | [FILL] | [FILL] |

---

## Section 7 — Post-Session Checklist

| # | Post-Session Check | Status | Notes |
|---|-------------------|--------|-------|
| Q-01 | All tested workflows appear in n8n workflow list | [FILL: PASS / FAIL] | [FILL] |
| Q-02 | All tested workflows show Inactive status | [FILL: PASS / FAIL] | [FILL] |
| Q-03 | No execution history for any tested workflow | [FILL: PASS / FAIL] | [FILL] |
| Q-04 | No real credentials configured at any point | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-05 | No workflow activated at any point | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-06 | No workflow manually executed at any point | [FILL: CONFIRMED / ISSUE] | [FILL] |

---

## Section 8 — Safety Confirmation

| Safety Gate | Confirmation | Operator Initials |
|------------|-------------|-------------------|
| No workflow activated | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No workflow executed | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No real credentials entered | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No content auto-posted | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No messages auto-sent to customers | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No ads launched or budget committed | [FILL: CONFIRMED / ISSUE] | [FILL] |
| [Add module-specific safety gates as needed] | [FILL] | [FILL] |

---

## Section 9 — Issue Summary

| # | Issue ID | Workflow | Description | Severity | Status |
|---|----------|----------|-------------|----------|--------|
| 1 | [FILL or NONE] | [FILL] | [FILL] | [FILL] | [FILL] |

*For BLOCKER issues: copy `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` to a separate file.*

---

## Section 10 — Final Result

| Field | Value |
|-------|-------|
| All workflows imported | [FILL: YES / NO / PARTIAL] |
| All workflows Inactive | [FILL: YES / NO] |
| No STOP conditions triggered | [FILL: YES / NO] |
| All safety gates confirmed | [FILL: YES / NO] |
| Issues count | [FILL: NONE / count] |
| Operator sign-off | [FILL: name + date] |

**FINAL RESULT:**

```
[ ] PASS       — All checks passed, all safety gates confirmed, no STOP conditions
[ ] BLOCKED    — One or more STOP conditions or BLOCKER issues (see Section 9)
[X] NOT_RUN    — Session has not been executed yet (default — change after session)
```

---

## Related Files

| File | Purpose |
|------|---------|
| `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | Full step-by-step import procedure |
| `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | Quick-reference import checklist |
| `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | Phase 11 specific evidence log (pre-filled for Phase 8 workflows) |
| `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` | Issue tracking template |
| `scripts/validate_n8n_workflows.mjs` | Static validator script |

---

*Template: n8n Import Dry-Run Evidence — Phase 11*
*Do NOT fill this template directly. Copy to a new file first.*
