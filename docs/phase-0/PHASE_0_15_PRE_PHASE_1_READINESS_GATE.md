# Phase 0.15 — Pre-Phase-1 Readiness Gate

Created By: Claude Code (Builder) — 2026-05-27
Closed By: Owner — 2026-05-27 (blocker-only policy)
Phase: 0.15
Command: CMD-0.15-001
Status: CLOSED

---

## Tên Phase (Phase Name)

Phase 0.15 — Pre-Phase-1 Readiness Gate (Cổng Kiểm Tra Sẵn Sàng Trước Phase 1)

---

## Phạm Vi (Scope)

Đánh giá toàn diện trạng thái sẵn sàng của hệ thống FnB OS V1 trước khi bắt đầu Phase 1 (Marketing Core). Phase này là **gate phase** — không build feature mới, chỉ kiểm tra và báo cáo.

| Hạng mục | Mô tả |
|---------|-------|
| Cơ sở hạ tầng Command/Agent | Kiểm tra tất cả command shortcuts, state files, handoff layer |
| Trạng thái Repo | Git status, working tree, commit history |
| Deliverables Phase 0.1–0.14 | Xác nhận tất cả artifacts đã được tạo |
| Human Actions Còn Chờ | Các việc Owner phải làm trước Phase 1 |
| Rủi ro Trước Phase 1 | Các điểm yếu cần giải quyết |
| Kết luận sẵn sàng | READY / READY WITH WARNINGS / NOT READY |

Không trong phạm vi: build Phase 1 marketing core, tạo production n8n workflow, gọi API thật, post/reply khách hàng thật, chạy quảng cáo.

---

## Điều Kiện Tiên Quyết Được Kiểm Tra (Preconditions Checked)

| # | Điều kiện | Kết quả | Nguồn kiểm tra |
|---|-----------|---------|----------------|
| P-1 | Phase 0.14 là CLOSED | ✅ PASS | `handoff/CURRENT_PHASE.md` → Status: CLOSED |
| P-2 | Không có active command | ✅ PASS | `commands/CURRENT_COMMAND.md` → "No active command" |
| P-3 | CMD-0.14-001 là CLOSED (commit 7305acb) | ✅ PASS | `commands/COMMAND_STATUS.md`, `commands/COMMAND_INBOX.md` |
| P-4 | Working tree sạch (chỉ `.claude/` untracked) | ✅ PASS | `git status --short` |
| P-5 | CREATE_SESSION_HANDOFF đã được thực thi | ✅ PASS | `handoff/SESSION_SUMMARY.md` → "CREATE_SESSION_HANDOFF — Phase 0.14 close" |
| P-6 | Không có stale active metadata | ✅ PASS | `logs/CURRENT_STATUS.md` → No active command |
| P-7 | `next_owner_action` trỏ đến Phase 0.15 | ✅ PASS | `handoff/SESSION_SUMMARY.md` → "Open Phase 0.15 in a fresh Claude Code session" |
| P-8 | `.claude/` không được tracked bởi git | ✅ PASS | `.gitignore` + `git status --short` |

**Tất cả 8 preconditions: PASS.**

---

## Trạng Thái Repo (Repo Status)

### git status --short

```
 M 06_HANDOFF/NEXT_ACTIONS.md
 M 09_LOGS/PHASE_LOG.md
 M commands/COMMAND_INBOX.md
 M commands/COMMAND_STATUS.md
 M commands/CURRENT_COMMAND.md
 M handoff/CURRENT_PHASE.md
 M logs/AGENT_ACTIVITY_LOG.md
?? .claude/
?? docs/phase-0/PHASE_0_15_PRE_PHASE_1_READINESS_GATE.md
```

**Trạng thái thực tế trong kỳ review:**

