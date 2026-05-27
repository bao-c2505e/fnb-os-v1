# Phase 1.1 — Brand Brain Foundation

Created By: Claude Code (Builder) — 2026-05-27
Phase: 1.1
Command: CMD-1.1-001
Status: REVIEW_REQUESTED

---

## Mục Tiêu (Objective)

Xây dựng Brand Brain Foundation — tầng kiến thức cốt lõi cho Vị Cuốn Growth OS. Đây là nền tảng để tất cả AI agents (Gemini Content, ChatGPT, Claude) hiểu đúng thương hiệu, menu, khách hàng, và quy tắc trước khi tạo bất kỳ nội dung marketing nào.

---

## Phạm Vi (Scope)

| File | Trạng thái | Nội dung |
|------|-----------|---------|
| `01_BRAIN/brand_brain.md` | ✅ FILLED | Brand identity, positioning, mission, values, tone, visual direction, USPs, AI safety rules |
| `01_BRAIN/menu_brain.md` | ✅ FILLED | Các danh mục menu (bánh tráng cuốn, bún trộn mắm nêm, gỏi cuốn, heo quay/nướng lu), combos, drinks, upsell logic, FAQs |
| `01_BRAIN/customer_brain.md` | ✅ FILLED | 5 customer segments (văn phòng, gia đình, sinh viên, healthy, du lịch Vinh), customer journey, CRM stages, FAQ answers, escalation rules |
| `01_BRAIN/content_brain.md` | ✅ FILLED | 5 content pillars, posting schedule, weekly calendar template, caption formulas với ví dụ thực tế, hashtag banks, approval flow, AI content constraints |
| `01_BRAIN/offer_brain.md` | ✅ FILLED | Active offers (Combo Trưa, Cuối Tuần, Gia Đình, Lần Đầu), offer rules, upsell/cross-sell triggers, promotion calendar, offer safety rules |
| `01_BRAIN/design_brain.md` | ✅ FILLED | Palette direction (warm street food), typography gợi ý, photography direction, creative formats, design brief format, asset storage structure |

**Không trong phạm vi Phase 1.1:**
- `01_BRAIN/ads_brain.md` — Phase 1.2+
- `01_BRAIN/crm_brain.md` — Phase 1.2+
- `01_BRAIN/comment_reply_brain.md` — Phase 1.2+
- n8n workflows — Phase 1.3+
- Google Sheet / Drive tạo thực tế — Phase 1.2+

---

## Assumptions Đã Thực Hiện

Tất cả nội dung brand_brain được xây dựng dựa trên context của Owner. Các assumptions cần Owner xác nhận:

| # | Assumption | File | Cần Owner xác nhận |
|---|-----------|------|-------------------|
| A-1 | Location: Vinh, Nghệ An | brand_brain.md | ✅ Đã biết từ brief |
| A-2 | Price range 60–80k/người | brand_brain.md, menu_brain.md | ✅ Đã biết từ brief |
| A-3 | Style: street food warm premium | brand_brain.md | ✅ Đã biết từ brief |
| A-4 | Products: bánh tráng cuốn, bún trộn mắm nêm, gỏi cuốn, heo quay/nướng lu | menu_brain.md | ✅ Đã biết từ brief |
| A-5 | Giá đơn lẻ 35–55k/phần (để đạt 60–80k khi kết hợp) | menu_brain.md | ⚠️ GỢI Ý — Owner điền giá thật |
| A-6 | Combo Trưa Thứ 2–6, 11:00–14:00 | menu_brain.md, offer_brain.md | ⚠️ GỢI Ý — Owner xác nhận |
| A-7 | Palette đỏ nâu ấm + kem ngà + xanh lá tươi | design_brain.md | ⚠️ GỢI Ý — Owner xác nhận màu từ Brand Kit |
| A-8 | Font Be Vietnam Pro / Inter | design_brain.md | ⚠️ GỢI Ý — Owner xác nhận từ Brand Kit |
| A-9 | 5 posting days/week Facebook, 3–4 TikTok | content_brain.md | ⚠️ GỢI Ý — Owner xác nhận lịch |
| A-10 | Tagline: "Cuốn đúng vị — Ấm lòng người" | brand_brain.md | ⚠️ GỢI Ý — Owner xác nhận hoặc thay |
| A-11 | Sinh viên ĐH Vinh là một segment | customer_brain.md | ⚠️ GỢI Ý dựa trên địa lý — Owner xác nhận |

