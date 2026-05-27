# Content Pack JSON Schema — Vị Cuốn

*Phase 1.3 — Approval Sheet & Pipeline Schema*
*Schema JSON cho Content Pack — đơn vị dữ liệu cơ bản của pipeline.*
*AI Agent tạo Content Pack theo schema này. n8n xử lý Content Pack theo schema này.*

---

## Tổng quan

**Content Pack** là một object JSON hoàn chỉnh chứa tất cả thông tin AI tạo ra cho một bài đăng cụ thể — caption, script, brief, offer, persona, và metadata approval.

Một Content Pack = một hàng trong Google Sheet **Content Approval Queue**.

---

## JSON Schema (Full)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ContentPack",
  "description": "Vị Cuốn Content Pack — AI-generated content unit for approval pipeline",
  "type": "object",
  "required": [
    "id",
    "brand",
    "platform",
    "content_type",
    "objective",
    "persona",
    "pillar",
    "angle",
    "safety_check",
    "approval",
    "metadata"
  ],
  "properties": {

    "id": {
      "type": "string",
      "description": "ID duy nhất của content pack",
      "pattern": "^VQ-[A-Z]{2,3}-[A-Z]{2,6}-[0-9]{8}-[0-9]{3}$",
      "example": "VQ-FB-PROD-20260527-001"
    },

    "brand": {
      "type": "string",
      "description": "Tên thương hiệu",
      "enum": ["Vi Cuon"],
      "example": "Vi Cuon"
    },

    "platform": {
      "type": "string",
      "description": "Nền tảng đăng bài",
      "enum": ["Facebook", "TikTok", "Instagram", "Zalo OA", "Multi"],
      "example": "Facebook"
    },

    "content_type": {
      "type": "string",
      "description": "Định dạng nội dung",
      "enum": ["Post", "Reel", "Story", "Carousel", "TikTok Video", "Zalo Broadcast", "Short Video"],
      "example": "Post"
    },

    "objective": {
      "type": "string",
      "description": "Mục tiêu marketing chính của bài",
      "enum": ["awareness", "engagement", "conversion", "retention", "education"],
      "example": "engagement"
    },

    "persona": {
      "type": "object",
      "description": "Persona và segment mục tiêu",
      "required": ["segment"],
      "properties": {
        "segment": {
          "type": "string",
          "description": "Segment khách hàng theo customer_brain.md",
          "enum": ["Segment A", "Segment B", "Segment C", "All"],
          "example": "Segment A"
        },
        "persona_name": {
          "type": "string",
          "description": "Tên persona cụ thể (nếu có)",
          "example": "Lan — dân văn phòng 28 tuổi"
        },
        "pain_point": {
          "type": "string",
          "description": "Điểm đau của persona này mà bài content giải quyết",
          "example": "Không biết trưa ăn gì, không muốn đặt ship xa"
        }
      }
    },

    "pillar": {
      "type": "string",
      "description": "Content pillar theo content_pillars.md",
      "enum": ["PROD", "BTS", "PROMO", "STORY", "COM", "SEASON"],
      "example": "PROD"
    },

    "angle": {
      "type": "object",
      "description": "Content angle và hook",
      "required": ["code", "name"],
      "properties": {
        "code": {
          "type": "string",
          "description": "Mã angle theo content_angles.md",
          "example": "ANG-01"
        },
        "name": {
          "type": "string",
          "description": "Tên angle ngắn",
          "example": "hero-shot"
        },
        "hook": {
          "type": "string",
          "description": "Hook mở đầu bài (câu đầu tiên thu hút)",
          "example": "Cuốn đúng vị — no đúng bữa 🍜"
        }
      }
    },

    "offer": {
      "type": "object",
      "description": "Thông tin offer nếu bài có promotion (nullable — bỏ qua nếu không có offer)",
      "properties": {
        "offer_id": {
          "type": "string",
          "description": "ID offer theo offer_engine.md",
          "example": "OF-01"
        },
        "offer_name": {
          "type": "string",
          "description": "Tên hiển thị của offer",
          "example": "Combo Trưa Vị Cuốn"
        },
        "voucher_code": {
          "type": "string",
          "description": "Voucher code nếu có (phải có trong Google Sheet Vouchers)",
          "example": "VQ-LUNCH-20260601"
        },
        "offer_summary": {
          "type": "string",
          "description": "Tóm tắt ngắn offer cho Telegram notification",
          "example": "[FILL]đ — bánh tráng cuốn + bún trộn + nước. T2–T6, 11:00–14:00"
        },
        "valid_until": {
          "type": "string",
          "format": "date",
          "description": "Ngày hết hạn offer (YYYY-MM-DD)",
          "example": "2026-06-30"
        }
      }
    },

    "caption_options": {
      "type": "array",
      "description": "1–3 phiên bản caption để Owner chọn. Luôn có ít nhất 1 option.",
      "minItems": 1,
      "maxItems": 3,
      "items": {
        "type": "object",
        "required": ["version", "text"],
        "properties": {
          "version": {
            "type": "string",
            "description": "Ký hiệu phiên bản",
            "enum": ["v1", "v2", "v3"],
            "example": "v1"
          },
          "text": {
            "type": "string",
            "description": "Nội dung caption đầy đủ",
            "example": "Hôm nay ăn gì chưa bạn ơi?..."
          },
          "char_count": {
            "type": "integer",
            "description": "Số ký tự (tính bằng code, không tính emoji là nhiều ký tự)",
            "example": 248
          },
          "note": {
            "type": "string",
            "description": "Ghi chú về phiên bản này (phong cách, độ dài, v.v.)",
            "example": "Phiên bản ngắn, phù hợp TikTok"
          }
        }
      }
    },

    "script_options": {
      "type": "array",
      "description": "Script video nếu content_type là video/reel (nullable)",
      "items": {
        "type": "object",
        "required": ["version", "template_id", "scenes"],
        "properties": {
          "version": {
            "type": "string",
            "enum": ["v1", "v2"],
            "example": "v1"
          },
          "template_id": {
            "type": "string",
            "description": "Template script dùng từ video_script_templates.md",
            "example": "VS-01"
          },
          "duration_target": {
            "type": "string",
            "description": "Thời lượng video mục tiêu",
            "example": "15–30 giây"
          },
          "scenes": {
            "type": "array",
            "description": "Danh sách cảnh quay",
            "items": {
              "type": "object",
              "properties": {
                "scene_number": { "type": "integer", "example": 1 },
                "duration": { "type": "string", "example": "3 giây" },
                "visual": { "type": "string", "example": "Close-up bánh tráng cuốn vừa cuốn xong" },
                "audio": { "type": "string", "example": "ASMR: tiếng cuốn giòn" },
                "text_overlay": { "type": "string", "example": "Cuốn đúng vị — Vị Cuốn" }
              }
            }
          },
          "cta": {
            "type": "string",
            "description": "Call to action cuối video",
            "example": "Ghé Vị Cuốn — [địa chỉ]"
          }
        }
      }
    },

    "image_brief": {
      "type": "object",
      "description": "Brief chụp ảnh cho bài đăng",
      "required": ["subject", "composition"],
      "properties": {
        "subject": {
          "type": "string",
          "description": "Chủ thể chính của ảnh",
          "example": "Bánh tráng cuốn thịt heo vừa cuốn xong, đặt trên đĩa tre"
        },
        "composition": {
          "type": "string",
          "description": "Góc chụp và bố cục",
          "example": "45 độ từ trên xuống, rule of thirds, mắm nêm ở góc phải"
        },
        "lighting": {
          "type": "string",
          "description": "Yêu cầu ánh sáng",
          "example": "Ánh sáng tự nhiên từ cửa sổ bên trái, nền sáng ấm"
        },
        "props": {
          "type": "string",
          "description": "Props đi kèm trong ảnh",
          "example": "Chén mắm nêm đỏ cam, rau sống xanh tươi, đũa gỗ"
        },
        "avoid": {
          "type": "string",
          "description": "Những gì KHÔNG muốn trong ảnh",
          "example": "Không có bàn bẩn, không bóng tối, không khăn ăn nhàu nát"
        },
        "reference_style": {
          "type": "string",
          "description": "Phong cách ảnh tham khảo",
          "example": "Ảnh food photography phong cách Việt — ấm áp, tươi sáng, không quá studio"
        }
      }
    },

    "design_brief": {
      "type": "object",
      "description": "Brief thiết kế đồ họa (nullable — chỉ khi cần thiết kế banner/story frame)",
      "properties": {
        "format": {
          "type": "string",
          "description": "Định dạng và kích thước",
          "example": "Story 1080x1920px, Facebook Post 1200x1200px"
        },
        "main_text": {
          "type": "string",
          "description": "Text chính trên design",
          "example": "COMBO TRƯA [FILL]đ"
        },
        "sub_text": {
          "type": "string",
          "description": "Text phụ",
          "example": "Thứ 2–6 | 11:00–14:00 | Tại quán & ShopeeFood"
        },
        "color_theme": {
          "type": "string",
          "description": "Theme màu theo brand kit",
          "example": "Nền kem nhạt #FDF5E6, text nâu đất #2C1810, accent đỏ cam #C0392B"
        },
        "font": {
          "type": "string",
          "description": "Font chữ (theo brand_brain.md visual identity)",
          "example": "Heading: [Brand font], Body: Be Vietnam Pro"
        },
        "cta_button": {
          "type": "string",
          "description": "Nút CTA nếu có",
          "example": "ĐẶT NGAY → [Link]"
        }
      }
    },

    "safety_check": {
      "type": "object",
      "description": "Kết quả AI Self-Check — bắt buộc điền trước khi set READY_FOR_REVIEW",
      "required": ["passed", "checked_at", "flags"],
      "properties": {
        "passed": {
          "type": "boolean",
          "description": "true nếu không có BLOCKER flag",
          "example": true
        },
        "checked_at": {
          "type": "string",
          "format": "date-time",
          "description": "Thời điểm AI chạy self-check",
          "example": "2026-05-27T10:30:00+07:00"
        },
        "flags": {
          "type": "array",
          "description": "Danh sách flags phát hiện (empty array = không có flag)",
          "items": {
            "type": "object",
            "properties": {
              "code": {
                "type": "string",
                "description": "Mã flag",
                "example": "EMOJI_OVERLOAD"
              },
              "severity": {
                "type": "string",
                "enum": ["BLOCKER", "WARNING", "NOTE"],
                "example": "WARNING"
              },
              "detail": {
                "type": "string",
                "description": "Mô tả cụ thể",
                "example": "Phát hiện 5 emoji trong caption v1. Đã giảm xuống 2 trong v2."
              }
            }
          },
          "example": []
        },
        "ai_notes": {
          "type": "string",
          "description": "Ghi chú của AI về quá trình tạo và self-check",
          "example": "Giá OF-01 dùng placeholder [FILL] vì menu_brain.md chưa có giá xác nhận. Owner cần xác nhận giá trước khi đăng."
        }
      }
    },

    "approval": {
      "type": "object",
      "description": "Thông tin approval do Owner cập nhật",
      "required": ["status"],
      "properties": {
        "status": {
          "type": "string",
          "description": "Trạng thái hiện tại trong pipeline",
          "enum": ["IDEA", "DRAFT", "READY_FOR_REVIEW", "REVISION_REQUESTED", "APPROVED", "SCHEDULE_PROPOSED", "PUBLISHED_MANUAL", "REJECTED", "ARCHIVED"],
          "example": "READY_FOR_REVIEW"
        },
        "owner_decision": {
          "type": ["string", "null"],
          "description": "Quyết định của Owner (null khi chưa review)",
          "enum": ["APPROVED", "REVISION_REQUESTED", "REJECTED", null],
          "example": null
        },
        "revision_note": {
          "type": ["string", "null"],
          "description": "Ghi chú chỉnh sửa của Owner",
          "example": null
        },
        "approval_timestamp": {
          "type": ["string", "null"],
          "format": "date-time",
          "description": "Thời điểm Owner approve",
          "example": null
        },
        "proposed_publish_date": {
          "type": ["string", "null"],
          "format": "date-time",
          "description": "Ngày/giờ đăng do Owner đề xuất",
          "example": null
        },
        "manual_publish_link": {
          "type": ["string", "null"],
          "format": "uri",
          "description": "Link bài đã đăng (điền sau khi đăng)",
          "example": null
        },
        "revision_count": {
          "type": "integer",
          "description": "Số lần đã revision (max 3)",
          "minimum": 0,
          "maximum": 3,
          "default": 0,
          "example": 0
        }
      }
    },

    "metadata": {
      "type": "object",
      "description": "Metadata kỹ thuật và traceability",
      "required": ["created_at", "created_by_agent", "source_brain_version"],
      "properties": {
        "created_at": {
          "type": "string",
          "format": "date-time",
          "description": "Thời điểm content pack được tạo",
          "example": "2026-05-27T10:00:00+07:00"
        },
        "updated_at": {
          "type": "string",
          "format": "date-time",
          "description": "Thời điểm cập nhật lần cuối",
          "example": "2026-05-27T10:30:00+07:00"
        },
        "created_by_agent": {
          "type": "string",
          "description": "Agent hoặc người tạo",
          "example": "Claude Code (Builder)"
        },
        "source_brain_version": {
          "type": "string",
          "description": "Phiên bản Brain files dùng khi tạo",
          "example": "Phase 1.2"
        },
        "n8n_workflow_id": {
          "type": ["string", "null"],
          "description": "ID workflow n8n tạo pack này (null nếu tạo thủ công)",
          "example": null
        },
        "drive_folder_url": {
          "type": ["string", "null"],
          "format": "uri",
          "description": "Link Google Drive folder chứa files của pack này",
          "example": null
        },
        "sheet_row_id": {
          "type": ["integer", "null"],
          "description": "Số hàng trong Google Sheet (gán sau khi ghi vào sheet)",
          "example": null
        }
      }
    }
  }
}
```

---

## Ví dụ Content Pack Đầy đủ

```json
{
  "id": "VQ-FB-PROD-20260527-001",
  "brand": "Vi Cuon",
  "platform": "Facebook",
  "content_type": "Post",
  "objective": "engagement",

  "persona": {
    "segment": "Segment A",
    "persona_name": "Lan — dân văn phòng 28 tuổi",
    "pain_point": "Không biết trưa ăn gì, cần no nhanh, giá hợp lý"
  },

  "pillar": "PROD",

  "angle": {
    "code": "ANG-01",
    "name": "hero-shot",
    "hook": "Cuốn đúng vị — no đúng bữa 🍜"
  },

  "offer": null,

  "caption_options": [
    {
      "version": "v1",
      "text": "Cuốn đúng vị — no đúng bữa 🍜\n\nBánh tráng mỏng giòn, thịt heo tươi, cuốn cùng rau sống xanh mướt. Chấm mắm nêm tự pha chua cay vừa miệng — một bữa trưa đúng nghĩa.\n\n📍 Vị Cuốn — Vinh, Nghệ An\n⏰ Mở từ 10:00 mỗi ngày\n\n#VịCuốn #ĂnVinh #VinhNghệAn #BánhTráng #MonNgon",
      "char_count": 280,
      "note": "Phiên bản đầy đủ, tập trung vào product description"
    },
    {
      "version": "v2",
      "text": "Hôm nay ăn gì chưa bạn ơi?\n\nBánh tráng cuốn thịt heo nhà mình — cuốn tay, chấm mắm nêm tự pha. Đơn giản mà ngon lạ.\n\nGhé Vị Cuốn ở Vinh — 10:00 mỗi ngày nhé!\n\n#VịCuốn #ĂnVinh #VinhNghệAn",
      "char_count": 185,
      "note": "Phiên bản ngắn, giọng gần gũi hơn"
    }
  ],

  "script_options": null,

  "image_brief": {
    "subject": "Bánh tráng cuốn thịt heo vừa cuốn xong, đặt trên đĩa tre nhỏ",
    "composition": "45 độ từ trên xuống, bánh tráng cuốn ở trung tâm, mắm nêm ở góc phải trước",
    "lighting": "Ánh sáng tự nhiên từ cửa sổ bên trái, tone ấm vàng nhẹ",
    "props": "Chén mắm nêm đỏ cam, vài lá rau sống xanh bên cạnh, đũa gỗ",
    "avoid": "Không có bàn bẩn, không bóng tối, không ảnh mờ nhòe",
    "reference_style": "Food photography Việt Nam — ấm áp, tự nhiên, không quá studio"
  },

  "design_brief": null,

  "safety_check": {
    "passed": true,
    "checked_at": "2026-05-27T10:30:00+07:00",
    "flags": [],
    "ai_notes": "Không có giá trong bài. Không có offer. Không có claim sức khỏe. Emoji 1 cái/caption. Hashtag đầy đủ. Pass all checks."
  },

  "approval": {
    "status": "READY_FOR_REVIEW",
    "owner_decision": null,
    "revision_note": null,
    "approval_timestamp": null,
    "proposed_publish_date": null,
    "manual_publish_link": null,
    "revision_count": 0
  },

  "metadata": {
    "created_at": "2026-05-27T10:00:00+07:00",
    "updated_at": "2026-05-27T10:30:00+07:00",
    "created_by_agent": "Claude Code (Builder)",
    "source_brain_version": "Phase 1.2",
    "n8n_workflow_id": null,
    "drive_folder_url": null,
    "sheet_row_id": null
  }
}
```

---

## Mapping: JSON Schema ↔ Google Sheet Columns

| JSON Path | Google Sheet Column | Ghi chú |
|-----------|---------------------|---------|
| `id` | A: content_id | |
| `brand` | B: brand | |
| `platform` | C: platform | |
| `content_type` | D: content_type | |
| `pillar` | E: pillar | |
| `angle.code` | F: angle | |
| `offer.offer_id` | G: offer_code | null → để trống |
| `caption_options[0].text` | H: caption | Caption v1 (Owner chọn phiên bản trong Drive) |
| `script_options[0].scenes` | I: video_script | Serialized text |
| `image_brief.subject + composition` | J: image_brief | Summary text |
| `design_brief.main_text` | K: design_brief | Summary text hoặc null |
| `persona.segment` | L: target_persona | |
| `approval.status` | M: status | |
| `approval.owner_decision` | N: owner_decision | |
| `approval.revision_note` | O: revision_note | |
| `approval.approval_timestamp` | P: approval_timestamp | |
| `approval.proposed_publish_date` | Q: proposed_publish_date | |
| `approval.manual_publish_link` | R: manual_publish_link | |
| `metadata.created_by_agent` | S: created_by_agent | |
| `metadata.source_brain_version` | T: source_brain_version | |
| `safety_check.flags[].code` | U: safety_flags | Joined by "\|" |

---

## File Storage Convention (Google Drive)

```
Google Drive: FNB_OS_V1_CONTENT/
  └── Draft/
      └── 2026-05/
          └── Facebook/
              └── VQ-FB-PROD-20260527-001/
                  ├── content_pack.json       ← Full JSON schema
                  ├── caption_v1.md           ← Caption option 1
                  ├── caption_v2.md           ← Caption option 2 (nếu có)
                  ├── image_brief.md          ← Image brief chi tiết
                  └── design_brief.md         ← Design brief (nếu có)
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-05-27 | Phase 1.3 — File tạo mới. Full JSON schema với example, Google Sheet mapping, Drive file convention. | Claude Code (Builder) |
