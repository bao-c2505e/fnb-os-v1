# Manual Test Input Examples — Vị Cuốn

*Phase 1.6 — Manual Content Pack Runbook*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*3 kịch bản mẫu đã điền sẵn để Owner chạy ngay — không cần suy nghĩ thêm*

---

## Hướng dẫn dùng file này

Chọn một trong 3 kịch bản bên dưới. Copy brief đã điền → paste vào cuối prompt template từ `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md` → gửi cho AI Worker.

Mỗi kịch bản có:
- Brief đầy đủ đã điền
- Điều kiện tiên quyết cần Owner xác nhận
- Kết quả mong đợi
- Câu hỏi kiểm tra sau khi AI trả output

---

## KỊCH BẢN 1 — OFFICE LUNCH

**Tên:** Combo Trưa Văn Phòng — Facebook Monday Push
**Mục đích test:** Kiểm tra PROMO flow + OF-01 + platform Facebook + Segment A

### Điều kiện tiên quyết

Owner cần xác nhận trước khi chạy:

| Field | Cần điền / Xác nhận |
|-------|---------------------|
| Giá Combo Trưa OF-01 | `02_CONTENT_ENGINE/offer_engine.md` → field `Giá` → điền giá thật (ví dụ: 65.000đ) |
| OF-01 status | `02_CONTENT_ENGINE/offer_engine.md` → set `ACTIVE` |
| Địa chỉ | `01_BRAIN/brand_brain.md` → field `Address` → điền địa chỉ thật |
| SĐT | `01_BRAIN/brand_brain.md` → field `Phone` → điền SĐT thật |

**Nếu chưa điền → vẫn chạy được nhưng output sẽ có [FILL] và sẽ là NEEDS_OWNER_REVIEW.**

### Brief Đã Điền

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

objective:      [x] conversion   (kích thích đặt hàng bữa trưa ngay)

target_persona: [x] Segment A    (dân văn phòng, 25–40 tuổi, Vinh)

pillar:         [x] PROMO

angle:          [x] C1  Combo Reveal — Phần ăn giá tốt, reveal đầy đủ combo

content_type:   [x] Post         (Ảnh + caption)

offer_type:     [x] OF-01  Combo Trưa (Thứ 2–6, 11:00–14:00)

tone:           [x] Vui vẻ, hào hứng (phù hợp PROMO)

constraints:
  - Caption tối đa 300 ký tự
  - Đăng lúc 10:30–11:00 thứ 2
  - Có CTA rõ ràng: "đặt ngay" hoặc "ghé quán"
  - Không đề cập đối thủ

owner_notes:
  Muốn nhắc combo trưa đầu tuần. Khách văn phòng khu vực quanh quán.
  Nếu giá OF-01 chưa confirm → dùng [FILL: ~65k] và đánh dấu NEEDS_OWNER_REVIEW.
  Ảnh sẽ dùng: combo trưa chụp thật từ quán (Owner có ảnh).

