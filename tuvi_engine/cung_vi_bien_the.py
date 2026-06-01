from .config import TEN_12_CUNG, DIA_CHI


def _chuan_hoa_ten_cung(ten):
    if ten in CUNG_NAME_MAP:
        return CUNG_NAME_MAP[ten]
    return ten


CUNG_NAME_MAP = {
    "Mệnh": "Mệnh", "Menh": "Mệnh",
    "Huynh Đệ": "Huynh đệ", "Huynh đệ": "Huynh đệ", "Huynh": "Huynh đệ",
    "Phu Thê": "Phu thê", "Phu thê": "Phu thê",
    "Tử Tức": "Tử tức", "Tử tức": "Tử tức",
    "Tài Bạch": "Tài bạch", "Tài bạch": "Tài bạch",
    "Tật Ách": "Tật ách", "Tật ách": "Tật ách",
    "Thiên Di": "Thiên di", "Thiên di": "Thiên di",
    "Nô Bộc": "Nô bộc", "Nô bộc": "Nô bộc",
    "Quan Lộc": "Quan lộc", "Quan lộc": "Quan lộc",
    "Điền Trạch": "Điền trạch", "Điền trạch": "Điền trạch",
    "Phúc Đức": "Phúc đức", "Phúc đức": "Phúc đức",
    "Phụ Mẫu": "Phụ mẫu", "Phụ mẫu": "Phụ mẫu",
}

RELATION_MAP = {
    "Bản Thân": {"cung_goc": "Mệnh", "loai": "trực_tiếp"},
    "Phụ":     {"cung_goc": "Phụ mẫu", "loai": "huyết_thống"},
    "Mẫu":     {"cung_goc": "Phụ mẫu", "loai": "huyết_thống"},
    "Phụ Mẫu": {"cung_goc": "Phụ mẫu", "loai": "huyết_thống"},
    "Huynh":   {"cung_goc": "Huynh đệ", "loai": "huyết_thống"},
    "Đệ":      {"cung_goc": "Huynh đệ", "loai": "huyết_thống"},
    "Tỷ":      {"cung_goc": "Huynh đệ", "loai": "huyết_thống"},
    "Muội":    {"cung_goc": "Huynh đệ", "loai": "huyết_thống"},
    "Phu":     {"cung_goc": "Phu thê", "loai": "hôn_nhân"},
    "Thê":     {"cung_goc": "Phu thê", "loai": "hôn_nhân"},
    "Trưởng Tử": {"cung_goc": "Tử tức", "loai": "huyết_thống"},
    "Thứ Tử":  {"cung_goc": "Tử tức", "loai": "huyết_thống"},
    "Nhi":     {"cung_goc": "Tử tức", "loai": "huyết_thống"},
    "Nữ":      {"cung_goc": "Tử tức", "loai": "huyết_thống"},
    "Bằng Hữu": {"cung_goc": "Nô bộc", "loai": "xã_giao"},
    "Cấp Trên": {"cung_goc": "Quan lộc", "loai": "chức_nghiệp"},
    "Đối Thủ":  {"cung_goc": "Thiên di", "loai": "quan_hệ"},
    "Nội Trợ":  {"cung_goc": "Điền trạch", "loai": "gia_đạo"},
}

CUNG_DOI = {
    "Mệnh": "Thiên di", "Huynh đệ": "Nô bộc", "Phu thê": "Quan lộc",
    "Tử tức": "Điền trạch", "Tài bạch": "Phúc đức", "Tật ách": "Phụ mẫu",
    "Thiên di": "Mệnh", "Nô bộc": "Huynh đệ", "Quan lộc": "Phu thê",
    "Điền trạch": "Tử tức", "Phúc đức": "Tài bạch", "Phụ mẫu": "Tật ách",
}

TAM_HOP_NHOM = [
    {"chi": ["Dần", "Ngọ", "Tuất"], "index": [2, 6, 10], "hanh": "Hỏa"},
    {"chi": ["Thân", "Tý", "Thìn"], "index": [8, 0, 4], "hanh": "Thủy"},
    {"chi": ["Tỵ", "Dậu", "Sửu"], "index": [5, 9, 1], "hanh": "Kim"},
    {"chi": ["Hợi", "Mão", "Mùi"], "index": [11, 3, 7], "hanh": "Mộc"},
]

TAM_PHUONG_TU_CHINH = {
    c: [(c + i) % 12 for i in [0, 4, 8, 6]]
    for c in range(12)
}
# Nam Phái / Tam Hợp Phái: Tứ Chính = Mệnh + Tài + Quan + Thiên Di
#   — dùng tam hợp địa chi (cách 4), thêm đối cung để xem tương tác tĩnh
# Bắc Phái / Tứ Hóa Phái: Tứ Chính = Mệnh + Tử + Di + Điền
#   — dùng "cung vị tứ tượng" (Thái Cực + Thiếu Dương + Thiếu Âm + Lão Âm)
#   — mục đích: lấy can 6 cung (Mệnh+Tài+Quan + Tử+Di+Điền) phi hóa luận đoán
#   — 6 cung này = "lục dương cung", đại biểu cho sự chủ động, biến động
BAC_PHAI_TU_CHINH = {
    c: [c, (c + 3) % 12, (c + 6) % 12, (c + 9) % 12]
    for c in range(12)
}
# Bắc Phái Tứ Chính luôn cách nhau 3 cung (90°) thay vì 4 cung (120°)
# tạo thành hình chữ thập: Mệnh ↔ Tử (cách 3) ↔ Di (cách 6) ↔ Điền (cách 9)


