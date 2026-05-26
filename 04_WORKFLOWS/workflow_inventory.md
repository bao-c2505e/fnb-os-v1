# Workflow Inventory — FnB OS V1

## Status Legend
- PLANNED — Not yet built
- DRAFT — JSON file created, not imported to n8n
- STAGED — Imported to n8n, not activated
- ACTIVE — Running in production
- PAUSED — Suspended
- DEPRECATED — No longer used

---

## Workflows

| ID | Name | File | Phase | Status | Description |
|----|------|------|-------|--------|-------------|
| WF-01 | Content Generation | `01_content_generation_v1.json` | 3 | PLANNED | Reads campaign, calls Content Agent, writes content pack |
| WF-02 | Design Brief Generation | `02_design_brief_v1.json` | 3 | PLANNED | Reads content pack, calls Design Agent, writes brief |
| WF-03 | Ads Pack Generation | `03_ads_pack_v1.json` | 3 | PLANNED | Reads campaign, calls Ads Agent, writes ads pack |
| WF-04 | CRM Follow-up | `04_crm_followup_v1.json` | 3 | PLANNED | Reads CRM, calls CRM Agent, sends messages |
| WF-05 | Comment Reply | `05_comment_reply_v1.json` | 3 | PLANNED | Receives webhook, classifies, replies or escalates |
| WF-06 | Telegram Approval Gate | `06_approval_gate_v1.json` | 3 | PLANNED | Sends approval requests, handles responses |
| WF-07 | Daily Summary | `07_daily_summary_v1.json` | 3 | PLANNED | Aggregates data, sends Telegram summary |
| WF-08 | QC Agent | `08_qc_agent_v1.json` | 3 | PLANNED | Reviews all agent outputs before approval |
| WF-09 | Error Alert | `09_error_alert_v1.json` | 3 | PLANNED | Monitors for errors, sends Telegram alert |
| WF-10 | Campaign Intake | `10_campaign_intake_v1.json` | 3 | PLANNED | Detects new campaign rows, triggers generation |

---

## Trigger Map

| Workflow | Trigger Type | Schedule / Event |
|----------|-------------|-----------------|
| WF-01 | Google Sheets poll | Every hour |
| WF-02 | Webhook from WF-01 | On content pack creation |
| WF-03 | Google Sheets poll | Every hour |
| WF-04 | Schedule | Daily at [FILL: time] |
| WF-05 | Platform Webhook | On new comment/message |
| WF-06 | Webhook | On approval request |
| WF-07 | Schedule | Daily at [FILL: time] |
| WF-08 | Webhook | On any agent output |
| WF-09 | Schedule | Every 15 minutes |
| WF-10 | Google Sheets poll | Every 30 minutes |

---

## Notes
- All workflows must be tested with fixtures in `07_TEST_FIXTURES/` before activation
- No workflow is activated until Phase 4 dry run is complete and user approves
