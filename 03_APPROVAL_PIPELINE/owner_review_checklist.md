# Owner Review Checklist — Vị Cuốn

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Checklist dành cho Owner khi duyệt từng content pack.*
*In ra hoặc mở trên điện thoại khi review — đánh dấu từng mục trước khi quyết định.*

---

## Cách dùng

1. Nhận thông báo Telegram từ n8n / AI Agent
2. Mở Google Drive link để xem full content pack
3. Đi qua từng mục trong checklist này
4. Nếu tất cả ✅ → APPROVE
5. Nếu có ❌ nhỏ → REVISE (ghi cụ thể cần sửa gì)
6. Nếu có ❌🔴 (blocker) → REJECT hoặc REVISE ngay

---

## PHẦN 1: Kiểm tra Thông tin Cơ bản

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Ghi chú |
|---|-------------|--------|--------|---------|
| 1.1 | Content ID đúng format và chưa bị trùng | | | |
| 1.2 | Platform đúng (Facebook / TikTok / IG / Zalo OA) | | | |
| 1.3 | Content type phù hợp với platform (Post / Reel / Story / v.v.) | | | |
| 1.4 | Pillar và angle đúng với nội dung thực tế | | | |
| 1.5 | Target persona đúng với nội dung hướng đến | | | |

---

## PHẦN 2: Kiểm tra Caption

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Ghi chú |
|---|-------------|--------|--------|---------|
| 2.1 | Caption đọc tự nhiên, không nghe "như robot viết" | | | |
| 2.2 | Giọng điệu phù hợp brand voice (ấm áp, gần gũi, không trang trọng) | | | |
| 2.3 | Không có lỗi chính tả tiếng Việt | | | |
| 2.4 | Không có giá không đúng so với menu_brain.md | | | |
| 2.5 | Không có claim sức khỏe ("tốt cho sức khỏe", "giảm cân", "detox") | | | |
| 2.6 | Không nhắc tên đối thủ | | | |
| 2.7 | Không có fake urgency ("Còn 3 suất!!!" khi không thật) | | | |
| 2.8 | Không dùng VIẾT HOA toàn câu để nhấn mạnh | | | |
| 2.9 | Emoji ≤ 3 cái trong toàn bộ caption | | | |
| 2.10 | Có hashtag cốt lõi: #VịCuốn #ĂnVinh #VinhNghệAn (trừ Zalo OA) | | | |
| 2.11 | Độ dài phù hợp platform (FB ≤2.000c, TikTok ≤150c, IG ≤2.200c) | | | |
| 2.12 | Có CTA rõ ràng (ghé quán / đặt ngay / inbox / v.v.) | | | |

---

## PHẦN 3: Kiểm tra Offer (Chỉ khi bài có offer)

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Không áp dụng | Ghi chú |
|---|-------------|--------|--------|--------------|---------|
| 3.1 | Offer ID có trong offer_engine.md | | | | |
| 3.2 | Trạng thái offer là ACTIVE | | | | |
| 3.3 | Giá offer khớp với offer_engine.md | | | | |
| 3.4 | Voucher code (nếu có) đã được đăng ký trong Google Sheet Vouchers | | | | |
| 3.5 | Ngày hiệu lực offer còn hạn vào ngày dự kiến đăng bài | | | | |
| 3.6 | Điều kiện áp dụng offer được nêu rõ trong caption (nếu có giới hạn) | | | | |

---

## PHẦN 4: Kiểm tra Hình ảnh / Video Brief

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Ghi chú |
|---|-------------|--------|--------|---------|
| 4.1 | Image brief mô tả rõ chủ thể, góc chụp, ánh sáng | | | |
| 4.2 | Brief yêu cầu ảnh thật của quán (không phải ảnh stock) | | | |
| 4.3 | Không có yêu cầu chỉnh màu đồ ăn quá mức | | | |
| 4.4 | Brief không yêu cầu bếp bẩn / sàn bẩn / nhân viên không chuyên nghiệp trong frame | | | |

*Nếu bài có video script:*

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Không áp dụng | Ghi chú |
|---|-------------|--------|--------|--------------|---------|
| 4.5 | Script có hook mạnh trong 3 giây đầu | | | | |
| 4.6 | Độ dài video phù hợp platform (TikTok 15–60s, Reels 15–30s) | | | | |
| 4.7 | Không yêu cầu nhạc bản quyền không có license | | | | |
| 4.8 | Script có subtitle / text overlay | | | | |
| 4.9 | CTA trong video rõ ràng | | | | |

---

## PHẦN 5: Kiểm tra Safety Flags (AI đã phát hiện)

