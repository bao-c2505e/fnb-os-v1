# Error Log Template

## Format (for Google Sheet `Error Log` tab)

| Field | Value |
|-------|-------|
| error_id | VQ-ERR-[YYYYMMDD]-[SEQ] |
| workflow_id | WF-[XX] |
| execution_id | n8n execution ID |
| agent | Agent or system that produced the error |
| error_code | Short code (e.g., SHEETS_WRITE_FAIL) |
| error_message | Full error message |
| severity | low / medium / high / critical |
| context | JSON string with relevant context |
| suggested_action | What to do next |
| status | open / in_review / resolved / ignored |
| resolved_by | Agent or person who resolved |
| occurred_at | ISO8601 timestamp |
| resolved_at | ISO8601 timestamp (if resolved) |

---

## Example Error Entry

```
error_id: VQ-ERR-20260601-001
workflow_id: WF-01
agent: n8n (Content Generation)
error_code: SHEETS_WRITE_FAIL
error_message: Error: 403 Forbidden — service account does not have write access
severity: high
context: {"sheet_id": "...", "tab": "Content Packs", "row": {...}}
suggested_action: Check service account permissions on Google Sheet
status: open
occurred_at: 2026-06-01T11:05:23+07:00
```

---

## Severity Guide

| Severity | Meaning | Response SLA |
|----------|---------|-------------|
| critical | System stopped, data loss risk | Immediate |
| high | Major feature broken | Within 1 hour |
| medium | Degraded but workaround exists | Within 4 hours |
| low | Minor issue, non-blocking | Next working day |
