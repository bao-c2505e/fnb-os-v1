# OS V1 — Workflow Infrastructure & ECC-lite Adoption Brief

**Project:** FnB OS V1 / Vị Cuốn Growth OS  
**Owner:** Bo Bao  
**Role model:** ChatGPT = Chief Architect, Claude Code = Builder, Codex = Reviewer, GitHub = Source of Truth, n8n = Runtime Automation  
**Created:** 2026-05-29  
**Purpose:** Tài liệu này tổng hợp các đề xuất phù hợp để áp dụng bộ công cụ Workflow / Infrastructure và tư tưởng ECC (Everything Claude Code) vào OS V1. Dùng làm master brief cho các phase tiếp theo khi build hệ thống.

---

## 1. Kết luận chiến lược

Bộ công cụ developer gồm GitHub, GitHub Actions, Husky, ESLint, Prettier, Docker, Sentry, PostHog, Supabase, Cloudflare, Coolify là stack rất tốt cho dự án phần mềm nghiêm túc. Tuy nhiên OS V1 hiện chưa phải SaaS/app production có nhiều user đăng nhập, mà đang là hệ thống AI Marketing Operating System vận hành qua repo, n8n workflow, approval gate và các AI agent.

ECC cũng rất đáng học, nhưng không nên bê nguyên vào OS V1 ngay. Cách đúng là áp dụng bản **ECC-lite**: chuẩn hóa agent, skills, hooks, memory, security, CI gate và handoff.

Định hướng đúng:

> Không biến OS V1 thành một hệ thống phức tạp quá sớm.  
> Tập trung nâng OS V1 từ “repo + n8n workflow + manual approval” thành “AI Agent Operating System có quy trình, kiểm tra, bảo mật và khả năng mở rộng”.

---

## 2. OS V1 hiện tại đã có gì

OS V1 hiện đã có nền tảng tốt:

- GitHub repo làm Source of Truth.
- Làm việc theo Phase.
- Có Claude Code làm Builder.
- Có Codex làm Reviewer.
- Có ChatGPT làm Chief Architect.
- Có n8n làm Runtime Automation.
- Có workflow JSON importable.
- Có sandbox/manual execution.
- Có approval gate.
- Có handoff/session summary/log.
- Có nguyên tắc không hardcode API key/token/password.
- Có nguyên tắc không auto-post, không auto-reply khách thật, không chạy ads tiêu tiền nếu chưa có Owner approval.

Đánh giá hiện tại:

- Tư duy vận hành: khoảng 7/10.
- Production readiness thật sự: khoảng 4/10.
- Sau khi thêm CI/Safety Gate: có thể lên khoảng 6/10.

---

## 3. Bộ công cụ Workflow / Infrastructure nên áp dụng

### 3.1. Áp dụng ngay hoặc rất sớm

#### GitHub

Đã dùng và phải tiếp tục giữ làm Source of Truth.

Vai trò trong OS V1:

- Lưu markdown, schema, workflow JSON, prompt, handoff, logs.
- Theo dõi phase.
- Là nơi Claude/Codex/ChatGPT cùng bám vào.
- Là lịch sử quyết định và bằng chứng tiến độ.

#### GitHub Actions

Nên thêm sau Phase 19 hoặc Phase 20.

Vai trò:

- Tự động kiểm tra repo.
- Validate workflow JSON.
- Kiểm tra secret/API key/token.
- Kiểm tra n8n workflow sandbox phải `active=false`.
- Kiểm tra file bắt buộc của phase có tồn tại.
- Tạo CI report để Codex review nhanh hơn.

Đề xuất phase:

> Phase 20 — Repository CI & Runtime Safety Gate

#### Prettier

Nên thêm sớm cho các file:

- Markdown `.md`
- JSON `.json`
- YAML `.yml/.yaml`

Lý do:

- OS V1 có nhiều workflow JSON, schema, docs, logs.
- Giúp file đồng nhất, giảm lỗi format do AI sinh ra.
- Hợp hơn ESLint ở giai đoạn hiện tại.

