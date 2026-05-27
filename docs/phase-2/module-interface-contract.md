# Module Interface Contract — FnB OS V1

**Version:** 2.2
**Maintained By:** ChatGPT (Chief Architect) + Claude Code (Builder)
**Last Updated:** 2026-05-28
**Phase:** 2.2

This document defines the standard interface for all 12 modules in FnB OS V1.
Every module that is built or automated in Phase 3+ must conform to the contract defined here.
Changes to any module's contract require a new phase command and Owner approval.

---

## Contract Field Definitions

| Field | Description |
|-------|-------------|
| `MODULE_ID` | Unique identifier. Format: `MOD-XX` |
| `MODULE_NAME` | Short human-readable name |
| `LAYER` | Which of the 6 layers this module belongs to |
| `PURPOSE` | What this module does — one to two sentences |
| `INPUTS` | What the module consumes to produce its outputs |
| `OUTPUTS` | What the module produces |
| `STORAGE` | Where outputs are stored (GitHub path, Google Sheets, Google Drive) |
| `APPROVAL_REQUIRED` | Whether an Owner approval step is required before action |
| `EXTERNAL_ACTION` | Whether this module contacts real customers, posts publicly, or spends money |
| `RISK_LEVEL` | LOW / MEDIUM / HIGH / CRITICAL — based on external action potential |
| `V1_SCOPE` | Current implementation status in V1 |
| `FUTURE_SCOPE` | Target automation level in future phases |

Risk level definitions:
- `LOW` — no external action; documentation, drafting, or logging only
- `MEDIUM` — non-customer-facing external calls (design API, web scraping)
- `HIGH` — external action that touches customers or is publicly visible
- `CRITICAL` — action that spends money or cannot be easily reversed

---

---

## MOD-01 — Brand Brain

```
MODULE_ID:         MOD-01
MODULE_NAME:       Brand Brain
LAYER:             Layer 1 — Brand Layer
PURPOSE:           Store the complete brand knowledge base for one F&B brand.
                   Acts as the primary data source for all production, interaction,
                   and intelligence modules (MOD-02 through MOD-12).
INPUTS:            - Brand identity data (name, location, hours, price range)
                   - Menu items and pricing
                   - Brand positioning and differentiation
                   - Customer segments and personas
                   - Content pillars and angles
                   - Offer rules and promotions
                   - Brand voice, tone, and style guidelines
                   - Design and visual guidelines
                   - Safety and compliance constraints
                   - CRM and comment reply rules
OUTPUTS:           - Structured brand data files (markdown)
                   - Data available to: MOD-02, 03, 04, 05, 06, 08, 09, 10, 11
STORAGE:           GitHub: 01_BRAIN/ directory
                   Files: brand_brain.md, menu_brain.md, customer_brain.md,
                          content_brain.md, offer_brain.md, design_brain.md,
                          crm_brain.md, comment_reply_brain.md, ads_brain.md
APPROVAL_REQUIRED: YES — Brand Brain content must be reviewed and confirmed by Owner
                   before being used as input to production modules.
                   Changes to Brand Brain require Owner approval.
EXTERNAL_ACTION:   NONE — Brand Brain is a data store. No external calls.
RISK_LEVEL:        LOW
V1_SCOPE:          EXISTS — Phase 1.1 built Brand Brain for Vị Cuốn.
                   All core files are populated. Some fields marked [FILL] await Owner input.
FUTURE_SCOPE:      AI-assisted Brand Brain updates when Owner adds new menu items,
                   changes offers, or updates positioning. All changes still require Owner approval.
```

---

## MOD-02 — Content Auto

