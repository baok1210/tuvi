from .config import (
    DIA_CHI, THIEN_CAN, TUAN_KHONG, TRIET_KHONG,
    VONG_TRANG_SINH, BAC_SY_12_THAN, TUONG_QUAN_12_THAN, TUE_PHA_12_THAN,
    TRANG_SINH_KHOI_DAU, TUONG_QUAN_KHOI_DAU,
)

ZIWEI_POS_TABLE = {
    2: [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 0, 0, 1, 1, 2, 2, 3, 3, 4],
    3: [4, 1, 2, 5, 2, 3, 6, 3, 4, 7, 4, 5, 8, 5, 6, 9, 6, 7, 10, 7, 8, 11, 8, 9, 0, 9, 10, 1, 10, 11],
    4: [11, 4, 1, 2, 0, 5, 2, 3, 1, 6, 3, 4, 2, 7, 4, 5, 3, 8, 5, 6, 4, 9, 6, 7, 5, 10, 7, 8, 6, 11],
    5: [6, 11, 4, 1, 2, 7, 0, 5, 2, 3, 8, 1, 6, 3, 4, 9, 2, 7, 4, 5, 10, 3, 8, 5, 6, 11, 4, 9, 6, 7],
    6: [9, 6, 11, 4, 1, 2, 10, 7, 0, 5, 2, 3, 11, 8, 1, 6, 3, 4, 0, 9, 2, 7, 4, 5, 1, 10, 3, 8, 5, 6],
}

ZIWEI_TO_TIANFU = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 11, 6: 10, 7: 9, 8: 8, 9: 7, 10: 6, 11: 5}

ZIWEI_OFFSETS = {"Tử Vi": 0, "Thiên Cơ": 11, "Thái Dương": 9, "Vũ Khúc": 8, "Thiên Đồng": 7, "Liêm Trinh": 4}
TIANFU_OFFSETS = {"Thiên Phủ": 0, "Thái Âm": 1, "Tham Lang": 2, "Cự Môn": 3, "Thiên Tướng": 4, "Thiên Lương": 5, "Thất Sát": 6, "Phá Quân": 10}

LOC_TON_POS = {"Giáp": 2, "Ất": 3, "Bính": 5, "Đinh": 6, "Mậu": 5, "Kỷ": 6, "Canh": 8, "Tân": 9, "Nhâm": 11, "Quý": 0}

THIEN_MA_POS = {"Tý": 2, "Sửu": 2, "Dần": 8, "Mão": 8, "Thìn": 8, "Tỵ": 11, "Ngọ": 11, "Mùi": 11, "Thân": 5, "Dậu": 5, "Tuất": 5, "Hợi": 2}


def an_tu_vi(ngay_sinh, cuc_so):
    if cuc_so not in [2, 3, 4, 5, 6]:
        cuc_so = 2
        
    k = (cuc_so - (ngay_sinh % cuc_so)) % cuc_so
    q = (ngay_sinh + k) // cuc_so
    
    if k % 2 == 0:
        pos = (q + k + 2) % 12
    else:
        pos = (q - k + 2) % 12
        
    return pos


def an_tu_vi_tinh_he(tu_vi_pos):
    stars = {}
    for ten, offset in ZIWEI_OFFSETS.items():
        pos = (tu_vi_pos + offset) % 12
        stars.setdefault(pos, []).append(ten)
    return stars


def an_thien_phu_tinh_he(tu_vi_pos):
    stars = {}
    thien_phu_pos = ZIWEI_TO_TIANFU[tu_vi_pos % 12]
    for ten, offset in TIANFU_OFFSETS.items():
        pos = (thien_phu_pos + offset) % 12
        stars.setdefault(pos, []).append(ten)
    return stars


def an_loc_ton(nam_can):
    pos = LOC_TON_POS.get(nam_can, 2)
    return pos


def an_kinh_duong_da_la(loc_ton_pos):
    return {"Kình Dương": (loc_ton_pos + 1) % 12, "Đà La": (loc_ton_pos - 1) % 12}


def an_thien_ma(nam_chi):
    pos = THIEN_MA_POS.get(nam_chi, 2)
    return {"Thiên Mã": pos}


def an_ta_phu_huu_bat(gio_sinh_index):
    return {"Tả Phụ": (gio_sinh_index + 4) % 12, "Hữu Bật": (10 - gio_sinh_index) % 12}


def an_van_xuong_khuc(gio_sinh_index):
    return {"Văn Xương": (10 - gio_sinh_index) % 12, "Văn Khúc": (4 + gio_sinh_index) % 12}


