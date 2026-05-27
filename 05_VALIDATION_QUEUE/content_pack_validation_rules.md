# Content Pack Validation Rules — Vị Cuốn

*Phase 1.5 — Content Pack Validation & Sample Queue*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Áp dụng cho mọi Content Pack trước khi vào Approval Pipeline*

---

## Tổng quan

Validation Rules là bộ tiêu chí kiểm tra bắt buộc mỗi Content Pack phải vượt qua **trước khi** chuyển sang `03_APPROVAL_PIPELINE/`. Mỗi Content Pack phải được đánh giá qua 7 nhóm tiêu chí dưới đây.

**Kết quả có thể:**

| Kết quả | Ý nghĩa | Hành động tiếp theo |
|---------|---------|---------------------|
| `READY_FOR_REVIEW` | Vượt qua tất cả nhóm, không có BLOCKER | Chuyển sang Approval Pipeline |
| `NEEDS_OWNER_REVIEW` | Có [FILL] hoặc [OWNER_CONFIRM] chưa điền | Owner điền xong → Re-validate |
| `REVISION_REQUESTED` | Có lỗi brand fit hoặc content fit yếu | Builder chỉnh sửa → Re-validate |
| `BLOCKED` | Có vi phạm nghiêm trọng | Dừng, báo cáo ngay |

---

## NHÓM V1 — BRAND FIT (Phù hợp Thương Hiệu)

*Nguồn kiểm tra: `01_BRAIN/brand_brain.md`, `02_CONTENT_ENGINE/content_pillars.md`*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V1-01 | **BLOCKER** | Caption KHÔNG nhắc tên đối thủ cạnh tranh (dù là so sánh tích cực) | [ ] Pass / [ ] Fail |
| V1-02 | **BLOCKER** | Caption KHÔNG có claim sức khỏe không có căn cứ ("giảm cân", "detox", "thanh lọc cơ thể", "tốt cho sức khỏe") | [ ] Pass / [ ] Fail |
| V1-03 | **BLOCKER** | Giọng văn KHÔNG trang trọng xa cách ("Quý khách kính mến", "Kính thưa") | [ ] Pass / [ ] Warn |
| V1-04 | **WARNING** | Caption dùng đúng giọng điệu Brand Voice (ấm áp, gần gũi, không áp lực) | [ ] Pass / [ ] Warn |
| V1-05 | **WARNING** | Emoji tối đa 2–3 cái trong toàn caption — không dày đặc mỗi dòng | [ ] Pass / [ ] Warn |
| V1-06 | **WARNING** | Caption KHÔNG viết hoa toàn câu để nhấn mạnh | [ ] Pass / [ ] Warn |
| V1-07 | **NOTE** | Hashtag cốt lõi có mặt: #VịCuốn và #ĂnVinh | [ ] Yes / [ ] Missing |
| V1-08 | **NOTE** | Nội dung phù hợp với pillar đã chọn (PROD / BTS / PROMO / STORY / COM / SEASON) | [ ] Yes / [ ] Mismatch |

**Kết quả nhóm V1:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V2 — MENU / PRODUCT FIT (Phù hợp Thực Đơn & Sản Phẩm)

*Nguồn kiểm tra: `01_BRAIN/menu_brain.md`*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V2-01 | **BLOCKER** | Mọi món đề cập trong caption PHẢI có trong `menu_brain.md` — không nhắc món không tồn tại | [ ] Pass / [ ] Fail |
| V2-02 | **BLOCKER** | Giá tiền (nếu có) PHẢI đến từ `menu_brain.md` hoặc `offer_engine.md` — không tự đặt giá | [ ] Pass / [ ] Fail |
| V2-03 | **WARNING** | Nếu giá chưa xác nhận → dùng `[FILL: ~XXđ]` thay vì bỏ trống hoàn toàn | [ ] Pass / [ ] Warn |
| V2-04 | **WARNING** | Mô tả món ăn chính xác với thực tế sản phẩm (không phóng đại, không thiếu thành phần) | [ ] Pass / [ ] Warn |
| V2-05 | **NOTE** | Caption có mô tả giác quan (màu sắc, mùi thơm, kết cấu) phù hợp với sản phẩm thật | [ ] Yes / [ ] Missing |

**Kết quả nhóm V2:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V3 — PLATFORM FIT (Phù hợp Nền Tảng)