```
MODULE_ID:         MOD-02
MODULE_NAME:       Content Auto
LAYER:             Layer 2 — Marketing Production Layer
PURPOSE:           Generate structured content packs for social media platforms
                   based on Brand Brain data, content pillars, and campaign angles.
INPUTS:            - Brand Brain: brand voice, tone, pillars, angles, segments,
                     offers, safety constraints (MOD-01)
                   - Selected content pillar (e.g., BTS, Social Proof, Offer)
                   - Selected content angle (specific sub-angle within pillar)
                   - Platform (TikTok, Facebook, Instagram)
                   - Target persona / segment
                   - Optional: campaign offer or promotion
                   - Optional: campaign brief from Owner
OUTPUTS:           - Content pack file containing:
                       - Caption (platform-appropriate)
                       - Video script (if applicable)
                       - Hashtag set
                       - Visual direction brief
                       - Persona targeting notes
                       - Content ID
                       - AI self-check result
STORAGE:           GitHub: 07_MANUAL_TEST_RUN/ (V1 manual)
                   Future: GitHub content pack files + Google Sheets approval pipeline
APPROVAL_REQUIRED: YES — all content packs must pass Owner review at MOD-07
                   before publishing.
EXTERNAL_ACTION:   NONE in V1 (draft only, no publishing).
                   Future: post to TikTok, Facebook, Instagram after approval.
RISK_LEVEL:        LOW in V1 (draft only).
                   HIGH in future phases when publishing is enabled.
V1_SCOPE:          EXISTS — Phase 1.4 built content pack generator schema.
                   Phase 1.6 built manual runbook. Phase 1.7 completed first manual test.
                   Content ID format: [BRAND]-[PLATFORM]-[PILLAR]-[DATE]-[SEQ]
FUTURE_SCOPE:      n8n workflow generates content packs on a schedule or Owner trigger.
                   AI auto-selects pillar/angle based on calendar and performance data.
                   All packs route to MOD-07 for approval before publishing.
```

---

## MOD-03 — Creative Asset Auto

```
MODULE_ID:         MOD-03
MODULE_NAME:       Creative Asset Auto
LAYER:             Layer 2 — Marketing Production Layer
PURPOSE:           Generate design briefs and creative directions for images,
                   videos, and graphic assets based on content pack and brand
                   design guidelines. Enables consistent visual production
                   without manual brief writing.
INPUTS:            - Approved content pack from MOD-02
                   - Brand Brain design guidelines (colors, fonts, visual style,
                     layout preferences) — MOD-01
                   - Platform technical specs (image size, video ratio, duration)
                   - Content type (static image, carousel, short video, story)
OUTPUTS:           - Design brief markdown (for human designer or AI design tool)
                   - Image prompt (for Midjourney/Canva/Gemini image generation)
                   - Video direction notes (scene descriptions, text overlay, music mood)
                   - Asset naming convention (linked to content ID from MOD-02)
STORAGE:           GitHub: design briefs in content pack directory
                   Google Drive: produced assets in Asset Library (MOD-11)
APPROVAL_REQUIRED: YES — design brief requires Owner review before production
                   begins. Produced asset requires Owner approval before use.
EXTERNAL_ACTION:   NONE in V1 (brief generation only, no API calls).
                   Future: send brief to Canva API or Midjourney after approval.
RISK_LEVEL:        LOW in V1.
                   MEDIUM in future (API calls to external design tools).
V1_SCOPE:          PARTIAL — design_brief_schema.json exists in 05_SCHEMAS/.
                   design_brain.md exists in 01_BRAIN/. Manual brief writing only.
FUTURE_SCOPE:      Auto-generate design brief from content pack.
                   Send to Canva API or AI image tool after Owner approval.
                   Store produced assets in MOD-11 Asset Library.
```

---

## MOD-04 — Ads Pack Auto

```
MODULE_ID:         MOD-04
MODULE_NAME:       Ads Pack Auto
LAYER:             Layer 2 — Marketing Production Layer
PURPOSE:           Assemble advertising packs for Meta (Facebook/Instagram) and
                   TikTok Ads including ad copy, audience targeting brief,
                   creative brief, and budget recommendation. Ensures every
                   ad campaign starts from a structured, approved document.
INPUTS:            - Approved content pack or campaign brief
                   - Brand Brain: positioning, customer segments, offer data — MOD-01
                   - Campaign objective (awareness, traffic, conversion)
                   - Target segment definition
                   - Budget range (Owner-set)
                   - Creative assets (from MOD-03, if available)
OUTPUTS:           - Ads pack document containing:
                       - Ad copy variants (primary, secondary)
                       - Audience targeting brief
                       - Creative brief
                       - Budget recommendation
                       - Campaign objective statement
                       - Risk notes (e.g., claim that needs compliance check)
STORAGE:           GitHub: 05_SCHEMAS/ads_pack_schema.json (schema)
                   Future: ads pack files in designated directory
                   Google Sheets: ads approval tracking
APPROVAL_REQUIRED: YES — all ads packs require explicit Owner approval before
                   any ad setup begins. No ad is created, budgeted, or launched
                   without Owner approval. This is a CRITICAL gate.
EXTERNAL_ACTION:   NONE in V1 (pack generation only, no platform calls).
                   Future: Meta Ads API / TikTok Ads API after Owner approval.
RISK_LEVEL:        LOW in V1.
                   CRITICAL in future (real money, irreversible spend).
V1_SCOPE:          PARTIAL — ads_pack_schema.json exists. ads_brain.md exists.
                   Manual ads pack creation only. No automated generation yet.
FUTURE_SCOPE:      Auto-generate ads pack from approved content + campaign brief.
                   Route to Owner approval at MOD-07.
                   After approval: submit to Meta/TikTok Ads API.
                   Budget gate: hard cap enforced at API level before submission.
```

