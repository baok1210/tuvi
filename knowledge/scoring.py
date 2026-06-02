STAR_BASE_SCORE = {
    "Tử Vi": 18, "Thiên Cơ": 10, "Thái Dương": 12, "Vũ Khúc": 11,
    "Thiên Đồng": 9, "Liêm Trinh": 8, "Thiên Phủ": 16, "Thái Âm": 11,
    "Tham Lang": 10, "Cự Môn": 6, "Thiên Tướng": 12, "Thiên Lương": 11,
    "Thất Sát": 7, "Phá Quân": 6,
    "Tả Phụ": 10, "Hữu Bật": 10, "Văn Xương": 9, "Văn Khúc": 9,
    "Thiên Khôi": 11, "Thiên Việt": 11, "Lộc Tồn": 8, "Thiên Mã": 4,
    "Kình Dương": -12, "Đà La": -10, "Hỏa Tinh": -8, "Linh Tinh": -8,
    "Địa Không": -9, "Địa Kiếp": -9, "Thiên Hình": -4,
    "Thái Tuế": -3, "Cô Thần": -4, "Quả Tú": -4,
}

BRIGHTNESS_COEF = {"Miếu": 1.5, "Vượng": 1.3, "Đắc": 1.1, "Bình": 1.0, "Hãm": 0.5}

SIHUA_MODIFIER = {"Lộc": 15, "Quyền": 12, "Khoa": 10, "Kỵ": -18}

CUNG_MULTIPLIER = {
    "Mệnh": 1.5, "Huynh đệ": 0.8, "Phu thê": 1.2, "Tử tức": 1.0,
    "Tài bạch": 1.3, "Tật ách": 1.2, "Thiên di": 1.0, "Nô bộc": 0.6,
    "Quan lộc": 1.4, "Điền trạch": 0.9, "Phúc đức": 0.8, "Phụ mẫu": 0.7,
}

DIMENSION_MAP = {
    "Sự nghiệp": ["Mệnh", "Quan lộc", "Thiên di"],
    "Tài chính": ["Tài bạch", "Phúc đức", "Điền trạch", "Mệnh"],
    "Tình cảm": ["Phu thê", "Tử tức", "Huynh đệ", "Mệnh"],
    "Sức khỏe": ["Tật ách", "Phụ mẫu", "Mệnh"],
}


def tinh_diem_cung(cung_data, tu_hoa_map):
    score = 50
    star_detail = []

    all_stars = cung_data.get("chinh_tinh", []) + cung_data.get("phu_tinh", []) + cung_data.get("sat_tinh", [])
    dac_tinh = cung_data.get("dac_tinh", {})

    for star in all_stars:
        base = STAR_BASE_SCORE.get(star, 0)
        coeff = BRIGHTNESS_COEF.get(dac_tinh.get(star, "Bình"), 1.0)
        adjusted = base * coeff
        score += adjusted

        hoa_loai = next((k for k, v in tu_hoa_map.items() if v == star), None)
        if hoa_loai:
            score += SIHUA_MODIFIER.get(hoa_loai, 0)
            star_detail.append({"sao": star, "diem_goc": base, "he_so": coeff, "hoa": hoa_loai})
        else:
            star_detail.append({"sao": star, "diem_goc": base, "he_so": coeff})

    multiplier = CUNG_MULTIPLIER.get(cung_data.get("ten", ""), 1.0)
    score = score * multiplier
    score = round(max(0, min(100, score)))

    return {
        "diem": score,
        "xep_loai": xep_loai(score),
        "chi_tiet": star_detail,
    }


def xep_loai(score):
    if score >= 85: return "Tốt"
    if score >= 70: return "Khá"
    if score >= 50: return "Trung bình"
    if score >= 30: return "Kém"
    return "Xấu"


def tinh_diem_toan_bo(thap_nhi_cung, tu_hoa):
    tu_hoa_map = {v: k for k, v in tu_hoa.items() if v}
    diem_cung = {}
    tong = 0
    count = 0
    for cung in thap_nhi_cung:
        result = tinh_diem_cung(cung, tu_hoa_map)
        diem_cung[cung["ten"]] = {"diem": result["diem"], "xep_loai": result["xep_loai"]}
        tong += result["diem"]
        count += 1

    diem_trung_binh = round(tong / count) if count else 50

    dimensions = {}
    for dim_name, cung_list in DIMENSION_MAP.items():
        dim_score = sum(diem_cung[c]["diem"] for c in cung_list if c in diem_cung)
        dim_count = sum(1 for c in cung_list if c in diem_cung)
        dimensions[dim_name] = {
            "diem": round(dim_score / dim_count) if dim_count else 50,
            "xep_loai": xep_loai(dim_score / dim_count) if dim_count else "Trung bình",
        }

    return {
        "diem_trung_binh": diem_trung_binh,
        "xep_loai_tong_quan": xep_loai(diem_trung_binh),
        "tung_cung": diem_cung,
        "cac_khia_canh": dimensions,
    }
