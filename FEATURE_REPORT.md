# Hệ Thống Tử Vi Đẩu Số — Báo Cáo Tính Năng Chi Tiết

---

## 1. Kiến Trúc Tổng Thể

```
H:\Tử vi\
├── tuvi_engine/          # Core engine (thuật toán)
├── knowledge/            # Knowledge base (RAG)
│   ├── classical/        # Cổ thư (Cốt Tủy Phú, Thái Vi Phú, Nữ Mệnh Phú)
│   └── Bac Phai          # Kiến thức Bắc Phái
├── tests/                # Benchmark (MingLi-Bench 160 câu)
├── prompts/              # Prompt templates
└── external/             # Reference repos (3 cloned)
    ├── ziwei-lzm0x219/   # Bắc Phái TypeScript (monorepo, 4 packages)
    ├── ziwei-doushu/     # Ni Haixia + patterns (1118 lines) + 518k samples
    └── ziwei-ruijayfeng/ # ZiweiKnows (knowledge-db, LLM interpretation)
```

---

## 2. Core Engine (`tuvi_engine/`)

### 2.1 `chart.py` — Lá Số Tử Vi

**Class**: `LaSoTuVi(nam, thang, ngay, gio, gioi_tinh)`

**Quy trình**: solar → lunar → can chi → cung Mệnh → cung Thân → ngũ hành cục → an Tử Vi → an tất cả sao → Tứ Hóa → đặc tính sao → to_dict()

**Output**: dict với:
- `thong_tin_co_ban`: duong_lich, am_lich, gioi_tinh, nam_can, nam_chi, nam_can_chi, gio_can_chi
- `menh_ban`: cung_menh, cung_than, cuc, hanh
- `tu_hoa`: {Lộc, Quyền, Khoa, Kỵ}
- `thap_nhi_cung`: 12 palaces, mỗi palace có ten, dia_chi, so_thu_tu, can_cung, chinh_tinh, phu_tinh, sat_tinh, dac_tinh
- `dai_han`: đại vận

### 2.2 `palaces.py` — Cung Vị Cơ Bản

- `tinh_cung_menh(thang_sinh, gio_sinh_index)`: công thức (13 + tháng - giờ) % 12
- `tinh_cung_than(thang_sinh, gio_sinh_index)`: công thức (1 + tháng + giờ) % 12
- `lap_dia_ban(cung_menh)`: tạo 12 cung với địa chi tương ứng

### 2.3 `stars.py` — An Sao

**Sao chính tinh (14)**: Tử Vi, Thiên Cơ, Thái Dương, Vũ Khúc, Thiên Đồng, Liêm Trinh, Thiên Phủ, Thái Âm, Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân

**Sao phụ (32+)**: Lộc Tồn, Kình Dương, Đà La, Thiên Mã, Tả Phụ, Hữu Bật, Văn Xương, Văn Khúc, Thiên Khôi, Thiên Việt, Hỏa Tinh, Linh Tinh, Địa Không, Địa Kiếp, Thái Tuế, Thiên Không, Hồng Loan, Thiên Hỷ, Đào Hoa, Cô Thần, Quả Tú, Thiên Hình, Thiên Riêu, Long Trì, Phượng Các, Ân Quang, Thiên Quý, Tam Thai, Bát Tọa, Thiên Giải, Địa Giải, Thiên Thương, Thiên Sứ, Lưu Hà, Tuần, Triệt, Kiếp Sát, Hoa Cái, Phúc Đức + Trường Sinh 12 sao + Bác Sỹ 12 sao + Tướng Quân + Tếu Phá

### 2.4 `cuc.py` — Ngũ Hành Cục

- `tinh_cuc(nam_can_index, cung_menh_pos)`: trả về (cuc_so, cuc_ten, cuc_hanh)
- Hỗ trợ 5 cục: Thủy nhị, Mộc tam, Kim tứ, Thổ ngũ, Hỏa lục

### 2.5 `can_chi.py` — Thiên Can Địa Chi