═══════════════════════════════════════════════════════════
```

### Kết quả Mong đợi từ AI

- Content ID dạng: `VQ-FB-PROMO-20260527-001`
- Caption v1: 150–300 ký tự, có hook "Bữa trưa hôm nay ăn gì?" hoặc tương tự
- Caption v2: <150 ký tự cho Story
- Hook options: 2–3 câu mở đầu khác nhau
- Image brief: close-up combo trưa, ánh sáng tự nhiên, prop mắm nêm
- Offer summary: OF-01 — gồm gì, giá [FILL nếu chưa có], thứ 2–6 11:00–14:00
- Safety flags: dự kiến `PRICE_UNCONFIRMED` và `ADDRESS_UNFILLED` nếu chưa điền
- `approval.status = DRAFT`

### Câu hỏi Kiểm tra sau khi nhận Output

1. Caption có hook bắt đầu bằng câu hỏi hay tình huống gần gũi không?
2. Giọng văn có ấm áp, gần gũi (như nhắn cho bạn) hay cứng nhắc (như quảng cáo)?
3. Offer OF-01 có ghi rõ điều kiện (thứ 2–6, 11:00–14:00) không?
4. Có đúng 3–5 hashtag Facebook không? (nên có #VịCuốn #ĂnVinh)
5. Image brief có dùng ảnh thật không — không đề xuất ảnh stock?
6. `approval.status = DRAFT` — xác nhận ngay trong JSON output.

---

## KỊCH BẢN 2 — RAINY DAY / MẮM NÊM CRAVING

**Tên:** Ngày Mưa + Bún Trộn Mắm Nêm — TikTok BTS
**Mục đích test:** Kiểm tra BTS flow + không có offer + TikTok video script + cảm xúc thời tiết

### Điều kiện tiên quyết

| Field | Cần xác nhận |
|-------|-------------|
| Thời tiết | Chỉ dùng kịch bản này vào ngày thật sự đang mưa (hoặc dùng để test trước) |
| OF-06 status | Không cần bật ngay — kịch bản này KHÔNG dùng OF-06 (thuần BTS, không push offer) |
| Không cần điền giá/địa chỉ | BTS content TikTok không cần giá trong caption |

**Đây là kịch bản dễ nhất để test — ít [FILL] nhất, phù hợp cho lần đầu tiên chạy.**

### Brief Đã Điền

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     2026-05-27
Người tạo brief:    Owner
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon

platform:       [x] TikTok

objective:      [x] engagement   (tăng tương tác, comment, follow)

target_persona: [x] Segment C    (sinh viên + gen Z, 18–26, xem TikTok buổi tối)

pillar:         [x] BTS          (Hậu trường — quy trình pha mắm nêm)

angle:          [x] B3  Quy trình mắm nêm — Pha từng mẻ buổi sáng

content_type:   [x] TikTok Video  (30–45 giây)

offer_type:     [ ] Không có offer

tone:           [x] Năng động, trẻ trung (TikTok)

constraints:
  - Hook xuất hiện trong 3 giây đầu (bắt buộc cho TikTok)
  - Không đề cập giá trong video
  - Caption TikTok tối đa 150 ký tự
  - ASMR element nếu có thể (âm thanh pha mắm, tiếng khuấy)

owner_notes:
  Hôm nay trời mưa — mood ngày mưa = thèm bún trộn mắm nêm. Góc nhìn:
  "Tại sao mắm nêm nhà Vị Cuốn ngon hơn mắm đóng chai?"
  Owner sẽ tự quay theo script. Không cần studio — quay bằng điện thoại được.
  Đây là content BTS thuần — không push offer, không cần giá.

═══════════════════════════════════════════════════════════
```

### Kết quả Mong đợi từ AI

- Content ID dạng: `VQ-TK-BTS-20260527-001`
- Script outline: 4–6 cảnh (30–45 giây), hook trong 3s đầu
  - Cảnh 1 (0–3s): Hook text overlay — câu hỏi gây tò mò
  - Cảnh 2–4: Cảnh pha mắm — tỏi ớt tươi, vắt chanh, khuấy
  - Cảnh 5: Chan thử + reaction
  - Cảnh cuối: CTA nhẹ nhàng
- Caption TikTok: <150 ký tự, không có giá, có 5–10 hashtag
- Safety flags: Chỉ `missing_video_footage` (NOTE level — không phải BLOCKER)
- `approval.status = DRAFT`
- `validation_status = READY_FOR_REVIEW` (vì không có [FILL] quan trọng)

### Câu hỏi Kiểm tra sau khi nhận Output

1. Script cảnh đầu có hook mạnh trong 3 giây không (không phải giới thiệu dài dòng)?
2. Video script có dùng ASMR element (âm thanh pha mắm, khuấy)?
3. Caption TikTok có dưới 150 ký tự không?
4. Có 5–10 hashtag TikTok không?
5. Không có giá trong caption hoặc script không?
6. AI có tự đề xuất ảnh stock hay AI-generated image không? (Không được — phải ảnh thật)

---

## KỊCH BẢN 3 — GROUP / FAMILY COMBO

**Tên:** Combo Gia Đình Cuối Tuần — Facebook + Instagram
**Mục đích test:** Kiểm tra Segment B flow + OF-03 + multi-platform (FB + IG) + PROMO cuối tuần

### Điều kiện tiên quyết

| Field | Cần điền / Xác nhận |
|-------|---------------------|
| Giá Combo Gia Đình OF-03 | `02_CONTENT_ENGINE/offer_engine.md` → điền giá thật |
| Giá mua lẻ tương đương | Để tính "tiết kiệm [Xk] so với mua lẻ" |
| OF-03 status | Set `ACTIVE` |
| Địa chỉ | `01_BRAIN/brand_brain.md` |
| SĐT hoặc link đặt hàng | `01_BRAIN/brand_brain.md` |

**Nếu chưa có → chạy vẫn được, AI sẽ dùng [FILL] và đánh dấu NEEDS_OWNER_REVIEW.**

### Brief Đã Điền

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     2026-05-27
Người tạo brief:    Owner
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon

platform:       [x] Multi (Facebook + Instagram)

objective:      [x] conversion   (gia đình đặt bàn hoặc đặt combo cuối tuần)

target_persona: [x] Segment B    (gia đình trẻ 28–40 tuổi, cuối tuần)

