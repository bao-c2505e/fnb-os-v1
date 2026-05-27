# Revision Rules — Vị Cuốn Content Pack

*Phase 1.5 — Content Pack Validation & Sample Queue*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Quy tắc xử lý sau Validation — quyết định trạng thái và hành động tiếp theo*

---

## Tổng quan

Revision Rules xác định rõ: khi một Content Pack có vấn đề cụ thể, trạng thái được set là gì và ai cần làm gì tiếp theo.

**Nguyên tắc tổng quát:**
- BLOCKER → BLOCKED (dừng hoàn toàn, không vào pipeline)
- [FILL] quan trọng còn tồn tại → NEEDS_OWNER_REVIEW (Owner điền xong mới tiếp tục)
- Brand fit yếu / content không đúng hướng → REVISION_REQUESTED (Builder chỉnh)
- Tất cả PASS, không còn [FILL] quan trọng → READY_FOR_REVIEW (vào pipeline)

---

## RULE SET 1 — Điều kiện dẫn đến NEEDS_OWNER_REVIEW

Content Pack được set `validation_status = NEEDS_OWNER_REVIEW` khi có BẤT KỲ một trong các điều kiện sau:

### R1-01: Thiếu Giá (Missing Price)

**Điều kiện:** Caption đề cập đến combo hoặc offer nhưng giá vẫn là `[FILL: ~XXđ]` và chưa được Owner xác nhận.

**Hành động:**
- Set `validation_status = NEEDS_OWNER_REVIEW`
- Ghi vào `missing_fields`: `["price_combo_trua", "price_confirmed"]`
- Ghi `next_action`: "Owner điền giá vào `menu_brain.md` và `offer_engine.md`, sau đó Builder cập nhật Content Pack"

**Mã flag:** `PRICE_UNCONFIRMED`

---

### R1-02: Thiếu Địa Chỉ (Missing Address)

**Điều kiện:** Caption có CTA "ghé quán" hoặc "đặt hàng trực tiếp" nhưng địa chỉ vẫn là `[FILL: địa chỉ chi tiết]`.

**Hành động:**
- Set `validation_status = NEEDS_OWNER_REVIEW`
- Ghi vào `missing_fields`: `["address_detail"]`
- Ghi `next_action`: "Owner cập nhật địa chỉ vào `brand_brain.md`, Builder cập nhật caption CTA"

**Mã flag:** `ADDRESS_UNFILLED`

---

### R1-03: Thiếu Số Điện Thoại (Missing Phone)

**Điều kiện:** Caption có CTA "gọi ngay" hoặc "inbox/gọi [số]" nhưng SĐT vẫn là `[FILL: SĐT]`.

**Hành động:**
- Set `validation_status = NEEDS_OWNER_REVIEW`
- Ghi vào `missing_fields`: `["phone_number"]`
- Ghi `next_action`: "Owner xác nhận SĐT trong `brand_brain.md`, Builder cập nhật CTA"

**Mã flag:** `ADDRESS_UNFILLED` (dùng chung)

---

### R1-04: Offer Status Chưa Xác Nhận (Unconfirmed Offer Status)

**Điều kiện:** Content Pack dùng offer (OF-01 đến OF-09) nhưng `trạng thái` trong `offer_engine.md` vẫn là `[FILL: ACTIVE / INACTIVE]`.

**Hành động:**
- Set `validation_status = NEEDS_OWNER_REVIEW`
- Ghi vào `missing_fields`: `["offer_status_[OF-ID]"]`
- Ghi `next_action`: "Owner xác nhận trạng thái offer trong `offer_engine.md` — set ACTIVE hoặc INACTIVE"

**Mã flag:** `OFFER_UNCONFIRMED`

---

### R1-05: Real Promo Chưa Xác Nhận (Unconfirmed Real Promotion)

**Điều kiện:** Content Pack đề cập đến chương trình khuyến mãi cụ thể (giảm %, tặng thêm món) nhưng Owner chưa xác nhận chương trình đó tồn tại.

**Hành động:**
- Set `validation_status = NEEDS_OWNER_REVIEW`
- Ghi `[OWNER_CONFIRM: xác nhận chương trình KM này có thật không?]` vào caption
- Ghi `next_action`: "Owner xác nhận KM trước khi Builder hoàn thiện caption"

**Mã flag:** `OFFER_UNCONFIRMED`

---

## RULE SET 2 — Điều kiện dẫn đến BLOCKED

Content Pack được set `validation_status = BLOCKED` và **DỪNG NGAY** khi có BẤT KỲ một trong các điều kiện sau:

### R2-01: Review / Đánh Giá Giả (Fake Review)

**Điều kiện:** Caption sử dụng review giả, trích dẫn khách hàng không có thật, hoặc đề xuất seeding review giả mạo.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["FAKE_REVIEW"]`
- Ghi `next_action`: "BLOCKER — Xóa toàn bộ phần review giả. Chỉ dùng review thật với sự đồng ý của khách."
- **Không cho vào pipeline dưới bất kỳ hình thức nào**

---

### R2-02: Discount Giả / Không Có Thật (Fake Discount)

**Điều kiện:** Caption tuyên bố mức giảm giá (VD: "Giảm 50%!") không có trong `offer_engine.md` hoặc không có xác nhận từ Owner.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["UNAUTHORIZED_PRICE", "FAKE_URGENCY"]`
- Ghi `next_action`: "BLOCKER — Xóa claim giảm giá. Chỉ dùng offer có trong offer_engine.md."

---

### R2-03: Claim Sức Khỏe Không Có Căn Cứ (Unsubstantiated Health Claim)

