# Manual Content Pack Runbook — Vị Cuốn

*Phase 1.6 — Manual Content Pack Runbook*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Dành cho: Owner tự chạy một Content Pack hoàn chỉnh bằng tay — không cần code, không cần kỹ thuật*

---

## Mục đích

Runbook này hướng dẫn Owner tạo một bài content hoàn chỉnh theo đúng quy trình FnB OS V1 — từ chọn nội dung đến duyệt và đăng. Đây là **lần chạy tay đầu tiên** để kiểm tra toàn bộ hệ thống đã xây từ Phase 1.1 đến 1.5 trước khi tự động hóa.

**Thời gian dự kiến:** 20–40 phút cho một Content Pack đầu tiên.

---

## Sơ đồ Tổng thể

```
[BƯỚC 1] Chuẩn bị        → Owner kiểm tra [FILL] nào cần thiết
[BƯỚC 2] Chọn nội dung   → Owner điền Input Brief
[BƯỚC 3] Tạo draft       → Owner gửi brief cho AI Worker (Claude Code)
[BƯỚC 4] AI tạo pack     → AI trả về Content Pack DRAFT
[BƯỚC 5] Validate        → Owner chạy validation checklist
[BƯỚC 6] Approval        → Owner tự duyệt (APPROVED / REVISE / REJECT)
[BƯỚC 7] Đăng bài        → Owner đăng tay sau khi APPROVED
```

---

## ⛔ STOP RULES — Dừng Ngay Khi Có Một Trong Các Tình Huống Sau

Phải dừng toàn bộ quy trình và không đăng bài nếu:

| # | Tình huống | Hành động |
|---|-----------|----------|
| S1 | Caption có giá cụ thể nhưng Owner chưa xác nhận giá đó trong `offer_engine.md` | Dừng. Điền giá thật vào `offer_engine.md` trước. |
| S2 | Caption có địa chỉ nhưng địa chỉ thật chưa được điền vào `brand_brain.md` | Dừng. Điền địa chỉ thật trước. |
| S3 | Caption có số điện thoại nhưng SĐT thật chưa được điền vào `brand_brain.md` | Dừng. Điền SĐT thật trước. |
| S4 | Caption có chương trình khuyến mãi cụ thể nhưng Owner chưa xác nhận KM đó tồn tại | Dừng. Xác nhận KM thật trước. |
| S5 | Caption gợi ý discount/review giả mạo | Dừng. Yêu cầu AI viết lại. |
| S6 | Output của AI có lệnh tự đăng bài, gọi API, hoặc gửi tin nhắn tự động | Dừng ngay. Báo cáo lỗi. |
| S7 | `approval.status` không phải `DRAFT` trong output AI | Dừng. AI Worker đã sai — báo cáo lỗi. |
| S8 | Owner chưa APPROVED mà có bất kỳ ai/hệ thống nào đăng bài | Dừng. Không chấp nhận dưới bất kỳ hình thức nào. |
| S9 | Content Pack chứa claim sức khỏe ("tốt cho sức khỏe", "giảm cân", "detox") | Dừng. Yêu cầu AI viết lại hoàn toàn. |
| S10 | Content Pack nhắc tên quán đối thủ | Dừng. Yêu cầu AI xóa và viết lại. |

---

## BƯỚC 1 — CHUẨN BỊ (5 phút)

### 1.1 Kiểm tra [FILL] Cần thiết

Trước khi tạo bất kỳ Content Pack nào, Owner cần biết mình đang có gì và thiếu gì.

**Mở file:** `01_BRAIN/brand_brain.md`

Tìm và kiểm tra trạng thái các field này:

| Field | Trạng thái hiện tại | Cần điền không? |
|-------|--------------------|----|
| Địa chỉ chi tiết | `[FILL: địa chỉ chi tiết]` | Có (cho CTA "ghé quán") |
| Số điện thoại | `[FILL: số điện thoại]` | Có (cho CTA "gọi ngay") |
| Giờ mở cửa | `[FILL: e.g., 10:00–21:00]` | Có (nếu đề cập trong caption) |
| Facebook handle | `[FILL: @VịCuốn]` | Có (nếu tag trong caption) |
| Tagline chính thức | chưa xác nhận | Tùy chọn |

**Mở file:** `02_CONTENT_ENGINE/offer_engine.md`

Kiểm tra offer sẽ dùng:

| Offer | Cần kiểm tra |
|-------|-------------|
| OF-01 Combo Trưa | Giá + trạng thái ACTIVE/INACTIVE |
| OF-02 Combo Cuối Tuần | Giá + trạng thái |
| OF-03 Combo Gia Đình | Giá + trạng thái |
| OF-06 Deal Ngày Mưa | Trạng thái (chỉ bật khi mưa thật) |

**Quyết định:** Nếu thiếu thông tin quan trọng → Owner điền trước hoặc chọn loại content không cần (ví dụ: BTS content không cần giá).

### 1.2 Chọn Mục tiêu Hôm Nay

Trả lời câu hỏi: **Hôm nay tôi muốn đạt được gì với bài này?**

| Mục tiêu | Chọn khi | Pillar phù hợp |
|---------|---------|---------------|
| **awareness** | Muốn thêm người biết đến Vị Cuốn | BTS, STORY |
| **engagement** | Muốn thêm tương tác (comment, share) | PROD, COM, SEASON |
| **conversion** | Muốn người ta đặt hàng ngay | PROMO, PROD |
| **retention** | Muốn khách cũ quay lại | PROMO (OF-05), COM |
| **education** | Muốn giải thích tại sao Vị Cuốn ngon | STORY, BTS |

---

## BƯỚC 2 — ĐIỀN INPUT BRIEF (5–10 phút)

**Mở file:** `04_CONTENT_PACK_GENERATOR/input_brief_template.md`

Copy phần **BRIEF FORM** và điền vào đây (hoặc mở file và điền trực tiếp):

```
═══════════════════════════════════════════════════════════
INPUT BRIEF — CONTENT PACK — VỊ CUỐN
═══════════════════════════════════════════════════════════
Ngày tạo brief:     ___________  (điền ngày hôm nay)
Người tạo brief:    Owner
Số pack cần tạo:    1
═══════════════════════════════════════════════════════════

brand:          [x] Vi Cuon

platform:       [ ] Facebook   [ ] TikTok   [ ] Instagram
                [ ] Zalo OA

objective:      [ ] awareness  [ ] engagement  [ ] conversion
                [ ] retention  [ ] education

target_persona: [ ] Segment A  (văn phòng, bữa trưa)
                [ ] Segment B  (gia đình, cuối tuần)
                [ ] Segment C  (sinh viên, giá nhạy)
                [ ] All

pillar:         [ ] PROD  [ ] BTS  [ ] PROMO  [ ] STORY
                [ ] COM   [ ] SEASON

angle:          [ ] AUTO  (AI tự chọn — khuyến nghị cho lần đầu)
                hoặc chọn angle cụ thể từ content_angles.md

content_type:   [ ] Post  [ ] Reel  [ ] Story  [ ] Carousel
                [ ] TikTok Video  [ ] Zalo Broadcast

offer_type:     [ ] Không có
                [ ] OF-01  [ ] OF-02  [ ] OF-03  [ ] OF-04
                [ ] OF-05  [ ] OF-06  [ ] OF-07  [ ] OF-08

owner_notes:
  ___________________________________________________________
  ___________________________________________________________

═══════════════════════════════════════════════════════════
```

**Gợi ý nhanh cho lần đầu:**
- Chọn **Facebook + PROD + angle AUTO + không có offer** — đây là bài dễ nhất, ít [FILL] nhất.
- Hoặc xem **Bước 3** trong `manual_test_input_examples.md` để dùng ngay một trong 3 kịch bản có sẵn.

---

## BƯỚC 3 — GỬI BRIEF CHO AI WORKER (2 phút)

### 3.1 Chuẩn bị Prompt

**Mở file:** `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md`

Copy toàn bộ nội dung trong block `═══` lớn (từ "NHIỆM VỤ: TẠO DRAFT CONTENT PACK" đến "KẾT THÚC PROMPT TEMPLATE").

### 3.2 Điền Placeholder

Thay thế từng `{{PLACEHOLDER}}` bằng giá trị từ brief đã điền ở Bước 2:

| Placeholder | Điền bằng |
|-------------|----------|
| `{{BRAND}}` | Vi Cuon |
| `{{PLATFORM}}` | Facebook (hoặc platform bạn chọn) |
| `{{OBJECTIVE}}` | conversion (hoặc objective bạn chọn) |
| `{{TARGET_PERSONA}}` | Segment A (hoặc persona bạn chọn) |
| `{{PILLAR}}` | PROMO (hoặc pillar bạn chọn) |
| `{{ANGLE}}` | AUTO (hoặc angle cụ thể) |
| `{{OFFER_TYPE}}` | OF-01 (hoặc null nếu không có offer) |
| `{{CONTENT_TYPE}}` | Post |
| `{{TONE}}` | Mặc định Brand Voice |
| `{{CONSTRAINTS}}` | (ghi ràng buộc nếu có, hoặc bỏ trống) |
| `{{OWNER_NOTES}}` | (ghi chú thêm của bạn) |
| `{{DATE_TODAY}}` | 2026-05-27 (ngày hôm nay) |

### 3.3 Gửi cho Claude Code

1. Mở Claude Code (chat với Builder Agent)
2. Paste toàn bộ prompt đã điền placeholder
3. Gửi
4. Đợi AI trả về Content Pack DRAFT

**Lưu ý:** AI sẽ trả về 2 phần — BLOCK A (Markdown, dễ đọc) và BLOCK B (JSON). Lưu cả hai.

---

## BƯỚC 4 — NHẬN VÀ LƯU CONTENT PACK DRAFT (2 phút)

Khi AI trả về Content Pack, làm theo:

1. **Copy BLOCK A** (Markdown) — lưu vào Google Drive hoặc file `.md` mới theo tên `VQ-[PLATFORM]-[PILLAR]-[NGAY]-001.md`

2. **Copy BLOCK B** (JSON) — lưu vào Google Sheet hoặc file riêng

3. **Kiểm tra nhanh 3 điều:**
   - `approval.status` = `DRAFT` — nếu không → STOP (rule S7)
   - Không có lệnh auto-post trong output — nếu có → STOP (rule S6)
   - Caption không có claim sức khỏe — nếu có → STOP (rule S9)

---

## BƯỚC 5 — VALIDATE (10 phút)

**Mở file:** `05_VALIDATION_QUEUE/validation_checklist.md`

Copy một bản checklist và điền cho Content Pack vừa nhận:

### Quick Scan (2 phút trước)

| # | Câu hỏi | Trả lời |
|---|---------|---------|
| Q1 | Content ID có đúng format `VQ-[PLAT]-[PILLAR]-[YYYYMMDD]-[SEQ]`? | [ ] Có [ ] Không |
| Q2 | `approval.status = DRAFT`? | [ ] Có [ ] Không |
| Q3 | Caption không có secret/credential? | [ ] Có [ ] Không |
| Q4 | Caption không nhắc tên đối thủ? | [ ] Có [ ] Không |
| Q5 | Caption không có claim sức khỏe? | [ ] Có [ ] Không |
| Q6 | Caption không có offer tự tạo? | [ ] Có [ ] Không |
| Q7 | Không có lệnh auto-post trong output? | [ ] Có [ ] Không |

**Nếu bất kỳ Q nào = Không → STOP. Xem STOP RULES.**

### Validate Đầy đủ 7 Nhóm

Theo `05_VALIDATION_QUEUE/content_pack_validation_rules.md`:

- **V1 Brand Fit** — Giọng văn, emoji, hashtag
- **V2 Product Fit** — Món ăn có trong menu, giá có nguồn
- **V3 Platform Fit** — content_type đúng, độ dài caption đúng
- **V4 Offer Validity** — Offer có trong offer_engine, không áp lực giả
- **V5 Safety** — Không có lệnh tự động, không có thông tin cá nhân khách
- **V6 Owner Readiness** — Mọi [FILL] quan trọng được ghi rõ
- **V7 [FILL] Handling** — [FILL] địa chỉ/SĐT đúng chuẩn

### Set Trạng thái Validation

Theo `05_VALIDATION_QUEUE/revision_rules.md`:

| Kết quả | Action |
|---------|--------|
| Có BLOCKER | Yêu cầu AI sửa → quay lại Bước 3 |
| Còn [FILL] quan trọng | Điền vào `brand_brain.md` / `offer_engine.md` → AI cập nhật → re-validate |
| Brand/content fit yếu | Yêu cầu AI chỉnh → quay lại Bước 3 |
| Tất cả PASS | Set `validation_status = READY_FOR_REVIEW` → sang Bước 6 |

---

## BƯỚC 6 — OWNER APPROVAL (5 phút)