#### Secret scanning / credential guard

Bắt buộc cần có.

Cần kiểm tra:

- Không commit `.env`.
- Không lộ API key/token/password.
- Không lưu credential thật trong n8n workflow JSON.
- Không lưu OAuth secret trong repo.
- Không lưu webhook secret hoặc Telegram bot token thật.

#### Docker / Docker Compose

Rất nên chuẩn hóa cho runtime production.

Áp dụng cho:

- n8n
- PostgreSQL
- Caddy hoặc Nginx reverse proxy
- Backup volume
- `.env.example`
- Deployment note

Mục tiêu:

- Đồng bộ local và VPS.
- Dễ backup/restore.
- Dễ migration sang VPS khác.
- Giảm lỗi “máy tôi chạy được, production không chạy”.

#### Cloudflare

Đã dùng và nên giữ.

Vai trò:

- DNS cho domain/subdomain.
- SSL/CDN.
- Sau này có thể dùng WAF/rules/basic protection.

---

### 3.2. Áp dụng sau, khi OS V1 có app/API/dashboard

#### Supabase

Không nên thay Google Sheet ngay lập tức. Nên dùng theo lộ trình:

Giai đoạn hiện tại:

- Google Sheet = Control Center dễ thao tác.
- n8n đọc/ghi trạng thái.

Giai đoạn V1.5:

- Supabase = database/log/asset/CRM chính.
- Google Sheet = view phụ hoặc công cụ owner dễ nhìn.

Giai đoạn V2:

- Supabase + dashboard riêng = OS thật cho nhiều brand F&B.

Supabase phù hợp cho:

- Auth.
- Postgres database.
- Storage.
- Realtime logs.
- Asset library.
- CRM records.
- Approval history.
- Multi-brand/multi-user sau này.

#### Coolify

Rất đáng dùng khi có dashboard/app/API/LangGraph service.

Không cần ngay nếu chỉ import workflow n8n thủ công.

Áp dụng khi có:

- Next.js dashboard.
- API service.
- LangGraph orchestrator.
- Worker service.
- Internal admin panel.
- Multiple runtime services trên VPS.

#### Sentry

Chưa cần ngay.

Dùng khi có:

- Web dashboard.
- API backend.
- LangGraph service.
- Worker service chạy production.

Vai trò:

- Error monitoring.
- Crash tracking.
- Stack trace.
- Release-level bug tracking.

#### PostHog

Chưa cần ngay.

Dùng khi OS V1 có user thật dùng dashboard.

Vai trò:

- Tracking hành vi user.
- Funnel.
- Session replay.
- Feature flags.
- Product analytics.

---

### 3.3. Chưa ưu tiên

#### Husky

Chưa cần ngay vì OS V1 hiện vận hành nhiều qua AI agent và GitHub, không phải team dev local đông người.

Có thể thêm sau khi có nhiều dev commit trực tiếp từ máy local.

#### ESLint

Chưa cần nếu repo chủ yếu là markdown, JSON, schema và n8n workflow.

Chỉ nên thêm khi có:

- Next.js dashboard.
- Node.js API.
- TypeScript worker.
- LangGraph/agent service bằng JS/TS.

---

## 4. ECC áp dụng vào OS V1 như thế nào

ECC không nên xem là tool thay thế OS V1. Nên xem là tư tưởng xây dựng **Agent Operating Layer** cho OS V1.

Điểm đáng học từ ECC:

- Agent không chỉ nhận prompt, mà có vai trò, luật, quyền hạn và điểm dừng.
- Skills là các gói năng lực tái sử dụng.
- Hooks giúp chặn lỗi/nguy hiểm trước khi commit/push/deploy.
- Memory giúp agent không quên quyết định và lỗi đã học.
- Security scan là bắt buộc.
- Workflow nghiêm túc quan trọng hơn việc model nào code giỏi hơn.

OS V1 nên áp dụng bản **ECC-lite**, không bê nguyên 61 agents / 246 skills.

---

## 5. Agent Operating Layer đề xuất cho OS V1

