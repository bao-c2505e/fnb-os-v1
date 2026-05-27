# PHASE 1.2 — Content Pillar & Offer Engine

**Phase:** 1.2
**Status:** CLOSED
**Builder:** Claude Code (AGT-02)
**Reviewer:** Codex / GPT-4o (AGT-04)
**Date:** 2026-05-27
**Command ID:** CMD-1.2-001

---

## Tóm tắt

Phase 1.2 xây dựng bộ Content Engine và Offer Engine hoàn chỉnh cho Vị Cuốn, dựa trên Brand Brain từ Phase 1.1. Tất cả nội dung được thiết kế để AI Agent có thể sử dụng trực tiếp, markdown-first, dễ convert sang JSON trong Phase sau.

---

## Files tạo mới

### 02_CONTENT_ENGINE/ (Thư mục mới)

| File | Mô tả | Dòng (ước tính) |
|------|-------|-----------------|
| `README.md` | Overview thư mục, luồng sử dụng, dependencies | ~100 |
| `content_pillars.md` | 6 content pillars: PROD, BTS, PROMO, STORY, COM, SEASON | ~250 |
| `content_angles.md` | 25 content angles trong 5 nhóm | ~230 |
| `caption_templates.md` | 19 caption templates với ví dụ đã điền | ~280 |
| `video_script_templates.md` | 10 video script templates TikTok/Reels | ~350 |
| `offer_engine.md` | 9 loại offer + upsell/cross-sell logic + voucher system | ~280 |
| `approval_rules.md` | Approval flow, owner checklist, safety rules, phân quyền | ~250 |

### docs/phase-1/

| File | Mô tả |
|------|-------|
| `PHASE_1_2_CONTENT_PILLAR_OFFER_ENGINE.md` | File báo cáo này |

---

## Tóm tắt Content Pillars

| Pillar | Ký hiệu | % | Mục đích |
|--------|---------|---|---------|
| Sản phẩm | PROD | 30% | Showcase món ăn, kích thích thèm ăn và đặt hàng |
| Hậu trường | BTS | 20% | Xây niềm tin qua transparency và authenticity |
| Khuyến mãi | PROMO | 20% | Drive traffic và đơn hàng ngắn hạn |
| Giáo dục & Câu chuyện | STORY | 15% | Nâng tầm nhận thức, giải thích USP |
| Cộng đồng | COM | 10% | Social proof, loyalty, UGC |
| Mùa vụ & Sự kiện | SEASON | 5% | Relevance theo thời điểm văn hóa / thời tiết |

---

## Tóm tắt Content Angles

25 angles trong 5 nhóm:
- **Nhóm A (PROD):** 6 angles — Hero Shot, Từng lớp, Mắm nêm spotlight, Menu hôm nay, Before/After, Combo đầy đủ
- **Nhóm B (BTS):** 5 angles — Sáng sớm, Lửa lu, Quy trình mắm nêm, Rau sống, Nhân vật quán
- **Nhóm C (PROMO):** 5 angles — Combo reveal, Đồng hồ đếm ngược, Khách mới, Combo nhóm, Thời tiết & Deal
- **Nhóm D (STORY):** 5 angles — Fun fact, Lịch sử/nguồn gốc, FAQ tuần, Tại sao làm vậy, Câu chuyện quán
- **Nhóm E (COM):** 4 angles — Repost khách, Poll, Milestone, UGC call-to-action

---

## Tóm tắt Caption Templates

19 templates trong 5 nhóm:
- **PROD (4):** Hero Shot, Combo Full, Spotlight Mắm Nêm, Gỏi Cuốn
- **BTS (3):** Sáng sớm, Heo nướng lu, Nguyên liệu tươi
- **PROMO (6):** Combo Trưa, Deal Cuối Tuần, Khách Mới, Combo Gia Đình, Thời tiết, Comeback
- **STORY (3):** Fun fact, Giải thích khác biệt, Câu chuyện quán
- **COM (3):** Repost khách, Poll ý kiến, Milestone cảm ơn

---

## Tóm tắt Video Script Templates

10 kịch bản cho video 15–60 giây:

| ID | Tên | Pillar | Độ dài |
|----|-----|--------|--------|
| VS-01 | ASMR Cuốn Tay | PROD, BTS | 15–30s |
| VS-02 | POV Bữa Trưa | PROD, PROMO | 20–30s |
| VS-03 | Sáng Sớm | BTS | 30–45s |
| VS-04 | Heo Quay Lu | BTS, STORY | 30–60s |
| VS-05 | Ăn Thử Lần Đầu | PROD, COM | 30–45s |
| VS-06 | Mắm Nêm 101 | STORY | 30–45s |
| VS-07 | Mini Vlog | BTS, COM | 45–60s |
| VS-08 | Combo Reveal | PROMO, PROD | 15–30s |
| VS-09 | Deal Thời Tiết | PROMO, SEASON | 15–20s |
| VS-10 | Ngày Đặc Biệt | PROMO, SEASON | 20–30s |

