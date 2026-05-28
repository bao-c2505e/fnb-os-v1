# 15 — Manual Test Pack

**Phase:** 6 — OS Readiness Pack
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Purpose:** Define manual tests that validate FnB OS V1 can produce correct outputs through each module before runtime automation is built.

---

## How to Run

These are manual tests — no code execution. Tester (Owner or Codex) reads the input files, follows the steps, and checks the expected output against the pass/fail rule. Tests are executed against the existing Phase 5 sample outputs or by re-running the relevant agent manually.

---

## TEST-01 — Content Agent Sample Generation

**Test ID:** TEST-01
**Purpose:** Verify that Content Agent can produce a schema-compliant content output using Brand Brain and Content Auto SOP.

**Input files:**
- `brand-brain/vi-cuon.md`
- `schemas/content-output.schema.json`
- `templates/content-output-template.md`
- `module-sops/content-auto-sop.md`

**Steps:**
1. Open `module-sops/content-auto-sop.md` — confirm all 8 sections are present.
2. Open `brand-brain/vi-cuon.md` — confirm brand name, tone, content pillars are readable.
3. Open `templates/content-output-template.md` — confirm all 16 schema fields are present as `## field_name` headings.
4. Open `samples/vi-cuon/content-sample.md` — verify Sample 1 (Facebook post) is filled.
5. Cross-check each field in Sample 1 against the schema: confirm all required fields (content_id, brand_id, brand_name, content_type, platform, objective, target_audience, hook, caption, cta, approval_status, created_by_agent, created_at) are populated.
6. Confirm `approval_status: Draft`.
7. Confirm no hardcoded price, offer, or address.

**Expected output:** Sample 1 has all required fields, uses Brand Brain data, approval_status is Draft, offer uses placeholder.

**Pass rule:** All 13 required schema fields are present and non-empty. No invented price or offer. `approval_status: Draft`.

**Fail rule:** Any required field is missing, empty, or uses invented data not in Brand Brain.

**Owner approval required?** No — this is a read/verify test only. Owner approval required before any content goes to production.

---

## TEST-02 — Creative Asset Sample Generation

**Test ID:** TEST-02
**Purpose:** Verify that Creative Asset Agent can produce a schema-compliant creative brief using the correct SOP and template.

**Input files:**
- `brand-brain/vi-cuon.md`
- `schemas/creative-brief.schema.json`
- `templates/creative-brief-template.md`
- `module-sops/creative-asset-auto-sop.md`

**Steps:**
1. Open `module-sops/creative-asset-auto-sop.md` — confirm all 8 sections present.
2. Open `templates/creative-brief-template.md` — confirm all 17 schema fields present.
3. Open `samples/vi-cuon/creative-brief-sample.md` — verify Brief 1 (food photo) is filled.
4. Confirm all required fields are present: brief_id, brand_id, brand_name, asset_type, platform, format, objective, concept, visual_direction, approval_status, created_by_agent, created_at.
5. Confirm `qa_checklist` and `required_inputs` are populated.
6. Confirm `approval_status: Draft`.
7. Confirm `ai_tool_prompt` is safe (no explicit content, no false claims, or is null for live-action briefs).

**Expected output:** Both sample briefs have all required fields, include qa_checklist, and are marked Draft.

**Pass rule:** All 12 required fields present. `qa_checklist` populated. `approval_status: Draft`. No invented brand data.

**Fail rule:** Missing required field, empty qa_checklist, or `approval_status` not Draft.

**Owner approval required?** No — test only. Owner approval needed before brief is sent to photographer or AI tool.

---

## TEST-03 — Ads Pack Sample Generation

**Test ID:** TEST-03
**Purpose:** Verify that Ads Pack Agent produces a schema-compliant, compliance-flagged ads pack draft with no budget or campaign setup.

**Input files:**
- `brand-brain/vi-cuon.md`
- `schemas/ads-pack.schema.json`
- `templates/ads-pack-template.md`
- `module-sops/ads-pack-auto-sop.md`

**Steps:**
1. Open `module-sops/ads-pack-auto-sop.md` — confirm approval gate and "no campaign launch" rule is stated.
2. Open `samples/vi-cuon/ads-pack-sample.md` — verify both samples exist.
3. Confirm all required fields for each pack: ads_pack_id, brand_id, brand_name, campaign_objective, platform, funnel_stage, target_audience, angle, primary_text, headline, cta, approval_status, created_by_agent, created_at.
4. Confirm `compliance_notes` is populated for each pack.
5. Confirm `approval_status: Draft`.
6. Confirm offer uses `[OWNER_TO_PROVIDE_OFFER]`.
7. Confirm no campaign ID, ad account ID, or budget is present.
8. Confirm WARNING footer is present at top of file.

