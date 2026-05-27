# PHASE 1.6 — Manual Content Pack Runbook

**Status:** CLOSED
**Phase:** 1.6
**Builder:** Claude Code (AGT-02)
**Date:** 2026-05-27
**Branch:** main
**Previous Phase:** 1.5 — Content Pack Validation & Sample Queue (CLOSED, commit: e18123b)

---

## Mục tiêu Phase 1.6

Tạo runbook thực hành để Owner có thể tự chạy một Content Pack hoàn chỉnh theo đúng luồng FnB OS V1 — không cần code, không cần kỹ thuật. Đây là **first manual test run** của toàn bộ hệ thống đã xây từ Phase 1.1 đến 1.5.

---

## Files được tạo trong Phase này

### Thư mục mới: `06_MANUAL_RUNBOOK/`

| File | Mô tả | Dòng |
|------|-------|------|
| `README.md` | Tổng quan, bắt đầu nhanh, liên kết hệ thống | ~80 dòng |
| `manual_content_pack_runbook.md` | Runbook chính 7 bước + 10 STOP rules | ~230 dòng |
| `manual_test_input_examples.md` | 3 kịch bản test mẫu đã điền sẵn | ~200 dòng |
| `manual_output_template.md` | Template ghi nhận output Content Pack | ~160 dòng |
| `owner_approval_flow.md` | Hướng dẫn chi tiết bước duyệt | ~250 dòng |

### Docs:
| File | Mô tả |
|------|-------|
| `docs/phase-1/PHASE_1_6_MANUAL_CONTENT_PACK_RUNBOOK.md` | File này |

---

## Runbook — Tóm tắt 7 Bước

| Bước | Tên | Thời gian | Output |
|------|-----|----------|--------|
| 1 | Chuẩn bị — kiểm tra [FILL] | 5 phút | Biết thiếu gì trước khi tạo |
| 2 | Điền Input Brief | 5–10 phút | Brief hoàn chỉnh |
| 3 | Gửi brief cho AI Worker | 2 phút | Prompt đã điền placeholder |
| 4 | Nhận và lưu Content Pack DRAFT | 2 phút | Content Pack đã lưu vào template |
| 5 | Validate 7 nhóm | 10 phút | Validation status: READY / NEEDS_REVIEW / REVISION / BLOCKED |
| 6 | Owner Approval | 5 phút | APPROVED / REVISION / REJECTED |
| 7 | Đăng tay + ghi link | 2–5 phút | Status PUBLISHED_MANUAL |
| **Tổng** | | **~30 phút** | **Content Pack đã đăng** |

---

## 10 STOP Rules

| # | Trigger | Hành động |
|---|---------|----------|
| S1 | Giá cụ thể nhưng chưa xác nhận trong offer_engine.md | Dừng. Điền giá thật trước. |
| S2 | Địa chỉ trong caption nhưng chưa điền trong brand_brain.md | Dừng. Điền địa chỉ thật trước. |
| S3 | SĐT trong caption nhưng chưa điền trong brand_brain.md | Dừng. Điền SĐT thật trước. |
| S4 | KM cụ thể nhưng Owner chưa xác nhận tồn tại | Dừng. Xác nhận KM thật trước. |
| S5 | Caption gợi ý fake review / fake discount | Dừng. Yêu cầu AI viết lại. |
| S6 | AI output có lệnh tự đăng / gọi API | Dừng ngay. Báo cáo lỗi. |
| S7 | `approval.status` ≠ `DRAFT` | Dừng. AI Worker đã sai. |
| S8 | Bất kỳ hệ thống nào đăng bài khi chưa Owner APPROVE | Dừng. Không chấp nhận. |
| S9 | Caption có claim sức khỏe | Dừng. AI viết lại hoàn toàn. |
| S10 | Caption nhắc tên đối thủ | Dừng. AI xóa và viết lại. |

---

## 3 Kịch bản Test Mẫu

| # | Kịch bản | Platform | Pillar | Offer | [FILL] cần | Độ khó |
|---|---------|---------|-------|-------|-----------|--------|
| 1 | Office Lunch — Combo Trưa | Facebook | PROMO | OF-01 | Giá + Địa chỉ + SĐT | Trung bình |
| 2 | Rainy Day / Mắm Nêm Craving | TikTok | BTS | Không | Không có | **Dễ nhất** |
| 3 | Group/Family Combo Cuối Tuần | Facebook + Instagram | PROMO | OF-03 | Giá + Địa chỉ + SĐT | Khó hơn (multi-platform) |

**Gợi ý lần đầu:** Chạy Kịch bản 2 — TikTok BTS không có offer, không cần giá/địa chỉ trong caption, sẽ đạt READY_FOR_REVIEW ngay sau khi AI tạo.

---

## Owner Approval Flow — Tóm tắt

```
Nhận Content Pack DRAFT
        ↓
Quick Gut Check (2 phút) → bài có cảm giác đúng không?
        ↓
Stop Rules Check (1 phút) → 10 rules kiểm tra nhanh
        ↓
Owner Review Checklist (5–10 phút) → 6 phần đầy đủ
        ↓
4 câu tự hỏi → tự tin đăng không?
        ↓
Ra quyết định:
  APPROVED → Lên lịch → Đăng tay → Ghi link
  REVISION → Ghi revision note cụ thể → AI sửa → Lặp lại (tối đa 3 lần)
  REJECTED → Không đăng → Brief lại nếu muốn
```

