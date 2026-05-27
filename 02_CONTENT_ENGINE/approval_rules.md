# Approval Rules — Vị Cuốn

*Phase 1.2 — Content Pillar & Offer Engine*
*Quy tắc duyệt nội dung bắt buộc áp dụng cho mọi bài đăng, video, offer.*
*AI Agent không được bỏ qua bất kỳ quy tắc nào trong file này.*

---

## Nguyên tắc Tuyệt đối

> **KHÔNG có bất kỳ nội dung nào được đăng lên bất kỳ nền tảng nào mà không qua Owner approve.**

Quy tắc này áp dụng với:
- Tất cả bài Facebook / TikTok / Instagram / Zalo OA
- Tất cả video / Reels / Stories
- Tất cả offer và voucher
- Tất cả reply comment công khai
- Tất cả broadcast Zalo OA

**AI chỉ tạo nội dung và trình Owner duyệt — AI KHÔNG tự đăng, KHÔNG tự lên lịch đăng.**

---

## Quy trình Approval Chuẩn

```
Bước 1: AI Agent tạo Content Pack
  → Caption + Image Brief + Hashtag + Offer (nếu có)
  → Lưu vào Google Drive: /Draft/[YYYY-MM]/[platform]/

Bước 2: AI gửi thông báo cho Owner
  → Telegram / Zalo / Kênh đã chọn
  → Nội dung: "Bài [tên] — [platform] — đã sẵn sàng để duyệt. Link: [link Drive]"

Bước 3: Owner review
  → Đọc caption, xem ảnh/video brief
  → Approve: Owner đăng tay hoặc chọn lên lịch thủ công
  → Reject: Owner ghi feedback → AI chỉnh sửa → quay lại Bước 1

Bước 4: Sau khi đăng
  → Lưu vào Google Drive: /Published/[YYYY-MM]/[platform]/
  → Cập nhật Content Calendar
```

---

## Checklist Duyệt Nội dung (Owner dùng)

Trước khi đăng bất kỳ bài nào, Owner kiểm tra:

### Checklist Nội dung

| # | Kiểm tra | Pass | Fail |
|---|---------|------|------|
| 1 | Caption không có giá sai so với menu_brain.md | ✅ | ❌ |
| 2 | Caption không claim sức khỏe / dinh dưỡng không có căn cứ | ✅ | ❌ |
| 3 | Caption không nhắc tên đối thủ | ✅ | ❌ |
| 4 | Caption không tạo áp lực giả ("Còn X suất" khi không thật) | ✅ | ❌ |
| 5 | Caption không dùng giọng điệu quá trang trọng hoặc Z quá đà | ✅ | ❌ |
| 6 | Hashtag đúng — có #VịCuốn #ĂnVinh #VinhNghệAn (trừ Zalo) | ✅ | ❌ |
| 7 | Emoji ≤ 2–3 cái/caption | ✅ | ❌ |

### Checklist Hình ảnh / Video

| # | Kiểm tra | Pass | Fail |
|---|---------|------|------|
| 8 | Hình ảnh là ảnh thật của quán (không phải ảnh stock) | ✅ | ❌ |
| 9 | Ảnh đủ sáng, rõ nét — không mờ, không tối | ✅ | ❌ |
| 10 | Màu đồ ăn tự nhiên — không chỉnh quá mức | ✅ | ❌ |
| 11 | Không có bếp bẩn, sàn bẩn, nhân viên không chuyên nghiệp trong frame | ✅ | ❌ |
| 12 | Video không dùng nhạc bản quyền không có license | ✅ | ❌ |
| 13 | Video có subtitle / text overlay (nhiều người xem tắt tiếng) | ✅ | ❌ |

### Checklist Offer (nếu bài có offer)

| # | Kiểm tra | Pass | Fail |
|---|---------|------|------|
| 14 | Offer có trong offer_engine.md với trạng thái ACTIVE | ✅ | ❌ |
| 15 | Giá offer khớp với offer_engine.md | ✅ | ❌ |
| 16 | Voucher code đã được đăng ký trong Google Sheet Vouchers | ✅ | ❌ |
| 17 | Thời hạn offer đúng (không hết hạn, không sắp hết hạn mà không thông báo) | ✅ | ❌ |

**Nếu bất kỳ ô nào là ❌ → KHÔNG đăng → gửi feedback cho AI chỉnh sửa.**

---

## Safety Rules — Nội dung Tuyệt đối KHÔNG làm

### Nhóm 1: Thông tin sai lệch

| Không làm | Lý do |
|-----------|-------|
| Viết giá không có trong menu_brain.md | Gây nhầm lẫn, mất trust, vi phạm giá |
| Claim sức khỏe: "tốt cho sức khỏe", "giảm cân", "detox" | Không có bằng chứng, rủi ro pháp lý |
| Hứa giao hàng nhanh khi không chắc chắn | Khách thất vọng khi không đúng hẹn |
| Fake urgency: "Còn 3 suất cuối!!!" khi không thật | Vi phạm trust — khách phát hiện sẽ mất mãi |
| Fake review: tự tạo review / screenshot giả | Vi phạm pháp luật, mất uy tín nghiêm trọng |
| Nói quán đang đông không tự nhiên | Tạo áp lực giả, khách biết sẽ mất trust |

### Nhóm 2: Nội dung nhạy cảm

| Không làm | Lý do |
|-----------|-------|
| Nhắc tên đối thủ (kể cả so sánh tích cực) | Kéo attention vào đối thủ, rủi ro conflict |
| Bình luận về giá đối thủ | Chiến tranh giá — không ai thắng |
| Nội dung chính trị, tôn giáo | Không liên quan, rủi ro cao |
| Nội dung có thể gây tranh luận xã hội | Tập trung vào ẩm thực, không đi vào vùng nhạy cảm |
| Ảnh/video bếp bẩn, thực phẩm rơi | Phá hỏng trust về vệ sinh |

