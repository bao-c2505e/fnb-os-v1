# 25 — Controlled n8n Import Dry-Run Handoff

**Phase:** 13 — Controlled n8n Import Dry-Run Handoff
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Purpose:** Step-by-step controlled handoff for Owner/operator to perform the actual n8n import dry-run in a sandbox/test environment.

---

## What This Document Is

This is the **operator handoff** for the n8n import dry-run. It gives the Owner/operator a single, self-contained reference to follow during the actual import session.

### Phase Distinction

| Phase | Role | Key Document |
|-------|------|-------------|
| Phase 10 | Procedure | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` — full 10-step procedure |
| Phase 11 | Evidence / Checklist Pack | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` — evidence log to fill |
| Phase 12 | Readiness Gate | `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` — GO / NO-GO criteria |
| Phase 13 | Controlled Operator Handoff | This document — what to do, step by step, during the session |

**Phase 13 does NOT execute the import.** Claude did not access n8n, perform any import, or activate any workflow. This document is prepared in advance for the Owner/operator to follow independently.

---

## Non-Negotiable Rules — Read Before Starting

These rules apply for the entire import session. There are no exceptions.

| Rule | Requirement |
|------|-------------|
| Sandbox/test n8n only | Use a local or isolated n8n instance. Never the production instance. |
| Import workflow JSON only | Do not activate, execute, or manually trigger any node. |
| Keep workflow inactive | After each import, confirm the workflow toggle shows Inactive. Do not click Activate. |
| Placeholder credentials only | Do not enter real API keys, tokens, or passwords into n8n at any time. |
| No production paths | Do not connect any node to a live Facebook Page, Instagram, TikTok, Zalo OA, Meta Ads Manager, or messaging platform. |
| No posting | No content published to any social media platform. |
| No replying | No messages sent to real customers. |
| No ads spend | No advertising budget committed. |
| Record results | Fill `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` during and after the session. |
| Record issues | If any issue occurs, fill `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md`. |

---

## Files to Have Open During the Session

Open these files before the import session begins. Do not rely on memory.

| Order | File | Purpose |
|-------|------|---------|
| 1 | `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` | Confirm GO status before starting |
| 2 | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | Full procedure reference |
| 3 | `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | Quick-reference checklist |
| 4 | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | Evidence log — fill this during the session |
| 5 | `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` | Issue template — open if any error occurs |
| 6 | This document | Operator handoff — step-by-step |

---

## Operator Checklist — Before Import

Complete all items before importing the first workflow. Do not skip.

| ID | Item | Done |
|----|------|------|
| B-01 | Readiness gate reviewed — all GO conditions met (`docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md`) | [ ] |
| B-02 | n8n instance confirmed as sandbox/test (not production) | [ ] |
| B-03 | n8n instance is accessible — UI opens without error | [ ] |
| B-04 | n8n Settings → Credentials checked — no real API tokens active | [ ] |
| B-05 | n8n version noted (visible in UI footer or Settings) | [ ] |
| B-06 | Node.js >= 16 confirmed (`node --version`) | [ ] |
| B-07 | Validation script passed — `node scripts/validate_n8n_workflows.mjs` exits 0 | [ ] |
| B-08 | All 6 workflow JSON files accessible in `n8n/workflows/` | [ ] |
| B-09 | Evidence log open — `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | [ ] |
| B-10 | Evidence log Section 2 filled — repo state (`git log --oneline -3` pasted) | [ ] |
| B-11 | Evidence log Section 4 filled — n8n instance URL, n8n version, Node.js version | [ ] |
| B-12 | Session start time noted | [ ] |
| B-13 | Uninterrupted time allocated — minimum 30 minutes, 60 minutes recommended | [ ] |

**All 13 items must be checked before proceeding.**

---

## Operator Checklist — During Import (Per Workflow)

Repeat for each of the 6 workflows in the order listed below.

### Import Order

| # | File | Short Name | Risk Level |
|---|------|-----------|-----------|
| 1 | `n8n/workflows/content_auto_skeleton.json` | Content Auto | Standard |
| 2 | `n8n/workflows/creative_asset_auto_skeleton.json` | Creative Asset Auto | Standard |
| 3 | `n8n/workflows/ads_pack_auto_skeleton.json` | Ads Pack Auto | High — no ads spend |
| 4 | `n8n/workflows/crm_followup_auto_skeleton.json` | CRM Followup Auto | High — no messaging |
| 5 | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Comment Inbox Reply Assistant | High — no reply |
| 6 | `n8n/workflows/approval_publishing_skeleton.json` | Approval Publishing | High — no publish |

