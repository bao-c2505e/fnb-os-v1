# Data Source — n8n Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT — Not implemented. No workflow JSON. No connections.

---

## Purpose

Define all data sources that n8n workflows will read from and write to. This blueprint distinguishes between current repo-based sources (available now) and future runtime sources (to be connected in later phases). It also defines the credential placeholder rule and the source of truth hierarchy.

---

## Current Repo Data Sources

These sources exist in the repository and are available in all phases.

| Source | Path | Type | Contains |
|--------|------|------|---------|
| Brand Brain | `brand-brain/vi-cuon.md` | Markdown | Brand identity, voice, menu, audience, offers, visual style |
| Content schema | `schemas/content-output.schema.json` | JSON Schema | Output validation rules for content |
| Creative brief schema | `schemas/creative-brief.schema.json` | JSON Schema | Output validation for creative briefs |
| Ads pack schema | `schemas/ads-pack.schema.json` | JSON Schema | Output validation for ads packs |
| CRM followup schema | `schemas/crm-followup.schema.json` | JSON Schema | Output validation for CRM messages |
| Inbox reply schema | `schemas/comment-inbox-reply.schema.json` | JSON Schema | Output validation for inbox replies |
| Approval status schema | `schemas/approval-status.schema.json` | JSON Schema | Approval state machine rules |
| Log entry schema | `schemas/log-entry.schema.json` | JSON Schema | Log entry structure |
| Content template | `templates/content-output-template.md` | Markdown | Content draft template |
| Creative brief template | `templates/creative-brief-template.md` | Markdown | Creative brief template |
| Ads pack template | `templates/ads-pack-template.md` | Markdown | Ads pack template |
| CRM template | `templates/crm-followup-template.md` | Markdown | CRM message template |
| Inbox reply template | `templates/comment-inbox-reply-template.md` | Markdown | Inbox reply template |
| Sample outputs | `samples/vi-cuon/` | Markdown | Reference examples for all output types |
| Handoff files | `handoff/` | Markdown | Phase context, session summaries |
| Activity logs | `logs/AGENT_ACTIVITY_LOG.md` | Markdown | Build-phase audit trail |
| Phase logs | `09_LOGS/PHASE_LOG.md` | Markdown | Phase milestone records |

---

## Future Runtime Data Sources

These sources will be connected in future phases. All credentials are placeholders in Phase 7.

| Source | Platform | Purpose | Credential Placeholder |
|--------|----------|---------|----------------------|
| Content request input | Google Sheets | Owner submits content requests via sheet | `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` |
| Approval table | Google Sheets | Owner approves/rejects drafts via sheet | `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` |
| Log storage | Google Sheets | Runtime execution logs | `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` |
| Content request input | Supabase | Structured database for content requests (future) | `REPLACE_WITH_SUPABASE_CREDENTIAL` |
| Log storage | Supabase | Queryable log table (future) | `REPLACE_WITH_SUPABASE_CREDENTIAL` |
| Asset storage | Google Drive | Brand assets (photos, logos, videos) | `REPLACE_WITH_GOOGLE_DRIVE_CREDENTIAL` |
| Approval channel | Telegram | Owner approves via Telegram Bot | `REPLACE_WITH_TELEGRAM_BOT_TOKEN` |
| Publishing | Meta / Facebook / Instagram | Post publishing (future, requires Owner approval first) | `REPLACE_WITH_META_API_CREDENTIAL` |
| Video publishing | TikTok | Video publishing (future, requires Owner approval first) | `REPLACE_WITH_TIKTOK_API_CREDENTIAL` |
| Messaging | Zalo | CRM messages (future, requires Owner approval first) | `REPLACE_WITH_ZALO_API_CREDENTIAL` |

---

## Data Owner

The following data must be provided by the Owner (Bo Bao) before any runtime execution:

| Data Type | Current State | Owner Action Required |
|-----------|--------------|----------------------|
| Real menu prices | Placeholder `[OWNER_TO_PROVIDE_PRICE]` | Owner fills in `brand-brain/vi-cuon.md` |
| Restaurant address | Placeholder `[OWNER_TO_PROVIDE_ADDRESS]` | Owner fills in `brand-brain/vi-cuon.md` |
| Opening hours | Placeholder `[OWNER_TO_PROVIDE_HOURS]` | Owner fills in `brand-brain/vi-cuon.md` |
| Active offers | Placeholder `[OWNER_TO_PROVIDE_OFFER]` | Owner confirms each offer before use |
| Delivery area | Placeholder `[OWNER_TO_PROVIDE_DELIVERY_AREA]` | Owner confirms delivery zone |
| Brand photos | Not in repo | Owner provides real food photography |
| Approval channel | Not configured | Owner confirms Telegram or Sheet method |
| n8n instance URL | Not configured | Owner provides n8n instance URL |

---

## Credential Rule

**No real credentials, tokens, API keys, passwords, or webhook URLs may be stored in this repository.**

All credential references in blueprints and future workflows must use placeholder strings:
- `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL`
- `REPLACE_WITH_SUPABASE_CREDENTIAL`
- `REPLACE_WITH_GOOGLE_DRIVE_CREDENTIAL`
- `REPLACE_WITH_TELEGRAM_BOT_TOKEN`
- `REPLACE_WITH_META_API_CREDENTIAL`
- `REPLACE_WITH_TIKTOK_API_CREDENTIAL`
- `REPLACE_WITH_ZALO_API_CREDENTIAL`

Credentials are configured directly in the n8n credential manager — never in workflow JSON, never in repo files.

---

## Source of Truth Rule

| Data | Source of Truth | Notes |
|------|----------------|-------|
| System files (schemas, templates, SOPs, blueprints) | GitHub repository | All agents read from repo |
| Brand Brain (current) | `brand-brain/vi-cuon.md` in GitHub | Owner updates repo file |
| Runtime content requests | Google Sheets or Supabase (future) | Set up by Owner in runtime phase |
| Runtime execution logs | Google Sheets or Supabase (future) | Append-only; never delete |
| Approval decisions | Google Sheets or Telegram (future) | Owner makes decisions; logs are written immediately |
| Published content | Platform itself (Facebook, TikTok, Zalo) | External source of truth; not stored in repo |

---

## Done Criteria

This blueprint is complete when:

- [ ] All current repo data sources are listed with path and type
- [ ] All future runtime data sources are listed with platform and credential placeholder
- [ ] Owner data requirements are listed with current state and required action
- [ ] Credential rule is stated clearly
- [ ] Source of truth hierarchy is defined
- [ ] No real credentials stored
- [ ] No live connections created

---

_This is a design document only. Implementation in Phase 8._
