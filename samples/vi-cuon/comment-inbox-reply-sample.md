# Comment Inbox Reply Samples — Vị Cuốn

**Phase:** 5 — Sample Outputs
**Agent:** Comment Inbox Agent (AGT-Inbox)
**Schema:** `schemas/comment-inbox-reply.schema.json`
**Template:** `templates/comment-inbox-reply-template.md`
**SOP:** `module-sops/comment-inbox-assistant-sop.md`
**Brand Brain:** `brand-brain/vi-cuon.md`

> **WARNING:** `human_review_required: true` on all reply drafts. No reply may be posted or sent without Owner review and `approval_status: Approved`. Escalation cases must be handled by Owner directly.

---

## Reply 1 — Menu Question

### reply_id
IR-VQ-20260528-001

### brand_id
VQ

### brand_name
Vị Cuốn

### channel
Facebook Comment

### customer_message
"Quán mình bán những món gì vậy ạ?"

### detected_intent
Menu Inquiry

### sentiment
Neutral

### draft_reply
Chào bạn! 😊 Vị Cuốn bán các món sau nha:

🥢 Bánh Tráng Cuốn Thịt Heo — thịt heo luộc / heo quay, rau sống, bánh tráng mỏng, mắm nêm tự pha
🍜 Bún Trộn Mắm Nêm — bún tươi, thịt heo / heo quay, đậu phộng rang, mắm nêm
🌿 Gỏi Cuốn — tôm thịt hoặc chay, chấm tương
🍖 Heo Quay Nướng Lu — thêm theo đơn

Giá tham khảo từ khoảng [OWNER_TO_PROVIDE_PRICE]/người ạ.

Bạn muốn xem menu đầy đủ không? Mình inbox link nhé! 📋

### escalation_required
false

### escalation_reason
null

### human_review_required
true

### approval_status
Draft

### created_by_agent
Comment Inbox Agent (AGT-Inbox)

### created_at
[AUTO_GENERATED — 2026-05-28T13:00:00+07:00]

### notes
Price field uses [OWNER_TO_PROVIDE_PRICE] — Owner to fill before approving. Menu link placeholder — Owner to insert Facebook album or menu link. Standard menu inquiry, no escalation needed.

---

## Reply 2 — Price Question

### reply_id
IR-VQ-20260528-002

### brand_id
VQ

### brand_name
Vị Cuốn

### channel
Facebook Messenger

### customer_message
"Cho mình hỏi giá một phần bánh tráng cuốn thịt heo là bao nhiêu vậy ạ?"

### detected_intent
Price Inquiry

### sentiment
Neutral

### draft_reply
Chào bạn! 😊 Một phần Bánh Tráng Cuốn Thịt Heo bên mình giá [OWNER_TO_PROVIDE_PRICE] ạ.

Nếu bạn muốn ăn no đủ bữa, mình có combo [OWNER_TO_PROVIDE_OFFER] — ngon và tiết kiệm hơn nha!

Bạn muốn đặt không? Nhắn lại cho mình số lượng và địa chỉ giao nhé 🙌

### escalation_required
false

### escalation_reason
null

### human_review_required
true

### approval_status
Draft

### created_by_agent
Comment Inbox Agent (AGT-Inbox)

### created_at
[AUTO_GENERATED — 2026-05-28T13:10:00+07:00]

### notes
Both [OWNER_TO_PROVIDE_PRICE] and [OWNER_TO_PROVIDE_OFFER] must be filled by Owner before this reply is approved. Do not guess or estimate prices in the reply.

---

## Reply 3 — Address / Location Question

### reply_id
IR-VQ-20260528-003

### brand_id
VQ

### brand_name
Vị Cuốn

### channel
Facebook Comment

### customer_message
"Quán ở đâu vậy bạn? Địa chỉ cụ thể?"

### detected_intent
Location Inquiry

### sentiment
Neutral

### draft_reply
Chào bạn! Vị Cuốn ở địa chỉ: [OWNER_TO_PROVIDE_ADDRESS] nhé 😊

Giờ mở cửa: [OWNER_TO_PROVIDE_OPENING_HOURS]

Bạn có thể tìm trên Google Maps bằng tên "Vị Cuốn" hoặc nhắn inbox để mình gửi link định vị nha! 📍

### escalation_required
false

### escalation_reason
null

### human_review_required
true

### approval_status
Draft

### created_by_agent
Comment Inbox Agent (AGT-Inbox)

### created_at
[AUTO_GENERATED — 2026-05-28T13:20:00+07:00]

### notes
[OWNER_TO_PROVIDE_ADDRESS] and [OWNER_TO_PROVIDE_OPENING_HOURS] must be filled by Owner. Google Maps link or pin reference — Owner to add when available. Standard location inquiry, no escalation.

---

## Reply 4 — Booking / Group Question

### reply_id
IR-VQ-20260528-004

### brand_id
VQ

### brand_name
Vị Cuốn

### channel
Facebook Messenger

### customer_message
"Mình muốn đặt bàn cho nhóm 8 người vào thứ 7 tuần này được không ạ? Quán có nhận đặt trước không?"

### detected_intent
Order Inquiry

### sentiment
Positive

### draft_reply
Chào bạn! Dạ được ạ, Vị Cuốn nhận đặt trước cho nhóm 😊

Bạn cho mình biết:
- Ngày và giờ muốn đến (thứ 7 này — giờ nào ạ?)
- Số người (8 người — mình ghi nhận rồi)
- Có yêu cầu đặc biệt gì không (ví dụ: có trẻ em, cần chỗ ngồi ngoài trời, v.v.)?

Mình xác nhận lại cho bạn ngay sau khi kiểm tra lịch nhé! 🙌

[OWNER_TO_PROVIDE — nếu quán có quy trình đặt cọc hoặc yêu cầu riêng cho nhóm lớn, Owner bổ sung vào đây]

### escalation_required
false

### escalation_reason
null

### human_review_required
true

### approval_status
Draft

### created_by_agent
Comment Inbox Agent (AGT-Inbox)

### created_at
[AUTO_GENERATED — 2026-05-28T13:30:00+07:00]

### notes
Group booking inquiry — reply collects necessary details before confirming. Owner to add deposit or group policy note if applicable. No commitment to availability made in draft — availability must be confirmed by Owner before final reply is sent.

---

## Reply 5 — Delivery Question

### reply_id
IR-VQ-20260528-005

### brand_id
VQ

### brand_name
Vị Cuốn

### channel
Facebook Comment

### customer_message
"Quán có giao hàng không ạ? Giao đến khu vực nào?"

### detected_intent
Order Inquiry

### sentiment
Neutral

### draft_reply
Chào bạn! 😊 Vị Cuốn có giao hàng nhé!

🛵 Đặt qua: [OWNER_TO_PROVIDE — tên app: ShopeeFood / GrabFood / Baemin / giao nội bộ]
📍 Khu vực giao: [OWNER_TO_PROVIDE_DELIVERY_AREA]

Hoặc bạn có thể nhắn inbox trực tiếp để mình hỗ trợ đặt hàng nha!

### escalation_required
false

### escalation_reason
null

### human_review_required
true

### approval_status
Draft

### created_by_agent
Comment Inbox Agent (AGT-Inbox)

### created_at
[AUTO_GENERATED — 2026-05-28T13:40:00+07:00]

### notes
Two critical placeholders: (1) delivery app names must be confirmed by Owner — do not assume ShopeeFood/GrabFood without confirmation; (2) delivery area must be confirmed by Owner. Both must be filled before this reply is approved.
