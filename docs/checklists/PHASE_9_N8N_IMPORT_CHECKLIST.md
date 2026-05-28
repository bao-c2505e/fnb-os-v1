# Phase 9 — n8n Import Checklist

Phase: 9 — n8n Import Validation Pack
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Filled By: Owner (Bo Bao)

---

## Instructions

Complete this checklist in order. For each item, mark:
- `[x]` = Done / Pass
- `[!]` = Blocked — note the blocker below the item
- `[~]` = Skipped — note the reason below the item

Record final results in `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md`.

---

## Section A — Pre-Import: Environment Check

- [ ] A1. n8n instance is running and accessible (local URL or cloud URL confirmed)
  - n8n version: `___________`
  - Instance type: `[ ] Self-hosted  [ ] n8n Cloud`
  - URL (do not record real URL in this file — note "confirmed" only): `___________`

- [ ] A2. Node.js >= 16 is installed on this machine
  - Run: `node --version`
  - Result: `___________`

- [ ] A3. Static validator has been run (or is marked "skipped — Node.js not available")
  - Run: `node scripts/validate_n8n_workflows.mjs` from repo root
  - Result: `[ ] All PASS  [ ] Failures found (see script output)  [ ] Skipped — no Node.js`

- [ ] A4. Phase 8 workflow files are present at `n8n/workflows/`
  - Confirm 6 files exist: content_auto, creative_asset_auto, ads_pack_auto, crm_followup_auto, comment_inbox_reply_assistant, approval_publishing
  - File count confirmed: `___________`

- [ ] A5. No real credentials will be entered during this import session
  - Confirm: `[ ] Confirmed — no real API keys or tokens will be entered`

- [ ] A6. No workflow will be activated during this import session
  - Confirm: `[ ] Confirmed — all workflows will remain inactive`

---

## Section B — Import: content_auto_skeleton.json

- [ ] B1. In n8n: Workflows → New → Import from file
- [ ] B2. Selected file: `n8n/workflows/content_auto_skeleton.json`
- [ ] B3. Import preview shows name: `FnB OS V1 — Content Auto [SKELETON]`
- [ ] B4. Import completed without error
- [ ] B5. Workflow canvas opened — node count visible
  - Expected: 15 nodes
  - Actual: `___________`
- [ ] B6. `active` toggle is OFF
- [ ] B7. Sticky Note warning "PHASE 8 SKELETON — DO NOT ACTIVATE" is visible on canvas
- [ ] B8. All credential slots show empty / "credential required" (no auto-filled credentials)
- [ ] B9. Workflow NOT activated — confirmed active=OFF before closing

**Section B result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section C — Import: creative_asset_auto_skeleton.json

- [ ] C1. In n8n: Workflows → New → Import from file
- [ ] C2. Selected file: `n8n/workflows/creative_asset_auto_skeleton.json`
- [ ] C3. Import preview shows name: `FnB OS V1 — Creative Asset Auto [SKELETON]`
- [ ] C4. Import completed without error
- [ ] C5. Workflow canvas opened — node count visible
  - Expected: 15 nodes
  - Actual: `___________`
- [ ] C6. `active` toggle is OFF
- [ ] C7. Sticky Note warning visible on canvas
- [ ] C8. All credential slots show empty / "credential required"
- [ ] C9. Workflow NOT activated

**Section C result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section D — Import: ads_pack_auto_skeleton.json

**Risk level: MEDIUM — contains NO ADS SPEND warning. Read sticky note before proceeding.**

- [ ] D1. In n8n: Workflows → New → Import from file
- [ ] D2. Selected file: `n8n/workflows/ads_pack_auto_skeleton.json`
- [ ] D3. Import preview shows name: `FnB OS V1 — Ads Pack Auto [SKELETON]`
- [ ] D4. Import completed without error
- [ ] D5. Workflow canvas opened — node count visible
  - Expected: 15 nodes
  - Actual: `___________`
- [ ] D6. `active` toggle is OFF
- [ ] D7. Sticky Note warning "NO ADS SPEND" visible on canvas
- [ ] D8. All credential slots show empty / "credential required"
- [ ] D9. Workflow NOT activated
- [ ] D10. Confirm: No ad spend has been triggered by this import

**Section D result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section E — Import: crm_followup_auto_skeleton.json

