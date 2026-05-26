# Command — CMD-[PHASE]-[SEQ]

Created By: [ChatGPT / Owner / Agent ID] — [YYYY-MM-DD]

---

## Command Metadata

| Field | Value |
| --- | --- |
| `command_id` | CMD-[PHASE]-[SEQ] |
| `phase` | [e.g. 0.6] |
| `created_by` | [ChatGPT / Owner / Agent ID] |
| `assigned_builder` | [e.g. Claude Code / Codex] |
| `assigned_reviewer` | [e.g. Codex / ChatGPT] |
| `priority` | [high / medium / low] |
| `status` | NEW |
| `review_required` | true |
| `approval_required` | true |

---

## Owner Request

[Plain-language description of what the Owner or ChatGPT wants done. One to three sentences. No screenshots — reference repo files, logs, or exact error text.]

---

## Scope Files

Files the Builder is allowed to create or modify:

- [exact/file/path.md]
- [exact/folder/]

---

## Forbidden Actions

- Do not hardcode API keys, tokens, passwords, or secrets.
- Do not auto-post, auto-reply, activate workflows, deploy, or spend money.
- Do not modify files outside Scope Files.
- Do not commit unless explicitly stated in this command.
- Do not open the next phase.

---

## Acceptance Criteria

- [ ] [Specific, testable condition — what does DONE look like?]
- [ ] [Another condition]

---

## Output Required

- [e.g. Patch to commands/COMMAND_INBOX.md]
- [e.g. Updated handoff/CURRENT_PHASE.md with status BUILDER_DONE_PENDING_REVIEW]
- [e.g. git status output showing only expected files changed]

---

## Handoff Required

true — Builder must update `handoff/CURRENT_PHASE.md`, `handoff/SESSION_SUMMARY.md`, and `logs/AGENT_ACTIVITY_LOG.md` before moving to `BUILDER_DONE`.

---

## Log Required

true — Builder must append an entry to `09_LOGS/PHASE_LOG.md` before moving to `BUILDER_DONE`.

---

## Notes

[Optional context. Do not include secrets. Reference external docs by URL or repo path only.]