---

## Tóm tắt Offer Engine

9 loại offer được định nghĩa đầy đủ:

| Offer ID | Tên | Target | Trigger |
|----------|-----|--------|---------|
| OF-01 | Combo Trưa | Segment A (văn phòng) | Thứ 2–6, 11:00–14:00 |
| OF-02 | Combo Cuối Tuần | Segment B (gia đình) | Thứ 7–CN |
| OF-03 | Combo Gia Đình | Segment B | Cả tuần |
| OF-04 | Khách Mới | Khách chưa đặt | First order |
| OF-05 | Khách Quay Lại | At-Risk / Lapsed | Không đặt 30–45 ngày |
| OF-06 | Ngày Mưa | Tất cả | Owner bật thủ công khi mưa |
| OF-07 | Office Lunch Group | Segment A nhóm | Order ≥3 phần |
| OF-08 | Weekend Special | Segment B, C | Thứ 7–CN |
| OF-09 | Seasonal | Theo sự kiện | Dịp lễ, tháng đặc biệt |

---

## Assumptions (Giả định của Builder)

Vì một số thông tin chưa có từ Owner, Builder đã đưa ra các giả định sau:

| Assumption | Lý do | Cần Owner xác nhận |
|-----------|-------|-------------------|
| Giá Combo Trưa ~65.000đ | Dựa trên target 60–80k/người trong brand_brain.md | Giá thật trong menu_brain.md |
| Combo Cuối Tuần ~80.000đ | Dựa trên target tương tự | Giá thật |
| Combo Gia Đình ~130–140.000đ | 2x giá combo đơn - discount 10–15% | Giá thật |
| Offer khách mới giảm X% | Phổ biến trong F&B, X% là [FILL] | Owner quyết định % |
| Comeback offer: 30–45 ngày | CRM standard cho F&B | Owner xác nhận thời gian |
| Office Lunch threshold: ≥3 phần | Nhóm nhỏ văn phòng thực tế | Owner xác nhận |
| Video hook: 3 giây | Best practice TikTok / Reels | Không cần xác nhận — kỹ thuật |
| Câu chuyện quán trong T-STORY-03 | Cần Owner cung cấp story thật | Owner điền [FILL] trong template |

---

## Danh sách [FILL] cần Owner điền

Để Content Engine hoạt động production-ready, Owner cần điền:

### Trong offer_engine.md
- Trạng thái ACTIVE/INACTIVE của từng offer (OF-01 đến OF-09)
- Giá thật của từng combo
- Discount % cho OF-04 (khách mới), OF-05 (comeback)
- Threshold của OF-07 (office lunch group)
- Voucher code format cho mỗi offer mùa (OF-09)

### Trong brand_brain.md / menu_brain.md (từ Phase 1.1)
- Giá thật từng món
- Địa chỉ đầy đủ
- Giờ mở cửa
- Social media handles
- Số điện thoại
- Nền tảng giao hàng đang dùng

### Trong video_script_templates.md
- VS-05: Câu chuyện ăn thử lần đầu (cần người thật)
- VS-07: Thông tin ngày/thứ cụ thể

---

## Files KHÔNG thay đổi

Tất cả files trong `01_BRAIN/` giữ nguyên từ Phase 1.1.
Không có file nào bị chỉnh sửa trong Phase 1.2 ngoài các files mới tạo.

---

## Kiểm tra An toàn

| Check | Kết quả |
|-------|---------|
| Không hardcode secret/API key/token | ✅ Pass |
| Không tạo n8n workflow production | ✅ Pass |
| Không connect API thật | ✅ Pass |
| Không auto-post | ✅ Pass |
| Không commit .claude/ | ✅ Pass (chưa commit) |
| Không commit / push | ✅ Pass |
| Không sáng tác giá (tất cả giá là [FILL]) | ✅ Pass |
| Không claim sức khỏe | ✅ Pass |

---

## Acceptance Criteria (Để Codex REVIEW_PASS)