- 7 file được modified (` M`) — đây là các state file cập nhật Phase 0.15 (COMMAND_INBOX, COMMAND_STATUS, CURRENT_COMMAND, CURRENT_PHASE, NEXT_ACTIONS, PHASE_LOG, AGENT_ACTIVITY_LOG). Chưa staged, chưa commit — **đúng theo quy trình**: commit chỉ được phép sau OWNER_APPROVED.
- `docs/phase-0/PHASE_0_15_PRE_PHASE_1_READINESS_GATE.md` — file mới (`??`), chưa staged — file này.
- `.claude/` — untracked. Nằm trong `.gitignore`, **không được commit** bất kỳ lúc nào.
- Không có staged changes. Không có conflicts.

**Repo clean state dự kiến:** Sau Owner approval + `git add` + `git commit` Phase 0.15, toàn bộ ` M` và `??` (ngoại trừ `.claude/`) sẽ biến mất. Repo sẽ sạch sau commit Phase 0.15.

**Repo status trong kỳ review: UNCOMMITTED PHASE 0.15 FILES — đúng quy trình, không phải lỗi.**

### git log --oneline -5

```
c1ca4ab chore(phase-0.14): add session handoff before phase 0.15
4610d7b chore(phase-0.14): avoid self-referential commit metadata
f03bccc chore(phase-0.14): refresh final current snapshot
5ba95f2 chore(phase-0.14): clean final stale metadata
a6a1640 chore(phase-0.14): refresh post-close metadata
```

Phase-close commit stable: `7305acb — chore(phase-0.14): close repo status smoke test`
HEAD hiện tại là metadata convention fix sau phase-close (không có feature change). Phase 0.15 chưa được commit.

### Nhánh và Remote

| Field | Giá trị |
|-------|---------|
| Branch | `main` |
| Remote | `https://github.com/bao-c2505e/fnb-os-v1` |
| Untracked | `.claude/` (không commit — đúng) + `PHASE_0_15_PRE_PHASE_1_READINESS_GATE.md` (chưa staged) |
| Uncommitted changes | 7 state files Modified (Phase 0.15 state updates — chờ commit sau OWNER_APPROVED) |
| Staged changes | Không có |
| Conflicts | Không có |

**Repo status: ĐANG REVIEW — Phase 0.15 files chưa commit. Đây là trạng thái bình thường trong kỳ review.**

---

## Trạng Thái Command/Status Layer

### Command Lifecycle

| File | Nội dung | Trạng thái |
|------|----------|-----------|
| `commands/COMMAND_INBOX.md` | CMD-0.15-001 (REVIEW_REQUESTED) + CMD-0.14-001 CLOSED stub | ✅ Current |
| `commands/COMMAND_STATUS.md` | CMD-0.15-001 → REVIEW_REQUESTED; CMD-0.14-001 → CLOSED (7305acb) | ✅ Current |
| `commands/CURRENT_COMMAND.md` | CMD-0.15-001 REVIEW_REQUESTED | ✅ Current |
| `commands/COMMAND_SHORTCUTS.md` | 8 shortcuts định nghĩa đầy đủ | ✅ Operational |
| `commands/COMMAND_ROUTING_RULES.md` | Role gate, file-write rules, error conditions | ✅ Operational |

### Kiểm Tra Stale Metadata

*Kiểm tra tại thời điểm precondition (trước khi Phase 0.15 build) — tất cả PASS.*

| Kiểm tra | Kết quả |
|---------|---------|
| Active command Phase 0.14 tồn tại ngoài CLOSED state | ❌ Không tìm thấy — PASS |
| CURRENT_COMMAND.md trỏ đến Phase 0.14 stale | ❌ Không — đã cleared trước khi Phase 0.15 mở |
| CURRENT_PHASE.md Phase 0.14 có status ≠ CLOSED | ❌ Không — Phase 0.14 CLOSED xác nhận |
| SESSION_SUMMARY.md có `active_command` Phase 0.14 | ❌ Không — "None" tại thời điểm precondition |
| NEXT_ACTIONS CURRENT STATE mâu thuẫn với Phase 0.14 CLOSED | ❌ Không — aligned |

**Command/status layer (tại precondition): SẠCH. Phase 0.15 command (CMD-0.15-001) đã được mở đúng quy trình và hiện đang REVIEW_REQUESTED.**

