THIEN_CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

DIA_CHI_INDEX = {c: i for i, c in enumerate(DIA_CHI)}

TEN_12_CUNG = [
    "Mệnh", "Huynh đệ", "Phu thê", "Tử tức",
    "Tài bạch", "Tật ách", "Thiên di", "Nô bộc",
    "Quan lộc", "Điền trạch", "Phúc đức", "Phụ mẫu"
]

TEN_12_CUNG_VIET = [
    "Mệnh", "Huynh Đệ", "Phu Thê", "Tử Tức",
    "Tài Bạch", "Tật Ách", "Thiên Di", "Nô Bộc",
    "Quan Lộc", "Điền Trạch", "Phúc Đức", "Phụ Mẫu"
]

NGU_HANH = {2: "Thủy nhị cục", 3: "Mộc tam cục", 4: "Kim tứ cục", 5: "Thổ ngũ cục", 6: "Hỏa lục cục"}
NGU_HANH_NAME = {2: "Thủy", 3: "Mộc", 4: "Kim", 5: "Thổ", 6: "Hỏa"}

THOI_GIAN = {23: 0, 0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4,
             9: 5, 10: 5, 11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8,
             17: 9, 18: 9, 19: 10, 20: 10, 21: 11, 22: 11}

CHINH_TINH = [
    "Tử Vi", "Thiên Cơ", "Thái Dương", "Vũ Khúc", "Thiên Đồng", "Liêm Trinh",
    "Thiên Phủ", "Thái Âm", "Tham Lang", "Cự Môn", "Thiên Tướng", "Thiên Lương",
    "Thất Sát", "Phá Quân"
]

CHINH_TINH_INFO = {
    "Tử Vi": {"ngu_hanh": "Thổ", "am_duong": "Dương", "tinh_he": "Bắc Đẩu", "dac_tinh": "Đế tinh"},
    "Thiên Cơ": {"ngu_hanh": "Mộc", "am_duong": "Âm", "tinh_he": "Nam Đẩu", "dac_tinh": "Mưu tinh"},
    "Thái Dương": {"ngu_hanh": "Hỏa", "am_duong": "Dương", "tinh_he": "Trung Thiên", "dac_tinh": "Quan tinh"},
    "Vũ Khúc": {"ngu_hanh": "Kim", "am_duong": "Âm", "tinh_he": "Bắc Đẩu", "dac_tinh": "Tài tinh"},
    "Thiên Đồng": {"ngu_hanh": "Thủy", "am_duong": "Dương", "tinh_he": "Bắc Đẩu", "dac_tinh": "Phúc tinh"},
    "Liêm Trinh": {"ngu_hanh": "Hỏa", "am_duong": "Âm", "tinh_he": "Bắc Đẩu", "dac_tinh": "Ác tinh"},
    "Thiên Phủ": {"ngu_hanh": "Thổ", "am_duong": "Dương", "tinh_he": "Nam Đẩu", "dac_tinh": "Phủ tinh"},
    "Thái Âm": {"ngu_hanh": "Thủy", "am_duong": "Âm", "tinh_he": "Trung Thiên", "dac_tinh": "Tài tinh"},
    "Tham Lang": {"ngu_hanh": "Thủy", "am_duong": "Âm", "tinh_he": "Bắc Đẩu", "dac_tinh": "Đào hoa"},
    "Cự Môn": {"ngu_hanh": "Thủy", "am_duong": "Âm", "tinh_he": "Bắc Đẩu", "dac_tinh": "Ám tinh"},
    "Thiên Tướng": {"ngu_hanh": "Thủy", "am_duong": "Dương", "tinh_he": "Nam Đẩu", "dac_tinh": "Ấn tinh"},
    "Thiên Lương": {"ngu_hanh": "Thổ", "am_duong": "Âm", "tinh_he": "Nam Đẩu", "dac_tinh": "Ấm tinh"},
    "Thất Sát": {"ngu_hanh": "Kim", "am_duong": "Dương", "tinh_he": "Nam Đẩu", "dac_tinh": "Sát tinh"},
    "Phá Quân": {"ngu_hanh": "Thủy", "am_duong": "Âm", "tinh_he": "Bắc Đẩu", "dac_tinh": "Hao tinh"},
}

PHU_TINH = [
    "Tả Phụ", "Hữu Bật", "Văn Xương", "Văn Khúc", "Thiên Khôi", "Thiên Việt",
    "Lộc Tồn", "Thiên Mã", "Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Hóa Kỵ",
    "Thiên Hình", "Thiên Riêu", "Long Trì", "Phượng Các",
    "Đào Hoa", "Hồng Loan", "Thiên Hỷ", "Cô Thần", "Quả Tú",
    "Thiên Tài", "Thiên Thọ", "Ân Quang", "Thiên Quý"
]

