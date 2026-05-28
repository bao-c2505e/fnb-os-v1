# n8n Runtime Rules — FnB OS V1

Version: 1.0
Date: 2026-05-28
Authority: ChatGPT (Chief Architect)
Executed by: n8n (AGT-05) after Owner approval

n8n is the Runtime Automation layer. It executes approved workflows.
It does not make approval decisions and does not self-activate.

---

## 1. Workflow File Requirements

Every n8n workflow in this project must comply with all of the following:

| Requirement | Detail |
|-------------|--------|
| Importable JSON | File must be valid n8n export format (`.json`), importable via n8n UI without manual edits |
| `active: false` | Every workflow JSON must have `"active": false` at the root — never `true` |
| Placeholder credentials | All credential fields must use placeholder values — never real tokens or passwords |
| Approval gate | Every workflow must include an explicit approval gate step before any external action |
| Log step | Every workflow must include a log step that writes execution metadata to `logs/` by default, unless the Owner-approved command explicitly names another log destination |
| Stored in `n8n/` | All workflow JSON files live in `D:\FNB_OS_V1\n8n\` |
| README entry | Every workflow must be listed in `04_WORKFLOWS/workflow_inventory.md` with status, trigger, and owner |

---

## 2. Approval Gate Standard

Every workflow that sends a message, posts content, triggers an ad, or modifies external state must include an approval gate node before the action node.

Reference implementation: `docs/phase-2/approval-gate-standard.md`

Minimum approval gate requirements:
- Sends a Telegram (or equivalent) message to the Owner with the proposed action and payload.
- Waits for an explicit approval response (`APPROVE` / `REJECT`).
- Proceeds only on `APPROVE`.
- On `REJECT` or timeout: stops execution and logs the rejection.
- Gate must be visible in the workflow canvas — not hidden in a sub-workflow.

---

## 3. Credential Handling in Workflows

| Credential Type | Required Value in JSON |
|----------------|----------------------|
| Telegram Bot Token | `REPLACE_WITH_TELEGRAM_BOT_TOKEN` |
| OpenAI API Key | `REPLACE_WITH_OPENAI_API_KEY` |
| Google Sheets API | `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL_ID` |
| Airtable API | `REPLACE_WITH_AIRTABLE_API_KEY` |
| Any other credential | `REPLACE_WITH_[SERVICE]_[TYPE]` |

Real credentials are set in n8n's credential manager after import — never in the JSON file.

---

## 4. Log Step Specification

Every workflow must contain a log step that captures:

```json
{
  "workflow_id": "{{$workflow.id}}",
  "workflow_name": "{{$workflow.name}}",
  "execution_id": "{{$execution.id}}",
  "timestamp": "{{$now.toISO()}}",
  "trigger": "{{$trigger.type}}",
  "status": "started | completed | rejected | error",
  "payload_summary": "{{short description of what was processed}}"
}
```

Log destination: write to `logs/` by default. A different destination may only be used if the Owner-approved command explicitly names it. Screenshots are not a substitute for required log files.

---

## 5. Workflow Activation Protocol

Workflows must never be activated without Owner approval. The activation sequence is:

1. Builder creates workflow JSON in `n8n/` with `active: false`.
2. Reviewer (Codex) confirms `active: false` and placeholder credentials.
3. Owner approves via `OWNER_APPROVED` on the command.
4. Owner (or designated operator) imports the JSON into n8n UI.
5. Owner manually sets credentials in n8n credential manager.
6. Owner manually tests the workflow in n8n UI (manual trigger).
7. Owner manually toggles `active: true` in n8n UI after successful test.

**No agent may set `active: true` in the JSON file or via API.**

---

## 6. Workflow Naming Convention

```
[module]-[action]-[version].json

Examples:
  content-approval-gate-v1.json
  comment-reply-router-v1.json
  daily-summary-report-v1.json
  crm-followup-trigger-v1.json
```

---

## 7. Prohibited Workflow Actions

n8n workflows must never:

- Auto-post to TikTok, Facebook, Instagram, or any social platform without approval gate.
- Auto-reply to real customers without approval gate.
- Create or modify ad campaigns or budgets.
- Access production databases directly.
- Call external APIs with real credentials stored in the JSON file.
- Send messages to customers during testing (use test accounts or mock endpoints).

---

## 8. Workflow Inventory

Every workflow must be registered in `04_WORKFLOWS/workflow_inventory.md` with:

| Field | Value |
|-------|-------|
| `workflow_id` | File name without extension |
| `status` | `draft` / `review` / `approved` / `active` / `deprecated` |
| `trigger` | `manual` / `webhook` / `schedule` / `event` |
| `approver` | Owner name and date |
| `last_tested` | Date of last manual test |
| `n8n_path` | Path within n8n/ directory |