---

## Trạng Thái Handoff/Session

| File | Nội dung | Trạng thái |
|------|----------|-----------|
| `handoff/CURRENT_PHASE.md` | Phase 0.15 REVIEW_REQUESTED; CMD-0.15-001 active | ✅ Current |
| `handoff/SESSION_SUMMARY.md` | Phase 0.14 CLOSED; next_owner_action = Phase 0.15 | ✅ Current (từ CREATE_SESSION_HANDOFF Phase 0.14) |
| `06_HANDOFF/NEXT_ACTIONS.md` | CURRENT STATE = Phase 0.15 REVIEW_REQUESTED | ✅ Current |
| `logs/CURRENT_STATUS.md` | CMD-0.15-001 REVIEW_REQUESTED *(cập nhật sau fix)* | ✅ Current |
| `09_LOGS/PHASE_LOG.md` | Phase 0.15 build entry là entry mới nhất | ✅ Current |

**Handoff/session layer: NHẤT QUÁN với Phase 0.15 REVIEW_REQUESTED.**

---

## Kiểm Tra Deliverables Phase 0.1–0.14

| Phase | Deliverables Chính | Trạng thái |
|-------|-------------------|-----------|
| 0.1 | `.env` (placeholders), `.env.example`, `.gitignore`, `check_env_safety.py` | ✅ Tạo — `.env` không commit |
| 0.3 | `08_DEPLOY/n8n_credentials_step_by_step.md` | ✅ Tạo |
| 0.4 | 5 smoke-test workflow JSONs trong `n8n/smoke-tests/` | ✅ Tạo — chưa chạy trong n8n |
| 0.5 | `06_HANDOFF/AGENT_REGISTRY.md`, `05_SCHEMAS/agent_task_schema.json` | ✅ Tạo |
| 0.6 | `commands/COMMAND_INBOX.md`, `commands/COMMAND_TEMPLATE.md`, `schemas/command.schema.json` | ✅ Tạo |
| 0.7 | `agents/AGENT_RUN_PROTOCOL.md`, `agents/BUILDER_PROTOCOL.md`, `agents/REVIEWER_PROTOCOL.md` | ✅ Tạo |
| 0.8 | `commands/GITHUB_COMMAND_BRIDGE.md`, `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`, `commands/COMMAND_ROUTING_RULES.md` | ✅ Tạo |
| 0.9 | `commands/COMMAND_SHORTCUTS.md` (6 shortcuts) | ✅ Tạo |
| 0.10 | Active Command Inference, `commands/CURRENT_COMMAND.md`, 8 shortcuts total | ✅ Tạo |
| 0.11 | `APPROVE_CURRENT_PHASE` shortcut, owner approval flow | ✅ Tạo |
| 0.12 | `SHOW_CURRENT_STATUS` expanded, `logs/CURRENT_STATUS.md` | ✅ Tạo |
| 0.13 | `CREATE_SESSION_HANDOFF` shortcut (8 shortcuts total) | ✅ Tạo |
| 0.14 | `docs/phase-0/PHASE_0_14_REPO_STATUS_SMOKE_TEST.md` — 5 PASS / 2 WARNING / 0 FAIL | ✅ Tạo |

**Tất cả Phase 0.1–0.14 deliverables: TỒN TẠI TRONG REPO.**

---

## Safety Guardrails

Các guardrail được xác nhận ĐANG HOẠT ĐỘNG:

| Guardrail | Cơ chế | Trạng thái |
|-----------|--------|-----------|
| Không hardcode API keys/tokens | `.gitignore` block `.env`; `check_env_safety.py` scan | ✅ Active |
| Không auto-post/auto-reply | `AUTO_PUBLISH_ENABLED=false`, `HUMAN_APPROVAL_REQUIRED=true` trong `.env.example`; tất cả smoke-test `active=false` | ✅ Active |
| Không activate n8n workflow | Tất cả workflow JSONs `active=false`; Builder must-NOT list | ✅ Active |
| Không commit `.claude/` | `.gitignore` rule | ✅ Active |
| Không push khi chưa OWNER_APPROVED | Command lifecycle, BUILDER_PROTOCOL | ✅ Active |
| Không chạy quảng cáo | Phase 0 scope lock; không Phase 1 code nào được tạo | ✅ Active |
| Phân quyền rõ ràng | Builder = Claude Code only; Reviewer = Codex only; Approver = Owner | ✅ Active |

---

## Rủi Ro Trước Phase 1 (Risks Before Phase 1)

### Risk-1: n8n Smoke Tests Chưa Được Chạy [HIGH]

**Mô tả:** 5 workflow smoke-test (Phase 0.4) đã được tạo và sẵn sàng import, nhưng Owner chưa chạy thực tế trong n8n UI. Không biết liệu credentials có hoạt động hay không.

**Tác động:** Nếu bất kỳ credential nào fail (Telegram, Google Sheets, Google Drive, OpenAI, Gemini) → Phase 1 không thể vận hành.

**Chủ thể giải quyết:** Owner

**Action cần thiết:**
1. Fill `.env` với API keys thật (Phase 0.2)
2. Tạo 6 credentials trong n8n UI (hướng dẫn: `08_DEPLOY/n8n_credentials_step_by_step.md`)
3. Import và chạy 5 smoke-test workflows, fill kết quả vào `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`

---

### Risk-2: BRAIN Files Còn [FILL] Placeholder [HIGH]

**Mô tả:** Tất cả BRAIN files (`01_BRAIN/*.md`) còn chứa `[FILL: ...]` placeholders. Phase 1 content agents (Gemini) sẽ đọc BRAIN files để generate nội dung cho thương hiệu Vị Cuốn.

**Tác động:** Nếu BRAIN files chưa được fill → content generation sẽ tạo ra nội dung sai thương hiệu hoặc fail.

**Chủ thể giải quyết:** Owner

**Action cần thiết:** Fill tất cả `[FILL: ...]` trong `01_BRAIN/brand_brain.md` và các BRAIN files khác với dữ liệu thật của Vị Cuốn.

---

### Risk-3: CLOSE_APPROVED_COMMAND Spec Thiếu Files [MEDIUM]

**Mô tả:** Từ Phase 0.14 WARNING-3: `commands/COMMAND_SHORTCUTS.md` spec cho `CLOSE_APPROVED_COMMAND` chỉ liệt kê 3–4 files nhưng thực tế cần cập nhật 9 files. Builder mới đọc spec có thể thực hiện close không đầy đủ.

**Tác động:** Incomplete phase close → stale metadata → state inconsistency trong Phase 1 operations.

**Chủ thể giải quyết:** Builder (Claude Code)

**Action cần thiết:** Cập nhật spec `CLOSE_APPROVED_COMMAND` trong `commands/COMMAND_SHORTCUTS.md` để liệt kê đủ 9 files. (Fix này có thể thực hiện trong Phase 0.15 hoặc ngay đầu Phase 1.)

---

### Risk-4: Google Sheet và Drive Chưa Được Tạo [MEDIUM]

**Mô tả:** Phase 1 yêu cầu Google Sheet Control Center và cấu trúc Google Drive folder. Các schema đã có (`08_DEPLOY/google_sheet_schema.md`, `08_DEPLOY/google_drive_structure.md`) nhưng chưa được tạo thực tế.

**Tác động:** n8n workflow Phase 1 sẽ không có data source để đọc/ghi → Phase 1 workflows fail.

**Chủ thể giải quyết:** Builder (Claude Code) — với Owner cung cấp Google account access.

**Action cần thiết:** Builder tạo Google Sheet và Drive folder theo schema. Yêu cầu OAuth access đã được setup.

---

### Risk-5: APPROVE_CURRENT_PHASE Combined-Pass Pattern Chưa Document [LOW]

