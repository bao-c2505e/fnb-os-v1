# Telegram Approval Message Template — Vị Cuốn

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Template thông báo Telegram gửi cho Owner khi nội dung sẵn sàng để duyệt.*
*n8n dùng template này để format tin nhắn. Owner nhận và phản hồi qua Telegram.*

---

## Tổng quan

Mỗi khi content pack chuyển sang `READY_FOR_REVIEW`, n8n tự động gửi tin nhắn Telegram cho Owner. Tin nhắn phải đủ thông tin để Owner quyết định mà không cần mở Google Sheet hay Google Drive ngay.

**Telegram Bot:** Sử dụng Bot đã cấu hình trong `.env` (`TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID`)
**Format:** Markdown (Telegram Markdown V2)
**Emoji:** Có — để dễ scan nhanh

---

## Template 1: Thông báo Nội dung Chờ Duyệt (READY_FOR_REVIEW)

```
📋 *NỘI DUNG CHỜ DUYỆT*

🆔 *ID:* `{{content_id}}`
📅 *Tạo lúc:* {{created_at}} (GMT+7)
👤 *Tạo bởi:* {{created_by_agent}}

━━━━━━━━━━━━━━━━━━━━
📱 *Nền tảng:* {{platform}} | {{content_type}}
🎯 *Pillar:* {{pillar}} | *Angle:* {{angle_name}}
👥 *Persona:* {{persona_segment}}
━━━━━━━━━━━━━━━━━━━━

📝 *Caption (preview):*
_{{caption_preview_100chars}}..._

{{#if offer_code}}
🎁 *Offer:* {{offer_id}} — {{offer_name}}
   {{offer_summary}}
{{/if}}

{{#if safety_flags}}
⚠️ *Safety Flags:*
{{safety_flags_formatted}}
{{else}}
✅ *Safety Check:* Không có flag
{{/if}}

━━━━━━━━━━━━━━━━━━━━
📁 *Xem đầy đủ:*
• Google Drive: {{drive_folder_url}}
• Google Sheet: {{sheet_row_url}}

⏰ *SLA:* Vui lòng duyệt trong 48 giờ

━━━━━━━━━━━━━━━━━━━━
👇 *HÀNH ĐỘNG CỦA OWNER:*

✅ Gõ: APPROVE {{content_id}}
📝 Gõ: REVISE {{content_id}} [lý do]
❌ Gõ: REJECT {{content_id}} [lý do]

_Hoặc mở Google Sheet để điền trực tiếp._
```

---

## Template 2: Nhắc nhở Lần 2 (Sau 48 giờ chưa có phản hồi)

```
⏰ *NHẮC NHỞ: Nội dung chờ duyệt > 48 giờ*

🆔 *ID:* `{{content_id}}`
📱 *Platform:* {{platform}} | {{pillar}}
⏳ *Chờ từ:* {{ready_for_review_timestamp}} ({{hours_waiting}} giờ trước)

Bài này vẫn đang chờ quyết định của bạn.

📁 Xem tại: {{drive_folder_url}}

👇 *HÀNH ĐỘNG:*
✅ APPROVE {{content_id}}
📝 REVISE {{content_id}} [lý do]
❌ REJECT {{content_id}} [lý do]

_Nếu bạn muốn bỏ qua bài này, gõ: REJECT {{content_id}} bỏ qua_
```

---

## Template 3: Thông báo Revision Hoàn thành (AI đã sửa xong)

```
📝 *ĐÃ SỬA XONG — Chờ Duyệt Lại*

🆔 *ID:* `{{content_id}}`
🔄 *Lần revision:* {{revision_count}}/3

📋 *Bạn đã yêu cầu:*
_"{{revision_note}}"_

✏️ *AI đã sửa:*
{{ai_revision_summary}}

📝 *Caption mới (preview):*
_{{new_caption_preview_100chars}}..._

{{#if safety_flags}}
⚠️ *Safety Flags còn lại:*
{{safety_flags_formatted}}
{{else}}
✅ *Safety Check:* Pass
{{/if}}

📁 Xem toàn bộ: {{drive_folder_url}}

👇 *QUYẾT ĐỊNH:*
✅ APPROVE {{content_id}}
📝 REVISE {{content_id}} [lý do tiếp]
❌ REJECT {{content_id}} [lý do]
```

