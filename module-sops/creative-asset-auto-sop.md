# Creative Asset Auto SOP

**Module:** Creative Asset Auto
**Agent:** Creative Asset Agent (AGT-Creative)
**Schema:** `schemas/creative-brief.schema.json`
**Template:** `templates/creative-brief-template.md`
**Brand Reference:** `brand-brain/vi-cuon.md`

---

## Purpose

Guide the Creative Asset Agent to produce image, video, and design briefs and AI generation prompts. Output is a brief only — not a final asset. No asset is produced or published without Owner approval.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Brand Brain | `brand-brain/vi-cuon.md` | Yes |
| Asset type | Owner brief or command | Yes |
| Platform and format | Owner brief or command | Yes |
| Marketing objective | Owner brief | Yes |
| Linked content output ID | Content Agent output | If asset is tied to a content piece |
| Real food photography | Owner | If photo-dependent brief |

---

## Process Steps

1. Read `brand-brain/vi-cuon.md` — confirm brand colors, visual style, and tone before drafting.
2. Identify asset type, platform, format, and objective from input.
3. Write creative concept (1–3 sentences describing the core idea).
4. Write detailed visual direction: mood, color palette, lighting, shot composition.
5. If video: write scene description (scene-by-scene breakdown).
6. If applicable: write AI tool prompt safe for use with Midjourney, DALL-E, or Kling.
7. List required inputs before production can begin (e.g., real dish photos, brand palette confirmation).
8. Write QA checklist items.
9. Fill all required fields from `schemas/creative-brief.schema.json`.
10. Set `approval_status: Draft`.
11. Set `created_by_agent: Creative Asset Agent (AGT-Creative)`.
12. Output using `templates/creative-brief-template.md`.

---

## Output Template

`templates/creative-brief-template.md`

---

## Approval Gate

- Agent outputs brief only — no final asset creation or generation.
- Owner must set `Approved` before brief is handed to any designer or AI generation tool.
- No hardcoded prices on visual elements unless Owner-confirmed.
- No unverified health claims or award references in copy overlay or brief.
- `Published` and `Scheduled` require prior `Approved`.

---

## Logging Requirements

- Add one row to `logs/AGENT_ACTIVITY_LOG.md` per brief produced.
- Use `templates/log-entry-template.md` format.

---

## Human Escalation Rules

Stop and escalate to Owner if:
- Real photography is required but not yet supplied by Owner.
- Visual brief includes specific pricing, promotions, or legal terms not in Brand Brain.
- Brand colors, logo, or font files are needed but not confirmed.
- Any competitor comparison or reference is requested.
- Brief requires a model/person's likeness — Owner consent is required.

---

## Done Criteria

- All required schema fields filled.
- `approval_status` is `Draft` or `Ready for Review`.
- AI tool prompt is safe to use (no explicit content, no false claims, no PII).
- No final asset submitted, generated, or auto-delivered.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
