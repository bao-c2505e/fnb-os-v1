# Approval Sheet Schema — Content Approval Queue

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Schema cho Google Sheet Tab: "Content Approval Queue"*
*Mỗi hàng = 1 content pack đang trong pipeline.*

---

## Tổng quan

Sheet này là bảng duyệt nội dung trung tâm của Vị Cuốn. AI Agent ghi dữ liệu vào đây. Owner duyệt ở đây. n8n đọc trạng thái từ đây để trigger workflow tiếp theo.

**Tên Sheet (Google Sheets tab):** `Content Approval Queue`
**Google Sheet file:** `FNB_OS_V1_CONTROL_CENTER`

---

## Cột Schema (Column Definitions)

### Cột A — content_id

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `content_id` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Format** | `VQ-[PLATFORM]-[PILLAR]-[YYYYMMDD]-[NNN]` |
| **Ví dụ** | `VQ-FB-PROD-20260527-001` |
| **Mô tả** | ID duy nhất của mỗi content pack. Không được trùng. |
| **Ai điền** | AI Agent (tự động tạo khi tạo content pack) |

**Format chi tiết:**
- `VQ` = Vị Cuốn (brand prefix)
- `FB` / `TK` / `IG` / `ZA` = Platform (Facebook / TikTok / Instagram / Zalo OA)
- `PROD` / `PROMO` / `BTS` / `STORY` / `COM` / `SEASON` = Pillar code
- `YYYYMMDD` = Ngày tạo
- `NNN` = Số thứ tự trong ngày (001–999)

---

### Cột B — brand

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `brand` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `Vi Cuon` |
| **Mô tả** | Tên thương hiệu. Luôn = "Vi Cuon". Giữ nguyên cho sau này khi mở rộng nhiều brand. |
| **Ai điền** | AI Agent |

---

### Cột C — platform

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `platform` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `Facebook`, `TikTok`, `Instagram`, `Zalo OA`, `Multi` |
| **Mô tả** | Nền tảng đăng bài. `Multi` = bài đăng trên nhiều nền tảng cùng lúc. |
| **Ai điền** | AI Agent |

---

### Cột D — content_type

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `content_type` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `Post`, `Reel`, `Story`, `Carousel`, `TikTok Video`, `Zalo Broadcast`, `Short Video` |
| **Mô tả** | Định dạng nội dung cụ thể. |
| **Ai điền** | AI Agent |

---

### Cột E — pillar

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `pillar` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `PROD`, `BTS`, `PROMO`, `STORY`, `COM`, `SEASON` |
| **Mô tả** | Content pillar theo `content_pillars.md`. Phải là một trong 6 pillar đã định nghĩa. |
| **Ai điền** | AI Agent |

---

### Cột F — angle

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `angle` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Format** | `ANG-[XX]` hoặc tên angle ngắn |
| **Ví dụ** | `ANG-01`, `hero-shot`, `asmr-cuon` |
| **Mô tả** | Góc tiếp cận nội dung theo `content_angles.md`. |
| **Ai điền** | AI Agent |

---

### Cột G — offer_code

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `offer_code` |
| **Kiểu dữ liệu** | String (nullable) |
| **Bắt buộc** | Không (chỉ điền nếu bài có offer) |
| **Ví dụ** | `OF-01`, `OF-04`, `VQ-LUNCH-20260601` |
| **Mô tả** | Mã offer theo `offer_engine.md`. Để trống nếu bài không có offer. |
| **Ai điền** | AI Agent |

---

### Cột H — caption

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `caption` |
| **Kiểu dữ liệu** | Long text |
| **Bắt buộc** | Có (trừ bài chỉ có video không cần caption) |
| **Giới hạn** | Facebook: ≤2.000 ký tự. TikTok: ≤150 ký tự. Instagram: ≤2.200 ký tự. |
| **Mô tả** | Caption chính của bài đăng. Đã qua AI Self-Check trước khi ghi vào đây. |
| **Ai điền** | AI Agent |

---

### Cột I — video_script

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `video_script` |
| **Kiểu dữ liệu** | Long text (nullable) |
| **Bắt buộc** | Không (chỉ có nếu content_type là video/reel) |
| **Mô tả** | Script quay video đã điền theo template từ `video_script_templates.md`. Bao gồm: hook, cảnh, lời thoại, text overlay, CTA. |
| **Ai điền** | AI Agent |

---

### Cột J — image_brief

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `image_brief` |
| **Kiểu dữ liệu** | Long text |
| **Bắt buộc** | Có (trừ bài chỉ có video) |
| **Mô tả** | Mô tả hình ảnh cần chụp/thiết kế: góc chụp, ánh sáng, bố cục, món ăn chính, props. |
| **Ai điền** | AI Agent |

