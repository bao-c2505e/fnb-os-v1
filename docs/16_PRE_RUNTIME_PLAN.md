# 16 — Pre-Runtime Plan

**Phase:** 6 — OS Readiness Pack
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Purpose:** Define what is ready, what is not, and what needs to happen before n8n runtime automation is built in Phase 7.

---

## What Is Ready (Phases 1–5)

| Component | Status | Location |
|-----------|--------|----------|
| Repo governance (CLAUDE.md, AGENTS.md, commands) | Ready | `CLAUDE.md`, `agents/`, `commands/` |
| Agent role definitions (9 agents) | Ready | `agents/*.md` |
| Brand Brain — Vị Cuốn | Partially ready | `brand-brain/vi-cuon.md` |
| JSON Schema contracts (7 marketing schemas) | Ready | `schemas/*.schema.json` |
| Module SOPs (6 modules) | Ready | `module-sops/*.md` |
| Output templates (7 templates) | Ready | `templates/*.md` |
| Sample outputs (7 sample files) | Ready | `samples/vi-cuon/*.md` |
| Approval state machine (7 states) | Ready | `schemas/approval-status.schema.json`, `module-sops/approval-publishing-sop.md` |
| Logging structure | Ready | `logs/`, `09_LOGS/`, `templates/log-entry-template.md` |
| Handoff system | Ready | `handoff/` |
| Safety rules (no auto-post, no auto-reply, no ads spend) | Ready | All agent files, SOPs, templates |

---

## What Is Not Ready

### Missing Brand Data (Owner Action Required)

| Data | Placeholder Used | Impact |
|------|-----------------|--------|
| Exact dish prices | `[OWNER_TO_PROVIDE_PRICE]` | Content, CRM, inbox replies cannot include real pricing |
| Physical address | `[OWNER_TO_PROVIDE_ADDRESS]` | Inbox replies, video overlays, CRM messages cannot include location |
| Opening hours | `[OWNER_TO_PROVIDE_OPENING_HOURS]` | Inbox replies, CRM messages incomplete |
| Combo / offer details | `[OWNER_TO_PROVIDE_OFFER]` | Content, ads, CRM cannot include real promotions |
| Delivery app names | `[OWNER_TO_PROVIDE]` | Inbox delivery replies incomplete |
| Delivery coverage area | `[OWNER_TO_PROVIDE_DELIVERY_AREA]` | Ads pack and inbox delivery replies incomplete |
| Facebook page link / ordering link | `[OWNER_TO_PROVIDE]` | CTAs in content and ads incomplete |
| Brand imagery (real food photos) | Not yet provided | Creative briefs require Owner to supply |
| Group booking policy | `[OWNER_TO_PROVIDE]` | Booking inbox reply incomplete |

### Infrastructure Not Yet Built

| Component | Phase |
|-----------|-------|
| n8n workflow automation | Phase 7 |
| Approval routing workflow (Draft → Approved → Published) | Phase 7 |
| Content trigger workflow (brief → agent → output) | Phase 7 |
| CRM sequence execution via Zalo/Messenger API | Phase 8+ |
| Comment inbox monitoring and reply automation | Phase 8+ |
| Ads pack submission to Ads Manager | Phase 8+ |
| Scheduling and publishing automation | Phase 8+ |

---

## Runtime Modules to Build (Phase 7+)

### Phase 7 — n8n Runtime Blueprint
- Design n8n workflow JSON for: content approval routing, content agent trigger, basic log writing.
- All workflows must default to `active: false`.
- No live connections — placeholder credentials only.

### Phase 8 — CRM + Inbox Automation
- Wire Zalo/Messenger API for CRM sequence sending (after Owner approval gate).
- Wire Facebook/TikTok comment monitoring for inbox draft generation.
- All require Owner Approved status before any real send.

### Phase 9 — Ads + Publishing Automation
- Wire Meta Ads API for ads pack submission (after Owner approval).
- Wire TikTok Ads API.
- Wire content scheduling to Facebook/Instagram/TikTok.
- All require Approved + approved_at before execution.