---

## Luồng Tích hợp Hệ thống

Phase 1.6 tích hợp và test toàn bộ outputs từ Phase 1.1 đến 1.5:

| Module | Phase tạo | Dùng ở Bước |
|--------|---------|------------|
| `01_BRAIN/brand_brain.md` | 1.1 | 1 (chuẩn bị) + 3 (AI đọc) |
| `01_BRAIN/menu_brain.md` | 1.1 | 5 (validate V2) |
| `02_CONTENT_ENGINE/content_pillars.md` | 1.2 | 2 (brief) + 3 (AI đọc) |
| `02_CONTENT_ENGINE/offer_engine.md` | 1.2 | 2 (brief) + 5 (validate V4) |
| `03_APPROVAL_PIPELINE/owner_review_checklist.md` | 1.3 | 6 (approval) |
| `04_CONTENT_PACK_GENERATOR/input_brief_template.md` | 1.4 | 2 (brief) |
| `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md` | 1.4 | 3 (gửi AI) |
| `04_CONTENT_PACK_GENERATOR/safety_self_check.md` | 1.4 | 4 (AI tự check) |
| `05_VALIDATION_QUEUE/validation_checklist.md` | 1.5 | 5 (validate) |
| `05_VALIDATION_QUEUE/revision_rules.md` | 1.5 | 5 (set status) |

---

## Giả định đã đặt trong Phase này

| # | Giả định | Lý do |
|---|---------|-------|
| A1 | Owner tự giao tiếp với AI Worker (Claude Code) qua chat — chưa có tự động hóa | Automation thuộc Phase 3 (n8n) |
| A2 | Owner đang dùng Claude Code (claude.ai/code hoặc VSCode extension) | Đây là môi trường hiện tại của Builder |
| A3 | Google Drive/Sheet chưa kết nối — Owner lưu output vào file manual hoặc copy paste | Kết nối GDrive/GSheet thuộc Phase 2+ |
| A4 | Telegram approval notification chưa hoạt động — Owner duyệt thủ công qua checklist | Telegram bot thuộc Phase 3 |
| A5 | Kịch bản 2 (TikTok BTS) được đề xuất là "lần đầu tiên" vì không có [FILL] quan trọng | Dựa trên kết quả Phase 1.5 — Item 05 trong sample queue đã là READY_FOR_REVIEW |
| A6 | Revision tối đa 3 lần — sau đó REJECT và brief lại | Theo owner_review_checklist.md "Escalation" rule |

---

## Checklist Phase 1.6 — Builder Verification

- [x] Thư mục `06_MANUAL_RUNBOOK/` tạo mới
- [x] `manual_content_pack_runbook.md` — 7 bước, 10 STOP rules
- [x] `manual_test_input_examples.md` — 3 kịch bản (office lunch, rainy day/mắm nêm, group/family)
- [x] `manual_output_template.md` — Template đầy đủ 11 sections
- [x] `owner_approval_flow.md` — Sơ đồ quyết định, 4 câu tự hỏi, ma trận quyết định
- [x] `README.md` — Tổng quan và bắt đầu nhanh
- [x] STOP rules cover: missing price/address/phone/promo → STOP; fake claim/review → STOP; auto-post → STOP; status ≠ APPROVED → STOP; Owner chưa confirm → STOP
- [x] 3 kịch bản test: office lunch (Facebook PROMO OF-01), rainy day BTS (TikTok, không offer), group/family (multi-platform PROMO OF-03)
- [x] `docs/phase-1/PHASE_1_6_MANUAL_CONTENT_PACK_RUNBOOK.md` tạo mới
- [x] Không commit
- [x] Không push
- [x] Không kết nối real API
- [x] Không tạo production n8n workflow
- [x] Không auto-post

---

## Strict Rules Compliance

| Rule | Status |
|------|--------|
| Không tạo production n8n workflow | ✓ Tuân thủ |
| Không kết nối real API | ✓ Tuân thủ |
| Không auto-post / auto-reply / run ads | ✓ Tuân thủ |
| Không hardcode secret | ✓ Tuân thủ |
| Không commit .claude/ | ✓ Tuân thủ |
| Không commit / push | ✓ Tuân thủ — chờ Owner approval |

---

## Phase Close Metadata

```
phase: 1.6
status: CLOSED
opened: 2026-05-27
closed: 2026-05-27
builder: Claude Code (AGT-02 — claude-sonnet-4-6)
reviewer: Codex (AGT-04) — PASS
owner_approved: APPROVED
commit_hash: cd314bd
files_created:
  - 06_MANUAL_RUNBOOK/README.md
  - 06_MANUAL_RUNBOOK/manual_content_pack_runbook.md
  - 06_MANUAL_RUNBOOK/manual_test_input_examples.md
  - 06_MANUAL_RUNBOOK/manual_output_template.md
  - 06_MANUAL_RUNBOOK/owner_approval_flow.md
  - docs/phase-1/PHASE_1_6_MANUAL_CONTENT_PACK_RUNBOOK.md
files_updated:
  - logs/CURRENT_STATUS.md
  - logs/AGENT_ACTIVITY_LOG.md
  - handoff/CURRENT_PHASE.md
  - 06_HANDOFF/PHASE_STATUS.md
  - 06_HANDOFF/NEXT_ACTIONS.md
```
