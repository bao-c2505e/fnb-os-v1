# PHASE 1.5 — Content Pack Validation & Sample Queue

**Status:** REVIEW_REQUESTED
**Phase:** 1.5
**Builder:** Claude Code (AGT-02)
**Date:** 2026-05-27
**Branch:** main
**Previous Phase:** 1.4 — Draft Content Pack Generator Schema (CLOSED, commit: 898921d)

---

## Mục tiêu Phase 1.5

Tạo hệ thống validation và sample queue để mọi Content Pack có thể được kiểm tra đầy đủ **trước khi** vào Approval Pipeline. Phase này đặt nền tảng cho vòng kiểm soát chất lượng tự động hóa từng bước.

---

## Files được tạo trong Phase này

### Thư mục mới: `05_VALIDATION_QUEUE/`

| File | Mô tả ngắn | Dòng |
|------|-----------|------|
| `README.md` | Tổng quan module, flow, cách dùng | ~70 dòng |
| `content_pack_validation_rules.md` | 7 nhóm validation rules đầy đủ | ~180 dòng |
| `validation_checklist.md` | Checklist thực hành theo từng Content Pack | ~200 dòng |
| `revision_rules.md` | 4 rule sets quyết định trạng thái sau validate | ~200 dòng |
| `sample_content_queue.md` | 10 mục queue mẫu đại diện Vị Cuốn | ~400 dòng |

### Docs:

| File | Mô tả |
|------|-------|
| `docs/phase-1/PHASE_1_5_CONTENT_PACK_VALIDATION_SAMPLE_QUEUE.md` | File này |

---

## Validation Rules — Tóm tắt 7 Nhóm

| Nhóm | Tên | Số tiêu chí | BLOCKER | WARNING | NOTE |
|------|-----|------------|---------|---------|------|
| V1 | Brand Fit | 8 | 2 | 4 | 2 |
| V2 | Menu/Product Fit | 5 | 2 | 2 | 1 |
| V3 | Platform Fit | 5 | 1 | 3 | 1 |
| V4 | Offer Validity | 6 | 3 | 2 | 1 |
| V5 | Safety & Compliance | 7 | 5 | 1 | 1 |
| V6 | Owner Approval Readiness | 6 | 1 | 3 | 2 |
| V7 | [FILL]/[OWNER_CONFIRM] Handling | 6 | 2 | 2 | 2 |
| **Tổng** | | **43 tiêu chí** | **16 BLOCKER** | **17 WARNING** | **10 NOTE** |

---

## Revision Rules — Tóm tắt

| Rule Set | Status kết quả | Trigger điều kiện | Số rules |
|----------|---------------|-----------------|---------|
| R1 | NEEDS_OWNER_REVIEW | Thiếu giá, địa chỉ, SĐT, offer status, real promo chưa xác nhận | 5 |
| R2 | BLOCKED | Fake review, fake discount, health claim, competitor mention, auto-trigger, secret exposed | 6 |
| R3 | REVISION_REQUESTED | Brand fit yếu, pillar mismatch, thiếu CTA, caption sai độ dài | 4 |
| R4 | READY_FOR_REVIEW | 0 BLOCKER + không còn [FILL] quan trọng + đủ điều kiện | 7 điều kiện |

---

## Sample Content Queue — Tóm tắt 10 Mục

| # | Content ID | Category | Platform | Validation Status |
|---|-----------|---------|---------|------------------|
| 1 | VQ-FB-PROMO-20260527-001 | Office Lunch | Facebook | NEEDS_OWNER_REVIEW |
| 2 | VQ-TK-PROD-20260527-002 | Office Lunch | TikTok | NEEDS_OWNER_REVIEW |
| 3 | VQ-ZL-PROMO-20260527-003 | Office Lunch | Zalo OA | NEEDS_OWNER_REVIEW |
| 4 | VQ-FB-PROMO-20260527-004 | Rainy Day | Facebook | NEEDS_OWNER_REVIEW |
| 5 | VQ-TK-BTS-20260527-005 | Mắm Nêm Craving | TikTok | **READY_FOR_REVIEW** |
| 6 | VQ-FB-PROMO-20260527-006 | Group/Family Combo | Facebook | NEEDS_OWNER_REVIEW |
| 7 | VQ-IG-PROD-20260527-007 | Group/Family Combo | Instagram | NEEDS_OWNER_REVIEW |
| 8 | VQ-FB-PROMO-20260527-008 | New Customer | Facebook | NEEDS_OWNER_REVIEW |
| 9 | VQ-ZL-PROMO-20260527-009 | Comeback Customer | Zalo OA | NEEDS_OWNER_REVIEW |
| 10 | VQ-FB-SEASON-20260527-010 | Weekend/Seasonal | Facebook | NEEDS_OWNER_REVIEW |

**Item duy nhất READY_FOR_REVIEW:** Item 05 (TikTok BTS — Mắm Nêm) — vì BTS content không cần giá/địa chỉ trong caption, không có BLOCKER, và caption không có [FILL] quan trọng.

---

## [FILL] Quan Trọng Nhất Cần Owner Điền

Để unblock 9/10 items còn lại, Owner cần điền (theo thứ tự ưu tiên):

