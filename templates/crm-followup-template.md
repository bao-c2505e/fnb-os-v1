# CRM Follow-Up Template

**Schema:** `schemas/crm-followup.schema.json`
**Agent:** CRM Follow-Up Agent (AGT-CRM)
**SOP:** `module-sops/crm-followup-auto-sop.md`

---

## sequence_id
[AUTO_GENERATED — Format: CRM-[BRAND]-[YYYYMMDD]-[NNN] — e.g., CRM-VQ-20260528-001]

## brand_id
[TO_FILL — Default: VQ for Vị Cuốn. Replace for other brands.]

## brand_name
[TO_FILL — Default: Vị Cuốn. Replace for other brands.]

## lead_segment
[TO_FILL — Select one: New Customer | Returning Customer | Lapsed Customer | VIP | Delivery Customer | Walk-in Customer]

## customer_status
[TO_FILL — Select one: New Lead | Active | At Risk | Lapsed | Churned | Unsubscribed]

## channel
[TO_FILL — Select one: Zalo | Facebook Messenger | SMS | Email | Telegram]

## trigger_event
[TO_FILL — Event that starts this sequence — e.g., "First order completed" or "No order in 30 days"]

## message_sequence

### Step 1
- **step:** 1
- **delay:** [TO_FILL — e.g., Immediately | 1 day | 3 days]
- **message_template:** [TO_FILL — Message text. Use [CUSTOMER_NAME] for personalization. No PII stored. Example: "Cảm ơn [CUSTOMER_NAME] đã ghé Vị Cuốn! Hẹn gặp lại bạn sớm nhé 🙂"]

### Step 2
- **step:** 2
- **delay:** [TO_FILL — e.g., 3 days after Step 1]
- **message_template:** [TO_FILL — Second message. Optional. Remove this step if sequence is 1 step only.]

### Step 3
- **step:** 3
- **delay:** [TO_FILL — e.g., 7 days after Step 2]
- **message_template:** [TO_FILL — Third message. Optional. Remove if not needed.]

## recommended_timing
[TO_FILL or null — Best send windows — e.g., "Weekdays 11am–1pm and 5pm–7pm (Vietnam time, GMT+7)"]

## human_review_required
true

## approval_status
Draft

## created_by_agent
CRM Follow-Up Agent (AGT-CRM)

## created_at
[AUTO_GENERATED — ISO 8601 datetime — e.g., 2026-05-28T09:00:00+07:00]

## notes
[TO_FILL — Required: include opt-in compliance note. Example: "All recipients in this sequence have opted in to receive messages via [channel]. Sequence complies with Zalo/SMS opt-in requirements. No PII stored."]

---

> **WARNING:** `human_review_required: true` — No message in this sequence may be sent to any real customer without Owner review and `approval_status: Approved`.
