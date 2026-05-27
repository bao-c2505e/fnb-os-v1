# Output Examples — Content Pack Generator

*Phase 1.4 — Draft Content Pack Generator Schema*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*3 ví dụ Content Pack đầy đủ cho Vị Cuốn — trạng thái DRAFT*

---

## Danh sách ví dụ

| # | ID | Chủ đề | Platform | Pillar |
|---|-----|--------|----------|--------|
| 1 | VQ-FB-PRMO-20260527-001 | Bữa Trưa Văn Phòng | Facebook | PROMO |
| 2 | VQ-FB-SESN-20260527-001 | Ngày Mưa / Thèm Mắm Nêm | Facebook | SEASON |
| 3 | VQ-FB-PRMO-20260527-002 | Combo Gia Đình Cuối Tuần | Facebook | PROMO |

---
---

# VÍ DỤ 1 — Bữa Trưa Văn Phòng

## BLOCK A — MARKDOWN

---

### Content ID
`VQ-FB-PRMO-20260527-001`

---

### Caption Options

**v1 — Đầy đủ (Facebook Post)**
> Hôm nay Combo Trưa tại Vị Cuốn nhé! 🍜
>
> Bánh tráng cuốn thịt heo tươi + bún trộn mắm nêm tự pha + nước chanh mát lạnh — no căng bụng, ví không đau.
>
> Chỉ **[FILL: giá OF-01]đ** thôi — đặt trước 5 phút là có ngay tại quán hoặc ShopeeFood.
>
> ⏰ Thứ 2–6 | 11:00–14:00
> 📍 Vị Cuốn — Vinh, Nghệ An ([FILL: địa chỉ chi tiết])
>
> #VịCuốn #ComboTrưa #ĂnVinh #VinhNghệAn #BữaTrưaNgon

*char_count: ~290 | note: Đầy đủ, tập trung conversion, có CTA rõ ràng*

---

**v2 — Ngắn (phù hợp Story hoặc đăng nhanh)**
> Combo Trưa hôm nay đây — bánh tráng cuốn + bún trộn mắm nêm + nước, chỉ [FILL]đ thôi!
>
> T2–T6, 11:00–14:00 tại Vị Cuốn — Vinh 🥢
>
> #VịCuốn #ĂnVinh

*char_count: ~145 | note: Ngắn gọn, đủ thông tin deal*

---

### Hook Options

| # | Text | Tone | Platform phù hợp |
|---|------|------|-----------------|
| H1 | "Hôm nay trưa ăn gì chưa? Vị Cuốn có combo [FILL]đ — no căng bụng luôn." | Thực tế, thân thiện | Facebook, Zalo OA |
| H2 | "Đầu tuần rồi — cần một bữa trưa ngon để có năng lượng chiến tiếp không?" | Đồng cảm, nhẹ nhàng | Facebook |
| H3 | "Combo Trưa: bánh tráng cuốn + bún trộn + nước. [FILL]đ. 11:00–14:00. Thế thôi." | Minimal, sự kiện thật | Facebook, Zalo OA |

---

### Short Video Script Options
*null — content_type là Post, không cần script*

---

### Image Brief

| Field | Nội dung |
|-------|---------|
| **subject** | Combo đầy đủ bày trên khay gỗ: đĩa bánh tráng cuốn thịt heo (2–3 cuốn), bát bún trộn mắm nêm nhỏ, ly nước chanh có đá |
| **composition** | Góc 45° nhìn từ trên xuống nhẹ, rule of thirds — combo ở trung tâm lệch trái, chén mắm nêm đỏ cam góc phải trước |
| **lighting** | Ánh sáng tự nhiên từ cửa sổ bên trái, tone ấm vàng nhạt, không bóng cứng |
| **props** | Khăn ăn gấp gọn màu trắng hoặc nâu nhạt, đũa gỗ đặt bên cạnh, vài lá rau sống xanh tươi ngoài đĩa |
| **avoid** | Bàn bẩn, nền tối, ảnh mờ, combo thiếu món, khăn ăn nhàu nát, bóng điện thoại |
| **reference_style** | Food photography Việt Nam phong cách tự nhiên — ấm áp, đời thường, không quá studio, không filter màu lạnh |

---

### Design Brief
*null — Post ảnh thật, không cần design overlay*

---

### Offer Summary
**OF-01 — Combo Trưa Vị Cuốn**
> 1 phần bánh tráng cuốn thịt heo + 1 bún trộn mắm nêm nhỏ + 1 nước (chanh tươi hoặc trà).
> Giá: [FILL: ~65.000đ — Owner xác nhận].
> Áp dụng: Thứ 2–6, 11:00–14:00. Tại quán và ShopeeFood/GrabFood.
> [OWNER_CONFIRM: Trạng thái OF-01 — active hay chưa?]