---

## [FILL] Items Còn Lại — Owner Phải Điền

| # | Item | File | Lý do cần Owner |
|---|------|------|----------------|
| F-1 | Năm thành lập | brand_brain.md | Chỉ Owner biết |
| F-2 | Địa chỉ đầy đủ | brand_brain.md, customer_brain.md | Chỉ Owner biết |
| F-3 | Giờ mở cửa chính xác | brand_brain.md, customer_brain.md | Chỉ Owner biết |
| F-4 | Số điện thoại | brand_brain.md | Chỉ Owner biết |
| F-5 | Social media handles & URLs | brand_brain.md | Chỉ Owner biết |
| F-6 | Giá thực từng món | menu_brain.md | Chỉ Owner biết |
| F-7 | Màu hex chính thức (Brand Kit) | brand_brain.md, design_brain.md | Từ Brand Kit của Owner |
| F-8 | Font chính thức | design_brain.md | Từ Brand Kit |
| F-9 | Google Drive links | design_brain.md | Owner tạo folder |
| F-10 | Delivery platforms đang dùng | brand_brain.md | Chỉ Owner biết |
| F-11 | Tên đối thủ cạnh tranh | brand_brain.md | Chỉ Owner biết |
| F-12 | Ngưỡng miễn phí giao hàng | offer_brain.md | Chỉ Owner quyết định |
| F-13 | % Discount lần đầu | offer_brain.md | Chỉ Owner quyết định |
| F-14 | Facebook Messenger link | customer_brain.md | Từ trang Facebook của Owner |
| F-15 | Bãi đỗ xe | customer_brain.md | Chỉ Owner biết |

**Tổng: 15 items cần Owner fill. Hầu hết là thông tin vận hành — không cần thiết để Codex review hay Phase 1.2 bắt đầu.**

---

## Safety Rules (Brand Brain Level)

Các quy tắc này áp dụng cho TẤT CẢ agents khi sử dụng Brand Brain:

| Quy tắc | Chi tiết |
|---------|---------|
| Không tự sáng tác giá | Chỉ dùng giá từ `menu_brain.md` |
| Không claim sức khỏe | Không viết "tốt cho sức khỏe", "giảm cân" |
| Không đề cập đối thủ | Kể cả so sánh tích cực |
| Không dùng ảnh stock | Chỉ ảnh thật của quán |
| Không đăng chưa qua duyệt | Owner approve 100% trước khi đăng |
| Không auto-reply | Comment reply phải qua người thật |
| Không tự tạo offer | Chỉ quảng bá offer đã có trong `offer_brain.md` |
| Không suy diễn thông tin quán | Nếu không biết → nói "Bạn inbox để hỏi thêm nhé!" |

---

## Done Criteria

- [x] `01_BRAIN/brand_brain.md` — Brand identity, mission, values, tone, USPs, AI safety rules
- [x] `01_BRAIN/menu_brain.md` — Danh mục menu, combos, upsell logic, FAQs
- [x] `01_BRAIN/customer_brain.md` — 5 segments, customer journey, CRM stages, escalation rules
- [x] `01_BRAIN/content_brain.md` — Content pillars, posting schedule, caption formulas, hashtags, approval flow
- [x] `01_BRAIN/offer_brain.md` — Offers, rules, upsell/cross-sell, promotion calendar
- [x] `01_BRAIN/design_brain.md` — Palette direction, typography, photography, brief format
- [x] Tất cả assumptions được đánh dấu rõ
- [x] Tất cả [FILL] items được liệt kê với lý do
- [x] Không có secrets hardcoded
- [x] Không có Phase 1 production workflow tạo ra
- [x] Không có auto-post/auto-reply
- [x] Không có n8n workflow mới
- [x] Không có commit, không có push
