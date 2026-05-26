# Phase 0.10 — One-Line Agent Commands

Created By: Claude Code (Builder) — 2026-05-26

---

## Problem Being Solved

After Phase 0.9, six shortcuts exist. But a gap remains: when Owner types `RUN_CURRENT_COMMAND`, an agent still needs to know *which* command is active. Without a formal inference rule, the agent might ask a clarifying question, or read the wrong command if multiple are present.

Phase 0.10 closes this gap by defining the **Active Command Inference Algorithm** — the exact steps an agent uses to identify the current command from `commands/COMMAND_INBOX.md` with zero additional input from Owner.

After Phase 0.10, these two lines are the complete session start protocol:

```
Owner → Claude Code:  RUN_CURRENT_COMMAND
Owner → Codex:        REVIEW_CURRENT_COMMAND
```

No phase number. No command ID. No context pasted. Agent reads everything from the repo.

---

## Objective

1. Define the Active Command Inference Algorithm so every agent can find the active command without Owner providing a command ID.
2. Document the exact reading sequence an agent follows when receiving only a shortcut token.
3. Update all agent protocols and shortcut definitions to reference the inference spec.
4. Ensure the inference algorithm is unambiguous for any future command history depth.

**Phase 0.10 does NOT automate any execution.** The inference algorithm is a reading protocol for agents — not a script, not an API call.

---

## Active Command Inference Algorithm

When an agent receives a shortcut token and no other context, it must identify the active command using this algorithm:

```
Step 1 — Open commands/COMMAND_INBOX.md
Step 2 — Scan records from top to bottom
Step 3 — Find the FIRST record that is NOT a CLOSED stub
           (A CLOSED stub contains: status = CLOSED or **CLOSED**)
Step 4 — Read that record's status field
Step 5 — Check: does the status match the shortcut's required trigger status?
           RUN_CURRENT_COMMAND  → requires ASSIGNED or IN_PROGRESS
           REVIEW_CURRENT_COMMAND → requires REVIEW_REQUESTED
           FIX_REVIEW_FAIL       → requires REVIEW_FAIL
           CLOSE_APPROVED_COMMAND → requires OWNER_APPROVED
           CREATE_SESSION_SUMMARY → any status
           SHOW_CURRENT_STATUS    → any status
Step 6 — If YES: this is the active command. Read all fields.
Step 7 — If NO: report the mismatch to Owner.
           Example: "Found CMD-0.10-001 with status REVIEW_REQUESTED,
                     but RUN_CURRENT_COMMAND requires ASSIGNED or IN_PROGRESS."
Step 8 — Verify assigned_builder or assigned_reviewer matches your identity.
           If mismatch → ROLE_CONFLICT → stop and report.
Step 9 — Read scope_files, forbidden_actions, acceptance_criteria.
Step 10 — Execute the shortcut action list.
```

**Why top-to-bottom, first non-CLOSED?**
`COMMAND_INBOX.md` is maintained with new commands at the top and CLOSED stubs below. The first non-CLOSED record is always the most recent active command. This requires no search by ID — just scan and stop at the first active record.

---

## What Changes After Phase 0.10

| Before Phase 0.10 | After Phase 0.10 |
|-------------------|------------------|
| Owner types shortcut; agent may ask "which command?" | Agent infers active command from COMMAND_INBOX.md automatically |
| Builder needs phase number or CMD-ID to start | Builder reads first non-CLOSED record in COMMAND_INBOX.md |
| Reviewer needs to know which phase is under review | Reviewer finds first REVIEW_REQUESTED record at top of COMMAND_INBOX.md |
| Status mismatch is silent or ambiguous | Agent reports exact mismatch: "found [status], need [required]" |

---

## How RUN_CURRENT_COMMAND Works (End-to-End)

Owner types:
```
RUN_CURRENT_COMMAND
```

