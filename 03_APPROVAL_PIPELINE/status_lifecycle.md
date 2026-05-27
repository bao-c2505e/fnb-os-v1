# Status Lifecycle — Content Approval Pipeline

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Vòng đời trạng thái nội dung từ lúc có ý tưởng đến khi đăng hoặc lưu trữ.*
*AI Agent bắt buộc tuân theo vòng đời này. Không được bỏ qua bước nào.*

---

## Tổng quan Vòng đời

```
IDEA
  ↓
DRAFT
  ↓
READY_FOR_REVIEW
  ↓ (Owner nhận thông báo)
  ├─→ REVISION_REQUESTED → (quay lại DRAFT)
  ├─→ REJECTED → ARCHIVED
  └─→ APPROVED
        ↓
     SCHEDULE_PROPOSED
        ↓ (Owner xác nhận thời điểm đăng)
     PUBLISHED_MANUAL
        ↓ (sau khi đăng xong)
     ARCHIVED
```

---

## Chi tiết từng Trạng thái

### 1. IDEA

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `IDEA` |
| **Ý nghĩa** | Ý tưởng nội dung vừa được ghi lại, chưa có bản nháp nào |
| **Ai set** | AI Agent / Nhân viên / Owner |
| **Bước tiếp theo** | AI hoặc nhân viên bắt đầu viết draft → chuyển sang `DRAFT` |
| **Yêu cầu** | Phải có: `pillar`, `angle`, `platform`, `content_type` |
| **Cấm** | Không gửi Owner duyệt khi còn ở IDEA |

---

### 2. DRAFT

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `DRAFT` |
| **Ý nghĩa** | AI đã tạo bản nháp caption / script / brief nhưng chưa tự kiểm tra xong |
| **Ai set** | AI Agent (tự động sau khi tạo xong nội dung) |
| **Bước tiếp theo** | AI tự chạy Safety Self-Check → nếu pass → chuyển sang `READY_FOR_REVIEW` |
| **Yêu cầu** | Caption hoặc script đã có nội dung. Image brief hoặc design brief đã có. |
| **Cấm** | Không gửi Owner duyệt khi còn là DRAFT (AI phải tự check trước) |

**AI Self-Check khi ở DRAFT:**
```
✅ Giá trong bài có trong menu_brain.md hoặc offer_engine.md?
✅ Không có claim sức khỏe / dinh dưỡng không có căn cứ?
✅ Không nhắc tên đối thủ?
✅ Không tạo fake urgency?
✅ Giọng điệu phù hợp brand voice?
✅ Hashtag đúng (#VịCuốn #ĂnVinh #VinhNghệAn)?
✅ Emoji ≤ 3 cái?
✅ Nếu có offer → offer đó có trong offer_engine.md không?

Nếu tất cả ✅ → set status = READY_FOR_REVIEW
Nếu có ❌ → sửa và tự check lại. Không set READY_FOR_REVIEW khi chưa pass.
```

---

### 3. READY_FOR_REVIEW

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `READY_FOR_REVIEW` |
| **Ý nghĩa** | AI đã tự check và pass. Bài đã sẵn sàng để Owner duyệt. |
| **Ai set** | AI Agent (sau khi AI Self-Check pass) |
| **Hành động tự động** | AI gửi thông báo Telegram cho Owner kèm tóm tắt nội dung |
| **Bước tiếp theo** | Owner review → `APPROVED` hoặc `REVISION_REQUESTED` hoặc `REJECTED` |
| **Yêu cầu** | AI Self-Check đã pass 100% |
| **Cấm** | AI không được set READY_FOR_REVIEW nếu chưa pass Self-Check |

---

### 4. REVISION_REQUESTED

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `REVISION_REQUESTED` |
| **Ý nghĩa** | Owner đã xem và yêu cầu chỉnh sửa. Bài chưa đạt yêu cầu. |
| **Ai set** | Owner |
| **Yêu cầu** | Owner phải ghi `revision_note` giải thích cần sửa gì |
| **Bước tiếp theo** | AI đọc `revision_note` → sửa bài → chạy lại Self-Check → set `DRAFT` → rồi `READY_FOR_REVIEW` |
| **Số lần tối đa** | Nếu revision ≥ 3 lần mà không đạt → Owner xem xét `REJECTED` |

---

### 5. APPROVED

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `APPROVED` |
| **Ý nghĩa** | Owner đã duyệt nội dung. Bài được phép đăng. |
| **Ai set** | Owner |
| **Yêu cầu** | Owner phải điền `approval_timestamp` và `owner_decision = APPROVED` |
| **Bước tiếp theo** | Owner đề xuất ngày đăng → set `SCHEDULE_PROPOSED` |
| **Cấm** | AI không tự set trạng thái này |

---