pillar:         [x] PROMO

angle:          [x] C4  Combo Nhóm — Ăn cùng tiết kiệm hơn

content_type:   [x] Post  (Facebook: ảnh + caption dài)
                [x] Post  (Instagram: ảnh đẹp + caption ngắn hơn)

offer_type:     [x] OF-03  Combo Gia Đình (2 người)

tone:           [x] Ấm áp, gần gũi (bữa ăn gia đình, không áp lực)

constraints:
  - Facebook caption 200–350 ký tự
  - Instagram caption < 200 ký tự (phần trước "xem thêm")
  - Không dùng "chỉ còn [X] suất" vì không có giới hạn suất thật
  - Đăng thứ 6 tối hoặc thứ 7 sáng
  - Nhấn vào cảm giác "bữa ăn cùng nhau" — không chỉ là deal

owner_notes:
  Muốn tạo 2 phiên bản caption — 1 cho Facebook (dài hơn, tâm sự hơn),
  1 cho Instagram (ngắn, hashtag nhiều, aesthetic). Ảnh: bàn ăn 2 người
  đầy đủ combo — không gian quán ấm cúng.
  OF-03 chưa có giá chính thức — dùng [FILL: ~130-140k] và NEEDS_OWNER_REVIEW.

═══════════════════════════════════════════════════════════
```

### Kết quả Mong đợi từ AI

- Content ID dạng: `VQ-FB-PROMO-20260527-002` (FB) và `VQ-IG-PROMO-20260527-003` (IG)
- Hoặc một pack multi-platform: `VQ-MULTI-PROMO-20260527-001`
- Facebook caption: 200–350 ký tự, giọng tâm sự, CTA "ghé quán" hoặc "đặt bàn"
- Instagram caption: <200 ký tự, ngắn gọn, hashtag 8–12 tags
- Offer summary: OF-03 gồm 2 phần cuốn + 2 bún trộn + 2 nước, [FILL: giá]
- Image brief: bàn ăn 2 người, combo đầy đủ, ánh sáng tự nhiên
- Safety flags: `PRICE_UNCONFIRMED`, `ADDRESS_UNFILLED`
- `approval.status = DRAFT`
- `validation_status = NEEDS_OWNER_REVIEW`

### Câu hỏi Kiểm tra sau khi nhận Output

1. Caption Facebook có khác caption Instagram không — hay chỉ là copy paste?
2. Giọng văn có tạo cảm giác "ăn cùng gia đình" hay chỉ đang bán deal?
3. Không có "chỉ còn [X] suất" giả tạo không?
4. Image brief có đề xuất thiết bị phức tạp không? (Không được — quán nhỏ)
5. Số hashtag Instagram có trong ngưỡng 5–15 không?
6. Đề xuất giờ đăng có đúng (thứ 6 tối / thứ 7 sáng) không?

---

## So sánh 3 Kịch bản

| | Kịch bản 1 | Kịch bản 2 | Kịch bản 3 |
|-|-----------|-----------|-----------|
| Platform | Facebook | TikTok | Facebook + Instagram |
| Pillar | PROMO | BTS | PROMO |
| Offer | OF-01 (Combo Trưa) | Không | OF-03 (Gia Đình) |
| [FILL] quan trọng | Giá + Địa chỉ + SĐT | Không có | Giá + Địa chỉ + SĐT |
| Dự kiến status | NEEDS_OWNER_REVIEW | READY_FOR_REVIEW | NEEDS_OWNER_REVIEW |
| Độ khó cho lần đầu | Trung bình | Dễ nhất | Khó hơn (multi-platform) |
| Cần media từ quán | Ảnh combo trưa | Video pha mắm nêm | Ảnh bàn ăn 2 người |

**Gợi ý cho lần đầu:** Chạy **Kịch bản 2** (TikTok BTS) vì ít [FILL] nhất và sẽ cho READY_FOR_REVIEW ngay nếu AI làm đúng.

---

## Ghi Lại Kết Quả Test

Sau khi chạy xong từng kịch bản, điền vào đây:

| Kịch bản | Ngày chạy | AI Worker | Content ID | Validation Status | Owner Decision | Ghi chú |
|---------|---------|----------|-----------|-----------------|--------------|---------|
| 1 — Office Lunch | | | | | | |
| 2 — Rainy Day / Mắm Nêm | | | | | | |
| 3 — Group/Family Combo | | | | | | |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.6 — File tạo mới. 3 kịch bản test mẫu đầy đủ: office lunch (Facebook PROMO), rainy day BTS (TikTok), family combo (multi-platform PROMO). | Claude Code (Builder) |
