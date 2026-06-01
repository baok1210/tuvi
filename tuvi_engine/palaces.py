from .config import TEN_12_CUNG, DIA_CHI


def tinh_cung_menh(thang_sinh, gio_sinh_index):
    return (13 + thang_sinh - gio_sinh_index) % 12


def tinh_cung_than(thang_sinh, gio_sinh_index):
    return (1 + thang_sinh + gio_sinh_index) % 12


def lap_dia_ban(cung_menh):
    dia_ban = {}
    for i in range(12):
        cung_pos = (cung_menh - i) % 12
        dia_ban[TEN_12_CUNG[i]] = {
            "ten": TEN_12_CUNG[i],
            "dia_chi": DIA_CHI[cung_pos],
            "so_thu_tu": cung_pos,
            "chinh_tinh": [],
            "phu_tinh": [],
            "sat_tinh": [],
            "tu_hoa": [],
        }
    return dia_ban