- `nam_can_chi(nam_duong_lich)`: chuyển năm dương → Can/Chi
- `thang_can_chi(nam_can, thang_am)`: Ngũ Hổ Độn (tháng)
- `ngay_can_chi(nam, thang, ngay)`: từ 1900-01-01
- `gio_can_chi(ngay_can, gio_duong)`: giờ → Can Chi
- `tinh_can_cung(nam_can, dia_chi_index)`: **Ngũ Hổ Độn cho 12 cung** — mới thêm
- `am_duong_nam(can)`: phân biệt Âm/Dương Nam

### 2.6 `dai_han.py` — Đại Hạn

- `tinh_dai_han(cung_menh_pos, cuc_so, gioi_tinh, nam_can_index)`: 10 đại hạn, mỗi hạn span theo cục
- `tinh_luu_nien(nam_hien_tai, cung_menh_pos, gioi_tinh, nam_can_index)`: lưu niên

### 2.7 `tu_hoa.py` — Tứ Hóa

- `tinh_tu_hoa(nam_can)`: {Lộc, Quyền, Khoa, Kỵ} dựa trên can năm
- Bảng Tứ Hóa 10 can: Giáp→Quý

---

## 3. Phi Tinh Engine (`tuvi_engine/phi_tinh.py`)

### 3.1 `TU_HOA_MAP` — Bảng Tứ Hóa (10 can × 4 loại)

Mỗi can (Giáp→Quý) → {Lộc, Quyền, Khoa, Kỵ} → tên sao. Đồng bộ với chuẩn Bắc Phái.

### 3.2 `phi_tu_hoa(thien_can, cung_map)`

Tìm sao của Tứ Hóa trong 12 cung → trả về {Lộc: {sao, cung, dia_chi}, ...}

### 3.3 `phi_cung_hoa_tuong(la_so_dict)`

**Chức năng**: Phi toàn bộ 12 cung
**Output**:
- `sinh_nien_tu_hoa`: 4 hóa năm sinh
- `lai_nhan_cung`: cung tương ứng với Địa Chi năm sinh
- `phi_cung`: array [{cung_goc, thien_can, loai, sao, cung_dich, dia_chi}] — 48 items (12 cung × 4 hóa)

### 3.4 `tu_hoa_analysis(sinh_nien_tu_hoa, phi_cung_list)`

Phân tích Ngã/Tha cung:
- `loc_nga_cung`, `loc_tha_cung`
- `ky_nga_cung`, `ky_tha_cung`
- `loc_ky_dong_cung`: Lộc-Kỵ đồng cung (tự hóa)

### 3.5 `phan_tich_nga_tha(hoa_loc_cung, hoa_ky_cung)`

**Ngã cung**: Mệnh, Tài Bạch, Quan Lộc, Tật Ách, Phúc Đức, Điền Trạch
**Tha cung**: Phu Thê, Tử Tức, Thiên Di, Nô Bộc, Huynh Đệ, Phụ Mẫu

---

## 4. Cung Vị Biến Thể (`tuvi_engine/cung_vi_bien_the.py`) — **MỚI**

### 4.1 `RELATION_MAP` — 18 đối tượng phân tích

| Đối tượng | Cung gốc (subject Mệnh) | Loại |
|-----------|------------------------|------|
| Bản Thân | Mệnh | trực_tiếp |
| Phụ / Mẫu / Phụ Mẫu | Phụ mẫu | huyết_thống |
| Huynh / Đệ / Tỷ / Muội | Huynh đệ | huyết_thống |
| Phu / Thê | Phu thê | hôn_nhân |
| Trưởng Tử / Thứ Tử / Nhi / Nữ | Tử tức | huyết_thống |
| Bằng Hữu | Nô bộc | xã_giao |
| Cấp Trên | Quan lộc | chức_nghiệp |
| Đối Thủ | Thiên di | quan_hệ |
| Nội Trợ | Điền trạch | gia_đạo |

### 4.2 `thanh_lap_ban_tam_thoi(la_so_dict, doi_tuong)`

