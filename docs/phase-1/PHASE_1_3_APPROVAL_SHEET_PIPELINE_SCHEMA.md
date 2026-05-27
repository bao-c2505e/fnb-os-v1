# PHASE 1.3 — Approval Sheet & Pipeline Schema

**Phase:** 1.3
**Status:** REVIEW_REQUESTED
**Builder:** Claude Code (AGT-02)
**Reviewer:** Codex / GPT-4o (AGT-04)
**Date:** 2026-05-27
**Command ID:** CMD-1.3-001

---

## Tóm tắt

Phase 1.3 xây dựng toàn bộ schema và cấu trúc cho hệ thống phê duyệt nội dung (Approval Pipeline) của Vị Cuốn. Đây là tầng trung gian kết nối AI Content Engine (Phase 1.2) với việc đăng bài thực tế trong các Phase sau.

**Kết quả chính:**
- Định nghĩa 9 trạng thái trong content lifecycle với transition rules nghiêm ngặt
- Schema đầy đủ cho Google Sheet "Content Approval Queue" (21 cột)
- JSON Schema hoàn chỉnh cho Content Pack (đơn vị dữ liệu AI tạo ra)
- 8-stage content pipeline từ Idea → Published → Archived
- 7 Telegram notification templates cho mọi scenario approval
- Owner review checklist 6 phần có thể dùng ngay
- Toàn bộ approval rules: AI chỉ tạo, Owner phê duyệt, không auto-post

---

## Files tạo mới

### 03_APPROVAL_PIPELINE/ (Thư mục mới)

| File | Mô tả | Dòng (ước tính) |
|------|-------|-----------------|
| `README.md` | Overview, dependencies, approval rules tóm tắt, phase readiness | ~130 |
| `status_lifecycle.md` | 9 trạng thái, transition rules, time limits, bảng tóm tắt | ~200 |
| `approval_sheet_schema.md` | 21 cột Google Sheet với validation rules, safety flags, setup notes | ~280 |
| `content_pipeline_schema.md` | 8-stage pipeline: Idea → Draft → Review → Approved → Scheduled → Published → Archived | ~250 |
| `content_pack_json_schema.md` | JSON Schema đầy đủ (JSON Schema Draft-07), ví dụ content pack, mapping sheet/JSON | ~400 |
| `telegram_approval_message_template.md` | 7 templates: READY_FOR_REVIEW, Reminder, Revision done, Schedule reminder, Confirm approve, Confirm reject, Escalation | ~300 |
| `owner_review_checklist.md` | Checklist 6 phần, ma trận quyết định, hướng dẫn revision note | ~200 |

### docs/phase-1/

| File | Mô tả |
|------|-------|
| `PHASE_1_3_APPROVAL_SHEET_PIPELINE_SCHEMA.md` | File này — Phase report |

---

## Chi tiết Deliverables

### 1. Status Lifecycle (9 trạng thái)

```
IDEA → DRAFT → READY_FOR_REVIEW
  ↓ (Owner review)
APPROVED → SCHEDULE_PROPOSED → PUBLISHED_MANUAL → ARCHIVED
  ↓ (nếu cần sửa)
REVISION_REQUESTED → (quay lại DRAFT)
  ↓ (nếu từ chối)
REJECTED → ARCHIVED
```

**Quy tắc quan trọng:**
- AI chỉ set: IDEA, DRAFT, READY_FOR_REVIEW
- Owner phải set: APPROVED, REVISION_REQUESTED, REJECTED, SCHEDULE_PROPOSED, PUBLISHED_MANUAL
- Không ai có thể bỏ qua bước (IDEA không thể nhảy thẳng lên APPROVED)
- READY_FOR_REVIEW chỉ được set sau khi AI Self-Check pass 100%

### 2. Approval Sheet Schema (21 cột)

| Nhóm cột | Cột | Ai điền |
|---------|-----|--------|
| Định danh | content_id, brand, platform, content_type | AI Agent |
| Nội dung | pillar, angle, offer_code | AI Agent |
| Nội dung bài | caption, video_script, image_brief, design_brief | AI Agent |
| Persona | target_persona | AI Agent |
| Trạng thái | status | AI + Owner |
| Quyết định Owner | owner_decision, revision_note, approval_timestamp | **Owner** |
| Lịch đăng | proposed_publish_date, manual_publish_link | **Owner** |
| Metadata | created_by_agent, source_brain_version | AI Agent |
| Safety | safety_flags | AI Agent |

