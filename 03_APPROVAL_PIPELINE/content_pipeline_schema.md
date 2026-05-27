# Content Pipeline Schema — Vị Cuốn

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Mô tả luồng dữ liệu từ khi ý tưởng được tạo đến khi nội dung được đăng.*
*Dùng bởi: AI Agent, n8n workflows, Owner.*

---

## Pipeline Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONTENT PIPELINE — VỊ CUỐN                      │
│                                                                     │
│  [IDEA INPUT]                                                       │
│       │                                                             │
│       ▼                                                             │
│  [AI CONTENT AGENT]                                                 │
│   - Chọn pillar + angle                                             │
│   - Tạo caption / script / brief                                    │
│   - Gán offer (nếu có)                                              │
│   - Chạy AI Self-Check                                              │
│       │                                                             │
│       ▼ (nếu Self-Check PASS)                                       │
│  [CONTENT PACK]  ──────────→  [Google Sheet: Content Approval Queue]│
│       │                              │                              │
│       ▼                              ▼                              │
│  [GOOGLE DRIVE]             [TELEGRAM NOTIFICATION → Owner]         │
│   Lưu draft files                    │                              │
│                                      ▼                              │
│                             [OWNER REVIEW]                          │
│                              ├─ APPROVED                            │
│                              ├─ REVISION_REQUESTED → AI sửa lại    │
│                              └─ REJECTED → ARCHIVED                 │
│                                      │ (APPROVED)                  │
│                                      ▼                              │
│                             [OWNER: SCHEDULE_PROPOSED]              │
│                             (chọn ngày/giờ đăng thủ công)          │
│                                      │                              │
│                                      ▼                              │
│                             [OWNER: PUBLISH MANUAL]                 │
│                             (copy caption → paste lên platform)     │
│                                      │                              │
│                                      ▼                              │
│                             [PUBLISHED_MANUAL]                      │
│                             (ghi link bài đã đăng)                  │
│                                      │                              │
│                                      ▼                              │
│                             [ARCHIVED]                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage 1 — Idea Intake (Tiếp nhận Ý tưởng)

### Input Sources

| Nguồn | Mô tả | Người / Agent |
|-------|-------|---------------|
| Content Calendar | Kế hoạch đăng bài theo tuần/tháng | Owner / AI Agent |
| Offer Trigger | Offer trong offer_engine.md kích hoạt bài promo | AI Agent (đọc trigger rules) |
| Seasonal Event | Sự kiện trong calendar (Tết, 8/3, v.v.) | AI Agent / Owner |
| Owner Request | Owner yêu cầu tạo bài cụ thể | Owner |
| Performance Signal | Bài cũ hiệu quả tốt → tạo biến thể | AI Agent (Phase sau) |

### Idea Record (Minimum Fields)

```json
{
  "content_id": "VQ-FB-PROD-20260527-001",
  "brand": "Vi Cuon",
  "platform": "Facebook",
  "content_type": "Post",
  "pillar": "PROD",
  "angle": "hero-shot",
  "status": "IDEA",
  "created_by_agent": "Claude Code (Builder)",
  "source_brain_version": "Phase 1.2"
}
```

---

## Stage 2 — Content Generation (AI Tạo Nội dung)

### AI sử dụng các nguồn sau

| File Brain | Dữ liệu lấy từ đây |
|-----------|-------------------|
| `brand_brain.md` | Brand voice, tone, visual identity, safety rules |
| `content_brain.md` | Content strategy tổng thể |
| `content_pillars.md` | Pillar definition, % mix, ví dụ nội dung |
| `content_angles.md` | Angle cụ thể, hook, messaging direction |
| `caption_templates.md` | Template caption có thể điền thông tin |
| `video_script_templates.md` | Template script video |
| `offer_engine.md` | Offer details, giá, điều kiện |
| `menu_brain.md` | Tên món, giá, mô tả |
| `customer_brain.md` | Persona, segment, điểm đau, triggers |

### AI Output (Content Pack Fields)