---

### Cột K — design_brief

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `design_brief` |
| **Kiểu dữ liệu** | Long text (nullable) |
| **Bắt buộc** | Không (chỉ có nếu cần thiết kế đồ họa: banner, story frame, v.v.) |
| **Mô tả** | Hướng dẫn thiết kế: màu sắc, font, bố cục, text overlay, kích thước theo platform. |
| **Ai điền** | AI Agent |

---

### Cột L — target_persona

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `target_persona` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `Segment A`, `Segment B`, `Segment C`, `All`, tên persona cụ thể |
| **Mô tả** | Segment khách hàng mục tiêu theo `customer_brain.md`. |
| **Ai điền** | AI Agent |

---

### Cột M — status

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `status` |
| **Kiểu dữ liệu** | String (Enum) |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `IDEA`, `DRAFT`, `READY_FOR_REVIEW`, `REVISION_REQUESTED`, `APPROVED`, `SCHEDULE_PROPOSED`, `PUBLISHED_MANUAL`, `REJECTED`, `ARCHIVED` |
| **Mô tả** | Trạng thái hiện tại trong pipeline. Xem `status_lifecycle.md` để biết transition rules. |
| **Ai điền** | AI Agent (IDEA, DRAFT, READY_FOR_REVIEW) + Owner (APPROVED, REVISION_REQUESTED, REJECTED, SCHEDULE_PROPOSED, PUBLISHED_MANUAL) |

---

### Cột N — owner_decision

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `owner_decision` |
| **Kiểu dữ liệu** | String (nullable) |
| **Bắt buộc** | Chỉ khi Owner đã xem xét |
| **Giá trị hợp lệ** | `APPROVED`, `REVISION_REQUESTED`, `REJECTED` |
| **Mô tả** | Quyết định chính thức của Owner. Để trống khi chưa qua tay Owner. |
| **Ai điền** | **Chỉ Owner** |

---

### Cột O — revision_note

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `revision_note` |
| **Kiểu dữ liệu** | Long text (nullable) |
| **Bắt buộc** | Bắt buộc khi `owner_decision = REVISION_REQUESTED` hoặc `REJECTED` |
| **Mô tả** | Ghi chú của Owner về những gì cần sửa hoặc lý do từ chối. AI đọc và sửa theo. |
| **Ai điền** | **Chỉ Owner** |

---

### Cột P — approval_timestamp

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `approval_timestamp` |
| **Kiểu dữ liệu** | DateTime |
| **Bắt buộc** | Chỉ khi `owner_decision = APPROVED` |
| **Format** | `YYYY-MM-DD HH:MM:SS` (GMT+7) |
| **Mô tả** | Thời điểm Owner duyệt. Dùng để audit và báo cáo. |
| **Ai điền** | Owner hoặc n8n tự điền khi Owner bấm Approve |

---

### Cột Q — proposed_publish_date

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `proposed_publish_date` |
| **Kiểu dữ liệu** | DateTime |
| **Bắt buộc** | Khi status = `SCHEDULE_PROPOSED` |
| **Format** | `YYYY-MM-DD HH:MM` (GMT+7) |
| **Mô tả** | Ngày và giờ đăng bài thủ công do Owner đề xuất. Không tự động đăng. |
| **Ai điền** | **Chỉ Owner** |

---

### Cột R — manual_publish_link

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `manual_publish_link` |
| **Kiểu dữ liệu** | URL (nullable) |
| **Bắt buộc** | Khi status = `PUBLISHED_MANUAL` |
| **Ví dụ** | `https://www.facebook.com/...` |
| **Mô tả** | Link trực tiếp đến bài đã đăng. Dùng để báo cáo và theo dõi hiệu quả. |
| **Ai điền** | **Chỉ Owner** sau khi đăng xong |

---

### Cột S — created_by_agent

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `created_by_agent` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Giá trị hợp lệ** | `Claude Code (Builder)`, `n8n Content Agent`, `Manual (Owner)`, `Manual (Staff)` |
| **Mô tả** | Agent hoặc người đã tạo content pack này. Để audit và cải thiện chất lượng AI. |
| **Ai điền** | AI Agent (tự điền) / Người tạo |

---

### Cột T — source_brain_version

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `source_brain_version` |
| **Kiểu dữ liệu** | String |
| **Bắt buộc** | Có |
| **Format** | `Phase X.Y` hoặc `v[commit-hash]` |
| **Ví dụ** | `Phase 1.2`, `v75dd288` |
| **Mô tả** | Phiên bản Brain files AI dùng khi tạo nội dung. Nếu Brand Brain được cập nhật, nội dung cũ có thể cần review lại. |
| **Ai điền** | AI Agent |

