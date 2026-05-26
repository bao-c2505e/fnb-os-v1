# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.8)

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.8-001

**Created By:** ChatGPT (Chief Architect) — 2026-05-26
**Updated By:** Claude Code (Builder) — 2026-05-26

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.8-001 |
| `phase` | 0.8 |
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
Build the GitHub Command Bridge — a protocol that lets Owner/ChatGPT issue structured commands via the repo or GitHub Issues, so agents read from a source of truth rather than from chat prompts. Must define two command modes (repo file vs. GitHub Issue), a GitHub Issue template, routing rules, and error conditions. No GitHub API calls in Phase 0.8 — design and templates only.

**Scope Files:**
- `docs/phase-0/PHASE_0_8_GITHUB_COMMAND_BRIDGE.md`
- `commands/GITHUB_COMMAND_BRIDGE.md`
- `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`
- `commands/COMMAND_ROUTING_RULES.md`
- `commands/COMMAND_INBOX.md`
- `commands/COMMAND_STATUS.md`
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
- Do not call the GitHub API — templates and protocol design only.

**Acceptance Criteria:**
- [ ] `PHASE_0_8_GITHUB_COMMAND_BRIDGE.md` explains problem, objective, two modes, flow, and what is out of scope
- [ ] `GITHUB_COMMAND_BRIDGE.md` defines mode decision guide, field mapping, status-to-label mapping, ownership rules, close conditions
- [ ] `GITHUB_ISSUE_COMMAND_TEMPLATE.md` provides complete Issue template matching all command fields
- [ ] `COMMAND_ROUTING_RULES.md` defines routing by agent, no-concurrent-edit rule, NEED_COMMAND_CLARIFICATION / SCOPE_CONFLICT / SECRET_RISK error conditions
- [ ] CMD-0.8-001 created in COMMAND_INBOX.md and COMMAND_STATUS.md
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.8 file

**Output Required:**
- 4 new files: PHASE_0_8 doc, GITHUB_COMMAND_BRIDGE, GITHUB_ISSUE_COMMAND_TEMPLATE, COMMAND_ROUTING_RULES
- Updated COMMAND_INBOX.md and COMMAND_STATUS.md
- Updated handoff, logs, and NEXT_ACTIONS
- Final output ending with: `READY FOR CODEX REVIEW`

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