Agent (Claude Code) executes:
```
1. Read commands/COMMAND_SHORTCUTS.md → resolve token to action list
2. Open commands/COMMAND_INBOX.md → scan top to bottom
3. First non-CLOSED record: CMD-0.10-001, status ASSIGNED
4. Status matches trigger (ASSIGNED) → this is the active command
5. Confirm assigned_builder: Claude Code → matches my identity → proceed
6. Read scope_files, forbidden_actions, acceptance_criteria from CMD-0.10-001
7. Announce: SCOPE LOCK — CMD-0.10-001 [list scope_files]
8. Execute acceptance_criteria within scope_files
9. Update handoff/CURRENT_PHASE.md, handoff/SESSION_SUMMARY.md, logs
10. Run git status --short and secret scan
11. Move status: IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED
12. Output ends: READY FOR CODEX REVIEW
```

Owner never provides CMD-0.10-001. Agent infers it from the repo.

---

## How REVIEW_CURRENT_COMMAND Works (End-to-End)

Owner types:
```
REVIEW_CURRENT_COMMAND
```

Agent (Codex) executes:
```
1. Read commands/COMMAND_SHORTCUTS.md → resolve token to action list
2. Open commands/COMMAND_INBOX.md → scan top to bottom
3. First non-CLOSED record: CMD-0.10-001, status REVIEW_REQUESTED
4. Status matches trigger (REVIEW_REQUESTED) → this is the active command
5. Confirm assigned_reviewer: Codex → matches identity → proceed
6. Read output_required from CMD-0.10-001
7. Open and read every file listed in output_required
8. Read handoff/SESSION_SUMMARY.md — Builder's session notes
9. Evaluate each acceptance_criteria: PASS or FAIL with specific reason
10. Run scope check, secret scan, role conflict check, safety check
11. Output: REVIEW RESULT: PASS or FAIL + structured table
```

Owner never provides CMD-0.10-001. Codex infers it from the repo.

---

## Files Delivered

| File | Purpose |
|------|---------|
| `docs/phase-0/PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md` | This file — problem, algorithm, end-to-end flows |
| `commands/CURRENT_COMMAND.md` | New — single-file active command pointer; agents read this for current command without scanning COMMAND_INBOX.md |
| `commands/COMMAND_SHORTCUTS.md` | Updated — Active Command Inference section + Owner usage examples added |
| `commands/COMMAND_ROUTING_RULES.md` | Updated — Active Command Inference section added |
| `agents/AGENT_RUN_PROTOCOL.md` | Updated — inference algorithm reference in session start |
| `agents/BUILDER_PROTOCOL.md` | Updated — Step 1 references inference spec |
| `agents/REVIEWER_PROTOCOL.md` | Updated — Identity Check references inference spec; added PASS_WITH_NOTES result + importability check |

---

## What Phase 0.10 Does NOT Do

- Does not automate shortcut execution
- Does not call any API
- Does not create n8n workflows or GitHub Actions
- Does not open Phase 1

---

## Done Criteria — Phase 0.10

- [x] `PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md` explains problem, inference algorithm, end-to-end flows for RUN and REVIEW
- [x] `commands/CURRENT_COMMAND.md` created — single-file active command pointer with update protocol
- [x] `COMMAND_SHORTCUTS.md` has Active Command Inference section (10-step algorithm) + Owner usage examples
- [x] `COMMAND_ROUTING_RULES.md` has Active Command Inference section
- [x] `AGENT_RUN_PROTOCOL.md` Session Start Checklist references inference
- [x] `BUILDER_PROTOCOL.md` Step 1 references inference spec
- [x] `REVIEWER_PROTOCOL.md` Identity Check references inference spec; PASS_WITH_NOTES added; importability check (Step 6b) added
- [x] CMD-0.10-001 in `COMMAND_INBOX.md` and `COMMAND_STATUS.md`; CMD-0.9-001 CLOSED (commit fd9c750)
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.10 file