| Thứ tự | Field | File cần cập nhật | Ảnh hưởng |
|--------|-------|------------------|----------|
| 1 | Địa chỉ chi tiết | `01_BRAIN/brand_brain.md` | 7/10 items |
| 2 | Số điện thoại | `01_BRAIN/brand_brain.md` | 6/10 items |
| 3 | Giá Combo Trưa (OF-01) | `02_CONTENT_ENGINE/offer_engine.md` | 2/10 items |
| 4 | Giá Combo Cuối Tuần (OF-02) | `02_CONTENT_ENGINE/offer_engine.md` | 2/10 items |
| 5 | Giá Combo Gia Đình (OF-03) | `02_CONTENT_ENGINE/offer_engine.md` | 1/10 items |
| 6 | OF-01 → OF-08 trạng thái (ACTIVE/INACTIVE) | `02_CONTENT_ENGINE/offer_engine.md` | 9/10 items |
| 7 | Voucher code VQ-NEW + VQ-BACK | Google Sheet Vouchers | 2/10 items |
| 8 | Offer detail OF-04 (form ưu đãi khách mới) | `02_CONTENT_ENGINE/offer_engine.md` | 1/10 items |
| 9 | Offer detail OF-05 (form comeback) | `02_CONTENT_ENGINE/offer_engine.md` | 1/10 items |

---

## Giả định đã đặt trong Phase này

| # | Giả định | Lý do |
|---|---------|-------|
| A1 | Item 05 (TikTok BTS) là READY_FOR_REVIEW vì BTS pillar không require giá/địa chỉ trong caption | Theo content_pillars.md Pillar 2 — BTS focus vào authenticity, không push offer/price |
| A2 | Giá combo ~65k (OF-01), ~80k (OF-02), ~130-140k (OF-03) dùng làm placeholder tạm thời | Dựa trên price range 60-80k/người trong brand_brain.md |
| A3 | Zalo OA không dùng hashtag (hashtag = 0) | Theo content_pillars.md Platform Mapping |
| A4 | OF-06 (Ngày Mưa) chỉ Owner kích hoạt thủ công — không bao giờ tự đăng | Quy tắc rõ trong offer_engine.md: "KHÔNG tự đăng" |
| A5 | Danh sách khách lapsed (OF-05) được Owner quản lý thủ công — CRM automation chưa có Phase này | CRM automation thuộc Phase sau |
| A6 | 3 items cần Owner quay/chụp media thật (Items 02, 05, 07) — AI Builder không tự tạo ảnh/video | Theo brand_brain.md "Không dùng ảnh stock" |
| A7 | Voucher code phải đăng ký trong Google Sheet Vouchers trước khi đưa vào caption | Theo offer_engine.md Voucher Safety Rules |

---

## Quy trình Flow sau Phase 1.5

```
Content Pack mới (DRAFT)
        ↓
Builder chạy Safety Self-Check (04_CONTENT_PACK_GENERATOR/safety_self_check.md)
        ↓
Builder validate 7 nhóm (05_VALIDATION_QUEUE/content_pack_validation_rules.md)
        ↓
Builder điền checklist (05_VALIDATION_QUEUE/validation_checklist.md)
        ↓
Set trạng thái theo revision_rules.md:
  BLOCKED → Dừng, fix trước
  NEEDS_OWNER_REVIEW → Owner điền [FILL] → Re-validate
  REVISION_REQUESTED → Builder chỉnh → Re-validate
  READY_FOR_REVIEW → Vào 03_APPROVAL_PIPELINE/
        ↓
Owner review trong Approval Pipeline
        ↓
APPROVED → Lên lịch đăng
REJECTED → Builder chỉnh lại
```

---

## Checklist Phase 1.5 — Builder Verification

- [x] Thư mục `05_VALIDATION_QUEUE/` tạo mới
- [x] `content_pack_validation_rules.md` — 7 nhóm, 43 tiêu chí
- [x] `validation_checklist.md` — Checklist thực hành đầy đủ
- [x] `revision_rules.md` — 4 rule sets, 15 rules cụ thể
- [x] `sample_content_queue.md` — 10 items (3+2+2+1+1+1)
- [x] Mỗi item có: content_id, platform, persona, pillar, angle, offer_type, draft_status, validation_status, safety_flags, missing_fields, next_action
- [x] Validation categories đầy đủ: brand fit, menu/product fit, platform fit, offer validity, safety/compliance, owner approval readiness, [FILL] handling
- [x] Revision rules cover: missing price/address/phone/promo → OWNER_CONFIRM; fake claim/review/discount → BLOCKER; weak brand fit → REVISION_REQUESTED; safe and complete → READY_FOR_REVIEW
- [x] `docs/phase-1/PHASE_1_5_...md` tạo mới
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
phase: 1.5
status: CLOSED
opened: 2026-05-27
closed: 2026-05-27
builder: Claude Code (AGT-02 — claude-sonnet-4-6)
reviewer: Codex (AGT-04) — PASS
owner_approved: APPROVED
commit_hash: e18123b
files_created:
  - 05_VALIDATION_QUEUE/README.md
  - 05_VALIDATION_QUEUE/content_pack_validation_rules.md
  - 05_VALIDATION_QUEUE/validation_checklist.md
  - 05_VALIDATION_QUEUE/revision_rules.md
  - 05_VALIDATION_QUEUE/sample_content_queue.md
  - docs/phase-1/PHASE_1_5_CONTENT_PACK_VALIDATION_SAMPLE_QUEUE.md
files_updated:
  - logs/build_log.md (PENDING)
  - handoff/CURRENT_HANDOFF.md (PENDING)
```
