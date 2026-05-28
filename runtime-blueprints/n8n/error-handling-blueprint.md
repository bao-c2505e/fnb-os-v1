# Error Handling — n8n Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT — Not implemented. No workflow JSON. No execution.

---

## Purpose

Define how all n8n workflows must respond to errors, failures, and unsafe conditions. The core principle: when in doubt, stop and log. Never continue past a blocking error to publish, send to customers, or spend money.

---

## Error Types

| Error Type | Description | Blocking? |
|-----------|-------------|-----------|
| Missing brand data | Brand Brain file not found or required field is empty placeholder | Yes |
| Invalid schema output | AI-generated output fails validation against JSON schema | Yes |
| Missing approval | Workflow attempts to publish/send/spend without `approval_status: Approved` | Yes |
| Credential missing | n8n credential not configured or expired | Yes |
| API failure | External API (Google Sheets, Telegram, Meta, TikTok, Zalo) returns error | Yes |
| Rate limit | API rate limit reached; request throttled or rejected | Conditional |
| File upload failure | Asset (photo, video) fails to upload to platform or Drive | Yes |
| Publishing blocked | Platform rejects publish request (policy, format, credential) | Yes |
| Timeout | Approval wait exceeds configured timeout | Yes |
| Duplicate request | Same content request submitted twice | Warning only |
| Missing Owner data | Required Owner-provided field still contains placeholder value | Yes |

---

## Required Behavior

For all blocking errors, the workflow MUST:

| Required Action | Detail |
|----------------|--------|
| Stop unsafe execution | Immediately halt the current workflow step; do not proceed to next node |
| Write error log | Create a log entry with `errors` field populated; include error type, message, step |
| Set owner_action_required | Set `owner_action_required: true` in log and output record |
| Create handoff note | Write a note to `handoff/SESSION_SUMMARY.md` or equivalent if the error requires Owner action |
| Notify Owner if needed | For critical errors, send notification via Telegram (future) or mark output for Owner review |
| Never continue to publish | Under no circumstances proceed to publish, reply to customers, or spend budget if a blocking error exists |
| Never continue to reply | Do not send any customer-facing message if an error has occurred |
| Never continue to spend | Do not commit any ads budget if an error has occurred |

For rate limit errors:
- If retry is safe: wait and retry with exponential backoff (max 3 attempts).
- If retry fails: treat as blocking error.

---

## Future n8n Error Node Plan

Every workflow must include the following error handling infrastructure:

| Step | Node Type | Node Name | Action |
|------|-----------|-----------|--------|
| E1 | Error Trigger | Catch Workflow Error | Activated when any node in workflow fails |
| E2 | Set | Prepare Error Log | Assemble error log fields: error type, message, step, timestamp |
| E3 | Function / Code | Classify Error | Determine if error is blocking or warning only |
| E4 | Google Sheets / Supabase | Write Error Log | Append error record to log destination |
| E5 | If | Check Notification Required | Is `owner_action_required: true`? |
| E6 | Telegram / HTTP Request | Notify Owner | Send error summary to Owner (if notification required) |
| E7 | Stop and Error | Halt Workflow | End workflow execution; mark run as failed in n8n execution log |

This error node plan must be included in every workflow built in Phase 8 and beyond.

---

## Specific Error Rules

### Missing Approval — HARD BLOCK

```
IF approval_status != "Approved"
  AND action == ("publish" OR "send" OR "spend")
THEN
  STOP immediately
  Write error log: "MISSING_APPROVAL — action blocked"
  Set owner_action_required: true
  Do NOT proceed
```

This rule cannot be bypassed by any agent or automation.

### Missing Credential — HARD BLOCK

```
IF credential == null OR credential == "REPLACE_WITH_*"
THEN
  STOP immediately
  Write error log: "CREDENTIAL_MISSING — [credential_name]"
  Set owner_action_required: true
  Notify Owner
```

### Invalid Schema Output

```
IF output fails schema validation
THEN
  STOP workflow
  Write error log: "SCHEMA_VALIDATION_FAIL — [field list]"
  Return output to revision queue with error details
  Do NOT send to approval queue
```

### API Failure

```
IF external API returns error (4xx or 5xx)
THEN
  Attempt retry if rate limit (429): wait exponential backoff, max 3 attempts
  For all other errors: STOP
  Write error log: "API_FAILURE — [service] — [status code] — [message]"
  Set owner_action_required: true
```

---

## Done Criteria

This blueprint is complete when:

- [ ] All error types are listed with blocking classification
- [ ] All required behaviors for blocking errors are defined
- [ ] Screenshot-as-log prohibition is upheld (logs required for errors)
- [ ] n8n error node plan is defined (Error Trigger through Halt)
- [ ] Specific rules for Missing Approval, Missing Credential, Invalid Schema, API Failure are written
- [ ] No-publish / no-reply / no-spend rule for errors is explicitly stated
- [ ] No real n8n JSON created
- [ ] No credentials stored

---

_This is a design document only. Implementation in Phase 8._
