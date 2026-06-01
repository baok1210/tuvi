from .config import DIA_CHI, TEN_12_CUNG


def tinh_dai_han(cung_menh_pos, cuc_so, gioi_tinh, nam_can_index):
    am_duong = "Dương" if nam_can_index % 2 == 0 else "Âm"
    if (am_duong == "Dương" and gioi_tinh == "Nam") or (am_duong == "Âm" and gioi_tinh == "Nữ"):
        direction = 1
    else:
        direction = -1

    dai_han = []
    start_age = cuc_so
    for i in range(12):
        cung_pos = (cung_menh_pos + i * direction) % 12
        age_start = start_age + i * 10
        age_end = age_start + 9
        dai_han.append({
            "cung": TEN_12_CUNG[i],
            "dia_chi": DIA_CHI[cung_pos],
            "tuoi": f"{age_start}-{age_end}",
            "start_age": age_start,
            "end_age": age_end,
        })
    return dai_han


def tinh_tieu_han(nam_hien_tai, nam_sinh_chi_index):
    offset = nam_hien_tai - (2024 - (nam_sinh_chi_index - 3) % 60)
    current_chi = (nam_sinh_chi_index + offset) % 12
    khoi_tieu_han_map = {
        0: 3, 1: 3, 2: 6, 3: 6, 4: 6,
        5: 9, 6: 9, 7: 9, 8: 0, 9: 0, 10: 0, 11: 3
    }
    start = khoi_tieu_han_map.get(current_chi, 3)
    tieu_han_pos = (start + (nam_hien_tai % 12)) % 12
    return DIA_CHI[tieu_han_pos]


def tinh_luu_niên(nam_hien_tai, cung_menh_pos, gioi_tinh, nam_can_index):
    am_duong = "Dương" if nam_can_index % 2 == 0 else "Âm"
    if (am_duong == "Dương" and gioi_tinh == "Nam") or (am_duong == "Âm" and gioi_tinh == "Nữ"):
        direction = 1
    else:
        direction = -1
    offset = nam_hien_tai - 2024
    cung_pos = (cung_menh_pos + offset * direction) % 12
    return DIA_CHI[cung_pos]
