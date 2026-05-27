# Sample Content Queue — Vị Cuốn

*Phase 1.5 — Content Pack Validation & Sample Queue*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*10 mục queue mẫu đại diện cho các segment và use case chính của Vị Cuốn*

---

## Tổng quan Queue

| # | Content ID | Category | Platform | Persona | Offer | Validation Status |
|---|-----------|---------|---------|---------|-------|------------------|
| 1 | VQ-FB-PROMO-20260527-001 | Office Lunch | Facebook | Segment A | OF-01 | NEEDS_OWNER_REVIEW |
| 2 | VQ-TK-PROD-20260527-002 | Office Lunch | TikTok | Segment A | — | NEEDS_OWNER_REVIEW |
| 3 | VQ-ZL-PROMO-20260527-003 | Office Lunch | Zalo OA | Segment A | OF-07 | NEEDS_OWNER_REVIEW |
| 4 | VQ-FB-PROMO-20260527-004 | Rainy Day | Facebook | Segment A+C | OF-06 | NEEDS_OWNER_REVIEW |
| 5 | VQ-TK-BTS-20260527-005 | Mắm Nêm Craving | TikTok | Segment C | — | READY_FOR_REVIEW |
| 6 | VQ-FB-PROMO-20260527-006 | Group/Family Combo | Facebook | Segment B | OF-03 | NEEDS_OWNER_REVIEW |
| 7 | VQ-IG-PROD-20260527-007 | Group/Family Combo | Instagram | Segment B | OF-02 | NEEDS_OWNER_REVIEW |
| 8 | VQ-FB-PROMO-20260527-008 | New Customer | Facebook | New | OF-04 | NEEDS_OWNER_REVIEW |
| 9 | VQ-ZL-PROMO-20260527-009 | Comeback Customer | Zalo OA | Lapsed | OF-05 | NEEDS_OWNER_REVIEW |
| 10 | VQ-FB-SEASON-20260527-010 | Weekend/Seasonal | Facebook | Segment B+C | OF-08 | NEEDS_OWNER_REVIEW |

---

## NHÓM 1 — OFFICE LUNCH (3 mục)

---

### ITEM 01

```yaml
content_id: VQ-FB-PROMO-20260527-001
category: office_lunch
platform: Facebook
persona: Segment A — Dân văn phòng (25–40 tuổi, Vinh, bữa trưa)
pillar: PROMO
angle: "Combo trưa nhanh, ngon, no — giải quyết bài toán 'trưa nay ăn gì'"
offer_type: OF-01 — Combo Trưa Vị Cuốn
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Photo + Caption
posting_time_suggestion: Thứ 2 hoặc Thứ 4, 10:30–11:00

caption_draft_v1: |
  Bữa trưa hôm nay chưa biết ăn gì?
  
  Combo Trưa Vị Cuốn: bánh tráng cuốn thịt heo + bún trộn mắm nêm + nước chanh tươi.
  No căng bụng — chỉ [FILL: ~65.000đ].
  
  Thứ 2–6, 11:00–14:00. Ghé Vị Cuốn tại [FILL: địa chỉ chi tiết] hoặc đặt qua [FILL: ShopeeFood/GrabFood].
  
  #VịCuốn #ĂnVinh #ComboTrưa #BánhTrángCuốn #ViNghệAn

caption_draft_v2: |
  12 giờ trưa. Vẫn chưa đặt cơm. Quen rồi 😄
  
  Để Vị Cuốn lo cho — Combo Trưa [FILL: ~65k] gồm:
  ✓ Bánh tráng cuốn thịt heo
  ✓ Bún trộn mắm nêm
  ✓ Nước chanh tươi
  
  Đặt qua [FILL: link/SĐT]. Thứ 2–6, trước 14:00.
  
  #VịCuốn #ĂnVinh #BữaTrưaVinh

safety_flags:
  - PRICE_UNCONFIRMED: "Giá ~65k chưa được Owner xác nhận trong offer_engine.md"
  - ADDRESS_UNFILLED: "Địa chỉ chi tiết chưa có trong brand_brain.md"
  - OFFER_UNCONFIRMED: "OF-01 status chưa được set ACTIVE trong offer_engine.md"

missing_fields:
  - price_combo_trua (OF-01)
  - address_detail
  - phone_or_delivery_link
  - offer_status_OF-01

next_action: |
  Owner điền: (1) giá Combo Trưa vào offer_engine.md, (2) địa chỉ chi tiết vào brand_brain.md,
  (3) set OF-01 = ACTIVE. Builder update caption và chuyển READY_FOR_REVIEW.

assumptions:
  - Giá ~65k dựa trên price range 60-80k/người trong brand_brain.md
  - Platform Facebook phù hợp cho Segment A theo content_pillars.md
  - Combo Trưa là OF-01 từ offer_engine.md
```