### Per-Workflow Import Steps

For each workflow, complete all steps before moving to the next:

| Step | Action |
|------|--------|
| D-01 | In n8n: go to Workflows → New → Import from File |
| D-02 | Select the workflow JSON file from `n8n/workflows/` |
| D-03 | Confirm import completes without error |
| D-04 | Open the imported workflow in n8n canvas |
| D-05 | Confirm workflow name contains `[SKELETON]` |
| D-06 | Confirm workflow toggle shows **Inactive** — do NOT activate |
| D-07 | Inspect nodes — confirm all publish/send/spend nodes are labeled `STUB DISABLED` or `NoOp` |
| D-08 | Confirm no node is connected to a live production credential |
| D-09 | Note any import warnings or errors |
| D-10 | Fill the per-workflow observation table in Evidence Log Section 6 |

### Per-Workflow Checks (Evidence Log Section 6)

For each workflow, record the following in the evidence log:

| Check | What to Record |
|-------|---------------|
| Import status | Imported without error / imported with warning / failed |
| Name in n8n | Copy exact name shown in n8n after import |
| Active status | Inactive (required) / Active (STOP — deactivate and record) |
| Node count | Count of nodes visible on canvas |
| Error Trigger present | Yes / No |
| Sticky Note present | Yes / No |
| Warnings during import | None / list any warnings |

**High-risk workflow additional checks (workflows 3–6):**

| Workflow | Extra Check |
|----------|-----------|
| Ads Pack Auto (WF-03) | Confirm: no Ads API node visible, no budget field populated |
| CRM Followup Auto (WF-04) | Confirm: `human_review_required` visible in node, no messaging API connected |
| Comment Inbox Reply Assistant (WF-05) | Confirm: escalation gate (If node) visible, both branches end in human review, no reply API connected |
| Approval Publishing (WF-06) | Confirm: all 5 publish branches are NoOp stubs, not-approved path ends in Stop and Error, no platform publish node |

---

## Operator Checklist — After Import

Complete after all 6 workflows have been imported.

| ID | Item | Done |
|----|------|------|
| A-01 | All 6 workflows imported | [ ] |
| A-02 | All 6 workflows show Inactive in n8n | [ ] |
| A-03 | No workflow was activated at any point | [ ] |
| A-04 | No node was manually triggered at any point | [ ] |
| A-05 | No real credentials were entered into n8n | [ ] |
| A-06 | No content was posted to any social platform | [ ] |
| A-07 | No message was sent to any customer | [ ] |
| A-08 | No advertising budget was committed | [ ] |
| A-09 | Evidence Log Sections 6 and 7 filled (per-workflow observations + post-import checklist) | [ ] |
| A-10 | Evidence Log Section 8 filled (safety confirmation gate with operator initials) | [ ] |
| A-11 | Evidence Log Section 9 filled (issue summary — enter "None" if no issues) | [ ] |
| A-12 | Evidence Log Section 10 filled — final result: PASS or BLOCKED (not NOT_RUN) | [ ] |
| A-13 | Any issues recorded in `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` (copy template, fill, save as new file in `logs/`) | [ ] |
| A-14 | Session end time noted | [ ] |

---

## Stop Conditions

Stop the import session immediately if any of the following occur. Record the stop condition in Evidence Log Section 9 and set Section 10 final result to BLOCKED.

| Stop ID | Condition | Immediate Action |
|---------|-----------|-----------------|
| S-01 | n8n import returns a hard error for any workflow | Stop. Do not import next workflow. Record error text in evidence log. |
| S-02 | Any imported workflow shows Active after import | Immediately set to Inactive. Record in evidence log. Treat Section 10 as BLOCKED. |
| S-03 | Any node is connected to a live production account | Abort session. Record in evidence log. Do not proceed. |
| S-04 | n8n instance is identified as production (not sandbox) | Abort session immediately. Do not import any workflow. |
| S-05 | A real API key, token, or password was accidentally entered | Revoke the credential immediately. Record in evidence log. |
| S-06 | Any automated execution is triggered (node runs, message sent, post published) | Abort session. Record what ran and what was sent/published. |
| S-07 | Validation script (`scripts/validate_n8n_workflows.mjs`) fails | Do not proceed with import. Fix reported failures first. |
| S-08 | Any of the 6 workflow JSON files are missing or corrupted | Stop. Restore from git: `git checkout HEAD -- n8n/workflows/`. Then re-run validation. |

