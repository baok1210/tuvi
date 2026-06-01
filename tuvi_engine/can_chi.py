from .config import THIEN_CAN, DIA_CHI, THOI_GIAN

NGU_HANH_NAP_AM = {
    ("Giáp", "Tý"): "Hải Trung Kim", ("Ất", "Sửu"): "Hải Trung Kim",
    ("Bính", "Dần"): "Lô Trung Hỏa", ("Đinh", "Mão"): "Lô Trung Hỏa",
    ("Mậu", "Thìn"): "Đại Lâm Mộc", ("Kỷ", "Tỵ"): "Đại Lâm Mộc",
    ("Canh", "Ngọ"): "Lộ Bàng Thổ", ("Tân", "Mùi"): "Lộ Bàng Thổ",
    ("Nhâm", "Thân"): "Kiếm Phong Kim", ("Quý", "Dậu"): "Kiếm Phong Kim",
    ("Giáp", "Tuất"): "Sơn Đầu Hỏa", ("Ất", "Hợi"): "Sơn Đầu Hỏa",
    ("Bính", "Tý"): "Giản Hạ Thủy", ("Đinh", "Sửu"): "Giản Hạ Thủy",
    ("Mậu", "Dần"): "Thành Đầu Thổ", ("Kỷ", "Mão"): "Thành Đầu Thổ",
    ("Canh", "Thìn"): "Bạch Lạp Kim", ("Tân", "Tỵ"): "Bạch Lạp Kim",
    ("Nhâm", "Ngọ"): "Dương Liễu Mộc", ("Quý", "Mùi"): "Dương Liễu Mộc",
    ("Giáp", "Thân"): "Tuyền Trung Thủy", ("Ất", "Dậu"): "Tuyền Trung Thủy",
    ("Bính", "Tuất"): "Ốc Thượng Thổ", ("Đinh", "Hợi"): "Ốc Thượng Thổ",
    ("Mậu", "Tý"): "Tích Lịch Hỏa", ("Kỷ", "Sửu"): "Tích Lịch Hỏa",
    ("Canh", "Dần"): "Tùng Bách Mộc", ("Tân", "Mão"): "Tùng Bách Mộc",
    ("Nhâm", "Thìn"): "Trường Lưu Thủy", ("Quý", "Tỵ"): "Trường Lưu Thủy",
    ("Giáp", "Ngọ"): "Sa Trung Kim", ("Ất", "Mùi"): "Sa Trung Kim",
    ("Bính", "Thân"): "Sơn Hạ Hỏa", ("Đinh", "Dậu"): "Sơn Hạ Hỏa",
    ("Mậu", "Tuất"): "Bình Địa Mộc", ("Kỷ", "Hợi"): "Bình Địa Mộc",
    ("Canh", "Tý"): "Bích Thượng Thổ", ("Tân", "Sửu"): "Bích Thượng Thổ",
    ("Nhâm", "Dần"): "Kim Bạch Kim", ("Quý", "Mão"): "Kim Bạch Kim",
    ("Giáp", "Thìn"): "Phú Đăng Hỏa", ("Ất", "Tỵ"): "Phú Đăng Hỏa",
    ("Bính", "Ngọ"): "Thiên Hà Thủy", ("Đinh", "Mùi"): "Thiên Hà Thủy",
    ("Mậu", "Thân"): "Đại Dịch Thổ", ("Kỷ", "Dậu"): "Đại Dịch Thổ",
    ("Canh", "Tuất"): "Thoa Xuyến Kim", ("Tân", "Hợi"): "Thoa Xuyến Kim",
    ("Nhâm", "Tý"): "Tang Đố Mộc", ("Quý", "Sửu"): "Tang Đố Mộc",
    ("Giáp", "Dần"): "Đại Khê Thủy", ("Ất", "Mão"): "Đại Khê Thủy",
    ("Bính", "Thìn"): "Sa Trung Thổ", ("Đinh", "Tỵ"): "Sa Trung Thổ",
    ("Mậu", "Ngọ"): "Thiên Thượng Hỏa", ("Kỷ", "Mùi"): "Thiên Thượng Hỏa",
    ("Canh", "Thân"): "Thạch Lựu Mộc", ("Tân", "Dậu"): "Thạch Lựu Mộc",
    ("Nhâm", "Tuất"): "Đại Hải Thủy", ("Quý", "Hợi"): "Đại Hải Thủy",
}


def nam_can_chi(nam_duong_lich):
    offset = nam_duong_lich - 4
    can = THIEN_CAN[offset % 10]
    chi = DIA_CHI[offset % 12]
    return can, chi


def thang_can_chi(nam_can, thang_am):
    thang_can_map = {
        "Giáp": "Bính", "Kỷ": "Bính",
        "Ất": "Mậu", "Canh": "Mậu",
        "Bính": "Canh", "Tân": "Canh",
        "Đinh": "Nhâm", "Nhâm": "Nhâm",
        "Mậu": "Giáp", "Quý": "Giáp",
    }
    offset = (DIA_CHI.index(thang_can_map[nam_can]) + (thang_am - 1) * 2) % 10
    can_thang = THIEN_CAN[offset]
    chi_thang = DIA_CHI[(thang_am + 1) % 12]
    return can_thang, chi_thang


def ngay_can_chi(nam, thang, ngay):
    base = date(1900, 1, 1)
    target = date(nam, thang, ngay)
    offset = (target - base).days
    can = THIEN_CAN[(offset + 9) % 10]
    chi = DIA_CHI[(offset + 0) % 12]
    return can, chi


def gio_can_chi(ngay_can, gio_duong):
    gio_map = {0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4,
               9: 5, 10: 5, 11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8,
               17: 9, 18: 9, 19: 10, 20: 10, 21: 11, 22: 11, 23: 0}
    chi_idx = gio_map.get(gio_duong, 0)
    gio_can_map = {c: i for i, c in enumerate(THIEN_CAN)}
    can_idx = (gio_can_map[ngay_can] % 5 * 2 + chi_idx) % 10
    return THIEN_CAN[can_idx], DIA_CHI[chi_idx]


def am_duong_nam(can):
    idx = THIEN_CAN.index(can)
    return "Dương" if idx % 2 == 0 else "Âm"


NGU_HO_DON = {
    "Giáp": "Bính", "Kỷ": "Bính",
    "Ất": "Mậu", "Canh": "Mậu",
    "Bính": "Canh", "Tân": "Canh",
    "Đinh": "Nhâm", "Nhâm": "Nhâm",
    "Mậu": "Giáp", "Quý": "Giáp",
}


def tinh_can_cung(nam_can, dia_chi_index):
    can_dan = NGU_HO_DON[nam_can]
    can_dan_idx = THIEN_CAN.index(can_dan)
    offset = (dia_chi_index - 2) % 12
    can_idx = (can_dan_idx + offset) % 10
    return THIEN_CAN[can_idx]
