# Phase 26 — First Sandbox Import: Creative Asset Auto Skeleton

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 26 — First Sandbox Import: Creative Asset Auto Skeleton
**By:** Claude Code (Builder, AGT-02)
**Date:** 2026-06-01
**Status:** IMPORT_EVIDENCE_READY — AWAITING OWNER SANDBOX IMPORT + CONFIRMATION

---

## Owner Approval Phrase — Captured

```
APPROVED FOR SANDBOX IMPORT ONLY — creative_asset_auto_skeleton — 2026-06-01
```

**Approval recorded in:** this document, `handoff/PHASE_26_HANDOFF.md`, `logs/AGENT_ACTIVITY_LOG.md`.

---

## Section A — Purpose

Phase 26 performs the first sandbox import of `creative_asset_auto_skeleton` into the n8n sandbox.

This phase **does not execute** the workflow. It **does not activate** the workflow. It imports only — making the workflow visible in the sandbox canvas for inspection and future execution planning.

This phase is authorized because:
- Phase 25 Sandbox Import Readiness Gate: DONE (commit `9bfaeecc`)
- Phase 22A Evidence Capture Pack: DONE (evidence pack and evidence log template ready)
- Owner approval phrase: issued this session, `2026-06-01`

---

## Section B — Pre-Import Verification (Builder-Confirmed)

The following items have been confirmed by Builder before this document was created.

### B1 — Repo State

| Check | Required | Confirmed | Detail |
|-------|----------|-----------|--------|
| git branch | main | YES | `git branch --show-current` → `main` |
| HEAD = origin/main | Yes | YES | `9bfaeecc` = `origin/main` |
| Working tree | Clean | YES | `git status --short` → (no output) |
| Phase 25 handoff exists | Yes | YES | `handoff/PHASE_25_HANDOFF.md` present |
| Phase 25 gate doc exists | Yes | YES | `docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md` present |
| CI history | Prior phases CLEAN | YES | Phase 20 CI 36/36 PASS; no workflow JSON modified since |

### B2 — Workflow / Module Identity

| Check | Required | Confirmed | Detail |
|-------|----------|-----------|--------|
| Workflow name | exact file in n8n/workflows/ | YES | `creative_asset_auto_skeleton` |
| Workflow JSON path | exists in repo | YES | `n8n/workflows/creative_asset_auto_skeleton.json` |
| Workflow JSON valid | CI validate_json PASS | YES | Phase 20 CI confirmed 36/36 PASS; file untouched since |
| `"active": false` | confirmed in JSON | YES | Line 7: `"active": false` |
| n8n name in JSON | `[SKELETON]` suffix | YES | `"FnB OS V1 — Creative Asset Auto [SKELETON]"` |
| Phase 22A evidence pack | exists | YES | `docs/36_PHASE_22A_CREATIVE_ASSET_SANDBOX_EVIDENCE_CAPTURE_PACK.md` |
| Phase 22A evidence log | exists | YES | `logs/phase_22a_creative_asset_sandbox_evidence_log.md` |

### B3 — Credential and Secret Safety

| Check | Required | Confirmed | Detail |
|-------|----------|-----------|--------|
| No production credentials | confirmed | YES | All credential fields use `REPLACE_WITH_*` placeholders |
| No secrets in repo | CI CLEAN | YES | `check_no_secrets.py` CLEAN in Phase 20 CI |
| No API keys in workflow JSON | confirmed | YES | `instanceId: REPLACE_WITH_INSTANCE_ID`, no real keys |
| No production webhook URLs | confirmed | YES | No HTTP Request node pointing to production endpoints |

### B4 — Phase Boundary

| Check | Required for this phase | Confirmed |
|-------|------------------------|-----------|
| Activation forbidden | YES | Import only — activation is a separate, higher-level approval |
| Manual execution forbidden | YES | Execution requires `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY` phrase |
| Real API calls forbidden | YES | Import is canvas import only — no workflow runs |
| Auto-post forbidden | YES | No execution, no auto-post possible |
| Auto-reply forbidden | YES | No execution, no auto-reply possible |
| Ad spend forbidden | YES | No execution, no ad spend possible |

---

## Section C — Import Instructions (Owner to Perform)

Builder cannot perform n8n UI actions. Owner performs the import manually in the n8n sandbox.

**Import type:** Canvas import via n8n UI — import workflow JSON from file.

**Step-by-step:**

