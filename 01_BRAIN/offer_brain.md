# Offer Brain — Vị Cuốn

*Phase 1.1 update: Filled với offer framework cho Vị Cuốn. Giá và % discount là [FILL] — Owner xác nhận.*

---

## Active Offers

| Tên Offer | Mô tả | Discount | Hiệu lực | Target Segment |
|-----------|-------|----------|----------|----------------|
| **Combo Trưa** | 1 bánh tráng cuốn thịt heo + 1 bún trộn nhỏ + 1 nước | [FILL: giá combo so với mua lẻ] | Thứ 2–6, 11:00–14:00 | Dân văn phòng |
| **Combo Cuối Tuần** | 1 cuốn + 1 bún trộn + 2 gỏi cuốn + 1 nước | [FILL: giá combo] | Thứ 7–CN | Gia đình, nhóm bạn |
| **Combo Gia Đình** (2 người) | 2 bánh tráng cuốn + 2 bún trộn + 2 nước | [FILL: giá — discount ~10–15%] | Cả ngày | Gia đình trẻ |
| **Lần đầu tiên** | Voucher giảm [FILL: %, e.g., 15%] cho khách mới qua ShopeeFood/GrabFood | [FILL: %] | First order only | Khách mới |
| [FILL: offer theo mùa/sự kiện] | [FILL] | [FILL] | [FILL] | [FILL] |

---

## Offer Rules

### Discount Logic
- Giảm tối đa một đơn: [FILL: %, gợi ý 20%]
- Combo không được stack với voucher khác (trừ khi Owner quyết định khác)
- Ngưỡng order miễn phí giao hàng: [FILL: VNĐ, gợi ý 150.000đ]
- Loyalty discount sau: [FILL: N lần, gợi ý sau 5 đơn]
- Voucher lần đầu: áp dụng 1 lần/tài khoản/số điện thoại

### Voucher Code Format
- Format: `VQ-[LOẠI]-[YYYYMMDD]`
- Ví dụ: `VQ-LUNCH-20260601`, `VQ-NEW-20260601`
- Tất cả voucher phải đăng ký trong Google Sheet tab: **Vouchers**
- Không tự phát voucher ngoài hệ thống mà không ghi vào Sheet

---

## Upsell Triggers

| Hành động khách | Tin nhắn upsell | Kênh |
|----------------|----------------|------|
| Đặt 1 phần bánh tráng cuốn | "Thêm bún trộn mắm nêm nhỏ cho no hơn — chỉ [FILL]đ thôi bạn ơi!" | Chat / menu mô tả |
| Chưa gọi đồ uống | "Thêm nước chanh tươi cho mát miệng — [FILL]đ!" | Khi xác nhận đơn |
| Tổng đơn dưới ngưỡng giao miễn phí | "Thêm [FILL: món] để đủ [FILL]đ giao miễn phí nhé!" | ShopeeFood/GrabFood |
| Khách hỏi món chay | "Bạn thử gỏi cuốn chay không? Rau tươi, đậu hũ chiên vàng, ngon lắm!" | Chat |
| Khách lần đầu | "Bạn là khách mới — giảm [FILL]% đơn đầu tiên, nhập mã [FILL: code]" | Tin nhắn chào mừng |

---

## Cross-sell Triggers

| Món đặt | Gợi ý thêm |
|---------|-----------|
| Bánh tráng cuốn thịt heo | Bún trộn mắm nêm, thêm mắm nêm riêng |
| Bún trộn mắm nêm | Gỏi cuốn tôm thịt, thêm đậu phộng rang |
| Gỏi cuốn | Nước chanh tươi, thêm tương hoisin |
| Heo quay | Bánh tráng cuốn heo quay, cơm trắng (nếu có) |

---

## Promotion Calendar (Template — Điền theo thực tế)

| Tháng | Chủ đề chiến dịch | Ngày key | Loại offer |
|-------|------------------|----------|-----------|
| Tháng 6 | Combo Trưa Hè | Weekdays | Combo discount |
| Tháng 8 | [FILL: Ngày lễ tháng 8 — Cách mạng 19/8] | 19/08 | Voucher đặc biệt |
| Tháng 9 | Back to School | Đầu tháng 9 | Deal sinh viên |
| Tháng 10 | [FILL: sự kiện địa phương Vinh] | [FILL] | [FILL] |
| Tháng 11 | 11/11 Mini-sale | 11/11 | [FILL: % off combo] |
| Tháng 12 | Combo Tất Niên | Cuối tháng 12 | Combo gia đình |
| [FILL] | [FILL] | [FILL] | [FILL] |

---

## Offer Safety Rules

| Quy tắc | Chi tiết |
|---------|---------|
| KHÔNG tự tạo deal ngoài danh sách | AI chỉ quảng bá offer đã được Owner phê duyệt |
| KHÔNG đăng giá sai | Giá offer phải từ bảng Active Offers ở trên |
| KHÔNG đặt voucher code chưa đăng ký | Tất cả code phải trong Google Sheet Vouchers |
| KHÔNG tự gia hạn offer | Chỉ gia hạn khi Owner cập nhật file này |
| Khi khách claim "không nhận được deal" | Chuyển cho nhân viên/Owner — không tự xử lý |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-26 | File created — placeholders only | Builder Agent (Claude) |
| 2026-05-27 | Phase 1.1 — Filled offer framework (Combo Trưa, Cuối Tuần, Gia Đình, Lần Đầu), upsell/cross-sell triggers, promotion calendar template, safety rules. Giá [FILL] — Owner xác nhận. | Claude Code (Builder) |
