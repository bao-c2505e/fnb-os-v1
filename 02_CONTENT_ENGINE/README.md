# 02_CONTENT_ENGINE — Vị Cuốn Content & Offer Engine

*Phase 1.2 — Content Pillar & Offer Engine*
*Được xây từ Brand Brain (Phase 1.1). Dùng bởi AI Content Agent và Owner.*

---

## Mục đích

Thư mục `02_CONTENT_ENGINE/` là bộ não sản xuất nội dung của Vị Cuốn.

Nó cung cấp:
1. **Định hướng chiến lược** — Pillar nào, Angle nào, tần suất bao nhiêu
2. **Template tái sử dụng** — Caption + Video Script sẵn sàng điền vào
3. **Logic Offer** — Offer nào, khi nào, deliver như thế nào
4. **Quy tắc an toàn** — Những gì KHÔNG được làm, quy trình duyệt

---

## Files trong thư mục

| File | Mục đích | Dùng khi nào |
|------|---------|-------------|
| [content_pillars.md](content_pillars.md) | 6 content pillars với mục đích, persona, examples, platforms | Lên kế hoạch content tuần/tháng |
| [content_angles.md](content_angles.md) | 25 góc nội dung tái sử dụng | Chọn angle cho từng bài cụ thể |
| [caption_templates.md](caption_templates.md) | 19 mẫu caption đầy đủ (PROD, BTS, PROMO, STORY, COM) | Viết caption từng bài |
| [video_script_templates.md](video_script_templates.md) | 10 kịch bản video ngắn TikTok/Reels | Quay và edit video |
| [offer_engine.md](offer_engine.md) | 9 loại offer + upsell logic + voucher system | Khi tạo/quảng bá offer |
| [approval_rules.md](approval_rules.md) | Quy trình duyệt, checklist, safety rules | Trước khi đăng bất kỳ bài nào |

---

## Cách sử dụng (Luồng tạo nội dung)

```
1. Xác định ngày / khung giờ / platform cần content

2. Mở content_pillars.md
   → Chọn Pillar phù hợp (PROD / BTS / PROMO / STORY / COM / SEASON)

3. Mở content_angles.md
   → Chọn Angle cụ thể trong Pillar đó

4. Mở caption_templates.md hoặc video_script_templates.md
   → Chọn template phù hợp → Điền [FILL] → Kiểm tra giá với menu_brain.md

5. Nếu bài có offer → mở offer_engine.md
   → Xác nhận offer ACTIVE → lấy thông tin giá/thời hạn/voucher

6. Mở approval_rules.md
   → Chạy AI Self-Check → Gửi Owner duyệt

7. Owner approve → Owner đăng tay / lên lịch thủ công
   → LƯU Ý: AI KHÔNG tự đăng
```

---

## Nguồn gốc dữ liệu

Tất cả nội dung trong `02_CONTENT_ENGINE/` được xây dựa trên Brand Brain từ Phase 1.1:

| File nguồn | Thông tin lấy từ đây |
|-----------|---------------------|
| `01_BRAIN/brand_brain.md` | Brand voice, tone, values, safety rules |
| `01_BRAIN/menu_brain.md` | Tên món, giá tham chiếu, mô tả sản phẩm |
| `01_BRAIN/customer_brain.md` | Segments, persona, pain points |
| `01_BRAIN/content_brain.md` | Pillar định nghĩa ban đầu, posting schedule |
| `01_BRAIN/offer_brain.md` | Offer framework, voucher rules, safety |
| `01_BRAIN/design_brain.md` | Visual direction cho brief ảnh/video |

**Nguyên tắc:** Nếu `01_BRAIN/` và `02_CONTENT_ENGINE/` mâu thuẫn → `01_BRAIN/` là nguồn đúng. Báo Owner cập nhật.

---

## Quy tắc quan trọng nhất

| # | Quy tắc | Không thể thương lượng |
|---|---------|----------------------|
| 1 | AI KHÔNG tự đăng bài | ❌ Luôn luôn |
| 2 | Mọi nội dung phải Owner approve | ❌ Luôn luôn |
| 3 | Giá lấy từ menu_brain.md / offer_engine.md | ❌ Luôn luôn |
| 4 | KHÔNG claim sức khỏe / dinh dưỡng | ❌ Luôn luôn |
| 5 | KHÔNG fake review / fake urgency | ❌ Luôn luôn |
| 6 | KHÔNG nhắc tên đối thủ | ❌ Luôn luôn |

---

## Phụ thuộc (Cần điền trước khi dùng production)

Các giá trị [FILL] còn lại trong Brand Brain cần Owner điền để Content Engine hoạt động tốt nhất:

- `brand_brain.md`: Địa chỉ đầy đủ, giờ mở cửa, handles mạng xã hội, số điện thoại
- `menu_brain.md`: Giá thật của từng món và combo
- `offer_brain.md` / `offer_engine.md`: Trạng thái ACTIVE/INACTIVE của từng offer, giá combo thật
- `content_brain.md`: Hashtag chiến dịch cụ thể khi có

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.2 — Thư mục và tất cả files tạo mới. 6 content pillars, 25 angles, 19 caption templates, 10 video scripts, 9 offer types, approval rules. | Claude Code (Builder) |
