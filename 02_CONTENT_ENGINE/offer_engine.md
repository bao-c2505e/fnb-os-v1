# Offer Engine — Vị Cuốn

*Phase 1.2 — Content Pillar & Offer Engine*
*Logic ưu đãi đầy đủ để AI và nhân viên xử lý đúng offer. Giá là [FILL] — Owner xác nhận.*
*Nguồn gốc: offer_brain.md (Phase 1.1) — Phase 1.2 mở rộng thêm offer logic và trigger rules.*

---

## Tổng quan Offer Engine

Offer Engine của Vị Cuốn hoạt động theo 3 lớp:

```
Lớp 1: TRIGGER — Điều kiện nào kích hoạt offer?
  ↓
Lớp 2: OFFER — Offer cụ thể là gì? (Gồm gì, giá bao nhiêu, thời hạn nào?)
  ↓
Lớp 3: DELIVERY — Deliver offer như thế nào? (Kênh, cách truyền thông, CTA)
```

**Quy tắc tuyệt đối:**
- AI KHÔNG tự tạo offer ngoài danh sách này
- AI KHÔNG tự chỉnh giá
- AI KHÔNG tự kích hoạt / hết hạn offer
- Mọi offer mới phải Owner phê duyệt và cập nhật file này

---

## CATALOG OFFER HIỆN TẠI

### OF-01: Combo Trưa (Weekday Lunch Combo)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-01 |
| **Tên hiển thị** | Combo Trưa Vị Cuốn |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Gồm** | 1 phần bánh tráng cuốn thịt heo + 1 bún trộn mắm nêm nhỏ + 1 nước (chanh tươi hoặc trà) |
| **Giá** | [FILL: VNĐ — target ~65.000đ] |
| **Giá mua lẻ tương đương** | [FILL: VNĐ] |
| **Tiết kiệm** | [FILL: X.000đ so với mua lẻ] |
| **Hiệu lực** | Thứ 2–6 | 11:00–14:00 |
| **Target segment** | Segment A (dân văn phòng) |
| **Kênh bán** | Tại quán, ShopeeFood, GrabFood, Zalo OA |
| **Không stack với** | Voucher giảm giá khác |
| **Caption trigger** | T-PROMO-01, T-PROD-02 |
| **Video trigger** | VS-02, VS-08 |

**Trigger Content:**
- Đăng bài nhắc COMBO TRƯA: Thứ 2 sáng + Thứ 4 trưa + Thứ 5 tối (nhắc cho hôm sau)
- Zalo OA broadcast: Thứ 2 và Thứ 4, 10:00–10:30

**Messaging ngắn gọn:**
> "Combo Trưa [FILL]đ — bánh tráng cuốn thịt heo + bún trộn + nước. Thứ 2–6, 11:00–14:00."

---

### OF-02: Combo Cuối Tuần (Weekend Combo)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-02 |
| **Tên hiển thị** | Combo Cuối Tuần Vị Cuốn |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Gồm** | 1 phần cuốn + 1 bún trộn mắm nêm + 2 gỏi cuốn tôm thịt + 1 nước |
| **Giá** | [FILL: VNĐ — target ~80.000đ/người] |
| **Giá mua lẻ tương đương** | [FILL: VNĐ] |
| **Hiệu lực** | Thứ 7–CN | Cả ngày |
| **Target segment** | Segment B (gia đình), nhóm bạn |
| **Kênh bán** | Tại quán, ShopeeFood, GrabFood |
| **Không stack với** | Voucher giảm giá khác |

**Trigger Content:**
- Đăng bài thứ 5 tối / thứ 6 sáng — nhắc deal cuối tuần sắp tới
- Caption template: T-PROMO-02

---

### OF-03: Combo Gia Đình (Family Combo — 2 người)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-03 |
| **Tên hiển thị** | Combo Gia Đình (2 người) |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Gồm** | 2 phần bánh tráng cuốn + 2 bún trộn mắm nêm + 2 nước |
| **Giá** | [FILL: VNĐ — target ~130.000–140.000đ] |
| **Discount so với lẻ** | [FILL: ~10–15%] |
| **Hiệu lực** | Cả tuần, cả ngày |
| **Target segment** | Segment B (gia đình trẻ) |
| **Kênh bán** | Tại quán, đặt trước qua Zalo/inbox |

