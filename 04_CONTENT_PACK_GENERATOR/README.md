# 04 — Content Pack Generator

*Phase 1.4 — Draft Content Pack Generator Schema*
*Builder: Claude Code (AGT-02) | Date: 2026-05-27*

---

## Mục đích

Thư mục này định nghĩa **cách AI Agent tạo ra Content Pack** cho Vị Cuốn — từ input brief đến output JSON hoàn chỉnh sẵn sàng đưa vào Approval Pipeline.

Content Pack Generator không đăng bài. Không tự chạy. Đây là schema + prompt template cho AI Worker đọc và thực thi khi Owner giao brief.

---

## Vị trí trong kiến trúc FnB OS V1

```
Owner / ChatGPT
  └── giao Input Brief (input_brief_template.md)
        └── AI Content Worker đọc:
              ├── 01_BRAIN/         ← Brand, persona, offer, design rules
              ├── 02_CONTENT_ENGINE/ ← Pillars, angles, scripts, captions
              └── 03_APPROVAL_PIPELINE/ ← Status rules, JSON schema
                    ↓
              Tạo Content Pack theo content_pack_generator_schema.md
              Dùng prompt từ content_pack_prompt_template.md
              Chạy safety check từ safety_self_check.md
                    ↓
              Output: output_examples.md (xem ví dụ)
                    ↓
              Giao Owner → Approval Pipeline (03_APPROVAL_PIPELINE/)
```

---

## Danh sách file

| File | Mục đích |
|------|---------|
| `content_pack_generator_schema.md` | Định nghĩa input fields + output fields đầy đủ |
| `content_pack_prompt_template.md` | Prompt template cho AI Worker sinh Content Pack |
| `input_brief_template.md` | Form Owner/ChatGPT điền để giao brief cho AI |
| `output_examples.md` | 3 ví dụ Content Pack hoàn chỉnh cho Vị Cuốn |
| `safety_self_check.md` | Danh sách kiểm tra AI tự review trước khi output |
| `README.md` | File này |

---

## Luồng làm việc

```
1. Owner / ChatGPT điền input_brief_template.md
   ↓
2. AI Worker đọc brief + đọc Brand Brain + Content Engine + Approval Pipeline
   ↓
3. AI Worker chạy content_pack_prompt_template.md để sinh draft
   ↓
4. AI Worker tự chạy safety_self_check.md trước khi output
   ↓
5. Output: Content Pack theo content_pack_generator_schema.md
   ↓
6. Content Pack vào 03_APPROVAL_PIPELINE/ → Owner review → APPROVED / REVISION
   ↓
7. Owner đăng thủ công (KHÔNG auto-post)
```

---

## Quy tắc TUYỆT ĐỐI

| Quy tắc | Mô tả |
|---------|-------|
| **KHÔNG auto-post** | Content Pack chỉ là DRAFT — KHÔNG bao giờ tự đăng |
| **KHÔNG hardcode giá** | Giá phải từ `menu_brain.md` hoặc `offer_engine.md` — dùng `[FILL]` nếu chưa có |
| **KHÔNG tự tạo offer** | Chỉ dùng offer từ `offer_engine.md` |
| **KHÔNG claim sức khỏe** | Không viết "tốt cho sức khỏe", "giảm cân", "detox" |
| **KHÔNG đề cập đối thủ** | Không nhắc tên quán khác |
| **Đánh dấu [FILL]** | Mọi thông tin chưa xác nhận đều phải có `[FILL]` |
| **Đánh dấu [OWNER_CONFIRM]** | Mọi giả định cần Owner xác nhận đều dùng tag này |
| **Chỉ draft** | Tất cả output đều ở trạng thái `DRAFT` — không `READY_FOR_REVIEW` tự động |

---

## Trạng thái Phase 1.4

| Trạng thái | Ngày | Người thực hiện |
|-----------|------|----------------|
| Builder Done | 2026-05-27 | Claude Code (AGT-02) |
| Codex Review | PENDING | Codex (AGT-04) |
| Owner Approval | PENDING | Owner |
| Commit | PENDING | Owner |

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — File tạo mới. README cho Content Pack Generator. | Claude Code (Builder) |
