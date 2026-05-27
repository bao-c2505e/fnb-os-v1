# Safety Self-Check — Content Pack Generator

*Phase 1.4 — Draft Content Pack Generator Schema*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*
*AI Worker chạy checklist này trước khi output Content Pack*

---

## Tổng quan

AI Worker PHẢI chạy toàn bộ checklist này sau khi draft xong, trước khi output Content Pack.

- **BLOCKER** → Dừng ngay. Không output. Báo cáo lỗi cho Owner/ChatGPT.
- **WARNING** → Output được nhưng phải ghi rõ trong `safety_check.flags[]` và `safety_check.ai_notes`.
- **NOTE** → Ghi vào `ai_notes` để Owner biết. Không chặn output.

Kết quả cuối cùng ghi vào `safety_check` block trong Content Pack JSON.

---

## NHÓM 1 — KIỂM TRA BẢO MẬT & TUÂN THỦ

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| SEC-01 | **BLOCKER** | Output KHÔNG chứa API key, token, password, secret thật | [ ] Pass / [ ] Fail |
| SEC-02 | **BLOCKER** | Output KHÔNG chứa thông tin cá nhân thật của khách hàng (tên, SĐT, địa chỉ nhà riêng) | [ ] Pass / [ ] Fail |
| SEC-03 | **BLOCKER** | Output KHÔNG trigger bất kỳ API đăng bài nào (Facebook, TikTok, Instagram, Zalo) | [ ] Pass / [ ] Fail |
| SEC-04 | **BLOCKER** | Output KHÔNG chứa lệnh gửi tin nhắn tự động cho khách hàng | [ ] Pass / [ ] Fail |
| SEC-05 | **BLOCKER** | `approval.status` = `DRAFT` (KHÔNG phải `READY_FOR_REVIEW` hoặc `APPROVED`) | [ ] Pass / [ ] Fail |

---

## NHÓM 2 — KIỂM TRA NỘI DUNG THƯƠNG HIỆU

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| BRAND-01 | **BLOCKER** | Caption KHÔNG có claim sức khỏe chưa có căn cứ ("tốt cho sức khỏe", "giảm cân", "detox", "thanh lọc cơ thể") | [ ] Pass / [ ] Fail |
| BRAND-02 | **BLOCKER** | Caption KHÔNG đề cập tên đối thủ cạnh tranh — kể cả so sánh tích cực | [ ] Pass / [ ] Fail |
| BRAND-03 | **BLOCKER** | Caption KHÔNG có giá tiền không có nguồn từ `menu_brain.md` hoặc `offer_engine.md` | [ ] Pass / [ ] Fail |
| BRAND-04 | **WARNING** | Caption KHÔNG dùng ngôn ngữ trang trọng xa cách ("Quý khách hàng kính mến", "Trân trọng kính mời") | [ ] Pass / [ ] Warn |
| BRAND-05 | **WARNING** | Caption KHÔNG viết hoa toàn câu để nhấn mạnh (VD: "SIÊU NGON SIÊU RẺ") | [ ] Pass / [ ] Warn |
| BRAND-06 | **WARNING** | Caption KHÔNG tạo áp lực giả ("Chỉ còn 2 suất!!!", "Hết ngay bây giờ!!!") khi không có thật | [ ] Pass / [ ] Warn |
| BRAND-07 | **WARNING** | Emoji trong caption tối đa 2–3 cái. Không dày đặc mỗi dòng | [ ] Pass / [ ] Warn |
| BRAND-08 | **NOTE** | Caption có CTA rõ ràng phù hợp với objective | [ ] Yes / [ ] Missing |
| BRAND-09 | **NOTE** | Hashtag có #VịCuốn và #ĂnVinh (2 hashtag cốt lõi của brand) | [ ] Yes / [ ] Missing |

---

## NHÓM 3 — KIỂM TRA OFFER & GIÁ

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| OFFER-01 | **BLOCKER** | Mọi offer đề cập trong bài đều từ `offer_engine.md` — không tự tạo offer mới | [ ] Pass / [ ] Fail |
| OFFER-02 | **BLOCKER** | Voucher code (nếu có) phải có trong `offer_engine.md` Voucher System — không dùng code chưa đăng ký | [ ] Pass / [ ] Fail |
| OFFER-03 | **WARNING** | Nếu offer status trong `offer_engine.md` là `[FILL]` → đánh dấu `[OWNER_CONFIRM: offer status]` trong output | [ ] Pass / [ ] Warn |
| OFFER-04 | **WARNING** | Giá trong caption dùng `[FILL: ~XXđ]` nếu `menu_brain.md` chưa có giá xác nhận — KHÔNG tự đặt giá cụ thể | [ ] Pass / [ ] Warn |
| OFFER-05 | **NOTE** | Điều kiện offer (thời gian, ngày, kênh) được trình bày rõ ràng trong caption | [ ] Yes / [ ] Missing |

