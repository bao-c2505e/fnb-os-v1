# 07_TEST_FIXTURES — Test Input Data

These JSON files are used for dry runs and QA testing.
They simulate real inputs without using live customer or campaign data.

## Files

| File | Simulates | Used In |
|------|-----------|---------|
| `test_campaign_combo_trua.json` | Weekday lunch combo campaign | WF-01, WF-02, WF-03 |
| `test_comment_hoi_dia_chi.json` | Customer asking for address | WF-05 |
| `test_comment_hoi_gia.json` | Customer asking for price | WF-05 |
| `test_lead_dat_ban.json` | Customer requesting to reserve | WF-04, WF-05 |
| `test_customer_complaint.json` | Customer complaint (escalation test) | WF-05, escalation flow |

## Rules
- Test fixtures must NOT contain real customer PII
- All phone numbers use format: `+84 9XX XXX XXX` (fictional)
- All customer names are generic (Khách A, Anh Minh, etc.)
- Fixtures are read-only — do not modify for production use
- If a fixture needs updating, create a new version with `_v2` suffix
