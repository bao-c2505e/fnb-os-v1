# PHASE 1.4 — Draft Content Pack Generator Schema

*Dự án: FnB OS V1 — Vị Cuốn Growth OS*
*Builder: Claude Code (AGT-02)*
*Ngày hoàn thành (Builder): 2026-05-27*
*Trạng thái: REVIEW_REQUESTED*

---

## Tóm tắt Phase

Phase 1.4 xây dựng schema và prompt template đầy đủ để AI Agent có thể tạo **Draft Content Pack** cho Vị Cuốn — từ một Input Brief đơn giản của Owner/ChatGPT, qua việc đọc Brand Brain + Content Engine + Approval Pipeline, đến một Content Pack JSON hoàn chỉnh chờ Owner phê duyệt.

**Đây là lớp "AI tạo nội dung" đầu tiên trong FnB OS V1** — kết nối dữ liệu tĩnh (Phase 1.1–1.3) với output nội dung có thể sử dụng thực tế.

---

## Deliverables

### Thư mục mới tạo

```
04_CONTENT_PACK_GENERATOR/
├── README.md                         ← Kiến trúc tổng quan + luồng làm việc
├── content_pack_generator_schema.md  ← Input/Output schema đầy đủ
├── content_pack_prompt_template.md   ← Prompt template cho AI Worker
├── input_brief_template.md           ← Form Owner/ChatGPT điền brief
├── output_examples.md                ← 3 Content Pack ví dụ
└── safety_self_check.md              ← Checklist AI tự kiểm tra
```

### File báo cáo phase

```
docs/phase-1/PHASE_1_4_DRAFT_CONTENT_PACK_GENERATOR_SCHEMA.md  ← File này
```

---

## Chi tiết từng deliverable

### 1. README.md
- Mô tả vị trí của Content Pack Generator trong kiến trúc FnB OS V1
- Sơ đồ luồng: Owner điền brief → AI đọc Brain/Engine → Tạo pack → Safety check → Giao Owner → Approval Pipeline
- Danh sách file và mục đích
- Quy tắc tuyệt đối (KHÔNG auto-post, KHÔNG hardcode giá, v.v.)

### 2. content_pack_generator_schema.md
Định nghĩa đầy đủ 7 phần:
- **INPUT schema** — 11 trường: brand, platform, objective, target_persona, pillar, angle, offer_type, content_type, tone, constraints, owner_notes
- **OUTPUT schema** — 12 nhóm trường: content_id, caption_options, hook_options, short_video_script_options, image_brief, design_brief, offer_summary, target_persona, platform_fit, safety_flags, approval_required, metadata
- **Content ID convention** — format `VQ-[PLAT]-[PILLAR]-[YYYYMMDD]-[SEQ]` + bảng platform/pillar codes
- **Platform Compatibility Matrix** — content_type allowed, pillar ưu tiên, max chars, hashtag rules
- **Pillar × Angle Mapping** — AI dùng khi `angle = "AUTO"`
- **Offer Integration Rules** — 5 quy tắc khi offer_type không null
- **[FILL] / [OWNER_CONFIRM] Convention** — chuẩn đánh dấu giả định

### 3. content_pack_prompt_template.md
Prompt 5 phần gửi cho AI Worker:
- **Phần 1** — Đọc nguồn: Brand Brain → Customer Brain → Content Engine → Offer Engine → Approval Pipeline
- **Phần 2** — Input Brief với 11 placeholder `{{FIELD}}`
- **Phần 3** — Tạo Content Pack: 12 mục (ID, caption, hook, script, image brief, design brief, offer, persona, platform fit, safety, approval, metadata)
- **Phần 4** — Format output: BLOCK A (Markdown cho Owner đọc) + BLOCK B (JSON-like cho n8n/Sheet)
- **Phần 5** — Kiểm tra cuối 11 điểm trước khi output

