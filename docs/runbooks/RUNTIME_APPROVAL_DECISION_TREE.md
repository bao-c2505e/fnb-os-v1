# Runtime Approval Decision Tree — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 24A — Sandbox Runbook Index & Owner Runtime Readiness)
Type: Owner-Facing Decision Tree
Audience: Owner (Bo Bao) and Agents (Builder, Reviewer)

---

## Purpose

Use this decision tree to determine what category a proposed action falls into and what approval level it requires. Start at Question 1 and follow the path to a final outcome.

**The outcomes define what is allowed — not what has been approved.** After reaching an outcome, the Owner must still provide an explicit approval phrase before the action proceeds.

---

## Decision Tree

```
START HERE
│
▼
Q1: Is this action DOCUMENTATION ONLY?
    (Creating, editing, or reading markdown files, JSON schemas,
     governance docs, runbooks, handoffs, or logs — with no
     import into n8n, no workflow execution, no API calls)
│
├── YES ──────────────────────────────────────────────────────────────────► OUTCOME 1
│                                                                            Documentation / repo update allowed.
│                                                                            No Owner approval required beyond normal
│                                                                            commit/push gates. Go to commit flow.
│
└── NO ──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                                                                                 │
▼                                                                                                                │
Q2: Is this action SANDBOX IMPORT ONLY?                                                                          │
    (Importing a workflow JSON file into an n8n sandbox/test instance,                                           │
     keeping it INACTIVE, no triggering or executing)                                                            │
│                                                                                                                │
├── YES ──► Q2a: Is the workflow JSON committed and reviewed?                                                    │
│           ├── NO  ──► OUTCOME BLOCKED: Commit workflow JSON first. Then return to Q1.                         │
│           └── YES ──► Q2b: Is there a per-workflow evidence pack / runbook?                                   │
│                       ├── NO  ──► OUTCOME BLOCKED: Create evidence pack first (e.g., Phase 20A, 22A).         │
│                       └── YES ──► Q2c: Has Owner completed OWNER_RUNTIME_READINESS_CHECKLIST.md?              │
│                                   ├── NO  ──► Go complete the checklist first.                                 │
│                                   └── YES ──► Q2d: Has Owner written explicit import approval phrase?         │
│                                               ├── NO  ──► OUTCOME BLOCKED: Write phrase first:                │
│                                               │           "APPROVED FOR SANDBOX IMPORT ONLY —                  │
│                                               │            [workflow name] — [date]"                           │
│                                               └── YES ──► OUTCOME 2                                           │
│                                                           Sandbox import allowed after explicit Owner approval. │
│                                                           Follow SANDBOX_IMPORT_TEST_RUNBOOK.md.               │
│                                                           Workflow must remain INACTIVE after import.          │
│                                                                                                                │
└── NO ──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                                                                                 │
▼                                                                                                                │
Q3: Is this action SANDBOX MANUAL EXECUTION?                                                                     │
    (Manually triggering an INACTIVE workflow in sandbox using dummy data,                                        │
     observing node output, capturing evidence)                                                                  │
│                                                                                                                │
├── YES ──► Q3a: Was sandbox import already completed with PASS result?                                          │
│           ├── NO  ──► OUTCOME BLOCKED: Complete sandbox import first (Q2 above).                               │
│           └── YES ──► Q3b: Does a per-workflow execution runbook exist?                                        │
│                       ├── NO  ──► OUTCOME BLOCKED: Create execution runbook first (e.g., Phase 20B).           │
│                       └── YES ──► Q3c: Has Owner completed OWNER_RUNTIME_READINESS_CHECKLIST.md again?        │
│                                   ├── NO  ──► Go complete the checklist again (separate from import check).   │
│                                   └── YES ──► Q3d: Has Owner written explicit execution approval phrase?      │
│                                               ├── NO  ──► OUTCOME BLOCKED: Write phrase first:                │
│                                               │           "APPROVED FOR SANDBOX MANUAL EXECUTION ONLY —       │
│                                               │            [workflow name] — [date]"                           │
│                                               └── YES ──► Q3e: Does this execution touch real customers?      │
│                                                           ├── YES ──► OUTCOME BLOCKED: Go to Q6.              │
│                                                           └── NO  ──► Q3f: Does it post publicly?             │
│                                                                       ├── YES ──► OUTCOME BLOCKED: Go to Q7.  │
│                                                                       └── NO  ──► Q3g: Does it commit ads?    │
│                                                                                   ├── YES ──► Go to Q8.       │
│                                                                                   └── NO  ──► OUTCOME 3       │
│                                                                                               Sandbox manual   │
│                                                                                               execution        │
│                                                                                               allowed after    │
│                                                                                               explicit Owner   │
│                                                                                               approval.        │
│                                                                                               Follow per-      │
│                                                                                               workflow runbook.│
│
└── NO ─────────────────────────────────────────────────────────────────────────────────────────────────────────┐
                                                                                                                 │
▼                                                                                                                │
Q4: Is this action PRODUCTION RUNTIME?                                                                           │
    (Using real credentials, real customer data, real triggers, production n8n)                                   │
│                                                                                                                │
├── NO  ──► OUTCOME BLOCKED: Clarify what category this action is. Return to Q1.                                 │
└── YES ──► Q4a: Is there a sandbox PASS recorded for this workflow?                                             │
            ├── NO  ──► OUTCOME BLOCKED: Complete sandbox execution first (Q3 above).                            │
            └── YES ──► Q4b: Has Owner written explicit production approval phrase?                              │
                        ├── NO  ──► OUTCOME BLOCKED: Write phrase first:                                         │
                        │           "APPROVED FOR PRODUCTION RUNTIME ONLY —                                       │
                        │            [workflow name] — [date]"                                                    │
                        └── YES ──► Go to Q5–Q9 for each specific risk check.                                   │
                                                                                                                 │
▼ (Only reached after Q4 production approval phrase is written)                                                  │
Q5: Does this action require production credentials?                                                             │
    (OpenAI API key, Meta Ads account, Zalo OA, Google Sheets, GitHub token)                                     │
├── YES ──► Each credential must be explicitly authorized by Owner.                                               │
│           Owner confirms: "CREDENTIAL APPROVED — [credential name] — [date]"                                   │
└── NO  ──► Continue to Q6.                                                                                      │
                                                                                                                 │
▼                                                                                                                │
Q6: Does this action touch real customers?                                                                       │
    (Sending DMs, replying to comments, sending Zalo/Messenger messages)                                         │
├── YES ──► OUTCOME BLOCKED BY DEFAULT.                                                                          │
│           Requires: explicit Gate 7 approval (Customer-Facing Output).                                          │
│           Owner must write: "APPROVED FOR CUSTOMER-FACING OUTPUT — [action] — [date]"                           │
└── NO  ──► Continue to Q7.                                                                                      │
                                                                                                                 │
▼                                                                                                                │
Q7: Does this action post publicly?                                                                              │
    (Facebook post, Instagram post, TikTok post, Zalo content)                                                   │
├── YES ──► OUTCOME BLOCKED BY DEFAULT.                                                                          │
│           Requires: explicit Gate 9 approval (Publishing).                                                      │
│           Owner must write: "APPROVED FOR PUBLISHING — [content item] — [date]"                                 │
└── NO  ──► Continue to Q8.                                                                                      │
                                                                                                                 │
▼                                                                                                                │
Q8: Does this action mutate ads, campaign, or budget?                                                            │
    (Meta Ads, TikTok Ads, Zalo Ads — creating, modifying, or spending)                                          │
├── YES ──► OUTCOME BLOCKED BY DEFAULT.                                                                          │
│           Requires: explicit Gate 8 approval (Ads Spend).                                                      │
│           Owner must write: "APPROVED FOR ADS SPEND — [platform] [amount] — [date]"                             │
└── NO  ──► Continue to Q9.                                                                                      │
                                                                                                                 │
▼                                                                                                                │
Q9: Has Owner explicitly approved this exact runtime action for this session?                                    │
├── NO  ──► OUTCOME BLOCKED: Owner has not approved this session's action.                                       │
│           Write the appropriate approval phrase and return to this tree.                                        │
└── YES ──► OUTCOME 4                                                                                            │
            Production runtime action allowed — only for the specific workflow,                                  │
            action, and date explicitly approved. All conditions Q4–Q9 must be met.                              │
```

