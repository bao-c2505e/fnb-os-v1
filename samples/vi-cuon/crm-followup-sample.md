# CRM Follow-Up Samples — Vị Cuốn

**Phase:** 5 — Sample Outputs
**Agent:** CRM Follow-Up Agent (AGT-CRM)
**Schema:** `schemas/crm-followup.schema.json`
**Template:** `templates/crm-followup-template.md`
**SOP:** `module-sops/crm-followup-auto-sop.md`
**Brand Brain:** `brand-brain/vi-cuon.md`

> **WARNING:** `human_review_required: true` on all sequences. No message may be sent to any real customer without Owner review and `approval_status: Approved`.

---

## Sample 1 — New Lead Inquiry (Menu / Price Question)

### sequence_id
CRM-VQ-20260528-001

### brand_id
VQ

### brand_name
Vị Cuốn

### lead_segment
New Customer

### customer_status
New Lead

### channel
Facebook Messenger

### trigger_event
Customer sends first inbox message asking about menu or pricing

### message_sequence

**Step 1**
- **step:** 1
- **delay:** Immediately (within 5–15 minutes of trigger)
- **message_template:**
> Chào [CUSTOMER_NAME]! 😊 Cảm ơn bạn đã nhắn tin cho Vị Cuốn nhé!
>
> Bên mình có các món chính:
> 🥢 Bánh Tráng Cuốn Thịt Heo — thịt heo luộc, rau sống, bánh tráng mỏng, mắm nêm tự pha
> 🍜 Bún Trộn Mắm Nêm — bún tươi, thịt heo / heo quay, đậu phộng rang
> 🌿 Gỏi Cuốn Tôm Thịt / Chay — cuốn tươi, chấm tương hoisin
>
> Giá từ khoảng [OWNER_TO_PROVIDE_PRICE] — combo đủ bữa [OWNER_TO_PROVIDE_OFFER].
>
> Bạn muốn xem menu đầy đủ không? Mình gửi link nhé! 📋

**Step 2**
- **step:** 2
- **delay:** 1 ngày sau Step 1 (nếu không có phản hồi)
- **message_template:**
> Chào [CUSTOMER_NAME]! Hôm nay bạn có muốn ghé Vị Cuốn không ạ? 😄
>
> Nếu bạn đặt hàng, nhắn lại cho mình biết số lượng và địa chỉ giao (nếu có) nhé!
>
> Địa chỉ quán: [OWNER_TO_PROVIDE_ADDRESS]
> Giờ mở cửa: [OWNER_TO_PROVIDE_OPENING_HOURS]

**Step 3**
- **step:** 3
- **delay:** 3 ngày sau Step 2 (nếu vẫn không có phản hồi — kết thúc sequence)
- **message_template:**
> Chào [CUSTOMER_NAME]! Vị Cuốn không muốn làm phiền bạn 😊 — đây là tin nhắn cuối mình gửi nhé.
>
> Khi nào bạn muốn thử, cứ nhắn lại là mình phục vụ ngay!
>
> Hẹn gặp bạn ở Vị Cuốn 🙌

### recommended_timing
Weekdays: 10:30–12:00 và 17:00–18:30 (Vietnam time, GMT+7). Tránh gửi sau 21:00 hoặc trước 08:00.

### human_review_required
true

### approval_status
Draft

### created_by_agent
CRM Follow-Up Agent (AGT-CRM)

### created_at
[AUTO_GENERATED — 2026-05-28T12:00:00+07:00]

### notes
Giá và offer dùng placeholder — Owner phải xác nhận [OWNER_TO_PROVIDE_PRICE] và [OWNER_TO_PROVIDE_OFFER] trước khi gửi. Địa chỉ và giờ mở cửa cũng là placeholder. Sequence kết thúc sau Step 3 nếu không có phản hồi — không gửi tiếp để tránh spam. Tất cả khách trong sequence này đã opt-in khi tự nhắn tin trước.

---

## Sample 2 — Lapsed Customer Reactivation (30+ Ngày Không Đặt)

### sequence_id
CRM-VQ-20260528-002

### brand_id
VQ

### brand_name
Vị Cuốn

### lead_segment
Lapsed Customer

### customer_status
At Risk

### channel
Zalo

### trigger_event
Customer has not placed an order or interacted for 30+ days

### message_sequence

**Step 1**
- **step:** 1
- **delay:** Immediately upon trigger (30-day inactivity flag)
- **message_template:**
> Chào [CUSTOMER_NAME]! Lâu rồi không thấy bạn ghé Vị Cuốn — nhớ bạn quá 😊
>
> Không biết gần đây bạn có bận không? Bếp vẫn mở cửa, vẫn tươi mỗi ngày như thường 🥢
>
> Bạn có muốn ghé lại không? [OWNER_TO_PROVIDE_OFFER]
>
> Địa chỉ: [OWNER_TO_PROVIDE_ADDRESS]
> Giờ mở cửa: [OWNER_TO_PROVIDE_OPENING_HOURS]

**Step 2**
- **step:** 2
- **delay:** 5 ngày sau Step 1 (nếu không có phản hồi — kết thúc sequence)
- **message_template:**
> Chào [CUSTOMER_NAME]! Đây là tin nhắn cuối Vị Cuốn gửi bạn 😄
>
> Khi nào bạn muốn ghé lại — cứ nhắn tin bất cứ lúc nào, mình luôn sẵn sàng!
>
> Hẹn gặp bạn sớm nhé 🙏

### recommended_timing
Weekdays: 11:00–12:00 hoặc 17:30–19:00 (Vietnam time, GMT+7). Không gửi thứ 2 đầu tuần — hiệu quả thấp hơn. Tốt nhất thứ 3, thứ 4, hoặc thứ 6.

### human_review_required
true

### approval_status
Draft

### created_by_agent
CRM Follow-Up Agent (AGT-CRM)

### created_at
[AUTO_GENERATED — 2026-05-28T12:15:00+07:00]

### notes
Offer field là placeholder — Owner xác nhận offer win-back nếu có, hoặc giữ nguyên không có offer. Sequence chỉ 2 bước để không spam khách lapsed. Khách opt-in Zalo đã có từ lịch sử đặt hàng trước — Owner xác nhận danh sách khách đủ điều kiện trước khi chạy. Nếu khách reply và yêu cầu hủy đăng ký — dừng toàn bộ sequence và ghi nhận.
