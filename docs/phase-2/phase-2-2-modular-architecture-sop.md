# Phase 2.2 — FnB OS V1 Modular Architecture SOP

**Status:** CLOSED
**Phase:** 2.2
**Builder:** Claude Code (AGT-02)
**Date:** 2026-05-28
**Branch:** main
**Previous Phase:** 2.1 — Builder/Reviewer Operating SOP (CLOSED, commit: 41b8abb)

---

## Purpose of FnB OS V1

FnB OS V1 is a modular AI Marketing Operating System for F&B brands.

It is not a single-brand tool, and it is not a video generator.

Its purpose is to give an F&B business owner a complete, AI-assisted marketing operation — from brand definition through content production, customer interaction, approval, analytics, and infrastructure — running with minimal manual work and full Owner control over every external action.

The system is designed so that:
- Any F&B brand can plug in their Brand Brain and run the same operating modules.
- All AI-generated outputs pass through an approval gate before any external action occurs.
- The Owner remains the final decision-maker on everything that touches real customers, real money, or public channels.

**Vị Cuốn is the first brand to implement FnB OS V1.** It is not the system itself.

---

## Official Architecture — 6 Layers / 12 Modules

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1 — BRAND LAYER                                  │
│  MOD-01: Brand Brain                                    │
│  (brand-specific — replaceable per brand)               │
└───────────────────────┬─────────────────────────────────┘
                        │  Brand data feeds all layers below
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 2 — MARKETING PRODUCTION LAYER                   │
│  MOD-02: Content Auto                                   │
│  MOD-03: Creative Asset Auto                            │
│  MOD-04: Ads Pack Auto                                  │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 3 — CUSTOMER INTERACTION LAYER                   │
│  MOD-05: CRM Follow-up Auto                             │
│  MOD-06: Comment / Inbox Reply Assistant                │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 4 — APPROVAL & EXECUTION LAYER                   │
│  MOD-07: Approval + Publishing Automation               │
│  (all outputs from Layers 2–3 pass through this gate)   │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 5 — INTELLIGENCE LAYER                           │
│  MOD-08: Competitor Intelligence                        │
│  MOD-09: Analytics Intelligence                         │
│  MOD-10: Website / Landing Page Intelligence            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  LAYER 6 — INFRASTRUCTURE LAYER (cross-cutting)         │
│  MOD-11: Asset Library                                  │
│  MOD-12: Logs / Governance / Cost / Safety              │
└─────────────────────────────────────────────────────────┘
```

---

## Layer Explanations

### Layer 1 — Brand Layer

Contains the brand-specific knowledge base. Every other module reads from this layer.

This layer holds brand identity, voice, tone, menu data, offer rules, customer segment definitions, design guidelines, and content constraints. It is the only layer that is replaced when a new F&B brand adopts FnB OS V1.

**Brand Brain is NOT reusable across brands — it is replaced per brand.**

### Layer 2 — Marketing Production Layer

Generates all outbound marketing materials: content packs, creative assets, and ad packs.

All outputs from this layer are drafts. Nothing in this layer posts, publishes, or spends money. Every output waits in the approval pipeline (Layer 4) before any external action occurs.

### Layer 3 — Customer Interaction Layer

Handles inbound customer signals: social media comments, inbox messages, and CRM events (reservations, visits, post-visit follow-ups).

All outputs from this layer are drafts — pre-written replies and CRM messages that wait for Owner review before sending. The AI never contacts a real customer without approval.

### Layer 4 — Approval & Execution Layer

The single gate through which all draft outputs must pass before any external action occurs.

This layer records Owner decisions as structured data (not just chat text), routes approvals to the appropriate execution module, and maintains the audit trail. No publish, reply, CRM send, or ad launch happens outside this gate.

### Layer 5 — Intelligence Layer

Passive monitoring and analysis modules. These modules consume external data (competitor activity, content performance, website traffic) and produce structured intelligence reports for Owner review.

Intelligence modules do not generate content or take external actions. They inform the Owner's decisions.

### Layer 6 — Infrastructure Layer (Cross-Cutting)

Provides storage and governance for the entire system. The Asset Library stores approved brand assets for reuse. The Logs/Governance module tracks all agent activity, costs, errors, and safety events.

This layer runs in the background across all other layers.

---

## Module Explanations

### MOD-01 — Brand Brain *(brand-specific)*

The structured knowledge base for one F&B brand. Contains: brand identity, positioning, menu, price range, customer segments, content pillars, offer rules, design guidelines, brand voice, and safety constraints.

**This is the only module replaced when deploying FnB OS V1 for a new brand.**
Modules 2–12 read from Brand Brain but do not embed brand-specific data directly.

Existing V1 implementation: `01_BRAIN/` directory (brand_brain.md, menu_brain.md, customer_brain.md, content_brain.md, offer_brain.md, design_brain.md, crm_brain.md, comment_reply_brain.md, ads_brain.md)

---

### MOD-02 — Content Auto *(reusable)*

Generates content packs for social media platforms: TikTok, Facebook, Instagram. A content pack includes a caption, video script, hashtag set, visual direction brief, and persona targeting notes.

Inputs: Brand Brain data, selected content pillar, content angle, platform, persona, optional offer.
Outputs: Structured content pack file (markdown or JSON).

Content packs are drafts. They enter the approval pipeline at Layer 4.

Existing V1 implementation: `02_CONTENT_ENGINE/`, `04_CONTENT_PACK_GENERATOR/`, `06_MANUAL_RUNBOOK/`, `07_MANUAL_TEST_RUN/`

---

### MOD-03 — Creative Asset Auto *(reusable)*

Generates design briefs and creative directions for images, videos, and graphic assets based on the content pack and brand design guidelines.

Inputs: Approved content pack (from MOD-02), Brand Brain design guidelines, platform size specs.
Outputs: Design brief markdown, image prompt, video direction notes.

Output goes to the designer (human or AI design tool) for production. Not auto-published.

---

### MOD-04 — Ads Pack Auto *(reusable)*

Assembles advertising packs for Meta (Facebook/Instagram) and TikTok Ads including copy, audience targeting brief, creative brief, and budget recommendation.

Inputs: Approved content, brand positioning, target segment definition, campaign budget (Owner-set), offer data.
Outputs: Ads pack document with copy, targeting brief, budget recommendation.

No ad is created or budgeted automatically. The Owner approves the ads pack and initiates setup manually or via an approved integration in a future phase.

---

### MOD-05 — CRM Follow-up Auto *(reusable)*

Generates follow-up messages for customer relationship management events: reservation confirmations, post-visit thank-you messages, loyalty outreach, and upsell nudges.

Inputs: Customer event data (reservation, visit, inquiry), customer contact info, message templates, CRM brain.
Outputs: Draft CRM message text, ready for Owner approval before sending.

No CRM message is sent automatically. Draft is reviewed and approved at Layer 4.

---

### MOD-06 — Comment / Inbox Reply Assistant *(reusable)*

Classifies incoming social media comments and inbox messages by intent (inquiry, complaint, compliment, spam, off-topic) and generates draft replies aligned with brand voice.

Inputs: Comment or message text, intent classification, Brand Brain tone, FAQ data.
Outputs: Draft reply text with suggested action label.

No reply is posted automatically. Draft is reviewed and approved at Layer 4.

---

### MOD-07 — Approval + Publishing Automation *(reusable)*

The central approval gate for the entire system. Manages the lifecycle of every draft output from Layers 2 and 3: routes to Owner for review, records the decision as structured data, and triggers execution only after explicit approval.

Inputs: Any draft from MOD-02, 03, 04, 05, or 06. Owner decision (Approved / Rejected / Revision).
Outputs: Approval record (structured data), status update, execution trigger (only post-approval).

See `docs/phase-2/approval-gate-standard.md` for the complete status lifecycle and rules.

Existing V1 implementation: `03_APPROVAL_PIPELINE/` (status_lifecycle.md, approval_sheet_schema.md, content_pipeline_schema.md)

---

### MOD-08 — Competitor Intelligence *(reusable)*

Monitors competitor activity — pricing changes, new menu items, promotions, content patterns — and generates structured intelligence reports for Owner review.

Inputs: Competitor profile data, monitoring schedule, social and web data (manual entry in V1).
Outputs: Competitor intelligence report markdown.

Reports are read-only. No external action is taken based on competitor data automatically.

Not started in V1. Planned for a future phase.

---

### MOD-09 — Analytics Intelligence *(reusable)*

Analyzes content performance, campaign ROI, customer behavior patterns, and generates actionable recommendations.

Inputs: Social media performance metrics (manual export in V1), sales data, publication log.
Outputs: Performance report, insight summary, recommended content or strategy adjustments.

Reports are informational. No external action is triggered automatically.

Not started in V1. Planned for a future phase.

---

### MOD-10 — Website / Landing Page Intelligence *(reusable)*

Monitors website and landing page performance, identifies conversion opportunities, and generates content update briefs.

Inputs: Website traffic data (manual export in V1), landing page content, conversion goals.
Outputs: Performance summary, page optimization brief.

Website changes require Owner approval before implementation.

Not started in V1. Planned for a future phase.

---

### MOD-11 — Asset Library *(reusable)*

Central storage and organization layer for all approved brand assets: images, videos, design files, copy templates, and approved content pack archives.

Inputs: Approved creative outputs from MOD-03, approved content packs from MOD-02, brand guidelines from MOD-01.
Outputs: Organized asset catalog with metadata and reuse references for other modules.

Storage: Google Drive (asset files), GitHub (metadata and catalog index).

Partially implemented in V1 via Google Drive structure (`08_DEPLOY/google_drive_structure.md`).

---

### MOD-12 — Logs / Governance / Cost / Safety *(reusable)*

Cross-cutting infrastructure module that tracks all agent actions, costs, errors, approvals, and safety violations. Enforces safety rules and provides governance data to the Owner.

Inputs: All module outputs, agent session logs, approval records, error events, cost data.
Outputs: Activity logs, error logs, cost summary, safety alerts.

No external action. Logging only.

Existing V1 implementation: `09_LOGS/`, `logs/AGENT_ACTIVITY_LOG.md`, `09_LOGS/PHASE_LOG.md`

---

## Brand-Specific vs. Reusable Modules

| Module | Type | Rationale |
|--------|------|-----------|
| MOD-01 Brand Brain | **Brand-specific** | Contains identity, menu, voice, offers — unique per brand. Replaced entirely for each new brand. |
| MOD-02 Content Auto | Reusable | Reads brand data from MOD-01. Logic is generic. |
| MOD-03 Creative Asset Auto | Reusable | Design brief format is generic. Brand style comes from MOD-01. |
| MOD-04 Ads Pack Auto | Reusable | Targeting and copy logic is generic. Brand angles come from MOD-01. |
| MOD-05 CRM Follow-up Auto | Reusable | Message templates are generic. Brand tone and customer data come from MOD-01 and CRM events. |
| MOD-06 Comment Reply | Reusable | Reply logic and intent classification are generic. Brand voice comes from MOD-01. |
| MOD-07 Approval Gate | Reusable | Status lifecycle and approval rules are generic across all brands. |
| MOD-08 Competitor Intelligence | Reusable | Report structure is generic. Competitor profiles are brand-specific inputs. |
| MOD-09 Analytics | Reusable | Performance metrics and analysis logic are generic. |
| MOD-10 Website Intelligence | Reusable | Monitoring and optimization logic are generic. |
| MOD-11 Asset Library | Reusable | Storage and catalog structure are generic. Assets are brand-specific data, not system logic. |
| MOD-12 Logs / Governance | Reusable | Logging and safety rules are generic across all brands. |

**Rule:** Brand-specific data belongs in Brand Brain (MOD-01) or in the brand's data files. It must not be hardcoded into module logic, prompt templates, schemas, or workflow JSON.

---

## How Brand Brain Feeds Modules 2–12

Brand Brain is not a passive reference document. It is the primary data source that every production, interaction, and intelligence module reads before generating any output.

```
Brand Brain (MOD-01) provides:
├── Brand identity, tone, voice → consumed by MOD-02, 03, 05, 06
├── Menu and price data → consumed by MOD-02, 04, 05
├── Content pillars and angles → consumed by MOD-02
├── Offer rules → consumed by MOD-02, 04, 05
├── Customer segments → consumed by MOD-02, 04, 05, 06
├── Design guidelines → consumed by MOD-03
├── Safety constraints → consumed by MOD-02, 03, 04, 05, 06
└── Competitor context → informs MOD-08
```

When Brand Brain is swapped for a new F&B brand, all modules automatically operate for the new brand — no module logic changes are needed.

---

## Vị Cuốn as the First Implementation Brand

Vị Cuốn (Vietnamese fresh roll restaurant, Vinh, Nghệ An) is the first F&B brand to run on FnB OS V1.

**What this means:**
- All V1 Brand Brain files are Vị Cuốn-specific: `01_BRAIN/brand_brain.md`, `menu_brain.md`, `customer_brain.md`, etc.
- All current content examples, test fixtures, and manual test runs use Vị Cuốn data.
- The brand name "Vị Cuốn" may appear in these data files — this is expected.

**What this does NOT mean:**
- The system architecture, schemas, module logic, workflow templates, prompt templates, and SOP documents must NOT hardcode Vị Cuốn-specific data.
- Module names, schema field names, and workflow node names must be brand-neutral.
- Any field that contains Vị Cuốn data must be clearly labeled as a brand data field, not a system constant.

**Deployment for a new brand:**
1. Create a new Brand Brain directory with the new brand's data files.
2. Point all modules to the new Brand Brain.
3. Run the same operating modules — no module rewrites needed.

---

## Automation Readiness by Module

| Module | V1 Status | Automation Level in V1 | Target Automation Level |
|--------|-----------|----------------------|------------------------|
| MOD-01 Brand Brain | EXISTS | Manual (Owner fills files) | Semi-auto (AI assists Brand Brain updates) |
| MOD-02 Content Auto | EXISTS (manual runbook) | Manual with AI assist | Full auto — n8n + AI generates packs on schedule |
| MOD-03 Creative Asset Auto | PARTIAL | Manual | Auto brief generation → design tool integration |
| MOD-04 Ads Pack Auto | PARTIAL | Manual | Auto pack generation → Ads platform after approval |
| MOD-05 CRM Follow-up Auto | PARTIAL | Manual | Auto draft + Zalo OA send after approval |
| MOD-06 Comment Reply | PARTIAL | Manual | Auto classify + draft → Owner approves → auto-reply |
| MOD-07 Approval Gate | EXISTS (schema) | Manual (Google Sheets) | Auto routing → Telegram approval → auto-execute |
| MOD-08 Competitor Intelligence | NOT STARTED | — | Auto monitoring + weekly report |
| MOD-09 Analytics Intelligence | NOT STARTED | — | Auto pull + weekly insight report |
| MOD-10 Website Intelligence | NOT STARTED | — | Auto monitoring + optimization briefs |
| MOD-11 Asset Library | PARTIAL | Manual (Google Drive) | Auto tagging + retrieval for MOD-02/03 |
| MOD-12 Logs / Governance | EXISTS | Auto (per session) | Full auto governance dashboard |

---

## Actions That Always Require Owner Approval

The following actions can never be automated without an explicit Owner approval step:

| Action | Module | Risk |
|--------|--------|------|
| Publish a social media post | MOD-02, 07 | Public brand impact |
| Reply to a customer comment | MOD-06, 07 | Public brand impact |
| Send a CRM message to a customer | MOD-05, 07 | Direct customer contact |
| Launch or modify a paid ad | MOD-04, 07 | Real money |
| Change website or landing page content | MOD-10 | Public brand impact |
| Execute any n8n workflow for the first time | All | Scope validation |

**This list is exhaustive in V1.** Any new external action added in future phases must be reviewed against this list and added here if it touches customers, money, or public channels.

---

## What V1 Builds Now vs. Later

### V1 builds now (Phase 1–2):
- Complete Brand Brain for Vị Cuốn
- Manual content pack runbook and first test run
- All schemas (content pack, approval, CRM, ads, design brief)
- Approval pipeline structure (manual, Google Sheets)
- All SOP documents for agents and operators
- Module interface contracts
- Agent operating protocols

### V1 builds in Phase 3+ (after architecture is stable):
- n8n workflow for content pack auto-generation (MOD-02)
- Telegram approval bot for Owner review (MOD-07)
- Zalo OA CRM send automation (MOD-05)
- Comment reply queue with auto-draft (MOD-06)
- Google Sheets approval tracking integration

### Future phases (beyond current roadmap):
- Competitor intelligence monitoring (MOD-08)
- Analytics pull + insight reports (MOD-09)
- Website intelligence (MOD-10)
- LangGraph orchestration across all modules
- Multi-brand deployment

---

## Anti-Scope-Creep Rules

These rules protect the architecture from uncontrolled expansion:

1. **No module may expand its own scope.** If a module needs new capabilities, the Owner and ChatGPT add them to the architecture explicitly. Agents do not add features without a new phase command.

2. **Brand data stays in Brand Brain.** Any new brand-specific data field belongs in `01_BRAIN/` — not in schemas, workflow nodes, or module prompts.

3. **No new external actions without architecture review.** Any action that contacts a real customer, posts publicly, or spends money requires a new phase, Owner approval, and an update to the approval gate standard.

4. **Intelligence modules do not generate.** MOD-08, 09, 10 produce reports only. They do not write captions, launch campaigns, or modify content.

5. **MOD-12 does not gate.** Logs/Governance is observational. It records and alerts. It does not block execution or approve actions — that is MOD-07's role.

6. **LangGraph is not active in Phase 2.** No LangGraph implementation is built until the full module interface contracts are stable and Owner approves the orchestration architecture.

---

## Boundaries for Future n8n / LangGraph Implementation

### n8n (Runtime Automation)

n8n workflows implement the automation logic for individual modules. Each workflow:
- Must correspond to exactly one module
- Must have `"active": false` in the repo JSON until Owner activates it in n8n
- Must not hardcode credentials — use n8n credential manager only
- Must trigger execution only after an approval record exists in the data store
- Must log every action to MOD-12

n8n workflows are built in Phase 3+. They are imported from the repo JSON — they are not created directly in the n8n UI.

### LangGraph (Orchestration)

LangGraph coordinates the handoff between modules, managing state across multi-step workflows:
- Routes ChatGPT planning → Claude Code building → Codex reviewing → Owner approval → n8n execution
- Tracks phase state across sessions
- Enforces session caps and handoff rules at the infrastructure level

LangGraph is not implemented in Phase 2. Its architecture is documented here for planning purposes only.

**Neither n8n nor LangGraph makes approval decisions. The Owner always approves.**

---

## Reference Documents

| Document | Purpose |
|----------|---------|
| `docs/phase-2/module-interface-contract.md` | Detailed interface spec for all 12 modules |
| `docs/phase-2/approval-gate-standard.md` | Approval status lifecycle and rules |
| `docs/phase-2/phase-2-1-builder-reviewer-operating-sop.md` | Agent collaboration SOP |
| `agents/AGENT_REGISTRY.md` | Agent IDs and roles |
| `01_BRAIN/brand_brain.md` | Vị Cuốn Brand Brain (MOD-01 implementation) |
| `03_APPROVAL_PIPELINE/status_lifecycle.md` | Phase 1.3 content status lifecycle |
| `05_SCHEMAS/` | All module schemas |
