# 06_HANDOFF — Agent Communication & Session Management

This folder is the control center for agent-to-agent communication, session continuity, and decision tracking.

## Files

| File | Purpose | Updated By |
|------|---------|-----------|
| `AGENT_COMMUNICATION_RULES.md` | How agents communicate with each other | Chief Architect |
| `TASK_CONTRACT.md` | Format for assigning tasks to agents | Chief Architect |
| `SESSION_HANDOFF.md` | Current session state and context | Every agent at session end |
| `SESSION_SUMMARY.md` | Summary after 10-message limit | Every agent at limit |
| `PHASE_STATUS.md` | Current phase progress | Builder agents |
| `DECISION_LOG.md` | All important decisions and rationale | All agents |
| `ERROR_LOG.md` | All errors and resolutions | All agents |
| `NEXT_ACTIONS.md` | Next steps queue | Chief Architect |
| `ACCEPTANCE_CRITERIA.md` | Pass/fail criteria for each phase | Chief Architect |

## Critical Rules
- Every agent session MUST end with an update to `SESSION_HANDOFF.md`
- Every important decision MUST be logged in `DECISION_LOG.md`
- Every error MUST be logged in `ERROR_LOG.md`
- `PHASE_STATUS.md` is the single source of truth for what's complete
- After 10 messages, create `SESSION_SUMMARY.md` update before stopping
