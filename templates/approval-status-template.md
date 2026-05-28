# Approval Status Template

**Schema:** `schemas/approval-status.schema.json`
**Agent:** Approval Publishing Agent (AGT-Approval)
**SOP:** `module-sops/approval-publishing-sop.md`

---

## item_id
[TO_FILL — ID of the item being tracked. References content_id, brief_id, ads_pack_id, sequence_id, or reply_id — e.g., CC-VQ-20260528-001]

## item_type
[TO_FILL — Select one: Content Output | Creative Brief | Ads Pack | CRM Follow-Up | Comment Reply]

## approval_status
[TO_FILL — Select one: Draft | Ready for Review | Needs Revision | Approved | Rejected | Scheduled | Published
- Default on creation: Draft
- Only Owner may set: Approved
- Scheduled and Published require prior Approved + approved_at]

## owner_decision
[TO_FILL or null — Select one: Approved | Rejected | Needs Revision | null
- null if no Owner decision yet
- Only Owner may set Approved]

## reviewer
[TO_FILL or null — Name or ID of reviewer who checked before Owner — e.g., "Codex (AGT-03)". Set to null if not yet reviewed.]

## review_notes
[TO_FILL or null — Reviewer notes. Required if owner_decision is Needs Revision or Rejected. Set to null otherwise.]

## approved_at
[TO_FILL or null — ISO 8601 datetime when Owner set Approved — e.g., 2026-05-28T10:00:00+07:00. Required before Scheduled or Published can be set. Set to null if not yet approved.]

## scheduled_at
[TO_FILL or null — ISO 8601 datetime scheduled for publishing. Requires prior Approved state and non-null approved_at. Set to null if not scheduled.]

## published_at
[TO_FILL or null — ISO 8601 datetime when item was published. Requires prior Approved state and non-null approved_at. Set to null if not published.]

## change_log

### Entry 1
- **timestamp:** [AUTO_GENERATED — ISO 8601 datetime]
- **from_status:** [TO_FILL — e.g., null (initial creation)]
- **to_status:** Draft
- **by:** [TO_FILL — Agent or human who created this item]
- **note:** [TO_FILL or null — Optional context for this transition]

### Entry 2
- **timestamp:** [TO_FILL — ISO 8601 datetime]
- **from_status:** Draft
- **to_status:** Ready for Review
- **by:** [TO_FILL — Agent name]
- **note:** [TO_FILL or null]

### Entry 3
- **timestamp:** [TO_FILL — ISO 8601 datetime]
- **from_status:** Ready for Review
- **to_status:** [TO_FILL — e.g., Approved | Needs Revision | Rejected]
- **by:** [TO_FILL — Owner or Reviewer name]
- **note:** [TO_FILL or null]

---

> **RULES:** Published and Scheduled require Approved + approved_at. Only Owner may set Approved. No automation publishes in Phase 4.