### 4. input_brief_template.md
- Form điền đầy đủ với checkbox cho từng option
- Tất cả 11 fields với hướng dẫn rõ ràng
- 3 ví dụ brief đã điền sẵn (Bữa Trưa / Ngày Mưa / Combo Gia Đình)
- FAQ xử lý các trường hợp đặc biệt

### 5. output_examples.md
3 Content Pack ví dụ hoàn chỉnh — mỗi pack có BLOCK A (Markdown) và BLOCK B (JSON):

| # | ID | Chủ đề | Đặc điểm |
|---|-----|--------|---------|
| 1 | VQ-FB-PRMO-20260527-001 | Bữa Trưa Văn Phòng | PROMO, Segment A, OF-01, angle C1 |
| 2 | VQ-FB-SESN-20260527-001 | Ngày Mưa / Mắm Nêm | SEASON, All, OF-06 (WARNING), angle C5 |
| 3 | VQ-FB-PRMO-20260527-002 | Combo Gia Đình Cuối Tuần | PROMO, Segment B, OF-03, angle C4 |

### 6. safety_self_check.md
7 nhóm kiểm tra với 35 điểm kiểm tra:
- **Nhóm 1** — Bảo mật & Tuân thủ (5 BLOCKER)
- **Nhóm 2** — Nội dung Thương hiệu (3 BLOCKER, 4 WARNING, 2 NOTE)
- **Nhóm 3** — Offer & Giá (2 BLOCKER, 2 WARNING, 1 NOTE)
- **Nhóm 4** — Thông tin bắt buộc (2 WARNING, 1 NOTE)
- **Nhóm 5** — Schema & Format (2 BLOCKER, 4 WARNING, 1 NOTE)
- **Nhóm 6** — Platform Fit (2 WARNING, 1 NOTE)
- **Nhóm 7** — AI Behavior (2 BLOCKER, 2 WARNING ... incl. AI-04 NOTE)
- Bảng tổng kết result template
- Flag code reference (22 mã flag)
- Quy trình xử lý BLOCKER và WARNING

---

## Luồng hoạt động Phase 1.4

```
Owner / ChatGPT
  └── Điền input_brief_template.md (11 trường)
        ↓
  AI Worker nhận brief
        ↓
  [Bước 1] Đọc Brand Brain (brand_brain.md, customer_brain.md)
  [Bước 2] Đọc Content Engine (content_pillars.md, content_angles.md,
                               caption_templates.md, video_script_templates.md)
  [Bước 3] Đọc Offer Engine nếu offer_type ≠ null (offer_engine.md)
  [Bước 4] Đọc Approval Pipeline rules (content_pack_json_schema.md)
        ↓
  [Bước 5] Tạo draft theo content_pack_prompt_template.md
  [Bước 6] Chạy safety_self_check.md
        ↓
  Nếu BLOCKER → Dừng. Báo cáo Owner.
  Nếu chỉ WARNING → Output với flags rõ ràng.
  Nếu PASS → Output đầy đủ.
        ↓
  Output: Content Pack DRAFT
    - BLOCK A (Markdown cho Owner đọc)
    - BLOCK B (JSON theo content_pack_json_schema.md)
        ↓
  Owner review → APPROVED hoặc REVISION_REQUESTED
        ↓
  Nếu APPROVED → Owner đăng thủ công (KHÔNG auto-post)
```

---

## Giả định (Assumptions) đã đặt trong Phase 1.4

