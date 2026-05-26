# Error Log — FnB OS V1

All errors are recorded here. Append only — never delete.
Also write errors to Google Sheet `Error Log` tab (Phase 1+).

---

## Log Format

```
## [ERR-ID] — [Short Description]
**Date:** YYYY-MM-DD HH:MM
**Agent:** [Agent Name]
**Phase:** [Phase]
**Severity:** Low | Medium | High | Critical
**Status:** Open | In Review | Resolved | Ignored

### Error
[What happened]

### Context
[What the agent was doing when the error occurred]

### Impact
[What was affected]

### Resolution
[How it was fixed, or N/A if unresolved]
```

---

## Active Errors

*No errors logged yet.*

---

## Resolved Errors

*No errors resolved yet.*

---

## Error Code Reference

| Code | Meaning |
|------|---------|
| SHEETS_READ_FAIL | Could not read from Google Sheets |
| SHEETS_WRITE_FAIL | Could not write to Google Sheets |
| DRIVE_UPLOAD_FAIL | Could not upload to Google Drive |
| API_TIMEOUT | External API call timed out |
| API_AUTH_FAIL | Authentication failed for external API |
| SCHEMA_INVALID | Agent output failed schema validation |
| QC_MAX_RETRY | QC failed after 3 regeneration attempts |
| TELEGRAM_FAIL | Could not send Telegram message |
| ESCALATION_MISSED | Escalation not handled within SLA |
| PROMPT_OVERLOAD | Agent prompt exceeded token limit |
| AGENT_ERROR | Agent returned error status |