**Mô tả:** Từ Phase 0.14 WARNING-1/WARNING-2: Spec `APPROVE_CURRENT_PHASE` chưa document "combined pass" pattern (Owner xác nhận Codex PASS cùng lúc). Step 7 vẫn dùng field cũ `next_agent_action`.

**Tác động:** Nhỏ — không blocking. Có thể gây nhầm lẫn cho Codex hoặc Builder mới.

**Chủ thể giải quyết:** Builder (Claude Code)

**Action cần thiết:** Update `commands/COMMAND_SHORTCUTS.md` (có thể bundle cùng Risk-3 fix).

---

### Risk-6: .env Chưa Được Fill Với Giá Trị Thật [HIGH — Human Action]

**Mô tả:** `.env` hiện chỉ có placeholder values (Phase 0.2 status: In Progress). Không có API keys thật → không thể test smoke workflows.

**Tác động:** Blocks Phase 0.4 smoke tests → blocks Phase 1.

**Chủ thể giải quyết:** Owner

**Action cần thiết:** Fill thủ công vào `D:\FNB_OS_V1\.env`:
- `OPENAI_API_KEY`, `GEMINI_API_KEY`
- `GOOGLE_DRIVE_ROOT_FOLDER_ID`, `GOOGLE_SHEET_CONTROL_CENTER_ID`
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- `N8N_API_KEY`, `GITHUB_TOKEN`

---

## Recommended Fixes Trước Phase 1

| # | Fix | Người thực hiện | Priority | Blocking Phase 1? |
|---|-----|----------------|----------|-------------------|
| F-1 | Fill `.env` với API keys thật | Owner | 🔴 HIGH | **YES** — blocks smoke tests |
| F-2 | Tạo 6 credentials trong n8n UI | Owner | 🔴 HIGH | **YES** — blocks smoke tests |
| F-3 | Chạy 5 smoke-test workflows, ghi kết quả | Owner | 🔴 HIGH | **YES** — Phase 1 gate |
| F-4 | Fill BRAIN files với dữ liệu Vị Cuốn | Owner | 🟠 MEDIUM | YES — blocks content generation |
| F-5 | Fix `CLOSE_APPROVED_COMMAND` spec (9 files) | Builder | 🟠 MEDIUM | Gián tiếp — risk stale metadata |
| F-6 | Tạo Google Sheet Control Center | Builder+Owner | 🟠 MEDIUM | YES — Phase 1 data layer |
| F-7 | Fix `APPROVE_CURRENT_PHASE` combined-pass pattern | Builder | 🟡 LOW | Không — minor spec gap |

**Tổng: 3 blocking fixes cần Owner action (F-1, F-2, F-3). 2 blocking fixes cần Builder+Owner (F-4, F-6). 2 non-blocking fixes (F-5, F-7).**

---

## Tóm Tắt Kiểm Tra Hệ Thống

| Layer | Trạng thái | Ghi chú |
|-------|-----------|---------|
| Git Repo | ✅ CLEAN (sau commit Phase 0.15) | Trong kỳ review: 7 M + 1 untracked — bình thường; `.claude/` không commit |
| Command System | ✅ OPERATIONAL | 8 shortcuts, role gates, lifecycle đầy đủ |
| Agent Protocol | ✅ OPERATIONAL | Builder/Reviewer/Owner roles rõ ràng |
| Handoff Layer | ✅ CURRENT | 14-field SESSION_SUMMARY, CURRENT_STATUS sạch |
| Safety Guardrails | ✅ ACTIVE | Không hardcode secrets, không auto-publish |
| Phase 0 Deliverables | ✅ ALL PRESENT | 75+ files, tất cả artifacts tồn tại |
| n8n Smoke Tests | ⚠️ NOT YET RUN | Artifacts ready — Owner must run in n8n UI |
| .env API Keys | ⚠️ PLACEHOLDER | Owner must fill with real values |
| BRAIN Files | ⚠️ PLACEHOLDER | Owner must fill with Vị Cuốn data |
| Google Sheet/Drive | ⚠️ NOT YET CREATED | Schema ready — Builder + Owner must create |
| Shortcut Spec Gaps | ⚠️ MINOR | Risk-3, Risk-5 — fix before heavy Phase 1 ops |