Xoay 12 cung theo Địa Chi offset. Công thức:
- `offset_dc = (subject_mệnh_dc - original_mệnh_dc + 12) % 12`
- Với mỗi cung gốc: `subject_palace_idx = (original_dc - offset_dc - menh_dc + 24) % 12`

### 4.3 `CUNG_DOI` — 6 cặp xung chiếu

Mệnh ↔ Thiên Di, Huynh Đệ ↔ Nô Bộc, Phu Thê ↔ Quan Lộc, Tử Tức ↔ Điền Trạch, Tài Bạch ↔ Phúc Đức, Tật Ách ↔ Phụ Mẫu

### 4.4 `TAM_HOP_NHOM` — 4 nhóm tam hợp

| Nhóm | Địa Chi | Ngũ Hành |
|------|---------|---------|
| 1 | Dần, Ngọ, Tuất | Hỏa |
| 2 | Thân, Tý, Thìn | Thủy |
| 3 | Tỵ, Dậu, Sửu | Kim |
| 4 | Hợi, Mão, Mùi | Mộc |

### 4.5 `TAM_PHUONG_TU_CHINH` — 12 palace × 4 direction

Dạng mã: `0→[0,4,8,6]`, `1→[1,5,9,7]`, ... (Mệnh→Mệnh+Tài+Quan+Thiên Di)

### 4.6 `ghep_chuoi_sao_tam_phuong(la_so_dict, doi_tuong, ten_cung)`

Gom tất cả sao trong tam phương tứ chính → context string

---

## 5. Thái Tuế Nhập Quái (`tuvi_engine/thai_tue_nhap_quai.py`) — **MỚI**

### 5.1 `thai_tue_nhap_quai(la_so_dict, nam_sinh_doi_tuong)`

- Lấy Địa Chi năm sinh đối tượng: `nam_chi_idx = nam_sinh % 12`
- Tìm cung tại Địa Chi đó trong lá số → làm Mệnh tạm của đối tượng
- Vẫn dùng Tứ Hóa của chủ lá số (không dùng Tứ Hóa của đối tượng)

**Ví dụ**: Chủ lá số 1990 (Canh Ngọ), phân tích người sinh 1965 (Ất Tỵ)
- 1965 % 12 = 9 → Dậu
- Cung tại Dậu = Tài bạch → Mệnh tạm
- Offset Địa Chi = 8
- Tứ Hóa: Canh (Thái Dương Lộc, Vũ Khúc Quyền, Thái Âm Khoa, Thiên Đồng Kỵ)

### 5.2 `y_niem_nhap_quai(la_so_dict, y_niem)`

- Map ý niệm → cung tiêu điểm (sự nghiệp→Quan lộc, tài chính→Tài bạch, hôn nhân→Phu thê, sức khỏe→Tật ách, etc.)
- Cung tiêu điểm làm Mệnh tạm
- Dùng Thiên Can của cung đó để phi Tứ Hóa (khác với Thái Tuế)

**20+ ý niệm hỗ trợ**: sự nghiệp, tài chính, gia đình, hôn nhân, sức khỏe, con cái, di chuyển, bạn bè, phúc đức, cha mẹ, anh em, bản thân, etc.

---

## 6. Tam Phương Tứ Chính (`tuvi_engine/tam_phuong_tu_chinh.py`) — **MỚI**

### 6.1 Vector không gian

- `khoang_cach_cung(cung_a, cung_b)`: min((a-b)%12, (b-a)%12)
- `quan_he_cung(cung_a, cung_b)`: "đồng cung" | "lân cận" | "xung chiếu" | "tam hợp" | v.v.
- `tam_phuong_tu_chinh(ten_cung)`: [Mệnh, Tài, Quan, Thiên Di]
- `tam_hop(dia_chi)`: [2 địa chi còn lại trong nhóm]
- `tam_hop_cung(ten_cung)`: [2 palace còn lại trong nhóm tam hợp]

### 6.2 Quan hệ đặc biệt