def an_thien_khoi_viet(nam_can):
    table = {"Giáp": (1, 7), "Ất": (0, 8), "Bính": (11, 9), "Đinh": (9, 11), "Mậu": (7, 1),
             "Kỷ": (0, 8), "Canh": (7, 1), "Tân": (6, 2), "Nhâm": (5, 3), "Quý": (3, 5)}
    khoi, viet = table.get(nam_can, (1, 7))
    return {"Thiên Khôi": khoi, "Thiên Việt": viet}


def an_hoa_linh(nam_chi_index, gio_sinh_index):
    table_h = {0: 3, 1: 4, 2: 8, 3: 9, 4: 2, 5: 3, 6: 7, 7: 8, 8: 1, 9: 2, 10: 6, 11: 7}
    table_l = {0: 9, 1: 8, 2: 5, 3: 4, 4: 1, 5: 0, 6: 9, 7: 8, 8: 5, 9: 4, 10: 1, 11: 0}
    offset_h = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}
    offset_l = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}
    hoa_base = table_h.get(nam_chi_index, 3)
    linh_base = table_l.get(nam_chi_index, 9)
    hoa_pos = (hoa_base + gio_sinh_index) % 12
    linh_pos = (linh_base + gio_sinh_index) % 12
    return {"Hỏa Tinh": hoa_pos, "Linh Tinh": linh_pos}


def an_dia_khong_kiep(gio_sinh_index):
    return {"Địa Không": (11 - gio_sinh_index) % 12, "Địa Kiếp": (gio_sinh_index + 11) % 12}


def an_thai_tue(nam_chi_index):
    return {"Thái Tuế": nam_chi_index}


def an_thien_khong(nam_can_index):
    table = {0: 9, 1: 7, 2: 9, 3: 7, 4: 9, 5: 7, 6: 9, 7: 7, 8: 9, 9: 7}
    return {"Thiên Không": table.get(nam_can_index, 9)}


def an_dao_hoa_hong_loan_thien_hy(nam_chi_index):
    dao = {0: 9, 1: 6, 2: 3, 3: 0, 4: 9, 5: 6, 6: 3, 7: 0, 8: 9, 9: 6, 10: 3, 11: 0}
    hong = {0: 10, 1: 9, 2: 0, 3: 11, 4: 2, 5: 1, 6: 4, 7: 3, 8: 6, 9: 5, 10: 8, 11: 7}
    hy = {0: 4, 1: 3, 2: 6, 3: 5, 4: 8, 5: 7, 6: 10, 7: 9, 8: 0, 9: 11, 10: 2, 11: 1}
    return {
        "Đào Hoa": dao.get(nam_chi_index, 9),
        "Hồng Loan": hong.get(nam_chi_index, 10),
        "Thiên Hỷ": hy.get(nam_chi_index, 4),
    }


def an_co_than_qua_tu(nam_chi_index):
    co = {0: 5, 1: 5, 2: 8, 3: 8, 4: 8, 5: 11, 6: 11, 7: 11, 8: 2, 9: 2, 10: 2, 11: 5}
    qua = {0: 7, 1: 7, 2: 10, 3: 10, 4: 10, 5: 1, 6: 1, 7: 1, 8: 4, 9: 4, 10: 4, 11: 7}
    return {"Cô Thần": co.get(nam_chi_index, 5), "Quả Tú": qua.get(nam_chi_index, 7)}


def an_thien_hinh(nam_chi_index):
    table = {0: 10, 1: 9, 2: 0, 3: 0, 4: 11, 5: 10, 6: 10, 7: 9, 8: 4, 9: 4, 10: 11, 11: 4}
    return {"Thiên Hình": table.get(nam_chi_index, 10)}


def an_thien_rieu(nam_chi_index):
    table = {0: 3, 1: 2, 2: 1, 3: 0, 4: 11, 5: 10, 6: 9, 7: 8, 8: 7, 9: 6, 10: 5, 11: 4}
    return {"Thiên Riêu": table.get(nam_chi_index, 3)}


def an_long_tri_phuong_cac(nam_chi_index):
    long_t = {0: 2, 1: 2, 2: 5, 3: 5, 4: 5, 5: 8, 6: 8, 7: 8, 8: 11, 9: 11, 10: 11, 11: 2}
    phuong = {0: 4, 1: 4, 2: 7, 3: 7, 4: 7, 5: 10, 6: 10, 7: 10, 8: 1, 9: 1, 10: 1, 11: 4}
    return {"Long Trì": long_t.get(nam_chi_index, 2), "Phượng Các": phuong.get(nam_chi_index, 4)}