---

## MOD-05 — CRM Follow-up Auto

```
MODULE_ID:         MOD-05
MODULE_NAME:       CRM Follow-up Auto
LAYER:             Layer 3 — Customer Interaction Layer
PURPOSE:           Generate draft follow-up messages for customer relationship
                   management events: reservation confirmations, post-visit
                   thank-you messages, loyalty outreach, and upsell nudges.
                   Ensures every customer touchpoint is timely, brand-consistent,
                   and approved before sending.
INPUTS:            - Customer event trigger (reservation, visit, inquiry, anniversary)
                   - Customer data: name, phone/Zalo, visit history (from POS or manual log)
                   - CRM Brain: message templates, tone rules, follow-up schedule — MOD-01
                   - Offer data (if upsell is included)
OUTPUTS:           - Draft CRM message (Zalo OA / SMS / WhatsApp-ready text)
                   - Message type label (confirmation / thank-you / loyalty / upsell)
                   - Recommended send time
                   - Customer ID reference
STORAGE:           GitHub: CRM templates in 02_PROMPTS/comment_reply_agent_prompt.md
                   Google Sheets: CRM event log and approval queue
APPROVAL_REQUIRED: YES — every CRM message requires Owner review and approval
                   before sending. The AI never contacts a real customer without
                   explicit Owner approval. This is a HIGH gate.
EXTERNAL_ACTION:   NONE in V1 (draft generation only).
                   Future: Zalo OA API send after Owner approval.
RISK_LEVEL:        LOW in V1 (draft only).
                   HIGH in future (direct contact with real customers).
V1_SCOPE:          PARTIAL — crm_followup_schema.json exists. crm_brain.md exists.
                   Manual CRM drafting only. No automated generation or sending.
FUTURE_SCOPE:      n8n reads CRM event from Google Sheets → generates draft message
                   → routes to Owner approval via Telegram → sends via Zalo OA
                   after approval. Full audit trail in MOD-12.
```

---

## MOD-06 — Comment / Inbox Reply Assistant

```
MODULE_ID:         MOD-06
MODULE_NAME:       Comment / Inbox Reply Assistant
LAYER:             Layer 3 — Customer Interaction Layer
PURPOSE:           Classify incoming social media comments and inbox messages by
                   intent, generate draft replies aligned with brand voice, and
                   route to Owner for approval before posting. Prevents slow or
                   inconsistent responses without enabling uncontrolled auto-reply.
INPUTS:            - Raw comment or inbox message text
                   - Platform (TikTok, Facebook, Instagram)
                   - Intent classification (inquiry, complaint, compliment, spam, off-topic)
                   - Brand Brain: tone, voice, FAQ data, escalation rules — MOD-01
OUTPUTS:           - Intent label (AI classification)
                   - Draft reply text
                   - Suggested action (reply / escalate to Owner / ignore / flag as spam)
                   - Risk flag if reply touches price, availability, complaint, or legal claim
STORAGE:           GitHub: comment_reply_schema.json in 05_SCHEMAS/
                   Google Sheets: comment queue and approval log
APPROVAL_REQUIRED: YES — all replies require Owner review before posting.
                   High-risk intents (complaint, price dispute, legal claim) require
                   mandatory Owner review with no auto-approve fallback.
EXTERNAL_ACTION:   NONE in V1 (draft generation and classification only).
                   Future: Facebook Graph API / TikTok API reply after Owner approval.
RISK_LEVEL:        LOW in V1 (draft only).
                   HIGH in future (public replies affect brand reputation).
V1_SCOPE:          PARTIAL — comment_reply_schema.json exists. comment_reply_brain.md
                   exists. Test fixtures exist in 07_TEST_FIXTURES/. Manual reply only.
FUTURE_SCOPE:      n8n reads new comments from Facebook/TikTok API → classifies intent
                   → generates draft → routes to Telegram approval bot → posts reply
                   after Owner approval. Complaint/dispute always escalated to Owner
                   regardless of automation level.
```

