# Owner Approval Flow — Vị Cuốn

*Phase 1.6 — Manual Content Pack Runbook*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*Hướng dẫn Owner ra quyết định duyệt nội dung — từ nhận Content Pack đến đăng bài*

---

## Nguyên tắc Nền tảng

> **"Owner là checkpoint cuối cùng và duy nhất. Không có gì được đăng nếu Owner chưa nói APPROVED."**

- AI chỉ tạo DRAFT — không bao giờ tự đăng
- Validation Queue chỉ kiểm tra kỹ thuật — không phải phán xét nội dung
- Owner review là phán xét nội dung cuối cùng
- Revision tối đa 3 lần trước khi cân nhắc REJECT và brief lại

---

## Sơ đồ Quyết định

```
Content Pack READY_FOR_REVIEW
           ↓
    Owner nhận output AI
           ↓
    Đọc qua 30 giây (quick gut check)
           ↓
    ┌──────────────────────────────────────────────┐
    │ Có STOP RULE nào vi phạm không?              │
    │ → Fake review / Fake discount                │
    │ → Claim sức khỏe                             │
    │ → Lệnh auto-post                             │
    │ → approval.status ≠ DRAFT                    │
    └──────────────────────────────────────────────┘
           │ Không                  │ Có
           ↓                        ↓
    Chạy Owner Review          [STOP] Báo lỗi
    Checklist đầy đủ           Yêu cầu AI sửa
    (6 phần)                   hoặc REJECT
           ↓
    ┌──────────────────────────────────────────────┐
    │ Kết quả checklist?                           │
    └──────────────────────────────────────────────┘
          │                  │                │
          ↓                  ↓                ↓
    Tất cả PASS        Có vấn đề nhỏ    Có BLOCKER
          ↓              1–3 mục              ↓
      APPROVED         REVISION           REJECT
          ↓            REQUESTED          hoặc
    Lên lịch đăng           ↓           REVISION
          ↓            AI sửa lại      tùy mức độ
    Đăng tay               ↓
          ↓            Re-submit
    Ghi link bài       (lần 2/3)
```

---

## PHẦN 1 — Quick Gut Check (2 phút)

Trước khi đọc kỹ, Owner đọc nhanh một lần và trả lời:

| # | Câu hỏi tự hỏi | Trả lời |
|---|---------------|---------|
| G1 | Đọc xong tôi có thấy muốn ghé quán không? | [ ] Có [ ] Không |
| G2 | Bài nghe như người bạn nhắn hay như quảng cáo trên TV? | [ ] Bạn bè [ ] Quảng cáo |
| G3 | Có điều gì trong bài khiến tôi do dự không? | [ ] Không [ ] Có (ghi chú: ___) |
| G4 | Bài này phù hợp với tuần này / ngày này không? | [ ] Có [ ] Không |

Nếu G3 = Có hoặc G2 = Quảng cáo → chú ý trong review chi tiết bên dưới.

---

## PHẦN 2 — Stop Rules Check (1 phút)

Kiểm tra nhanh 10 Stop Rules từ Runbook:

| # | Stop Rule | Vi phạm? |
|---|----------|---------|
| S1 | Caption có giá cụ thể nhưng chưa xác nhận? | [ ] Ổn [ ] STOP |
| S2 | Caption có địa chỉ nhưng chưa điền thật? | [ ] Ổn [ ] STOP |
| S3 | Caption có SĐT nhưng chưa điền thật? | [ ] Ổn [ ] STOP |
| S4 | Có KM cụ thể nhưng Owner chưa xác nhận tồn tại? | [ ] Ổn [ ] STOP |
| S5 | Caption gợi ý fake review / fake discount? | [ ] Ổn [ ] STOP |
| S6 | Output có lệnh tự đăng / gọi API? | [ ] Ổn [ ] STOP |
| S7 | `approval.status` ≠ `DRAFT`? | [ ] Ổn [ ] STOP |
| S8 | Bài đã được đăng trước khi Owner APPROVE? | [ ] Ổn [ ] STOP |
| S9 | Caption có claim sức khỏe? | [ ] Ổn [ ] STOP |
| S10 | Caption nhắc tên đối thủ? | [ ] Ổn [ ] STOP |