---

### Cột U — safety_flags

| Trường | Giá trị |
|--------|---------|
| **Tên cột** | `safety_flags` |
| **Kiểu dữ liệu** | String / JSON (nullable) |
| **Bắt buộc** | Không (chỉ điền nếu có flag) |
| **Format** | Danh sách flags ngăn cách bằng `|` hoặc JSON array |
| **Ví dụ** | `PRICE_UNVERIFIED\|OFFER_NOT_IN_ENGINE` |
| **Giá trị hợp lệ** | Xem bảng Safety Flags bên dưới |
| **Mô tả** | Các cờ cảnh báo AI tự phát hiện trong quá trình tạo. Owner đọc và xử lý trước khi approve. |
| **Ai điền** | AI Agent (tự phát hiện và điền) |

**Bảng Safety Flags:**

| Flag | Ý nghĩa | Mức độ |
|------|---------|--------|
| `PRICE_UNVERIFIED` | Có giá trong bài chưa xác nhận từ menu_brain.md | 🔴 BLOCKER |
| `OFFER_NOT_IN_ENGINE` | Offer được nhắc chưa có trong offer_engine.md | 🔴 BLOCKER |
| `HEALTH_CLAIM_DETECTED` | Phát hiện claim sức khỏe chưa có căn cứ | 🔴 BLOCKER |
| `FAKE_URGENCY_RISK` | Caption có dấu hiệu fake urgency | 🔴 BLOCKER |
| `COMPETITOR_MENTION` | Phát hiện nhắc đến đối thủ | 🔴 BLOCKER |
| `EMOJI_OVERLOAD` | Emoji > 3 cái trong caption | 🟠 WARNING |
| `MISSING_HASHTAG` | Thiếu hashtag cốt lõi (#VịCuốn) | 🟠 WARNING |
| `CAPTION_TOO_LONG` | Caption vượt giới hạn platform | 🟠 WARNING |
| `TONE_MISMATCH` | Giọng điệu không phù hợp brand voice | 🟡 NOTE |
| `IMAGE_NOT_SPECIFIED` | Chưa có image brief cụ thể | 🟡 NOTE |
| `OFFER_EXPIRED_RISK` | Offer có nguy cơ hết hạn trước ngày đăng | 🟠 WARNING |

---

## Validation Rules

```
REQUIRED khi tạo mới:
- content_id: unique, match format VQ-[PLATFORM]-[PILLAR]-[YYYYMMDD]-[NNN]
- brand: = "Vi Cuon"
- platform: in ['Facebook','TikTok','Instagram','Zalo OA','Multi']
- content_type: in valid list
- pillar: in ['PROD','BTS','PROMO','STORY','COM','SEASON']
- angle: not empty
- caption OR video_script: at least one must be present
- target_persona: not empty
- status: = 'IDEA' or 'DRAFT' on create
- created_by_agent: not empty
- source_brain_version: not empty

REQUIRED khi status → READY_FOR_REVIEW:
- caption OR video_script: filled
- image_brief: filled (unless video only)
- safety_flags: AI must run check — empty string means "no flags found"

REQUIRED khi owner_decision = APPROVED:
- approval_timestamp: filled
- owner_decision: = 'APPROVED'

REQUIRED khi status → SCHEDULE_PROPOSED:
- proposed_publish_date: filled

REQUIRED khi status → PUBLISHED_MANUAL:
- manual_publish_link: filled
```

---

## Google Sheets Setup Notes

- **Freeze row 1** (header row)
- **Cột M (status):** Dùng Data Validation → Dropdown list với 9 giá trị
- **Cột N (owner_decision):** Dùng Data Validation → Dropdown: `APPROVED | REVISION_REQUESTED | REJECTED`
- **Cột P (approval_timestamp):** Format → Date time
- **Cột Q (proposed_publish_date):** Format → Date time
- **Màu sắc hàng (Conditional Formatting):**
  - `READY_FOR_REVIEW` → nền vàng nhạt (cần Owner xem)
  - `APPROVED` → nền xanh lá nhạt
  - `REVISION_REQUESTED` → nền cam nhạt
  - `REJECTED` → nền đỏ nhạt
  - `PUBLISHED_MANUAL` → nền xanh dương nhạt
  - `ARCHIVED` → nền xám nhạt

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. 21 cột với validation rules, safety flags, Google Sheets setup notes. | Claude Code (Builder) |
