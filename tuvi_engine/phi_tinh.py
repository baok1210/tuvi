TU_HOA_MAP = {
    "Giáp": {"Lộc": "Liêm Trinh", "Quyền": "Phá Quân", "Khoa": "Vũ Khúc", "Kỵ": "Thái Dương"},
    "Ất":  {"Lộc": "Thiên Cơ", "Quyền": "Thiên Lương", "Khoa": "Tử Vi", "Kỵ": "Thái Âm"},
    "Bính": {"Lộc": "Thiên Đồng", "Quyền": "Thiên Cơ", "Khoa": "Văn Xương", "Kỵ": "Liêm Trinh"},
    "Đinh": {"Lộc": "Thái Âm", "Quyền": "Thiên Đồng", "Khoa": "Thiên Cơ", "Kỵ": "Cự Môn"},
    "Mậu": {"Lộc": "Tham Lang", "Quyền": "Thái Âm", "Khoa": "Hữu Bật", "Kỵ": "Thiên Cơ"},
    "Kỷ":  {"Lộc": "Vũ Khúc", "Quyền": "Tham Lang", "Khoa": "Thiên Lương", "Kỵ": "Văn Khúc"},
    "Canh": {"Lộc": "Thái Dương", "Quyền": "Vũ Khúc", "Khoa": "Thái Âm", "Kỵ": "Thiên Đồng"},
    "Tân": {"Lộc": "Cự Môn", "Quyền": "Thái Dương", "Khoa": "Văn Khúc", "Kỵ": "Văn Xương"},
    "Nhâm": {"Lộc": "Thiên Lương", "Quyền": "Tử Vi", "Khoa": "Tả Phụ", "Kỵ": "Vũ Khúc"},
    "Quý": {"Lộc": "Phá Quân", "Quyền": "Cự Môn", "Khoa": "Thái Âm", "Kỵ": "Tham Lang"},
}

NGA_CUNG = {"Mệnh", "Tài Bạch", "Quan Lộc", "Tật Ách", "Phúc Đức", "Điền Trạch"}
THA_CUNG = {"Phu Thê", "Tử Tức", "Thiên Di", "Nô Bộc", "Huynh Đệ", "Phụ Mẫu"}


def phi_tu_hoa(thien_can, cung_map):
    hoa = TU_HOA_MAP.get(thien_can)
    if not hoa:
        return {}

    result = {}
    for loai, sao in hoa.items():
        for cung_ten, cung_data in cung_map.items():
            chinh_tinh_list = [s.split("(")[0] for s in cung_data.get("chinh_tinh", [])]
            phu_tinh = cung_data.get("phu_tinh", [])
            all_stars = chinh_tinh_list + phu_tinh
            if sao in all_stars:
                result[loai] = {"sao": sao, "cung": cung_ten, "dia_chi": cung_data["dia_chi"]}
                break
    return result


def phi_cung_hoa_tuong(la_so_dict):
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    cung_map = {}
    for c in thap_nhi_cung:
        cung_map[c["ten"]] = c

    sinh_nien_can = la_so_dict["thong_tin_co_ban"].get("nam_can")
    sinh_nien_chi = la_so_dict["thong_tin_co_ban"].get("nam_chi")

    sinh_nien_tu_hoa = phi_tu_hoa(sinh_nien_can, cung_map) if sinh_nien_can else {}

    ket_qua = {
        "sinh_nien_tu_hoa": sinh_nien_tu_hoa,
        "phi_cung": [],
    }

    if sinh_nien_chi:
        lai_nhan_index = ({"Tý": 0, "Sửu": 1, "Dần": 2, "Mão": 3, "Thìn": 4, "Tỵ": 5,
                           "Ngọ": 6, "Mùi": 7, "Thân": 8, "Dậu": 9, "Tuất": 10, "Hợi": 11}
                          .get(sinh_nien_chi, 0))
        for c in thap_nhi_cung:
            if c["so_thu_tu"] == lai_nhan_index:
                ket_qua["lai_nhan_cung"] = c["ten"]
                break

    for c in thap_nhi_cung:
        can_cung = c.get("can_cung")
        if can_cung and can_cung in TU_HOA_MAP:
            phi = phi_tu_hoa(can_cung, cung_map)
            if phi:
                for loai, info in phi.items():
                    ket_qua["phi_cung"].append({
                        "cung_goc": c["ten"],
                        "thien_can": can_cung,
                        "loai": loai,
                        "sao": info["sao"],
                        "cung_dich": info["cung"],
                        "dia_chi": info["dia_chi"],
                    })

    return ket_qua