Tạo thư mục:

```text
/00_AGENT_OS
  /agents
  /skills
  /hooks
  /memory
  /schemas
```

### 5.1. Agents

Đề xuất ban đầu 8 agent:

```text
/00_AGENT_OS/agents
  chief-architect.md
  claude-builder.md
  codex-reviewer.md
  security-reviewer.md
  n8n-workflow-validator.md
  documentation-maintainer.md
  sandbox-test-reporter.md
  brand-marketing-strategist.md
```

#### Chief Architect

Vai trò:

- Chia phase.
- Thiết kế kiến trúc.
- Viết task cho Builder.
- Quyết định scope.
- Không trực tiếp sửa repo nếu chưa cần.
- Bảo vệ nguyên tắc OS V1.

#### Claude Builder

Vai trò:

- Tạo/sửa file.
- Build workflow.
- Cập nhật docs/schema/log.
- Không tự push nếu Owner chưa cho phép.
- Không tự thay đổi scope.
- Không hardcode secret.

#### Codex Reviewer

Vai trò:

- Review output.
- Kiểm tra scope, risk, missing files.
- Không commit.
- Không push.
- Chỉ block nếu có blocker thật.

Blocker thật gồm:

1. Lộ secret/API key/token/password.
2. Workflow JSON lỗi không import được.
3. Sai scope nghiêm trọng.
4. Mất file quan trọng.
5. Auto-post/auto-reply/chạy ads thật khi chưa approval.
6. Runtime nguy hiểm ảnh hưởng dữ liệu thật.

#### Security Reviewer

Vai trò:

- Quét secret.
- Kiểm tra file nguy hiểm.
- Kiểm tra credential.
- Kiểm tra webhook/API exposure.
- Tạo security report.

#### n8n Workflow Validator

Vai trò:

- Validate JSON.
- Check `active=false`.
- Check credential placeholder.
- Check node naming.
- Check workflow importability.
- Check sandbox safety.

#### Documentation Maintainer

Vai trò:

- Cập nhật README, CURRENT_PHASE, PHASE_LOG, SESSION_SUMMARY, HANDOFF.
- Đảm bảo tài liệu khớp với code/workflow thật.

#### Sandbox Test Reporter

Vai trò:

- Tạo test instruction.
- Ghi execution result.
- Ghi evidence pack.
- Ghi owner manual action.
- Không tự động chạy dữ liệu thật.

#### Brand/Marketing Strategist

Vai trò:

- Bảo vệ Brand Brain.
- Kiểm tra output có đúng tone Vị Cuốn.
- Đánh giá content/ads/CRM/comment reply.
- Gắn với mục tiêu F&B/agency.

---

## 6. Skill System đề xuất

Tạo thư mục:

```text
/00_AGENT_OS/skills
```

Mỗi skill gồm:

```text
SKILL.md
input_schema.json
output_schema.json
checklist.md
examples/
```

### 6.1. Danh sách skill giai đoạn đầu

```text
phase-plan-create
repo-scope-check
n8n-workflow-validate
secret-scan-check
brand-brain-update
content-output-generate
creative-brief-generate
ads-pack-generate
crm-followup-generate
comment-inbox-reply-generate
approval-message-build
sandbox-log-create
handoff-summary-create
codex-review-pack-create
issue-to-fix-plan
```

### 6.2. Skill quan trọng nhất: n8n-workflow-validate

Nhiệm vụ:

- Kiểm tra workflow JSON parse được.
- Kiểm tra `active=false`.
- Kiểm tra không có credential thật.
- Kiểm tra không có API key/token/password.
- Kiểm tra node name rõ ràng.
- Kiểm tra trigger không gây chạy thật ngoài ý muốn.
- Kiểm tra importability.
- Xuất validation report.

### 6.3. Skill secret-scan-check

Nhiệm vụ:

- Quét chuỗi nguy hiểm.
- Quét `.env`.
- Quét token pattern.
- Quét n8n credentials.
- Quét webhook secrets.
- Quét Google/Telegram/ElevenLabs/OpenAI/Claude/Gemini/Supabase keys.
- Xuất security report.

