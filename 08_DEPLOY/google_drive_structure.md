# Google Drive Structure — FnB OS V1

## Root Folder
`Vị Cuốn — FnB OS V1`
- Folder ID stored in `.env` as `GOOGLE_DRIVE_FOLDER_ID`

---

## Folder Structure

```
Vị Cuốn — FnB OS V1/
├── Brand Kit/
│   ├── Logos/
│   │   ├── logo_primary.png
│   │   ├── logo_white.png
│   │   └── logo_dark.png
│   ├── Fonts/
│   ├── Colors/
│   └── Brand Guidelines.pdf
│
├── Content Packs/
│   ├── 2026-06/
│   │   ├── VQ-CP-20260601-001.json
│   │   └── ...
│   └── [YYYY-MM]/
│
├── Design Briefs/
│   ├── 2026-06/
│   │   ├── VQ-DB-20260601-001.json
│   │   └── ...
│   └── [YYYY-MM]/
│
├── Ads Packs/
│   ├── 2026-06/
│   │   ├── VQ-ADS-20260601-001.json
│   │   └── ...
│   └── [YYYY-MM]/
│
├── Published/
│   ├── 2026-06/
│   │   ├── Facebook/
│   │   ├── TikTok/
│   │   └── Instagram/
│   └── [YYYY-MM]/
│
├── Photography/
│   ├── Menu Items/
│   ├── Behind the Scenes/
│   └── Events/
│
└── Archive/
    └── [older content by year]
```

---

## Folder IDs (fill after creation)

| Folder | Env Variable | ID |
|--------|-------------|-----|
| Root | `GOOGLE_DRIVE_FOLDER_ID` | [FILL after creation] |
| Content Packs | `GOOGLE_DRIVE_CONTENT_PACKS_FOLDER_ID` | [FILL] |
| Design Briefs | `GOOGLE_DRIVE_DESIGN_BRIEFS_FOLDER_ID` | [FILL] |
| Ads Packs | `GOOGLE_DRIVE_ADS_PACKS_FOLDER_ID` | [FILL] |

---

## Access Control
- Service account has Editor access to root folder (inherited)
- Human staff have Commenter or Viewer access (set manually)
- No public sharing enabled
