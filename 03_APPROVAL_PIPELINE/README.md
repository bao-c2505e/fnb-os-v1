# 03_APPROVAL_PIPELINE — Approval Queue & Pipeline Schema

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Trung tâm kiểm soát luồng duyệt nội dung của Vị Cuốn.*

---

## Mục đích

Thư mục này định nghĩa toàn bộ schema và luồng dữ liệu cho hệ thống phê duyệt nội dung. Đây là tầng trung gian giữa AI tạo nội dung (02_CONTENT_ENGINE) và việc đăng bài thực tế.

**Nguyên tắc trung tâm:** AI chỉ tạo — Owner quyết định — không có gì được đăng mà không qua Owner.

---

## Files trong thư mục này

| File | Mục đích | Dùng bởi |
|------|---------|---------|
| `README.md` | File này — overview và hướng dẫn dùng | Tất cả |
| `status_lifecycle.md` | 9 trạng thái, transition rules, time limits | AI Agent, n8n, Owner |
| `approval_sheet_schema.md` | 21 cột của Google Sheet "Content Approval Queue" | AI Agent, n8n |
| `content_pipeline_schema.md` | Luồng đầy đủ từ Idea → Published → Archived (8 stages) | Builder, n8n |
| `content_pack_json_schema.md` | JSON Schema đầy đủ của Content Pack + ví dụ | AI Agent, n8n |
| `telegram_approval_message_template.md` | 7 templates tin nhắn Telegram cho Owner | n8n |
| `owner_review_checklist.md` | Checklist 6 phần Owner dùng khi review | Owner |

---

## Luồng Tóm tắt

```
AI tạo Content Pack (JSON)
    ↓
Ghi vào Google Sheet: Content Approval Queue
    ↓
Telegram notification → Owner
    ↓
Owner review (dùng owner_review_checklist.md)
    ↓
APPROVED → Owner đăng tay → PUBLISHED_MANUAL
```

---

## Trạng thái Nội dung (Tóm tắt)

| Trạng thái | Ai set | Ý nghĩa |
|-----------|--------|---------|
| `IDEA` | AI/Owner | Ý tưởng chưa có draft |
| `DRAFT` | AI | AI đang viết, chưa check xong |
| `READY_FOR_REVIEW` | AI | AI đã check pass, chờ Owner |
| `REVISION_REQUESTED` | **Owner** | Owner muốn AI sửa lại |
| `APPROVED` | **Owner** | Owner đã duyệt |
| `SCHEDULE_PROPOSED` | **Owner** | Đã chọn ngày đăng |
| `PUBLISHED_MANUAL` | **Owner** | Đã đăng tay |
| `REJECTED` | **Owner** | Từ chối hoàn toàn |
| `ARCHIVED` | System/Owner | Kết thúc vòng đời |

→ Xem đầy đủ: [status_lifecycle.md](status_lifecycle.md)

---

## Dependencies (Phụ thuộc)

Files trong thư mục này đọc từ:

| File | Lý do cần |
|------|-----------|
| `01_BRAIN/brand_brain.md` | Brand voice, safety rules |
| `01_BRAIN/menu_brain.md` | Xác minh giá trong content |
| `02_CONTENT_ENGINE/content_pillars.md` | Pillar codes (PROD, BTS, PROMO, v.v.) |
| `02_CONTENT_ENGINE/content_angles.md` | Angle codes (ANG-01, v.v.) |
| `02_CONTENT_ENGINE/offer_engine.md` | Xác minh offer ID và giá |
| `02_CONTENT_ENGINE/approval_rules.md` | Safety rules cho self-check |

---

## Approval Rules Tóm tắt (Quy tắc Không Thương lượng)

### AI được phép

- ✅ Tạo caption, script, image brief, design brief
- ✅ Chọn pillar, angle, persona
- ✅ Tự chạy safety self-check
- ✅ Set status: IDEA → DRAFT → READY_FOR_REVIEW
- ✅ Gửi Telegram notification cho Owner
- ✅ Đọc revision_note và sửa bài

### AI KHÔNG được phép

- ❌ Tự set status = APPROVED
- ❌ Tự đăng bài lên bất kỳ platform nào
- ❌ Tự reply comment / tin nhắn khách hàng
- ❌ Tự tạo offer ngoài offer_engine.md
- ❌ Tự lên lịch đăng (auto-schedule)
- ❌ Chạy quảng cáo trả phí
- ❌ Set READY_FOR_REVIEW khi còn BLOCKER flag

### Owner bắt buộc

- ✅ Đọc checklist trước khi approve
- ✅ Điền revision_note khi yêu cầu sửa
- ✅ Đăng bài thủ công sau khi approve
- ✅ Điền manual_publish_link sau khi đăng

---

## Phase Readiness (Sẵn sàng đến đâu)

| Component | Phase 1.3 | Phase 2 | Phase 3 |
|-----------|-----------|---------|---------|
| Schema định nghĩa | ✅ DONE | — | — |
| Google Sheet setup thực tế | 📋 Schema ready | ✅ Build | — |
| AI tạo Content Pack | 📋 Schema ready | ✅ Build | — |
| Telegram notification | 📋 Template ready | — | ✅ Build |
| n8n Approval Monitor | 📋 Spec ready | — | ✅ Build |
| Auto-reminder | 📋 Spec ready | — | ✅ Build |
| Telegram Command Parser | 📋 Spec ready | — | ✅ Build |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — Thư mục tạo mới. 7 files: README, status_lifecycle, approval_sheet_schema, content_pipeline_schema, content_pack_json_schema, telegram_approval_message_template, owner_review_checklist. | Claude Code (Builder) |
