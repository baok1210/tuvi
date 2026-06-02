"""
Trung Châu tử vi đẩu số - Tứ Hóa Phái (中州紫微斗数 - 四化派).
Nguyễn Anh Vũ dịch - Trường phái Trung Châu do Vương Đình Chi (王亭之) công khai hóa.
"""

TRUNG_CHAU_HOA_BANG = {
    "Giap": {"Lộc": "Liêm Trinh", "Quyền": "Phá Quân", "Khoa": "Vũ Khúc", "Kỵ": "Thái Dương"},
    "Ất": {"Lộc": "Thiên Cơ", "Quyền": "Thiên Lương", "Khoa": "Tử Vi", "Kỵ": "Thái Âm"},
    "Bính": {"Lộc": "Thiên Đồng", "Quyền": "Thiên Cơ", "Khoa": "Văn Xương", "Kỵ": "Liêm Trinh"},
    "Đinh": {"Lộc": "Thái Âm", "Quyền": "Thiên Đồng", "Khoa": "Thiên Cơ", "Kỵ": "Cự Môn"},
    "Mậu": {"Lộc": "Tham Lang", "Quyền": "Thái Dương", "Khoa": "Hữu Bật", "Kỵ": "Thiên Cơ"},
    "Kỷ": {"Lộc": "Vũ Khúc", "Quyền": "Tham Lang", "Khoa": "Thiên Lương", "Kỵ": "Văn Khúc"},
    "Canh": {"Lộc": "Thái Dương", "Quyền": "Vũ Khúc", "Khoa": "Thái Âm", "Kỵ": "Thiên Đồng"},
    "Tân": {"Lộc": "Cự Môn", "Quyền": "Thái Dương", "Khoa": "Văn Khúc", "Kỵ": "Văn Xương"},
    "Nhâm": {"Lộc": "Thiên Lương", "Quyền": "Tử Vi", "Khoa": "Tả Phụ", "Kỵ": "Vũ Khúc"},
    "Quý": {"Lộc": "Phá Quân", "Quyền": "Cự Môn", "Khoa": "Thái Âm", "Kỵ": "Tham Lang"},
}

TRUNG_CHAU_PHU_TINH_HOA = {
    "Tả Phụ": {"Khoa": "Kỷ", "Kỵ": "Quý"},
    "Hữu Bật": {"Khoa": "Mậu", "Kỵ": "Giáp"},
    "Văn Xương": {"Khoa": "Bính", "Lộc": "Quý", "Kỵ": "Tân"},
    "Văn Khúc": {"Khoa": "Tân", "Lộc": "Ất", "Kỵ": "Kỷ"},
}

TRUNG_CHAU_LAI_NHAN_CUNG = {
    "mo_ta": "Lai Nhân Cung (来因宫) là cung của can năm sinh, là cung gốc phát ra tất cả các phi hóa trong lá số. Là 'nguyên nhân đến' của kiếp người này.",
    "y_nghia": {
        "Mệnh": "Lai Nhân từ Mệnh — sự nghiệp, bản thân là trung tâm của cuộc đời",
        "Huynh đệ": "Lai Nhân từ Huynh đệ — mẹ, bạn bè, đồng nghiệp quyết định cuộc đời",
        "Phu thê": "Lai Nhân từ Phu thê — hôn nhân, người phối ngẫu là then chốt",
        "Tử tức": "Lai Nhân từ Tử tức — con cái, học trò, đệ tử là tâm huyết",
        "Tài bạch": "Lai Nhân từ Tài bạch — tài chính, tiền bạc là trọng tâm",
        "Tật ách": "Lai Nhân từ Tật ách — sức khỏe, bệnh tật ảnh hưởng mọi mặt",
        "Thiên di": "Lai Nhân từ Thiên di — xuất ngoại, du lịch, môi trường bên ngoài",
        "Nô bộc": "Lai Nhân từ Nô bộc — cấp dưới, bạn bè, giao tế xã hội",
        "Quan lộc": "Lai Nhân từ Quan lộc — sự nghiệp, công danh",
        "Điền trạch": "Lai Nhân từ Điền trạch — nhà cửa, bất động sản, tài sản",
        "Phúc đức": "Lai Nhân từ Phúc đức — tổ tiên, phúc báo, tâm linh",
        "Phụ mẫu": "Lai Nhân từ Phụ mẫu — cha mẹ, dòng họ, văn bằng chứng chỉ",
    },
}

TRUNG_CHAU_THAI_CUC_MO_RONG = {
    "mo_ta": "Lập Thái Cực chức năng mở rộng: dùng cung X để quan sát cung Y, tạo thành các cặp phản ánh chức năng chuyên môn.",
    "cap_mo_rong": [
        {"tu": "Tài bạch của Quan lộc", "la": "Mệnh", "y_nghia": "Năng lực tài chính ảnh hưởng trực tiếp đến sự nhận thức và bản mệnh"},
        {"tu": "Quan lộc của Tật ách", "la": "Huynh đệ", "y_nghia": "Khí số cơ thể, tình trạng sức khỏe của anh em"},
        {"tu": "Nô bộc của Tài bạch", "la": "Phụ mẫu", "y_nghia": "Chi phiếu, khế ước, giấy tờ tài chính"},
        {"tu": "Tử tức của Phu thê", "la": "Tật ách", "y_nghia": "Sức khỏe liên quan đến con cái và hôn nhân"},
        {"tu": "Phúc đức của Thiên di", "la": "Điền trạch", "y_nghia": "Phúc báo khi ra ngoài xã hội"},
        {"tu": "Tài bạch của Quan lộc", "la": "Mệnh", "y_nghia": "Sự nghiệp tiêu hao tài chính thế nào"},
        {"tu": "Quan lộc của Tài bạch", "la": "Tật ách", "y_nghia": "Công việc ảnh hưởng đến sức khỏe"},
        {"tu": "Huynh đệ của Phúc đức", "la": "Phu thê", "y_nghia": "Quan hệ gia đình và hôn nhân"},
    ],
}

TRUNG_CHAU_QUOTES = [
    {
        "text": "Có thể chia Tử Vi Đẩu Số thành 2 dòng chính: Một là chủ yếu lấy 'tinh diệu' để luận đoán, gọi chung là Tam Hợp phái. Hai là chủ yếu lấy 'tứ hóa' làm dụng thần, gọi chung là Tứ Hóa Phái.",
        "source": "Trung Châu Tứ Hóa Phái – Nguyễn Anh Vũ biên dịch",
    },
    {
        "text": "Lai Nhân Cung là cung của can năm sinh, từ đó khởi nguồn tất cả suy luận Tứ Hóa trong lá số. Nó quyết định 'nguyên nhân đến' của kiếp người.",
        "source": "Trung Châu Tứ Hóa Phái – Nguyễn Anh Vũ biên dịch",
    },
    {
        "text": "Đẩu Số phi năng tùy thời biến dịch bất khả — Tử Vi Đẩu Số không thể tùy tiện thay đổi theo thời đại.",
        "source": "Trung Châu phái – Vương Đình Chi",
    },
    {
        "text": "Tài bạch của Quan lộc là Mệnh: năng lực tài chính quyết định sự nghiệp thành bại.",
        "source": "Trung Châu Tứ Hóa Phái – Nguyễn Anh Vũ biên dịch — Thái Cực mở rộng",
    },
    {
        "text": "Tử Vi Đẩu Số giống như một 'cẩm nang quản trị nhân sự' của hoàng đế, có thể cung cấp thông tin nhân sự chi tiết, chuẩn xác để đưa ra quyết định.",
        "source": "Trung Châu phái",
    },
]