**Trigger Content:**
- Cuối tuần: caption T-PROMO-04
- Hình ảnh bàn ăn gia đình

---

### OF-04: Khách Mới (New Customer Offer)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-04 |
| **Tên hiển thị** | Ưu Đãi Lần Đầu |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Hình thức** | Giảm [FILL: X%] hoặc giảm [FILL: X.000đ] đơn đầu tiên |
| **Điều kiện** | Áp dụng 1 lần / tài khoản / số điện thoại |
| **Đơn tối thiểu** | [FILL: VNĐ] |
| **Voucher code** | [FILL: VQ-NEW-YYYYMMDD] |
| **Hiệu lực** | [FILL: ngày bắt đầu] → [FILL: ngày hết hạn] |
| **Kênh áp dụng** | ShopeeFood, GrabFood, [OPT: Zalo OA] |
| **Target segment** | Khách chưa từng đặt |

**Trigger:**
- Bài Facebook/TikTok mời thử: Caption T-PROMO-03
- Đặt trên ShopeeFood/GrabFood: description mention offer

---

### OF-05: Khách Quay Lại (Comeback Offer)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-05 |
| **Tên hiển thị** | Nhớ Bạn Rồi! |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Trigger condition** | Khách không đặt trong [FILL: 30–45 ngày] |
| **Hình thức** | [FILL: voucher X% hoặc tặng topping / đồ uống] |
| **Voucher code** | [FILL: VQ-BACK-YYYYMMDD] |
| **Kênh deliver** | Zalo OA (tin nhắn cá nhân hóa), Facebook Messenger |
| **Target segment** | At-Risk và Lapsed (từ customer_brain.md) |

**Messaging mẫu:**
> "Lâu rồi không ghé nhà mình rồi bạn ơi 🥲 Hôm nay có deal đặc biệt dành cho bạn — [FILL: mô tả offer]. Mã: [FILL: code] | Hết hạn: [FILL: ngày]"

**Ghi chú:** Chỉ gửi khi Owner xác nhận voucher code đã được tạo trong hệ thống.

---

### OF-06: Ngày Mưa / Trời Lạnh (Rainy Day Offer)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-06 |
| **Tên hiển thị** | Deal Ngày Mưa |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE — chỉ bật khi trời mưa thật] |
| **Trigger thực tế** | Owner bật thủ công khi trời mưa ở Vinh |
| **Hình thức** | [FILL: giao hàng miễn phí / giảm X% / tặng thêm phần nước] |
| **Hiệu lực** | Trong ngày Owner kích hoạt |
| **Kênh deliver** | Facebook post nhanh, Zalo OA broadcast |
| **Món đề xuất** | Bún trộn mắm nêm (ấm), bánh tráng cuốn thịt heo (no) |

**Content trigger:** T-PROMO-05, VS-09

**Quy tắc:** KHÔNG tự đăng. Owner thấy trời mưa → bật OF-06 → post bài theo T-PROMO-05.

---

### OF-07: Bữa Trưa Văn Phòng (Office Lunch Group Order)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-07 |
| **Tên hiển thị** | Order Nhóm Văn Phòng |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Điều kiện** | Đặt từ [FILL: X] phần trở lên (nhóm ≥3 người) |
| **Ưu đãi** | [FILL: giao miễn phí / giảm X% toàn đơn / tặng thêm đồ uống] |
| **Đơn tối thiểu** | [FILL: VNĐ] |
| **Kênh bán** | Gọi trực tiếp / inbox / Zalo — đặt trước 30 phút |
| **Target segment** | Segment A — văn phòng gần quán |

**Messaging mẫu:**
> "Cả văn phòng muốn ăn cùng? Đặt từ [FILL: X] phần — nhà mình có ưu đãi đặc biệt. Inbox hoặc gọi [FILL: số] trước [FILL: giờ] nhé!"

---

### OF-08: Combo Cuối Tuần (Weekend Special Upgrade)