---

### ITEM 02

```yaml
content_id: VQ-TK-PROD-20260527-002
category: office_lunch
platform: TikTok
persona: Segment A — Dân văn phòng (25–35 tuổi, xem TikTok giờ nghỉ trưa)
pillar: PROD
angle: "ASMR cuốn — hook thị giác và âm thanh kéo người đang lăn TikTok dừng lại"
offer_type: N/A (Bài PROD — không push offer, chỉ showcase sản phẩm)
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Short Video 30–45s (TikTok Reel)
posting_time_suggestion: Thứ 4 hoặc Thứ 5, 19:00–20:00 (xem TikTok sau giờ làm)

script_outline: |
  [0–3s] HOOK: Cảnh close-up tay cuốn bánh tráng — âm thanh giòn của bánh tráng
  [3–10s] Thịt heo mềm, da giòn vàng, thêm rau sống xanh tươi vào cuốn
  [10–20s] Chan mắm nêm — màu đỏ cam — gần camera
  [20–30s] Cắn miếng đầu tiên — reaction tự nhiên / cut sang bàn ăn đầy đủ
  [30–40s] Text overlay: "Vị Cuốn — [FILL: địa chỉ ngắn]" + nhạc nền vui tươi
  [40–45s] CTA: "Địa chỉ trong bio / Comment 'MENU' để xem thực đơn"

caption_draft: |
  POV: đang nghĩ bữa trưa ăn gì thì thấy cái này 🥢
  
  Bánh tráng cuốn thịt heo + mắm nêm tự pha nhà mình — cuốn tay, ăn tươi ngay tại bàn.
  
  📍 Vị Cuốn — Vinh, Nghệ An
  👇 Comment MENU để xem thực đơn đầy đủ!
  
  #VịCuốn #ĂnVinh #BánhTrángCuốn #FoodTikTok #ĂnVặtVinh #ASMR #ViNghệAn #FoodVlog #MonNgon

safety_flags:
  - ADDRESS_UNFILLED: "Địa chỉ ngắn trong text overlay chưa có"

missing_fields:
  - address_short (cho text overlay video)
  - actual_video_footage (cần Owner quay — AI không tự tạo video)

next_action: |
  Owner quay footage theo script outline. Builder review caption sau khi có địa chỉ.
  Sau đó READY_FOR_REVIEW.

assumptions:
  - Video phải do Owner/nhân viên quay thật — Builder chỉ cung cấp script
  - ASMR angle phù hợp TikTok giờ trưa theo content_pillars.md TikTok guidelines
  - Caption TikTok ≤150 ký tự chính (phần đầu trước "xem thêm")
```

---

### ITEM 03

```yaml
content_id: VQ-ZL-PROMO-20260527-003
category: office_lunch
platform: Zalo OA
persona: Segment A — Dân văn phòng đã follow Zalo OA (khách cũ / khách đăng ký nhận deal)
pillar: PROMO
angle: "Broadcast ngắn, thực tế, nhắc deal trưa trước giờ ăn"
offer_type: OF-07 — Order Nhóm Văn Phòng (đặt nhóm ≥3 người)
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Zalo OA Broadcast Message (text + ảnh)
posting_time_suggestion: Thứ 2 hoặc Thứ 4, 10:00–10:30

message_draft_v1: |
  🍜 Bữa trưa hôm nay cả văn phòng ăn gì rồi?
  
  Order nhóm từ 3 người — Vị Cuốn có deal đặc biệt:
  [OWNER_CONFIRM: mô tả ưu đãi OF-07 cụ thể — giao miễn phí / giảm X% / tặng đồ uống]
  
  Đặt trước 11:30 qua: [FILL: SĐT] / [FILL: link Zalo chat]
  Giao tận nơi hoặc ghé lấy: [FILL: địa chỉ]

message_draft_v2: |
  Văn phòng bạn mấy người? 🙋‍♀️
  
  Đặt nhóm ≥3 phần tại Vị Cuốn — [OWNER_CONFIRM: ưu đãi cụ thể].
  
  📞 [FILL: SĐT] | Trước 11:30 | Thứ 2–6

safety_flags:
  - OFFER_UNCONFIRMED: "OF-07 ưu đãi cụ thể chưa được Owner xác định"
  - ADDRESS_UNFILLED: "Địa chỉ và SĐT chưa có"

missing_fields:
  - offer_detail_OF-07 (ưu đãi cụ thể: giao miễn phí hay giảm %)
  - phone_number
  - zalo_chat_link
  - address_detail

next_action: |
  Owner xác nhận ưu đãi OF-07 trong offer_engine.md + điền SĐT + địa chỉ.
  Sau đó Builder finalize message và READY_FOR_REVIEW.

assumptions:
  - Zalo OA dùng format text ngắn gọn theo content_pillars.md — không dùng hashtag
  - OF-07 nhắm nhóm văn phòng ≥3 người theo offer_engine.md
```