---

### Target Persona

| Field | Nội dung |
|-------|---------|
| segment | Segment A |
| persona_name | Lan — nhân viên văn phòng, 28 tuổi, Vinh [OWNER_CONFIRM: tên persona chính thức từ customer_brain.md] |
| pain_point | Không biết trưa ăn gì, không muốn đặt ship xa, cần no nhanh trong giờ nghỉ trưa ngắn |

---

### Platform Fit

| Field | Nội dung |
|-------|---------|
| recommended_post_time | Thứ 2 lúc 10:30–11:00 (trước giờ trưa) — theo content_pillars.md Pillar 3 [OWNER_CONFIRM: lịch thực tế] |
| format_notes | Facebook Post: ảnh 1200×1200px hoặc 4:5. Caption Facebook không giới hạn nhưng 300 ký tự hiển thị trước "Xem thêm" |
| hashtags | #VịCuốn #ComboTrưa #ĂnVinh #VinhNghệAn #BữaTrưaNgon |

---

### Safety Flags

| Field | Nội dung |
|-------|---------|
| passed | ✅ true |
| flags | Không có BLOCKER |
| ai_notes | Giá [FILL] vì menu_brain.md chưa có giá xác nhận cho OF-01. Trạng thái OF-01 chưa xác nhận → [OWNER_CONFIRM]. Địa chỉ chi tiết chưa có → [FILL]. Tất cả thông tin còn lại OK. |

---

### Approval Required

| Field | Value |
|-------|-------|
| status | **DRAFT** |
| owner_decision | null |
| revision_note | null |
| revision_count | 0 |

---

### Metadata

| Field | Value |
|-------|-------|
| created_at | 2026-05-27T10:00:00+07:00 |
| created_by_agent | Claude Code (Builder) — Phase 1.4 example |
| source_brain_version | Phase 1.4 |
| input_brief_ref | input_brief_template.md — Ví dụ 1 |
| assumptions | ["OF-01 assumed active — chưa xác nhận", "Giá ~65.000đ là target từ offer_engine.md, chưa phải giá chính thức", "Giờ đăng 10:30–11:00 theo content_pillars.md Pillar 3"] |

---

## BLOCK B — JSON

```json
{
  "id": "VQ-FB-PRMO-20260527-001",
  "brand": "Vi Cuon",
  "platform": "Facebook",
  "content_type": "Post",
  "objective": "conversion",

  "persona": {
    "segment": "Segment A",
    "persona_name": "Lan — nhân viên văn phòng 28 tuổi [OWNER_CONFIRM]",
    "pain_point": "Không biết trưa ăn gì, không muốn đặt ship xa, cần no nhanh"
  },

  "pillar": "PRMO",

  "angle": {
    "code": "C1",
    "name": "combo-reveal",
    "hook": "Hôm nay trưa ăn gì chưa? Vị Cuốn có combo [FILL]đ — no căng bụng luôn."
  },

  "offer": {
    "offer_id": "OF-01",
    "offer_name": "Combo Trưa Vị Cuốn",
    "voucher_code": null,
    "offer_summary": "Bánh tráng cuốn + bún trộn + nước. [FILL: ~65.000đ]. T2–T6, 11:00–14:00. [OWNER_CONFIRM: offer active?]",
    "valid_until": null
  },

  "caption_options": [
    {
      "version": "v1",
      "text": "Hôm nay Combo Trưa tại Vị Cuốn nhé! 🍜\n\nBánh tráng cuốn thịt heo tươi + bún trộn mắm nêm tự pha + nước chanh mát lạnh — no căng bụng, ví không đau.\n\nChỉ [FILL: giá OF-01]đ thôi — đặt trước 5 phút là có ngay tại quán hoặc ShopeeFood.\n\n⏰ Thứ 2–6 | 11:00–14:00\n📍 Vị Cuốn — Vinh, Nghệ An ([FILL: địa chỉ])\n\n#VịCuốn #ComboTrưa #ĂnVinh #VinhNghệAn #BữaTrưaNgon",
      "char_count": 290,
      "note": "Đầy đủ, tập trung conversion, có CTA rõ ràng"
    },
    {
      "version": "v2",
      "text": "Combo Trưa hôm nay đây — bánh tráng cuốn + bún trộn mắm nêm + nước, chỉ [FILL]đ thôi!\n\nT2–T6, 11:00–14:00 tại Vị Cuốn — Vinh 🥢\n\n#VịCuốn #ĂnVinh",
      "char_count": 145,
      "note": "Ngắn gọn, phù hợp Story hoặc đăng nhanh"
    }
  ],

  "script_options": null,

  "image_brief": {
    "subject": "Combo đầy đủ: đĩa bánh tráng cuốn (2–3 cuốn), bát bún trộn mắm nêm nhỏ, ly nước chanh có đá, trên khay gỗ",
    "composition": "Góc 45° từ trên xuống nhẹ, combo ở trung tâm lệch trái, chén mắm nêm đỏ cam góc phải trước",
    "lighting": "Ánh sáng tự nhiên từ cửa sổ bên trái, tone ấm vàng nhạt, không bóng cứng",
    "props": "Khăn ăn trắng/nâu nhạt gấp gọn, đũa gỗ bên cạnh, vài lá rau sống xanh tươi",
    "avoid": "Bàn bẩn, nền tối, ảnh mờ, combo thiếu món, khăn nhàu nát, bóng điện thoại",
    "reference_style": "Food photography Việt Nam — ấm áp, đời thường, không quá studio, không filter màu lạnh"
  },

  "design_brief": null,

  "safety_check": {
    "passed": true,
    "checked_at": "2026-05-27T10:00:00+07:00",
    "flags": [],
    "ai_notes": "Giá [FILL] — menu_brain.md chưa có giá OF-01. Offer status [OWNER_CONFIRM]. Địa chỉ [FILL]. Không có claim sức khỏe. Không đề cập đối thủ. Emoji 2 cái. Pass."
  },

  "approval": {
    "status": "DRAFT",
    "owner_decision": null,
    "revision_note": null,
    "approval_timestamp": null,
    "proposed_publish_date": null,
    "manual_publish_link": null,
    "revision_count": 0
  },

  "metadata": {
    "created_at": "2026-05-27T10:00:00+07:00",
    "updated_at": "2026-05-27T10:00:00+07:00",
    "created_by_agent": "Claude Code (Builder) — Phase 1.4 example",
    "source_brain_version": "Phase 1.4",
    "input_brief_ref": "input_brief_template.md — Ví dụ 1",
    "assumptions": [
      "OF-01 assumed active — chưa xác nhận từ offer_engine.md",
      "Giá ~65.000đ là target từ offer_engine.md, chưa phải giá chính thức",
      "Giờ đăng 10:30–11:00 theo content_pillars.md Pillar 3 — Owner xác nhận lịch thực tế"
    ],
    "n8n_workflow_id": null,
    "drive_folder_url": null,
    "sheet_row_id": null
  }
}
```

