# 07_MANUAL_TEST_RUN — Vị Cuốn Growth OS

*Phase 1.7 — First Manual Content Pack Test*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*

---

## Mục đích

`07_MANUAL_TEST_RUN` lưu trữ kết quả của các lần chạy manual content pack test — bằng chứng thực tế rằng hệ thống FnB OS V1 hoạt động từ đầu đến cuối mà không cần code hay automation.

Đây là đầu ra sau khi Owner (hoặc Builder) đã chạy theo runbook tại `06_MANUAL_RUNBOOK/`.

---

## Cấu trúc File

| File | Nội dung | Phase |
|------|---------|-------|
| `README.md` | File này — tổng quan | 1.7 |
| `content_pack_VQ-TK-BTS-20260527-001.md` | Content Pack đầu tiên — TikTok BTS Mắm Nêm | 1.7 |

---

## Luồng Test

```
Kịch bản 2 (manual_test_input_examples.md)
        ↓
Builder điền brief → AI Worker (Claude Code) tạo content pack
        ↓
07_MANUAL_TEST_RUN/content_pack_VQ-TK-BTS-20260527-001.md  ← Bạn đang ở đây
        ↓
Owner chạy validation_checklist.md (05_VALIDATION_QUEUE/)
        ↓
Owner chạy owner_approval_flow.md (06_MANUAL_RUNBOOK/)
        ↓
Owner quyết định: APPROVED → Đăng tay → Ghi link
```

---

## Test Runs

| # | Content ID | Kịch bản | Platform | Status | Ngày |
|---|-----------|---------|---------|--------|------|
| 1 | VQ-TK-BTS-20260527-001 | Rainy Day / Mắm Nêm | TikTok | READY_FOR_REVIEW | 2026-05-27 |

---

## Liên kết Hệ thống

| Module | Link |
|--------|------|
| Runbook | `06_MANUAL_RUNBOOK/manual_content_pack_runbook.md` |
| Input Brief | `06_MANUAL_RUNBOOK/manual_test_input_examples.md` → Kịch bản 2 |
| Output Template | `06_MANUAL_RUNBOOK/manual_output_template.md` |
| Validation Checklist | `05_VALIDATION_QUEUE/validation_checklist.md` |
| Approval Flow | `06_MANUAL_RUNBOOK/owner_approval_flow.md` |
| Owner Review Checklist | `03_APPROVAL_PIPELINE/owner_review_checklist.md` |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.7 — Thư mục tạo mới. First manual test: VQ-TK-BTS-20260527-001 (TikTok BTS Mắm Nêm). | Claude Code (Builder) |
