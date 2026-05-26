# CRM Brain — Vị Cuốn

## CRM Platform
- Primary: [FILL: e.g., Google Sheets CRM tab / Zalo OA / custom]
- Backup: Google Sheets `CRM` tab

---

## Customer Data Fields

| Field | Type | Source | Notes |
|-------|------|--------|-------|
| customer_id | string | Auto-generated | Format: `VQ-[YYYYMMDD]-[SEQ]` |
| name | string | Self-reported | |
| phone | string | Self-reported | Vietnamese format |
| zalo_id | string | Zalo OA | Optional |
| segment | enum | CRM logic | New / Active / At-Risk / Lapsed / VIP |
| first_order_date | date | Order system | |
| last_order_date | date | Order system | |
| total_orders | integer | Order system | |
| total_spend | integer | Order system | VNĐ |
| preferred_items | array | Order history | |
| notes | text | Manual | |

---

## Follow-up Sequences

### New Customer (after first order)
| Step | Timing | Message | Channel |
|------|--------|---------|---------|
| 1 | +1 day | Thank you + feedback request | Zalo / SMS |
| 2 | +3 days | Menu highlight / upsell | Zalo |
| 3 | +7 days | Combo offer for second visit | Zalo |

### At-Risk Customer (no order 30–60 days)
| Step | Timing | Message | Channel |
|------|--------|---------|---------|
| 1 | Day 30 | "Lâu rồi không gặp!" + offer | Zalo |
| 2 | Day 45 | Last chance offer | Zalo |

### VIP Customer
| Step | Timing | Message | Channel |
|------|--------|---------|---------|
| 1 | Monthly | Exclusive offer preview | Zalo |
| 2 | Birthday | Birthday discount | Zalo / SMS |

---

## Segmentation Rules

| Segment | Condition |
|---------|-----------|
| New | First order within last 7 days |
| Active | Order within last 30 days |
| At-Risk | No order in 30–60 days |
| Lapsed | No order in 60+ days |
| VIP | Total orders ≥ [FILL: N] OR total spend ≥ [FILL: VNĐ] |

---

## Message Templates (Vietnamese)

### Thank You (New Customer)
```
Cảm ơn [Tên] đã ghé Vị Cuốn! 🌿
Hy vọng bạn thích [món đã đặt].
Lần sau nhớ ghé lại nhé — có combo trưa siêu ngon đang chờ!
```

### Win-Back (At-Risk)
```
[Tên] ơi, lâu rồi không thấy bạn ghé 🥺
Hôm nay có [offer] dành riêng cho bạn!
[CTA + link đặt hàng]
```

---

## Privacy & Consent Rules
- Only message customers who opted in via Zalo OA follow or explicit consent
- No cold messaging via phone/SMS without consent
- Customer data stored in Google Sheets with access controls
- No PII stored in repo

---

## Changelog
| Date | Change | Author |
|------|--------|--------|
| 2026-05-26 | File created — placeholders only | Builder Agent (Claude) |
