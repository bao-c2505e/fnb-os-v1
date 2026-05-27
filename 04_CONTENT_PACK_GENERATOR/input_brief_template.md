# Input Brief Template — Content Pack Generator

*Phase 1.4 — Draft Content Pack Generator Schema*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Dùng cho: Owner hoặc ChatGPT điền khi muốn giao lệnh tạo Content Pack*

---

## Hướng dẫn

1. Copy toàn bộ **BRIEF FORM** bên dưới
2. Điền tất cả trường REQUIRED
3. Điền các trường OPTIONAL nếu có yêu cầu đặc biệt
4. Gửi brief đã điền cho AI Worker (Claude Code / Codex / Gemini)
5. AI Worker sẽ chạy `content_pack_prompt_template.md` với brief này

---

## BRIEF FORM

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     ____________________
Người tạo brief:    ____________________  (Owner / ChatGPT / v.v.)
Số pack cần tạo:    ____________________  (mặc định: 1)
═══════════════════════════════════════════════════════════

─── TRƯỜNG BẮT BUỘC (REQUIRED) ──────────────────────────

brand:
  [ ] Vi Cuon                          ← Chọn (chỉ có 1 option)

platform:
  [ ] Facebook
  [ ] TikTok
  [ ] Instagram
  [ ] Zalo OA
  [ ] Multi (Facebook + TikTok)

objective:
  [ ] awareness      (tăng độ nhận biết thương hiệu)
  [ ] engagement     (tăng tương tác, comment, share)
  [ ] conversion     (kích thích đặt hàng ngay)
  [ ] retention      (giữ chân khách cũ)
  [ ] education      (giáo dục khách về sản phẩm/thương hiệu)

target_persona:
  [ ] Segment A      (dân văn phòng, 22–35 tuổi, bữa trưa)
  [ ] Segment B      (gia đình trẻ, 28–40 tuổi, cuối tuần)
  [ ] Segment C      (sinh viên, 18–24 tuổi, giá nhạy)
  [ ] All            (nhắm tất cả segment)

pillar:
  [ ] PROD           (Sản phẩm — showcase món ăn)
  [ ] BTS            (Hậu trường — quy trình, con người)
  [ ] PROMO          (Khuyến mãi — offer, deal, combo)
  [ ] STORY          (Câu chuyện — giáo dục, nguồn gốc)
  [ ] COM            (Cộng đồng — khách hàng, repost, UGC)
  [ ] SEASON         (Mùa vụ — thời tiết, lễ hội)

angle:
  Nhập mã angle (xem content_angles.md) HOẶC chọn AUTO:
  [ ] AUTO           (AI tự chọn angle phù hợp nhất)
  [ ] A1  Hero Shot — Một ảnh/video duy nhất, để hình tự nói
  [ ] A2  Từng lớp — Mô tả giác quan từng thành phần
  [ ] A3  Spotlight Mắm Nêm — USP nước chấm tự pha
  [ ] A4  Menu Highlight — Menu hôm nay / tuần này
  [ ] A5  Before/After — Nguyên liệu → Thành phẩm
  [ ] A6  Combo đầy đủ — Bày toàn bộ combo, show giá trị
  [ ] B1  5 giờ sáng — Chuẩn bị đầu ngày
  [ ] B2  Lửa Lu — Heo nướng lu truyền thống
  [ ] B3  Quy trình mắm nêm — Pha từng mẻ
  [ ] B4  Rau sống — Tươi thật sự
  [ ] B5  Nhân vật quán — Con người thương hiệu
  [ ] C1  Combo Reveal — Phần ăn giá tốt
  [ ] C2  Đồng hồ đếm ngược — Deal khung giờ
  [ ] C3  Khách mới — Lần đầu tiên
  [ ] C4  Combo Nhóm — Ăn cùng tiết kiệm hơn
  [ ] C5  Thời tiết & Deal — Relevance theo ngày
  [ ] D1  Bạn có biết? — Fun fact ẩm thực
  [ ] D2  Lịch sử / Nguồn gốc — Đặc sản miền Trung
  [ ] D3  Giải đáp thắc mắc — FAQ
  [ ] D4  Tại sao nhà mình làm vậy — Transparency
  [ ] D5  Câu chuyện quán — Origin story
  [ ] E1  Repost khách — Social proof
  [ ] E2  Poll / Hỏi ý kiến — Engagement
  [ ] E3  Milestone — Cột mốc cảm ơn
  [ ] E4  UGC Call — Kêu gọi tag quán

content_type:
  [ ] Post           (Ảnh + caption — Facebook/IG)
  [ ] Reel           (Video ngắn — Facebook/IG)
  [ ] Story          (Story 24h — Facebook/IG/Zalo)
  [ ] Carousel       (Nhiều ảnh — Facebook/IG)
  [ ] TikTok Video   (Video — TikTok)
  [ ] Zalo Broadcast (Broadcast message — Zalo OA)
  [ ] Short Video    (Video ngắn chung)

─── TRƯỜNG TÙY CHỌN (OPTIONAL) ──────────────────────────