---
---

# VÍ DỤ 2 — Ngày Mưa / Thèm Mắm Nêm

## BLOCK A — MARKDOWN

---

### Content ID
`VQ-FB-SESN-20260527-001`

---

### Caption Options

**v1 — Đầy đủ (Facebook Post)**
> Vinh đang mưa — và nhà mình đang có bún trộn mắm nêm nóng hổi chờ bạn. 🌧️
>
> Ngày này mà ngồi húp bát bún trộn mắm nêm tự pha — chua cay vừa miệng, ấm từ trong ra ngoài — thật sự không có gì bằng.
>
> Ghé Vị Cuốn hoặc đặt qua ShopeeFood nhé — giao đến tận cửa cho bạn khỏi ướt mưa!
>
> 📍 [FILL: địa chỉ Vị Cuốn]
> 📞 [FILL: số điện thoại]
>
> #VịCuốn #NgàyMưa #BúnTrộnMắmNêm #ĂnVinh #VinhNghệAn

*char_count: ~320 | note: Emotional, dựa vào thời tiết thật — chỉ đăng khi đang mưa ở Vinh*

---

**v2 — Ngắn hơn**
> Vinh mưa rồi — bún trộn mắm nêm nóng tại Vị Cuốn đang chờ bạn nhé 🌧️
>
> Đặt qua ShopeeFood — giao tận cửa, khỏi ướt mưa!
>
> #VịCuốn #NgàyMưa #ĂnVinh

*char_count: ~145 | note: Post nhanh, phù hợp khi trời mưa bất chợt*

---

### Hook Options

| # | Text | Tone | Platform phù hợp |
|---|------|------|-----------------|
| H1 | "Vinh đang mưa — không biết ăn gì? Bún trộn mắm nêm nóng tại Vị Cuốn đang sẵn sàng." | Thực tế, kịp thời | Facebook |
| H2 | "Ngày mưa mà thèm cái gì đó ấm nóng, chua cay vừa miệng — bún trộn mắm nêm là đây." | Gợi cảm giác | Facebook |
| H3 | "Mưa rồi. Đặt đi bạn ơi — khỏi nghĩ nữa." | Hài hước nhẹ | Facebook |

---

### Short Video Script Options (Reel 15–30 giây — tùy chọn nếu Owner muốn làm Reel)

**v1 — "Mưa Và Bún Trộn"** *(template: VS-09 — Weather Trigger)*