**Nếu BẤT KỲ ô nào là STOP → dừng, không tiếp tục review chi tiết.**

---

## PHẦN 3 — Review Chi tiết (5–10 phút)

Dùng `03_APPROVAL_PIPELINE/owner_review_checklist.md` — 6 phần đầy đủ.

### Tóm tắt nhanh 6 phần:

**P1 — Thông tin cơ bản:** Content ID, Platform, Pillar, Angle, Persona đúng không?

**P2 — Caption:**
- Đọc tự nhiên, không nghe "robot viết"?
- Giọng điệu ấm áp, gần gũi?
- Không lỗi chính tả?
- Giá đúng menu? Không claim sức khỏe? Không đối thủ?
- Không fake urgency? Không viết hoa toàn câu?
- Emoji ≤ 3? Hashtag đúng? Có CTA rõ?

**P3 — Offer (nếu có):** Offer ID hợp lệ, status ACTIVE, giá khớp, voucher đăng ký chưa?

**P4 — Hình ảnh / Video:** Brief mô tả rõ, yêu cầu ảnh thật, không ảnh stock, hook video trong 3s?

**P5 — Safety Flags:** AI đã báo flag gì? Các BLOCKER đã giải quyết chưa?

**P6 — Tổng thể:** Phù hợp kế hoạch tuần? Không xung đột bài cũ? Tự tin đăng không?

---

## PHẦN 4 — 4 Câu hỏi Tự hỏi Trước khi APPROVE

> 1. **Tôi có tự tin đăng bài này ngay bây giờ không?**
>    → Nếu do dự → REVISION, không APPROVE rồi lo sau
>
> 2. **Bài này có thể gây hiểu nhầm không?**
>    → Nếu có khả năng → sửa trước khi đăng
>
> 3. **Khách hàng của mình sẽ cảm thấy gì khi đọc bài này?**
>    → Thèm ăn, muốn ghé → tốt
>    → Hoang mang, nghi ngờ → sửa lại
>
> 4. **Nếu bài này bị screenshot và share rộng rãi, tôi có OK không?**
>    → Nếu không OK → sửa trước khi đăng

---

## PHẦN 5 — Ra Quyết định

### Quyết định APPROVED ✅

**Khi nào:** Tất cả checklist pass, 4 câu hỏi tự hỏi đều YES, không có STOP rule nào vi phạm.

**Làm gì:**
1. Điền vào Content Pack output:
   ```
   owner_decision:         APPROVED
   approval_timestamp:     [ngày giờ hiện tại, VD: 2026-05-27 14:30 +07:00]
   proposed_publish_date:  [ngày đăng, VD: 2026-05-28 11:00]
   approval.status:        APPROVED  ← Owner mới được set field này
   ```

2. Chọn ngày và giờ đăng (xem gợi ý trong Content Pack section "Platform Fit")

3. Sang Bước 7 trong Runbook — Đăng tay

---

### Quyết định REVISION_REQUESTED 📝

**Khi nào:** 1–3 vấn đề nhỏ trong caption, hình ảnh brief, hoặc format. Không phải BLOCKER nghiêm trọng.

**Cách viết revision note hiệu quả:**

| Viết MƠ HỒ ❌ | Viết CỤ THỂ ✅ |
|-------------|------------|
| "Caption không hay" | "Caption v1 giọng quá cứng, đổi 'Quý khách' thành 'bạn'" |
| "Sửa lại" | "Rút ngắn caption từ 320 còn 200 ký tự, giữ nguyên hook đầu" |
| "Không đúng tone" | "Tone quá marketing. Viết như nhắn tin cho bạn bè hơn" |
| "Thêm thứ gì đó" | "Thêm giờ mở cửa vào CTA: 'ghé quán từ 10h nha'" |

**Làm gì:**
1. Điền vào Content Pack:
   ```
   owner_decision:   REVISION_REQUESTED
   revision_note:    "1. [vấn đề cụ thể] — [mong muốn cụ thể]
                      2. [vấn đề cụ thể] — [mong muốn cụ thể]"
   revision_count:   1 (tăng lên mỗi lần)
   ```

