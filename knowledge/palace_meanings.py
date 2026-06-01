PALACE_MEANINGS = {
    "Mệnh": {
        "ten": "Mệnh",
        "y_nghia": "Cung quan trọng nhất, đại diện cho bản thân, tính cách và vận mệnh cả đời.",
        "chi_tiet": "Phân tích nhân cách, sức khỏe, ngoại hình, tài năng bẩm sinh và khuynh hướng cuộc đời.",
    },
    "Huynh đệ": {
        "ten": "Huynh Đệ",
        "y_nghia": "Cung về anh chị em, bạn bè thân thiết, đồng nghiệp.",
        "chi_tiet": "Thể hiện mối quan hệ với anh chị em ruột, bạn bè thân và cấp dưới.",
    },
    "Phu thê": {
        "ten": "Phu Thê",
        "y_nghia": "Cung về hôn nhân, người bạn đời và quan hệ vợ chồng.",
        "chi_tiet": "Phân tích tình duyên, hôn nhân, phẩm chất người bạn đời và cuộc sống gia đình.",
    },
    "Tử tức": {
        "ten": "Tử Tức",
        "y_nghia": "Cung về con cái, việc sinh nở và quan hệ cha mẹ - con cái.",
        "chi_tiet": "Thể hiện số lượng, tính cách con cái, mối quan hệ và sự nghiệp của chúng.",
    },
    "Tài bạch": {
        "ten": "Tài Bạch",
        "y_nghia": "Cung về tài chính, tiền bạc và khả năng kiếm tiền.",
        "chi_tiet": "Phân tích thu nhập, chi tiêu, đầu tư, khả năng tích lũy và vận may tài chính.",
    },
    "Tật ách": {
        "ten": "Tật Ách",
        "y_nghia": "Cung về sức khỏe, bệnh tật và tai nạn.",
        "chi_tiet": "Thể hiện tình trạng sức khỏe, các bệnh dễ mắc phải và khả năng gặp tai nạn.",
    },
    "Thiên di": {
        "ten": "Thiên Di",
        "y_nghia": "Cung về sự di chuyển, xuất ngoại và các mối quan hệ xã hội.",
        "chi_tiet": "Phân tích vận mệnh khi ra ngoài, đi xa, xuất ngoại và khả năng gặp quý nhân.",
    },
    "Nô bộc": {
        "ten": "Nô Bộc",
        "y_nghia": "Cung về bạn bè, đồng nghiệp, cấp dưới và các mối quan hệ xã hội.",
        "chi_tiet": "Thể hiện chất lượng bạn bè, mối quan hệ với đồng nghiệp và người giúp việc.",
    },
    "Quan lộc": {
        "ten": "Quan Lộc",
        "y_nghia": "Cung về sự nghiệp, công danh và địa vị xã hội.",
        "chi_tiet": "Phân tích con đường sự nghiệp, thành công, thăng tiến và uy tín xã hội.",
    },
    "Điền trạch": {
        "ten": "Điền Trạch",
        "y_nghia": "Cung về nhà cửa, đất đai và tài sản bất động sản.",
        "chi_tiet": "Thể hiện vận mệnh về nhà ở, đất đai, khả năng mua bán và đầu tư bất động sản.",
    },
    "Phúc đức": {
        "ten": "Phúc Đức",
        "y_nghia": "Cung về phúc khí, tổ tiên và đời sống tinh thần.",
        "chi_tiet": "Phân tích phúc đức tổ tiên, đời sống tinh thần, tâm linh và hưởng thụ.",
    },
    "Phụ mẫu": {
        "ten": "Phụ Mẫu",
        "y_nghia": "Cung về cha mẹ, trưởng bối và nguồn gốc gia đình.",
        "chi_tiet": "Thể hiện mối quan hệ với cha mẹ, sự giáo dục và ảnh hưởng từ gia đình.",
    },
}


def tra_cuu_cung(ten_cung):
    return PALACE_MEANINGS.get(ten_cung)
