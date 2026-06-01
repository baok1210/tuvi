from .config import TU_HOA, DIA_CHI, TEN_12_CUNG


def tinh_tu_hoa(nam_can):
    hoa = TU_HOA.get(nam_can, {})
    return {
        "Hóa Lộc": hoa.get("Lộc", ""),
        "Hóa Quyền": hoa.get("Quyền", ""),
        "Hóa Khoa": hoa.get("Khoa", ""),
        "Hóa Kỵ": hoa.get("Kỵ", ""),
    }


def tim_cung_chua_sao(sao, all_stars_positions):
    for cung, stars in all_stars_positions.items():
        if sao in stars:
            return cung
    return None


def gan_tu_hoa_vao_cung(tu_hoa, all_stars_positions):
    result = {}
    for loai, sao in tu_hoa.items():
        if not sao:
            continue
        cung = tim_cung_chua_sao(sao, all_stars_positions)
        if cung is not None:
            result[cung] = result.get(cung, []) + [f"{sao}({loai})"]
    return result