| Cảnh | Thời lượng | Visual | Audio | Text Overlay |
|------|-----------|--------|-------|-------------|
| 1 | 2s | Cảnh mưa rơi qua cửa sổ quán | Tiếng mưa nhẹ | "Vinh đang mưa..." |
| 2 | 3s | Tay múc bát bún trộn nóng bốc khói nhẹ | Tiếng muỗng chạm bát | "Và bún trộn mắm nêm đang sẵn" |
| 3 | 5s | Close-up bát bún trộn — rau xanh, mắm nêm đỏ cam, sợi bún trắng | Nhạc nền nhẹ ấm áp | "Chua cay — ấm lòng" |
| 4 | 3s | Cảnh đặt bát trước khách, khói bốc lên | Nhạc tiếp | "Ghé quán hoặc đặt ship" |
| 5 | 2s | Logo Vị Cuốn + địa chỉ | Nhạc nhẹ | "Vị Cuốn — Vinh, Nghệ An" |

CTA: "Đặt ngay qua ShopeeFood — giao tận cửa"

*⚠️ [OWNER_CONFIRM: quán có cảnh quay mưa qua cửa sổ không? Nếu không có thể thay bằng cảnh bát bún bốc khói.]*

---

### Image Brief

| Field | Nội dung |
|-------|---------|
| **subject** | Bát bún trộn mắm nêm đang bốc khói nhẹ, đặt trên bàn gỗ, phía sau là khung cửa sổ mờ có vẻ ẩm ướt/mưa |
| **composition** | Góc 45° vừa, bát bún ở trung tâm nhẹ lệch phải, chén mắm nêm đỏ cam bên trái trước |
| **lighting** | Ánh sáng ấm từ trong quán, tạo cảm giác ấm cúng tương phản với ngoài trời xám xịt |
| **props** | Đũa gỗ đặt bên bát, vài lát ớt đỏ trên mặt bát, nền nhìn thấy một chút khung cửa sổ mờ |
| **avoid** | Ánh sáng quá sáng lạnh, ảnh trời mưa quá nặng nề, bát trống, bàn bẩn |
| **reference_style** | Ảnh food cozy/comfort food — tone ấm vàng nâu, gợi cảm giác muốn ăn ngay |

---

### Design Brief
*null — Post ảnh thật*

---

### Offer Summary
**OF-06 — Deal Ngày Mưa**
> [OWNER_CONFIRM: OF-06 chưa xác nhận trạng thái. Chỉ dùng bài này khi Owner bật OF-06.]
> Hình thức: [FILL — giao hàng miễn phí / giảm X% / tặng thêm nước — Owner quyết định khi bật]
> Áp dụng: Trong ngày Owner kích hoạt

*⚠️ KHÔNG đăng offer trong caption nếu OF-06 chưa active — dùng caption không đề cập giá/deal*

---

### Target Persona

| Field | Nội dung |
|-------|---------|
| segment | All |
| persona_name | Tất cả khách ở Vinh trong ngày mưa |
| pain_point | Không muốn ra ngoài mưa, thèm ăn gì đó ấm nóng, ngại nấu |

---

### Platform Fit

| Field | Nội dung |
|-------|---------|
| recommended_post_time | Đăng ngay khi trời mưa — 11:00–13:00 hoặc 17:00–18:00 [OWNER_CONFIRM: thời điểm mưa thực tế] |
| format_notes | Post nhanh — tính kịp thời quan trọng hơn hoàn hảo. Facebook reach tốt nhất cho nội dung thời tiết. |
| hashtags | #VịCuốn #NgàyMưa #BúnTrộnMắmNêm #ĂnVinh #VinhNghệAn #ComfortFood |

---

### Safety Flags

| Field | Nội dung |
|-------|---------|
| passed | ✅ true (với điều kiện OF-06 được xác nhận trước khi đăng) |
| flags | WARNING: OF-06 status chưa xác nhận — không đăng deal nếu chưa active |
| ai_notes | OF-06 [OWNER_CONFIRM]. Địa chỉ và số điện thoại [FILL]. Không có claim sức khỏe. Cảm giác "ấm nóng" là mô tả giác quan, không phải health claim. Caption không có giá → an toàn. |

---

### Approval Required

| Field | Value |
|-------|-------|
| status | **DRAFT** |
| owner_decision | null |
| revision_count | 0 |

---

### Metadata

| Field | Value |
|-------|-------|
| created_at | 2026-05-27T10:00:00+07:00 |
| created_by_agent | Claude Code (Builder) — Phase 1.4 example |
| source_brain_version | Phase 1.4 |
| assumptions | ["OF-06 chưa xác nhận — caption v1/v2 không đề cập deal cụ thể để an toàn", "Giờ đăng = khi trời mưa thật — không thể lên lịch trước", "Bài này có Reel option tùy chọn — Owner quyết định có quay không"] |

