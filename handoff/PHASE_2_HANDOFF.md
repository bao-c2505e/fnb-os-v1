# Phase 2 Handoff

Phase: 2 — Agent Prompts + SOP
Created By: Claude Code (Builder, AGT-02)
Date: 2026-05-28
Status: BUILDER_DONE_PENDING_REVIEW

---

## Goal

Create reusable agent prompt files and SOP documentation for FnB OS V1. Define roles, missions, inputs, outputs, guardrails, and approval requirements for all agents in the system. Ensure the system is reusable for any F&B brand by replacing Brand Brain context only.

---

## Files Created

| File | Description |
|------|-------------|
| `agents/chief-architect.md` | ChatGPT Chief Architect — system design, phase planning |
| `agents/builder-claude-code.md` | Claude Code Builder — file execution, scope, handoff |
| `agents/reviewer-codex.md` | Codex Reviewer — quality gate, PASS/FAIL verdict |
| `agents/content-agent.md` | Content Agent — posts, scripts, captions, hooks |
| `agents/creative-asset-agent.md` | Creative Asset Agent — briefs, AI prompts, QA checklists |
| `agents/ads-pack-agent.md` | Ads Pack Agent — ad angles, copy, campaign notes (draft only) |
| `agents/crm-followup-agent.md` | CRM Follow-up Agent — lead sequences, customer care drafts |
| `agents/comment-inbox-agent.md` | Comment/Inbox Agent — reply drafts, escalation rules |
| `agents/approval-publishing-agent.md` | Approval + Publishing Agent — state machine, publishing gate |
| `docs/07_AGENT_PROMPT_SYSTEM.md` | Agent system overview, brand replacement, I/O contracts |
| `docs/08_PHASE_2_SOP.md` | Phase 2 workflow SOP, roles, forbidden actions |
| `handoff/PHASE_2_HANDOFF.md` | This file |

---

## Scope Completed

- [x] 9 agent prompt files created (chief-architect through approval-publishing)
- [x] Each agent file has all 7 required sections: Role, Mission, Inputs, Outputs, Guardrails, Approval Requirements, Done Criteria
- [x] Brand replacement mechanism documented in `docs/07_AGENT_PROMPT_SYSTEM.md`
- [x] Standard input/output contracts defined
- [x] Approval gate principle documented
- [x] Logging/handoff principle documented
- [x] Session limit principle documented
- [x] Phase 2 SOP covers full workflow: plan → approve → build → validate → review → approve commit
- [x] Owner role clarified: approves only, does not debug manually
- [x] All forbidden actions listed (n8n, code, auto-post, auto-reply, ads, commit before PASS)

---

## Validation Checklist

| Check | Result |
|-------|--------|
| All 12 files created at correct paths | PASS |
| Each agent file has 7 required sections | PASS |
| No secrets / API keys / tokens in any file | PASS |
| No n8n workflow JSON / executable code | PASS |
| No auto-post / auto-reply / ads mechanisms | PASS |
| Brand replacement approach documented | PASS |
| Approval gate documented in every agent | PASS |
| Escalation paths defined where required | PASS |
| Markdown structure is valid | PASS |
| No files outside scope_files were touched | PASS |

---

## Known Limitations

1. **Approval state machine** — `agents/approval-publishing-agent.md` defines the SOP but no automation logic exists yet. SCHEDULED and PUBLISHED states are Phase 3+ only.
2. **CRM sequences** — no real CRM platform connection. Drafts only. Platform integration is Phase 3+.
3. **Comment/Inbox Agent** — no live social platform connection. Operates on copy-pasted messages only. Automation is Phase 3+.
4. **Brand Brain gaps** — `01_BRAIN/brand_brain.md` still has `[FILL]` placeholders (address, phone, some offer prices). These must be filled by Owner before agents can produce accurate output.
5. **Agent IDs AGT-03, AGT-05–AGT-09** — reserved for future agents (LangGraph orchestrator, Gemini, etc.). Not defined in Phase 2.

---

## Codex Review Instructions

Codex: Review all 12 files listed in the Files Created section above.

Check for the 5 FAIL conditions:
1. Secret / API key / token / password leak — scan all created files
2. Out-of-scope runtime code / n8n workflow / scripts
3. Auto-post / auto-reply / ads spend mechanism
4. Missing required files (all 12 must be present)
5. Broken repo structure (log/handoff entries must exist)

Expected verdict: PASS — no blockers present in Phase 2 markdown-only build.

If PASS WITH NOTES: list observations. Owner may approve with awareness of notes.
If FAIL: identify specific file and line. Builder will fix before resubmission.

---

## Next Phase Recommendation

Recommended next phases (Chief Architect to confirm order):

**Phase 2.3 — Brand Brain Gap Fill**
- Owner fills `[FILL]` placeholders in `01_BRAIN/brand_brain.md` and `02_CONTENT_ENGINE/offer_engine.md`
- Unblocks 9/10 queue items in content pipeline

**Phase 2.4 — Content Agent First Run**
- Run Content Agent against filled Brand Brain
- Produce first batch of content drafts for Owner review

**Phase 3.x — Automation Layer**
- n8n workflow integration
- Telegram approval gate
- Scheduled publishing (after Owner authorizes)

---

## Commit Instruction

**DO NOT COMMIT until:**
1. Codex review is complete with PASS or PASS WITH NOTES verdict
2. Owner gives explicit `OWNER_APPROVED` on this phase

After Owner approval:
```
git add agents/chief-architect.md agents/builder-claude-code.md agents/reviewer-codex.md agents/content-agent.md agents/creative-asset-agent.md agents/ads-pack-agent.md agents/crm-followup-agent.md agents/comment-inbox-agent.md agents/approval-publishing-agent.md docs/07_AGENT_PROMPT_SYSTEM.md docs/08_PHASE_2_SOP.md handoff/PHASE_2_HANDOFF.md handoff/CURRENT_PHASE.md handoff/SESSION_SUMMARY.md logs/AGENT_ACTIVITY_LOG.md 09_LOGS/PHASE_LOG.md
git commit -m "feat(phase-2): create agent prompt files and SOP docs"
```

Do not `git push` until Owner confirms.