```
BẮTBUỘC:
- content_id (tự tạo)
- caption (hoặc video_script)
- image_brief (hoặc design_brief)
- target_persona
- safety_flags (empty string nếu không có flag)

TÙY CHỌN:
- offer_code (nếu bài có offer)
- video_script (nếu là video)
- design_brief (nếu cần thiết kế)
- caption_options (nhiều phiên bản để Owner chọn)
```

---

## Stage 3 — AI Self-Check (Kiểm tra Tự động)

### Quy trình Self-Check

```python
# Pseudo-code: AI Self-Check Process
def ai_self_check(content_pack):
    flags = []
    
    # Check 1: Giá
    if has_price_claim(content_pack.caption):
        if not price_in_menu_brain(content_pack.caption):
            flags.append("PRICE_UNVERIFIED")
    
    # Check 2: Offer
    if content_pack.offer_code:
        if not offer_in_engine(content_pack.offer_code):
            flags.append("OFFER_NOT_IN_ENGINE")
    
    # Check 3: Health claims
    if has_health_claim(content_pack.caption):
        flags.append("HEALTH_CLAIM_DETECTED")
    
    # Check 4: Fake urgency
    if has_fake_urgency_pattern(content_pack.caption):
        flags.append("FAKE_URGENCY_RISK")
    
    # Check 5: Competitor
    if mentions_competitor(content_pack.caption):
        flags.append("COMPETITOR_MENTION")
    
    # Check 6: Emoji count
    if emoji_count(content_pack.caption) > 3:
        flags.append("EMOJI_OVERLOAD")
    
    # Check 7: Hashtag
    if not has_core_hashtags(content_pack.caption):
        flags.append("MISSING_HASHTAG")
    
    # Check 8: Caption length
    if caption_exceeds_limit(content_pack.caption, content_pack.platform):
        flags.append("CAPTION_TOO_LONG")
    
    # Blockers: bất kỳ BLOCKER flag nào → KHÔNG set READY_FOR_REVIEW
    blockers = [f for f in flags if is_blocker(f)]
    if blockers:
        # Sửa và check lại
        return "FAIL", flags
    
    content_pack.safety_flags = "|".join(flags)  # lưu WARNING/NOTE flags
    return "PASS", flags
```

### Kết quả Self-Check

| Kết quả | Hành động |
|---------|-----------|
| PASS (không có BLOCKER) | Set `status = READY_FOR_REVIEW`, ghi `safety_flags` vào sheet, gửi Telegram cho Owner |
| FAIL (có ≥1 BLOCKER) | AI tự sửa nội dung, chạy lại check. Không gửi Owner khi còn BLOCKER. |

---

## Stage 4 — Owner Notification (Thông báo cho Owner)

### Trigger

Khi `status` chuyển từ `DRAFT` → `READY_FOR_REVIEW`, n8n gửi Telegram tới Owner.

### Notification Content

```
📋 NỘI DUNG CHỜ DUYỆT

🆔 ID: VQ-FB-PROD-20260527-001
📱 Platform: Facebook | Loại: Post
🎯 Pillar: PROD | Angle: hero-shot
👥 Persona: Segment A (dân văn phòng)

📝 Caption (preview):
"[50 ký tự đầu của caption]..."

🎁 Offer: OF-01 — Combo Trưa
⚠️ Safety Flags: EMOJI_OVERLOAD

📁 Google Drive: [link folder Draft]
📊 Sheet: [link dòng trong Google Sheet]

👇 HÀNH ĐỘNG:
✅ [APPROVE]  📝 [REVISE]  ❌ [REJECT]
```

---

## Stage 5 — Owner Review (Duyệt bởi Owner)

### Owner Workflow

```
1. Nhận Telegram notification
2. Mở Google Drive link → đọc full content pack
3. Kiểm tra theo owner_review_checklist.md
4. Quyết định:
   a. APPROVE → ghi owner_decision = APPROVED + approval_timestamp vào Sheet
   b. REVISE → ghi owner_decision = REVISION_REQUESTED + revision_note
   c. REJECT → ghi owner_decision = REJECTED + lý do trong revision_note
5. n8n phát hiện thay đổi trong Sheet → trigger bước tiếp theo
```

### Thời gian SLA

