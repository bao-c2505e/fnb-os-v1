# Logging — n8n Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT — Not implemented. No workflow JSON. No execution.

---

## Purpose

Define how every agent action, workflow execution, approval decision, and error event must be logged. Logging provides an audit trail that supports Owner oversight, Codex review, and debugging. Logs are the authoritative record of what happened — screenshots are NOT a substitute for logs.

---

## Log Schema Reference

All log entries must conform to the following:

| File | Purpose |
|------|---------|
| `schemas/log-entry.schema.json` | JSON schema defining all required log fields and types |
| `templates/log-entry-template.md` | Markdown template for manual log entries in build phases |

---

## What to Log

Every workflow execution and agent action must produce a log entry with the following fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `log_id` | string | yes | Unique identifier. Example: `LOG-20260528-001` |
| `timestamp` | string (ISO 8601) | yes | Date and time of action |
| `phase` | string | yes | Phase number. Example: `7` |
| `agent` | string | yes | Agent or module that produced the output. Example: `content-agent`, `n8n-content-auto` |
| `input_ref` | string | yes | Reference to input file, request ID, or sheet row |
| `output_ref` | string | yes | Reference to output file, draft ID, or approval record |
| `approval_status` | string | yes | Current approval state. Must be one of the 7 defined states |
| `errors` | array | yes | List of errors encountered. Empty array `[]` if none |
| `owner_action_required` | boolean | yes | `true` if Owner must take an action before workflow continues |
| `next_action` | string | yes | What happens next. Example: `send to approval queue`, `await Owner review` |

Additional optional fields defined in `schemas/log-entry.schema.json`.

---

## Screenshot Rule

**Screenshots do not replace logs.**

A screenshot of an output, a chat message, or a tool response is NOT a valid log entry. Every action must be recorded in a structured log file or table. Screenshots may be used as supplementary reference only, never as the primary audit record.

---

## Future Log Destinations

Logs are stored in different locations depending on the phase:

| Phase | Destination | Format | Notes |
|-------|------------|--------|-------|
| Build phases (1–7) | `logs/AGENT_ACTIVITY_LOG.md` | Markdown table | Append-only; one row per agent session |
| Build phases (1–7) | `09_LOGS/PHASE_LOG.md` | Markdown entries | One entry per phase milestone |
| Runtime phases (8+) | Google Sheets log tab | Spreadsheet rows | One row per execution; requires Google Sheets credential (placeholder) |
| Runtime phases (8+) | Supabase `logs` table | Database rows | Structured; queryable; requires Supabase credential (placeholder) |
| n8n execution | n8n Execution Log | n8n built-in | Visible in n8n dashboard; not exported to repo |

---

## Future n8n Node Plan

The following node sequence describes how logging will be implemented in n8n workflows. These nodes will appear in every workflow that produces an output.

| Step | Node Type | Node Name | Action |
|------|-----------|-----------|--------|
| 1 | Set | Prepare Log Entry | Assemble log fields: log_id, timestamp, phase, agent, input_ref, output_ref, approval_status |
| 2 | Function / Code | Validate Log Fields | Check all required fields present and non-empty |
| 3 | Google Sheets / Supabase | Write Log to Destination | Append log row to Google Sheet or Supabase table |
| 4 | If | Check Write Success | If write fails, route to error log handler |
| 5 | Error Handler | Log Write Failure | Write fallback error note to n8n execution log; set `owner_action_required: true` |

---

## Error Log Handling

When an error occurs anywhere in a workflow, an error log entry must be created immediately:

- `errors` field must contain the error type, message, and step where it occurred.
- `approval_status` must be set to `Draft` or remain unchanged — never advance on error.
- `owner_action_required` must be `true` when the error blocks the workflow.
- `next_action` must describe what the Owner or agent must do to resolve.

No workflow may continue past a blocking error without first creating an error log entry.

---

## Done Criteria

This blueprint is complete when:

- [ ] Log schema reference files are listed
- [ ] All required log fields are defined with type and description
- [ ] Screenshot-as-log prohibition is stated
- [ ] All future log destinations are listed with format and credential note
- [ ] n8n node plan covers prepare, validate, write, check, error-handler steps
- [ ] Error log handling requirements are defined
- [ ] No real n8n JSON created
- [ ] No credentials stored

---

_This is a design document only. Implementation in Phase 8._
