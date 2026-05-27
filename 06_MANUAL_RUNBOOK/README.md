# 06_MANUAL_RUNBOOK — Vị Cuốn Growth OS

*Phase 1.6 — Manual Content Pack Runbook*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*

---

## Mục đích

`06_MANUAL_RUNBOOK` là hướng dẫn để Owner **tự tay chạy** một Content Pack hoàn chỉnh qua toàn bộ hệ thống FnB OS V1 — từ lúc chọn nội dung đến khi đăng bài lên mạng xã hội.

Đây là **Phase 1.6 — First Manual Test Run** — lần đầu tiên Owner kiểm tra toàn bộ luồng hệ thống đã xây từ Phase 1.1 đến 1.5, không cần code và không tự động hóa.

---

## Files trong thư mục này

| File | Mục đích | Đọc trước |
|------|---------|----------|
| `manual_content_pack_runbook.md` | Runbook chính — 7 bước từ đầu đến cuối | Đọc đầu tiên |
| `manual_test_input_examples.md` | 3 kịch bản mẫu đã điền sẵn để test ngay | Dùng thay vì tự nghĩ brief |
| `manual_output_template.md` | Template ghi lại output AI theo chuẩn | Dùng khi nhận output AI |
| `owner_approval_flow.md` | Hướng dẫn chi tiết bước duyệt và quyết định | Dùng tại Bước 6 |
| `README.md` | File này — tổng quan và hướng dẫn bắt đầu | Đọc đầu tiên |

---

## Luồng Hệ thống Đầy đủ

```
01_BRAIN/                  → Nguồn thông tin thương hiệu
02_CONTENT_ENGINE/         → Pillar, angle, offer logic
04_CONTENT_PACK_GENERATOR/ → Prompt template + brief form
         ↓
06_MANUAL_RUNBOOK/         ← Bạn đang ở đây
  [Owner điền brief]
  [AI tạo Content Pack DRAFT]
  [Owner validate + approve]
         ↓
05_VALIDATION_QUEUE/       → 7 nhóm validation rules
03_APPROVAL_PIPELINE/      → Owner review checklist
         ↓
[Owner đăng tay sau APPROVED]
```

---

## Bắt đầu Nhanh (5 phút)

1. **Mở** `manual_test_input_examples.md`
2. **Chọn** Kịch bản 2 (TikTok BTS — Mắm Nêm) — ít [FILL] nhất, dễ READY_FOR_REVIEW nhất
3. **Copy** brief đã điền sẵn trong Kịch bản 2
4. **Mở** `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md` — copy prompt template
5. **Paste** brief vào cuối prompt → thay {{PLACEHOLDER}} bằng giá trị từ brief
6. **Gửi** cho Claude Code (AI Worker)
7. **Nhận** Content Pack DRAFT → điền vào `manual_output_template.md`
8. **Validate** theo `05_VALIDATION_QUEUE/validation_checklist.md`
9. **Duyệt** theo `owner_approval_flow.md`
10. **Đăng tay** nếu APPROVED

---

## STOP Rules Tóm tắt

Dừng ngay nếu:
- Caption có giá/địa chỉ/SĐT/KM chưa xác nhận thật
- Caption có fake review / fake discount
- AI output có lệnh auto-post
- `approval.status` ≠ `DRAFT`
- Owner chưa APPROVED nhưng có ai/hệ thống đăng bài

---

## Liên kết Hệ thống

| Module | Link |
|--------|------|
| Brand Brain | `01_BRAIN/brand_brain.md` |
| Offer Engine | `02_CONTENT_ENGINE/offer_engine.md` |
| Content Pillars | `02_CONTENT_ENGINE/content_pillars.md` |
| Input Brief Form | `04_CONTENT_PACK_GENERATOR/input_brief_template.md` |
| Prompt Template | `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md` |
| Validation Rules | `05_VALIDATION_QUEUE/content_pack_validation_rules.md` |
| Validation Checklist | `05_VALIDATION_QUEUE/validation_checklist.md` |
| Revision Rules | `05_VALIDATION_QUEUE/revision_rules.md` |
| Owner Review Checklist | `03_APPROVAL_PIPELINE/owner_review_checklist.md` |
| Safety Self-Check | `04_CONTENT_PACK_GENERATOR/safety_self_check.md` |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.6 — Thư mục tạo mới. 5 files: runbook (7 bước, 10 stop rules), 3 kịch bản test, output template, approval flow, README. | Claude Code (Builder) |
