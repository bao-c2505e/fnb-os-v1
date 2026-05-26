# Command Inbox

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) - 2026-05-26

This is the canonical intake queue for commands from ChatGPT Chief Architect or Owner to Builder agents.

Rules:

- Add new commands at the top of the inbox.
- Each command must conform to `schemas/command.schema.json`.
- Builder agents must not start work on a command until Owner or ChatGPT moves it to `ASSIGNED`.
- Do not include API keys, tokens, passwords, customer secrets, or private credentials.
- Do not paste screenshots as the only source of truth; reference repo files, logs, or exact error text.

## Inbox

---

### CMD-0.7-001

**Created By:** ChatGPT (Chief Architect) — 2026-05-26
**Updated By:** Claude Code (Builder) — 2026-05-26 (REVIEW_FAIL fix: added command record)

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.7-001 |
| `phase` | 0.7 |
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
Build the Agent Run Protocol — the operational layer that tells agents how to pick up a command, execute safely, log activity, produce a handoff, and stop correctly. Must cover Builder protocol, Reviewer protocol, session limit rule, and approval gate. No content to duplicate from Phase 0.5/0.6 infrastructure — cross-reference by path only.

**Scope Files:**
- `agents/AGENT_RUN_PROTOCOL.md`
- `agents/BUILDER_PROTOCOL.md`
- `agents/REVIEWER_PROTOCOL.md`
- `agents/SESSION_LIMIT_RULE.md`
- `docs/phase-0/PHASE_0_7_AGENT_RUN_PROTOCOL.md`
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
- [ ] `agents/AGENT_RUN_PROTOCOL.md` covers: session start checklist, execution constraints, stop conditions, pre-BUILDER_DONE checklist, mandatory output format
- [ ] `agents/BUILDER_PROTOCOL.md` covers: 7-step Builder workflow, scope lock, allowed/forbidden status transitions
- [ ] `agents/REVIEWER_PROTOCOL.md` covers: 6 checks (acceptance criteria, scope, secrets, role conflict, safety), unambiguous PASS/FAIL output
- [ ] `agents/SESSION_LIMIT_RULE.md` covers: 10-turn cap, turn 8 checkpoint, 7 required SESSION_SUMMARY fields, resume protocol
- [ ] No content duplicated from Phase 0.5/0.6 infrastructure
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.7 file

**Output Required:**
- 4 protocol files under `agents/`
- Phase doc under `docs/phase-0/`
- Updated handoff, logs, and NEXT_ACTIONS
- Final output ending with: `READY FOR CODEX REVIEW`

---

*For next command, use `commands/COMMAND_TEMPLATE.md`.*