def phan_tich_dai_van_phi_hoa(la_so_dict, dai_van_bat_dau):
    sinh_nien_can = la_so_dict["thong_tin_co_ban"].get("nam_can")
    thap_nhi_cung = la_so_dict["thap_nhi_cung"]
    cung_map = {}
    for c in thap_nhi_cung:
        cung_map[c["ten"]] = c

    dai_van_phi = []
    for c in thap_nhi_cung:
        can_cung = c.get("can_cung")
        if can_cung and can_cung in TU_HOA_MAP:
            hoa = TU_HOA_MAP[can_cung]
            for loai, sao in hoa.items():
                for cung_ten, cung_data in cung_map.items():
                    chinh_tinh_list = [s.split("(")[0] for s in cung_data.get("chinh_tinh", [])]
                    if sao in chinh_tinh_list:
                        dai_van_phi.append({
                            "dai_van_cung": c["ten"],
                            "thien_can": can_cung,
                            "loai": loai,
                            "sao": sao,
                            "nhap_cung": cung_ten,
                        })
                        break
    return dai_van_phi


def tu_hoa_analysis(sinh_nien_tu_hoa, phi_cung_list):
    result = {
        "loc_nga_cung": [],
        "loc_tha_cung": [],
        "ky_nga_cung": [],
        "ky_tha_cung": [],
        "loc_ky_dong_cung": [],
    }

    for item in phi_cung_list:
        cung_dich = item["cung_dich"]
        loai = item["loai"]
        if loai == "Lộc":
            if cung_dich in NGA_CUNG:
                result["loc_nga_cung"].append(item)
            else:
                result["loc_tha_cung"].append(item)
        elif loai == "Kỵ":
            if cung_dich in NGA_CUNG:
                result["ky_nga_cung"].append(item)
            else:
                result["ky_tha_cung"].append(item)

    for loc_item in result["loc_nga_cung"] + result["loc_tha_cung"]:
        for ky_item in result["ky_nga_cung"] + result["ky_tha_cung"]:
            if (loc_item["sao"] == ky_item["sao"]
                    and loc_item["cung_dich"] == ky_item["cung_dich"]):
                result["loc_ky_dong_cung"].append({
                    "cung": loc_item["cung_dich"],
                    "sao": loc_item["sao"],
                    "loc_tu": loc_item["cung_goc"],
                    "ky_tu": ky_item["cung_goc"],
                })

    return result


def phan_tich_nga_tha(hoa_loc_cung, hoa_ky_cung):
    if hoa_loc_cung in NGA_CUNG:
        loc_str = f"Hóa Lộc tại {hoa_loc_cung} (Ngã cung) -> Lợi ích thực sự cho mình"
    else:
        loc_str = f"Hóa Lộc tại {hoa_loc_cung} (Tha cung) -> Tốt cho người khác, mình hưởng gián tiếp"

    if hoa_ky_cung in NGA_CUNG:
        ky_str = f"Hóa Kỵ tại {hoa_ky_cung} (Ngã cung) -> Mình gánh trách nhiệm"
    else:
        ky_str = f"Hóa Kỵ tại {hoa_ky_cung} (Tha cung) -> Từ người khác, ảnh hưởng qua xung chiếu"

    return f"{loc_str}. {ky_str}."