**Expected output:** Two ads packs, both Draft, compliance_notes filled, no budget/campaign data, offer placeholder used.

**Pass rule:** All 14 required fields present. `compliance_notes` non-empty. No campaign/budget data. `approval_status: Draft`.

**Fail rule:** Missing compliance_notes, any campaign ID or budget present, or offer hardcoded.

**Owner approval required?** No — test only. Owner approval required before any ad is launched.

---

## TEST-04 — CRM Follow-Up Sample Generation

**Test ID:** TEST-04
**Purpose:** Verify that CRM Follow-Up Agent produces sequences with human_review_required: true and no auto-send capability.

**Input files:**
- `brand-brain/vi-cuon.md`
- `schemas/crm-followup.schema.json`
- `templates/crm-followup-template.md`
- `module-sops/crm-followup-auto-sop.md`

**Steps:**
1. Open `module-sops/crm-followup-auto-sop.md` — confirm "human_review_required must always be true" and "no message sent" rules are stated.
2. Open `samples/vi-cuon/crm-followup-sample.md` — verify both sequences exist.
3. Confirm all required fields: sequence_id, brand_id, brand_name, lead_segment, customer_status, channel, trigger_event, message_sequence, human_review_required, approval_status, created_by_agent, created_at.
4. Confirm `human_review_required: true` on both sequences.
5. Confirm `message_sequence` has at least 1 step with step, delay, and message_template.
6. Confirm all message_template values use `[CUSTOMER_NAME]` — not real customer names.
7. Confirm `notes` field contains opt-in compliance statement.
8. Confirm WARNING footer present.

**Expected output:** Both sequences have human_review_required: true, message_sequence with ≥1 step, [CUSTOMER_NAME] placeholder, opt-in note.

**Pass rule:** `human_review_required: true` confirmed. No real customer data. `approval_status: Draft`. Opt-in note present.

**Fail rule:** `human_review_required` missing or false. Real PII present. No opt-in note.

**Owner approval required?** No — test only. Owner approval required before any message is sent.

---

## TEST-05 — Comment / Inbox Reply Sample Generation

**Test ID:** TEST-05
**Purpose:** Verify that Comment Inbox Agent produces reply drafts with human_review_required: true, correct escalation handling, and no auto-reply.

**Input files:**
- `brand-brain/vi-cuon.md`
- `schemas/comment-inbox-reply.schema.json`
- `templates/comment-inbox-reply-template.md`
- `module-sops/comment-inbox-assistant-sop.md`

**Steps:**
1. Open `module-sops/comment-inbox-assistant-sop.md` — confirm escalation table and "no auto-reply" rule.
2. Open `samples/vi-cuon/comment-inbox-reply-sample.md` — verify all 5 reply drafts exist.
3. For each reply: confirm reply_id, brand_id, brand_name, channel, customer_message, detected_intent, sentiment, human_review_required, approval_status, created_by_agent, created_at are present.
4. Confirm `human_review_required: true` on all 5 replies.
5. Confirm `customer_message` is verbatim (not summarized).
6. Confirm non-escalation replies have `escalation_required: false` and a non-null `draft_reply`.
7. Confirm address/price fields in draft replies use placeholders.
8. Confirm WARNING footer present.

**Expected output:** 5 replies, all human_review_required: true, verbatim customer messages, no auto-reply, placeholders for missing data.

**Pass rule:** `human_review_required: true` on all. Non-escalation cases have draft_reply. Placeholders used. `approval_status: Draft`.

**Fail rule:** Any reply missing human_review_required. Any draft_reply containing real address or price.

**Owner approval required?** No — test only. Owner approval required before any reply is posted.

---

## TEST-06 — Approval Status Transition

**Test ID:** TEST-06
**Purpose:** Verify the approval state machine works correctly — no item advances beyond Ready for Review without Owner action, and Published/Scheduled require prior Approved.

**Input files:**
- `schemas/approval-status.schema.json`
- `templates/approval-status-template.md`
- `samples/vi-cuon/approval-status-sample.md`
- `module-sops/approval-publishing-sop.md`

**Steps:**
1. Open `module-sops/approval-publishing-sop.md` — confirm state machine table with who-can-set rules.
2. Open `samples/vi-cuon/approval-status-sample.md` — verify 5 approval records.
3. Confirm all records are at Draft or Ready for Review only — none at Approved, Scheduled, or Published.
4. Confirm all `owner_decision` fields are `null` (no Owner decision yet in samples).
5. Confirm all `approved_at` fields are `null`.
6. Confirm `change_log` is present on all records with at least 1 entry.
7. Review state machine: confirm Published requires approved_at to be non-null.