**Điều kiện:** Caption chứa các từ: "tốt cho sức khỏe", "giảm cân", "detox", "thanh lọc cơ thể", "kháng khuẩn", hoặc bất kỳ tuyên bố y tế nào.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["HEALTH_CLAIM"]`
- Ghi `next_action`: "BLOCKER — Xóa claim sức khỏe. Thay bằng mô tả giác quan (tươi ngon, giòn, thơm)."

---

### R2-04: Nhắc Tên Đối Thủ (Competitor Mention)

**Điều kiện:** Caption nhắc tên quán/thương hiệu đối thủ — dù để so sánh tích cực, trung lập, hay tiêu cực.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["COMPETITOR_MENTION"]`
- Ghi `next_action`: "BLOCKER — Xóa tên đối thủ. Tập trung vào USP của Vị Cuốn."

---

### R2-05: Lệnh Tự Động / Kết Nối API (Auto-Trigger / API Connection)

**Điều kiện:** Content Pack chứa bất kỳ lệnh nào gọi API đăng bài, gửi tin nhắn tự động, hoặc kết nối hệ thống thật.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["AUTO_POST_TRIGGER"]`
- Ghi `next_action`: "BLOCKER nghiêm trọng — Xóa ngay lệnh tự động. Phase 1.5 chưa kết nối production."

---

### R2-06: Thông Tin Secret Bị Lộ (Exposed Secret)

**Điều kiện:** Output chứa API key, token, password, secret thật của bất kỳ dịch vụ nào.

**Hành động:**
- Set `validation_status = BLOCKED`
- Set `safety_flags = ["SECRET_EXPOSED"]`
- Ghi `next_action`: "BLOCKER NGHIÊM TRỌNG — Xóa secret ngay. Rotate credentials nếu đã bị lộ. Báo Owner."

---

## RULE SET 3 — Điều kiện dẫn đến REVISION_REQUESTED

Content Pack được set `validation_status = REVISION_REQUESTED` khi:

### R3-01: Brand Fit Yếu (Weak Brand Fit)

**Điều kiện:** Caption tồn tại nhưng giọng văn không đúng tone (quá lạnh lùng, quá bán hàng kiểu cứng, không ấm áp).

**Hành động:**
- Set `validation_status = REVISION_REQUESTED`
- Ghi `next_action`: "Builder chỉnh lại giọng văn theo Brand Voice: ấm áp, gần gũi, thân thiện như người quen"

---

### R3-02: Pillar / Angle Không Khớp (Pillar / Angle Mismatch)

**Điều kiện:** Caption được gán pillar PROMO nhưng không có offer rõ ràng; hoặc gán BTS nhưng không có element hậu trường.

**Hành động:**
- Set `validation_status = REVISION_REQUESTED`
- Ghi `next_action`: "Builder chỉnh lại nội dung cho đúng pillar đã chọn, hoặc đổi pillar cho phù hợp"

---

### R3-03: Thiếu CTA (Missing Call-to-Action)

**Điều kiện:** Caption hoàn toàn không có CTA rõ ràng (không có "ghé quán", "đặt ngay", "inbox", "gọi ngay", "comment").

**Hành động:**
- Set `validation_status = REVISION_REQUESTED`
- Ghi `next_action`: "Builder thêm CTA phù hợp với objective của Content Pack"

---

### R3-04: Caption Quá Dài / Quá Ngắn

**Điều kiện:** Caption vượt ngưỡng platform (Facebook >800 ký tự thực tế, TikTok >200 ký tự) hoặc quá ngắn (<50 ký tự).

**Hành động:**
- Set `validation_status = REVISION_REQUESTED`
- Ghi `next_action`: "Builder rút ngắn/dài thêm caption cho đúng ngưỡng platform"

---

## RULE SET 4 — Điều kiện dẫn đến READY_FOR_REVIEW

Content Pack được set `validation_status = READY_FOR_REVIEW` khi ĐẦY ĐỦ các điều kiện sau:

| Điều kiện | Trạng thái |
|-----------|-----------|
| Không có bất kỳ BLOCKER nào trong V1–V7 | [ ] ✓ |
| Không còn [FILL] quan trọng (giá, địa chỉ, SĐT, offer status) | [ ] ✓ |
| Giọng văn đúng Brand Voice | [ ] ✓ |
| Pillar và angle khớp với nội dung | [ ] ✓ |
| CTA rõ ràng và phù hợp | [ ] ✓ |
| Platform fit đạt | [ ] ✓ |
| `approval.status = DRAFT` (chưa tự approve) | [ ] ✓ |

**Khi đạt READY_FOR_REVIEW:**
→ Chuyển Content Pack vào `03_APPROVAL_PIPELINE/` để Owner review
→ Ghi `next_action`: "Gửi Telegram summary cho Owner theo template `telegram_approval_message_template.md`"

---

## Quy Trình Revision Loop

```
[Content Pack DRAFT]
       ↓
[Validation — 7 nhóm]
       ↓
    ┌──────────────────────────────────────────┐
    │ Kết quả?                                 │
    ├──────────────────────────────────────────┤
    │ BLOCKED        → Dừng. Báo Owner. Fix.   │
    │ NEEDS_REVIEW   → Owner điền [FILL]. Redo.│
    │ REVISION       → Builder chỉnh. Redo.    │
    │ READY          → Vào Approval Pipeline.  │
    └──────────────────────────────────────────┘
       ↓ (nếu READY)
[Owner Review — Approval Pipeline]
       ↓
[APPROVED → Lên lịch đăng / REJECTED → Builder chỉnh lại]
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.5 — File tạo mới. 4 rule sets: NEEDS_OWNER_REVIEW (R1), BLOCKED (R2), REVISION_REQUESTED (R3), READY_FOR_REVIEW (R4). 14 rules cụ thể cho Vị Cuốn. | Claude Code (Builder) |