---

## BLOCK B — JSON

```json
{
  "id": "VQ-FB-SESN-20260527-001",
  "brand": "Vi Cuon",
  "platform": "Facebook",
  "content_type": "Post",
  "objective": "engagement",

  "persona": {
    "segment": "All",
    "persona_name": "Tất cả khách ở Vinh trong ngày mưa",
    "pain_point": "Không muốn ra ngoài mưa, thèm ăn gì đó ấm nóng, ngại nấu"
  },

  "pillar": "SESN",

  "angle": {
    "code": "C5",
    "name": "thoi-tiet-deal",
    "hook": "Vinh đang mưa — không biết ăn gì? Bún trộn mắm nêm nóng tại Vị Cuốn đang sẵn sàng."
  },

  "offer": {
    "offer_id": "OF-06",
    "offer_name": "Deal Ngày Mưa",
    "voucher_code": null,
    "offer_summary": "[OWNER_CONFIRM: OF-06 chưa xác nhận active. Hình thức: [FILL]. Áp dụng: ngày Owner kích hoạt.]",
    "valid_until": null
  },

  "caption_options": [
    {
      "version": "v1",
      "text": "Vinh đang mưa — và nhà mình đang có bún trộn mắm nêm nóng hổi chờ bạn. 🌧️\n\nNgày này mà ngồi húp bát bún trộn mắm nêm tự pha — chua cay vừa miệng, ấm từ trong ra ngoài — thật sự không có gì bằng.\n\nGhé Vị Cuốn hoặc đặt qua ShopeeFood nhé — giao đến tận cửa cho bạn khỏi ướt mưa!\n\n📍 [FILL: địa chỉ]\n📞 [FILL: số điện thoại]\n\n#VịCuốn #NgàyMưa #BúnTrộnMắmNêm #ĂnVinh #VinhNghệAn",
      "char_count": 320,
      "note": "Emotional, dựa vào thời tiết thật — chỉ đăng khi đang mưa ở Vinh"
    },
    {
      "version": "v2",
      "text": "Vinh mưa rồi — bún trộn mắm nêm nóng tại Vị Cuốn đang chờ bạn nhé 🌧️\n\nĐặt qua ShopeeFood — giao tận cửa, khỏi ướt mưa!\n\n#VịCuốn #NgàyMưa #ĂnVinh",
      "char_count": 145,
      "note": "Post nhanh khi trời mưa bất chợt"
    }
  ],

  "script_options": [
    {
      "version": "v1",
      "template_id": "VS-09",
      "duration_target": "15–30 giây",
      "scenes": [
        {"scene_number": 1, "duration": "2s", "visual": "Cảnh mưa rơi qua cửa sổ quán", "audio": "Tiếng mưa nhẹ", "text_overlay": "Vinh đang mưa..."},
        {"scene_number": 2, "duration": "3s", "visual": "Tay múc bát bún trộn nóng bốc khói", "audio": "Tiếng muỗng chạm bát", "text_overlay": "Bún trộn mắm nêm đang sẵn"},
        {"scene_number": 3, "duration": "5s", "visual": "Close-up bát bún: rau xanh, mắm nêm đỏ cam, sợi bún trắng", "audio": "Nhạc nền nhẹ ấm áp", "text_overlay": "Chua cay — ấm lòng"},
        {"scene_number": 4, "duration": "3s", "visual": "Đặt bát trước khách, khói nhẹ bốc lên", "audio": "Nhạc tiếp", "text_overlay": "Ghé quán hoặc đặt ship"},
        {"scene_number": 5, "duration": "2s", "visual": "Logo Vị Cuốn + địa chỉ", "audio": "Nhạc nhẹ fade", "text_overlay": "Vị Cuốn — Vinh, Nghệ An"}
      ],
      "cta": "Đặt ngay qua ShopeeFood — giao tận cửa"
    }
  ],

  "image_brief": {
    "subject": "Bát bún trộn mắm nêm bốc khói nhẹ, trên bàn gỗ, phía sau là khung cửa sổ mờ ẩm ướt",
    "composition": "Góc 45° vừa, bát bún trung tâm lệch phải, chén mắm nêm đỏ cam bên trái trước",
    "lighting": "Ánh sáng ấm từ trong quán, tương phản với ngoài trời xám",
    "props": "Đũa gỗ bên bát, vài lát ớt đỏ trên mặt, nhìn thấy khung cửa sổ mờ phía sau",
    "avoid": "Ánh sáng lạnh, trời mưa quá nặng nề, bát trống, bàn bẩn",
    "reference_style": "Comfort food cozy — tone ấm vàng nâu, gợi cảm giác muốn ăn ngay"
  },

  "design_brief": null,

  "safety_check": {
    "passed": true,
    "checked_at": "2026-05-27T10:00:00+07:00",
    "flags": [
      {
        "code": "OFFER_UNCONFIRMED",
        "severity": "WARNING",
        "detail": "OF-06 status chưa xác nhận. Caption không đề cập deal cụ thể để an toàn. Owner phải bật OF-06 trước khi thêm offer vào caption."
      }
    ],
    "ai_notes": "OF-06 [OWNER_CONFIRM] — caption draft không đề cập deal để tránh sai. Địa chỉ và SĐT [FILL]. 'Ấm nóng' là mô tả giác quan — không phải health claim. Tính kịp thời quan trọng: chỉ đăng khi đang mưa."
  },

  "approval": {
    "status": "DRAFT",
    "owner_decision": null,
    "revision_note": null,
    "approval_timestamp": null,
    "proposed_publish_date": null,
    "manual_publish_link": null,
    "revision_count": 0
  },

  "metadata": {
    "created_at": "2026-05-27T10:00:00+07:00",
    "updated_at": "2026-05-27T10:00:00+07:00",
    "created_by_agent": "Claude Code (Builder) — Phase 1.4 example",
    "source_brain_version": "Phase 1.4",
    "input_brief_ref": "input_brief_template.md — Ví dụ 2",
    "assumptions": [
      "OF-06 chưa xác nhận — caption không đề cập deal cụ thể",
      "Giờ đăng = khi trời mưa thật — không lên lịch trước được",
      "Reel script là tùy chọn — Owner quyết định có quay không"
    ],
    "n8n_workflow_id": null,
    "drive_folder_url": null,
    "sheet_row_id": null
  }
}
```