---

## Outcome Summary Table

| Outcome | What It Means | Who Authorizes |
|---------|--------------|---------------|
| **OUTCOME 1** — Documentation allowed | Repo/doc-only work. No runtime. Normal commit/push gates apply. | Builder initiates; Owner approves commit/push per normal gates |
| **OUTCOME 2** — Sandbox import allowed after explicit approval | Import into sandbox n8n (INACTIVE). Requires Owner approval phrase. | Owner only |
| **OUTCOME 3** — Sandbox execution allowed after explicit approval | Manual trigger in sandbox with dummy data. Requires Owner approval phrase (separate from import). | Owner only |
| **OUTCOME 4** — Production runtime allowed after explicit approval | Real credentials, real customers, real n8n. Each workflow/action requires its own explicit Owner approval phrase. All Q5–Q9 checks must pass. | Owner only |
| **OUTCOME BLOCKED** | A required precondition is missing. Do not proceed. | N/A — resolve the precondition first |

---

## Default Outcome (No Decision Made)

If you are unsure which outcome applies:

**Default: OUTCOME BLOCKED.**

Stop and clarify. Do not assume an action is allowed because a prior related action was allowed. Every runtime action requires its own explicit Owner approval for that specific action.

---

## Auto-Post / Auto-Reply / Ads Spend — Always Blocked By Default