---

## MOD-07 — Approval + Publishing Automation

```
MODULE_ID:         MOD-07
MODULE_NAME:       Approval + Publishing Automation
LAYER:             Layer 4 — Approval & Execution Layer
PURPOSE:           Manage the complete approval lifecycle for all draft outputs
                   from Layers 2 and 3. Route drafts to Owner for review, record
                   decisions as structured data, and trigger execution only after
                   explicit approval. This is the single gate through which all
                   external actions must pass.
INPUTS:            - Draft output from MOD-02 (content pack)
                   - Draft output from MOD-03 (design brief / creative asset)
                   - Draft output from MOD-04 (ads pack)
                   - Draft output from MOD-05 (CRM message)
                   - Draft output from MOD-06 (comment reply)
                   - Owner decision (Approved / Rejected / Revision Requested)
                   - Approval timestamp and Owner identifier
OUTPUTS:           - Approval record (structured data: item ID, status, decision,
                     timestamp, notes)
                   - Status update on the draft item
                   - Execution trigger (only after Approved)
                   - Rejection record with reason (if Rejected)
STORAGE:           GitHub: approval logs in 09_LOGS/
                   Google Sheets: approval tracking sheet (primary approval data store)
                   Approval records must be stored as structured data, not only in chat.
APPROVAL_REQUIRED: IS THE APPROVAL GATE — Owner decision is mandatory for every
                   external action. No execution trigger fires without a stored
                   approval record that contains: item ID, status = Approved,
                   Owner decision, and timestamp.
EXTERNAL_ACTION:   NONE in V1 (routing and recording only).
                   Future: trigger posting, sending, scheduling after approval.
RISK_LEVEL:        LOW in V1 (no execution).
                   CRITICAL in future (gate failure means unauthorized action).
V1_SCOPE:          EXISTS — approval_schema.json in 05_SCHEMAS/. approval_sheet_schema.md,
                   content_pipeline_schema.md, status_lifecycle.md in 03_APPROVAL_PIPELINE/.
                   Manual Google Sheets approval in V1.
FUTURE_SCOPE:      Telegram bot routes draft to Owner → Owner taps Approve/Reject →
                   n8n reads approval record → triggers execution.
                   Full approval history in Google Sheets. Audit trail in MOD-12.
```

---

## MOD-08 — Competitor Intelligence

```
MODULE_ID:         MOD-08
MODULE_NAME:       Competitor Intelligence
LAYER:             Layer 5 — Intelligence Layer
PURPOSE:           Monitor competitor activity (pricing, promotions, new menu items,
                   content patterns, customer reviews) and generate structured
                   intelligence reports for Owner review. Enables data-informed
                   positioning decisions without manual tracking.
INPUTS:            - Competitor profile data (name, channels, product categories)
                   - Monitoring schedule (weekly, event-triggered)
                   - Social media data from competitor pages (manual entry in V1)
                   - Web data: competitor website, Google Maps reviews (manual in V1)
OUTPUTS:           - Competitor intelligence report (markdown)
                   - Change summary (what is new since last report)
                   - Implication notes (what this means for Vị Cuốn or target brand)
STORAGE:           GitHub: intelligence reports directory (to be created in future phase)
                   Google Drive: archived reports
APPROVAL_REQUIRED: NO — reports are informational and read-only.
                   No external action is triggered by competitor intelligence.
EXTERNAL_ACTION:   NONE in V1.
                   Future: automated web scraping (MEDIUM risk — scraping policies apply).
RISK_LEVEL:        LOW in V1.
                   MEDIUM in future (web scraping requires compliance review).
V1_SCOPE:          NOT STARTED — no implementation in Phase 1 or 2.
                   Planned for a future phase.
FUTURE_SCOPE:      Automated weekly competitor monitoring via web scraping and
                   social media API. Structured report generated and stored.
                   Delivered to Owner as Telegram summary.
```