---
---

# VÍ DỤ 3 — Combo Gia Đình Cuối Tuần

## BLOCK A — MARKDOWN

---

### Content ID
`VQ-FB-PRMO-20260527-002`

---

### Caption Options

**v1 — Đầy đủ (Facebook Post)**
> Cuối tuần rồi — bữa ăn gia đình nên có gì đặc biệt hơn chứ nhỉ? 🏠
>
> Combo Gia Đình Vị Cuốn dành cho 2 người:
> ✔ 2 phần bánh tráng cuốn thịt heo
> ✔ 2 bát bún trộn mắm nêm
> ✔ 2 ly nước
>
> No đủ 2 người — chỉ **[FILL: giá OF-03]đ** thôi, tiết kiệm hơn đặt riêng lẻ.
>
> Đặt trước qua Zalo/inbox nhé — ghé quán hoặc giao về nhà!
>
> 📍 Vị Cuốn — Vinh, Nghệ An ([FILL: địa chỉ])
> 📞 [FILL: số điện thoại / Zalo]
>
> #VịCuốn #ComboGiaDình #ĂnVinh #VinhNghệAn #BữaĂnGiaDình #CuốiTuầnNgon

*char_count: ~360 | note: Rõ ràng từng món trong combo, tập trung giá trị "đáng đồng tiền"*

---

**v2 — Ngắn hơn**
> Cuối tuần — bữa ăn gia đình ngon tại Vị Cuốn nhé! 🏠
>
> Combo 2 người: bánh tráng cuốn + bún trộn mắm nêm + nước. Chỉ [FILL]đ — no đủ 2 người luôn!
>
> Đặt qua Zalo hoặc ghé trực tiếp. #VịCuốn #ĂnVinh

*char_count: ~175 | note: Ngắn gọn, đủ thông tin*

---

### Hook Options

| # | Text | Tone | Platform phù hợp |
|---|------|------|-----------------|
| H1 | "Cuối tuần bữa ăn gia đình — đơn giản mà ngon, không cần phải đi xa." | Ấm áp | Facebook |
| H2 | "2 người ăn no — [FILL]đ — cuối tuần không cần nấu cũng được." | Thực tế, tiết kiệm | Facebook |
| H3 | "Bữa ăn cuối tuần của gia đình bạn hôm nay là gì? 🏠" | Hỏi, tạo tương tác | Facebook |

---

### Short Video Script Options
*null — content_type là Post. Nếu Owner muốn Reel: dùng template VS-02 (Combo Reveal) với cảnh bày 2 bộ combo lên bàn, đặt cạnh nhau — visual "gia đình" rõ ràng.*

---

### Image Brief