| Field | Value |
|-------|-------|
| **Offer ID** | OF-08 |
| **Tên hiển thị** | Bữa Cuối Tuần Đặc Biệt |
| **Trạng thái** | [FILL: ACTIVE / INACTIVE] |
| **Trigger** | Thứ 7–CN |
| **Ưu đãi** | [FILL: nâng cấp heo quay / tặng gỏi cuốn / free topping] |
| **Hiệu lực** | Thứ 7–CN | Cả ngày |
| **Target segment** | Segment B (gia đình), Segment C (sinh viên) |

---

### OF-09: Offer Theo Mùa / Sự Kiện (Seasonal Offer)

*Template cho mỗi sự kiện — Owner điền khi có sự kiện cụ thể.*

| Field | Value |
|-------|-------|
| **Offer ID** | OF-09-[EVENT] |
| **Tên hiển thị** | [FILL: tên offer theo sự kiện] |
| **Sự kiện** | [FILL: 8/3 / 11/11 / Tết / Back to School / v.v.] |
| **Gồm** | [FILL] |
| **Giá / Discount** | [FILL] |
| **Hiệu lực** | [FILL: ngày bắt đầu] → [FILL: ngày kết thúc] |
| **Voucher code** | [FILL: VQ-[EVENT]-YYYYMMDD] |
| **Target segment** | [FILL] |

**Ví dụ sự kiện đề xuất:**

| Sự kiện | Tháng | Offer gợi ý |
|---------|-------|------------|
| Ngày Lễ 8/3 | Tháng 3 | Giảm X% cho khách nữ hoặc combo đôi |
| Back to School | Tháng 9 | Deal sinh viên — combo X người giá Y |
| 11/11 | Tháng 11 | Mini-sale 11% off combo trưa trong 11 tiếng |
| Tất Niên | Tháng 12 | Combo gia đình lớn hơn, giá ưu đãi |
| Ngày Lễ Tình Nhân 14/2 | Tháng 2 | Combo đôi đặc biệt |

---

## OFFER DECISION MATRIX

### Khi nào dùng offer nào?

| Tình huống | Offer đề xuất | Kênh deliver |
|-----------|--------------|-------------|
| Đầu tuần — văn phòng trưa | OF-01 (Combo Trưa) | Facebook sáng thứ 2, Zalo OA |
| Cuối tuần sắp tới | OF-02 (Combo Cuối Tuần) | Facebook thứ 5–6, IG |
| Khách đặt đơn đầu tiên | OF-04 (Khách Mới) | ShopeeFood/GrabFood |
| Khách không ghé 30+ ngày | OF-05 (Comeback) | Zalo OA, Messenger |
| Trời mưa | OF-06 (Ngày Mưa) | Facebook nhanh, Zalo OA |
| Nhóm văn phòng 3+ người | OF-07 (Office Lunch) | Tin nhắn trực tiếp |
| Cuối tuần gia đình | OF-03 + OF-02 | Facebook ảnh đẹp |
| Dịp lễ | OF-09 (Seasonal) | Tất cả platform |

---

## UPSELL LOGIC (Tích hợp vào mọi kênh)

### Quy tắc Upsell
1. **Upsell chỉ sau khi xác nhận order — không upsell khi khách hỏi thông tin**
2. **1 lần upsell/đơn — không spam thêm nhiều lần**
3. **Upsell phải liên quan đến món đang đặt**

### Bảng Upsell Cụ thể

| Khách đặt | Gợi ý upsell | Text mẫu |
|-----------|-------------|---------|
| 1 phần bánh tráng cuốn | Thêm bún trộn mắm nêm | "Thêm bún trộn nhỏ để no hơn — chỉ [FILL]đ thôi bạn ơi!" |
| Chưa gọi đồ uống | Nước chanh tươi hoặc trà | "Thêm nước chanh tươi cho mát miệng — [FILL]đ!" |
| Đơn dưới ngưỡng ship miễn phí | Thêm món nhỏ | "Thêm [món] để đủ [FILL]đ giao miễn phí nhé!" |
| Khách hỏi chay | Gỏi cuốn chay | "Bạn thử gỏi cuốn chay không? Rau tươi, đậu hũ chiên vàng — ngon lắm!" |
| 2+ người đặt riêng lẻ | Combo gia đình | "Hai bạn đặt cùng — mình có Combo Gia Đình [FILL]đ tiết kiệm hơn đó!" |