### Nhóm 3: Quyền riêng tư & Bản quyền

| Không làm | Lý do |
|-----------|-------|
| Dùng ảnh stock đồ ăn | Không phải ảnh thật → mất authenticity |
| Repost ảnh khách mà không xin phép | Vi phạm quyền riêng tư |
| Dùng nhạc bản quyền không có license | Nền tảng xóa bài, account bị phạt |
| Đăng thông tin cá nhân của khách | Vi phạm PDPA / quyền riêng tư |
| Dùng logo/hình ảnh thương hiệu khác | Rủi ro bản quyền |

### Nhóm 4: Hành vi tự động bị cấm tuyệt đối

| Không làm | Lý do |
|-----------|-------|
| Auto-post lên Facebook/TikTok/IG/Zalo | Rủi ro đăng nội dung sai, không kiểm soát được |
| Auto-reply comment của khách | Có thể reply sai, gây incident |
| Auto-reply tin nhắn Messenger/Zalo | Rủi ro xử lý sai khiếu nại |
| Chạy quảng cáo trả phí tự động | Burn tiền không kiểm soát |
| Tự tạo voucher/deal ngoài offer_engine.md | Tài chính không kiểm soát |

---

## Phân loại Mức độ Rủi ro

### 🔴 BLOCKER — Dừng và báo ngay

Phát hiện bất kỳ điều sau → DỪNG, KHÔNG đăng, báo Owner ngay:

- Thông tin giá sai
- Claim sức khỏe không có căn cứ
- Fake review / fake urgency
- Nội dung liên quan đến khiếu nại an toàn thực phẩm
- Ảnh/video lộ thông tin nhạy cảm
- API key / token / mật khẩu lộ trong nội dung

### 🟠 CẢNH BÁO — Cần sửa trước khi đăng

- Emoji quá nhiều (>3/caption)
- Thiếu hashtag cốt lõi
- Giọng điệu không đúng brand voice (quá trang trọng / quá Z)
- Caption quá dài cho platform (TikTok >150 chữ, IG >2200 chữ)
- Hình ảnh hơi tối / cần chỉnh sáng nhẹ

### 🟡 GHI CHÚ — Có thể đăng nhưng nên cải thiện

- Có thể thêm emoji phù hợp
- CTA có thể mạnh hơn
- Caption có thể ngắn hơn để dễ đọc trên mobile

---

## Quy trình Xử lý Sự cố Sau Đăng

### Nếu phát hiện lỗi sau khi bài đã đăng

```
1. Owner edit bài ngay (không xóa trừ khi thật sự cần)
2. Nếu giá sai → comment cải chính ngay dưới bài
3. Nếu claim sức khỏe sai → sửa caption, xóa claim
4. Ghi lại incident trong Error Log: 06_HANDOFF/ERROR_LOG.md
5. Cập nhật approval checklist nếu cần thêm bước kiểm tra
```

### Nếu khách comment phàn nàn về bài đăng

```
1. Owner đọc comment — đánh giá nghiêm trọng
2. Không reply vội — đặc biệt nếu comment nhạy cảm
3. Nếu liên quan an toàn thực phẩm: escalate ngay (xem escalation rules trong customer_brain.md)
4. Nếu thông tin sai: thừa nhận + cảm ơn khách đã góp ý + sửa bài
5. Không reply bằng AI — dùng người thật
```

---

## Qui trình Review của AI Agent

Khi AI tạo content pack, AI tự check:

```
AI SELF-CHECK TRƯỚC KHI GỬI OWNER:

✅ Giá trong bài có trong menu_brain.md hoặc offer_engine.md?
✅ Không có claim sức khỏe / dinh dưỡng?
✅ Không nhắc tên đối thủ?
✅ Không tạo fake urgency?
✅ Giọng điệu phù hợp brand voice (ấm áp, gần gũi, không trang trọng)?
✅ Hashtag có #VịCuốn #ĂnVinh #VinhNghệAn?
✅ Emoji ≤ 3 cái?
✅ Nếu có offer → offer_engine.md có offer này không?

Nếu tất cả ✅ → Gửi Owner duyệt.
Nếu có ❌ → Sửa trước khi gửi.
AI KHÔNG gửi bài lỗi cho Owner.
```

---

## Phân quyền Nội dung

| Hành động | AI được phép? | Nhân viên được phép? | Owner cần? |
|-----------|--------------|---------------------|-----------|
| Tạo caption draft | ✅ | ✅ | Review |
| Tạo image brief | ✅ | ✅ | Review |
| Chọn hashtag | ✅ | ✅ | Review |
| Đăng bài lên Facebook | ❌ | ❌ (chỉ theo lệnh Owner) | Approve trước |
| Lên lịch đăng | ❌ | ❌ | Approve trước |
| Reply comment | ❌ | ✅ (theo kịch bản) | Không cần cho reply thường |
| Reply phàn nàn nghiêm trọng | ❌ | ❌ | Phải xử lý trực tiếp |
| Tạo offer mới | ❌ | ❌ | Phê duyệt và ghi vào offer_engine.md |
| Phát voucher | ❌ | ❌ (chỉ theo hệ thống) | Quyết định và đăng ký voucher |
| Chạy quảng cáo | ❌ | ❌ | Phê duyệt budget và creative |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.2 — File tạo mới. Approval flow, owner checklist, safety rules, incident handling, phân quyền. | Claude Code (Builder) |