SAT_TINH = [
    "Kình Dương", "Đà La", "Hỏa Tinh", "Linh Tinh", "Địa Không", "Địa Kiếp",
    "Kiếp Sát", "Thiên Không"
]

VONG_TRANG_SINH = [
    "Trường Sinh", "Mộc Dục", "Quan Đới", "Lâm Quan",
    "Đế Vượng", "Suy", "Bệnh", "Tử", "Mộ", "Tuyệt", "Thai", "Dưỡng"
]

BAC_SY_12_THAN = [
    "Bác Sỹ", "Lực Sỹ", "Thanh Long", "Tiểu Hao",
    "Tướng Quân", "Tấu Thư", "Phi Liêm", "Hỷ Thần",
    "Bệnh Phù", "Đại Hao", "Phục Binh", "Quan Phủ"
]

TUONG_QUAN_12_THAN = [
    "Tướng Quân", "Phan Án", "Tuế Dịch", "Tức Thần",
    "Hoa Cái", "Kiếp Sát", "Tai Sát", "Thiên Sát",
    "Chỉ Bối", "Hàm Trì", "Nguyệt Sát", "Vong Thần"
]

TUE_PHA_12_THAN = [
    "Tuế Kiến", "Hối Khí", "Tang Môn", "Quán Tác",
    "Quan Phù", "Tiểu Hao", "Đại Hao", "Long Đức",
    "Bạch Hổ", "Thiên Đức", "Điếu Khách", "Bệnh Phù"
]

TUAN_KHONG = {
    0: (10, 11), 1: (10, 11),  # Giáp, Ất → Tuất, Hợi
    2: (8, 9),   3: (8, 9),    # Bính, Đinh → Thân, Dậu
    4: (6, 7),   5: (6, 7),    # Mậu, Kỷ → Ngọ, Mùi
    6: (4, 5),   7: (4, 5),    # Canh, Tân → Thìn, Tỵ
    8: (2, 3),   9: (2, 3),    # Nhâm, Quý → Dần, Mão
}

TRIET_KHONG = {
    0: (8, 9),   1: (8, 9),    # Giáp, Ất → Thân, Dậu
    2: (6, 7),   3: (6, 7),    # Bính, Đinh → Ngọ, Mùi
    4: (4, 5),   5: (4, 5),    # Mậu, Kỷ → Thìn, Tỵ
    6: (2, 3),   7: (2, 3),    # Canh, Tân → Dần, Mão
    8: (0, 1),   9: (0, 1),    # Nhâm, Quý → Tý, Sửu
}

TRANG_SINH_KHOI_DAU = {2: 7, 3: 11, 4: 4, 5: 7, 6: 2}

TUONG_QUAN_KHOI_DAU = {
    2: 6, 6: 6, 10: 6,    # Dần(2), Ngọ(6), Tuất(10) → Ngọ(6)
    0: 0, 4: 0, 8: 0,     # Tý(0), Thìn(4), Thân(8) → Tý(0)
    3: 9, 7: 9, 11: 9,    # Mão(3), Mùi(7), Hợi(11) → Dậu(9)
    1: 3, 5: 3, 9: 3,     # Sửu(1), Tỵ(5), Dậu(9) → Mão(3)
}

PHU_TINH = [
    "Tả Phụ", "Hữu Bật", "Văn Xương", "Văn Khúc", "Thiên Khôi", "Thiên Việt",
    "Lộc Tồn", "Thiên Mã", "Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Hóa Kỵ",
    "Thiên Hình", "Thiên Riêu", "Long Trì", "Phượng Các",
    "Đào Hoa", "Hồng Loan", "Thiên Hỷ", "Cô Thần", "Quả Tú",
    "Thiên Tài", "Thiên Thọ", "Ân Quang", "Thiên Quý",
    "Tuần", "Triệt",
    "Trường Sinh", "Mộc Dục", "Quan Đới", "Lâm Quan", "Đế Vượng",
    "Suy", "Bệnh", "Tử", "Mộ", "Tuyệt", "Thai", "Dưỡng",
    "Bác Sỹ", "Lực Sỹ", "Thanh Long", "Tiểu Hao",
    "Tướng Quân", "Tấu Thư", "Phi Liêm", "Hỷ Thần",
    "Bệnh Phù", "Đại Hao", "Phục Binh", "Quan Phủ",
    "Phan Án", "Tuế Dịch", "Tức Thần",
    "Tai Sát", "Thiên Sát", "Chỉ Bối", "Hàm Trì", "Nguyệt Sát", "Vong Thần",
    "Tuế Kiến", "Hối Khí", "Tang Môn", "Quán Tác",
    "Quan Phù", "Long Đức", "Bạch Hổ", "Thiên Đức", "Điếu Khách",
]

SAT_TINH = [
    "Kình Dương", "Đà La", "Hỏa Tinh", "Linh Tinh", "Địa Không", "Địa Kiếp",
    "Kiếp Sát", "Thiên Không",
]