---

## MOD-09 — Analytics Intelligence

```
MODULE_ID:         MOD-09
MODULE_NAME:       Analytics Intelligence
LAYER:             Layer 5 — Intelligence Layer
PURPOSE:           Analyze content performance, campaign ROI, and customer behavior
                   patterns to generate actionable insights and content strategy
                   recommendations. Closes the loop between production (Layer 2)
                   and future planning.
INPUTS:            - Social media performance metrics (manual export in V1):
                     reach, engagement rate, saves, shares, follower growth
                   - Publication log from MOD-07
                   - Sales data (manual entry in V1)
                   - Content pack archive from MOD-02
OUTPUTS:           - Weekly performance report (markdown)
                   - Top-performing content patterns
                   - Underperforming content flags
                   - Recommended pillar/angle adjustments
                   - ROI summary (if campaign data available)
STORAGE:           GitHub: analytics reports directory (to be created in future phase)
                   Google Sheets: performance data source
APPROVAL_REQUIRED: NO — reports are informational.
                   Owner reviews reports to inform strategy decisions.
EXTERNAL_ACTION:   NONE in V1.
                   Future: Facebook Insights API, TikTok Analytics API.
RISK_LEVEL:        LOW in V1.
                   LOW in future (read-only API calls).
V1_SCOPE:          NOT STARTED — no implementation in Phase 1 or 2.
                   Planned for a future phase.
FUTURE_SCOPE:      Auto-pull weekly metrics from social platforms.
                   AI generates performance summary and strategy suggestions.
                   Delivered to Owner as Telegram report.
```

---

## MOD-10 — Website / Landing Page Intelligence

```
MODULE_ID:         MOD-10
MODULE_NAME:       Website / Landing Page Intelligence
LAYER:             Layer 5 — Intelligence Layer
PURPOSE:           Monitor website and landing page performance, identify conversion
                   drop-off points, and generate content update and optimization briefs
                   for the Owner to review and action.
INPUTS:            - Website traffic data (manual export from Google Analytics in V1)
                   - Landing page content (current version)
                   - Conversion goals (reservation, order, lead form)
                   - Campaign traffic source data (from MOD-04 if available)
OUTPUTS:           - Performance summary report (markdown)
                   - Conversion funnel analysis
                   - Page optimization brief (recommended changes with rationale)
                   - Priority ranking (what to fix first)
STORAGE:           GitHub: website intelligence reports (to be created in future phase)
APPROVAL_REQUIRED: YES — website content changes require Owner approval before
                   implementation. Reports are read-only; any changes actioned from
                   the report must be explicitly approved.
EXTERNAL_ACTION:   NONE in V1.
                   Future: CMS API integration (MEDIUM risk — modifies live website).
RISK_LEVEL:        LOW in V1 (reports only).
                   MEDIUM in future (live website changes).
V1_SCOPE:          NOT STARTED — no implementation in Phase 1 or 2.
                   Planned for a future phase.
FUTURE_SCOPE:      Auto-pull Google Analytics data weekly.
                   AI generates optimization brief.
                   Owner approves changes.
                   Future: CMS API applies approved changes automatically.
```

---

## MOD-11 — Asset Library

```
MODULE_ID:         MOD-11
MODULE_NAME:       Asset Library
LAYER:             Layer 6 — Infrastructure Layer
PURPOSE:           Provide centralized, organized storage for all approved brand
                   assets — images, videos, design files, copy templates, and
                   content pack archives. Makes assets discoverable and reusable
                   across all production modules.
INPUTS:            - Approved creative assets from MOD-03
                   - Approved content packs from MOD-02 (archive)
                   - Brand Brain static assets (logo, brand kit) from MOD-01
                   - Asset metadata: content ID, platform, date, content type, status
OUTPUTS:           - Organized asset catalog with metadata
                   - Asset retrieval references for MOD-02, 03, 04
                   - Approved asset list (available for reuse)
STORAGE:           Google Drive: primary file storage
                     /FnB OS V1/[Brand]/Assets/Images/
                     /FnB OS V1/[Brand]/Assets/Videos/
                     /FnB OS V1/[Brand]/Assets/Design Files/
                     /FnB OS V1/[Brand]/Content Packs/
                   GitHub: asset catalog index (metadata only, not the binary files)
APPROVAL_REQUIRED: NO — storage and retrieval are automated.
                   Assets in the library are already approved (approval happened at MOD-07).
EXTERNAL_ACTION:   NONE — local storage only.
RISK_LEVEL:        LOW
V1_SCOPE:          PARTIAL — Google Drive folder structure defined in
                   08_DEPLOY/google_drive_structure.md.
                   No automated asset tagging or catalog yet.
FUTURE_SCOPE:      Automated asset tagging when assets are uploaded post-approval.
                   AI-assisted asset retrieval: "find an image for a rainy day BTS post"
                   returns matching approved assets from the library.
```

