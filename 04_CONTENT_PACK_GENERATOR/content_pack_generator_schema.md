# Content Pack Generator Schema — Vị Cuốn

*Phase 1.4 — Draft Content Pack Generator Schema*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Nguồn tham chiếu: 01_BRAIN/ · 02_CONTENT_ENGINE/ · 03_APPROVAL_PIPELINE/content_pack_json_schema.md*

---

## Tổng quan

Schema này định nghĩa đầy đủ:
- **INPUT** — Owner/ChatGPT cung cấp gì để AI tạo Content Pack
- **OUTPUT** — AI tạo ra Content Pack theo cấu trúc nào
- **QUY TẮC** — Ràng buộc khi tạo

Content Pack Generator **KHÔNG** là n8n workflow. Đây là schema để AI Worker (Claude Code / Codex / Gemini) đọc và thực thi thủ công hoặc semi-automated.

---

## PHẦN 1 — INPUT SCHEMA

### Input Fields (11 trường)

```
INPUT BRIEF
──────────────────────────────────────────────────────────────
Field           Type        Required    Mô tả
──────────────────────────────────────────────────────────────
brand           string      REQUIRED    Tên thương hiệu
                                        Allowed: "Vi Cuon"
                                        
platform        string      REQUIRED    Nền tảng đăng
                                        Allowed: Facebook | TikTok | Instagram
                                                 | Zalo OA | Multi
                                                 
objective       string      REQUIRED    Mục tiêu marketing
                                        Allowed: awareness | engagement
                                                 | conversion | retention
                                                 | education
                                                 
target_persona  string      REQUIRED    Segment khách hàng
                                        Allowed: Segment A | Segment B
                                                 | Segment C | All
                                        Tham chiếu: customer_brain.md
                                        
pillar          string      REQUIRED    Content Pillar
                                        Allowed: PROD | BTS | PROMO
                                                 | STORY | COM | SEASON
                                        Tham chiếu: content_pillars.md
                                        
angle           string      REQUIRED    Content Angle (mã hoặc tên)
                                        Ví dụ: A1 | B2 | C4 | D3 | E1
                                        Tham chiếu: content_angles.md
                                        Nếu "AUTO" → AI tự chọn phù hợp
                                        
offer_type      string      OPTIONAL    Mã offer nếu bài có promotion
                                        Allowed: OF-01 | OF-02 | OF-03 |
                                                 OF-04 | OF-05 | OF-06 |
                                                 OF-07 | OF-08 | OF-09
                                                 | null
                                        Tham chiếu: offer_engine.md
                                        
content_type    string      REQUIRED    Định dạng nội dung
                                        Allowed: Post | Reel | Story |
                                                 Carousel | TikTok Video |
                                                 Zalo Broadcast | Short Video
                                                 
tone            string      OPTIONAL    Giọng điệu cụ thể (ghi đè Brand Voice)
                                        Ví dụ: "ấm áp gần gũi" | "vui nhộn"
                                                | "giáo dục nhẹ nhàng"
                                        Nếu trống → dùng Brand Voice mặc định
                                        từ brand_brain.md
                                        
constraints     string[]    OPTIONAL    Các ràng buộc đặc biệt từ Owner
                                        Ví dụ: ["không đề cập giá",
                                                "chỉ dùng ảnh từ bộ tháng 5",
                                                "caption tối đa 150 ký tự"]
                                        
owner_notes     string      OPTIONAL    Ghi chú tự do từ Owner
                                        Ví dụ: "Tuần này trời mưa, tập trung
                                                vào bún trộn ấm nóng"
──────────────────────────────────────────────────────────────
```

### Validation Rules cho Input

| Rule | Mô tả |
|------|-------|
| `brand` phải là `"Vi Cuon"` | Chỉ một brand trong Phase 1 |
| `offer_type` không null → AI phải đọc `offer_engine.md` | Verify offer còn active trước khi dùng |
| `platform` + `content_type` phải compatible | Ví dụ: TikTok Video chỉ dùng cho TikTok, không cho Zalo OA |
| `pillar` phải phù hợp với `objective` | PROMO → conversion; STORY → education; v.v. |
| Nếu `angle = "AUTO"` → AI chọn từ `content_angles.md` theo pillar/platform | AI phải ghi rõ angle đã chọn trong output |

---

## PHẦN 2 — OUTPUT SCHEMA

### Output Content Pack (12 nhóm trường)

