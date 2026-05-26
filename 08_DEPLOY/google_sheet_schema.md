# Google Sheet Schema — FnB OS V1

## Sheet Name
`FnB OS V1 — Vị Cuốn`

## Tabs (in order)

---

### Tab 1: Campaigns
| Column | Type | Description |
|--------|------|-------------|
| campaign_id | string | VQ-CAMP-[YYYYMMDD]-[SEQ] |
| name | string | Human-readable name |
| type | enum | content / ads / crm / combo / event / seasonal |
| status | enum | new / in_progress / approved / scheduled / active / completed / cancelled |
| start_date | date | YYYY-MM-DD |
| end_date | date | YYYY-MM-DD |
| target_segment | enum | office_workers / families / students / health_conscious / all |
| dish_name | string | Featured dish |
| offer | string | Offer description |
| platforms | string | Comma-separated list |
| budget_placeholder | string | Placeholder note only |
| notes | string | Free text |
| created_at | datetime | ISO8601 |
| created_by | string | Agent name |

---

### Tab 2: Content Packs
| Column | Type | Description |
|--------|------|-------------|
| content_pack_id | string | VQ-CP-[YYYYMMDD]-[SEQ] |
| campaign_id | string | FK to Campaigns |
| platform | enum | facebook / tiktok / instagram / zalo |
| content_pillar | enum | product / promotion / behind_scenes / education / community |
| caption_vi | string | Vietnamese caption |
| hashtags | string | Comma-separated |
| call_to_action | string | CTA text |
| post_time_suggestion | time | HH:MM |
| confidence_score | number | 0.0–1.0 |
| requires_human_review | boolean | TRUE/FALSE |
| status | enum | draft / qc_pass / qc_fail / approved / rejected / scheduled / posted |
| qc_score | number | 0.0–1.0 |
| approval_id | string | FK to Approvals |
| drive_file_url | string | Google Drive link |
| generated_at | datetime | ISO8601 |
| approved_at | datetime | ISO8601 |
| scheduled_at | datetime | ISO8601 |

---

### Tab 3: Design Briefs
| Column | Type | Description |
|--------|------|-------------|
| design_brief_id | string | VQ-DB-[YYYYMMDD]-[SEQ] |
| campaign_id | string | FK to Campaigns |
| content_pack_id | string | FK to Content Packs |
| format | enum | feed_square / feed_portrait / story / cover / thumbnail |
| dimensions | string | e.g., 1080x1080px |
| status | enum | draft / approved / rejected / in_production / delivered |
| drive_file_url | string | Google Drive link |
| generated_at | datetime | ISO8601 |

---

### Tab 4: Ads Packs
| Column | Type | Description |
|--------|------|-------------|
| ads_pack_id | string | VQ-ADS-[YYYYMMDD]-[SEQ] |
| campaign_id | string | FK to Campaigns |
| platform | enum | facebook / tiktok / google |
| objective | enum | awareness / engagement / conversion / traffic |
| headline | string | Max 40 chars |
| body_copy | string | Max 125 chars |
| cta_button | string | Standard CTA |
| status | enum | draft / approved / rejected / ready_for_upload / live / paused |
| drive_file_url | string | Google Drive link |
| generated_at | datetime | ISO8601 |

---

### Tab 5: CRM
| Column | Type | Description |
|--------|------|-------------|
| customer_id | string | VQ-[YYYYMMDD]-[SEQ] |
| name | string | Customer name |
| phone | string | Vietnamese phone format |
| zalo_id | string | Zalo user ID |
| segment | enum | new / active / at_risk / lapsed / vip |
| first_order_date | date | YYYY-MM-DD |
| last_order_date | date | YYYY-MM-DD |
| total_orders | integer | Count |
| total_spend | integer | VNĐ |
| preferred_items | string | Comma-separated |
| do_not_contact | boolean | TRUE/FALSE |
| notes | string | Free text |

---

### Tab 6: CRM Messages Sent
| Column | Type | Description |
|--------|------|-------------|
| crm_message_id | string | VQ-CRM-[YYYYMMDD]-[SEQ] |
| customer_id | string | FK to CRM |
| channel | enum | zalo / sms / email |
| trigger | enum | post_order / win_back / birthday / loyalty / campaign |
| message_vi | string | Message content |
| status | enum | draft / approved / queued / sent / failed |
| sent_at | datetime | ISO8601 |

---

### Tab 7: Comment Replies
| Column | Type | Description |
|--------|------|-------------|
| reply_id | string | VQ-REP-[YYYYMMDD]-[SEQ] |
| comment_id | string | Platform comment ID |
| platform | enum | Platform name |
| category | enum | Comment category |
| sentiment | enum | positive / neutral / negative |
| escalation_flag | boolean | TRUE/FALSE |
| auto_post_safe | boolean | TRUE/FALSE |
| status | enum | draft / approved / posted / escalated / ignored |
| posted_at | datetime | ISO8601 |

---

### Tab 8: Approvals
| Column | Type | Description |
|--------|------|-------------|
| approval_id | string | VQ-APR-[YYYYMMDD]-[SEQ] |
| object_type | enum | Object type |
| object_id | string | Object being approved |
| status | enum | pending / approved / rejected / edited / timeout |
| reviewer_notes | string | Notes |
| created_at | datetime | ISO8601 |
| responded_at | datetime | ISO8601 |

---

### Tab 9: Execution Log
| Column | Type | Description |
|--------|------|-------------|
| log_id | string | VQ-LOG-[YYYYMMDD]-[SEQ] |
| workflow_id | string | n8n workflow ID |
| step | string | Step name |
| status | enum | success / failed / skipped |
| duration_ms | integer | Execution time |
| message | string | Log message |
| timestamp | datetime | ISO8601 |

---

### Tab 10: Error Log
| Column | Type | Description |
|--------|------|-------------|
| error_id | string | VQ-ERR-[YYYYMMDD]-[SEQ] |
| workflow_id | string | n8n workflow ID |
| error_code | string | Error code |
| error_message | string | Full error |
| severity | enum | low / medium / high / critical |
| status | enum | open / in_review / resolved / ignored |
| occurred_at | datetime | ISO8601 |

---

### Tab 11: Daily Summaries
| Column | Type | Description |
|--------|------|-------------|
| date | date | YYYY-MM-DD |
| content_packs_generated | integer | Count |
| posts_approved | integer | Count |
| posts_scheduled | integer | Count |
| crm_messages_sent | integer | Count |
| comments_replied | integer | Count |
| errors_count | integer | Count |
| summary_text | string | Full summary |