---

## NHÓM 2 — RAINY DAY / MẮM NÊM CRAVING (2 mục)

---

### ITEM 04

```yaml
content_id: VQ-FB-PROMO-20260527-004
category: rainy_day
platform: Facebook
persona: Segment A + Segment C — Dân văn phòng + sinh viên đang ở nhà ngày mưa
pillar: PROMO (kết hợp SEASON)
angle: "Ngày mưa Vinh = bún trộn mắm nêm nóng — emotional trigger thời tiết"
offer_type: OF-06 — Deal Ngày Mưa (chỉ bật khi trời mưa thật)
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Photo + Caption (đăng nhanh khi trời mưa)
posting_time_suggestion: Ngày mưa — đăng trong vòng 30 phút sau khi Owner kích hoạt OF-06

caption_draft_v1: |
  Vinh đang mưa... 🌧
  
  Những lúc này chỉ muốn ngồi yên với một tô bún trộn mắm nêm nóng.
  
  Deal ngày mưa hôm nay: [OWNER_CONFIRM: mô tả offer OF-06 — giao miễn phí / giảm X% / tặng nước]
  
  Đặt ngay — giao tận nơi: [FILL: SĐT hoặc link đặt hàng]
  
  #VịCuốn #ĂnVinh #NgàyMưa #BúnTrộnMắmNêm #ViNghệAn

caption_draft_v2: |
  Mưa Vinh rồi — ở nhà ăn gì bạn ơi?
  
  Bún trộn mắm nêm + bánh tráng cuốn thịt heo giao tận cửa.
  Hôm nay: [OWNER_CONFIRM: offer OF-06]. Đặt: [FILL: SĐT]
  
  #VịCuốn #ĂnVinh #MưaVinh

safety_flags:
  - OFFER_UNCONFIRMED: "OF-06 phải Owner kích hoạt thủ công — không tự đăng"
  - ADDRESS_UNFILLED: "SĐT / link đặt hàng chưa có"

missing_fields:
  - offer_detail_OF-06 (Owner quyết định form ưu đãi mỗi ngày mưa)
  - phone_or_order_link

next_action: |
  QUAN TRỌNG: Bài này chỉ đăng khi Owner thấy trời mưa và bật OF-06 thủ công.
  Builder chuẩn bị sẵn 2 phiên bản. Owner chọn + điền offer cụ thể + post.

assumptions:
  - OF-06 là offer linh hoạt — Owner quyết định form ưu đãi mỗi ngày kích hoạt
  - Không tự đăng khi không có lệnh Owner — theo offer_engine.md "Quy tắc: KHÔNG tự đăng"
```

---

### ITEM 05