### 6.4. Skill handoff-summary-create

Nhiệm vụ:

- Tóm tắt phase hiện tại.
- Ghi latest commit.
- Ghi files changed.
- Ghi decision.
- Ghi known issues.
- Ghi next phase recommendation.
- Giúp chuyển session không mất ngữ cảnh.

### 6.5. Skill codex-review-pack-create

Nhiệm vụ:

- Gom output cho Codex review.
- Nêu scope.
- Nêu expected files.
- Nêu acceptance criteria.
- Nêu risk areas.
- Yêu cầu Codex chỉ review, không sửa, không commit, không push.

---

## 7. Hooks / Gates đề xuất

Tạo thư mục:

```text
/00_AGENT_OS/hooks
```

Ban đầu chưa cần hook kỹ thuật phức tạp. Có thể bắt đầu bằng checklist + GitHub Actions.

### 7.1. Pre-commit checklist

Kiểm tra trước khi commit:

- Có đúng scope phase không?
- Có file lạ không?
- Có secret không?
- Có `.env` không?
- Workflow JSON có valid không?
- n8n workflow có `active=false` không?
- Có cập nhật phase log không?
- Có cập nhật session summary/handoff không?

### 7.2. Pre-push checklist

Kiểm tra trước khi push:

- Git status clean sau commit?
- Latest commit đúng message?
- CI local/basic pass?
- Không có credential thật?
- Owner đã cho phép push chưa?
- Codex review pass nếu phase yêu cầu?

### 7.3. CI required checks

GitHub Actions nên kiểm tra:

- JSON validity.
- Markdown formatting.
- Required files.
- Secret scan.
- No active n8n workflow.
- No real credential.
- Phase log updated.
- Schema validity.

---

## 8. Memory Layer đề xuất

Tạo thư mục:

```text
/00_AGENT_OS/memory
```

Các file đề xuất:

```text
decisions.md
architecture.md
constraints.md
known-issues.md
reusable-patterns.md
agent-learning-log.md
```

### 8.1. decisions.md

Lưu các quyết định đã chốt:

- OS V1 là AI Marketing Automation tổng thể cho F&B, không chỉ video.
- Không auto-post nếu chưa approval.
- GitHub là Source of Truth.
- n8n là runtime.
- Claude là Builder.
- Codex là Reviewer only.
- ChatGPT là Chief Architect.
- Owner chỉ duyệt kế hoạch/output, không debug thủ công quá nhiều.

### 8.2. constraints.md

Lưu luật không được vi phạm:

- Không hardcode secret.
- Không commit `.env`.
- Không chạy workflow với dữ liệu khách thật nếu chưa duyệt.
- Không auto-reply khách thật.
- Không chạy ads tiêu tiền.
- Không sửa ngoài scope.
- Không tự push nếu Owner chưa cho phép.
- Một phase chỉ có một Builder chính.

### 8.3. known-issues.md

Lưu lỗi đã gặp:

- Google Sheet tab name phải khớp tuyệt đối.
- n8n workflow import cần JSON sạch.
- Workflow sandbox nên `active=false`.
- Telegram message hay lỗi newline escaping.
- API model name phải đúng.
- Không để credential thật trong workflow JSON.

### 8.4. reusable-patterns.md

Lưu pattern đã chứng minh chạy tốt:

- Phase-based delivery.
- Builder/Reviewer separation.
- Handoff sau mỗi session dài.
- Evidence pack sau sandbox test.
- Approval gate trước publishing.
- Manual sandbox execution trước production.

### 8.5. agent-learning-log.md

Lưu bài học cho agent:

- Sau 10 lượt trao đổi, agent phải tạo SESSION_SUMMARY và chuyển session mới.
- Codex không commit/push.
- Claude không tự đổi scope.
- Mọi output phải qua repo.
- Tất cả workflow runtime cần có log/evidence.

---

## 9. Schemas đề xuất

Tạo thư mục:

```text
/00_AGENT_OS/schemas
```

