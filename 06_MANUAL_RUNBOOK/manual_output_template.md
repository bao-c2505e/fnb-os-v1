# Manual Output Template — Vị Cuốn Content Pack

*Phase 1.6 — Manual Content Pack Runbook*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Template ghi nhận output Content Pack theo chuẩn FnB OS V1 — dùng khi AI trả về output*

---

## Hướng dẫn Dùng File này

Khi AI Worker trả về Content Pack DRAFT, Owner copy output vào template này để:
1. Lưu có cấu trúc, không mất thông tin
2. Dễ so sánh với validation checklist
3. Chuẩn bị cho bước Approval

**Cách dùng:** Copy toàn bộ phần "CONTENT PACK OUTPUT" bên dưới, điền thông tin từ AI output.

---

## CONTENT PACK OUTPUT

```
╔═══════════════════════════════════════════════════════════╗
║           CONTENT PACK — VỊ CUỐN                         ║
║           TRẠNG THÁI: DRAFT                               ║
╚═══════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THÔNG TIN CƠ BẢN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Content ID:         ___________________________________________
                    (Format: VQ-[PLAT]-[PILLAR]-[YYYYMMDD]-[SEQ])

Platform:           ___________________________________________
Content Type:       ___________________________________________
Pillar:             ___________________________________________
Angle:              ___________________________________________
Target Persona:     ___________________________________________
Objective:          ___________________________________________
Offer (nếu có):     ___________________________________________

Tạo bởi AI:         ___________________________________________
Tạo lúc:            ___________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPTION OPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

── CAPTION V1 (Đầy đủ) ──────────────────────────────────────
[Dán caption v1 từ AI output vào đây]


Số ký tự: _______  (ngưỡng platform: _______)

── CAPTION V2 (Ngắn hơn) ────────────────────────────────────
[Dán caption v2 từ AI output vào đây]


Số ký tự: _______

── CAPTION V3 (Minimal — nếu có) ────────────────────────────
[Dán caption v3 nếu AI tạo]


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
HOOK OPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hook 1: ______________________________________________________
        Tone: _______________  Platform fit: ________________

Hook 2: ______________________________________________________
        Tone: _______________  Platform fit: ________________

Hook 3 (nếu có): _____________________________________________
        Tone: _______________  Platform fit: ________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VIDEO SCRIPT (Chỉ khi content_type là video)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[  ] Không áp dụng (content_type không phải video)
[  ] Có video script — điền bên dưới:

Độ dài mục tiêu: _________ giây

Cảnh 1 (0–___s):
  Visual: ___________________________________________________
  Audio:  ___________________________________________________
  Text:   ___________________________________________________

Cảnh 2 (___–___s):
  Visual: ___________________________________________________
  Audio:  ___________________________________________________
  Text:   ___________________________________________________

Cảnh 3 (___–___s):
  Visual: ___________________________________________________
  Audio:  ___________________________________________________
  Text:   ___________________________________________________

Cảnh 4 (___–___s):
  Visual: ___________________________________________________
  Audio:  ___________________________________________________
  Text:   ___________________________________________________

CTA cuối: _________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMAGE BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Chủ thể:      _______________________________________________
Góc chụp:     _______________________________________________
Ánh sáng:     _______________________________________________
Props:         _______________________________________________
Tránh:         _______________________________________________
Phong cách:   _______________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OFFER SUMMARY (Chỉ khi có offer)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[  ] Không có offer
[  ] Có offer:

Offer ID:        ___________________________________________
Tên offer:       ___________________________________________
Gồm:             ___________________________________________
Giá:             ___________ (hoặc [FILL: ~XXk] nếu chưa confirm)
Điều kiện:       ___________________________________________
Voucher code:    ___________ (hoặc N/A)
Hiệu lực:        ___________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PLATFORM FIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Giờ đăng đề xuất:   ________________________________________
Lưu ý định dạng:    ________________________________________
Hashtags:           ________________________________________
                    ________________________________________
Số hashtag:         ____  (Ngưỡng: FB 3–5 | TK 5–10 | IG 5–15 | Zalo 0)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SAFETY FLAGS (AI tự báo cáo)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Safety check passed:  [ ] Có (không BLOCKER)  [ ] Không (có BLOCKER)

Flags (nếu có):
  1. _________________________________ [BLOCKER/WARNING/NOTE]
  2. _________________________________ [BLOCKER/WARNING/NOTE]
  3. _________________________________ [BLOCKER/WARNING/NOTE]

AI Notes: __________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APPROVAL (LUÔN LÀ DRAFT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

approval.status:        DRAFT   ← Phải là DRAFT, không phải gì khác
owner_decision:         null
revision_note:          null
revision_count:         0
approval_timestamp:     null
proposed_publish_date:  null

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
METADATA & ASSUMPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tạo bởi:            ________________________________________
Source brain:        Phase 1.6
Input brief ref:     Kịch bản __ (từ manual_test_input_examples.md)

Assumptions (AI ghi):
  1. ________________________________________________________
  2. ________________________________________________________
  3. ________________________________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[FILL] CÒN LẠI CẦN OWNER ĐIỀN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[  ] Không có [FILL] quan trọng → READY_FOR_REVIEW
[  ] Còn [FILL] → NEEDS_OWNER_REVIEW

[FILL] cần điền:
  1. _________________________________ → File: ____________
  2. _________________________________ → File: ____________
  3. _________________________________ → File: ____________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VALIDATION STATUS (Sau khi chạy validation_checklist.md)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[  ] READY_FOR_REVIEW    — 0 BLOCKER, không còn [FILL] quan trọng
[  ] NEEDS_OWNER_REVIEW  — 0 BLOCKER, còn [FILL] cần Owner điền
[  ] REVISION_REQUESTED  — Brand/content fit yếu, Builder chỉnh
[  ] BLOCKED             — Có BLOCKER, dừng ngay

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OWNER DECISION (Sau bước Approval)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ngày duyệt:              ___________________________________
Owner quyết định:        [ ] APPROVED  [ ] REVISION  [ ] REJECTED

Nếu APPROVED:
  Ngày đăng dự kiến:     ___________________________________
  Giờ đăng:              ___________________________________

Nếu REVISION_REQUESTED:
  Revision note:
  1. _______________________________________________________
  2. _______________________________________________________

Nếu REJECTED:
  Lý do:                 ___________________________________

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SAU KHI ĐĂNG (Điền khi đã đăng xong)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Final status:            [ ] PUBLISHED_MANUAL
Đăng lúc:                ___________________________________
Link bài đã đăng:        ___________________________________

Kết quả sau 24h:
  React/thích:           ___________________________________
  Comment:               ___________________________________
  Share:                 ___________________________________
  Inbox nhận được:       ___________________________________
  Đơn hàng từ bài:       ___________________________________

═══════════════════════════════════════════════════════════════
```

---

## Ghi chú Điền Output

### Về Caption
- Copy chính xác từ AI output — không tự chỉnh trước khi validate
- Đếm ký tự bằng tool online hoặc Word: [wordcount.net](https://wordcount.net) / ctrl+A trong Notes
- Ghi rõ xem caption có [FILL] nào còn tồn tại không

### Về Safety Flags
- AI phải tự báo cáo flags trong output
- Nếu AI không báo cáo flags → đây là WARNING (AI có thể đã bỏ sót bước safety check)
- Owner vẫn cần chạy validation checklist độc lập

### Về approval.status
- **Phải là DRAFT** — nếu AI output có status khác (READY_FOR_REVIEW, APPROVED) → STOP rule S7
- Owner là người duy nhất set status → APPROVED, sau khi chạy qua toàn bộ checklist

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.6 — File tạo mới. Output template đầy đủ 11 sections: thông tin cơ bản, caption options, hook, video script, image brief, offer summary, platform fit, safety flags, approval, [FILL] tracking, post-publish tracking. | Claude Code (Builder) |