offer_type:
  [ ] Không có offer (null)
  [ ] OF-01  Combo Trưa (T2–T6, 11:00–14:00)
  [ ] OF-02  Combo Cuối Tuần (T7–CN)
  [ ] OF-03  Combo Gia Đình (2 người)
  [ ] OF-04  Ưu Đãi Khách Mới
  [ ] OF-05  Khách Quay Lại
  [ ] OF-06  Deal Ngày Mưa (chỉ khi trời mưa thật)
  [ ] OF-07  Order Nhóm Văn Phòng
  [ ] OF-08  Weekend Special Upgrade
  [ ] OF-09  Offer Sự Kiện (điền tên sự kiện bên dưới)
  Tên sự kiện (nếu OF-09): ____________________

tone:
  [ ] Mặc định Brand Voice (ấm áp, gần gũi)
  [ ] Vui vẻ, hào hứng (phù hợp PROMO)
  [ ] Giáo dục nhẹ nhàng (phù hợp STORY)
  [ ] Năng động, trẻ trung (phù hợp TikTok)
  [ ] Khác: ____________________

constraints:
  (Các ràng buộc đặc biệt — gạch đầu dòng mỗi ràng buộc)
  -
  -
  -

owner_notes:
  (Ghi chú tự do — ví dụ: "tuần này trời mưa nhiều", "tập trung món heo quay",
   "đừng đề cập giá vì chưa có deal chính thức", v.v.)

  ____________________________________________________________________
  ____________________________________________________________________
  ____________________________________________________________________

═══════════════════════════════════════════════════════════
SAU KHI ĐIỀN XONG:
- Gửi toàn bộ brief này cho AI Worker
- AI Worker chạy content_pack_prompt_template.md
- Output: Content Pack ở trạng thái DRAFT
- Owner review → APPROVED / REVISION_REQUESTED
═══════════════════════════════════════════════════════════
```

---

## Ví dụ Brief đã điền — Bữa Trưa Văn Phòng

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     2026-05-27
Người tạo brief:    Owner
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon
platform:       [x] Facebook
objective:      [x] conversion
target_persona: [x] Segment A  (dân văn phòng)
pillar:         [x] PROMO
angle:          [x] C1  Combo Reveal
content_type:   [x] Post
offer_type:     [x] OF-01  Combo Trưa
tone:           [x] Vui vẻ, hào hứng
constraints:
  - Caption tối đa 300 ký tự
  - Đăng lúc 11:00 thứ 2
owner_notes:
  Muốn nhắc combo trưa đầu tuần. Khách văn phòng gần quán.
  Chưa có giá chính thức — dùng [FILL].
═══════════════════════════════════════════════════════════
```

---

## Ví dụ Brief đã điền — Ngày Mưa Mắm Nêm

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     2026-05-27
Người tạo brief:    Owner
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon
platform:       [x] Facebook
objective:      [x] engagement
target_persona: [x] All
pillar:         [x] SEASON
angle:          [x] C5  Thời tiết & Deal
content_type:   [x] Post
offer_type:     [x] OF-06  Deal Ngày Mưa
tone:           [x] Ấm áp, gần gũi
constraints:
  - Nhấn vào cảm giác ấm nóng ngày mưa
  - Không đặt giá
owner_notes:
  Hôm nay Vinh đang mưa lớn. Muốn post nhanh gợi cảm
  giác bún trộn nóng. OF-06 chưa active — cần Owner xác nhận.
═══════════════════════════════════════════════════════════
```

---

## Ví dụ Brief đã điền — Combo Gia Đình Cuối Tuần

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     2026-05-27
Người tạo brief:    ChatGPT (Chief Architect)
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon
platform:       [x] Facebook
objective:      [x] conversion
target_persona: [x] Segment B  (gia đình trẻ)
pillar:         [x] PROMO
angle:          [x] C4  Combo Nhóm
content_type:   [x] Post
offer_type:     [x] OF-03  Combo Gia Đình
tone:           [x] Ấm áp, gần gũi
constraints:
  - Nhấn vào bữa ăn gia đình cuối tuần
  - Đăng thứ 5 tối hoặc thứ 6 sáng để nhắc cuối tuần
owner_notes:
  Muốn nhắm gia đình 2 người lớn + trẻ em. Hình ảnh
  bàn ăn ấm cúng. OF-03 chưa có giá — dùng [FILL].
═══════════════════════════════════════════════════════════
```

---

## Câu hỏi thường gặp

**Q: Tôi có thể điền nhiều platform cùng lúc không?**
A: Chọn `Multi` nếu muốn một brief cho nhiều platform. AI sẽ tạo caption variants cho từng platform. Tuy nhiên, mỗi platform thường có yêu cầu riêng — tốt nhất là 1 brief = 1 platform.

**Q: Nếu tôi không biết chọn angle nào?**
A: Chọn `AUTO`. AI sẽ tự chọn angle phù hợp nhất với pillar + platform + objective và ghi lý do chọn vào output.

**Q: Tôi có thể yêu cầu nhiều Content Pack trong 1 brief không?**
A: Có — điền `Số pack cần tạo: [N]` và AI sẽ tạo N pack. Tuy nhiên, khuyến nghị không quá 3 pack/lần để đảm bảo chất lượng.

**Q: Offer chưa active thì sao?**
A: Vẫn điền offer_type. AI sẽ đánh dấu `[OWNER_CONFIRM: offer status]` và nhắc Owner xác nhận trước khi đăng.

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — File tạo mới. Input Brief Template với form đầy đủ, 3 ví dụ brief đã điền, FAQ. | Claude Code (Builder) |
