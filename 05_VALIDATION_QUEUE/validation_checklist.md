# Validation Checklist — Vị Cuốn Content Pack

*Phase 1.5 — Content Pack Validation & Sample Queue*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Dùng cho từng Content Pack khi bước vào Validation Queue*

---

## Cách dùng Checklist này

1. In ra hoặc copy một bản cho mỗi Content Pack cần validate.
2. Điền `Content Pack ID`, `Validator`, `Date` ở đầu.
3. Chạy qua từng mục — tick `[x]` cho Pass, ghi chú cho Fail/Warn.
4. Điền Bảng Tổng Kết ở cuối.
5. Set `validation_status` trong Content Pack theo kết quả.

---

## THÔNG TIN CƠ BẢN

```
Content Pack ID:  ___________________________
Platform:         ___________________________
Pillar:           ___________________________
Persona:          ___________________________
Offer (nếu có):   ___________________________
Validated by:     ___________________________
Validated date:   ___________________________
```

---

## CHECKLIST NHANH — 5 PHÚT

*Dùng cho quick-scan trước khi validate đầy đủ*

| # | Kiểm tra nhanh | OK? |
|---|---------------|-----|
| Q1 | Content Pack có `content_id` hợp lệ theo format `VQ-[PLAT]-[PILLAR]-[YYYYMMDD]-[SEQ]`? | [ ] |
| Q2 | `approval.status = DRAFT`? | [ ] |
| Q3 | Không có secret/API key trong output? | [ ] |
| Q4 | Không có tên đối thủ trong caption? | [ ] |
| Q5 | Không có claim sức khỏe trong caption? | [ ] |
| Q6 | Không có offer tự tạo ngoài offer_engine.md? | [ ] |
| Q7 | Không có lệnh auto-post / auto-reply? | [ ] |

**Nếu bất kỳ Q nào = Không → BLOCKER. Dừng. Không tiếp tục.**

---

## PHẦN 1 — BRAND FIT

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V1-01 | Caption KHÔNG nhắc tên đối thủ | [ ] Pass [ ] **FAIL** | |
| V1-02 | Caption KHÔNG claim sức khỏe | [ ] Pass [ ] **FAIL** | |
| V1-03 | Giọng văn KHÔNG trang trọng xa cách | [ ] Pass [ ] Warn | |
| V1-04 | Giọng điệu ấm áp, gần gũi, đúng brand voice | [ ] Pass [ ] Warn | |
| V1-05 | Emoji tối đa 2–3 trong toàn caption | [ ] Pass [ ] Warn | Đếm: ___ |
| V1-06 | Không viết hoa toàn câu | [ ] Pass [ ] Warn | |
| V1-07 | Có hashtag #VịCuốn và #ĂnVinh | [ ] Yes [ ] Missing | |
| V1-08 | Nội dung đúng pillar đã khai báo | [ ] Yes [ ] Mismatch | |

**Brand Fit tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## PHẦN 2 — MENU / PRODUCT FIT

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V2-01 | Mọi món đề cập có trong menu_brain.md | [ ] Pass [ ] **FAIL** | Món không có: ___ |
| V2-02 | Giá tiền đến từ menu_brain.md / offer_engine.md | [ ] Pass [ ] **FAIL** | |
| V2-03 | Giá chưa xác nhận → dùng [FILL: ~XXđ] | [ ] Pass [ ] Warn | |
| V2-04 | Mô tả món ăn chính xác, không phóng đại | [ ] Pass [ ] Warn | |
| V2-05 | Có mô tả giác quan phù hợp | [ ] Yes [ ] Missing | |

**Product Fit tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## PHẦN 3 — PLATFORM FIT

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V3-01 | Platform hợp lệ | [ ] Pass [ ] **FAIL** | Platform: ___ |
| V3-02 | Content type phù hợp platform | [ ] Pass [ ] Warn | Type: ___ |
| V3-03 | Độ dài caption trong ngưỡng | [ ] Pass [ ] Warn | Ký tự: ___ / Ngưỡng: ___ |
| V3-04 | Số hashtag đúng theo platform | [ ] Pass [ ] Warn | Số lượng: ___ |
| V3-05 | Thời điểm đăng đề xuất hợp lý | [ ] Yes [ ] Missing | |

**Platform Fit tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## PHẦN 4 — OFFER VALIDITY

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V4-01 | Offer có trong offer_engine.md | [ ] Pass [ ] **FAIL** [ ] N/A | Offer ID: ___ |
| V4-02 | Voucher code đã đăng ký (nếu có) | [ ] Pass [ ] **FAIL** [ ] N/A | Code: ___ |
| V4-03 | Không có áp lực giả | [ ] Pass [ ] **FAIL** | |
| V4-04 | Offer status [FILL] → có [OWNER_CONFIRM] | [ ] Pass [ ] Warn [ ] N/A | |
| V4-05 | Điều kiện offer trình bày rõ trong caption | [ ] Yes [ ] Missing [ ] N/A | |
| V4-06 | Offer phù hợp với target persona | [ ] Yes [ ] Mismatch | |

**Offer Validity tổng:** [ ] PASS [ ] WARN [ ] FAIL [ ] N/A

---

