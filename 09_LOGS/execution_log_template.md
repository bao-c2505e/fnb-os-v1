# Execution Log Template

## Format (for Google Sheet `Execution Log` tab)

Each workflow execution step writes one row:

| Field | Value |
|-------|-------|
| log_id | VQ-LOG-[YYYYMMDD]-[SEQ] |
| workflow_id | WF-[XX] |
| workflow_name | Human-readable workflow name |
| execution_id | n8n execution ID |
| step | Step name (e.g., "read_campaign", "call_content_agent") |
| status | success / failed / skipped |
| input_summary | Short description of inputs |
| output_summary | Short description of outputs |
| duration_ms | Execution time in milliseconds |
| message | Log message or error details |
| timestamp | ISO8601 in Asia/Ho_Chi_Minh |

---

## Example Log Entry

```
log_id: VQ-LOG-20260601-001
workflow_id: WF-01
workflow_name: Content Generation
execution_id: n8n-exec-abc123
step: read_campaign
status: success
input_summary: Campaign VQ-CAMP-20260601-001 (Combo Trưa)
output_summary: Campaign data loaded, 1 row
duration_ms: 234
message: Campaign data read successfully from Google Sheet
timestamp: 2026-06-01T11:00:01+07:00
```

---

## Log Aggregation

Daily summary reads Execution Log to count:
- Total workflow runs
- Success rate
- Average duration per workflow
- Most common failure steps