### 3. Content Pack JSON Schema

Gồm 13 fields cấp cao:
- `id`, `brand`, `platform`, `content_type`, `objective`
- `persona` (segment, persona_name, pain_point)
- `pillar`, `angle` (code, name, hook)
- `offer` (offer_id, offer_name, voucher_code, offer_summary, valid_until)
- `caption_options` (array: version, text, char_count, note)
- `script_options` (array: version, template_id, duration, scenes, cta)
- `image_brief` (subject, composition, lighting, props, avoid, reference_style)
- `design_brief` (format, main_text, sub_text, color_theme, font, cta_button)
- `safety_check` (passed, checked_at, flags, ai_notes)
- `approval` (status, owner_decision, revision_note, approval_timestamp, proposed_publish_date, manual_publish_link, revision_count)
- `metadata` (created_at, updated_at, created_by_agent, source_brain_version, n8n_workflow_id, drive_folder_url, sheet_row_id)

### 4. Approval Rules (Nhắc lại từ Phase 1.2 + bổ sung)

| Quy tắc | Chi tiết |
|---------|---------|
| AI tạo nội dung | AI được tạo caption, script, brief, angle, pillar |
| Owner phê duyệt trước khi đăng | Không có ngoại lệ, kể cả bài "đơn giản" |
| Không auto-reply khách hàng | AI không reply comment / tin nhắn bất kỳ |
| Không fake review | Tuyệt đối cấm tạo review giả |
| Không sai giá / unverified claim | Giá phải từ menu_brain.md, không claim sức khỏe |
| Không auto-post | Không có auto-schedule / auto-publish trong Phase 1–2 |
| Không auto-run ads | Quảng cáo phải Owner quyết định budget và creative |
| Không tạo offer ngoài engine | Chỉ dùng offer từ offer_engine.md |
| Không đưa production n8n workflow | Phase 3 mới build n8n production workflows |

### 5. Telegram Notification System (7 templates)

| Template | Trigger |
|---------|---------|
| T1: Chờ duyệt | status → READY_FOR_REVIEW |
| T2: Nhắc lần 2 | 48 giờ sau READY_FOR_REVIEW không có phản hồi |
| T3: Revision xong | AI hoàn thành chỉnh sửa |
| T4: Nhắc ngày đăng | Sáng ngày proposed_publish_date |
| T5: Xác nhận approve | Owner vừa approve |
| T6: Xác nhận reject | Owner vừa reject |
| T7: Escalation | revision_count ≥ 3 lần không đạt |

---

## Assumptions (Giả định)

1. **Google Sheet format:** Dựa trên schema từ `08_DEPLOY/google_sheet_schema.md` (Phase 0). Tab "Content Approval Queue" chưa tồn tại — sẽ tạo trong Phase 2.

2. **Telegram Bot:** Đã được cấu hình (xem Phase 0.2). Template sử dụng `TELEGRAM_BOT_TOKEN` và `TELEGRAM_CHAT_ID` từ `.env`.

3. **Google Drive folder:** Drive root folder được lấy từ `GOOGLE_DRIVE_ROOT_FOLDER_ID` trong `.env`. Cấu trúc `/Draft/[YYYY-MM]/[Platform]/[content_id]/` sẽ được tạo trong Phase 2.

4. **n8n Telegram Command Parser:** Được mô tả trong `telegram_approval_message_template.md` nhưng sẽ chỉ build trong Phase 3. Trong Phase 1–2, Owner điền Google Sheet trực tiếp.

5. **Persona segments:** Dựa trên `customer_brain.md` — Segment A (dân văn phòng), Segment B (gia đình trẻ), Segment C (sinh viên). Owner xác nhận segment names khi fill [FILL] trong customer_brain.md.

6. **Content_id format:** `VQ-[PLATFORM]-[PILLAR]-[YYYYMMDD]-[NNN]`. Platform codes: FB, TK, IG, ZA. Pillar codes: PROD, PROMO, BTS, STORY, COM, SEASON. Có thể điều chỉnh nếu Owner yêu cầu format khác.