## PHẦN 5 — SAFETY & COMPLIANCE

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V5-01 | Không có secret/credential thật | [ ] Pass [ ] **FAIL** | |
| V5-02 | Không có thông tin cá nhân khách thật | [ ] Pass [ ] **FAIL** | |
| V5-03 | Không có lệnh auto-post/gọi API | [ ] Pass [ ] **FAIL** | |
| V5-04 | Không có review/đánh giá giả mạo | [ ] Pass [ ] **FAIL** | |
| V5-05 | Không có discount giả không có thật | [ ] Pass [ ] **FAIL** | |
| V5-06 | Không dùng ảnh stock / ảnh không phải quán | [ ] Pass [ ] Warn | |
| V5-07 | Không vi phạm chính sách quảng cáo platform | [ ] Yes [ ] Risk | |

**Safety tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## PHẦN 6 — OWNER APPROVAL READINESS

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V6-01 | approval.status = DRAFT | [ ] Pass [ ] **FAIL** | |
| V6-02 | [FILL] placeholder có mô tả rõ cần điền gì | [ ] Pass [ ] Warn | Số lượng [FILL]: ___ |
| V6-03 | [OWNER_CONFIRM] có mô tả cụ thể | [ ] Pass [ ] Warn | Số lượng: ___ |
| V6-04 | CTA rõ ràng và phù hợp objective | [ ] Pass [ ] Warn | |
| V6-05 | metadata.assumptions[] đầy đủ | [ ] Yes [ ] Missing | |
| V6-06 | Có ≥2 phiên bản caption option | [ ] Yes [ ] Only 1 | |

**Owner Readiness tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## PHẦN 7 — [FILL] / [OWNER_CONFIRM] HANDLING

| Mã | Tiêu chí | Kết quả | Ghi chú |
|----|---------|---------|---------|
| V7-01 | Địa chỉ thiếu → dùng template đúng | [ ] Pass [ ] **FAIL** | |
| V7-02 | SĐT thiếu → dùng [FILL: số điện thoại] | [ ] Pass [ ] **FAIL** | |
| V7-03 | Handle chưa xác nhận → dùng mô tả thay @handle | [ ] Pass [ ] Warn | |
| V7-04 | Mọi [FILL] có prefix mô tả rõ | [ ] Pass [ ] Warn | |
| V7-05 | Đã đếm và ghi tổng số [FILL] vào missing_fields | [ ] Done [ ] Skipped | Tổng: ___ |
| V7-06 | [FILL] quan trọng → status = NEEDS_OWNER_REVIEW | [ ] Applied [ ] Skipped | |

**[FILL] Handling tổng:** [ ] PASS [ ] WARN [ ] FAIL

---

## BẢNG TỔNG KẾT

```
═══════════════════════════════════════════════════════════
VALIDATION CHECKLIST — KẾT QUẢ CUỐI
═══════════════════════════════════════════════════════════

Content Pack ID:  ___________________________
Validated by:     ___________________________
Date:             ___________________________

P1 Brand Fit:     [ ] PASS  [ ] WARN  [ ] FAIL
P2 Product Fit:   [ ] PASS  [ ] WARN  [ ] FAIL
P3 Platform Fit:  [ ] PASS  [ ] WARN  [ ] FAIL
P4 Offer:         [ ] PASS  [ ] WARN  [ ] FAIL  [ ] N/A
P5 Safety:        [ ] PASS  [ ] WARN  [ ] FAIL
P6 Approval:      [ ] PASS  [ ] WARN  [ ] FAIL
P7 [FILL]:        [ ] PASS  [ ] WARN  [ ] FAIL

BLOCKER count: ___  WARNING count: ___  NOTE count: ___

FINAL VALIDATION STATUS:
  [ ] READY_FOR_REVIEW    — 0 BLOCKER, không còn [FILL] quan trọng
  [ ] NEEDS_OWNER_REVIEW  — 0 BLOCKER, còn [FILL] cần Owner điền
  [ ] REVISION_REQUESTED  — Brand/Content fit yếu, Builder chỉnh
  [ ] BLOCKED             — Có ≥1 BLOCKER, dừng ngay

NEXT ACTION:
_______________________________________________________________

VALIDATOR NOTES:
_______________________________________________________________
═══════════════════════════════════════════════════════════
```

---

## Danh Sách [FILL] Cần Owner Điền (Phase hiện tại)

*Danh sách này áp dụng cho toàn bộ queue — cập nhật khi Owner điền thêm*

| Field | Nơi khai báo | Trạng thái |
|-------|-------------|-----------|
| Địa chỉ chi tiết | brand_brain.md | [ ] Chưa điền |
| Số điện thoại | brand_brain.md | [ ] Chưa điền |
| Giờ mở cửa | brand_brain.md | [ ] Chưa điền |
| Facebook handle | brand_brain.md | [ ] Chưa điền |
| TikTok handle | brand_brain.md | [ ] Chưa điền |
| Zalo OA handle | brand_brain.md | [ ] Chưa điền |
| Giá Combo Trưa OF-01 | offer_engine.md | [ ] Chưa điền |
| Giá Combo Cuối Tuần OF-02 | offer_engine.md | [ ] Chưa điền |
| Giá Combo Gia Đình OF-03 | offer_engine.md | [ ] Chưa điền |
| OF-01 status | offer_engine.md | [ ] Chưa điền |
| OF-07 status | offer_engine.md | [ ] Chưa điền |
| Logo file | brand_brain.md | [ ] Chưa điền |
| Tagline chính thức | brand_brain.md | [ ] Chưa xác nhận |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.5 — File tạo mới. Checklist 7 phần với Quick Scan 5 phút, chi tiết từng nhóm, bảng tổng kết, danh sách [FILL] hiện tại cần Owner điền. | Claude Code (Builder) |