def _build_diachi_to_cung(thap_nhi_cung):
    return {c["so_thu_tu"]: c for c in thap_nhi_cung}


def _build_cung_to_diachi(thap_nhi_cung):
    return {c["ten"]: c["so_thu_tu"] for c in thap_nhi_cung}


def _palace_type_index(ten_cung):
    try:
        return TEN_12_CUNG.index(ten_cung)
    except ValueError:
        return None


def thanh_lap_ban_tam_thoi(la_so_dict, doi_tuong):
    if doi_tuong not in RELATION_MAP:
        return None

    info = RELATION_MAP[doi_tuong]
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    cung_to_dc = _build_cung_to_diachi(thap_nhi_cung)

    if doi_tuong == "Bản Thân":
        offset_dc = 0
    else:
        cung_goc = info["cung_goc"]
        menh_dc = cung_to_dc.get("Mệnh", 0)
        subject_menh_dc = cung_to_dc.get(cung_goc, 0)
        offset_dc = (subject_menh_dc - menh_dc + 12) % 12

    ban_tam_thoi = {
        "doi_tuong": doi_tuong,
        "cung_goc_menh": info["cung_goc"],
        "offset_dia_chi": offset_dc,
        "loai": info["loai"],
        "cac_cung": [],
    }

    for c in thap_nhi_cung:
        ori_dc = c["so_thu_tu"]
        subject_dc = (ori_dc - offset_dc + 12) % 12
        subject_palace_idx = (subject_dc - cung_to_dc.get("Mệnh", 0) + 12) % 12
        ten_tam = TEN_12_CUNG[subject_palace_idx]

        ban_tam_thoi["cac_cung"].append({
            "cung_goc": c["ten"],
            "cung_tam_thoi": ten_tam,
            "dia_chi": DIA_CHI[ori_dc],
            "dia_chi_index": ori_dc,
            "chinh_tinh": c["chinh_tinh"],
            "phu_tinh": c["phu_tinh"],
            "sat_tinh": c["sat_tinh"],
            "dac_tinh": c.get("dac_tinh", {}),
        })

    return ban_tam_thoi


def lay_cung_theo_doi_tuong(la_so_dict, doi_tuong, ten_cung_can_tim):
    ban = thanh_lap_ban_tam_thoi(la_so_dict, doi_tuong)
    if not ban:
        return None
    ten_cung_can_tim = _chuan_hoa_ten_cung(ten_cung_can_tim)
    for c in ban["cac_cung"]:
        if c["cung_tam_thoi"] == ten_cung_can_tim:
            return c
    return None


def lay_tam_phuong_tu_chinh(la_so_dict, doi_tuong, ten_cung):
    ban = thanh_lap_ban_tam_thoi(la_so_dict, doi_tuong)
    if not ban:
        return []

    cung_map = {c["cung_tam_thoi"]: c for c in ban["cac_cung"]}
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    cung_idx = _palace_type_index(ten_cung)
    if cung_idx is None:
        return []

    tam_phuong_idx = TAM_PHUONG_TU_CHINH.get(cung_idx, [cung_idx])
    result = []
    for idx in tam_phuong_idx:
        ten = TEN_12_CUNG[idx]
        if ten in cung_map:
            result.append(cung_map[ten])
    return result


def ghep_chuoi_sao_tam_phuong(la_so_dict, doi_tuong, ten_cung):
    cac_cung = lay_tam_phuong_tu_chinh(la_so_dict, doi_tuong, ten_cung)
    if not cac_cung:
        return ""

    parts = []
    for c in cac_cung:
        stars = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
        dc = c.get("dac_tinh", {})
        info_parts = []
        for s in stars:
            base = s.split("(")[0]
            b = dc.get(s, "")
            info_parts.append(f"{s}" + (f"({b})" if b else ""))
        parts.append(f"{c['cung_tam_thoi']}({c['dia_chi']}): {', '.join(info_parts)}")

    return "; ".join(parts)


def lay_cung_doi(cung_ten):
    return CUNG_DOI.get(cung_ten)


def lay_tam_hop_nhom(dia_chi):
    for i, nhom in enumerate(TAM_HOP_NHOM):
        if dia_chi in nhom["chi"]:
            return nhom
    return None


def lay_tam_hop_nhom_theo_index(dc_index):
    for nhom in TAM_HOP_NHOM:
        if dc_index in nhom["index"]:
            return nhom
    return None