| # | Mục kiểm tra | ✅ Xử lý | ❌ Chưa xử lý | Ghi chú |
|---|-------------|---------|-------------|---------|
| 5.1 | Xem qua danh sách safety_flags trong content pack | | | |
| 5.2 | Các flag BLOCKER đã được giải quyết (không còn trong bài) | | | |
| 5.3 | Các flag WARNING đã được review — Owner quyết định chấp nhận hay sửa | | | |
| 5.4 | Không có flag nào bị bỏ qua mà không có lý do | | | |

---

## PHẦN 6: Kiểm tra Tổng thể

| # | Mục kiểm tra | ✅ Pass | ❌ Fail | Ghi chú |
|---|-------------|--------|--------|---------|
| 6.1 | Bài phù hợp với kế hoạch content tuần này | | | |
| 6.2 | Tone và nội dung không xung đột với bài đã đăng gần nhất | | | |
| 6.3 | Bài không vi phạm bất kỳ quy định nào trong approval_rules.md | | | |
| 6.4 | Owner cảm thấy tự tin khi đăng bài này | | | |

---

## Ma trận Quyết định

```
Sau khi check xong:

✅ Tất cả mục pass (không có ❌)
→ APPROVE: ghi owner_decision = APPROVED + approval_timestamp

❌ Có 1–3 mục fail nhỏ (sai tone, emoji nhiều, caption dài hơn chút)
→ REVISE: ghi owner_decision = REVISION_REQUESTED
→ Ghi rõ revision_note: "1. Caption quá dài, cần rút ngắn còn ~180 ký tự.
                           2. Thêm CTA rõ hơn ở cuối."
→ AI sẽ sửa và gửi lại

❌ Có bất kỳ BLOCKER nào (giá sai, claim sức khỏe, fake review, v.v.)
→ REVISE hoặc REJECT ngay
→ Ghi lý do cụ thể

❌ Bài hoàn toàn không phù hợp (sai hướng hoàn toàn / tone quá lạ)
→ REJECT: ghi lý do
→ Cân nhắc: cần brief lại AI chi tiết hơn trước khi tạo bài mới
```

---

## Hướng dẫn Viết Revision Note Hiệu quả

### Cấu trúc tốt

```
REVISION_NOTE CẦN:
1. [Vấn đề cụ thể] — [Mong muốn cụ thể]
2. [Vấn đề cụ thể] — [Mong muốn cụ thể]

Ví dụ:
"1. Caption v1 quá dài (280 ký tự) — cần rút ngắn còn ~150 ký tự cho Facebook.
 2. Thiếu giờ mở cửa trong CTA — thêm 'mở từ 10h hàng ngày' vào.
 3. Emoji ở dòng 2 không cần — bỏ đi."
```

### Tránh viết mơ hồ

| Viết MƠ HỒ ❌ | Viết CỤ THỂ ✅ |
|-------------|------------|
| "Caption không hay" | "Caption v1 giọng quá trang trọng, cần gần gũi hơn — đổi 'Quý khách' thành 'bạn'" |
| "Sửa lại" | "Rút ngắn caption từ 280 còn 150 ký tự, giữ nguyên hook đầu" |
| "Không đúng tone" | "Tone quá marketing, nghe như quảng cáo. Cần viết như đang nhắn tin cho bạn bè" |
| "Hình ảnh không đẹp" | "Brief cần thêm: muốn ảnh có rau sống xanh rõ nét bên cạnh cuốn" |

---

## Thời gian Review Đề xuất

| Loại bài | Thời gian review đề xuất |
|---------|------------------------|
| Bài đơn (Post / Story) | 3–5 phút |
| Bài có video script | 5–10 phút |
| Bài có offer | 5–8 phút (cần check offer engine) |
| Bài multi-platform | 8–12 phút |

---

## Câu hỏi Owner Tự hỏi Trước khi APPROVE

> 1. **Tôi có tự tin đăng bài này ngay bây giờ không?**
>    → Nếu do dự → REVISE, không phải APPROVE rồi sửa sau
>
> 2. **Bài này có thể gây hiểu nhầm không?**
>    → Nếu có khả năng → sửa trước
>
> 3. **Khách hàng của mình sẽ cảm thấy gì khi đọc bài này?**
>    → Thèm ăn, muốn ghé → tốt
>    → Hoang mang, nghi ngờ → sửa lại
>
> 4. **Nếu bài này bị screenshot và share rộng rãi, tôi có OK không?**
>    → Nếu không OK → sửa trước khi đăng

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. 6 phần checklist, ma trận quyết định, hướng dẫn revision note. | Claude Code (Builder) |
