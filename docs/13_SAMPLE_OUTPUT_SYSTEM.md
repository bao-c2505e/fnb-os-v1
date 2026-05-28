# 13 — Sample Output System

**Phase:** 5 — Sample Outputs for Vị Cuốn
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28

---

## What Are Sample Outputs?

Sample outputs are filled instances of the Phase 4 output templates, produced using the Vị Cuốn Brand Brain. They demonstrate what a real agent output looks like for each module in FnB OS V1 — before any runtime automation is built.

A sample output is not a live published item. It is a structured draft that:
- Proves the schema fields are practical and completable.
- Proves the templates are usable by a content, CRM, or inbox agent.
- Shows the Owner what the system will eventually produce at scale.
- Surfaces gaps (missing brand data) before automation is wired.

---

## Why Phase 5 Exists

Phases 1–4 built the infrastructure:
- Phase 1: Brand brain content files
- Phase 2: Agent role definitions and SOPs
- Phase 3: JSON schema contracts
- Phase 4: Module SOPs and output templates

Phase 5 **proves it works** by running the system manually — agents (Claude Code acting as each module agent) fill the templates using the Brand Brain and schemas. The result is a set of practical sample outputs that can be reviewed, critiqued, and refined before n8n automation replaces the manual step.

Without Phase 5, Phase 6 (n8n automation) would be wiring up an untested system.

---

## How Samples Validate the Full Stack

Each sample output exercises the following chain:

```
Brand Brain → Agent SOP → Schema Contract → Output Template → Sample Output
```

For each module, the sample proves:
1. The agent can follow the SOP steps.
2. The schema fields are all meaningful and fillable.
3. The template matches the schema.
4. The output is practical for real F&B marketing use.
5. The approval gate works — all samples start at `Draft`, not `Published`.

---

## Why Incomplete Brand Brain Requires Placeholders

The Vị Cuốn Brand Brain (`brand-brain/vi-cuon.md`) is not yet complete. The following data is missing and must be confirmed by Owner before any output can go to production:

| Missing Data | Placeholder Used |
|-------------|-----------------|
| Exact dish prices | `[OWNER_TO_PROVIDE_PRICE]` |
| Physical address | `[OWNER_TO_PROVIDE_ADDRESS]` |
| Opening hours | `[OWNER_TO_PROVIDE_OPENING_HOURS]` |
| Combo/offer details | `[OWNER_TO_PROVIDE_OFFER]` |
| Delivery app names | `[OWNER_TO_PROVIDE]` |
| Delivery coverage area | `[OWNER_TO_PROVIDE_DELIVERY_AREA]` |

**Why placeholders instead of guesses:**
- Incorrect prices in content damage brand credibility.
- Wrong address causes customer frustration.
- Fake offers or promotions violate compliance rules.
- Inventing brand data would make the samples useless for production — they would need to be completely rewritten anyway.

Placeholders make the gaps visible and actionable. Once Owner fills them, the samples become production-ready with minimal changes.

---

## How Samples Should Be Refreshed After Owner Updates Brand Data

When Owner confirms real data:

1. **Update Brand Brain:** Fill the `[FILL]` and placeholder fields in `brand-brain/vi-cuon.md`, `01_BRAIN/menu_brain.md`, and `01_BRAIN/customer_brain.md`.
2. **Regenerate samples:** Re-run each module agent against the updated Brand Brain. The agent follows the same SOP — just with real data substituted for placeholders.
3. **Do not manually patch samples:** Avoid editing samples by hand with real data — regenerate via the agent so the full SOP path is exercised.
4. **Re-submit for approval:** All refreshed samples start at `Draft` again and require Owner approval before use.

Refreshed samples should be versioned by date in the filename or frontmatter (e.g., `content-sample-20260601.md`) to distinguish from earlier placeholder versions.

---

## No Runtime Automation in Phase 5

Phase 5 is a manual demonstration of the system. It does not:
- Create n8n workflows or automation nodes.
- Write Python, JavaScript, or other runtime scripts.
- Connect to any external API (Facebook, TikTok, Zalo, GrabFood, etc.).
- Store or process real customer data.
- Trigger any real publishing, messaging, or ad action.

Automation wiring happens in Phase 6 and beyond, using Phase 5 samples as the validated contract for what each n8n node should produce.

---

## No Auto-Post, Auto-Reply, or Ads Spend

All Phase 5 sample outputs are marked `approval_status: Draft`.

- No content output may be posted without Owner changing status to `Approved`.
- No CRM sequence may be sent without `human_review_required: true` satisfied and Owner `Approved`.
- No inbox reply may be posted without Owner review and `Approved`.
- No ads pack may be launched without Owner `Approved` and manual campaign setup in Ads Manager.
- No budget is allocated or spent at any point in Phase 5.

---

## Sample Output Registry

| File | Module | Samples |
|------|--------|---------|
| `samples/vi-cuon/content-sample.md` | Content Auto | 3 (Facebook post, TikTok script, 3-post calendar) |
| `samples/vi-cuon/creative-brief-sample.md` | Creative Asset Auto | 2 (food photo brief, TikTok video brief) |
| `samples/vi-cuon/ads-pack-sample.md` | Ads Pack Auto | 2 (TOF awareness, BOF message conversion) |
| `samples/vi-cuon/crm-followup-sample.md` | CRM Follow-Up Auto | 2 (new lead, lapsed reactivation) |
| `samples/vi-cuon/comment-inbox-reply-sample.md` | Comment Inbox Assistant | 5 (menu, price, address, booking, delivery) |
| `samples/vi-cuon/approval-status-sample.md` | Approval & Publishing | 5 (one per module) |
| `samples/vi-cuon/log-entry-sample.md` | Log (all modules) | 4 (phase start, content, brief, phase complete) |

---

## Related Files

- Brand Brain: `brand-brain/vi-cuon.md`
- Schema contracts: `schemas/*.schema.json`
- Module SOPs: `module-sops/*.md`
- Output templates: `templates/*.md`
- Module SOP system: `docs/11_MODULE_SOP_SYSTEM.md`
- Template system: `docs/12_OUTPUT_TEMPLATE_SYSTEM.md`
