# Content Auto SOP

**Module:** Content Auto
**Agent:** Content Agent (AGT-Content)
**Schema:** `schemas/content-output.schema.json`
**Template:** `templates/content-output-template.md`
**Brand Reference:** `brand-brain/vi-cuon.md`

---

## Purpose

Guide the Content Agent to produce captions, hooks, video scripts, content calendar drafts, and ideas that match the Vị Cuốn brand and are ready for Owner review. No content is published without Approved status.

---

## Required Inputs

| Input | Source | Required |
|-------|--------|----------|
| Brand Brain | `brand-brain/vi-cuon.md` | Yes |
| Content type | Owner brief or command | Yes |
| Platform | Owner brief or command | Yes |
| Target audience segment | Owner brief or `brand-brain/vi-cuon.md` | Yes |
| Offer details | Owner-provided or `[OWNER_TO_PROVIDE_OFFER]` | If campaign includes offer |

---

## Process Steps

1. Read `brand-brain/vi-cuon.md` — confirm brand name, tone, content pillars, and compliance rules before drafting.
2. Identify content type, platform, and target audience from the input brief.
3. Draft a hook (attention-grabbing, 1–2 seconds, based on Brand Brain content pillars).
4. Draft caption (hook + body + CTA).
5. If video: draft script with scene breakdown and voiceover cues.
6. If offer is required: insert `[OWNER_TO_PROVIDE_OFFER]` unless Owner has confirmed offer text.
7. Fill all required fields from `schemas/content-output.schema.json`.
8. Set `approval_status: Draft`.
9. Set `created_by_agent: Content Agent (AGT-Content)`.
10. Output using `templates/content-output-template.md`.

---

## Output Template

`templates/content-output-template.md`

---

## Approval Gate

- Agent sets `approval_status: Draft` on all outputs.
- Agent may advance to `Ready for Review` only after self-check passes (all required fields filled, no hardcoded prices without Owner confirmation, no false claims).
- Only Owner may set `Approved`.
- `Published` and `Scheduled` require prior `Approved` — never advance directly from Draft.
- No direct publishing — never call any publish API or post action.

---

## Logging Requirements

After each output:
- Add one row to `logs/AGENT_ACTIVITY_LOG.md`.
- Add one entry to `09_LOGS/PHASE_LOG.md` if this is a phase milestone.
- Use `templates/log-entry-template.md` for structured log format.

---

## Human Escalation Rules

Stop and escalate to Owner (do not draft) if:
- Offer price or promotion details are needed but not confirmed by Owner.
- Content requires claims about health, nutrition, or awards not found in Brand Brain.
- Content involves legal terms, refund policies, or regulatory notices.
- Target audience segment is unclear or not found in Brand Brain.
- Input brief contradicts Brand Brain tone or compliance rules.

---

## Done Criteria

- All required schema fields are filled (no empty required fields).
- `approval_status` is `Draft` or `Ready for Review`.
- No hardcoded prices unless Owner-confirmed.
- No publish action taken.
- Log entry written in `logs/AGENT_ACTIVITY_LOG.md`.