```
1. Open n8n sandbox (NOT the production n8n instance — confirm URL is sandbox).
2. Confirm you are in the n8n SANDBOX, not production.
3. In n8n, navigate to: Workflows → New → Import from File (or drag-and-drop).
4. Select the file: n8n/workflows/creative_asset_auto_skeleton.json
   (locate this in the local repo directory D:\FNB_OS_V1\n8n\workflows\)
5. After import, confirm the workflow name shows:
   "FnB OS V1 — Creative Asset Auto [SKELETON]"
6. Confirm the workflow status is INACTIVE (toggle OFF / active = false).
   STOP if the workflow appears active = true after import.
7. Do NOT click the Activate toggle.
8. Do NOT click Execute Workflow or Test Workflow.
9. View the canvas. Confirm nodes are visible. Do not modify any node.
10. Take a screenshot of the workflow canvas showing:
    - Workflow name
    - Inactive status
    - Node structure visible
11. Record the n8n sandbox URL used.
12. Record execution count = 0 (verify in n8n execution history).
13. Fill the evidence log: logs/phase_26_creative_asset_sandbox_import_evidence_log.md
14. Return to Builder/Codex for evidence review.
```

---

## Section D — Expected Post-Import State

| Item | Expected State |
|------|---------------|
| Workflow appears in n8n sandbox | YES — canvas view accessible |
| Workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| Workflow active status | **INACTIVE** (`active = false`) |
| Execution count | **Zero** — no executions |
| Credentials visible | `REPLACE_WITH_*` placeholders — no real credentials |
| Webhook URLs | Stub only — no production endpoints |
| Node count | 14 nodes (matching Phase 22A Section E node chain) |

---

## Section E — Evidence Log Reference

Evidence log for this import event:

```
logs/phase_26_creative_asset_sandbox_import_evidence_log.md
```

Owner fills this log after performing the import. See Section C step 13 above.

---

## Section F — Stop Conditions

If any of the following occur, stop immediately:

| Stop Condition | Action |
|---------------|--------|
| Workflow shows `active = true` after import | Stop. Deactivate immediately. Notify Builder. Do not proceed. |
| n8n instance URL matches production URL | Stop. Do not import. Notify Builder. |
| Real credential prompt appears during import | Stop. Do not enter credentials. Notify Builder. |
| Execution count is non-zero after import | Stop. Something triggered unexpectedly. Notify Builder. |
| Any real API call triggered during import | Stop. Document and escalate immediately. |
| Any message sent to real customer | Stop. Document and escalate immediately. |
| Import fails with unexpected error | Stop. Do not retry without Owner re-approval. |

---

## Section G — Safety Confirmation (Builder Pre-Import)

| Confirmation | Status |
|-------------|--------|
| Workflow imported into n8n (this section) | NO — awaiting Owner action |
| Workflow activated | NO |
| Workflow executed | NO |
| Real API called | NO |
| Production credentials added | NO |
| Real customer data used | NO |
| Auto-post performed | NO |
| Auto-reply performed | NO |
| Ad spend committed | NO |
| Workflow JSON modified | NO |
| `"active": true` introduced | NO |
| Secrets added to repo | NO |

---

## Section H — Related Documents

| Document | Path |
|----------|------|
| Phase 25 Sandbox Import Readiness Gate | `docs/PHASE_25_SANDBOX_IMPORT_READINESS_GATE.md` |
| Pre-Import Checklist | `docs/runbooks/SANDBOX_IMPORT_READINESS_CHECKLIST.md` |
| Sandbox Import Test Runbook | `docs/runbooks/SANDBOX_IMPORT_TEST_RUNBOOK.md` |
| Phase 22A Evidence Capture Pack | `docs/36_PHASE_22A_CREATIVE_ASSET_SANDBOX_EVIDENCE_CAPTURE_PACK.md` |
| Phase 22A Evidence Log | `logs/phase_22a_creative_asset_sandbox_evidence_log.md` |
| Phase 26 Evidence Log | `logs/phase_26_creative_asset_sandbox_import_evidence_log.md` |
| Sandbox Evidence Pack Template | `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md` |
| Workflow JSON | `n8n/workflows/creative_asset_auto_skeleton.json` |
| Owner Approval Gate | `docs/governance/OWNER_APPROVAL_GATE.md` |

---

## Section I — Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 22A | Owner Evidence Capture Pack — creative_asset_auto_skeleton | DONE + PUSHED |
| Phase 24A | Sandbox Runbook Index & Owner Runtime Readiness | DONE + PUSHED |
| Phase 24B | Sandbox Evidence Pack Template & Execution Log Standardization | DONE + PUSHED |
| Phase 25 | Sandbox Import Readiness Gate | DONE + PUSHED (commit `9bfaeecc`) |
| **Phase 26** | **First Sandbox Import — creative_asset_auto_skeleton (this phase)** | **IMPORT_EVIDENCE_READY — awaiting Owner import + confirmation** |
| Phase 27 (next) | Sandbox Manual Execution — creative_asset_auto_skeleton | FUTURE — requires Phase 26 import DONE + new Owner approval phrase |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*Phase 26 is sandbox import only. Execution requires a separate approval phrase: `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — creative_asset_auto_skeleton — [date]`*
