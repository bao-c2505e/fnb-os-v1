# n8n Import Dry-Run Evidence Log — Phase 11

**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Phase:** 11 — n8n Import Dry-Run Evidence Pack
**Purpose:** Structured evidence record to be filled by Owner/Operator during the actual import dry-run session.

> **STATUS: NOT_RUN**
> This file is a pre-structured evidence log. No import has been executed.
> No n8n instance was accessed during Phase 11.
> All sections marked [FILL] must be completed by Owner/Operator during the actual dry-run session.
> Procedure to follow: `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`
> Checklist to follow: `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md`

---

## Section 1 — Phase Metadata

| Field | Value |
|-------|-------|
| Evidence Log ID | `EV-PH11-N8N-DRY-RUN-001` |
| Phase | 11 |
| Log Created By | Claude Code (Builder, AGT-02) |
| Log Created Date | 2026-05-28 |
| Log Filled By | [FILL: Owner / Operator name] |
| Log Fill Date | [FILL: YYYY-MM-DD] |
| Dry-Run Session Duration | [FILL: e.g. 45 minutes] |
| Session Type | Import Dry-Run — no workflow activation, no real credentials |

---

## Section 2 — Repo State at Time of Dry-Run

Fill this section at the start of the dry-run session by running `git log --oneline -1` and `git status --short`.

| Field | Value at Phase 11 Creation | Value at Dry-Run (FILL) |
|-------|---------------------------|------------------------|
| Branch | main | [FILL] |
| HEAD commit | `e4ea363` — docs: add phase 10 n8n import dry-run procedure | [FILL] |
| Working tree | PRE-COMMIT — 4 modified tracked files + 4 untracked Phase 11 files (not clean until commit approved) | [FILL: run `git status --short` at dry-run start — should be Clean after commit] |
| Phase 8 JSON status | `ad867b3` — zero local modifications, untouched from Phase 8 commit | [FILL: confirm still `ad867b3` or note if changed] |
| Phase 9 script present | `scripts/validate_n8n_workflows.mjs` — YES | [FILL: YES / NO] |

---

## Section 3 — Workflows Under Test

All 6 Phase 8 workflow skeleton JSON files. Paths relative to repo root.

| # | File Path | Expected Workflow Name | Node Count | Status |
|---|-----------|----------------------|-----------|--------|
| WF-01 | `n8n/workflows/content_auto_skeleton.json` | `FnB OS V1 — Content Auto [SKELETON]` | 15 | [FILL: IMPORTED / FAILED / SKIPPED] |
| WF-02 | `n8n/workflows/creative_asset_auto_skeleton.json` | `FnB OS V1 — Creative Asset Auto [SKELETON]` | 15 | [FILL] |
| WF-03 | `n8n/workflows/ads_pack_auto_skeleton.json` | `FnB OS V1 — Ads Pack Auto [SKELETON]` | 15 | [FILL] |
| WF-04 | `n8n/workflows/crm_followup_auto_skeleton.json` | `FnB OS V1 — CRM Follow-Up Auto [SKELETON]` | 15 | [FILL] |
| WF-05 | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]` | 13 | [FILL] |
| WF-06 | `n8n/workflows/approval_publishing_skeleton.json` | `FnB OS V1 — Approval and Publishing Gate [SKELETON]` | 18 | [FILL] |

---

## Section 4 — Import Target Environment

Fill before starting the dry-run. Do NOT enter real credentials here.

| Field | Value |
|-------|-------|
| n8n Instance Type | [FILL: Local / Docker / Cloud — specify] |
| n8n Instance URL | [FILL: e.g. `http://localhost:5678` — do not use production URL] |
| n8n Version | [FILL: run Settings → About in n8n] |
| Host OS | [FILL: e.g. Windows 10 / macOS 14 / Ubuntu 22] |
| Node.js Version | [FILL: run `node --version`] |
| npm Version | [FILL: run `npm --version`] |
| Static Validator Run | [FILL: PASS (exit 0) / BLOCKED_BY_ENVIRONMENT / SKIPPED] |
| Import Method | [FILL: n8n UI → Import from File / n8n CLI] |
| Is Production Instance | [FILL: YES / NO — must be NO for dry-run] |

> **STOP:** If "Is Production Instance = YES" — do not proceed. Use a local instance only.

---

## Section 5 — Pre-Import Checklist