### Quy tắc KHÔNG Upsell
- KHÔNG upsell khi khách phàn nàn / có vấn đề
- KHÔNG upsell khi khách hỏi giờ mở cửa / địa chỉ
- KHÔNG upsell món không có trong `menu_brain.md`
- KHÔNG đặt giá ngoài `menu_brain.md`

---

## CROSS-SELL LOGIC

| Món đặt | Gợi ý cross-sell | Khi nào |
|---------|-----------------|--------|
| Bánh tráng cuốn thịt heo | Bún trộn mắm nêm | Xác nhận đơn |
| Bún trộn mắm nêm | Gỏi cuốn tôm thịt | Xác nhận đơn |
| Gỏi cuốn | Thêm tương hoisin / tương lạc | Khi chuẩn bị đơn |
| Heo quay | Thêm bánh tráng cuốn heo quay | Xác nhận đơn |
| Đơn chay | Gỏi cuốn chay + nước chanh không đường | Khi khách hỏi |

---

## VOUCHER CODE SYSTEM

### Format Chuẩn
```
VQ-[LOẠI]-[YYYYMMDD]
```

**Ví dụ:**
- `VQ-LUNCH-20260601` — Combo Trưa tháng 6
- `VQ-NEW-20260601` — Khách mới tháng 6
- `VQ-BACK-20260601` — Comeback khách cũ tháng 6
- `VQ-8T3-20260308` — Offer 8/3
- `VQ-1111-20261111` — Sale 11/11

### Quy tắc Voucher
1. Tất cả voucher PHẢI đăng ký trong Google Sheet tab: **Vouchers** trước khi phát
2. Không phát voucher code không có trong hệ thống
3. Voucher không được stack với nhau (trừ khi Owner quyết định)
4. Mỗi voucher có limit sử dụng — AI không tự gia hạn
5. Khi khách claim "không nhận được deal" → chuyển Owner/nhân viên xử lý

---

## OFFER SAFETY RULES

| Quy tắc | Mô tả | Hậu quả nếu vi phạm |
|---------|-------|---------------------|
| KHÔNG tự tạo offer | AI chỉ dùng offer trong file này | Gây nhầm lẫn, thiệt hại tài chính |
| KHÔNG tự sửa giá | Giá luôn từ menu_brain.md/offer_engine.md | Sai lệch định giá, thiệt hại |
| KHÔNG phát voucher chưa đăng ký | Voucher phải có trong Google Sheet | Voucher giả, thiệt hại |
| KHÔNG tự gia hạn | Owner quyết định thời gian offer | Offer chạy sai thời điểm |
| KHÔNG tự xử lý claim | Chuyển Owner/nhân viên | Risk tranh chấp với khách |
| KHÔNG stack offer không được phép | Ghi rõ từng offer có stack được không | Bán lỗ ngoài ý muốn |

---

## Trạng thái Offer (Owner cập nhật)

| Offer ID | Tên | Trạng thái | Ngày cập nhật |
|----------|-----|-----------|--------------|
| OF-01 | Combo Trưa | [FILL: ACTIVE] | [FILL] |
| OF-02 | Combo Cuối Tuần | [FILL] | [FILL] |
| OF-03 | Combo Gia Đình | [FILL] | [FILL] |
| OF-04 | Khách Mới | [FILL] | [FILL] |
| OF-05 | Khách Quay Lại | [FILL] | [FILL] |
| OF-06 | Ngày Mưa | [FILL] | [FILL] |
| OF-07 | Office Lunch | [FILL] | [FILL] |
| OF-08 | Weekend Special | [FILL] | [FILL] |
| OF-09 | Seasonal | [FILL: theo sự kiện] | [FILL] |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.2 — File tạo mới. 9 offer types: Combo Trưa, Cuối Tuần, Gia Đình, Khách Mới, Comeback, Ngày Mưa, Office Lunch, Weekend Special, Seasonal. Upsell/cross-sell logic, voucher system, safety rules. Giá [FILL] — Owner xác nhận. | Claude Code (Builder) |