---

## Template 4: Nhắc Ngày Đăng (Sáng ngày SCHEDULE_PROPOSED)

```
📅 *NHẮC ĐĂNG BÀI HÔM NAY*

🆔 *ID:* `{{content_id}}`
📱 *Platform:* {{platform}} | {{content_type}}
🕐 *Giờ đăng đề xuất:* {{proposed_publish_time}} hôm nay

📝 *Caption:*
_{{caption_preview_200chars}}..._

📁 Full content: {{drive_folder_url}}

━━━━━━━━━━━━━━━━━━━━
📌 Sau khi đăng xong, ghi link bài vào Google Sheet:
• Cột R (manual_publish_link) — dòng {{sheet_row_id}}

Hoặc gõ: PUBLISHED {{content_id}} [link_bài_đăng]
```

---

## Template 5: Xác nhận Đã Approve

```
✅ *ĐÃ APPROVE*

🆔 `{{content_id}}` đã được duyệt lúc {{approval_timestamp}}

Bước tiếp theo:
1. Chọn ngày/giờ đăng → điền cột Q trong Sheet
2. Hoặc gõ: SCHEDULE {{content_id}} [YYYY-MM-DD HH:MM]

Mình sẽ nhắc bạn vào sáng ngày đó nhé 📅
```

---

## Template 6: Xác nhận Đã Reject

```
❌ *ĐÃ REJECT*

🆔 `{{content_id}}` đã bị từ chối.

📝 *Lý do:* _{{rejection_reason}}_

Bài này sẽ chuyển sang ARCHIVED.
AI sẽ không tạo lại bài này trừ khi bạn yêu cầu.

_Cảm ơn bạn đã review!_
```

---

## Template 7: Escalation (Revision ≥ 3 lần)

```
🚨 *CẦN OWNER TỰ VIẾT / BRIEF THÊM*

🆔 *ID:* `{{content_id}}`
⚠️ *Bài này đã qua 3 lần revision nhưng vẫn chưa đạt yêu cầu.*

Lịch sử revision:
1. {{revision_1_note}}
2. {{revision_2_note}}
3. {{revision_3_note}}

AI cần thêm thông tin để tạo đúng nội dung bạn muốn.

Bạn có thể:
• 📝 Gõ: BRIEF {{content_id}} [mô tả chi tiết hơn về bài bạn muốn]
• ✏️ Tự viết caption và điền vào Google Sheet
• ❌ Gõ: REJECT {{content_id}} bỏ qua nếu không cần bài này nữa
```

---

## Variable Reference (Biến trong Template)

| Biến | Nguồn dữ liệu | Ví dụ |
|------|--------------|-------|
| `{{content_id}}` | content_pack.id | `VQ-FB-PROD-20260527-001` |
| `{{created_at}}` | metadata.created_at | `27/05/2026 10:00` |
| `{{created_by_agent}}` | metadata.created_by_agent | `Claude Code (Builder)` |
| `{{platform}}` | content_pack.platform | `Facebook` |
| `{{content_type}}` | content_pack.content_type | `Post` |
| `{{pillar}}` | content_pack.pillar | `PROD` |
| `{{angle_name}}` | content_pack.angle.name | `hero-shot` |
| `{{persona_segment}}` | content_pack.persona.segment | `Segment A (dân văn phòng)` |
| `{{caption_preview_100chars}}` | caption_options[0].text — 100 ký tự đầu | `Cuốn đúng vị — no đúng bữa...` |
| `{{offer_code}}` | offer.offer_id | `OF-01` |
| `{{offer_name}}` | offer.offer_name | `Combo Trưa Vị Cuốn` |
| `{{offer_summary}}` | offer.offer_summary | `[FILL]đ — bánh tráng + bún trộn + nước` |
| `{{safety_flags_formatted}}` | safety_check.flags — formatted list | `⚠️ EMOJI_OVERLOAD (Warning)` |
| `{{drive_folder_url}}` | metadata.drive_folder_url | Google Drive link |
| `{{sheet_row_url}}` | Computed from metadata.sheet_row_id | Google Sheet link |
| `{{hours_waiting}}` | Computed: now - ready_for_review_timestamp | `51` |
| `{{revision_count}}` | approval.revision_count | `1` |
| `{{revision_note}}` | approval.revision_note | `Caption quá dài, cần ngắn hơn` |
| `{{ai_revision_summary}}` | AI-generated summary of changes | `Đã rút ngắn caption từ 280 → 180 ký tự` |
| `{{proposed_publish_time}}` | approval.proposed_publish_date — time only | `18:00` |
| `{{approval_timestamp}}` | approval.approval_timestamp | `27/05/2026 14:30` |
| `{{rejection_reason}}` | approval.revision_note (khi REJECTED) | `Bài không phù hợp với tone tuần này` |