Complete before importing any workflow. Check each item or record BLOCKED.

| # | Pre-Condition | Status | Notes |
|---|--------------|--------|-------|
| P-01 | Node.js >= 16 installed and `node --version` returns valid version | [FILL: PASS / BLOCKED] | [FILL] |
| P-02 | Static validator run: `node scripts/validate_n8n_workflows.mjs` exits 0 | [FILL: PASS / BLOCKED / SKIPPED] | [FILL] |
| P-03 | n8n instance is local (not production) | [FILL: PASS / BLOCKED] | [FILL] |
| P-04 | n8n instance is running and workflow list page is accessible | [FILL: PASS / BLOCKED] | [FILL] |
| P-05 | All 6 workflow JSON files present in `n8n/workflows/` | [FILL: PASS / BLOCKED] | [FILL] |
| P-06 | No real credentials will be entered during this session | [FILL: CONFIRMED / BLOCKED] | [FILL] |
| P-07 | Owner/Operator has read `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | [FILL: CONFIRMED / NOT READ] | [FILL] |
| P-08 | Owner/Operator has read `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | [FILL: CONFIRMED / NOT READ] | [FILL] |
| P-09 | Current workflow count in n8n noted for comparison after import | [FILL: CONFIRMED — count: X] | [FILL] |

> If any P-01 through P-06 is BLOCKED: **do not proceed.** Record blocker and stop.

---

## Section 6 — Per-Workflow Import Observations

Fill one row per workflow immediately after importing. Do NOT fill from memory after the session.