### 6. SCHEDULE_PROPOSED

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `SCHEDULE_PROPOSED` |
| **Ý nghĩa** | Owner đã chọn ngày/giờ đăng thủ công. Bài đang chờ đến thời điểm đăng. |
| **Ai set** | Owner |
| **Yêu cầu** | `proposed_publish_date` phải được điền |
| **Bước tiếp theo** | Đến ngày đăng → Owner đăng tay → set `PUBLISHED_MANUAL` |
| **Cấm** | AI không tự đăng bài. Không có auto-schedule trong giai đoạn này. |

---

### 7. PUBLISHED_MANUAL

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `PUBLISHED_MANUAL` |
| **Ý nghĩa** | Bài đã được Owner đăng tay lên platform. |
| **Ai set** | Owner |
| **Yêu cầu** | `manual_publish_link` phải được điền (link bài đã đăng) |
| **Bước tiếp theo** | Sau chu kỳ báo cáo → set `ARCHIVED` |
| **Lưu ý** | Đây là trạng thái cuối của luồng thành công |

---

### 8. REJECTED

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `REJECTED` |
| **Ý nghĩa** | Owner từ chối bài này hoàn toàn, không cần sửa lại. |
| **Ai set** | Owner |
| **Yêu cầu** | Owner ghi `owner_decision = REJECTED` và lý do trong `revision_note` |
| **Bước tiếp theo** | Chuyển sang `ARCHIVED` |
| **Lưu ý** | REJECTED khác REVISION_REQUESTED — REJECTED không cần AI sửa lại |

---

### 9. ARCHIVED

| Trường | Giá trị |
|--------|---------|
| **Mã trạng thái** | `ARCHIVED` |
| **Ý nghĩa** | Nội dung đã hoàn thành vòng đời (đã đăng) hoặc bị từ chối vĩnh viễn. |
| **Ai set** | System / Owner |
| **Yêu cầu** | Không |
| **Bước tiếp theo** | Không có — đây là trạng thái kết thúc |
| **Lưu ý** | Bài PUBLISHED_MANUAL sau 30 ngày tự động suggest ARCHIVED để dọn queue |

---

## Bảng Tóm tắt Trạng thái

| Trạng thái | Ai set | Ai nhận thông báo | Hành động tiếp theo |
|-----------|--------|------------------|---------------------|
| `IDEA` | AI / Nhân viên / Owner | — | AI bắt đầu viết draft |
| `DRAFT` | AI | — | AI tự kiểm tra |
| `READY_FOR_REVIEW` | AI | **Owner (Telegram)** | Owner review |
| `REVISION_REQUESTED` | Owner | AI Agent | AI sửa → DRAFT |
| `APPROVED` | **Owner** | AI Agent | Owner chọn ngày đăng |
| `SCHEDULE_PROPOSED` | Owner | — | Owner đăng đúng ngày |
| `PUBLISHED_MANUAL` | **Owner** | — | Lưu link, ghi nhận |
| `REJECTED` | **Owner** | AI Agent | → ARCHIVED |
| `ARCHIVED` | System / Owner | — | Kết thúc |

---

## Transition Rules (Luật chuyển trạng thái)

```
ALLOWED TRANSITIONS:
IDEA → DRAFT
DRAFT → READY_FOR_REVIEW  (chỉ khi AI Self-Check pass)
READY_FOR_REVIEW → APPROVED
READY_FOR_REVIEW → REVISION_REQUESTED
READY_FOR_REVIEW → REJECTED
REVISION_REQUESTED → DRAFT
APPROVED → SCHEDULE_PROPOSED
SCHEDULE_PROPOSED → PUBLISHED_MANUAL
PUBLISHED_MANUAL → ARCHIVED
REJECTED → ARCHIVED

FORBIDDEN TRANSITIONS:
IDEA → READY_FOR_REVIEW  (phải qua DRAFT trước)
IDEA → APPROVED  (AI không được tự approve)
DRAFT → APPROVED  (phải qua READY_FOR_REVIEW trước)
APPROVED → PUBLISHED_MANUAL  (phải qua SCHEDULE_PROPOSED trước)
ANY → PUBLISHED_MANUAL  (chỉ Owner set sau khi đăng tay)
ARCHIVED → ANY  (ARCHIVED là trạng thái cuối)
```

---

## Thời gian Tối đa ở mỗi Trạng thái

| Trạng thái | Thời gian tối đa đề xuất | Hành động nếu quá hạn |
|-----------|------------------------|----------------------|
| IDEA | 7 ngày | Nhắc Owner quyết định tiếp tục hay ARCHIVED |
| DRAFT | 3 ngày | Nhắc AI hoàn thành hoặc escalate |
| READY_FOR_REVIEW | 48 giờ | Nhắc Owner lần 2 |
| REVISION_REQUESTED | 3 ngày | Nhắc AI sửa xong |
| APPROVED | 14 ngày | Nhắc Owner đăng hoặc đặt SCHEDULE_PROPOSED |
| SCHEDULE_PROPOSED | Đến ngày đăng + 3 ngày | Nhắc Owner nếu qua ngày đăng mà chưa PUBLISHED |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. 9 trạng thái, transition rules, time limits. | Claude Code (Builder) |