- `nhi_hop(dia_chi)`: Tý-Sửu, Dần-Hợi, Mão-Tuất, Thìn-Dậu, Tỵ-Thân, Ngọ-Mùi
- `am_hop(dia_chi)`: Tý-Dậu, Sửu-Thân, Dần-Mùi, Mão-Ngọ, Thìn-Tỵ

---

## 7. 2-Layer Pipeline (`tuvi_engine/pipeline.py`) — **MỚI**

### 7.1 `Layer1Algorithm` (Tầng Thuật Toán)

**Input**: `run(nam, thang, ngay, gio, gioi_tinh, [doi_tuong, nam_sinh_doi_tuong, y_niem])`

**4 modes**:
1. **Bản Thân**: Chart gốc + Tứ Hóa + Phi Cung + tam phương 12 cung
2. **Đối tượng cố định**: Xoay 12 cung theo RELATION_MAP + Tứ Hóa chart chủ
3. **Thái Tuế**: Nhập quái theo năm sinh đối tượng
4. **Ý Niệm**: Nhập quái theo chủ đề

**Output**: ctx dict với `{birth, menh_ban, analysis_subject, tu_hoa, lai_nhan_cung, phi_cung (48 items), all_palaces (12 rotated), tam_phuong_strings (12 cung)}`

**`format_context(ctx)`**: → string 5000+ chars, structured:
```
THÔNG TIN CƠ BẢN
  Ngày sinh: 1990-06-15 10h
  Âm lịch: 1990 năm tháng 5 ngày 23
  Năm can chi: CanhNgọ
  Mệnh: Sửu - Thân: Hợi
  Cục: Mộc tam cục
  Đối tượng PT: Phụ

TỨ HÓA NĂM SINH
  Lộc: Thái Dương tại Quan lộc (Tỵ)
  ...

PHI CUNG HÓA TƯỢNG (48 items)
  Mệnh (Kỷ) -> Lộc Vũ Khúc nhập Điền trạch
  ...

LÁ SỐ (xoay theo đối tượng)
  Phụ mẫu (Sửu): Thiên Lương(Đắc), Quả Tú, ...
  Mệnh (Dần): Thất Sát(Miếu), Ân Quang, ...
  ...

Tam phương Mệnh: ...
```

### 7.2 `Layer2RAG` (Tầng RAG + LLM)

**Input**: context string từ Layer1

**`retrieve_relevant(context_str)`**: 11 keywords → truy_xuat từ knowledge index
- Thiên Lương, Tứ Hóa, Bắc phái, cách cục, Cốt Tủy Phú, Lộc Tồn, sao phụ, tam hợp, Tử Vi, Thất Sát, cung Mệnh

**`build_prompt(context_str, retrieved)`**: → prompt 6500+ chars:
- System role (chuyên gia Tử Vi Đẩu Số)
- Chart context (format_context output)
- Retrieved knowledge (kiến thức tham khảo)
- Structured analysis instructions (7 sections)

---

## 8. Knowledge Base (`knowledge/`)

### 8.1 `retriever.py` — BM25 Search

**171 knowledge sources** (từ 84 lên 171 sau cập nhật):
- 14 sao chính, 12 cung, 32 cách cục, 19 tổ hợp sao, 12 luận giải
- 31 Bắc Phái entries, 26 Cổ Thư entries, 25 sao phụ Nghê Hải Hạ

**Search**: BM25 với stop words, phân tích token, trả về top-k theo score

### 8.2 `bac_phai_knowledge.py` — Kiến Thức Bắc Phái

12 sections:
- Giới thiệu, Tứ Hóa (4 sao × ý nghĩa), Lai Nhân Cung, Phi Cung Hóa Tượng
- Ngã/Tha cung, Tam Tài (Thiên-Địa-Nhân), Thể/Dụng
- Bảng Tứ Hóa 10 can, Sao Nam/Sao Nữ
- 15 quy tắc Bắc Phái (quy_tac_1 đến quy_tac_15)
- 6 kỹ thuật cơ bản

