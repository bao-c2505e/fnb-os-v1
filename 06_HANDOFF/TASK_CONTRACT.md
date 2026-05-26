# Task Contract Format — FnB OS V1

**Version:** v0.1.0
**Last Updated:** 2026-05-26

---

## Purpose
A Task Contract is how the Chief Architect (ChatGPT) assigns work to a Builder Agent (Claude Code, Codex, Gemini).

Every task must have a contract. Agents do not start work without one.

---

## Task Contract Format

```markdown
# Task Contract — [TASK-ID]

**Assigned To:** [Agent Name]
**Assigned By:** [Chief Architect / User]
**Phase:** [Phase number]
**Priority:** [High / Medium / Low]
**Created:** [YYYY-MM-DD]
**Deadline:** [YYYY-MM-DD or N/A]

## Goal
[1–2 sentence description of what must be achieved]

## Inputs
- [File or data the agent needs to read]
- [File or data the agent needs to read]

## Expected Outputs
- [Exact file path or object to create]
- [Exact file path or object to create]

## Acceptance Criteria
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]

## Hard Constraints
- [What the agent must NOT do]
- [What the agent must NOT do]

## Schema References
- [Schema file path if applicable]

## Related Files
- [Other files to read for context]

## Success Condition
[Exact condition that signals this task is complete]

## Status
[ ] Not Started
[ ] In Progress
[ ] Complete — awaiting review
[ ] Approved
[ ] Rejected — reason: [reason]
```

---

## Active Tasks

| Task ID | Agent | Phase | Status | Created |
|---------|-------|-------|--------|---------|
| TASK-001 | Claude Code (Builder) | 0 | ✅ Complete | 2026-05-26 |

---

## Task ID Format
`TASK-[SEQ]` — sequential, never reused

---

## TASK-001 — Phase 0 Foundation Build

**Assigned To:** Claude Code (Builder)
**Assigned By:** Human (User)
**Phase:** 0
**Priority:** High
**Created:** 2026-05-26

### Goal
Create the complete FnB OS V1 repo structure with all foundation files, schemas, prompts, SOPs, and checklists as specified in the Phase 0 brief.

### Expected Outputs
- All files in folders 00_README through 09_LOGS created
- All `[FILL]` placeholders used where real data is not yet available
- No hardcoded credentials anywhere

### Acceptance Criteria
- [ ] All 60+ files created per spec
- [ ] All JSON schemas valid
- [ ] All HANDOFF files written
- [ ] PHASE_STATUS.md updated to reflect completion
- [ ] DECISION_LOG.md has at least one entry

### Status
✅ In Progress → Complete