| # | Giả định | Lý do | Cần Owner xác nhận |
|---|---------|-------|-------------------|
| A1 | Brand chỉ có "Vi Cuon" trong Phase 1 | Scope hiện tại | Khi thêm brand mới |
| A2 | Giá tất cả offer dùng `[FILL]` | menu_brain.md chưa có giá xác nhận | Owner điền giá thật |
| A3 | Platform Compatibility Matrix dựa trên content_pillars.md Phase 1.2 | Chưa có data thực tế | Điều chỉnh sau khi chạy thật |
| A4 | Persona names là gợi ý ("Lan văn phòng") không phải persona chính thức | customer_brain.md có thể có persona khác | Owner xác nhận persona chính thức |
| A5 | Giờ đăng tối ưu từ content_pillars.md — chưa có data analytics | Không có data thực tế | A/B test sau khi chạy |
| A6 | Video script templates tham chiếu VS-01, VS-02, v.v. từ video_script_templates.md | Chưa verify đủ template IDs | Xem video_script_templates.md |
| A7 | Reel/Short Video option trong ví dụ 2 là tùy chọn | Quán chưa xác nhận setup quay video | Owner quyết định |
| A8 | Design brief dùng hex màu gợi ý từ brand_brain.md | Brand kit chính thức chưa có | Owner xác nhận brand kit |

---

## Kết nối với các Phase trước

| Phase | File | Cách Phase 1.4 sử dụng |
|-------|------|----------------------|
| 1.1 | `01_BRAIN/brand_brain.md` | Brand voice, safety rules, visual identity |
| 1.1 | `01_BRAIN/customer_brain.md` | Persona, pain points, segment |
| 1.1 | `01_BRAIN/offer_brain.md` | Offer logic cơ bản |
| 1.2 | `02_CONTENT_ENGINE/content_pillars.md` | 6 pillars, timing, platform fit |
| 1.2 | `02_CONTENT_ENGINE/content_angles.md` | 25 angles, hook templates |
| 1.2 | `02_CONTENT_ENGINE/offer_engine.md` | 9 offer types với messaging templates |
| 1.2 | `02_CONTENT_ENGINE/caption_templates.md` | Caption structure patterns |
| 1.2 | `02_CONTENT_ENGINE/video_script_templates.md` | Video script templates |
| 1.3 | `03_APPROVAL_PIPELINE/content_pack_json_schema.md` | Output JSON schema |
| 1.3 | `03_APPROVAL_PIPELINE/approval_sheet_schema.md` | Google Sheet column mapping |
| 1.3 | `02_CONTENT_ENGINE/approval_rules.md` | Safety rules tham chiếu |

---

## Trạng thái Safety Review Phase 1.4

| Quy tắc | Tuân thủ |
|---------|---------|
| KHÔNG tạo production n8n workflow | ✅ Không có workflow nào được tạo |
| KHÔNG kết nối API thật | ✅ Không có API call nào |
| KHÔNG auto-post / auto-reply | ✅ Tất cả output đều DRAFT, manual publish |
| KHÔNG hardcode secret | ✅ Không có secret trong bất kỳ file nào |
| KHÔNG commit .claude/ | ✅ .claude/ không được đề cập |
| KHÔNG commit / push trước Owner approval | ✅ Chưa commit, chưa push |
| Tất cả Content Pack ví dụ = DRAFT | ✅ approval.status = "DRAFT" trong mọi ví dụ |
| Giá dùng [FILL] | ✅ Tất cả giá đều [FILL] vì menu_brain.md chưa có |

---

## Tiêu chí Review (Codex / Owner)

### BLOCKER (Codex phải flag)
- [ ] Secret/API key/token thật trong bất kỳ file nào
- [ ] .claude/ được đề cập để commit
- [ ] Production n8n workflow được tạo
- [ ] Auto-post / auto-reply behavior được định nghĩa
- [ ] File trống, unusable, hoặc hoàn toàn không liên quan đến Vị Cuốn

### PASS (không cần block)
- [ ] Schema input/output có đủ 11+12 trường theo yêu cầu Phase 1.4
- [ ] Prompt template đủ 5 phần (đọc nguồn, input, tạo pack, format, kiểm tra)
- [ ] Ít nhất 3 ví dụ Content Pack (office lunch, ngày mưa, gia đình combo)
- [ ] Safety check có phân loại BLOCKER / WARNING / NOTE
- [ ] Tất cả output ví dụ ở trạng thái DRAFT
- [ ] Tất cả giá dùng [FILL]