### 8.3 `classical/co_tuy_phu.py` — Cổ Thư

- `COT_TUY_PHU`: 15 rules (Cơ Nguyệt Đồng Lương, Sát Phá Tham, Tử Phủ đồng cung, Hóa Kỵ nhập Mệnh, etc.)
- `THAI_VI_PHU`: 12 rules
- `NU_MENH_PHU`: 12 rules (nữ mệnh)
- `CAC_SAO_PHU_NI_HAI_XIA`: 25 phụ tinh từ Nghê Hải Hạ
- `ClassicalRuleEngine.match(la_so_dict)`: pattern matching với 26 rules + điều kiện if/then

### 8.4 `star_knowledge.py` — Star Database

- `BRIGHTNESS_MAP`: 14 chính tinh × Miếu/Vượng positions (from ziwei-1.0 / Nghê Hải Hạ)
- `DIMMED_MAP`: 14 chính tinh × Hãm positions
- `tra_cuu_brightness(sao, chi_index)`: lookup function

### 8.5 `patterns.py` — Cách Cục

32 patterns: Tử Phủ đồng cung, Tử Sát đồng cung, Cơ Nguyệt Đồng Lương, Sát Phá Tham, Tham Linh Hỏa, Nhật Nguyệt Tịnh Minh, etc.

---

## 9. Benchmark (`tests/mingli_bench.py`)

- 160 câu hỏi từ MingLi-Bench (Global Fortune Teller 2022-2025)
- 12 categories: Marriage (44), Career (25), Family (22), Health (17), Personality (14), Wealth (13), Education (11), Children (6), Appearance (3), Fortune (2), Calamity (2), Legal (1)
- 32 unique case studies
- `evaluate_model(model_fn)`: accuracy scoring
- `evaluate_from_file(predictions_file)`: batch evaluation từ JSON
- `format_birth_info(q)`: extract structured birth data

---

## 10. External Repositories (`external/`)

### 10.1 `ziwei-lzm0x219/` — Bắc Phái TypeScript

**Monorepo (4 packages)**: core, react, i18n, ziwei (aggregator)

**Core structure** (22 files under `packages/core/src/`):
- `constants/index.ts`: BRANCH, STEM, STAR_HANS, PALACE_HANS, STEM_TRANSFORMATIONS, FIVE_ELEMENT_TABLE, PALACE_KEYS
- `utils/math.ts`: `wrapIndex()`, `relativeIndex()`, `oppositeIndex()`
- `rules/palace.ts`: palace calculations + Ngũ Hổ Độn
- `rules/star.ts`: star placement (Tử Vi → Thiên Phủ, 6 minor stars), `calculateStarTransformation()`
- `rules/decade.ts`: đại hạn calculation
- `services/natal.ts`: main chart assembly
- `services/star.ts`: self-transformation (离心/向心 tự hóa)

**Unique features not yet ported**:
- Star placement formula for 紫微/天府 systems (exact mathematical positions)
- 6 minor stars (左辅右弼, 文昌文曲, 天魁天钺) placement
- Runtime context and i18n (zh-Hans/zh-Hant)
- Monorepo build system with pnpm + moon

### 10.2 `ziwei-doushu/` — Ni Haixia System (22 files, 4856 lines)