| Field | Nội dung |
|-------|---------|
| **subject** | Bàn ăn với 2 bộ combo đầy đủ đặt cạnh nhau: mỗi bộ gồm đĩa bánh tráng cuốn, bát bún trộn, ly nước — bày trên bàn gỗ ấm áp |
| **composition** | Góc chụp nhìn từ trên xuống (flat lay) hoặc 45° nhẹ. 2 bộ combo đối xứng nhau, chén mắm nêm ở giữa chia sẻ |
| **lighting** | Ánh sáng tự nhiên ấm, tone nâu gỗ + trắng + đỏ cam của mắm nêm |
| **props** | Khăn ăn nhỏ cho mỗi bộ, đũa gỗ 2 đôi, không có điện thoại trong khung |
| **avoid** | Bàn quá chật, combo thiếu món, không gian nhìn lạnh lẽo, một bộ thiếu |
| **reference_style** | Bữa ăn gia đình ấm cúng — ảnh đời thường, không phải set up quán phức tạp |

---

### Design Brief
*null — Post ảnh thật*

---

### Offer Summary
**OF-03 — Combo Gia Đình (2 người)**
> 2 phần bánh tráng cuốn thịt heo + 2 bát bún trộn mắm nêm + 2 ly nước.
> Giá: [FILL: ~130.000–140.000đ — Owner xác nhận].
> Tiết kiệm: [FILL: ~10–15% so với đặt riêng lẻ].
> Áp dụng: Cả tuần, cả ngày. Đặt qua Zalo / inbox trực tiếp.
> [OWNER_CONFIRM: Trạng thái OF-03 — active hay chưa?]

---

### Target Persona

| Field | Nội dung |
|-------|---------|
| segment | Segment B |
| persona_name | Chị Hà — mẹ trẻ 32 tuổi, gia đình 2 người lớn, Vinh [OWNER_CONFIRM: tên persona chính thức từ customer_brain.md] |
| pain_point | Cuối tuần muốn có bữa ăn ngon cho gia đình nhưng không muốn nấu hoặc đi quá xa |

---

### Platform Fit

| Field | Nội dung |
|-------|---------|
| recommended_post_time | Thứ 5 tối (19:00–21:00) hoặc thứ 6 sáng (8:00–9:00) — nhắc trước cuối tuần theo content_pillars.md [OWNER_CONFIRM] |
| format_notes | Facebook Post: ảnh 4:5 hoặc 1:1. Caption dài hơn OK trên Facebook — khách Segment B đọc nhiều hơn sinh viên |
| hashtags | #VịCuốn #ComboGiaDình #ĂnVinh #VinhNghệAn #BữaĂnGiaDình #CuốiTuầnNgon |

---

### Safety Flags

| Field | Nội dung |
|-------|---------|
| passed | ✅ true |
| flags | Không có BLOCKER |
| ai_notes | Giá OF-03 [FILL] — offer_engine.md chỉ có target range ~130.000–140.000đ. Trạng thái OF-03 [OWNER_CONFIRM]. Địa chỉ và SĐT [FILL]. Không có claim sức khỏe. Không đề cập đối thủ. Emoji 2 cái. Pass. |

---

### Approval Required

| Field | Value |
|-------|-------|
| status | **DRAFT** |
| owner_decision | null |
| revision_count | 0 |

---

### Metadata

| Field | Value |
|-------|-------|
| created_at | 2026-05-27T10:00:00+07:00 |
| created_by_agent | Claude Code (Builder) — Phase 1.4 example |
| source_brain_version | Phase 1.4 |
| assumptions | ["OF-03 assumed could be active — chưa xác nhận", "Giá ~130.000–140.000đ là target range từ offer_engine.md, chưa phải giá chính thức", "Timing thứ 5–6 theo content_pillars.md Pillar 3 — Owner xác nhận lịch thực tế"] |

---

## BLOCK B — JSON