```
OUTPUT CONTENT PACK
──────────────────────────────────────────────────────────────
Nhóm            Fields          Mô tả
──────────────────────────────────────────────────────────────
1. IDENTITY     content_id      ID duy nhất: VQ-[PLAT]-[PILLAR]-[DATE]-[SEQ]
                                Ví dụ: VQ-FB-PROD-20260527-001
                                
2. CAPTION      caption_options 1–3 phiên bản caption
                                - v1: đầy đủ (Facebook/Instagram)
                                - v2: ngắn hơn (TikTok/Story)
                                - v3: minimal (Zalo/story)
                                Mỗi option: text | char_count | note
                                
3. HOOK         hook_options    1–3 câu mở đầu (hook) có thể dùng
                                Dùng cho caption v1 hoặc video script
                                Mỗi hook: text | tone_label | platform_fit
                                
4. VIDEO        short_video_    Script video nếu content_type = video
   SCRIPT       script_options  Format: scenes (visual/audio/text_overlay)
                                Template từ video_script_templates.md
                                1–2 phiên bản: v1 (ngắn) / v2 (dài hơn)
                                
5. IMAGE        image_brief     Brief chụp ảnh:
   BRIEF                        - subject (chủ thể)
                                - composition (góc chụp)
                                - lighting (ánh sáng)
                                - props (đạo cụ)
                                - avoid (tránh gì)
                                - reference_style (phong cách)
                                
6. DESIGN       design_brief    Brief thiết kế (nullable)
   BRIEF                        - format (kích thước)
                                - main_text / sub_text
                                - color_theme (theo brand_brain.md)
                                - font (theo brand_brain.md)
                                - cta_button
                                
7. OFFER        offer_summary   Tóm tắt offer ngắn gọn (từ offer_engine.md)
   SUMMARY                      Null nếu không có offer
                                Format: "[GIẢM X]đ — [GỒM GÌ]. [ĐIỀU KIỆN]"
                                
8. TARGET       target_persona  Đối tượng đích cụ thể:
   PERSONA                      - segment (A/B/C/All)
                                - persona_name (ví dụ: "Lan văn phòng 28t")
                                - pain_point (điểm đau bài giải quyết)
                                
9. PLATFORM     platform_fit    Đánh giá độ phù hợp:
   FIT                          - recommended_post_time (giờ đăng tối ưu)
                                - format_notes (ghi chú định dạng)
                                - hashtags (danh sách hashtag)
                                
10. SAFETY      safety_flags    Kết quả tự kiểm tra:
    FLAGS                       - passed (true/false)
                                - flags[] (mảng cờ cảnh báo)
                                - ai_notes (ghi chú AI)
                                
11. APPROVAL    approval_       Trạng thái trong pipeline:
    REQUIRED    required        Status = DRAFT (luôn luôn khi AI tạo mới)
                                owner_decision = null
                                revision_count = 0
                                
12. METADATA    metadata        Traceability:
                                - created_at (ISO 8601)
                                - created_by_agent
                                - source_brain_version
                                - input_brief_ref (link/tên file brief)
                                - assumptions[] (danh sách giả định AI đã đặt)
──────────────────────────────────────────────────────────────
```

### Output Format Requirements

1. **Luôn output cả Markdown block VÀ JSON-like block** — Markdown để Owner đọc dễ, JSON để ghi vào Google Sheet / n8n
2. **Luôn có ít nhất 2 caption options** — v1 (đầy đủ) và v2 (ngắn)
3. **Luôn có ít nhất 2 hook options** — Owner chọn
4. **Video script chỉ bắt buộc** khi `content_type` là Reel / TikTok Video / Short Video
5. **Design brief chỉ bắt buộc** khi `content_type` là Story / Carousel với overlay text
6. **Mọi giá tiền đều [FILL]** cho đến khi `menu_brain.md` có giá xác nhận
7. **Assumptions rõ ràng** — mọi thông tin AI suy luận phải có tag `[OWNER_CONFIRM]`

---

## PHẦN 3 — CONTENT ID CONVENTION

### Format

```
VQ-[PLATFORM_CODE]-[PILLAR_CODE]-[YYYYMMDD]-[SEQ_3_DIGITS]
```

### Platform Codes

| Platform | Code |
|----------|------|
| Facebook | FB |
| TikTok | TT |
| Instagram | IG |
| Zalo OA | ZL |
| Multi-platform | MP |