**Mở file:** `03_APPROVAL_PIPELINE/owner_review_checklist.md`

Đọc qua 6 phần checklist và đưa ra quyết định:

### Quyết định

```
╔══════════════════════════════════════════════════════╗
║            OWNER APPROVAL DECISION                   ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Content Pack ID: _______________________________    ║
║                                                      ║
║  [ ] APPROVED                                        ║
║      → Điền: approval_timestamp = [ngày giờ]         ║
║      → Điền: proposed_publish_date = [ngày đăng]     ║
║      → Sang Bước 7                                   ║
║                                                      ║
║  [ ] REVISION_REQUESTED                              ║
║      → Ghi revision_note:                            ║
║        1. ______________________________________     ║
║        2. ______________________________________     ║
║      → Gửi revision note cho AI → quay lại Bước 3   ║
║      → Tối đa 3 lần revision trước khi REJECT        ║
║                                                      ║
║  [ ] REJECTED                                        ║
║      → Ghi lý do: ____________________________       ║
║      → Không đăng. Brief lại từ đầu nếu muốn.       ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

**4 câu hỏi tự hỏi trước khi APPROVE:**
1. Tôi có tự tin đăng bài này ngay bây giờ không?
2. Bài này có thể gây hiểu nhầm không?
3. Khách hàng sẽ cảm thấy gì khi đọc bài này — thèm ăn hay hoang mang?
4. Nếu bài bị screenshot và share rộng, tôi có OK không?

**Nếu do dự bất kỳ câu nào → REVISION_REQUESTED, không phải APPROVE.**

---

## BƯỚC 7 — ĐĂNG BÀI THỦ CÔNG (2–5 phút)

**CHỈ thực hiện khi `owner_decision = APPROVED`.**

### 7.1 Kiểm tra lần cuối trước khi đăng

| # | Kiểm tra | OK? |
|---|---------|-----|
| C1 | `approval.status = APPROVED` (không phải DRAFT) | [ ] |
| C2 | Caption đã hoàn thiện, không còn [FILL] quan trọng | [ ] |
| C3 | Đã có ảnh/video thật để đăng kèm | [ ] |
| C4 | Ngày và giờ đăng đã được chọn | [ ] |
| C5 | Không có lệnh auto-post — Owner đăng tay | [ ] |

**Nếu bất kỳ C nào chưa OK → chưa đăng.**

### 7.2 Đăng tay

1. Mở Facebook / TikTok / Instagram / Zalo OA tương ứng
2. Copy caption đã APPROVED từ Content Pack
3. Upload ảnh/video thật của quán (không dùng ảnh stock)
4. Kiểm tra preview một lần nữa
5. Đăng bài

### 7.3 Ghi lại sau khi đăng

Sau khi đăng xong, ghi vào Content Pack:

| Field | Giá trị |
|-------|---------|
| `status` | `PUBLISHED_MANUAL` |
| `manual_publish_link` | Link bài đã đăng |
| `published_at` | Thời điểm đăng (VD: `2026-05-27 11:00 +07:00`) |

---

## Theo dõi Kết quả (Sau 24–48 giờ)

Xem lại bài đã đăng và ghi nhận:

| Metric | Ghi nhận |
|--------|---------|
| Lượt thích/react | |
| Lượt comment | |
| Lượt share | |
| Inbox từ bài này | |
| Đơn hàng từ bài này | |

Đây là dữ liệu thực tế để cải thiện content pack tiếp theo.

---

## Tóm tắt Quy trình (1 trang)

```
Owner ─┬─[1] Kiểm tra [FILL] cần thiết
       ├─[2] Điền Input Brief (chọn platform/pillar/angle/offer)
       ├─[3] Gửi brief + prompt template cho AI Worker
       ├─[4] Nhận Content Pack DRAFT từ AI
       ├─[5] Validate 7 nhóm (Brand/Product/Platform/Offer/Safety/Readiness/[FILL])
       │     ↑ nếu có vấn đề → quay về [3] yêu cầu AI sửa
       ├─[6] Owner tự APPROVE / REVISE / REJECT
       │     ↑ nếu REVISE → quay về [3]
       └─[7] Đăng tay sau khi APPROVED → ghi link bài
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.6 — File tạo mới. 7 bước runbook, 10 STOP rules, Quick Scan, Owner Decision form, post-publish tracking. | Claude Code (Builder) |