---

## MOD-12 — Logs / Governance / Cost / Safety

```
MODULE_ID:         MOD-12
MODULE_NAME:       Logs / Governance / Cost / Safety
LAYER:             Layer 6 — Infrastructure Layer
PURPOSE:           Track all agent actions, module outputs, approval decisions,
                   errors, costs, and safety violations across the entire FnB OS V1
                   system. Provide governance data and safety alerts to the Owner.
                   This module is observational — it records and alerts but does not
                   gate or approve.
INPUTS:            - Agent session outputs (Builder, Reviewer, Orchestrator)
                   - Module execution logs (from all MOD-01 through MOD-11)
                   - Approval records (from MOD-07)
                   - Error events (from any module)
                   - Cost data (API usage, n8n execution credits)
                   - Safety violation flags (from any module's self-check)
OUTPUTS:           - Agent activity log (per session)
                   - Phase log (per phase)
                   - Error log (per incident)
                   - Cost summary (weekly/monthly)
                   - Safety alert (when a violation is detected)
                   - Governance dashboard data (future)
STORAGE:           GitHub: logs/ directory (AGENT_ACTIVITY_LOG.md, PHASE_LOG.md)
                             09_LOGS/ directory (execution_log_template.md,
                             error_log_template.md, approval_log_template.md)
APPROVAL_REQUIRED: NO — logging is automatic and does not require approval.
                   Safety alerts are surfaced to Owner for review but do not
                   automatically block execution (MOD-07 gates execution).
EXTERNAL_ACTION:   NONE — logging and alerting only.
                   Future: Telegram alert to Owner when safety violation detected.
RISK_LEVEL:        LOW
V1_SCOPE:          EXISTS — AGENT_ACTIVITY_LOG.md, PHASE_LOG.md, and log templates
                   are active from Phase 0. Agent sessions append rows per session.
FUTURE_SCOPE:      Automated cost tracking from API usage.
                   Real-time safety monitoring with Telegram alerts.
                   Governance dashboard (Google Sheets or Notion) showing system health.
```

---

## Module Dependency Map

```
         MOD-01 (Brand Brain)
              │
    ┌─────────┼──────────┐
    ▼         ▼          ▼
 MOD-02    MOD-03     MOD-04
(Content) (Creative) (Ads Pack)
    │         │          │
    └────┬────┘          │
         ▼               ▼
      MOD-07 (Approval Gate) ◄── MOD-05 (CRM)
              │                       ▲
              │           MOD-06 (Comment Reply)
              │
    ┌─────────┼──────────┐
    ▼         ▼          ▼
 MOD-08    MOD-09     MOD-10
(Compete) (Analytics)(Website)
              │
         MOD-11 (Asset Library) ◄── all approved assets
              │
         MOD-12 (Logs/Governance) ◄── all modules
```

---

## Anti-Hardcoding Rule

No module contract, schema, workflow, or prompt template may embed brand-specific data directly.

**Allowed in module files:**
- Field names and structure (generic)
- Placeholder text: `[BRAND_NAME]`, `[MENU_ITEM]`, `[OFFER_TEXT]`
- References to Brand Brain: "read from `01_BRAIN/brand_brain.md`"

**Not allowed in module files:**
- Hard values like "Vị Cuốn", "Vinh Nghệ An", "80.000đ", specific menu items
- These belong in Brand Brain data files only

This rule ensures modules remain reusable when FnB OS V1 is deployed for a second brand.