---

## Kết Quả Sẵn Sàng (Final Readiness Result)

```
╔══════════════════════════════════════════════════════════════╗
║   PHASE 0.15 READINESS RESULT: READY WITH WARNINGS           ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  ✅ Command/Agent Infrastructure: READY                      ║
║  ✅ Repo State: CLEAN (sau commit Phase 0.15)                ║
║  ✅ Phase 0 Deliverables: ALL PRESENT                        ║
║  ✅ Safety Guardrails: ACTIVE                                ║
║  ✅ Blocker Check: PASS — không có secret, không .claude/   ║
║                                                              ║
║  ⚠️  n8n Smoke Tests: NOT YET RUN (Owner action needed)     ║
║  ⚠️  .env API Keys: PLACEHOLDER (Owner action needed)       ║
║  ⚠️  BRAIN Files: PLACEHOLDER (Owner action needed)         ║
║  ⚠️  Google Sheet/Drive: NOT YET CREATED                    ║
║  ⚠️  CLOSE_APPROVED_COMMAND spec: INCOMPLETE (minor)        ║
║  ⚠️  Report/metadata wording: non-blocking imperfections    ║
║                                                              ║
║  OWNER DECISION: Đóng Phase 0.15 theo blocker-only policy.  ║
║  Warnings trên là non-blocking — không ngăn Phase 1.        ║
║  → Phase 1.1 mở sau khi Owner ready.                       ║
╚══════════════════════════════════════════════════════════════╝
```

### Quyết Định Đóng Phase (Owner — Blocker-Only Policy)

Kể từ Phase 0.15: **chỉ blockers thật mới có thể ngăn đóng phase.** Blockers thật bao gồm:
- Secret/API key/token/password được commit hoặc staged
- `.claude/` được commit
- Phase 1 marketing core được tạo trước khi approve
- Production n8n workflow được tạo trước khi approve
- Hành vi auto-post/auto-reply/chạy ads thực tế

Metadata wording, report formatting, status field labels không phải blockers.

### Điều kiện để chuyển sang Phase 1

| # | Điều kiện | Trạng thái |
|---|-----------|-----------|
| 1 | Phase 0.14 CLOSED | ✅ ĐÃ ĐẠT |
| 2 | Command system operational | ✅ ĐÃ ĐẠT |
| 3 | Phase 0.15 CLOSED | ✅ ĐÃ ĐẠT — Owner force-close blocker-only |
| 4 | `.env` filled với API keys thật | ⏳ CHỜ OWNER (làm trước hoặc song song Phase 1) |
| 5 | 6 credentials tạo trong n8n | ⏳ CHỜ OWNER |
| 6 | 5 smoke tests PASS trong n8n | ⏳ CHỜ OWNER |
| 7 | BRAIN files filled | ⏳ CHỜ OWNER (song song Phase 1) |

---

## Done Criteria

- [x] Phase name, scope định rõ
- [x] 8 preconditions kiểm tra — tất cả PASS
- [x] Repo status xác nhận: git status, git log
- [x] Command/status layer xác nhận: không stale metadata
- [x] Handoff/session layer xác nhận: nhất quán
- [x] Tất cả Phase 0.1–0.14 deliverables xác nhận tồn tại
- [x] Safety guardrails xác nhận active
- [x] 6 risks trước Phase 1 được document với severity và action
- [x] 7 recommended fixes với priority và blocking status
- [x] Final readiness result: **READY WITH WARNINGS**
- [x] Điều kiện chuyển Phase 1 rõ ràng
- [x] Không thực thi shortcut nào — review/inspection only
- [x] Blocker check: PASS — không có secrets, .claude/ không staged
- [x] Phase 0.15 CLOSED theo Owner blocker-only policy
- [x] Next: Phase 1.1 — Brand Brain Foundation