2. Gửi revision note cho AI Worker cùng với Content Pack gốc

3. AI sửa và gửi lại Content Pack mới

4. Owner review lại từ Bước 5 (Validate) → Bước 6 (Approval)

**Giới hạn revision:** Tối đa 3 lần. Nếu lần 3 vẫn không đạt → cân nhắc REJECT và brief lại hoàn toàn.

---

### Quyết định REJECTED ❌

**Khi nào:**
- Có BLOCKER nghiêm trọng không thể sửa nhỏ (fake claim, auto-post trigger)
- Bài hoàn toàn không phù hợp với brief ban đầu
- Đã qua 3 lần revision mà vẫn không đạt
- Owner không muốn đăng bài này dưới bất kỳ hình thức nào

**Làm gì:**
1. Điền vào Content Pack:
   ```
   owner_decision:  REJECTED
   revision_note:   "[lý do cụ thể]"
   approval.status: REJECTED
   ```

2. Bài này chuyển sang ARCHIVED — không đăng, không chỉnh thêm

3. Nếu muốn content về topic này: tạo Input Brief mới, mô tả rõ hơn những gì không muốn → bắt đầu lại từ Bước 2

---

## Ma trận Quyết định Nhanh

| Tình huống | Quyết định | Action |
|-----------|-----------|--------|
| Tất cả checklist pass, tự tin 100% | APPROVED | Lên lịch đăng |
| Caption có 1–2 chỗ cần sửa nhỏ | REVISION | Ghi rõ 1–2 điểm cần sửa |
| Giọng văn không đúng tone | REVISION | Yêu cầu viết lại giọng văn |
| Caption quá dài / quá ngắn | REVISION | Ghi số ký tự mong muốn |
| Giá sai / offer không tồn tại | REVISION hoặc REJECT | Xem mức độ |
| Caption có claim sức khỏe | REJECT + Báo lỗi | Yêu cầu AI sửa hoàn toàn |
| Có fake review / fake discount | REJECT + STOP | Dừng ngay |
| AI output có lệnh auto-post | REJECT + STOP | Dừng ngay, báo cáo lỗi |
| Lần revision thứ 3 vẫn không đạt | REJECT | Brief lại từ đầu |

---

## Thời gian Đề xuất cho Mỗi Bước

| Giai đoạn | Thời gian đề xuất |
|-----------|-----------------|
| Quick gut check | 1–2 phút |
| Stop rules check | 1 phút |
| Review chi tiết (bài đơn) | 3–5 phút |
| Review chi tiết (bài có offer) | 5–8 phút |
| Review chi tiết (bài có video) | 5–10 phút |
| Ra quyết định + ghi revision note | 2–3 phút |
| **Tổng review một bài** | **10–20 phút** |

---

## Workflow Revision (Khi cần sửa)

```
Owner gửi Revision Note → AI nhận:
  [Content ID] + [Revision Note] + [Content Pack gốc]
  ↓
AI sửa theo đúng revision note
  - Không tự thêm thứ không có trong revision note
  - Không tự sửa phần không được đề cập
  - Ghi lại thay đổi đã làm vào ai_revision_summary
  ↓
AI trả về Content Pack mới (vẫn DRAFT, revision_count +1)
  ↓
Owner review lại Bước 5 → Bước 6
```

---

## Sau khi APPROVED — Quy trình Đăng Tay

Xem chi tiết tại `manual_content_pack_runbook.md` → Bước 7.

Tóm tắt:
1. Kiểm tra 5 điểm cuối (C1–C5)
2. Mở platform (Facebook / TikTok / Instagram / Zalo OA)
3. Copy caption đã APPROVED
4. Upload ảnh/video thật
5. Preview một lần
6. Đăng
7. Ghi link bài vào Manual Output Template

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.6 — File tạo mới. Sơ đồ quyết định đầy đủ, Quick Gut Check, Stop Rules Check, Review chi tiết, 4 câu hỏi tự hỏi, ma trận quyết định, revision workflow, thời gian đề xuất. | Claude Code (Builder) |