def an_am_quang_thien_quy(nam_chi_index):
    table = {0: 1, 1: 1, 2: 10, 3: 10, 4: 5, 5: 5, 6: 2, 7: 2, 8: 5, 9: 5, 10: 10, 11: 10}
    return {"Ân Quang": table.get(nam_chi_index, 1), "Thiên Quý": table.get(nam_chi_index, 1)}


def an_tam_thai_bat_toa(nam_chi_index):
    tam = {0: 10, 1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0, 11: 11}
    bat = {0: 2, 1: 3, 2: 4, 3: 5, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 11, 10: 0, 11: 1}
    return {"Tam Thai": tam.get(nam_chi_index, 10), "Bát Tọa": bat.get(nam_chi_index, 2)}


def an_thien_giai_dia_giai(nam_chi_index):
    return {"Thiên Giải": (nam_chi_index + 4) % 12, "Địa Giải": (nam_chi_index + 6) % 12}


def an_thien_thuong_thien_su(cung_no_boc, cung_tat_ach):
    return {"Thiên Thương": cung_no_boc, "Thiên Sứ": cung_tat_ach}


def an_luu_ha(nam_chi_index):
    table = {0: 10, 1: 9, 2: 4, 3: 3, 4: 10, 5: 9, 6: 4, 7: 3, 8: 10, 9: 9, 10: 4, 11: 3}
    return {"Lưu Hà": table.get(nam_chi_index, 10)}


def an_kiep_sat(nam_chi_index):
    table = {0: 5, 1: 5, 2: 8, 3: 8, 4: 8, 5: 11, 6: 11, 7: 11, 8: 2, 9: 2, 10: 2, 11: 5}
    return {"Kiếp Sát": table.get(nam_chi_index, 5)}


def an_hoa_cai(nam_chi_index):
    table = {0: 3, 1: 3, 2: 6, 3: 6, 4: 6, 5: 9, 6: 9, 7: 9, 8: 0, 9: 0, 10: 0, 11: 3}
    return {"Hoa Cái": table.get(nam_chi_index, 3)}


def an_phuc_duc(nam_chi_index):
    table = {0: 1, 1: 1, 2: 4, 3: 4, 4: 4, 5: 7, 6: 7, 7: 7, 8: 10, 9: 10, 10: 10, 11: 1}
    return {"Phúc Đức": table.get(nam_chi_index, 1)}

def an_tuan(nam_can_index):
    pos = TUAN_KHONG.get(nam_can_index % 10, (10, 11))
    return {"Tuần": pos}

def an_triet(nam_can_index):
    pos = TRIET_KHONG.get(nam_can_index % 10, (8, 9))
    return {"Triệt": pos}

def an_vong_trang_sinh(nam_can_index, gioi_tinh, cuc_so):
    start = TRANG_SINH_KHOI_DAU.get(cuc_so, 7)
    duong_nam = (nam_can_index % 2 == 0)
    is_male = (gioi_tinh == "Nam")
    thuan = (duong_nam and is_male) or (not duong_nam and not is_male)
    result = {}
    for i, ten in enumerate(VONG_TRANG_SINH):
        if thuan:
            pos = (start + i) % 12
        else:
            pos = (start - i) % 12
        result[ten] = pos
    return result

def an_bac_sy(loc_ton_pos, nam_can_index, gioi_tinh):
    duong_nam = (nam_can_index % 2 == 0)
    is_male = (gioi_tinh == "Nam")
    thuan = (duong_nam and is_male) or (not duong_nam and not is_male)
    result = {}
    for i, ten in enumerate(BAC_SY_12_THAN):
        if thuan:
            pos = (loc_ton_pos + i) % 12
        else:
            pos = (loc_ton_pos - i) % 12
        result[ten] = pos
    return result

def an_tuong_quan(nam_chi_index):
    start = TUONG_QUAN_KHOI_DAU.get(nam_chi_index, 6)
    result = {}
    for i, ten in enumerate(TUONG_QUAN_12_THAN):
        pos = (start + i) % 12
        result[ten] = pos
    return result

def an_tue_pha(nam_chi_index):
    start = nam_chi_index
    result = {}
    for i, ten in enumerate(TUE_PHA_12_THAN):
        pos = (start + i) % 12
        result[ten] = pos
    return result
