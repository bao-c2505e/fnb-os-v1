# 02_PROMPTS — Agent System Prompts

All agent system prompts are stored here. These are the exact prompts loaded into each AI worker agent at the start of a session.

## Files

| File | Agent | Purpose |
|------|-------|---------|
| `master_system_prompt.md` | All agents | Shared base rules, brand context, safety rules |
| `content_agent_prompt.md` | Content Agent | Generate captions, content packs |
| `design_agent_prompt.md` | Design Agent | Generate design briefs for creatives |
| `ads_agent_prompt.md` | Ads Pack Agent | Generate ads copy and targeting briefs |
| `crm_agent_prompt.md` | CRM Agent | Generate follow-up messages |
| `comment_reply_agent_prompt.md` | Reply Agent | Generate comment and inbox replies |
| `quality_check_prompt.md` | QC Agent | Review and score all agent outputs |

## Rules for Prompt Files
- All prompts must begin with a reference to `master_system_prompt.md`
- Prompts must specify output format (JSON schema reference)
- Prompts must include explicit "do not" rules
- Version number in each file header
- Any prompt change must be logged in `06_HANDOFF/DECISION_LOG.md`

## Prompt Version Format
```
Version: v0.1.0
Last Updated: YYYY-MM-DD
Updated By: [agent or person]
Change: [brief description]
```
