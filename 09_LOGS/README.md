# 09_LOGS — Log Templates

This folder contains templates for all log files used by n8n workflows and agents.

## Files

| File | Purpose |
|------|---------|
| `execution_log_template.md` | Template for workflow execution logs |
| `error_log_template.md` | Template for error logs |
| `approval_log_template.md` | Template for approval decision logs |

## Rules
- Templates are for human reference — actual logs go to Google Sheet (Phase 1+)
- Phase 0: manual log entries added to `06_HANDOFF/ERROR_LOG.md`
- Phase 1+: all logs written to Google Sheet tabs automatically
- Logs are append-only — never delete entries
- All logs use ISO8601 timestamps in `Asia/Ho_Chi_Minh` timezone