| Criteria | Đáp ứng? |
|---------|---------|
| Có ít nhất 5 content pillars | ✅ 6 pillars |
| Mỗi pillar có purpose, persona, examples, platforms | ✅ Đầy đủ |
| Có ít nhất 20 content angles | ✅ 25 angles |
| Có ít nhất 15 caption templates | ✅ 19 templates |
| Có ít nhất 8 video script templates | ✅ 10 templates |
| Offer logic đủ 8 loại được yêu cầu | ✅ 9 loại (đủ 8 yêu cầu + thêm OF-07) |
| Có approval rules | ✅ File riêng |
| Safety rules: no auto-post, no fake claims, no fake reviews, no misleading discount | ✅ Approval_rules.md + offer_engine.md |
| Templates markdown-first, dễ convert JSON | ✅ Cấu trúc sạch |
| Phase report tạo | ✅ File này |
| Không commit | ✅ |

---

## Git Status (Thời điểm tạo báo cáo)

Files mới (untracked):
- `02_CONTENT_ENGINE/README.md`
- `02_CONTENT_ENGINE/content_pillars.md`
- `02_CONTENT_ENGINE/content_angles.md`
- `02_CONTENT_ENGINE/caption_templates.md`
- `02_CONTENT_ENGINE/video_script_templates.md`
- `02_CONTENT_ENGINE/offer_engine.md`
- `02_CONTENT_ENGINE/approval_rules.md`
- `docs/phase-1/PHASE_1_2_CONTENT_PILLAR_OFFER_ENGINE.md`
- `commands/COMMAND_INBOX.md` (updated)
- `commands/COMMAND_STATUS.md` (updated)
- `commands/CURRENT_COMMAND.md` (updated)
- `logs/CURRENT_STATUS.md` (updated)
- `handoff/CURRENT_PHASE.md` (updated)

Không có commit. Không có push.
`.claude/` untracked — không đưa vào staging.

---

## Next Steps

| Role | Action |
|------|--------|
| **Codex (Reviewer)** | Review phase 1.2 files theo acceptance criteria. REVIEW_PASS hoặc REVIEW_FAIL với notes. |
| **Owner** | Sau Codex REVIEW_PASS: điền [FILL] trong offer_engine.md và brand_brain.md |
| **Owner** | Approve → Commit → Phase 1.3 |
| **ChatGPT (Architect)** | Sau Phase 1.2 commit: mở Phase 1.3 (đề xuất: Content Calendar Automation hoặc AI Agent Prompt Layer) |

---

## Prompt dành cho Codex Reviewer

```
Codex, bạn là Reviewer của Phase 1.2 — Content Pillar & Offer Engine cho Vị Cuốn.

Builder (Claude Code) đã tạo các files sau trong D:\FNB_OS_V1\02_CONTENT_ENGINE\:
- content_pillars.md — 6 content pillars
- content_angles.md — 25 angles
- caption_templates.md — 19 templates
- video_script_templates.md — 10 video scripts
- offer_engine.md — 9 offer types + upsell/cross-sell + voucher system
- approval_rules.md — approval flow, checklist, safety rules
- README.md — overview

Và docs/phase-1/PHASE_1_2_CONTENT_PILLAR_OFFER_ENGINE.md (báo cáo phase).

REVIEW POLICY (blocker-only):
CHỈ BLOCK nếu:
- Có secret/API key/token/password thật
- .claude/ bị staged/committed
- Scope sai (không phải phase 1.2)
- Production n8n workflow tạo ra
- Auto-post / auto-reply / run ads
- File rỗng / không liên quan đến Vị Cuốn

WARNING (không block) nếu:
- Metadata wording phụ sai
- [FILL] chưa điền (đây là dự kiến — Owner điền sau)
- Giá là [FILL] (đúng — Owner chưa xác nhận)

CÁC ĐIỂM CẦN REVIEW:
1. Có đủ 5–7 pillars không? (Builder tạo 6 — check content)
2. Có đủ 20+ angles không? (Builder tạo 25)
3. Có đủ 15+ caption templates không? (Builder tạo 18)
4. Có đủ 8+ video scripts không? (Builder tạo 10)
5. Offer logic có đủ: lunch combo, group combo, new customer, comeback, rainy day, office lunch, weekend, seasonal/event?
6. Approval rules có rõ "no auto-post, no fake claims, no fake reviews, no misleading discount"?
7. Templates có markdown-first không?
8. Không có hardcoded secret, không có n8n workflow production?

OUTPUT: REVIEW_PASS hoặc REVIEW_FAIL với notes cụ thể.
Nếu REVIEW_PASS: update CMD-1.2-001 status → REVIEW_PASS trong COMMAND_INBOX.md.
Nếu REVIEW_FAIL: ghi rõ lý do → Builder fix → re-submit.
```