**Risk level: MEDIUM — contains NO AUTO-SEND warning. Read sticky note before proceeding.**

- [ ] E1. In n8n: Workflows → New → Import from file
- [ ] E2. Selected file: `n8n/workflows/crm_followup_auto_skeleton.json`
- [ ] E3. Import preview shows name: `FnB OS V1 — CRM Follow-Up Auto [SKELETON]`
- [ ] E4. Import completed without error
- [ ] E5. Workflow canvas opened — node count visible
  - Expected: 15 nodes
  - Actual: `___________`
- [ ] E6. `active` toggle is OFF
- [ ] E7. Sticky Note warning "NO AUTO-SEND" visible on canvas
- [ ] E8. All credential slots show empty / "credential required"
- [ ] E9. Workflow NOT activated
- [ ] E10. Confirm: No messages have been sent to any customer

**Section E result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section F — Import: comment_inbox_reply_assistant_skeleton.json

**Risk level: MEDIUM — contains escalation gate. Read sticky note before proceeding.**

- [ ] F1. In n8n: Workflows → New → Import from file
- [ ] F2. Selected file: `n8n/workflows/comment_inbox_reply_assistant_skeleton.json`
- [ ] F3. Import preview shows name: `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]`
- [ ] F4. Import completed without error
- [ ] F5. Workflow canvas opened — node count visible
  - Expected: 13 nodes
  - Actual: `___________`
- [ ] F6. `active` toggle is OFF
- [ ] F7. Sticky Note warning visible on canvas
- [ ] F8. All credential slots show empty / "credential required"
- [ ] F9. Workflow NOT activated
- [ ] F10. Confirm: No replies have been posted to any social media comment

**Section F result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section G — Import: approval_publishing_skeleton.json

**Risk level: HIGH — this is the publishing gate. Read sticky note before proceeding.**

- [ ] G1. In n8n: Workflows → New → Import from file
- [ ] G2. Selected file: `n8n/workflows/approval_publishing_skeleton.json`
- [ ] G3. Import preview shows name: `FnB OS V1 — Approval and Publishing Gate [SKELETON]`
- [ ] G4. Import completed without error
- [ ] G5. Workflow canvas opened — node count visible
  - Expected: 17 nodes
  - Actual: `___________`
- [ ] G6. `active` toggle is OFF
- [ ] G7. Sticky Note warning visible on canvas
- [ ] G8. All credential slots show empty / "credential required"
- [ ] G9. Webhook trigger is visible but NOT connected to any real endpoint
- [ ] G10. Workflow NOT activated
- [ ] G11. Confirm: No content has been published to any platform

**Section G result: `[ ] PASS  [ ] FAIL  [ ] BLOCKED`**
Notes: `___________`

---

## Section H — Post-Import Verification

- [ ] H1. All 6 workflows appear in n8n Workflows list
- [ ] H2. All 6 workflows show active=OFF in the list view
- [ ] H3. No workflow has been executed (execution count = 0 for all)
- [ ] H4. No credentials have been created or auto-filled during this session
- [ ] H5. No external services were contacted during this session (Google Sheets, Telegram, Meta, TikTok, Zalo, Anthropic API)

---

## Section I — Log and Sign-Off

- [ ] I1. Results recorded in `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md`
- [ ] I2. Any FAIL or BLOCKED items noted with exact n8n error message
- [ ] I3. Screenshots taken (optional — note file location here): `___________`
  - Note: Screenshots are optional and supplementary. The filled log template is the authoritative record.

**Overall Result: `[ ] ALL PASS  [ ] PARTIAL — some BLOCKED  [ ] FAIL`**

**Filled By:** `___________`
**Date:** `___________`
**n8n Version:** `___________`

---

## STOP Conditions

Do NOT continue with Phase 10 credential setup if any of the following are true:

| Condition | Action |
|-----------|--------|
| Any workflow fails to import with a JSON parse error | Report to Builder. JSON file may be malformed. |
| Any workflow shows `active: true` after import | STOP. Do NOT proceed. Contact Builder immediately. |
| Any credential was auto-filled during import | STOP. Delete the workflow. Check n8n credential store. Contact Builder. |
| Any workflow shows execution count > 0 | STOP. Check n8n execution log. Contact Builder. |
| Any message was sent or ad spend triggered | STOP. Contact Builder and document immediately. |