### Pillar Codes

| Pillar | Code |
|--------|------|
| PROD | PROD |
| BTS | BTS |
| PROMO | PRMO |
| STORY | STRY |
| COM | COM |
| SEASON | SESN |

### Ví dụ IDs hợp lệ

```
VQ-FB-PROD-20260527-001    Facebook, Product Showcase, ngày 27/05, pack đầu tiên
VQ-TT-BTS-20260527-001     TikTok, Behind the Scenes, ngày 27/05
VQ-IG-STRY-20260603-002    Instagram, Story/STORY pillar, ngày 03/06, pack thứ 2
VQ-ZL-PRMO-20260527-001    Zalo OA, Promotion, ngày 27/05
VQ-MP-PROD-20260527-001    Multi-platform, Product
```

---

## PHẦN 4 — PLATFORM COMPATIBILITY MATRIX

| Platform | Allowed content_type | Pillar ưu tiên | Max caption chars | Hashtag |
|----------|---------------------|----------------|------------------|---------|
| Facebook | Post, Reel, Story, Carousel | PROD, PROMO | ~500 chars | 3–5 tags |
| TikTok | TikTok Video, Short Video | BTS, PROD | 150 chars | 5–10 tags |
| Instagram | Post, Reel, Story, Carousel | PROD, BTS | ~300 chars | 5–15 tags |
| Zalo OA | Zalo Broadcast | PROMO | ~300 chars | Không dùng |
| Multi | Post + Short Video | Linh hoạt | Theo platform chính | Theo platform |

---

## PHẦN 5 — PILLAR × ANGLE MAPPING

AI Worker dùng bảng này khi `angle = "AUTO"`:

| Pillar | Ưu tiên angle | Platform phù hợp |
|--------|--------------|-----------------|
| PROD | A1, A2, A6 | Facebook, Instagram |
| PROD | A5, A3 | TikTok, Instagram |
| BTS | B1, B2, B3 | TikTok, Facebook |
| PROMO | C1, C2 | Facebook, Zalo OA |
| PROMO | C4, C5 | Facebook |
| STORY | D1, D3, D4 | Facebook, Instagram |
| COM | E1, E2 | Facebook, Instagram |
| SEASON | C5, A4 | Facebook, Zalo OA |

---

## PHẦN 6 — OFFER INTEGRATION RULES

Khi `offer_type` không null:

1. AI PHẢI đọc `offer_engine.md` section tương ứng (OF-XX)
2. AI PHẢI check `Trạng thái` field — nếu `[FILL]` → đánh dấu `[OWNER_CONFIRM: offer status]`
3. AI KHÔNG được tự đặt giá — dùng `[FILL: giá OF-XX]` nếu chưa có
4. AI PHẢI copy messaging template từ `offer_engine.md` vào `offer_summary`
5. Voucher code chỉ dùng nếu đã đăng ký — đánh dấu `[OWNER_CONFIRM: voucher active]`

---

## PHẦN 7 — ASSUMPTIONS & [FILL] CONVENTION

### Tag conventions

| Tag | Ý nghĩa | Khi dùng |
|-----|---------|---------|
| `[FILL]` | Thông tin chưa có, Owner cần điền | Giá, địa chỉ, số điện thoại, social handles |
| `[FILL: gợi ý]` | Thông tin chưa có nhưng AI đề xuất | `[FILL: ~65.000đ]` |
| `[OWNER_CONFIRM]` | AI đã suy luận, cần Owner xác nhận | Giả định về tone, timing |
| `[OWNER_CONFIRM: lý do]` | Giải thích tại sao cần xác nhận | `[OWNER_CONFIRM: offer OF-06 chưa active]` |

### Assumptions log

Mọi giả định AI đặt ra PHẢI được liệt kê trong `metadata.assumptions[]`:

```json
"assumptions": [
  "Combo Trưa OF-01 được giả định là ACTIVE — chưa xác nhận từ offer_engine.md",
  "Giờ đăng 11:00 dựa trên content_pillars.md Pillar 3 — Owner xác nhận lịch thực tế",
  "Ảnh dùng: chưa có file thực tế — image_brief là hướng dẫn chụp"
]
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — File tạo mới. Định nghĩa đầy đủ Input/Output schema, ID convention, platform matrix, pillar/angle mapping, offer integration rules, assumptions convention. | Claude Code (Builder) |