**Key files**:
- `lib/ziwei/constants.ts` (144 lines): STEMS, BRANCHES, PALACE_NAMES_ORDER, SI_HUA_TABLE, TIANKUI_TABLE, LUCUN_TABLE, TIANMA_TABLE, STAR_BRIGHTNESS (6 stars), STAR_DESCRIPTIONS (14 stars)
- `lib/ziwei/sihua.ts` (198 lines): `getSiHuaByStem()`, `getDaXianSiHua()`, `getLiuNianSiHua()`, `detectSelfSihua()`, `findIncomingPalaces()`, `buildAllSelfSihua()`, `buildOverlayForStar()`
- `lib/ziwei/patterns.ts` (1118 lines): 39 pattern detectors (君臣庆会, 紫府同宫, 火贪格, 杀破狼, 机月同梁, 化忌入命迁, 羊陀夹忌, etc.)
- `lib/classics/data/gusuifu.ts` (218 lines): 9 chapters Cốt Tủy Phú
- `lib/classics/data/quanshu.ts` (146 lines): 紫微斗数全书
- `lib/classics/data/quanji.ts` (195 lines): 紫微斗数全集
- `lib/ziwei/heming-knowledge.ts` (329 lines): compatibility analysis
- `lib/nihai/`: Ni Haixia biography + tam kỳ system (thiên kỳ 548 lines, nhân kỳ 659 lines, địa kỳ 183 lines)
- `lib/ziwei/cities.ts` (511 lines): China province/city longitude database

**518,400 sample dataset**: Ni Haixia system interpretations, 5.5GB, 3 volumes

### 10.3 `ziwei-ruijayfeng/` — ZiweiKnows (Next.js + iztro)

**Knowledge DB (14 files)**:
- `knowledge-db/entries/stars.ts` (201 lines): 14 major star guidance
- `knowledge-db/entries/palaces.ts` (179 lines): 12 palace guidance
- `knowledge-db/entries/sihua.ts` (118 lines): 4 sihua guidance
- `knowledge-db/entries/sihuaPalaces.ts` (238 lines): sihua-in-palace combos
- `knowledge-db/entries/principles.ts` (192 lines): 7 interpretation principles
- `knowledge-db/entries/combos.ts` (711 lines): 25+ combo guidance
- `knowledge-db/retrieval/retrieve.ts` (149 lines): local guidance retrieval engine

**Fortune Scoring** (`fortune-score.ts`, 1393 lines):
- STAR_BASE_SCORE (紫微=18, 擎羊=-12, etc.)
- BRIGHTNESS_COEF (庙=1.5, 旺=1.3, 陷=0.5)
- SIHUA_MODIFIER (禄=+15, 权=+12, 科=+10, 忌=-18)
- Palace weights (4 dimensions: career, wealth, relationship, health)
- `calculatePeriodScore()`, `generateDecadalKLines()`, `generateYearlyKLines()`, `generateLifetimeKLines()`
- K-line formula: 0-100 scale

---

## 11. Tổng Quan Modules

| Module | Tệp | Dòng | Trạng thái |
|--------|-----|------|-----------|
| Chart | `chart.py` | 290 | Cập nhật (thêm can_cung, nam_can/chi) |
| Palace | `palaces.py` | 25 | Ổn định |
| Stars | `stars.py` | 750+ | Ổn định |
| Cục | `cuc.py` | 40 | Ổn định |
| Can Chi | `can_chi.py` | 85 | Cập nhật (thêm tinh_can_cung) |
| Đại Hạn | `dai_han.py` | 50 | Ổn định |
| Tứ Hóa | `tu_hoa.py` | 40 | Ổn định |
| Phi Tinh | `phi_tinh.py` | 153 | Ổn định |
| **Cung Vị Biến Thể** | `cung_vi_bien_the.py` | 180 | **Mới** |
| **Thái Tuế Nhập Quái** | `thai_tue_nhap_quai.py` | 107 | **Mới** |
| **Tam Phương Tứ Chính** | `tam_phuong_tu_chinh.py` | 120 | **Mới** |
| **Pipeline (2-layer)** | `pipeline.py` | 165 | **Mới** |
| Retriever | `retriever.py` | 134 | Cập nhật (thêm cổ thư, sao phụ) |
| Bắc Phái Knowledge | `bac_phai_knowledge.py` | 220 | Cập nhật |
| Cổ Thư | `co_tuy_phu.py` | 250 | Cập nhật (thêm sao phụ nihaixia) |
| Star Knowledge | `star_knowledge.py` | ~180 | Cập nhật (thêm brightness/dim tables) |
| MingLi-Bench | `mingli_bench.py` | ~100 | Cập nhật |
