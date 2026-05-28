# Comment Inbox Reply Template

**Schema:** `schemas/comment-inbox-reply.schema.json`
**Agent:** Comment Inbox Agent (AGT-Inbox)
**SOP:** `module-sops/comment-inbox-assistant-sop.md`

---

## reply_id
[AUTO_GENERATED — Format: IR-[BRAND]-[YYYYMMDD]-[NNN] — e.g., IR-VQ-20260528-001]

## brand_id
[TO_FILL — Default: VQ for Vị Cuốn. Replace for other brands.]

## brand_name
[TO_FILL — Default: Vị Cuốn. Replace for other brands.]

## channel
[TO_FILL — Select one: TikTok Comment | Instagram Comment | Facebook Comment | Facebook Messenger | Zalo | Google Review]

## customer_message
[TO_FILL — Paste customer message VERBATIM. Do not summarize, paraphrase, or modify. Preserve original text exactly as received.]

## detected_intent
[TO_FILL — Select one: Menu Inquiry | Order Inquiry | Complaint | Compliment | Spam / Irrelevant | Sensitive / Legal | Price Inquiry | Location Inquiry | Other]

## sentiment
[TO_FILL — Select one: Positive | Neutral | Negative | Angry | Unclear]

## draft_reply
[TO_FILL or null —
- If escalation_required is true: set to null. Do NOT draft a reply.
- If not escalated: write reply in brand tone from brand-brain/vi-cuon.md. Warm, helpful, on-brand.]

## escalation_required
[TO_FILL — true or false.
- true: Angry | Complaint | Sensitive/Legal | Unclear risk | Refund | Food safety | Legal demand
- false: All other cases where a draft reply is appropriate]

## escalation_reason
[TO_FILL or null —
- Required if escalation_required is true: explain why Owner must handle this directly.
- Set to null if escalation_required is false.]

## human_review_required
true

## approval_status
Draft

## created_by_agent
Comment Inbox Agent (AGT-Inbox)

## created_at
[AUTO_GENERATED — ISO 8601 datetime — e.g., 2026-05-28T09:00:00+07:00]

## notes
[TO_FILL or null — Optional notes for Owner or Reviewer. Flag any unusual context or suggested Owner action.]

---

> **WARNING:** `human_review_required: true` — No reply may be posted or sent to any customer without Owner review and `approval_status: Approved`. Escalation cases must be handled by Owner directly.