---

## NHÓM 4 — KIỂM TRA THÔNG TIN BẮT BUỘC

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| INFO-01 | **WARNING** | Thông tin địa chỉ chưa xác nhận → dùng "Vị Cuốn — Vinh, Nghệ An" + `[FILL: địa chỉ chi tiết]` | [ ] Pass / [ ] Warn |
| INFO-02 | **WARNING** | Social handles (@) chưa xác nhận → dùng tag mô tả thay vì @handle + `[FILL: xác nhận handle]` | [ ] Pass / [ ] Warn |
| INFO-03 | **NOTE** | SĐT / Zalo chưa có → dùng `[FILL: SĐT]` — không bỏ trống hoàn toàn | [ ] Yes / [ ] Missing |

---

## NHÓM 5 — KIỂM TRA SCHEMA & FORMAT

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| SCHEMA-01 | **BLOCKER** | JSON output có đủ tất cả `required` fields theo `content_pack_json_schema.md`: id, brand, platform, content_type, objective, persona, pillar, angle, safety_check, approval, metadata | [ ] Pass / [ ] Fail |
| SCHEMA-02 | **BLOCKER** | `id` theo đúng format `VQ-[PLAT]-[PILLAR]-[YYYYMMDD]-[SEQ]` | [ ] Pass / [ ] Fail |
| SCHEMA-03 | **WARNING** | `caption_options` có ít nhất 2 phiên bản (v1 và v2) | [ ] Pass / [ ] Warn |
| SCHEMA-04 | **WARNING** | `hook_options` có ít nhất 2 options | [ ] Pass / [ ] Warn |
| SCHEMA-05 | **WARNING** | Nếu `content_type` là video (Reel/TikTok Video/Short Video) → `script_options` không null | [ ] Pass / [ ] Warn |
| SCHEMA-06 | **NOTE** | `metadata.assumptions[]` có đầy đủ tất cả giả định đã đặt trong output | [ ] Yes / [ ] Missing |

---

## NHÓM 6 — KIỂM TRA PLATFORM FIT

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| PLAT-01 | **WARNING** | `content_type` phù hợp với `platform` theo Platform Compatibility Matrix (`content_pack_generator_schema.md`) | [ ] Pass / [ ] Warn |
| PLAT-02 | **WARNING** | Caption length phù hợp với platform: TikTok < 150 chars, Facebook < 500 chars đề xuất | [ ] Pass / [ ] Warn |
| PLAT-03 | **NOTE** | Số lượng hashtag phù hợp: Facebook 3–5, TikTok 5–10, Instagram 5–15, Zalo 0 | [ ] Yes / [ ] Out-of-range |

---

## NHÓM 7 — KIỂM TRA AI BEHAVIOR

| Mã | Mức | Kiểm tra | Kết quả |
|----|-----|---------|---------|
| AI-01 | **BLOCKER** | Không có lệnh tự động hóa nào được nhúng trong output (không có URL gọi API, không có script chạy) | [ ] Pass / [ ] Fail |
| AI-02 | **BLOCKER** | Không output thông tin "nội bộ" của hệ thống FnB OS (API keys, webhook URLs, database paths) | [ ] Pass / [ ] Fail |
| AI-03 | **WARNING** | Không sử dụng thông tin về Vị Cuốn từ training data mà chưa verify với `brand_brain.md` | [ ] Pass / [ ] Warn |
| AI-04 | **NOTE** | Content Pack được tạo từ đọc file thật (không phải hallucinate) — AI ghi rõ nguồn dữ liệu dùng | [ ] Yes / [ ] Unclear |

---

## Bảng tổng kết Safety Check

Sau khi chạy qua tất cả nhóm, điền vào đây:

