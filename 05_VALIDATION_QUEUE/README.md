# 05_VALIDATION_QUEUE — Vị Cuốn Growth OS

*Phase 1.5 — Content Pack Validation & Sample Queue*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*

---

## Mục đích

`05_VALIDATION_QUEUE` là cổng kiểm tra bắt buộc cho mọi Content Pack trước khi vào `03_APPROVAL_PIPELINE/`. Không Content Pack nào được phép đi thẳng từ Generator sang Approval mà bỏ qua bước này.

```
[04_CONTENT_PACK_GENERATOR]
         ↓
[05_VALIDATION_QUEUE]  ← Bạn đang ở đây
         ↓
[03_APPROVAL_PIPELINE]
         ↓
[Đăng bài / Lịch đăng]
```

---

## Files trong thư mục này

| File | Mục đích |
|------|---------|
| `content_pack_validation_rules.md` | Bộ quy tắc validation đầy đủ — 7 nhóm tiêu chí |
| `validation_checklist.md` | Checklist thực hành — dùng cho từng Content Pack |
| `revision_rules.md` | Quy tắc quyết định trạng thái sau validation (READY / NEEDS_REVIEW / REVISION / BLOCKED) |
| `sample_content_queue.md` | 10 mục queue mẫu đại diện cho các use case chính của Vị Cuốn |
| `README.md` | File này — tổng quan và hướng dẫn sử dụng |

---

## Các trạng thái Validation

| Status | Ý nghĩa | Hành động |
|--------|---------|----------|
| `READY_FOR_REVIEW` | Không có BLOCKER, không còn [FILL] quan trọng | → Chuyển vào `03_APPROVAL_PIPELINE/` |
| `NEEDS_OWNER_REVIEW` | Không BLOCKER, còn [FILL] cần Owner điền | → Owner điền → Re-validate |
| `REVISION_REQUESTED` | Nội dung yếu / brand fit kém | → Builder chỉnh → Re-validate |
| `BLOCKED` | Có vi phạm nghiêm trọng | → Dừng, báo Owner, fix trước |

---

## Quy trình sử dụng (từng Content Pack)

1. **Builder tạo Content Pack** theo `04_CONTENT_PACK_GENERATOR/input_brief_template.md`
2. **Builder tự chạy Safety Self-Check** theo `04_CONTENT_PACK_GENERATOR/safety_self_check.md`
3. **Builder validate** theo `content_pack_validation_rules.md` (7 nhóm)
4. **Builder điền checklist** trong `validation_checklist.md` cho Content Pack đó
5. **Set trạng thái** theo `revision_rules.md`
6. **Nếu READY_FOR_REVIEW** → Chuyển sang `03_APPROVAL_PIPELINE/`

---

## Lưu ý quan trọng

- AI Builder KHÔNG tự approve — chỉ đưa lên trạng thái `READY_FOR_REVIEW`
- Owner là người duy nhất quyết định `APPROVED` trong `03_APPROVAL_PIPELINE/`
- Content Pack có BLOCKER KHÔNG được vào pipeline dưới bất kỳ hình thức nào
- Mọi [FILL] quan trọng (giá, địa chỉ, SĐT, voucher code, offer status) phải Owner xác nhận trước khi READY

---

## Liên kết đến các module khác

| Module | Link |
|--------|------|
| Brand Brain | `01_BRAIN/brand_brain.md` |
| Content Pillars | `02_CONTENT_ENGINE/content_pillars.md` |
| Offer Engine | `02_CONTENT_ENGINE/offer_engine.md` |
| Approval Pipeline | `03_APPROVAL_PIPELINE/` |
| Content Pack Generator | `04_CONTENT_PACK_GENERATOR/` |
| Safety Self-Check | `04_CONTENT_PACK_GENERATOR/safety_self_check.md` |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.5 — Thư mục tạo mới. 5 files: validation_rules, checklist, revision_rules, sample_queue, README. | Claude Code (Builder) |