These three categories of action are **blocked by default** regardless of any other approval:

| Category | Always Blocked Unless... |
|----------|------------------------|
| Auto-post to social media (Facebook, Instagram, TikTok, Zalo) | Owner writes explicit Gate 9 approval phrase for each post |
| Auto-reply to customer messages (DM, comment, Zalo) | Owner writes explicit Gate 7 approval phrase for each customer interaction |
| Ads spend (Meta Ads, TikTok Ads, Zalo Ads, Google Ads) | Owner writes explicit Gate 8 approval phrase for each campaign and amount |

**No workflow, no automation, and no agent may bypass these defaults.**

---

## Approval Phrases Reference

| Action | Required Phrase |
|--------|----------------|
| Sandbox import | `APPROVED FOR SANDBOX IMPORT ONLY — [workflow name] — [date]` |
| Sandbox execution | `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — [workflow name] — [date]` |
| Production runtime | `APPROVED FOR PRODUCTION RUNTIME ONLY — [workflow name] — [date]` |
| Customer-facing output | `APPROVED FOR CUSTOMER-FACING OUTPUT — [action] — [date]` |
| Publishing | `APPROVED FOR PUBLISHING — [content item] — [date]` |
| Ads spend | `APPROVED FOR ADS SPEND — [platform] [amount] — [date]` |
| Credential authorization | `CREDENTIAL APPROVED — [credential name] — [date]` |

---

## Related Documents

- [OWNER_RUNTIME_READINESS_CHECKLIST.md](OWNER_RUNTIME_READINESS_CHECKLIST.md) — pre-action checklist
- [SANDBOX_RUNBOOK_INDEX.md](SANDBOX_RUNBOOK_INDEX.md) — workflow runbook status
- [SANDBOX_IMPORT_TEST_RUNBOOK.md](SANDBOX_IMPORT_TEST_RUNBOOK.md) — import step-by-step
- [docs/governance/OWNER_APPROVAL_GATE.md](../governance/OWNER_APPROVAL_GATE.md) — formal gate definitions (Gates 5–9)
- [docs/governance/AGENT_OPERATION_RULES.md](../governance/AGENT_OPERATION_RULES.md) — no-runtime policy

---

*FnB OS V1 — Vị Cuốn Growth OS*
*This decision tree is documentation-only. Reaching an "allowed" outcome does not authorize the action — explicit Owner approval phrase is always required.*