Schemas ban đầu:

```text
agent_task.schema.json
review_report.schema.json
skill_output.schema.json
phase_handoff.schema.json
workflow_validation_report.schema.json
security_scan_report.schema.json
sandbox_execution_report.schema.json
approval_gate.schema.json
```

Mục tiêu:

- Output của AI có cấu trúc.
- Codex review dễ hơn.
- CI validate được.
- Sau này LangGraph/n8n có thể đọc được.

---

## 10. Lộ trình phase đề xuất

### Phase 20 — Repository CI & Runtime Safety Gate

Mục tiêu:

- Thêm GitHub Actions.
- Validate JSON.
- Secret scan.
- Check workflow `active=false`.
- Check required docs/logs.
- Tạo CI report.

Deliverables:

```text
.github/workflows/repo-safety-check.yml
scripts/validate-json.js hoặc validate-json.py
scripts/check-no-secrets.js hoặc check-no-secrets.py
scripts/check-n8n-workflows.js hoặc check-n8n-workflows.py
docs/PHASE_20_CI_SAFETY_GATE.md
handoff/PHASE_20_HANDOFF.md
```

Acceptance criteria:

- CI chạy được trên pull/push.
- Fail nếu có JSON lỗi.
- Fail nếu có secret pattern rõ ràng.
- Fail nếu workflow active=true.
- Không làm thay đổi workflow runtime thật.

---

### Phase 21 — Agent Operating Layer

Mục tiêu:

- Tạo `/00_AGENT_OS`.
- Tạo agent profiles.
- Tạo memory layer.
- Tạo hooks checklist.
- Tạo schemas nền.

Deliverables:

```text
/00_AGENT_OS/agents/*.md
/00_AGENT_OS/hooks/*.md
/00_AGENT_OS/memory/*.md
/00_AGENT_OS/schemas/*.json
docs/PHASE_21_AGENT_OPERATING_LAYER.md
handoff/PHASE_21_HANDOFF.md
```

Acceptance criteria:

- Mỗi agent có role, allowed actions, forbidden actions, output format.
- Memory layer có quyết định, constraints, known issues.
- Hooks checklist rõ ràng.
- Không thay đổi runtime n8n ở phase này.

---

### Phase 22 — FnB Marketing Skill Pack

Mục tiêu:

- Đóng gói skills cho các module marketing chính.
- Tạo input/output schema.
- Tạo checklist cho từng skill.

Deliverables:

```text
/00_AGENT_OS/skills/brand-brain-update
/00_AGENT_OS/skills/content-output-generate
/00_AGENT_OS/skills/creative-brief-generate
/00_AGENT_OS/skills/ads-pack-generate
/00_AGENT_OS/skills/crm-followup-generate
/00_AGENT_OS/skills/comment-inbox-reply-generate
/00_AGENT_OS/skills/approval-message-build
```

Acceptance criteria:

- Mỗi skill có SKILL.md.
- Có input/output schema.
- Có checklist.
- Có ví dụ output mẫu.
- Gắn với 12 modules của FnB OS V1.

---

### Phase 23 — Runtime Observability Foundation

Mục tiêu:

- Chuẩn hóa log runtime.
- Chuẩn hóa error report.
- Chuẩn hóa execution evidence.
- Chuẩn bị nền cho Sentry/PostHog sau này.

Deliverables:

```text
/09_LOGS/runtime_execution_log.schema.json
/09_LOGS/error_report.schema.json
/09_LOGS/approval_history.schema.json
docs/PHASE_23_RUNTIME_OBSERVABILITY.md
```

Acceptance criteria:

- Mỗi workflow có log format.
- Có error classification.
- Có approval history.
- Có evidence format cho sandbox và production.

---

### Phase 24+ — Production Infrastructure

Áp dụng sau khi OS V1 ổn hơn:

- Docker Compose chuẩn.
- Supabase integration.
- Coolify deploy.
- Sentry monitoring.
- PostHog analytics.
- Dashboard nội bộ.
- LangGraph orchestrator.
- Multi-brand readiness.