### Phase 10+ — Analytics + Reporting
- Pull performance data from Meta/TikTok/Zalo into Google Sheets or Supabase.
- Feed performance back into Content Agent for optimization.

---

## Required External Systems (Future Phases)

| System | Purpose | Phase |
|--------|---------|-------|
| **n8n** (self-hosted or cloud) | Workflow automation engine | Phase 7 |
| **Google Sheets or Supabase** | Content queue, approval status tracking, CRM data | Phase 7–8 |
| **Google Drive** | Brand asset storage (images, videos, briefs) | Phase 7 |
| **Telegram Bot** | Owner approval notifications and decisions | Phase 7–8 |
| **Meta / Facebook / Instagram API** | Content publishing, ad management, inbox monitoring | Phase 9 |
| **TikTok API** | Content publishing, TikTok Ads | Phase 9 |
| **Zalo OA API** | CRM message sending, customer inbox | Phase 8 |
| **ShopeeFood / GrabFood / Baemin** | Delivery order integration (if applicable) | Phase 10+ |
| **Google Maps / Google Business Profile** | Location data, review monitoring | Phase 10+ |

---

## Data Still Needed From Owner

Owner must provide the following before production automation can run:

### Brand Data
- [ ] Confirmed exact prices for each dish
- [ ] Confirmed combo/offer names and prices
- [ ] Full physical address (number, street, ward, Vinh, Nghệ An)
- [ ] Opening hours (days and times)
- [ ] Delivery app(s) in use and delivery coverage area
- [ ] Facebook page URL and ordering inbox link
- [ ] Brand images (hero dish photos, logo files, menu photos)

### Customer Data
- [ ] Real confirmed FAQ answers (what do customers ask most?)
- [ ] Confirmed publishing channels (Facebook only? TikTok? Zalo OA? Instagram?)
- [ ] Opt-in list format for CRM (how are customers currently recorded?)

### Approval Preferences
- [ ] Preferred approval channel (Telegram? WhatsApp? Email?)
- [ ] Response time SLA for approvals (e.g., within 24 hours)
- [ ] Who is the backup approver if Owner is unavailable?

---

## Runtime Safety Rules

These rules are non-negotiable and must be enforced in every Phase 7+ workflow:

| Rule | Detail |
|------|--------|
| **No auto-publish without Approved** | No content, ad, or reply may be sent/published without `approval_status: Approved` set by Owner |
| **No real customer auto-reply without Approved** | CRM sequences and inbox replies require Owner approval before any real message is sent |
| **No ads spend without Approved** | No ad campaign may launch and no budget may be allocated without Owner Approved status |
| **All workflow JSON must be importable** | n8n workflow files must be self-contained JSON, importable via n8n UI without running a script |
| **workflow active=false by default** | All n8n workflow JSON files must have `"active": false` — Owner activates manually after review |
| **Credentials as placeholders** | All n8n workflow credentials must use placeholder values (`REPLACE_WITH_*`) — never commit real tokens |
| **Approval checkpoint in every workflow** | Every workflow that produces a customer-facing output must include an approval wait node before delivery |
| **Log every action** | Every n8n workflow execution must write a log entry in the format of `schemas/log-entry.schema.json` |
| **Human escalation path always exists** | Every workflow must have a defined path to pause execution and notify Owner for human decision |

---

## Recommended Phase 7 Starting Point

Before writing any n8n workflow JSON:

1. Owner fills all placeholder brand data in `brand-brain/vi-cuon.md` and `01_BRAIN/` files.
2. Owner confirms preferred approval channel (Telegram recommended for mobile-first workflow).
3. Builder creates n8n workflow for content approval routing only — the simplest, lowest-risk workflow.
4. Codex reviews the workflow JSON before it is imported into any n8n instance.
5. Owner imports and tests in n8n with `active: false` before activating.