*Nguồn kiểm tra: `02_CONTENT_ENGINE/content_pillars.md` — Platform Mapping*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V3-01 | **BLOCKER** | `platform` hợp lệ: Facebook / TikTok / Instagram / Zalo OA / ShopeeFood / GrabFood | [ ] Pass / [ ] Fail |
| V3-02 | **WARNING** | `content_type` phù hợp với `platform` theo Platform Compatibility Matrix | [ ] Pass / [ ] Warn |
| V3-03 | **WARNING** | Độ dài caption trong ngưỡng khuyến nghị của platform (Facebook ≤500 ký tự, TikTok ≤150 ký tự) | [ ] Pass / [ ] Warn |
| V3-04 | **WARNING** | Số lượng hashtag đúng theo platform: Facebook 3–5, TikTok 5–10, Instagram 5–15, Zalo 0 | [ ] Pass / [ ] Warn |
| V3-05 | **NOTE** | Thời điểm đăng đề xuất phù hợp với pillar và platform | [ ] Yes / [ ] Missing |

**Platform Compatibility Matrix nhanh:**

| Platform | Content type phù hợp | Không phù hợp |
|----------|---------------------|--------------|
| Facebook | Photo, Carousel, Reel, Story | Long-form video >5 phút |
| TikTok | Short Video 15–60s, TikTok Reel | Carousel ảnh đơn thuần |
| Instagram | Photo, Carousel, Reel, Story | Text-only |
| Zalo OA | Text + ảnh (broadcast) | Video nặng |

**Kết quả nhóm V3:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V4 — OFFER VALIDITY (Tính Hợp Lệ của Ưu Đãi)

*Nguồn kiểm tra: `02_CONTENT_ENGINE/offer_engine.md`*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V4-01 | **BLOCKER** | Mọi offer đề cập phải là offer có trong `offer_engine.md` (OF-01 đến OF-09) | [ ] Pass / [ ] Fail |
| V4-02 | **BLOCKER** | Voucher code (nếu có) phải đã đăng ký trong Voucher System — không dùng code chưa đăng ký | [ ] Pass / [ ] Fail |
| V4-03 | **BLOCKER** | KHÔNG tạo áp lực giả ("Chỉ còn 2 suất!", "Sắp hết!") khi không có xác nhận từ Owner | [ ] Pass / [ ] Fail |
| V4-04 | **WARNING** | Nếu offer status là `[FILL]` → đánh dấu `[OWNER_CONFIRM: offer status]` | [ ] Pass / [ ] Warn |
| V4-05 | **WARNING** | Điều kiện offer (thời gian, kênh, đơn tối thiểu) được trình bày rõ ràng trong caption | [ ] Pass / [ ] Warn |
| V4-06 | **NOTE** | Offer phù hợp với target segment của pillar và persona đã chọn | [ ] Yes / [ ] Mismatch |

**Kết quả nhóm V4:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V5 — SAFETY & COMPLIANCE (An Toàn & Tuân Thủ)

*Nguồn: `04_CONTENT_PACK_GENERATOR/safety_self_check.md`, `01_BRAIN/brand_brain.md` AI Safety Rules*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V5-01 | **BLOCKER** | Output KHÔNG chứa API key, token, password, secret thật | [ ] Pass / [ ] Fail |
| V5-02 | **BLOCKER** | Output KHÔNG chứa thông tin cá nhân thật của khách hàng (tên, SĐT riêng, địa chỉ nhà) | [ ] Pass / [ ] Fail |
| V5-03 | **BLOCKER** | Không có lệnh tự động đăng bài, gửi tin nhắn, hoặc gọi API nào trong output | [ ] Pass / [ ] Fail |
| V5-04 | **BLOCKER** | Không có review/đánh giá giả mạo, follower giả, engagement giả được đề xuất | [ ] Pass / [ ] Fail |
| V5-05 | **BLOCKER** | Không có discount giả không có thật (ví dụ: "Giảm 50%!" khi offer engine không có) | [ ] Pass / [ ] Fail |
| V5-06 | **WARNING** | Không sử dụng ảnh stock hoặc ảnh không phải của quán trong brief hình ảnh | [ ] Pass / [ ] Warn |
| V5-07 | **NOTE** | Nội dung không vi phạm chính sách quảng cáo của Facebook/TikTok/Instagram | [ ] Yes / [ ] Risk |

**Kết quả nhóm V5:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V6 — OWNER APPROVAL READINESS (Sẵn Sàng Để Owner Duyệt)

