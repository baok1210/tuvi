from .config import THIEN_CAN, DIA_CHI
from .stars import LOC_TON_POS, THIEN_MA_POS

LUU_VAN_XUONG_TABLE = {
    "Giáp": 5, "Ất": 6, "Bính": 8, "Đinh": 9, "Mậu": 8,
    "Kỷ": 9, "Canh": 11, "Tân": 0, "Nhâm": 2, "Quý": 3,
}

LUU_VAN_KHUC_TABLE = {
    "Giáp": 9, "Ất": 8, "Bính": 6, "Đinh": 5, "Mậu": 6,
    "Kỷ": 5, "Canh": 3, "Tân": 2, "Nhâm": 0, "Quý": 11,
}

HOI_HONG_LOAN = {
    0: 10, 1: 9, 2: 0, 3: 11, 4: 2, 5: 1,
    6: 4, 7: 3, 8: 6, 9: 5, 10: 8, 11: 7,
}


def tinh_luu_nien(nam_can, nam_chi):
    can_idx = THIEN_CAN.index(nam_can)
    chi_idx = DIA_CHI.index(nam_chi)

    van_xuong_pos = LUU_VAN_XUONG_TABLE.get(nam_can, 5)
    van_khuc_pos = LUU_VAN_KHUC_TABLE.get(nam_can, 9)

    thien_khoi, thien_viet = 1, 7
    khoi_viet_table = {
        "Giáp": (1, 7), "Ất": (0, 8), "Bính": (10, 6), "Đinh": (9, 5),
        "Mậu": (7, 1), "Kỷ": (8, 0), "Canh": (6, 10), "Tân": (5, 9),
        "Nhâm": (3, 7), "Quý": (4, 8),
    }
    thien_khoi, thien_viet = khoi_viet_table.get(nam_can, (1, 7))

    loc_ton_pos = LOC_TON_POS.get(nam_can, 6)
    kinh_duong_pos = (loc_ton_pos + 1) % 12
    da_la_pos = (loc_ton_pos - 1) % 12

    thien_ma_pos = THIEN_MA_POS.get(nam_chi, 2)

    hong_loan_pos = HOI_HONG_LOAN.get(chi_idx, 10)
    thien_hy_pos = (hong_loan_pos + 6) % 12

    thai_tue_pos = chi_idx

    flow_stars = [
        ("Văn Xương", van_xuong_pos),
        ("Văn Khúc", van_khuc_pos),
        ("Thiên Khôi", thien_khoi),
        ("Thiên Việt", thien_viet),
        ("Lộc Tồn", loc_ton_pos),
        ("Kình Dương", kinh_duong_pos),
        ("Đà La", da_la_pos),
        ("Thiên Mã", thien_ma_pos),
        ("Hồng Loan", hong_loan_pos),
        ("Thiên Hỷ", thien_hy_pos),
        ("Thái Tuế", thai_tue_pos),
    ]

    return flow_stars


def tinh_luu_nien_cho_laso(la_so_dict, nam_xem):
    from .can_chi import nam_can_chi
    nam_can, nam_chi = nam_can_chi(nam_xem)
    flow_stars = tinh_luu_nien(nam_can, nam_chi)

    result = []
    for cung in la_so_dict["thap_nhi_cung"]:
        pos = cung["so_thu_tu"]
        sao_trong_cung = [ten for ten, p in flow_stars if p == pos]
        if sao_trong_cung:
            result.append({
                "cung": cung["ten"],
                "dia_chi": cung["dia_chi"],
                "sao_luu": sao_trong_cung,
            })

    return {
        "nam_xem": nam_xem,
        "nam_can_chi": f"{nam_can}{nam_chi}",
        "sao_luu_nien": {
            ten: DIA_CHI[vi_tri] for ten, vi_tri in flow_stars
        },
        "cac_cung_co_sao": result,
    }