### WARNING (Codex ghi chú nhưng không block)
- [ ] Wording giả định trong persona names
- [ ] Giờ đăng chưa verify với data thực tế

---

## Prompt cho Codex Reviewer

```
═══════════════════════════════════════════════════════════════
CODEX REVIEW REQUEST — PHASE 1.4
═══════════════════════════════════════════════════════════════

Dự án: FnB OS V1 — Vị Cuốn Growth OS
Phase: 1.4 — Draft Content Pack Generator Schema
Builder: Claude Code (AGT-02)
Date: 2026-05-27

NHIỆM VỤ CỦA CODEX:
Review các file sau trong thư mục 04_CONTENT_PACK_GENERATOR/:
1. README.md
2. content_pack_generator_schema.md
3. content_pack_prompt_template.md
4. input_brief_template.md
5. output_examples.md
6. safety_self_check.md

Và file báo cáo:
7. docs/phase-1/PHASE_1_4_DRAFT_CONTENT_PACK_GENERATOR_SCHEMA.md

TIÊU CHÍ BLOCK (Dừng — phải sửa trước khi Owner approve):
1. Secret/API key/token/password thật trong bất kỳ file nào
2. .claude/ được đề cập để commit
3. Production n8n workflow được tạo
4. Auto-post / auto-reply / chạy ads behavior được định nghĩa
5. File trống hoặc hoàn toàn không liên quan đến Vị Cuốn
6. Content Pack ví dụ có approval.status ≠ DRAFT

TIÊU CHÍ PASS (không block, ghi chú nếu cần):
1. Input schema đủ 11 trường theo OBJECTIVE của Phase 1.4
2. Output schema đủ 12 nhóm trường theo OBJECTIVE
3. Prompt template đủ 5 phần và có thể thực thi được
4. 3 ví dụ Content Pack cho: văn phòng trưa, ngày mưa, combo gia đình
5. Safety check phân loại rõ BLOCKER / WARNING / NOTE
6. Tất cả giá là [FILL], tất cả offer status là [OWNER_CONFIRM]

HÀNH ĐỘNG:
- Nếu PASS → Ghi "REVIEW_PASS" vào đây và notify Owner approve + commit
- Nếu FAIL → Ghi "REVIEW_FAIL", liệt kê từng BLOCKER, notify Builder sửa

Output của Codex:
  Verdict: [REVIEW_PASS / REVIEW_FAIL]
  Blockers (nếu có): [danh sách]
  Warnings (nếu có): [danh sách]
  Notes: [ghi chú thêm]
═══════════════════════════════════════════════════════════════
```

---

## Git Status Summary

| File | Trạng thái |
|------|-----------|
| `04_CONTENT_PACK_GENERATOR/README.md` | Untracked (mới tạo) |
| `04_CONTENT_PACK_GENERATOR/content_pack_generator_schema.md` | Untracked (mới tạo) |
| `04_CONTENT_PACK_GENERATOR/content_pack_prompt_template.md` | Untracked (mới tạo) |
| `04_CONTENT_PACK_GENERATOR/input_brief_template.md` | Untracked (mới tạo) |
| `04_CONTENT_PACK_GENERATOR/output_examples.md` | Untracked (mới tạo) |
| `04_CONTENT_PACK_GENERATOR/safety_self_check.md` | Untracked (mới tạo) |
| `docs/phase-1/PHASE_1_4_DRAFT_CONTENT_PACK_GENERATOR_SCHEMA.md` | Untracked (mới tạo) |
| `06_HANDOFF/PHASE_STATUS.md` | Modified |
| `06_HANDOFF/NEXT_ACTIONS.md` | Modified |

**Commit: CHƯA THỰC HIỆN — chờ Owner approval**
**Push: CHƯA THỰC HIỆN — chờ Owner approval**

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.4 — Builder done. 6 files trong 04_CONTENT_PACK_GENERATOR/ + báo cáo phase. Awaiting Codex review → Owner approval → commit. | Claude Code (Builder) |