---

## 11. Stack đề xuất theo giai đoạn

### OS V1 hiện tại / Sandbox

```text
GitHub
n8n
Google Sheet
Google Drive
Telegram
Claude Code
Codex
ChatGPT
GitHub Actions basic
Prettier
Secret scan
Cloudflare DNS
```

### OS V1.5 / Production nội bộ

```text
Docker Compose
PostgreSQL hoặc Supabase
GitHub Actions CI
n8n production
Backup workflow
Runtime logs
Approval history
Asset library
Basic dashboard
```

### OS V2 / Agency SaaS hoặc Multi-brand OS

```text
Next.js dashboard
Supabase Auth + Database + Storage
Coolify deploy
Sentry monitoring
PostHog analytics
Cloudflare CDN/WAF/DNS
GitHub Actions CI/CD
LangGraph orchestrator
n8n runtime workers
Multi-brand Brand Brain
```

---

## 12. Những thứ không nên làm ngay

Không nên làm ngay:

- Không copy nguyên ECC.
- Không tạo 61 agents.
- Không tạo 246 skills.
- Không thêm dashboard GUI quá sớm.
- Không thêm MCP khi repo/n8n/CI chưa ổn.
- Không thay Google Sheet bằng Supabase ngay lập tức.
- Không thêm Sentry/PostHog khi chưa có app/API/user dashboard.
- Không thêm quá nhiều automation production khi sandbox chưa pass ổn định.

---

## 13. Prompt sử dụng tài liệu này ở lần sau

Khi mở hội thoại mới, Owner có thể đưa prompt sau:

```text
Tôi đang tiếp tục project FnB OS V1 / Vị Cuốn Growth OS.

Hãy dùng file OS_V1_WORKFLOW_INFRA_ECC_LITE_ADOPTION_BRIEF.md làm định hướng build các phase tiếp theo.

Mục tiêu:
- Áp dụng chọn lọc bộ công cụ Workflow/Infrastructure.
- Áp dụng ECC-lite, không bê nguyên ECC.
- Ưu tiên GitHub Actions, CI Safety Gate, secret scan, n8n workflow validation.
- Sau đó xây Agent Operating Layer gồm agents, skills, hooks, memory, schemas.
- Giữ đúng nguyên tắc OS V1: GitHub Source of Truth, n8n runtime, Claude Builder, Codex Reviewer only, ChatGPT Chief Architect, Owner approval gate.
- Không hardcode secret.
- Không auto-post/auto-reply/chạy ads thật nếu chưa approval.

Hãy đề xuất phase tiếp theo phù hợp và viết prompt giao việc cho Claude Code + prompt review cho Codex.
```

---

## 14. Quyết định đề xuất

Quyết định nên chốt:

> Sau Phase 19 manual sandbox execution, OS V1 nên đi vào Phase 20 — Repository CI & Runtime Safety Gate trước, rồi mới làm Agent Operating Layer theo ECC-lite.

Lý do:

- CI/Safety Gate bảo vệ repo ngay lập tức.
- Giảm lỗi do AI agent sinh file sai.
- Giảm phụ thuộc vào review thủ công.
- Tạo nền để áp dụng ECC-lite an toàn hơn.
- Phù hợp với mục tiêu SOLO Business: Owner duyệt output, không debug thủ công quá nhiều.

---

## 15. Final recommendation

Thứ tự áp dụng tốt nhất:

```text
1. Phase 20 — GitHub Actions + Safety Gate
2. Phase 21 — Agent Operating Layer
3. Phase 22 — FnB Marketing Skill Pack
4. Phase 23 — Runtime Observability
5. Phase 24+ — Docker/Supabase/Coolify/Sentry/PostHog khi cần production thật
```

Câu chốt:

> Code chỉ là khởi đầu. Với OS V1, thứ cần build tiếp không phải thêm thật nhiều workflow, mà là lớp vận hành giúp AI agent làm việc có luật, có kiểm tra, có trí nhớ, có bảo mật và có khả năng scale.
