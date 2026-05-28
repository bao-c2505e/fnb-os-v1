# 07 — Agent Prompt System

Version: 1.0
Created By: Claude Code (Builder) — 2026-05-28
Phase: 2

---

## Purpose

The Agent Prompt System defines how AI agents collaborate inside FnB OS V1 to produce safe, approved, brand-consistent marketing output. Each agent has a fixed role, defined inputs and outputs, and cannot take action outside its guardrails without Owner approval.

This document is the master reference for:
- What agents exist and what they do
- How brand context is injected and replaced
- What every agent must receive (input contract)
- What every agent must deliver (output contract)
- How the approval gate works
- How logging and handoff work
- Session limits

---

## Agent Map

| Agent ID | Name | Role | File |
|----------|------|------|------|
| AGT-01 | Chief Architect (ChatGPT) | System design, phase planning | `agents/chief-architect.md` |
| AGT-02 | Builder (Claude Code) | File execution, build | `agents/builder-claude-code.md` |
| AGT-04 | Reviewer (Codex) | Quality gate, review | `agents/reviewer-codex.md` |
| AGT-10 | Content Agent | Content drafts (posts, scripts, captions) | `agents/content-agent.md` |
| AGT-11 | Creative Asset Agent | Creative briefs, AI image/video prompts | `agents/creative-asset-agent.md` |
| AGT-12 | Ads Pack Agent | Ad angles, copy, campaign notes | `agents/ads-pack-agent.md` |
| AGT-13 | CRM Follow-up Agent | Lead sequences, customer care drafts | `agents/crm-followup-agent.md` |
| AGT-14 | Comment / Inbox Agent | Reply drafts for comments and DMs | `agents/comment-inbox-agent.md` |
| AGT-15 | Approval + Publishing Agent | Approval state machine, publishing gate | `agents/approval-publishing-agent.md` |

---

## How Brand Brain Replacement Works

**Default brand: Vị Cuốn** (Vietnamese fresh roll restaurant, Vinh, Nghệ An)

FnB OS V1 is designed to be reusable for any F&B brand. The Brand Brain is the only context layer that changes between brands. Agent roles, guardrails, schemas, and approval gates do not change.

### Brand Brain files (Vị Cuốn defaults):

| File | Purpose |
|------|---------|
| `01_BRAIN/brand_brain.md` | Core identity, tone, audience, USPs, contact info |
| `01_BRAIN/target_audience.md` | Audience segments and insights |
| `01_BRAIN/visual_identity.md` | Colors, fonts, photography style |
| `01_BRAIN/competitor_map.md` | Competitive context |
| `02_CONTENT_ENGINE/content_pillars.md` | Content categories and themes |
| `02_CONTENT_ENGINE/offer_engine.md` | Active offers and pricing |

### To deploy for a new F&B brand:

1. Replace or duplicate the Brand Brain files above with the new brand's data.
2. Update `01_BRAIN/brand_brain.md` with the new brand's identity, tone, contact info.
3. Update `02_CONTENT_ENGINE/offer_engine.md` with the new brand's offers.
4. All agents will operate against the new Brand Brain without any other changes.
5. Keep agent role files (`agents/*.md`) unchanged — they are brand-agnostic.

---

## Standard Input Contract

Every agent session must receive:

| Input Field | Required | Description |
|-------------|----------|-------------|
| `brand_brain` | Yes | Path or content of Brand Brain file |
| `active_phase` | Yes | Current phase and command ID |
| `task_brief` | Yes | What this agent is being asked to produce |
| `scope_files` | Yes | Files this agent may touch |
| `platform_target` | Conditional | Required for Content, Creative, Ads agents |
| `offer_reference` | Conditional | Required when output involves pricing or promotion |
| `approval_state` | Conditional | Required for Publishing Agent |

---

## Standard Output Contract

Every agent session must deliver:

| Output Field | Required | Description |
|-------------|----------|-------------|
| `output_files` | Yes | List of files created or modified |
| `status` | Yes | DRAFT / READY_FOR_REVIEW / BLOCKED |
| `approval_state` | Yes | PENDING_REVIEW (default for new output) |
| `validation_notes` | Yes | Any warnings, known gaps, or issues |
| `log_entry` | Yes | Row for `logs/AGENT_ACTIVITY_LOG.md` |
| `handoff_note` | Yes | Summary for `handoff/SESSION_SUMMARY.md` |

---

## Approval Gate Principle

No output from any agent reaches a real customer, platform, or ad system without:

1. Agent self-check → status = READY_FOR_REVIEW
2. Codex Reviewer PASS (for repo changes)
3. **Owner explicit approval** → status = APPROVED
4. Authorized publishing action (Phase 3+ only)

The approval gate cannot be bypassed by any agent.

---

## Logging and Handoff Principle

Every agent session must produce:

| Log File | Entry Type |
|----------|-----------|
| `logs/AGENT_ACTIVITY_LOG.md` | Time \| Agent \| Task \| Action \| Result \| Files |
| `09_LOGS/PHASE_LOG.md` | By \| Status \| Detail |
| `handoff/SESSION_SUMMARY.md` | Session changes, decisions, open issues |
| `handoff/CURRENT_PHASE.md` | Updated phase status |

Logs are the source of truth for all agent actions. Screenshots and verbal notes do not replace logs.

---

## Session Limit Principle

- Maximum 10 interaction turns per agent session.
- At turn 8: agent pauses and updates `handoff/SESSION_SUMMARY.md` with progress, decisions, and open issues.
- At turn 10: agent stops, creates final handoff, delivers end-of-session report.
- The next session resumes from `SESSION_SUMMARY.md` — no context is lost.
- Session limits apply to all agents: Builder, Content Agent, Creative Agent, etc.
