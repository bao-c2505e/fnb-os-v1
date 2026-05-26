# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-27 (Phase 0.13)

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.14-001

**Created By:** Owner — 2026-05-27
**Updated By:** Claude Code (Builder) — 2026-05-27

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.14-001 |
| `phase` | 0.14 |
| `objective` | Static smoke test of shortcut system (Phases 0.10–0.13) before Phase 1 |
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
Run static smoke test on all 7 shortcuts (RUN_CURRENT_COMMAND, REVIEW_CURRENT_COMMAND, APPROVE_CURRENT_PHASE, CLOSE_APPROVED_COMMAND, SHOW_CURRENT_STATUS, CREATE_SESSION_SUMMARY, CREATE_SESSION_HANDOFF). Inspect spec files, verify each shortcut has clear purpose/input/output/safe boundary/handoff behavior. Document results in a phase report file. No destructive actions. No commit or push.

**Scope Files:**
- `docs/phase-0/PHASE_0_14_REPO_STATUS_SMOKE_TEST.md`
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
- Do not open Phase 1.

**Acceptance Criteria:**
- [ ] `docs/phase-0/PHASE_0_14_REPO_STATUS_SMOKE_TEST.md` created with: phase name, scope, files inspected, per-shortcut checklist (PASS/WARNING/FAIL), issues found, recommended fixes, final recommendation
- [ ] All 7 shortcuts verified: RUN_CURRENT_COMMAND, REVIEW_CURRENT_COMMAND, APPROVE_CURRENT_PHASE, CLOSE_APPROVED_COMMAND, SHOW_CURRENT_STATUS, CREATE_SESSION_SUMMARY, CREATE_SESSION_HANDOFF
- [ ] Each shortcut has: clear purpose, expected input, expected output, safe boundary, handoff behavior noted
- [ ] No destructive actions taken — static verification only
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.14 file

**Output Required:**
- 1 new file: `docs/phase-0/PHASE_0_14_REPO_STATUS_SMOKE_TEST.md`
- Updated: `commands/COMMAND_INBOX.md`, `commands/COMMAND_STATUS.md`, handoff files, logs
- Final output ending with: `READY FOR CODEX REVIEW`

---

### CMD-0.13-001

**Closed By:** Owner — 2026-05-27 (commit c014a25)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.13-001 |
| `phase` | 0.13 |
| `status` | **CLOSED** |
| `commit` | c014a25 |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*

---

### CMD-0.12-001

**Closed By:** Owner — 2026-05-26 (commit 36fcfe)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.12-001 |
| `phase` | 0.12 |
| `status` | **CLOSED** |
| `commit` | 36fcfe |

*This command is closed. See `commands/COMMAND_STATUS.md` for history.*

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