```yaml
content_id: VQ-TK-BTS-20260527-005
category: mam_nem_craving
platform: TikTok
persona: Segment C — Sinh viên (18–24) + ai đang thèm đặc sản Nghệ An
pillar: BTS (Behind the Scenes)
angle: "Quy trình pha mắm nêm tự pha — USP khác biệt của Vị Cuốn, tạo tò mò và thèm ăn"
offer_type: N/A (BTS content — không push offer)
draft_status: DRAFT
validation_status: READY_FOR_REVIEW
content_type: Short Video 45–60s (TikTok — format "Bạn có biết không?")
posting_time_suggestion: Thứ 3 hoặc Thứ 5, 20:00–21:00

script_outline: |
  [0–3s] HOOK TEXT: "Tại sao mắm nêm Vị Cuốn ngon hơn mắm đóng chai?"
  [3–15s] Cảnh pha mắm: đổ mắm nêm nguyên chất → vắt chanh → thêm tỏi ớt tươi giã
  [15–30s] Khuấy đều — màu đỏ cam đẹp — close-up bát mắm nêm thành phẩm
  [30–45s] Chấm thử — thịt heo cuốn bánh tráng nhúng vào mắm — reaction tự nhiên
  [45–55s] Text: "Pha mỗi buổi sáng — không đóng chai, không bảo quản qua đêm"
  [55–60s] CTA: "Follow để xem thêm bếp nhà Vị Cuốn"

caption_draft: |
  Mắm nêm nhà mình pha mỗi sáng — không đóng hộp, không để qua đêm 🫙
  
  Tỏi ớt tươi giã tay, chanh vắt ngay lúc pha — đó là lý do bạn thấy khác.
  
  📍 Vị Cuốn — Vinh, Nghệ An
  💬 Hỏi công thức thì mình bí mật thôi nha 😄
  
  #VịCuốn #ĂnVinh #MắmNêm #BánhTrángCuốn #BếpViệt #FoodTikTok #ViNghệAn #HậuTrường #MonNgon

safety_flags: []

missing_fields:
  - actual_video_footage (Owner/nhân viên quay thật)

next_action: |
  Owner quay footage theo script outline. Caption đã đủ — không có [FILL] quan trọng.
  Sau khi có video → READY_FOR_REVIEW và vào Approval Pipeline.
  
  GHI CHÚ: Đây là item DUY NHẤT trong queue có validation_status = READY_FOR_REVIEW
  vì caption không có [FILL] quan trọng và BTS content không cần giá/địa chỉ trong caption.

assumptions:
  - BTS content không cần giá trong caption — đúng theo content_pillars.md Pillar 2
  - Caption TikTok phần đầu < 150 ký tự là đủ để "xem thêm"
  - Địa chỉ đặt trong profile bio TikTok — không cần trong caption
  - Script dựa trên brand_brain.md USP số 2: "Mắm nêm tự pha theo công thức riêng"
```

---

## NHÓM 3 — GROUP / FAMILY COMBO (2 mục)

---

### ITEM 06

```yaml
content_id: VQ-FB-PROMO-20260527-006
category: group_family_combo
platform: Facebook
persona: Segment B — Gia đình trẻ có con nhỏ (28–40 tuổi, tìm bữa cuối tuần ngon)
pillar: PROMO
angle: "Combo Gia Đình 2 người — tiết kiệm, no đủ, cùng nhau ăn ngon cuối tuần"
offer_type: OF-03 — Combo Gia Đình (2 người)
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Photo (bàn ăn 2 người đầy đủ) + Caption
posting_time_suggestion: Thứ 6, 17:00–19:00 (chuẩn bị tâm lý cuối tuần)

caption_draft_v1: |
  Cuối tuần rồi — bữa tối cả hai ăn gì?
  
  Combo Gia Đình Vị Cuốn (2 người):
  → 2 phần bánh tráng cuốn thịt heo
  → 2 bún trộn mắm nêm
  → 2 nước
  Chỉ [FILL: ~130–140k] — tiết kiệm [FILL: X.000đ] so với gọi lẻ.
  
  Ghé quán: [FILL: địa chỉ] | Đặt qua: [FILL: SĐT/ShopeeFood]
  
  #VịCuốn #ĂnVinh #ComboGiaDình #CuốiTuần #BánhTrángCuốn

caption_draft_v2: |
  Hai người — một bữa ngon — không lo tính tiền.
  
  Combo Gia Đình: 2 phần cuốn + 2 bún trộn + 2 nước.
  [FILL: giá combo 2 người]. Thứ 7–CN cả ngày.
  
  📍 [FILL: địa chỉ] | 📞 [FILL: SĐT]
  
  #VịCuốn #ĂnVinh #CuốiTuần

safety_flags:
  - PRICE_UNCONFIRMED: "Giá Combo Gia Đình OF-03 chưa xác nhận"
  - ADDRESS_UNFILLED: "Địa chỉ và SĐT chưa có"
  - OFFER_UNCONFIRMED: "OF-03 status chưa set ACTIVE"

missing_fields:
  - price_combo_gia_dinh (OF-03)
  - price_le_tuong_duong (để tính tiết kiệm)
  - address_detail
  - phone_number
  - offer_status_OF-03

next_action: |
  Owner điền giá OF-03 + địa chỉ + SĐT + set OF-03 ACTIVE.
  Builder finalize caption, chuyển READY_FOR_REVIEW.
```

