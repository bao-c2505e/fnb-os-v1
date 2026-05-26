# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.9)

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.9-001

**Created By:** ChatGPT (Chief Architect) — 2026-05-26
**Updated By:** Claude Code (Builder) — 2026-05-26

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.9-001 |
| `phase` | 0.9 |
| `objective` | Create Command Execution Shortcuts so Owner can trigger any standard agent action with a single token |
| `created_by` | ChatGPT (Chief Architect) |
| `assigned_builder` | Claude Code |
| `assigned_reviewer` | Codex |
| `priority` | high |
| `status` | REVIEW_REQUESTED |
| `review_required` | true |
| `approval_required` | true |
| `handoff_required` | true |
| `log_required` | true |

**Owner Request:**
Build the Command Execution Shortcuts system so Owner no longer needs to paste long role-specific prompts when starting Builder or Reviewer sessions. Define 6 shortcut tokens (RUN_CURRENT_COMMAND, REVIEW_CURRENT_COMMAND, FIX_REVIEW_FAIL, CLOSE_APPROVED_COMMAND, CREATE_SESSION_SUMMARY, SHOW_CURRENT_STATUS), each with exact role, trigger status, action list, and error conditions. Update routing rules and agent protocols to reference shortcuts. Design only — no automation or API calls.

**Scope Files:**
- `commands/COMMAND_SHORTCUTS.md`
- `commands/COMMAND_INBOX.md`
- `commands/COMMAND_STATUS.md`
- `commands/COMMAND_ROUTING_RULES.md`
- `agents/AGENT_RUN_PROTOCOL.md`
- `agents/BUILDER_PROTOCOL.md`
- `agents/REVIEWER_PROTOCOL.md`
- `docs/phase-0/PHASE_0_9_COMMAND_EXECUTION_SHORTCUTS.md`
- `handoff/CURRENT_PHASE.md`
- `handoff/SESSION_SUMMARY.md`
- `06_HANDOFF/NEXT_ACTIONS.md`
- `09_LOGS/PHASE_LOG.md`
- `logs/AGENT_ACTIVITY_LOG.md`

**Forbidden Actions:**
- Do not hardcode API keys, tokens, passwords, or secrets.
- Do not commit or push without `OWNER_APPROVED`.
- Do not auto-post, auto-reply to real users, activate n8n workflows, or run paid ads.
- Do not modify files outside Scope Files.
- Do not open Phase 1 or any subsequent phase.
- Do not call any external API or automate shortcut execution.

**Acceptance Criteria:**
- [ ] `COMMAND_SHORTCUTS.md` defines all 6 shortcuts with role, trigger status, required actions, error conditions, and quick-reference table
- [ ] `COMMAND_ROUTING_RULES.md` has a Shortcut Routing section covering role gating and all 5 error conditions (ROLE_CONFLICT, NO_ACTIVE_COMMAND, NEED_COMMAND_CLARIFICATION, SCOPE_CONFLICT, SECRET_RISK)
- [ ] `BUILDER_PROTOCOL.md` references `RUN_CURRENT_COMMAND` as entry point at Step 1
- [ ] `REVIEWER_PROTOCOL.md` references `REVIEW_CURRENT_COMMAND` as entry point at Identity Check
- [ ] `AGENT_RUN_PROTOCOL.md` describes shortcut layer in integration section
- [ ] CMD-0.9-001 in `COMMAND_INBOX.md` and `COMMAND_STATUS.md`; CMD-0.8-001 marked CLOSED
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.9 file

**Output Required:**
- 1 new file: `commands/COMMAND_SHORTCUTS.md`
- 1 new file: `docs/phase-0/PHASE_0_9_COMMAND_EXECUTION_SHORTCUTS.md`
- Updated: `commands/COMMAND_ROUTING_RULES.md`, `agents/AGENT_RUN_PROTOCOL.md`, `agents/BUILDER_PROTOCOL.md`, `agents/REVIEWER_PROTOCOL.md`
- Updated: `commands/COMMAND_INBOX.md`, `commands/COMMAND_STATUS.md`, handoff files, logs
- Final output ending with: `READY FOR CODEX REVIEW`

---

### CMD-0.8-001

**Closed By:** Owner — 2026-05-26 (commit e58427c)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.8-001 |
| `phase` | 0.8 |
| `status` | **CLOSED** |
| `commit` | e58427c |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*
*Full record archived above for reference only — not an active command.*

---

### CMD-0.7-001

**Created By:** ChatGPT (Chief Architect) — 2026-05-26
**Closed By:** Owner — 2026-05-26 (commit d4771a)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.7-001 |
| `phase` | 0.7 |
| `status` | **CLOSED** |
| `commit` | d4771a |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*
*Full record archived above for reference only — not an active command.*

---

*For next command, use `commands/COMMAND_TEMPLATE.md`.*
