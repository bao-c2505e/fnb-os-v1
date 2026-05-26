# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.10)

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.10-001

**Created By:** ChatGPT (Chief Architect) — 2026-05-26
**Updated By:** Claude Code (Builder) — 2026-05-26

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.10-001 |
| `phase` | 0.10 |
| `objective` | Define Active Command Inference so agents can execute one-line shortcuts with zero additional context from Owner |
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
Make one-line commands fully operational. Owner must be able to type only `RUN_CURRENT_COMMAND` to Claude and `REVIEW_CURRENT_COMMAND` to Codex — no phase number, no command ID, no context pasted. Define the Active Command Inference Algorithm (how agents find the active command from COMMAND_INBOX.md), document end-to-end flows for both shortcuts, and update all agent protocols to reference the inference spec.

**Scope Files:**
- `docs/phase-0/PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md`
- `commands/CURRENT_COMMAND.md`
- `commands/COMMAND_SHORTCUTS.md`
- `commands/COMMAND_INBOX.md`
- `commands/COMMAND_STATUS.md`
- `commands/COMMAND_ROUTING_RULES.md`
- `agents/AGENT_RUN_PROTOCOL.md`
- `agents/BUILDER_PROTOCOL.md`
- `agents/REVIEWER_PROTOCOL.md`
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
- Do not automate or script the inference algorithm.

**Acceptance Criteria:**
- [ ] Owner can tell Claude only `RUN_CURRENT_COMMAND` and Claude infers active command without additional context
- [ ] Owner can tell Codex only `REVIEW_CURRENT_COMMAND` and Codex infers active command without additional context
- [ ] `PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md` explains inference algorithm and end-to-end flows for both shortcuts
- [ ] `commands/CURRENT_COMMAND.md` exists as single-file active command pointer with update protocol
- [ ] `COMMAND_SHORTCUTS.md` has Active Command Inference section (10-step algorithm) + Owner usage examples
- [ ] `COMMAND_ROUTING_RULES.md` has Active Command Inference section
- [ ] `AGENT_RUN_PROTOCOL.md` Session Start Checklist references inference
- [ ] `BUILDER_PROTOCOL.md` Step 1 and `REVIEWER_PROTOCOL.md` Identity Check reference inference spec
- [ ] `REVIEWER_PROTOCOL.md` has `PASS_WITH_NOTES` result option and importability check (Step 6b)
- [ ] CMD-0.10-001 in COMMAND_INBOX.md and COMMAND_STATUS.md; CMD-0.9-001 CLOSED (commit fd9c750)
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.10 file

**Output Required:**
- 1 new file: `docs/phase-0/PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md`
- Updated: `commands/COMMAND_SHORTCUTS.md`, `commands/COMMAND_ROUTING_RULES.md`
- Updated: `agents/AGENT_RUN_PROTOCOL.md`, `agents/BUILDER_PROTOCOL.md`, `agents/REVIEWER_PROTOCOL.md`
- Updated: `commands/COMMAND_INBOX.md`, `commands/COMMAND_STATUS.md`, handoff files, logs
- Final output ending with: `READY FOR CODEX REVIEW`

---

### CMD-0.9-001

**Closed By:** Owner — 2026-05-26 (commit fd9c750)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.9-001 |
| `phase` | 0.9 |
| `status` | **CLOSED** |
| `commit` | fd9c750 |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*

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