7. **Safety flags severity:** Phân loại BLOCKER / WARNING / NOTE dựa trên `approval_rules.md` (Phase 1.2). Owner có thể thêm flag types trong Phase sau.

---

## Không làm trong Phase 1.3

| Không làm | Lý do |
|-----------|-------|
| Tạo Google Sheet thực tế | Phase 2 — cần Owner xác nhận schema trước |
| Build n8n notification workflow | Phase 3 — sau khi Owner approve schema |
| Tạo AI Content Agent thực tế | Phase 3 — sau khi Google Sheet sẵn sàng |
| Connect Telegram Bot thực tế | Phase 3 — sau khi template được approve |
| Commit / Push code | Chờ Owner approve Phase 1.3 |

---

## Acceptance Criteria

- [ ] 7 files trong `03_APPROVAL_PIPELINE/` được tạo với nội dung đầy đủ
- [ ] 9 trạng thái được định nghĩa với transition rules và time limits
- [ ] 21 cột Google Sheet được định nghĩa với validation rules
- [ ] JSON Schema cho Content Pack có thể validate với JSON Schema validator
- [ ] Telegram templates có đủ biến để n8n điền vào
- [ ] Owner Review Checklist có thể dùng được ngay (in ra hoặc mở trên điện thoại)
- [ ] Không có secret, API key, hoặc token nào trong bất kỳ file nào
- [ ] Không có production n8n workflow được tạo
- [ ] Không có file nào liên quan đến .claude/ được stage/commit

---

## Git Status Summary

Tất cả files mới được tạo trong working tree nhưng **CHƯA được stage hay commit**.

```
Files mới (untracked):
  03_APPROVAL_PIPELINE/README.md
  03_APPROVAL_PIPELINE/status_lifecycle.md
  03_APPROVAL_PIPELINE/approval_sheet_schema.md
  03_APPROVAL_PIPELINE/content_pipeline_schema.md
  03_APPROVAL_PIPELINE/content_pack_json_schema.md
  03_APPROVAL_PIPELINE/telegram_approval_message_template.md
  03_APPROVAL_PIPELINE/owner_review_checklist.md
  docs/phase-1/PHASE_1_3_APPROVAL_SHEET_PIPELINE_SCHEMA.md
  06_HANDOFF/PHASE_STATUS.md (updated)
  06_HANDOFF/NEXT_ACTIONS.md (updated)
```

**Không có commit. Không có push.**

---

## Prompt cho Codex Reviewer

```
CODEX REVIEW REQUEST — Phase 1.3 — Approval Sheet & Pipeline Schema

Role: Codex = Reviewer only. Không sửa files. Chỉ report.

Files cần review:
1. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\README.md
2. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\status_lifecycle.md
3. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\approval_sheet_schema.md
4. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\content_pipeline_schema.md
5. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\content_pack_json_schema.md
6. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\telegram_approval_message_template.md
7. D:\FNB_OS_V1\03_APPROVAL_PIPELINE\owner_review_checklist.md
8. D:\FNB_OS_V1\docs\phase-1\PHASE_1_3_APPROVAL_SHEET_PIPELINE_SCHEMA.md

Review Policy — BLOCK chỉ khi có:
- Real secret/API key/token/password hardcoded
- .claude/ staged hoặc referenced trong commit-ready files
- Wrong major scope (files không liên quan đến Phase 1.3 objective)
- Production n8n workflow được tạo
- Auto-post / auto-reply / auto-ads execution behavior trong schema
- Files rỗng, unusable, hoặc unrelated đến Vị Cuốn

Minor metadata wording issues = WARNING only, không block.

Acceptance Criteria:
✅ 7 files trong 03_APPROVAL_PIPELINE/ có nội dung đầy đủ
✅ 9 status states được định nghĩa với transition rules
✅ 21 Google Sheet columns được định nghĩa
✅ JSON Schema có thể validate
✅ Telegram templates có đủ biến
✅ Owner Review Checklist usable
✅ Không có secret nào bị hardcode
✅ Không có production workflow
✅ Không có .claude/ reference

Output required:
1. REVIEW_PASS hoặc REVIEW_FAIL
2. Nếu FAIL: liệt kê blocker(s) cụ thể
3. Nếu WARNING: liệt kê warnings (không block)
4. Recommendation cho Owner
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — Report tạo mới. Status: REVIEW_REQUESTED. | Claude Code (Builder) |