---

### ITEM 07

```yaml
content_id: VQ-IG-PROD-20260527-007
category: group_family_combo
platform: Instagram
persona: Segment B — Gia đình trẻ + Segment C — nhóm bạn (25–35 tuổi, Instagram-active)
pillar: PROD
angle: "Mâm ăn nhóm bạn / gia đình đẹp — aesthetic, ngon mắt, gợi cảm giác ăn cùng nhau"
offer_type: OF-02 — Combo Cuối Tuần
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Carousel (3–5 ảnh: mâm đầy đủ → từng món close-up → mắm nêm tự pha)
posting_time_suggestion: Thứ 7, 10:00–11:00

caption_draft: |
  Bữa cuối tuần đúng nghĩa — cả nhóm quây quần, cuốn tay, chấm mắm nêm. 🥢
  
  Combo Cuối Tuần Vị Cuốn gồm: bánh tráng cuốn + bún trộn + 2 gỏi cuốn tôm thịt + nước.
  [FILL: giá combo cuối tuần] / người. Thứ 7–CN cả ngày.
  
  Ghé tại [FILL: địa chỉ] hoặc đặt qua [FILL: link].
  
  #VịCuốn #ĂnVinh #ComboNhóm #CuốiTuần #BánhTrángCuốn #GỏiCuốn #ĂnViệt #ViNghệAn #FoodVinh

safety_flags:
  - PRICE_UNCONFIRMED: "Giá OF-02 chưa xác nhận"
  - ADDRESS_UNFILLED: "Địa chỉ chưa có"
  - OFFER_UNCONFIRMED: "OF-02 status chưa set ACTIVE"

missing_fields:
  - price_combo_cuoi_tuan (OF-02)
  - address_detail
  - delivery_link
  - offer_status_OF-02
  - actual_carousel_photos (Owner chụp mâm ăn thật)

next_action: |
  Owner chụp 3–5 ảnh mâm ăn đẹp + điền giá OF-02 + địa chỉ.
  Builder hoàn thiện carousel captions, chuyển READY_FOR_REVIEW.

assumptions:
  - Carousel phù hợp Instagram theo content_pillars.md — "Feed ảnh đẹp, Saves rất cao"
  - PROD pillar không cần caption push mạnh offer — chỉ mention nhẹ
  - Instagram hashtag đúng ngưỡng 5–15 (đang có 9 hashtag)
```

---

## NHÓM 4 — NEW CUSTOMER (1 mục)

---

### ITEM 08

```yaml
content_id: VQ-FB-PROMO-20260527-008
category: new_customer
platform: Facebook
persona: Khách mới — chưa từng đặt Vị Cuốn, đang lăn Facebook feed giờ trưa / buổi tối
pillar: PROMO
angle: "Lần đầu thử — không rủi ro, có deal, dễ đặt"
offer_type: OF-04 — Ưu Đãi Lần Đầu
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Photo + Caption (Hero shot của combo trưa đẹp nhất)
posting_time_suggestion: Thứ 3 hoặc Thứ 5, 11:00 hoặc 19:00

caption_draft_v1: |
  Chưa thử Vị Cuốn bao giờ?
  
  Lần đầu ghé — riêng bạn có deal đặc biệt:
  [OWNER_CONFIRM: mô tả offer OF-04 — giảm X% / giảm Xk / tặng gì]
  Mã: [FILL: VQ-NEW-YYYYMMDD] | Hết hạn: [FILL: ngày]
  
  Đặt qua [FILL: ShopeeFood / GrabFood / SĐT].
  Một lần thử — để biết tại sao mắm nêm nhà mình khác.
  
  #VịCuốn #ĂnVinh #KháchMới #BánhTrángCuốn #ViNghệAn #MonNgon

caption_draft_v2: |
  Lần đầu tiên — nên thử gì ở Vị Cuốn?
  
  👉 Bánh tráng cuốn thịt heo + mắm nêm tự pha — combo cơ bản mà ngon nhất nhà mình.
  
  Deal khách mới: [OWNER_CONFIRM: offer OF-04].
  Mã [FILL: code] — áp dụng qua [FILL: nền tảng đặt hàng].
  
  #VịCuốn #ĂnVinh #KhácnMới

safety_flags:
  - OFFER_UNCONFIRMED: "OF-04 chưa được Owner xác nhận form ưu đãi + tạo voucher code"
  - PRICE_UNCONFIRMED: "Không nên mention giá trong bài khách mới nếu giá chưa confirm"

missing_fields:
  - offer_detail_OF-04 (% hoặc Xk hoặc tặng gì)
  - voucher_code_NEW (phải đăng ký trong Voucher System trước)
  - voucher_expiry_date
  - order_platform_link (ShopeeFood/GrabFood link cụ thể)

next_action: |
  QUAN TRỌNG: Owner tạo voucher code theo format VQ-NEW-[YYYYMMDD] trong Google Sheet.
  Owner xác nhận form ưu đãi OF-04. Builder điền code + finalize caption.
  
  Không được phát voucher code trước khi Owner đăng ký trong hệ thống
  (theo offer_engine.md Voucher Safety Rules).

assumptions:
  - OF-04 là offer 1 lần / tài khoản / SĐT theo offer_engine.md
  - Bài này target via boosted post (nếu Owner muốn) — không auto-boost
```

