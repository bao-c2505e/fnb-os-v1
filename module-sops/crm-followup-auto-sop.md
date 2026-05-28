# CRM Follow-Up Auto SOP

**Module:** CRM Follow-Up Auto
**Agent:** CRM Follow-Up Agent (AGT-CRM)
**Schema:** `schemas/crm-followup.schema.json`
**Template:** `templates/crm-followup-template.md`
**Brand Reference:** `brand-brain/vi-cuon.md`

---

## Purpose

Guide the CRM Follow-Up Agent to draft customer follow-up message sequences for Zalo, Facebook Messenger, SMS, or email. All sequences require human review before any sending. No real customer messages are sent in Phase 4.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Brand Brain | `brand-brain/vi-cuon.md` | Yes |
| Lead segment | Owner brief | Yes |
| Customer status | Owner brief | Yes |
| Channel | Owner brief | Yes |
| Trigger event | Owner brief | Yes |
| Offer | Owner-provided or `[OWNER_TO_PROVIDE_OFFER]` | If offer-based sequence |

---

## Process Steps

1. Read `brand-brain/vi-cuon.md` — confirm brand tone, customer segment descriptions, and compliance rules.
2. Confirm lead segment, customer status, channel, and trigger event from input.
3. Draft message sequence with minimum 1 step.
4. Use `[CUSTOMER_NAME]` as the only personalization placeholder — do not store or use real customer data.
5. Add `delay` for each step (e.g., `Immediately`, `1 day`, `3 days`).
6. Write `recommended_timing` (e.g., weekdays 11am–1pm Vietnam time).
7. Set `human_review_required: true` — this is a schema constant and cannot be false.
8. Add opt-in compliance note in the `notes` field.
9. Fill all required fields from `schemas/crm-followup.schema.json`.
10. Set `approval_status: Draft`.
11. Set `created_by_agent: CRM Follow-Up Agent (AGT-CRM)`.
12. Output using `templates/crm-followup-template.md`.

---

## Output Template

`templates/crm-followup-template.md`

---

## Approval Gate

- `human_review_required` must always be `true` — hardcoded by schema `const: true`, cannot be overridden.
- No message is sent to any real customer without Owner `Approved` status.
- No real customer data (name, phone, order history) is stored in the output file.
- No messaging API is called in Phase 4.
- Opt-in compliance: output must note that all recipients must have opted in to receive messages.

---

## Logging Requirements

- Add one row to `logs/AGENT_ACTIVITY_LOG.md` per sequence produced.
- Use `templates/log-entry-template.md` format.

---

## Human Escalation Rules

Stop immediately and escalate to Owner (do not draft a message) if:
- Customer has requested to opt out or unsubscribe.
- Customer has expressed anger, distress, or made a complaint.
- Sequence contains pricing or promotional terms not confirmed by Owner.
- Message could be construed as spam or unsolicited commercial communication.
- Customer's communication channel or opt-in status is unclear.
- Any legal or regulatory concern is detected in the message content.

---

## Done Criteria

- All required schema fields filled.
- `human_review_required: true` confirmed in output.
- `approval_status` is `Draft` or `Ready for Review`.
- No customer PII stored in output file.
- No message sent to any channel.
- Opt-in compliance note present in `notes`.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