*Kiểm tra xem Content Pack có đủ thông tin để Owner review và quyết định không*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V6-01 | **BLOCKER** | `approval.status` = `DRAFT` — chưa tự chuyển sang APPROVED | [ ] Pass / [ ] Fail |
| V6-02 | **WARNING** | Mọi `[FILL]` placeholder đã được ghi chú rõ Owner cần điền gì | [ ] Pass / [ ] Warn |
| V6-03 | **WARNING** | Mọi `[OWNER_CONFIRM]` placeholder có mô tả cụ thể cần confirm | [ ] Pass / [ ] Warn |
| V6-04 | **WARNING** | CTA (call-to-action) rõ ràng và phù hợp với objective | [ ] Pass / [ ] Warn |
| V6-05 | **NOTE** | `metadata.assumptions[]` có ghi đầy đủ giả định đã đặt | [ ] Yes / [ ] Missing |
| V6-06 | **NOTE** | Caption options có ít nhất 2 phiên bản để Owner chọn | [ ] Yes / [ ] Only 1 |

**Kết quả nhóm V6:** [ ] PASS [ ] WARN [ ] FAIL

---

## NHÓM V7 — MISSING [FILL] / [OWNER_CONFIRM] HANDLING

*Xử lý đặc biệt cho các placeholder chưa điền — không để trống mà phải ghi rõ*

| Mã | Mức | Tiêu chí | Kết quả |
|----|-----|---------|---------|
| V7-01 | **BLOCKER** | Địa chỉ chi tiết chưa có → dùng "Vị Cuốn — Vinh, Nghệ An" + `[FILL: địa chỉ chi tiết]` — không bỏ hẳn CTA địa chỉ | [ ] Pass / [ ] Fail |
| V7-02 | **BLOCKER** | SĐT chưa có → dùng `[FILL: số điện thoại]` — không bỏ trống CTA gọi điện | [ ] Pass / [ ] Fail |
| V7-03 | **WARNING** | Social handle chưa xác nhận → dùng "trang Vị Cuốn" thay vì "@handle_sai" | [ ] Pass / [ ] Warn |
| V7-04 | **WARNING** | Mọi [FILL] đều có prefix rõ ràng mô tả nội dung cần điền (VD: `[FILL: giá combo trưa]` không chỉ `[FILL]`) | [ ] Pass / [ ] Warn |
| V7-05 | **NOTE** | Đếm tổng số [FILL] và [OWNER_CONFIRM] còn lại — ghi vào `missing_fields` | [ ] Done / [ ] Skipped |
| V7-06 | **NOTE** | Content Pack có [FILL] quan trọng (giá, địa chỉ, SĐT, offer status) → `validation_status = NEEDS_OWNER_REVIEW` | [ ] Applied / [ ] Skipped |

**Kết quả nhóm V7:** [ ] PASS [ ] WARN [ ] FAIL

---

## Bảng Tổng Kết Validation

```
═══════════════════════════════════════════════════════
VALIDATION RESULT SUMMARY
═══════════════════════════════════════════════════════
Content Pack ID:    ____________________
Validated at:       ____________________
Validated by:       ____________________

Nhóm V1 (Brand Fit):         [ ] PASS [ ] WARN [ ] FAIL
Nhóm V2 (Product Fit):       [ ] PASS [ ] WARN [ ] FAIL
Nhóm V3 (Platform Fit):      [ ] PASS [ ] WARN [ ] FAIL
Nhóm V4 (Offer Validity):    [ ] PASS [ ] WARN [ ] FAIL
Nhóm V5 (Safety):            [ ] PASS [ ] WARN [ ] FAIL
Nhóm V6 (Approval Readiness):[ ] PASS [ ] WARN [ ] FAIL
Nhóm V7 ([FILL] Handling):   [ ] PASS [ ] WARN [ ] FAIL

BLOCKER count:  ____
WARNING count:  ____
NOTE count:     ____

FINAL STATUS:
  [ ] READY_FOR_REVIEW   — 0 BLOCKER, tất cả [FILL] quan trọng đã điền
  [ ] NEEDS_OWNER_REVIEW — 0 BLOCKER, còn [FILL]/[OWNER_CONFIRM] cần Owner điền
  [ ] REVISION_REQUESTED — Brand fit yếu hoặc content cần chỉnh, chưa có BLOCKER
  [ ] BLOCKED            — Có ≥1 BLOCKER, dừng ngay

Next action: ____________________
═══════════════════════════════════════════════════════
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.5 — File tạo mới. 7 nhóm validation: Brand Fit, Product Fit, Platform Fit, Offer Validity, Safety/Compliance, Owner Approval Readiness, [FILL] Handling. Tích hợp từ brand_brain.md, offer_engine.md, safety_self_check.md. | Claude Code (Builder) |