---

## NHÓM 5 — COMEBACK CUSTOMER (1 mục)

---

### ITEM 09

```yaml
content_id: VQ-ZL-PROMO-20260527-009
category: comeback_customer
platform: Zalo OA
persona: Khách cũ — đã từng đặt nhưng không ghé trong 30–45 ngày (At-Risk / Lapsed segment)
pillar: PROMO (CRM-triggered)
angle: "Nhắc nhở ấm áp, không áp lực — 'Nhớ bạn rồi' — kéo khách quay lại tự nhiên"
offer_type: OF-05 — Nhớ Bạn Rồi! (Comeback Offer)
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Zalo OA Personal Message / Broadcast có cá nhân hóa
posting_time_suggestion: Thứ 2 hoặc Thứ 4, 10:00–10:30 (batch gửi)

message_draft_v1: |
  Lâu rồi không ghé Vị Cuốn rồi bạn ơi 🥲
  
  Hôm nay nhà mình có deal dành riêng cho bạn:
  [OWNER_CONFIRM: mô tả offer OF-05 — voucher % hoặc tặng topping / đồ uống]
  
  Mã: [FILL: VQ-BACK-YYYYMMDD] | Hết hạn: [FILL: ngày]
  
  Ghé lại nhen! Mắm nêm vẫn pha mỗi sáng, heo vẫn nướng lu mỗi ngày như cũ 😄
  📞 [FILL: SĐT / Zalo]

message_draft_v2: |
  Vị Cuốn nhớ bạn! 👋
  
  Đã [FILL: X ngày] chưa thấy bạn ghé — hôm nay có deal comeback:
  [OWNER_CONFIRM: offer OF-05]
  
  Mã: [FILL: code] | Hết hạn: [FILL: ngày]
  Đặt: [FILL: SĐT]

safety_flags:
  - OFFER_UNCONFIRMED: "OF-05 form ưu đãi chưa xác nhận — voucher % hay tặng gì?"
  - PRICE_UNCONFIRMED: "Phụ thuộc form OF-05"

missing_fields:
  - offer_detail_OF-05
  - voucher_code_BACK (đăng ký trong Voucher System)
  - voucher_expiry_date
  - phone_or_zalo_link
  - days_since_last_order (dữ liệu CRM — Owner có hệ thống này không?)

next_action: |
  QUAN TRỌNG: Gửi Zalo OA message cần:
  (1) Owner xác nhận OF-05 form ưu đãi
  (2) Owner tạo voucher code VQ-BACK-[YYYYMMDD] trong Voucher System
  (3) Owner có danh sách khách lapsed (CRM / Google Sheet)
  
  Không gửi tự động — Owner gửi thủ công hoặc qua Zalo OA broadcast.

assumptions:
  - Danh sách khách lapsed được Owner quản lý thủ công (Google Sheet) — CRM chưa tự động
  - "X ngày" trong v2 cần Owner điền số thực tế
  - Tone "Nhớ bạn rồi" phù hợp brand voice ấm áp theo brand_brain.md
```

---

## NHÓM 6 — WEEKEND / SEASONAL (1 mục)

---

### ITEM 10

