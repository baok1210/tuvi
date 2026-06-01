from .config import DIA_CHI, TEN_12_CUNG
from .phi_tinh import TU_HOA_MAP, phi_tu_hoa
from .cung_vi_bien_the import (
    _chuan_hoa_ten_cung, CUNG_NAME_MAP, _build_cung_to_diachi,
    _palace_type_index, TAM_PHUONG_TU_CHINH,
)

YN_NHIEM_MAP = {
    "sự nghiệp": "Quan lộc", "công danh": "Quan lộc", "công việc": "Quan lộc",
    "tài chính": "Tài bạch", "tiền bạc": "Tài bạch", "tiền tài": "Tài bạch",
    "gia đình": "Điền trạch", "nhà cửa": "Điền trạch",
    "hôn nhân": "Phu thê", "tình cảm": "Phu thê", "tình yêu": "Phu thê", "vợ chồng": "Phu thê",
    "sức khỏe": "Tật ách", "bệnh tật": "Tật ách",
    "con cái": "Tử tức", "học hành": "Tử tức",
    "di chuyển": "Thiên di", "xuất ngoại": "Thiên di",
    "bạn bè": "Nô bộc", "quan hệ": "Nô bộc",
    "phúc đức": "Phúc đức", "tâm linh": "Phúc đức",
    "cha mẹ": "Phụ mẫu", "anh em": "Huynh đệ",
    "bản thân": "Mệnh", "tổng quan": "Mệnh", "tính cách": "Mệnh",
}


def _xoay_cung_tu_menh(thap_nhi_cung, cung_menh_tam):
    cung_to_dc = _build_cung_to_diachi(thap_nhi_cung)
    menh_dc = cung_to_dc.get("Mệnh", 0)
    tam_menh_dc = cung_to_dc.get(_chuan_hoa_ten_cung(cung_menh_tam), menh_dc)
    offset_dc = (tam_menh_dc - menh_dc + 12) % 12

    ban = {"offset_dia_chi": offset_dc, "cung_menh_tam": cung_menh_tam, "cac_cung": []}
    for c in thap_nhi_cung:
        ori_dc = c["so_thu_tu"]
        subj_dc = (ori_dc - offset_dc + 12) % 12
        palace_idx = (subj_dc - menh_dc + 12) % 12
        ten_tam = TEN_12_CUNG[palace_idx]
        ban["cac_cung"].append({
            "cung_goc": c["ten"], "cung_tam_thoi": ten_tam,
            "dia_chi": DIA_CHI[ori_dc], "dia_chi_index": ori_dc,
            "chinh_tinh": c["chinh_tinh"], "phu_tinh": c["phu_tinh"],
            "sat_tinh": c["sat_tinh"], "dac_tinh": c.get("dac_tinh", {}),
        })
    return ban


def thai_tue_nhap_quai(la_so_dict, nam_sinh_doi_tuong):
    nam_chi_idx = nam_sinh_doi_tuong % 12
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    dc_to_cung = {c["so_thu_tu"]: c for c in thap_nhi_cung}
    target = dc_to_cung.get(nam_chi_idx)
    if not target:
        return None

    cung_menh_tam = _chuan_hoa_ten_cung(target["ten"])

    sinh_nien_can = la_so_dict["thong_tin_co_ban"].get("nam_can")
    cung_map = {c["ten"]: c for c in thap_nhi_cung}
    sinh_nien_tu_hoa = {}
    if sinh_nien_can:
        sinh_nien_tu_hoa = phi_tu_hoa(sinh_nien_can, cung_map)

    ban = _xoay_cung_tu_menh(thap_nhi_cung, cung_menh_tam)

    return {
        "phuong_phap": "Thái Tuế Nhập Quái",
        "doi_tuong_nam_chi": DIA_CHI[nam_chi_idx],
        "cung_menh_tam": cung_menh_tam,
        "offset_dia_chi": ban["offset_dia_chi"],
        "su_dung_tu_hoa_cua_nam": sinh_nien_can,
        "sinh_nien_tu_hoa": sinh_nien_tu_hoa,
        "cac_cung": ban["cac_cung"],
    }


def y_niem_nhap_quai(la_so_dict, y_niem):
    y_niem = y_niem.lower().strip()
    cung_tieu_diem = YN_NHIEM_MAP.get(y_niem)
    if not cung_tieu_diem:
        return None

    cung_menh_tam = _chuan_hoa_ten_cung(cung_tieu_diem)
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    ban = _xoay_cung_tu_menh(thap_nhi_cung, cung_menh_tam)

    cung_map = {c["ten"]: c for c in thap_nhi_cung}
    cung_tieu_chuan = cung_map.get(cung_menh_tam, {})
    can_cung_tieu_diem = cung_tieu_chuan.get("can_cung", "")

    tu_hoa_tieu_diem = {}
    if can_cung_tieu_diem and can_cung_tieu_diem in TU_HOA_MAP:
        tu_hoa_tieu_diem = phi_tu_hoa(can_cung_tieu_diem, cung_map)

    return {
        "phuong_phap": "Ý Niệm Nhập Quái",
        "y_niem": y_niem,
        "cung_tieu_diem": cung_tieu_diem,
        "cung_menh_tam": cung_menh_tam,
        "offset_dia_chi": ban["offset_dia_chi"],
        "tu_hoa_theo_cung": {
            "thien_can": can_cung_tieu_diem,
            "tu_hoa": tu_hoa_tieu_diem,
        },
        "cac_cung": ban["cac_cung"],
    }


def lay_cung_nhap_quai(la_so_dict, doi_tuong_nam_sinh=None, y_niem=None):
    if doi_tuong_nam_sinh is not None:
        return thai_tue_nhap_quai(la_so_dict, doi_tuong_nam_sinh)
    elif y_niem:
        return y_niem_nhap_quai(la_so_dict, y_niem)
    return None


def ghep_chuoi_nhap_quai(la_so_dict, doi_tuong_nam_sinh=None, y_niem=None):
    ban = lay_cung_nhap_quai(la_so_dict, doi_tuong_nam_sinh, y_niem)
    if not ban:
        return ""

    parts = [f"[{ban['phuong_phap']}] Mệnh tạm: {ban['cung_menh_tam']}"]
    for c in ban["cac_cung"]:
        stars = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
        if stars:
            parts.append(f"{c['cung_tam_thoi']}({c['dia_chi']}): {', '.join(stars)}")
    return "\n".join(parts)