| Hành động | SLA đề xuất |
|-----------|------------|
| Owner reply thông báo | 48 giờ |
| Nếu không reply sau 48h | n8n gửi reminder lần 2 |
| Nếu không reply sau 72h | n8n gửi escalation |

---

## Stage 6 — Revision Loop (Vòng lặp Chỉnh sửa)

### Khi `status = REVISION_REQUESTED`

```
1. n8n notify AI Agent: "Bài [ID] cần chỉnh sửa"
2. AI đọc revision_note từ Owner
3. AI sửa: caption / script / brief
4. AI chạy lại Self-Check
5. Nếu pass → set status = READY_FOR_REVIEW (version 2)
6. Nếu fail → sửa tiếp (lặp lại)
7. Gửi Telegram notification mới cho Owner: "Bài [ID] đã được sửa lại"

Giới hạn: ≤ 3 revision cycles
Nếu > 3 lần mà vẫn cần sửa → escalate: "Bài [ID] cần Owner tự viết
hoặc cung cấp thêm brief chi tiết"
```

---

## Stage 7 — Scheduling & Publishing (Lên lịch & Đăng)

### Sau khi APPROVED

```
1. Owner chọn ngày/giờ đăng phù hợp
2. Owner điền proposed_publish_date vào Sheet
3. Set status = SCHEDULE_PROPOSED
4. n8n có thể gửi reminder cho Owner vào sáng ngày đề xuất đăng:
   "Hôm nay là ngày đăng bài [ID] — [Platform]. Nội dung đã ready."
5. Owner copy caption → paste lên platform → đăng thủ công
6. Owner ghi manual_publish_link vào Sheet
7. Set status = PUBLISHED_MANUAL
```

**QUAN TRỌNG: Không có auto-publish trong Phase 1.x. Mọi bài phải Owner đăng tay.**

---

## Stage 8 — Post-Publish (Sau khi Đăng)

### Tracking tối thiểu

| Trường theo dõi | Nguồn | Ghi vào đâu |
|----------------|-------|------------|
| Link bài đăng | Owner điền | `manual_publish_link` trong Sheet |
| Ngày đăng thực tế | Hệ thống ghi khi set `PUBLISHED_MANUAL` | Sheet |
| Performance (Phase sau) | Facebook Insights / TikTok Analytics | Google Sheet tab riêng |

### Archive

Sau 30 ngày kể từ ngày đăng, n8n gợi ý Owner archive bài:
- Status: `PUBLISHED_MANUAL` → `ARCHIVED`
- Giải phóng queue view để tập trung vào bài mới

---

## Data Flow Diagram (Dữ liệu đi qua đâu)

```
Brain Files (01_BRAIN/, 02_CONTENT_ENGINE/)
    │
    ▼ (AI đọc)
AI Content Agent (Claude / n8n)
    │
    ▼ (AI viết)
Content Pack (JSON + Markdown)
    │
    ├──▶ Google Sheet: Content Approval Queue (row mới)
    │
    └──▶ Google Drive: /Draft/[YYYY-MM]/[Platform]/[content_id]/
              ├── caption.md
              ├── video_script.md (nếu có)
              ├── image_brief.md
              └── design_brief.md (nếu có)
```

---

## Integration Points (Tích hợp với hệ thống khác)

| Hệ thống | Tích hợp | Phase sẵn sàng |
|----------|---------|---------------|
| Google Sheet (Content Approval Queue) | AI ghi, Owner chỉnh, n8n đọc | Phase 1.3 (schema), Phase 2 (production) |
| Google Drive (Draft folder) | AI ghi files, Owner đọc | Phase 1.3 (schema), Phase 2 (production) |
| Telegram Bot | n8n gửi notification cho Owner | Phase 2 |
| n8n Workflow: Content Generator | Tạo content pack tự động | Phase 3 |
| n8n Workflow: Approval Monitor | Watch Sheet → trigger notification | Phase 3 |
| n8n Workflow: Reminder | Nhắc Owner nếu quá SLA | Phase 3 |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. 8 stages, data flow, integration points, AI self-check pseudo-code. | Claude Code (Builder) |