```yaml
content_id: VQ-FB-SEASON-20260527-010
category: weekend_seasonal
platform: Facebook
persona: Segment B (gia đình) + Segment C (sinh viên) — cuối tuần Vinh, khí hậu Nghệ An
pillar: SEASON (kết hợp PROD)
angle: "Cuối tuần + ngày nóng Nghệ An — gỏi cuốn mát lạnh / bánh tráng cuốn nhẹ nhàng"
offer_type: OF-08 — Bữa Cuối Tuần Đặc Biệt
draft_status: DRAFT
validation_status: NEEDS_OWNER_REVIEW
content_type: Photo (bàn ăn cuối tuần đẹp) + Caption kết hợp SEASON và PROD
posting_time_suggestion: Thứ 7, 09:30–10:30

caption_draft_v1: |
  Cuối tuần Vinh nóng vừa — gỏi cuốn tôm tươi là chân ái rồi! ☀️
  
  Mâm cuối tuần nhà Vị Cuốn:
  → Gỏi cuốn tôm thịt — rau sống tươi, tôm ngọt giòn
  → Bánh tráng cuốn thịt heo — cuốn tay, chấm mắm nêm
  → Nước chanh tươi mát
  
  Cuối tuần này: [OWNER_CONFIRM: offer OF-08 — nâng cấp / tặng gỏi / free topping]
  
  Ghé quán: [FILL: địa chỉ] | Hoặc đặt: [FILL: ShopeeFood/GrabFood]
  
  #VịCuốn #ĂnVinh #CuốiTuần #GỏiCuốn #NghệAn #BánhTrángCuốn #ViNghệAn

caption_draft_v2: |
  Nghệ An nắng nóng — ăn gỏi cuốn là đúng nhất.
  
  Cuối tuần tại Vị Cuốn: gỏi cuốn tôm tươi + bánh tráng cuốn heo quay + mắm nêm tự pha.
  [OWNER_CONFIRM: offer OF-08 nếu có].
  
  📍 [FILL: địa chỉ] | 📞 [FILL: SĐT]
  
  #VịCuốn #ĂnVinh #GỏiCuốn #CuốiTuần #MonNgon

safety_flags:
  - OFFER_UNCONFIRMED: "OF-08 Weekend Special ưu đãi cụ thể chưa xác nhận"
  - ADDRESS_UNFILLED: "Địa chỉ và SĐT chưa có"

missing_fields:
  - offer_detail_OF-08 (nâng cấp heo quay / tặng gỏi cuốn / free topping)
  - address_detail
  - phone_number
  - delivery_platform_links
  - offer_status_OF-08

next_action: |
  Owner xác nhận OF-08 ưu đãi cụ thể + điền địa chỉ + SĐT.
  Builder finalize 1 trong 2 phiên bản caption theo feedback Owner.
  Chuyển READY_FOR_REVIEW sau khi Owner điền đủ.

assumptions:
  - Mùa hè / thời tiết nóng Nghệ An (tháng 5–8) — SEASON angle phù hợp
  - Gỏi cuốn tôm thịt có trong menu theo brand_brain.md USPs
  - Bài SEASON đăng cuối tuần theo content_pillars.md Pillar 6
```

---

## Tổng Kết Queue Stats

| Metric | Số lượng |
|--------|---------|
| Tổng items | 10 |
| READY_FOR_REVIEW | 1 (Item 05) |
| NEEDS_OWNER_REVIEW | 9 (Items 01, 02, 03, 04, 06, 07, 08, 09, 10) |
| BLOCKED | 0 |
| Items có BLOCKER flag | 0 |
| Items có [FILL] quan trọng | 9 |
| Items cần Owner tạo voucher trước | 2 (Items 08, 09) |
| Items cần Owner quay/chụp media | 3 (Items 02, 05, 07) |

**[FILL] quan trọng nhất cần Owner điền để unblock queue:**
1. Địa chỉ chi tiết (ảnh hưởng 7/10 items)
2. Số điện thoại (ảnh hưởng 6/10 items)
3. Giá các combo OF-01, OF-02, OF-03 (ảnh hưởng 4/10 items)
4. Offer status OF-01 đến OF-08 (ảnh hưởng 9/10 items)

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.5 — File tạo mới. 10 sample queue items: 3 office lunch, 2 rainy day/mắm nêm, 2 group/family, 1 new customer, 1 comeback, 1 weekend/seasonal. Đầy đủ fields theo spec Phase 1.5. | Claude Code (Builder) |
