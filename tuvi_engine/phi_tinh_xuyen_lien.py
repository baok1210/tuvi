"""
Tứ Hóa Xuyến Liên (Point-to-Point Chaining).
Tính toán 4 luồng quỹ đạo: Lộc→Lộc, Lộc→Kị, Kị→Lộc, Kị→Kị.
"""

CUNG_THU_TU = [
    "Mệnh", "Huynh đệ", "Phu thê", "Tử tức",
    "Tài bạch", "Tật ách", "Thiên di", "Nô bộc",
    "Quan lộc", "Điền trạch", "Phúc đức", "Phụ mẫu",
]

CUNG_INDEX = {c: i for i, c in enumerate(CUNG_THU_TU)}


def hoa_loai_to_ten(loai):
    return {"Lộc": "Hóa Lộc", "Quyền": "Hóa Quyền", "Khoa": "Hóa Khoa", "Kỵ": "Hóa Kỵ"}.get(loai, loai)


def tinh_xuyen_lien(thap_nhi_cung, tu_hoa_dict, phi_cung_list=None):
    """Compute the 4 Tứ Hóa chaining trajectories from the Lái Nhân Cung (birth Tứ Hóa).

    Args:
        thap_nhi_cung: 12 palace data list
        tu_hoa_dict: dict like {"Lộc": "Thiên Đồng", "Quyền": "Thiên Cơ", ...}
        phi_cung_list: list of phi cung items (optional), each with cung_goc, loai, sao, cung_dich

    Returns:
        dict with xuyen_lien chains, khoang_cach analysis, and warnings
    """
    tu_hoa_map = {v: k for k, v in tu_hoa_dict.items() if v}
    
    # Normalize star names (lowercase for matching; lasotuvi returns "Thiên đồng" but config has "Thiên Đồng")
    def norm(s):
        return s.lower().replace(" ", "")

    palace_by_star = {}
    palace_by_star_lower = {}
    for c in thap_nhi_cung:
        ten = c["ten"]
        all_s = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
        for s in all_s:
            if s not in palace_by_star:
                palace_by_star[s] = ten
            nk = norm(s)
            if nk not in palace_by_star_lower:
                palace_by_star_lower[nk] = ten

    # Step 1: Find which palaces have the Hóa stars
    hoa_palaces = {}
    for loai, sao in tu_hoa_dict.items():
        if not sao:
            continue
        if sao in palace_by_star:
            cung_ten = palace_by_star[sao]
        else:
            nk = norm(sao)
            cung_ten = palace_by_star_lower.get(nk)
        if cung_ten:
            hoa_palaces[loai] = {
                "sao": sao,
                "cung": cung_ten,
                "dia_chi": next((c["dia_chi"] for c in thap_nhi_cung if c["ten"] == cung_ten), ""),
            }

    # Step 2: Xuyến liên
    chains = {
        "Loc_chuyen_Loc": _build_chain("Lộc", "Lộc", hoa_palaces, thap_nhi_cung),
        "Loc_chuyen_Ki": _build_chain("Lộc", "Kỵ", hoa_palaces, thap_nhi_cung),
        "Ki_chuyen_Loc": _build_chain("Kỵ", "Lộc", hoa_palaces, thap_nhi_cung),
        "Ki_chuyen_Ki": _build_chain("Kỵ", "Kỵ", hoa_palaces, thap_nhi_cung),
    }

    # Step 3: Ma trận Khoảng cách
    khoang_cach = {}
    if "Lộc" in hoa_palaces and "Kỵ" in hoa_palaces:
        loc_cung = hoa_palaces["Lộc"]["cung"]
        ky_cung = hoa_palaces["Kỵ"]["cung"]
        if loc_cung in CUNG_INDEX and ky_cung in CUNG_INDEX:
            dist = (CUNG_INDEX[ky_cung] - CUNG_INDEX[loc_cung]) % 12
            if dist == 0:
                dist = 12
            ten_khoang = {4: "Tứ Phụng", 3: "Tam Kỳ", 2: "Lưỡng Nghi"}.get(dist, None)
            khoang_cach = {
                "cung_loc": loc_cung,
                "cung_ky": ky_cung,
                "khoang_cach": dist,
                "ten_khoang": ten_khoang,
                "nhan_xet": _dien_giai_khoang_cach(dist, ten_khoang),
            }

    # Step 4: Tự Hóa & Thị Phi detection
    tu_hoa_trang_thai = _phat_hien_tu_hoa(thap_nhi_cung, tu_hoa_dict)
    thi_phi = _phat_hien_thi_phi(phi_cung_list or [])

    return {
        "co_so": {
            "tu_hoa_nam_sinh": tu_hoa_dict,
            "hoa_palaces": hoa_palaces,
        },
        "xuyen_lien": {k: v for k, v in chains.items() if v},
        "khoang_cach": khoang_cach if khoang_cach else None,
        "tu_hoa_trang_thai": tu_hoa_trang_thai if tu_hoa_trang_thai else None,
        "thi_phi": thi_phi if thi_phi else None,
        "canh_bao": _tao_canh_bao(chains, khoang_cach, tu_hoa_trang_thai),
    }


