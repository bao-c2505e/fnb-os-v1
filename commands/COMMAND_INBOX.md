# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.12)

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.12-001

**Created By:** Owner — 2026-05-26
**Updated By:** Claude Code (Builder) — 2026-05-26

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.12-001 |
| `phase` | 0.12 |
| `objective` | Expand SHOW_CURRENT_STATUS to write a persistent status snapshot to logs/CURRENT_STATUS.md |
| `created_by` | Owner |
| `assigned_builder` | Claude Code |
| `assigned_reviewer` | Codex |
| `priority` | high |
| `status` | OWNER_APPROVED |
| `review_required` | true |
| `approval_required` | true |
| `handoff_required` | true |
| `log_required` | true |

**Owner Request:**
Expand `SHOW_CURRENT_STATUS` shortcut so it writes a structured status snapshot to `logs/CURRENT_STATUS.md`. Snapshot must include: current phase, active command ID and status, latest commit, working tree state, reviewer state, owner approval state, blockers, and next exact action for Owner/Builder/Reviewer. Must not modify feature files, commit, push, or expose secrets.

**Scope Files:**
- `docs/phase-0/PHASE_0_12_STATUS_SNAPSHOT_SHORTCUT.md`
- `commands/COMMAND_SHORTCUTS.md`
- `commands/COMMAND_ROUTING_RULES.md`
- `logs/CURRENT_STATUS.md`
- `commands/COMMAND_INBOX.md`
- `commands/COMMAND_STATUS.md`
- `commands/CURRENT_COMMAND.md`
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

**Acceptance Criteria:**
- [ ] `SHOW_CURRENT_STATUS` in `COMMAND_SHORTCUTS.md` updated — expanded action list (9 steps), writes `logs/CURRENT_STATUS.md`
- [ ] Snapshot format defined with all 10 required fields: phase, command ID, status, latest commit, working tree, reviewer state, owner approval state, blockers, next actions (Owner/Builder/Reviewer)
- [ ] `SHOW_CURRENT_STATUS` guardrails explicit: only writes `logs/CURRENT_STATUS.md`, no commit/push, no API calls, no secrets
- [ ] `logs/CURRENT_STATUS.md` exists as initial snapshot for Phase 0.12
- [ ] `COMMAND_ROUTING_RULES.md` updated to note `SHOW_CURRENT_STATUS` now writes one file
- [ ] `PHASE_0_12_STATUS_SNAPSHOT_SHORTCUT.md` documents problem, spec, snapshot format, guardrails, done criteria
- [ ] CMD-0.11-001 CLOSED (commit bbda9d1); CMD-0.12-001 in COMMAND_INBOX.md and COMMAND_STATUS.md
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.12 file

**Output Required:**
- 1 new file: `docs/phase-0/PHASE_0_12_STATUS_SNAPSHOT_SHORTCUT.md`
- 1 new file: `logs/CURRENT_STATUS.md`
- Updated: `commands/COMMAND_SHORTCUTS.md`, `commands/COMMAND_ROUTING_RULES.md`
- Updated: `commands/COMMAND_INBOX.md`, `commands/COMMAND_STATUS.md`, handoff files, logs
- Final output ending with: `READY FOR CODEX REVIEW`

---

### CMD-0.11-001

**Closed By:** Owner — 2026-05-26 (commit bbda9d1)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.11-001 |
| `phase` | 0.11 |
| `status` | **CLOSED** |
| `commit` | bbda9d1 |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*

---

### CMD-0.10-001

**Closed By:** Owner — 2026-05-26 (commit 7498c73)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.10-001 |
| `phase` | 0.10 |
| `status` | **CLOSED** |
| `commit` | 7498c73 |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*

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