### WF-01: Content Auto

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — Content Auto [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible | Yes | [FILL] | [FILL] |
| Node count visible | 15 | [FILL] | [FILL] |
| Error Trigger node visible | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

### WF-02: Creative Asset Auto

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — Creative Asset Auto [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible | Yes | [FILL] | [FILL] |
| Node count visible | 15 | [FILL] | [FILL] |
| Error Trigger node visible | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

### WF-03: Ads Pack Auto

> **HIGH-RISK WORKFLOW — Ads spend possible in production.** Extra confirmations required.

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — Ads Pack Auto [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible (orange/warning color) | Yes | [FILL] | [FILL] |
| Node count visible | 15 | [FILL] | [FILL] |
| NO Meta/TikTok/Zalo Ads API node visible | Confirmed absent | [FILL] | [FILL] |
| All output nodes are NoOp stubs | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| No ads budget committed | Confirmed | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

### WF-04: CRM Follow-Up Auto

> **HIGH-RISK WORKFLOW — Customer messages possible in production.** Extra confirmations required.

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — CRM Follow-Up Auto [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible (orange/warning color) | Yes | [FILL] | [FILL] |
| Node count visible | 15 | [FILL] | [FILL] |
| `Set: Draft Status + Human Review Flag` node visible | Yes | [FILL] | [FILL] |
| NO Zalo/Messenger/SMS API node visible | Confirmed absent | [FILL] | [FILL] |
| NoOp stub for queue (not a real send node) | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| No messages sent to real customers | Confirmed | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

### WF-05: Comment Inbox Reply Assistant

> **HIGH-RISK WORKFLOW — Auto-reply to real customers possible in production.** Extra confirmations required.

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible (orange/warning color) | Yes | [FILL] | [FILL] |
| Node count visible | 13 | [FILL] | [FILL] |
| `If: Escalation Required` node visible | Yes | [FILL] | [FILL] |
| Two branches visible (escalation + draft paths) | Yes | [FILL] | [FILL] |
| NO Facebook/TikTok/Instagram/Zalo reply API node | Confirmed absent | [FILL] | [FILL] |
| NoOp stub for reply queue (not a real reply node) | Yes | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| No auto-reply sent to real customers | Confirmed | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

### WF-06: Approval and Publishing Gate

> **GATE WORKFLOW — Connects to all publishing actions.** Most critical to verify as skeleton.

| Check | Expected | Observed | Pass? |
|-------|----------|----------|-------|
| Import succeeded without error | Yes | [FILL] | [FILL] |
| Workflow name in n8n | `FnB OS V1 — Approval and Publishing Gate [SKELETON]` | [FILL] | [FILL] |
| Active toggle state | OFF (Inactive) | [FILL] | [FILL] |
| Sticky Note node visible (blue — approval gate color) | Yes | [FILL] | [FILL] |
| Node count visible | 18 | [FILL] | [FILL] |
| Webhook trigger shows placeholder path (not live URL) | Yes | [FILL] | [FILL] |
| `Switch: Item Type` node with 5 branches visible | Yes | [FILL] | [FILL] |
| All 5 publish branches are NoOp stubs | Yes | [FILL] | [FILL] |
| `If: Is Approved` node visible | Yes | [FILL] | [FILL] |
| Not-approved path leads to `Stop and Error` | Yes | [FILL] | [FILL] |
| NO platform publish API node visible | Confirmed absent | [FILL] | [FILL] |
| No execution triggered | Yes | [FILL] | [FILL] |
| No real credential entered | Yes | [FILL] | [FILL] |
| No content published to any platform | Confirmed | [FILL] | [FILL] |
| No ads spend committed | Confirmed | [FILL] | [FILL] |
| Workflow saved | Yes | [FILL] | [FILL] |
| Any issues noted | None expected | [FILL] | [FILL] |

---

## Section 7 — Post-Import Checklist

Complete after all 6 workflows are imported.

| # | Post-Import Check | Status | Notes |
|---|------------------|--------|-------|
| Q-01 | All 6 workflows appear in n8n workflow list | [FILL: PASS / FAIL] | [FILL] |
| Q-02 | All 6 workflows show Inactive status in list | [FILL: PASS / FAIL] | [FILL] |
| Q-03 | No execution history for any of the 6 workflows | [FILL: PASS / FAIL] | [FILL] |
| Q-04 | No real credentials were configured at any point | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-05 | No workflow was activated at any point during this session | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-06 | No workflow was manually executed at any point during this session | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-07 | n8n instance is still local (not production) | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Q-08 | All issues (if any) logged in issue template | [FILL: CONFIRMED / N/A] | [FILL] |

---

## Section 8 — Safety Confirmation

Operator completes this section at end of dry-run session. Each item must be explicitly confirmed.

| Safety Gate | Confirmation | Operator Initials |
|------------|-------------|-------------------|
| No n8n workflow was activated | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No n8n workflow was manually executed | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No real API credentials were entered into n8n | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No content was auto-posted to any social platform | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No message was auto-sent to any real customer | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No ads campaign was launched or budget committed | [FILL: CONFIRMED / ISSUE] | [FILL] |
| No customer data was stored or processed | [FILL: CONFIRMED / ISSUE] | [FILL] |
| Approval gate workflows remain as NoOp stubs | [FILL: CONFIRMED / ISSUE] | [FILL] |

---

## Section 9 — Issue Summary

List any issues found during the dry-run. If none, write NONE.

| # | Issue ID | Workflow | Description | Severity | Status |
|---|----------|----------|-------------|----------|--------|
| 1 | [FILL or NONE] | [FILL] | [FILL] | [FILL: BLOCKER / WARNING / INFO] | [FILL: OPEN / RESOLVED] |

> For each BLOCKER: copy `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` and fill a separate issue file before proceeding to Phase 12.

---

## Section 10 — Final Dry-Run Result

| Field | Value |
|-------|-------|
| All 6 workflows imported | [FILL: YES / NO / PARTIAL] |
| All 6 workflows Inactive after import | [FILL: YES / NO] |
| No STOP conditions triggered | [FILL: YES / NO] |
| All safety gates confirmed | [FILL: YES / NO] |
| Issues logged | [FILL: NONE / count] |
| Operator sign-off | [FILL: Owner/Operator name + date] |

**FINAL RESULT:**

```
[ ] PASS       — All 6 imported, all Inactive, no STOP conditions, all safety gates confirmed
[ ] BLOCKED    — One or more STOP conditions triggered (see Section 9)
[X] NOT_RUN    — Dry-run has not been executed yet (default until session completed)
```

---

## Background — Phase 10 Environment Note

Phase 10 found that Node.js was not available on the build machine (BLOCKED_BY_ENVIRONMENT). This is a background note only. Phase 11 does not re-test Node.js. Before executing this evidence log, Owner must confirm Node.js >= 16 is available and run `node scripts/validate_n8n_workflows.mjs` per Section 5 pre-condition P-01 and P-02.

---

*Phase 11 — n8n Import Dry-Run Evidence Pack*
*Builder: Claude Code (AGT-02) — 2026-05-28*
*Evidence log created: 2026-05-28 | Dry-run executed: [FILL]*