```json
{
  "id": "VQ-FB-PRMO-20260527-002",
  "brand": "Vi Cuon",
  "platform": "Facebook",
  "content_type": "Post",
  "objective": "conversion",

  "persona": {
    "segment": "Segment B",
    "persona_name": "Chị Hà — mẹ trẻ 32 tuổi, gia đình 2 người lớn, Vinh [OWNER_CONFIRM]",
    "pain_point": "Cuối tuần muốn bữa ăn ngon cho gia đình nhưng không muốn nấu hoặc đi xa"
  },

  "pillar": "PRMO",

  "angle": {
    "code": "C4",
    "name": "combo-nhom",
    "hook": "Cuối tuần bữa ăn gia đình — đơn giản mà ngon, không cần phải đi xa."
  },

  "offer": {
    "offer_id": "OF-03",
    "offer_name": "Combo Gia Đình (2 người)",
    "voucher_code": null,
    "offer_summary": "2 phần cuốn + 2 bún trộn + 2 nước. [FILL: ~130.000–140.000đ]. Tiết kiệm ~10–15% so với lẻ. Cả tuần, cả ngày. [OWNER_CONFIRM: offer active?]",
    "valid_until": null
  },

  "caption_options": [
    {
      "version": "v1",
      "text": "Cuối tuần rồi — bữa ăn gia đình nên có gì đặc biệt hơn chứ nhỉ? 🏠\n\nCombo Gia Đình Vị Cuốn dành cho 2 người:\n✔ 2 phần bánh tráng cuốn thịt heo\n✔ 2 bát bún trộn mắm nêm\n✔ 2 ly nước\n\nNo đủ 2 người — chỉ [FILL: giá OF-03]đ thôi, tiết kiệm hơn đặt riêng lẻ.\n\nĐặt trước qua Zalo/inbox nhé — ghé quán hoặc giao về nhà!\n\n📍 Vị Cuốn — Vinh, Nghệ An ([FILL: địa chỉ])\n📞 [FILL: SĐT / Zalo]\n\n#VịCuốn #ComboGiaDình #ĂnVinh #VinhNghệAn #BữaĂnGiaDình #CuốiTuầnNgon",
      "char_count": 360,
      "note": "Rõ ràng từng món, nhấn giá trị đáng đồng tiền"
    },
    {
      "version": "v2",
      "text": "Cuối tuần — bữa ăn gia đình ngon tại Vị Cuốn nhé! 🏠\n\nCombo 2 người: bánh tráng cuốn + bún trộn mắm nêm + nước. Chỉ [FILL]đ — no đủ 2 người luôn!\n\nĐặt qua Zalo hoặc ghé trực tiếp. #VịCuốn #ĂnVinh",
      "char_count": 175,
      "note": "Ngắn gọn, đủ thông tin key"
    }
  ],

  "script_options": null,

  "image_brief": {
    "subject": "Bàn ăn 2 bộ combo đầy đủ cạnh nhau: đĩa bánh tráng cuốn, bát bún trộn, ly nước — mỗi bộ đầy đủ",
    "composition": "Flat lay hoặc 45° nhẹ. 2 bộ combo đối xứng, chén mắm nêm ở giữa chia sẻ",
    "lighting": "Ánh sáng tự nhiên ấm, tone nâu gỗ + trắng + đỏ cam mắm nêm",
    "props": "Khăn ăn nhỏ cho mỗi bộ, 2 đôi đũa gỗ, không điện thoại trong khung",
    "avoid": "Bàn chật, combo thiếu món, không gian lạnh lẽo, bộ thiếu",
    "reference_style": "Bữa ăn gia đình ấm cúng — đời thường, không set up phức tạp"
  },

  "design_brief": null,

  "safety_check": {
    "passed": true,
    "checked_at": "2026-05-27T10:00:00+07:00",
    "flags": [],
    "ai_notes": "Giá OF-03 [FILL] — target range ~130k–140k từ offer_engine.md, chưa phải giá chính thức. OF-03 status [OWNER_CONFIRM]. Địa chỉ và SĐT [FILL]. Không claim sức khỏe. Không đề cập đối thủ. Emoji 2 cái. Pass."
  },

  "approval": {
    "status": "DRAFT",
    "owner_decision": null,
    "revision_note": null,
    "approval_timestamp": null,
    "proposed_publish_date": null,
    "manual_publish_link": null,
    "revision_count": 0
  },

  "metadata": {
    "created_at": "2026-05-27T10:00:00+07:00",
    "updated_at": "2026-05-27T10:00:00+07:00",
    "created_by_agent": "Claude Code (Builder) — Phase 1.4 example",
    "source_brain_version": "Phase 1.4",
    "input_brief_ref": "input_brief_template.md — Ví dụ 3",
    "assumptions": [
      "OF-03 có thể active — chưa xác nhận từ offer_engine.md",
      "Giá ~130.000–140.000đ là target range, chưa phải giá chính thức",
      "Timing thứ 5–6 theo content_pillars.md Pillar 3 — Owner xác nhận"
    ],
    "n8n_workflow_id": null,
    "drive_folder_url": null,
    "sheet_row_id": null
  }
}
```

---

## Tổng kết 3 ví dụ

| Pack | Đặc điểm | Safety |
|------|---------|--------|
| VQ-FB-PRMO-20260527-001 | Combo Trưa — PROMO đầu tuần, Segment A | ✅ Pass — giá [FILL] |
| VQ-FB-SESN-20260527-001 | Ngày Mưa — SEASON, All, tính kịp thời | ✅ Pass — OF-06 WARNING (unconfirmed) |
| VQ-FB-PRMO-20260527-002 | Combo Gia Đình — PROMO cuối tuần, Segment B | ✅ Pass — giá [FILL] |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — File tạo mới. 3 Content Pack ví dụ đầy đủ: Combo Trưa Văn Phòng, Ngày Mưa Mắm Nêm, Combo Gia Đình Cuối Tuần. Mỗi pack có BLOCK A (Markdown) và BLOCK B (JSON). | Claude Code (Builder) |