```
═══════════════════════════════════════════════════
SAFETY CHECK RESULT
═══════════════════════════════════════════════════
Content Pack ID:  ____________________
Checked at:       ____________________
Checked by:       AI Worker (agent name)

BLOCKER flags:    ____ cái
WARNING flags:    ____ cái
NOTE flags:       ____ cái

Overall result:
  [ ] PASS — Không có BLOCKER. Output được.
  [ ] FAIL — Có ____ BLOCKER. Dừng output. Báo cáo ngay.

Nếu PASS với WARNING:
  → Output được nhưng ghi tất cả WARNING vào safety_check.flags[]
  → Ghi rõ ai_notes giải thích từng WARNING

Nếu FAIL (có BLOCKER):
  → DỪNG. Không output Content Pack.
  → Ghi lại mã BLOCKER và lý do fail.
  → Báo cáo cho Owner / ChatGPT để giải quyết.
═══════════════════════════════════════════════════
```

---

## Mã Flag Reference

| Mã Flag | Severity | Mô tả ngắn |
|---------|---------|-----------|
| `SECRET_EXPOSED` | BLOCKER | Phát hiện secret/credential trong output |
| `AUTO_POST_TRIGGER` | BLOCKER | Output chứa lệnh tự đăng bài |
| `STATUS_NOT_DRAFT` | BLOCKER | approval.status khác DRAFT |
| `HEALTH_CLAIM` | BLOCKER | Claim sức khỏe không có căn cứ |
| `COMPETITOR_MENTION` | BLOCKER | Đề cập đối thủ |
| `UNAUTHORIZED_PRICE` | BLOCKER | Giá không có nguồn |
| `UNAUTHORIZED_VOUCHER` | BLOCKER | Voucher không đăng ký |
| `SCHEMA_INCOMPLETE` | BLOCKER | Thiếu required field trong JSON |
| `OFFER_UNCONFIRMED` | WARNING | Offer status chưa xác nhận |
| `PRICE_UNCONFIRMED` | WARNING | Giá dùng [FILL] — chưa chính thức |
| `FAKE_URGENCY` | WARNING | Áp lực giả nghi ngờ |
| `FORMAL_TONE` | WARNING | Giọng văn quá trang trọng |
| `CAPS_OVERUSE` | WARNING | Viết hoa quá mức |
| `EMOJI_OVERLOAD` | WARNING | Quá nhiều emoji (>3) |
| `ADDRESS_UNFILLED` | WARNING | Địa chỉ dùng [FILL] |
| `HANDLE_UNCONFIRMED` | WARNING | Social handle chưa xác nhận |
| `PLATFORM_MISMATCH` | WARNING | content_type không phù hợp platform |
| `CAPTION_TOO_LONG` | WARNING | Caption vượt ngưỡng khuyến nghị |
| `HASHTAG_COUNT` | NOTE | Số hashtag ngoài range đề xuất |
| `NO_CTA` | NOTE | Caption thiếu CTA |
| `NO_CORE_HASHTAG` | NOTE | Thiếu #VịCuốn hoặc #ĂnVinh |
| `ASSUMPTION_UNLISTED` | NOTE | Giả định chưa được liệt kê trong metadata |

---

## Xử lý khi có BLOCKER

```
Khi phát hiện BLOCKER:

1. DỪNG ngay — không output Content Pack
2. Ghi log:
   - Mã BLOCKER
   - Vị trí trong output (field nào, dòng nào)
   - Nguyên nhân (AI tự sinh hay từ input brief sai?)
3. Báo cáo:
   "⛔ BLOCKER: [mã] — [mô tả]. Content Pack [ID] không thể output.
    Cần giải quyết: [hành động cần làm]"
4. Đề xuất sửa (nếu có thể):
   - Thay thông tin bằng [FILL] / [OWNER_CONFIRM]
   - Xóa phần vi phạm
   - Yêu cầu input brief rõ hơn từ Owner
```

---

## Xử lý khi chỉ có WARNING

```
Khi chỉ có WARNING (không có BLOCKER):

1. Output Content Pack — được phép
2. Trong safety_check.flags[]:
   - Ghi đủ: code, severity = "WARNING", detail
3. Trong safety_check.ai_notes:
   - Giải thích từng WARNING
   - Ghi rõ Owner cần làm gì trước khi đăng
4. Trong approval.status:
   - Giữ = "DRAFT"
   - Owner phải manually review WARNING trước khi approve
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — File tạo mới. 7 nhóm kiểm tra (Bảo mật, Thương hiệu, Offer/Giá, Thông tin, Schema, Platform, AI Behavior), flag reference table, xử lý BLOCKER/WARNING. | Claude Code (Builder) |
