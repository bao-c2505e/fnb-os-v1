# Reviewer Protocol — Codex

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.7

This protocol applies exclusively to Codex acting as Reviewer.
Read `agents/AGENT_RUN_PROTOCOL.md` first — this document adds Reviewer-specific steps only.

---

## Identity Check

Before starting any review session, confirm:

```
My identity: Codex / GPT-4o (AGT-04)
My role this session: Reviewer
My command: CMD-[PHASE]-[SEQ]
My assigned_reviewer field in the command: Codex
```

If `assigned_reviewer` does not match → do not review. Set status `BLOCKED`, record reason, notify Owner.

---

## Step 1 — Read the Command and All Outputs

1. Open `commands/COMMAND_INBOX.md`. Read the command with status `REVIEW_REQUESTED`.
2. Read every field in the command: `scope_files`, `forbidden_actions`, `acceptance_criteria`, `output_required`.
3. Open and read every file listed in `output_required`. Do not skip any.
4. Read `handoff/SESSION_SUMMARY.md` for the Builder's session notes.
5. Read `logs/AGENT_ACTIVITY_LOG.md` — most recent row.
6. State in your first line: Command ID, phase, and files reviewed.

---

## Step 2 — Acceptance Criteria Check

For each item in `acceptance_criteria`, evaluate PASS or FAIL with a specific reason:

```
| # | Criterion | Result | Reason |
|---|-----------|--------|--------|
| 1 | [criterion text] | PASS | [brief evidence] |
| 2 | [criterion text] | FAIL | [exact issue] |
```

One FAIL is enough to return to Builder. Record all failures — do not stop at the first one.

---

## Step 3 — Scope Violation Check

List every file that was created or modified by the Builder (from git status or SESSION_SUMMARY).
Compare against `scope_files` in the command.

```
| File | In scope_files? | Note |
|------|----------------|------|
| [path] | YES / NO | [if NO, describe the violation] |
```

Any file outside `scope_files` without a documented reason is a scope violation → FAIL.

---

## Step 4 — Secret Leak Check

Scan every file in `scope_files` for the following patterns:

- Hardcoded API keys (e.g. `sk-`, `AIza`, `ghp_`, `ya29.`)
- Hardcoded passwords or tokens
- Real credential values (not placeholders)
- Real user data (names, phone numbers, email addresses of real customers)

```
Secret scan result: CLEAN / WARN
[If WARN: file name and pattern found]
```

Any hardcoded secret → FAIL, regardless of other criteria.

---

## Step 5 — Role Conflict Check

Verify the Builder did not perform actions reserved for Reviewer or Owner:

- Did the Builder move status to `REVIEW_PASS`, `OWNER_APPROVED`, or `CLOSED`? → FAIL
- Did the Builder commit or push to git? → FAIL
- Did the Builder self-approve their own output? → FAIL

```
Role conflict check: PASS / FAIL
[If FAIL: describe]
```

---

## Step 6 — Safety Check

Verify none of the following occurred:

- Auto-posting content to any social media or messaging platform
- Auto-replying to real customers or users
- Activating n8n workflows (`active: true`)
- Running paid ads or spending money
- Modifying production data

```
Safety check: PASS / FAIL
[If FAIL: describe]
```

---

## Step 7 — Mandatory Review Output

End every Reviewer session with this exact structure:

```
## REVIEW RESULT: PASS
```
or
```
## REVIEW RESULT: FAIL
```

Followed by:

```
### Acceptance Criteria
| # | Criterion | Result | Reason |
|---|-----------|--------|--------|

### Scope Violation Check
| File | In scope? | Note |

### Secret Scan
Result: CLEAN / WARN

### Role Conflict
Result: PASS / FAIL

### Safety Check
Result: PASS / FAIL

### Summary
[2–3 sentences]
```

If PASS:
```
OWNER CAN APPROVE
Next: Owner moves CMD-[PHASE]-[SEQ] to OWNER_APPROVED, then commits.
```

If FAIL:
```
RETURN TO BUILDER
Issues:
1. [exact issue with file and line if applicable]
2. [...]
Builder must fix and re-submit to REVIEW_REQUESTED.
```

---

## Status Transitions the Reviewer May Make

| From | To | Condition |
|------|----|-----------|
| `REVIEW_REQUESTED` | `REVIEW_PASS` | All checks pass |
| `REVIEW_REQUESTED` | `REVIEW_FAIL` | Any check fails |

The Reviewer must NOT move status to `OWNER_APPROVED` or `CLOSED` — those belong to Owner.
The Reviewer must NOT move status to `IN_PROGRESS` or `BUILDER_DONE` — those belong to Builder.

---

## What the Reviewer Must Never Do

- Rebuild files or rewrite large sections of Builder output
- Make edits to `scope_files` content (add review notes to a separate section only)
- Approve work that has a secret leak, scope violation, or role conflict
- Commit or push
- Auto-post, auto-reply, activate workflows, run ads
- Approve work that does not meet every `acceptance_criteria` item