TU_HOA = {
    "Giáp": {"Lộc": "Liêm Trinh", "Quyền": "Phá Quân", "Khoa": "Vũ Khúc", "Kỵ": "Thái Dương"},
    "Ất": {"Lộc": "Thiên Cơ", "Quyền": "Thiên Lương", "Khoa": "Tử Vi", "Kỵ": "Thái Âm"},
    "Bính": {"Lộc": "Thiên Đồng", "Quyền": "Thiên Cơ", "Khoa": "Văn Xương", "Kỵ": "Liêm Trinh"},
    "Đinh": {"Lộc": "Thái Âm", "Quyền": "Thiên Đồng", "Khoa": "Thiên Cơ", "Kỵ": "Cự Môn"},
    "Mậu": {"Lộc": "Tham Lang", "Quyền": "Thái Âm", "Khoa": "Hữu Bật", "Kỵ": "Thiên Cơ"},
    "Kỷ": {"Lộc": "Vũ Khúc", "Quyền": "Tham Lang", "Khoa": "Thiên Lương", "Kỵ": "Văn Khúc"},
    "Canh": {"Lộc": "Thái Dương", "Quyền": "Vũ Khúc", "Khoa": "Thiên Đồng", "Kỵ": "Thái Âm"},
    "Tân": {"Lộc": "Cự Môn", "Quyền": "Thái Dương", "Khoa": "Văn Khúc", "Kỵ": "Văn Xương"},
    "Nhâm": {"Lộc": "Thiên Lương", "Quyền": "Tử Vi", "Khoa": "Thiên Phủ", "Kỵ": "Vũ Khúc"},
    "Quý": {"Lộc": "Phá Quân", "Quyền": "Cự Môn", "Khoa": "Thái Âm", "Kỵ": "Tham Lang"},
}

NATAL_STAR_MATRIX = {
    "Tử Vi": ["B", "Đ", "M", "B", "V", "M", "M", "Đ", "M", "B", "V", "B"],
    "Liêm Trinh": ["V", "Đ", "V", "H", "M", "H", "V", "Đ", "V", "H", "M", "H"],
    "Thiên Đồng": ["V", "H", "M", "Đ", "H", "Đ", "H", "H", "M", "H", "H", "Đ"],
    "Vũ Khúc": ["V", "M", "V", "Đ", "M", "H", "V", "M", "V", "Đ", "M", "H"],
    "Thái Dương": ["H", "Đ", "V", "V", "V", "M", "M", "Đ", "H", "H", "H", "H"],
    "Thiên Cơ": ["Đ", "Đ", "H", "M", "M", "V", "Đ", "Đ", "V", "M", "M", "H"],
    "Thiên Phủ": ["Đ", "V", "Đ", "M", "B", "H", "B", "Đ", "Đ", "Đ", "Đ", "Đ"],
    "Thái Âm": ["V", "Đ", "H", "H", "H", "H", "H", "Đ", "V", "M", "M", "M"],
    "Tham Lang": ["H", "M", "Đ", "H", "V", "H", "H", "M", "Đ", "H", "V", "H"],
    "Cự Môn": ["V", "H", "V", "M", "H", "H", "V", "H", "Đ", "M", "H", "Đ"],
    "Thiên Tướng": ["V", "Đ", "M", "H", "V", "Đ", "V", "Đ", "M", "H", "V", "Đ"],
    "Thiên Lương": ["V", "Đ", "V", "V", "M", "H", "M", "Đ", "V", "H", "M", "H"],
    "Thất Sát": ["M", "Đ", "M", "H", "H", "V", "M", "Đ", "M", "H", "H", "V"],
    "Phá Quân": ["M", "V", "H", "H", "Đ", "H", "M", "V", "H", "H", "Đ", "H"],
    "Văn Xương": ["H", "Đ", "Đ", "M", "H", "Đ", "Đ", "M", "H", "Đ", "Đ", "M"],
    "Văn Khúc": ["B", "V", "Đ", "M", "H", "V", "Đ", "M", "H", "V", "Đ", "M"],
    "Hỏa Tinh": ["M", "Đ", "H", "Đ", "M", "Đ", "H", "Đ", "M", "Đ", "H", "Đ"],
    "Linh Tinh": ["M", "Đ", "H", "Đ", "M", "Đ", "H", "Đ", "M", "Đ", "H", "Đ"],
    "Kình Dương": ["", "H", "M", "", "H", "M", "", "H", "M", "", "H", "M"],
    "Đà La": ["H", "", "M", "H", "", "M", "H", "", "M", "H", "", "M"],
}

DAC_TINH_LABEL = {"M": "Miếu", "V": "Vượng", "Đ": "Đắc", "B": "Bình", "H": "Hãm"}
