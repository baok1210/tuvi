from .config import DIA_CHI, TEN_12_CUNG
from .cung_vi_bien_the import (
    CUNG_DOI, TAM_HOP_NHOM, TAM_PHUONG_TU_CHINH, BAC_PHAI_TU_CHINH,
    _chuan_hoa_ten_cung, _palace_type_index, _build_cung_to_diachi,
)

TAM_HOP_MAP = {}
for nhom in TAM_HOP_NHOM:
    for c in nhom["chi"]:
        TAM_HOP_MAP[c] = [x for x in nhom["chi"] if x != c]

NHI_HOP = {
    "Tý": "Sửu", "Sửu": "Tý", "Dần": "Hợi", "Mão": "Tuất",
    "Thìn": "Dậu", "Tỵ": "Thân", "Ngọ": "Mùi", "Mùi": "Ngọ",
    "Thân": "Tỵ", "Dậu": "Thìn", "Tuất": "Mão", "Hợi": "Dần",
}

AM_HOP = {
    "Tý": "Dậu", "Sửu": "Thân", "Dần": "Mùi", "Mão": "Ngọ",
    "Thìn": "Tỵ", "Tỵ": "Thìn", "Ngọ": "Mão", "Mùi": "Dần",
    "Thân": "Sửu", "Dậu": "Tý", "Tuất": "Hợi", "Hợi": "Tuất",
}


def xung_chieu(ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    return CUNG_DOI.get(ten_cung)


def tam_hop(dia_chi):
    return TAM_HOP_MAP.get(dia_chi, [])


def tam_hop_cung(ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    idx = _palace_type_index(ten_cung)
    if idx is None:
        return []
    chi_nhom = {}
    for nhom in TAM_HOP_NHOM:
        chi_nhom[nhom["hanh"]] = nhom["index"]
    for hanh, indices in chi_nhom.items():
        if idx in indices:
            return [TEN_12_CUNG[i] for i in indices if i != idx]
    return []


def tam_phuong_tu_chinh(ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    idx = _palace_type_index(ten_cung)
    if idx is None:
        return [ten_cung]
    tp_idx = TAM_PHUONG_TU_CHINH.get(idx, [idx])
    return [TEN_12_CUNG[i] for i in tp_idx]


def nhi_hop(dia_chi):
    return NHI_HOP.get(dia_chi)


def am_hop(dia_chi):
    return AM_HOP.get(dia_chi)


def lay_sao_trong_tam_phuong(la_so_dict, ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    tp = tam_phuong_tu_chinh(ten_cung)
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    cung_map = {c["ten"]: c for c in thap_nhi_cung}
    result = {}
    for ten in tp:
        c = cung_map.get(ten)
        if c:
            result[ten] = {
                "dia_chi": c["dia_chi"],
                "chinh_tinh": c["chinh_tinh"],
                "phu_tinh": c["phu_tinh"],
                "sat_tinh": c["sat_tinh"],
                "dac_tinh": c.get("dac_tinh", {}),
            }
    return result


def bac_phai_tu_chinh(ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    idx = _palace_type_index(ten_cung)
    if idx is None:
        return [ten_cung]
    bp_idx = BAC_PHAI_TU_CHINH.get(idx, [idx])
    return [TEN_12_CUNG[i] for i in bp_idx]


def cac_sao_trong_tam_phuong(la_so_dict, ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    data = lay_sao_trong_tam_phuong(la_so_dict, ten_cung)
    sao_set = set()
    for c in data.values():
        for star_list in [c["chinh_tinh"], c["phu_tinh"], c["sat_tinh"]]:
            sao_set.update(star_list)
    return sao_set


def dem_sat_trong_tam_phuong(la_so_dict, ten_cung, ds_sat=None):
    if ds_sat is None:
        ds_sat = ["Kình Dương", "Đà La", "Hỏa Tinh", "Linh Tinh", "Địa Không", "Địa Kiếp"]
    sao_set = cac_sao_trong_tam_phuong(la_so_dict, ten_cung)
    return sum(1 for s in ds_sat if s in sao_set)


def get_giap_cung(la_so_dict, ten_cung):
    ten_cung = _chuan_hoa_ten_cung(ten_cung)
    idx = _palace_type_index(ten_cung)
    if idx is None:
        return {"truoc": None, "sau": None}
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    cung_map = {c["so_thu_tu"]: c["ten"] for c in thap_nhi_cung}
    return {
        "truoc": cung_map.get((idx - 1) % 12),
        "sau": cung_map.get((idx + 1) % 12),
    }


def ghep_chuoi_tam_phuong(la_so_dict, ten_cung):
    data = lay_sao_trong_tam_phuong(la_so_dict, ten_cung)
    parts = []
    for ten, c in data.items():
        stars = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
        if stars:
            parts.append(f"{ten}({c['dia_chi']}): {', '.join(stars)}")
    return "; ".join(parts)


def khoang_cach_cung(cung_a, cung_b):
    a = _palace_type_index(_chuan_hoa_ten_cung(cung_a))
    b = _palace_type_index(_chuan_hoa_ten_cung(cung_b))
    if a is None or b is None:
        return None
    return min((a - b) % 12, (b - a) % 12)


def quan_he_cung(cung_a, cung_b):
    dc = khoang_cach_cung(cung_a, cung_b)
    if dc is None:
        return "không xác định"
    if dc == 0:
        return "đồng cung"
    if dc == 1 or dc == 11:
        return "lân cận (cách 1 cung)"
    if dc == 6:
        return "xung chiếu (đối cung)"
    if dc == 4 or dc == 8:
        return "tam hợp"
    if dc == 2 or dc == 10:
        return "cách 2 cung (tam hợp xa)"
    if dc == 3 or dc == 9:
        return "cách 3 cung"
    if dc == 5 or dc == 7:
        return "cách 5 cung"
    return f"cách {dc} cung"