def _build_chain(loai_a, loai_b, hoa_palaces, thap_nhi_cung):
    """Build a single chaining path: loai_A → loai_B."""
    if loai_a not in hoa_palaces or loai_b not in hoa_palaces:
        return None
    cung_a = hoa_palaces[loai_a]["cung"]
    cung_b = hoa_palaces[loai_b]["cung"]
    if cung_a == cung_b:
        return None

    chains = {
        "Lộc": "Lộc→Lộc",
        "Lộc_Kỵ": "Lộc→Kị",
        "Kỵ_Lộc": "Kị→Lộc",
        "Kỵ_Kỵ": "Kị→Kị",
    }
    chain_map = {("Lộc", "Lộc"): "Lộc", ("Lộc", "Kỵ"): "Lộc_Kỵ",
                 ("Kỵ", "Lộc"): "Kỵ_Lộc", ("Kỵ", "Kỵ"): "Kỵ_Kỵ"}
    key = (loai_a, loai_b)
    
    return {
        "loai": chain_map.get(key, f"{loai_a}→{loai_b}"),
        "cung_goc": cung_a,
        "sao_goc": hoa_palaces[loai_a]["sao"],
        "cung_dich": cung_b,
        "sao_dich": hoa_palaces[loai_b]["sao"],
        "y_nghia": _y_nghia_xuyen_lien(loai_a, loai_b),
    }


def _y_nghia_xuyen_lien(loai_a, loai_b):
    meanings = {
        ("Lộc", "Lộc"): "Ta muốn làm tốt điều gì? Ta sẽ nhận được điều đó, và tốt cụ thể ở chỗ nào?",
        ("Lộc", "Kỵ"): "Ta muốn làm hoặc sẽ nhận được gì, nhưng điều tốt đẹp đó sẽ tiềm ẩn nguy cơ hoặc mất đi ở đâu?",
        ("Kỵ", "Lộc"): "Điểm tổn thất, tai ách nằm ở đâu? Ta sẽ nhận được sự bồi thường, bù đắp hoặc cứu giải ở cung vị nào?",
        ("Kỵ", "Kỵ"): "Ta đang chấp mê, mệt mỏi vì điều gì? Kết quả cuối cùng sẽ thất bại ở đâu, dưới tay ai?",
    }
    return meanings.get((loai_a, loai_b), "")


def _dien_giai_khoang_cach(dist, ten_khoang):
    if ten_khoang is None:
        return f"Khoảng cách {dist} cung: không thuộc cấu trúc đặc biệt."
    descriptions = {
        "Tứ Phụng": "Biểu hiện quan hệ đối đãi và biến hóa sâu sắc giữa nguyên nhân và kết quả.",
        "Tam Kỳ": "Biểu hiện biến động rõ rệt về cát hung, thời vận.",
        "Lưỡng Nghi": "Biểu hiện mối quan hệ đối đãi xung đột, không thuận lợi.",
    }
    return descriptions.get(ten_khoang, "")


def _phat_hien_tu_hoa(thap_nhi_cung, tu_hoa_dict):
    """Phát hiện Tự Hóa (tự hóa Lộc/Kị/Quyền/Khoa) trong thập nhị cung."""
    def norm(s):
        return s.lower().replace(" ", "")
    all_lower = {}
    for c in thap_nhi_cung:
        for s in c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]:
            all_lower[(norm(s), c["ten"])] = s
    results = []
    for c in thap_nhi_cung:
        all_s = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
        all_s_lower = [norm(s) for s in all_s]
        for loai, sao in tu_hoa_dict.items():
            if sao and norm(sao) in all_s_lower:
                results.append({
                    "cung": c["ten"],
                    "sao": sao,
                    "hoa_loai": loai,
                    "trang_thai": "Tự Hóa (đồng cung)" if c["ten"] != "Mệnh" else "Niên Hóa (tiên thiên)",
                })
    return results if results else None


def _phat_hien_thi_phi(phi_cung_list):
    """Detect Thị Phi Kị (Lộc lai Kị) patterns."""
    results = []
    for p in phi_cung_list:
        if p.get("loai") == "Hóa Lộc":
            # Check if the destination palace has a Kỵ
            dich = p.get("cung_dich", "")
            for p2 in phi_cung_list:
                if p2.get("loai") == "Hóa Kỵ" and p2.get("cung_goc") == dich:
                    results.append({
                        "cung_goc": p["cung_goc"],
                        "cung_nhan_loc": p["cung_dich"],
                        "loai": "Thị Phi Kị (Lộc lai Kị)",
                        "mo_ta": f"{p['cung_goc']} phi Lộc nhập {p['cung_dich']}, {p['cung_dich']} phi Kị phản hồi. Ban ơn mắc oán.",
                    })
    return results if results else None


def _tao_canh_bao(chains, khoang_cach, tu_hoa_trang_thai):
    """Generate warnings based on analysis."""
    warnings = []
    if chains.get("Ki_chuyen_Ki"):
        warnings.append({
            "muc": "CAO",
            "noi_dung": f"Kị→Kị: {chains['Ki_chuyen_Ki']['cung_goc']} → {chains['Ki_chuyen_Ki']['cung_dich']}. Chuỗi tổn thất kép.",
        })
    if khoang_cach and khoang_cach.get("ten_khoang") == "Lưỡng Nghi":
        warnings.append({
            "muc": "TRUNG BÌNH",
            "noi_dung": f"Lộc-Kị đối xung (Lưỡng Nghi). Mâu thuẫn giữa điều tốt và xấu.",
        })
    if tu_hoa_trang_thai:
        for th in tu_hoa_trang_thai:
            if th["hoa_loai"] == "Kỵ":
                warnings.append({
                    "muc": "TRUNG BÌNH",
                    "noi_dung": f"Tự Hóa Kỵ tại {th['cung']}: Kị xuất, hóa thành không.",
                })
    return warnings if warnings else None
