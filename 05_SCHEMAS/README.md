# 05_SCHEMAS — JSON Schemas

All data objects passed between agents and written to Google Sheets or Google Drive are defined here.

## Files

| File | Object | Used By |
|------|--------|---------|
| `campaign_schema.json` | Campaign | n8n, all agents |
| `content_pack_schema.json` | Content Pack | Content Agent, QC Agent |
| `design_brief_schema.json` | Design Brief | Design Agent, QC Agent |
| `ads_pack_schema.json` | Ads Pack | Ads Agent, QC Agent |
| `crm_followup_schema.json` | CRM Message | CRM Agent, QC Agent |
| `comment_reply_schema.json` | Comment Reply | Reply Agent, QC Agent |
| `approval_schema.json` | Approval Request/Response | n8n, Telegram |
| `error_log_schema.json` | Error Log Entry | All agents, n8n |

## Rules
- All agent outputs MUST validate against the relevant schema before submission
- Schema versions are tracked in the `$schema_version` field
- Any schema change requires a DECISION_LOG entry and version bump
- Breaking changes require migration notes
