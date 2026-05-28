# Comment Inbox Assistant SOP

**Module:** Comment Inbox Assistant
**Agent:** Comment Inbox Agent (AGT-Inbox)
**Schema:** `schemas/comment-inbox-reply.schema.json`
**Template:** `templates/comment-inbox-reply-template.md`
**Brand Reference:** `brand-brain/vi-cuon.md`

---

## Purpose

Guide the Comment Inbox Agent to classify incoming comments and inbox messages, then draft replies for Owner review. All replies require human review before posting. No auto-reply is executed. Escalation cases receive no draft reply — Owner handles them directly.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Brand Brain | `brand-brain/vi-cuon.md` | Yes |
| Customer message (verbatim) | Owner or platform export | Yes |
| Channel | Owner brief | Yes |

---

## Process Steps

1. Read `brand-brain/vi-cuon.md` — confirm brand tone and escalation rules before processing.
2. Copy customer message verbatim into `customer_message` — do not summarize, paraphrase, or modify.
3. Detect intent from allowed values: Menu Inquiry, Order Inquiry, Complaint, Compliment, Spam / Irrelevant, Sensitive / Legal, Price Inquiry, Location Inquiry, Other.
4. Assess sentiment from allowed values: Positive, Neutral, Negative, Angry, Unclear.
5. Apply escalation rules (see table below):
   - If escalation required: set `escalation_required: true`, set `draft_reply: null`, write `escalation_reason`.
   - If not escalated: draft reply in brand tone using Brand Brain voice guidelines.
6. Set `human_review_required: true` — always, regardless of escalation.
7. Fill all required fields from `schemas/comment-inbox-reply.schema.json`.
8. Set `approval_status: Draft`.
9. Set `created_by_agent: Comment Inbox Agent (AGT-Inbox)`.
10. Output using `templates/comment-inbox-reply-template.md`.

---

## Output Template

`templates/comment-inbox-reply-template.md`

---

## Escalation Rules

| Trigger | Action |
|---------|--------|
| Sentiment: Angry | `escalation_required: true` — `draft_reply: null` |
| Intent: Complaint | `escalation_required: true` — `draft_reply: null` |
| Intent: Sensitive / Legal | `escalation_required: true` — `draft_reply: null` |
| Unclear message + ambiguous risk | `escalation_required: true` — `draft_reply: null` |
| Refund or return request | `escalation_required: true` — `draft_reply: null` |
| Food safety or health complaint | `escalation_required: true` — `draft_reply: null` |
| Legal demand or regulatory mention | `escalation_required: true` — `draft_reply: null` |

---

## Approval Gate

- `human_review_required` is always `true` — hardcoded by schema `const: true`.
- No reply is ever posted without Owner review and `Approved` status.
- No auto-reply API is called in Phase 4.
- Escalation cases: `draft_reply` must be `null` — never draft a reply for escalation cases.

---

## Logging Requirements

- Add one row to `logs/AGENT_ACTIVITY_LOG.md` per reply draft or escalation output.
- Use `templates/log-entry-template.md` format.

---

## Human Escalation Rules

Owner must handle the following cases directly — agent produces escalation record only:
- Angry customers: Owner responds personally to de-escalate.
- Complaints: Owner investigates and responds with authority.
- Sensitive or legal messages: Owner consults with legal/relevant party before responding.
- Refund or return requests: Owner makes the decision on outcome before any reply.
- Food safety issues: Owner handles with full information about the specific incident.
- Unclear cases where a wrong reply could damage brand or customer relationship.

---

## Done Criteria

- Customer message copied verbatim into `customer_message`.
- `human_review_required: true` confirmed in output.
- Escalation rules applied correctly.
- If escalated: `draft_reply` is `null` and `escalation_reason` is written.
- `approval_status` is `Draft` or `Ready for Review`.
- No reply posted, sent, or scheduled.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
