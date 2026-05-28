# 09 — Brand Brain System

Version: 1.0
Created By: Claude Code (Builder, AGT-02)
Date: 2026-05-28
Phase: 3 — Brand Brain + Input/Output Schemas

---

## What Is the Brand Brain?

The Brand Brain is a single markdown file that defines the complete identity, voice, audience, and rules for a brand operating inside FnB OS V1.

It is the **single source of brand truth** that every agent reads before producing any output. Agents must not invent brand details — they must read from the Brand Brain.

The Brand Brain is **not** a database, not a configuration file, and not executable code. It is a structured markdown document designed to be:
- Human-readable by the Owner
- Machine-interpretable by AI agents
- Replaceable without touching agents or schemas

---

## Default Brand Brain: Vị Cuốn

The default Brand Brain for FnB OS V1 is:

```
brand-brain/vi-cuon.md
```

This file contains the complete brand identity for **Vị Cuốn** — a Vietnamese F&B brand in Vinh, Nghệ An, specializing in fresh rolls and street-food-inspired meals.

### Key sections in vi-cuon.md

| Section | Purpose |
|---------|---------|
| Brand Snapshot | Core identity: name, category, market, positioning, price range, main menu, personality |
| Target Customers | Audience segments agents should write for |
| Core Selling Points | What makes Vị Cuốn different and worth choosing |
| Tone of Voice | Language rules: warmth, honesty, CTAs, emoji usage |
| Content Pillars | 8 recurring content themes agents must draw from |
| Offer Rules | When and how to mention offers; placeholder rules |
| Compliance / Safety | Hard lines: no fake reviews, no fake scarcity, no auto-post |
| Replaceable Brand Context | How to swap this Brand Brain for another brand |

---

## What Agents Must Read from the Brand Brain

Every agent that produces customer-facing or marketing output must read the Brand Brain before generating any content. Specifically:

| Agent | Must Read from Brand Brain |
|-------|---------------------------|
| Content Agent | Brand Snapshot, Target Customers, Tone of Voice, Content Pillars, Offer Rules |
| Creative Asset Agent | Brand Snapshot, Tone of Voice, visual personality implied by Brand Snapshot |
| Ads Pack Agent | Brand Snapshot, Target Customers, Core Selling Points, Offer Rules, Compliance/Safety |
| CRM Follow-Up Agent | Target Customers, Tone of Voice, Offer Rules, Compliance/Safety |
| Comment Inbox Agent | Brand Snapshot, Tone of Voice, Compliance/Safety |
| Approval/Publishing Agent | Compliance/Safety, Offer Rules — for final gate check |

---

## What Must NOT Be Invented

Agents must never invent the following without Owner confirmation:

| Prohibited Invention | Correct Behavior |
|---------------------|-----------------|
| Prices, discounts, or offers | Use `[OWNER_TO_PROVIDE_OFFER]` |
| Customer testimonials or reviews | Do not fabricate; use real customer voice only with Owner input |
| Health or nutrition claims | Do not state without Owner confirmation |
| "Limited time" or scarcity language | Do not use without Owner confirmation |
| New menu items | Use only items listed in Brand Brain |
| Brand taglines | Use only taglines confirmed by Owner |

---

## Owner Approval Required

All public-facing content derived from the Brand Brain requires Owner approval before publication. This includes:

- Social media captions and scripts
- Ad copy
- CRM message sequences
- Comment and inbox replies

No agent may publish, send, or schedule content without an explicit `Approved` status set by the Owner. See `schemas/approval-status.schema.json` for the full approval state machine.

---

## How to Replace the Brand Brain for Another F&B Brand

FnB OS V1 is designed to be reusable across F&B brands. The Brand Brain is the only file that needs to change.

**Steps to replace:**

1. **Copy** `brand-brain/vi-cuon.md` to a new file: `brand-brain/[your-brand-slug].md`
2. **Replace** all Vị Cuốn-specific content:
   - Brand name, category, market, positioning
   - Price range, main menu items
   - Brand personality and tone
   - Target customer segments
   - Content pillars relevant to the new brand
   - Offer rules specific to the new brand
3. **Update** `brand_id` and `brand_name` fields in all agent inputs and schema-generated outputs.
4. **Point agents** to the new Brand Brain file path — no agent code or schema changes required.
5. **Owner must review** the new Brand Brain before any content generation begins.

The agents, schemas, workflows, and approval gates are **brand-neutral** — only the Brand Brain file content changes.

---

## Brand Brain and the Phase System

| Phase | Brand Brain Role |
|-------|----------------|
| Phase 1.1 | Original Brand Brain Foundation (01_BRAIN/) — filled with Vị Cuốn data |
| Phase 3 | Structured Brand Brain document (`brand-brain/vi-cuon.md`) — canonical version for agent consumption |
| Phase 4+ | n8n/LangGraph agents will read Brand Brain as part of automated pipelines |

The `01_BRAIN/` files from Phase 1.1 remain as supplementary reference. `brand-brain/vi-cuon.md` is the canonical structured Brand Brain for Phase 3 and onwards.