---

## Telegram Bot Command Parser (n8n xử lý phản hồi)

Khi Owner gõ lệnh trong Telegram, n8n bot parser hiểu:

| Lệnh Owner gõ | n8n xử lý |
|--------------|----------|
| `APPROVE VQ-FB-PROD-20260527-001` | Set Sheet row: owner_decision=APPROVED, approval_timestamp=now, status=APPROVED |
| `REVISE VQ-FB-PROD-20260527-001 Caption quá dài` | Set Sheet row: owner_decision=REVISION_REQUESTED, revision_note="Caption quá dài", status=REVISION_REQUESTED |
| `REJECT VQ-FB-PROD-20260527-001 Không phù hợp` | Set Sheet row: owner_decision=REJECTED, revision_note="Không phù hợp", status=REJECTED |
| `SCHEDULE VQ-FB-PROD-20260527-001 2026-06-01 18:00` | Set Sheet row: proposed_publish_date=2026-06-01 18:00, status=SCHEDULE_PROPOSED |
| `PUBLISHED VQ-FB-PROD-20260527-001 https://fb.com/...` | Set Sheet row: manual_publish_link=URL, status=PUBLISHED_MANUAL |
| `BRIEF VQ-FB-PROD-20260527-001 Muốn tập trung vào...` | Create revision note, trigger AI revision |

**LƯU Ý: Telegram Command Parser là Phase 3 (n8n workflow). Phase 1.3 chỉ định nghĩa template. Trong Phase 1–2, Owner điền trực tiếp vào Google Sheet.**

---

## Ví dụ Tin nhắn Thực tế

### Ví dụ: Thông báo bài PROD chờ duyệt

```
📋 NỘI DUNG CHỜ DUYỆT

🆔 ID: VQ-FB-PROD-20260527-001
📅 Tạo lúc: 27/05/2026 10:30 (GMT+7)
👤 Tạo bởi: Claude Code (Builder)

━━━━━━━━━━━━━━━━━━
📱 Nền tảng: Facebook | Post
🎯 Pillar: PROD | Angle: hero-shot
👥 Persona: Segment A (dân văn phòng)
━━━━━━━━━━━━━━━━━━

📝 Caption (preview):
"Cuốn đúng vị — no đúng bữa 🍜
Bánh tráng mỏng giòn, thịt heo tươi, cuốn cùng rau sống..."

✅ Safety Check: Không có flag

━━━━━━━━━━━━━━━━━━
📁 Xem đầy đủ:
• Google Drive: [link]
• Google Sheet: [link dòng 5]

⏰ SLA: Vui lòng duyệt trong 48 giờ
━━━━━━━━━━━━━━━━━━

👇 HÀNH ĐỘNG CỦA OWNER:

✅ Gõ: APPROVE VQ-FB-PROD-20260527-001
📝 Gõ: REVISE VQ-FB-PROD-20260527-001 [lý do]
❌ Gõ: REJECT VQ-FB-PROD-20260527-001 [lý do]
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. 7 templates, variable reference, command parser spec. | Claude Code (Builder) |
