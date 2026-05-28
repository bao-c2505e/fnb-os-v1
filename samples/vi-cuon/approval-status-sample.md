# Approval Status Samples — Vị Cuốn

**Phase:** 5 — Sample Outputs
**Agent:** Approval Publishing Agent (AGT-Approval)
**Schema:** `schemas/approval-status.schema.json`
**Template:** `templates/approval-status-template.md`
**SOP:** `module-sops/approval-publishing-sop.md`

> **Note:** All samples in Phase 5 are kept at `Draft` or `Ready for Review`. Nothing is marked `Approved`, `Published`, or `Scheduled` in this sample set — these states require Owner action.

---

## Approval Record 1 — Content Output

### item_id
CC-VQ-20260528-001

### item_type
Content Output

### approval_status
Draft

### owner_decision
null

### reviewer
null

### review_notes
null

### approved_at
null

### scheduled_at
null

### published_at
null

### change_log

**Entry 1**
- **timestamp:** 2026-05-28T09:00:00+07:00
- **from_status:** null
- **to_status:** Draft
- **by:** Content Agent (AGT-Content)
- **note:** Initial creation of Facebook feed post sample (Bánh Tráng Cuốn Thịt Heo — lunch occasion).

---

## Approval Record 2 — Creative Brief

### item_id
CB-VQ-20260528-001

### item_type
Creative Brief

### approval_status
Ready for Review

### owner_decision
null

### reviewer
null

### review_notes
null

### approved_at
null

### scheduled_at
null

### published_at
null

### change_log

**Entry 1**
- **timestamp:** 2026-05-28T10:00:00+07:00
- **from_status:** null
- **to_status:** Draft
- **by:** Creative Asset Agent (AGT-Creative)
- **note:** Initial creation of food photo brief for Facebook.

**Entry 2**
- **timestamp:** 2026-05-28T10:05:00+07:00
- **from_status:** Draft
- **to_status:** Ready for Review
- **by:** Creative Asset Agent (AGT-Creative)
- **note:** Self-check passed — all required fields filled, no prices hardcoded, no false claims, QA checklist populated. Pending Owner review before handing to photographer.

---

## Approval Record 3 — Ads Pack

### item_id
AP-VQ-20260528-001

### item_type
Ads Pack

### approval_status
Draft

### owner_decision
null

### reviewer
null

### review_notes
null

### approved_at
null

### scheduled_at
null

### published_at
null

### change_log

**Entry 1**
- **timestamp:** 2026-05-28T11:00:00+07:00
- **from_status:** null
- **to_status:** Draft
- **by:** Ads Pack Agent (AGT-Ads)
- **note:** Initial creation of TOF awareness ad for Facebook. Offer pending Owner confirmation. No campaign setup at this stage.

---

## Approval Record 4 — CRM Follow-Up Sequence

### item_id
CRM-VQ-20260528-001

### item_type
CRM Follow-Up

### approval_status
Draft

### owner_decision
null

### reviewer
null

### review_notes
null

### approved_at
null

### scheduled_at
null

### published_at
null

### change_log

**Entry 1**
- **timestamp:** 2026-05-28T12:00:00+07:00
- **from_status:** null
- **to_status:** Draft
- **by:** CRM Follow-Up Agent (AGT-CRM)
- **note:** Initial creation of new lead inquiry sequence (Facebook Messenger, 3 steps). human_review_required: true. Price and offer placeholders present — Owner must confirm before approval.

---

## Approval Record 5 — Comment Reply Draft

### item_id
IR-VQ-20260528-001

### item_type
Comment Reply

### approval_status
Ready for Review

### owner_decision
null

### reviewer
null

### review_notes
null

### approved_at
null

### scheduled_at
null

### published_at
null

### change_log

**Entry 1**
- **timestamp:** 2026-05-28T13:00:00+07:00
- **from_status:** null
- **to_status:** Draft
- **by:** Comment Inbox Agent (AGT-Inbox)
- **note:** Initial creation of menu question reply draft (Facebook Comment). human_review_required: true. escalation_required: false.

**Entry 2**
- **timestamp:** 2026-05-28T13:02:00+07:00
- **from_status:** Draft
- **to_status:** Ready for Review
- **by:** Comment Inbox Agent (AGT-Inbox)
- **note:** Self-check passed — customer message copied verbatim, no auto-escalation required, draft reply in brand tone, price placeholder present. Pending Owner review.