**Expected output:** 5 records all at Draft or Ready for Review. No Approved/Published/Scheduled. change_log populated.

**Pass rule:** No sample has approval_status beyond Ready for Review. owner_decision is null. approved_at is null.

**Fail rule:** Any sample has approval_status of Approved, Scheduled, or Published. Any owner_decision is not null.

**Owner approval required?** Yes — only Owner can advance to Approved in a real run.

---

## TEST-07 — Log Entry Creation

**Test ID:** TEST-07
**Purpose:** Verify that structured log entries are created correctly using the log-entry schema and template.

**Input files:**
- `schemas/log-entry.schema.json`
- `templates/log-entry-template.md`
- `samples/vi-cuon/log-entry-sample.md`

**Steps:**
1. Open `templates/log-entry-template.md` — confirm all 12 schema fields present as headings.
2. Open `samples/vi-cuon/log-entry-sample.md` — verify 4 log entries exist.
3. For each entry: confirm log_id, timestamp, phase, agent_name, action_type, status, summary are present and non-empty.
4. Confirm action_type uses only allowed enum values (File Created, Content Draft, Phase Complete, etc.).
5. Confirm status uses only allowed enum values (Success, In Progress, Blocked, Failed, Needs Review).
6. Confirm `owner_action_required` is true or false (not null, not missing).

**Expected output:** 4 log entries, all required fields present, valid enum values used.

**Pass rule:** All 7 required fields non-empty. Valid action_type and status enum values. owner_action_required is boolean.

**Fail rule:** Any required field empty. Invalid enum value. owner_action_required missing.

**Owner approval required?** No — log entries are system records.

---

## TEST-08 — Handoff Creation

**Test ID:** TEST-08
**Purpose:** Verify that phase handoff files are complete, accurate, and contain the correct Codex review instructions and commit rule.

**Input files:**
- `handoff/PHASE_6_HANDOFF.md`
- `handoff/CURRENT_PHASE.md`
- `handoff/SESSION_SUMMARY.md`

**Steps:**
1. Open `handoff/PHASE_5_HANDOFF.md` — confirm all required sections: Phase name, Goal, Files Created, Scope Completed, Validation Checklist, Known Limitations, Codex Review Instructions, Next Phase Recommendation, Commit Instruction.
2. Confirm Codex Review Instructions lists specific checks (not just "review everything").
3. Confirm Commit Instruction states "do not commit until Codex PASS and Owner approval".
4. Open `handoff/CURRENT_PHASE.md` — confirm it shows Phase 6 as current phase.
5. Open `handoff/SESSION_SUMMARY.md` — confirm Phase 6 session block is the latest (top) entry.

**Expected output:** All handoff files are consistent, complete, and show Phase 6 as current.

**Pass rule:** All 9 sections present in PHASE_5_HANDOFF.md. Commit instruction correct. CURRENT_PHASE shows Phase 6.

**Fail rule:** Missing sections. No commit instruction. CURRENT_PHASE shows wrong phase.

**Owner approval required?** No — handoff files are internal.

---

## TEST-09 — Brand Brain Replacement Test

**Test ID:** TEST-09
**Purpose:** Verify that FnB OS V1 is brand-agnostic and can be used for a different F&B brand by swapping only the Brand Brain file.

**Input files:**
- `brand-brain/vi-cuon.md`
- `docs/12_OUTPUT_TEMPLATE_SYSTEM.md`

**Steps:**
1. Open `brand-brain/vi-cuon.md` — find "Replaceable Brand Context" section.
2. Confirm the section describes exactly how to replace for another brand (copy, rename, replace values, update brand_id).
3. Open `docs/12_OUTPUT_TEMPLATE_SYSTEM.md` — find "How Brand Brain Can Be Replaced" section.
4. Confirm the guide states: create new `brand-brain/[brand-slug].md`, update brand_id and brand_name in template outputs, keep all schema field names and enum values unchanged.
5. Open any template file (e.g., `templates/content-output-template.md`) — confirm `brand_id` and `brand_name` are `[TO_FILL]` placeholders, not hardcoded to `VQ` or `Vị Cuốn`.

**Expected output:** Brand replacement guide exists in both Brand Brain and docs. Templates use placeholders for brand fields.

**Pass rule:** Replacement guide exists in both files. Templates have `[TO_FILL]` for brand_id and brand_name.

**Fail rule:** No replacement guide. Templates hardcode `VQ` or `Vị Cuốn`.

**Owner approval required?** No — architecture test only.