---

## Evidence Required

The following evidence must be recorded in `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` for the dry-run session to be considered complete:

| Evidence Item | Location in Evidence Log |
|--------------|--------------------------|
| Repo state at session start (git log output) | Section 2 |
| n8n environment details (instance URL, version, Node.js version) | Section 4 |
| Pre-import checklist (P-01–P-09) with pass/fail | Section 5 |
| Per-workflow observation tables for all 6 workflows | Section 6 |
| Post-import checklist (Q-01–Q-08) with pass/fail | Section 7 |
| Safety confirmation gate (8 items, operator initials) | Section 8 |
| Issue summary (or "None") | Section 9 |
| Final result: PASS or BLOCKED | Section 10 |

**Screenshots are supplementary — they do not replace the evidence log.** The evidence log is the primary record.

---

## Issue Recording Procedure

If any issue occurs during the import session:

1. Copy `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md`.
2. Save the copy as `logs/N8N_IMPORT_ISSUE_[WORKFLOW_SHORT]-[DATE]-001.md` (e.g., `logs/N8N_IMPORT_ISSUE_CONTENT-20260601-001.md`).
3. Fill in all fields in the issue file.
4. Reference the issue ID in Evidence Log Section 9.
5. Determine if the issue is a STOP condition (see Stop Conditions above).
6. If STOP: set Evidence Log Section 10 to BLOCKED and do not continue the session.
7. If non-blocking: note the issue, continue, and resolve before signing off.

---

## Credential Placeholder Behavior During Dry-Run

All workflow nodes reference credentials by placeholder name (e.g., `REPLACE_WITH_N8N_SUPABASE_CREDENTIAL_NAME`). During the import dry-run:

- Placeholder credential names will not resolve in n8n. This is **expected**.
- n8n may display a "Credential not found" warning on affected nodes. This is **not a failure**.
- Do NOT create real credentials to resolve these warnings.
- Enter `TEST_PLACEHOLDER` as a credential value only if n8n requires a value to complete the import. Note this in the evidence log.
- The purpose of the dry-run is to test import structure, not credential connectivity.

---

## What Happens After a Successful Dry-Run

After all 6 workflows import without errors and the evidence log Section 10 is set to PASS:

1. Save and close the evidence log.
2. The dry-run is complete — no further action in n8n.
3. Do NOT activate any workflow in n8n.
4. Do NOT configure real credentials in n8n at this stage.
5. Report the evidence log result to the Builder/Reviewer for next-phase planning.
6. Phase 14 (if planned) will address credential setup, production configuration, and controlled live testing — separate from this dry-run.

---

## Phase Connections

| Phase | Document | Relationship to Phase 13 |
|-------|----------|--------------------------|
| Phase 8 | `docs/20_N8N_WORKFLOW_SKELETONS.md` | Source of the 6 workflow JSONs being imported |
| Phase 9 | `scripts/validate_n8n_workflows.mjs` | Validation script to run before import (B-07) |
| Phase 10 | `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` | Full procedure — read before this handoff |
| Phase 11 | `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` | Evidence log to fill during session |
| Phase 11 | `docs/23_N8N_IMPORT_DRY_RUN_CHECKLIST.md` | Quick-reference checklist companion |
| Phase 12 | `docs/24_N8N_IMPORT_DRY_RUN_READINESS_GATE.md` | GO / NO-GO gate to confirm before starting |
| Phase 13 | This document | Operator handoff — use during session |

---

## Known Limitations

1. **Claude did not perform this import** — the import must be performed by the Owner/operator in their own environment.
2. **n8n version compatibility** — workflow JSONs target n8n's standard import format. Minor `typeVersion` differences may produce import warnings for specific n8n versions. Record any such warnings in the evidence log; they are generally non-blocking.
3. **Node.js required** — the validation script (`scripts/validate_n8n_workflows.mjs`) requires Node.js >= 16. If not installed, complete B-06 first.
4. **Credential placeholders will not resolve** — see Credential Placeholder Behavior section above.
5. **Phase 13 does not replace Phase 10** — Phase 10 is the primary procedure document. Phase 13 is the operator-facing handoff summary for use during the session.

---

*End of Phase 13 Controlled n8n Import Dry-Run Handoff*
