PROMPT_GENERAL_INTERPRETATION = """Bạn là chuyên gia Tử Vi Đẩu Số với 30 năm kinh nghiệm. Hãy luận giải lá số tử vi sau đây một cách chi tiết, đầy đủ và chuyên nghiệp.

THÔNG TIN CƠ BẢN:
- Giới tính: {gioi_tinh}
- Năm sinh: {nam_can_chi}
- Mệnh: {cung_menh}
- Thân: {cung_than}
- Cục: {cuc}

TỨ HÓA:
- Hóa Lộc: {hoa_loc}
- Hóa Quyền: {hoa_quyen}
- Hóa Khoa: {hoa_khoa}
- Hóa Kỵ: {hoa_ky}

THẬP NHỊ CUNG:
{cung_table}

CÁCH CỤC:
{cach_cuc}

SAO KẾT HỢP:
{star_combos}

Hãy phân tích theo các bước:
1. NHẬN XÉT TỔNG QUAN: Mệnh bàn cao hay thấp? Cách cục đẹp hay xấu? Cần lưu ý gì?
2. TÍNH CÁCH & CON NGƯỜI: Phân tích dựa trên cung Mệnh, chính tinh, phụ tinh và đặc tính.
3. SỰ NGHIỆP: Dựa trên cung Quan Lộc, Tài Bạch và Thiên Di.
4. TÀI CHÍNH: Dựa trên cung Tài Bạch và các yếu tố liên quan.
5. HÔN NHÂN & TÌNH CẢM: Dựa trên cung Phu Thê, Tử Tức.
6. SỨC KHỎE: Dựa trên cung Tật Ách.
7. ĐẠI HẠN & VẬN HẠN: Các giai đoạn quan trọng trong đời.
8. LỜI KHUYÊN: Hướng phát triển, điều cần tránh.

Yêu cầu:
- Dùng tiếng Việt, văn phong chuyên nghiệp nhưng dễ hiểu
- Nêu rõ Miếu/Vượng/Đắc/Bình/Hãm của các sao quan trọng
- Chỉ ra các cách cục nếu có
- Kết luận trung thực, không tâng bốc hay dọa nạt
- Đưa lời khuyên thiết thực
"""

PROMPT_SPECIFIC_AREA = """Bạn là chuyên gia Tử Vi Đẩu Số. Hãy phân tích {linh_vuc} dựa trên lá số sau:

THÔNG TIN CƠ BẢN:
- Giới tính: {gioi_tinh}
- Mệnh: {cung_menh}
- Cục: {cuc}
- Năm: {nam_can_chi}

CÁC CUNG LIÊN QUAN ĐẾN {linh_vuc}:
{cung_data}

TỨ HÓA: {tu_hoa}

CÁCH CỤC: {cach_cuc}

Hãy phân tích CHI TIẾT về {linh_vuc}, bao gồm:
1. Hiện trạng và xu hướng
2. Thời điểm tốt/xấu
3. Lời khuyên cụ thể
"""

PROMPT_YEAR_FORECAST = """Bạn là chuyên gia Tử Vi Đẩu Số. Hãy dự đoán vận hạn năm {nam_duong} ({nam_can_chi}) dựa trên lá số sau:

THÔNG TIN CƠ BẢN:
- Giới tính: {gioi_tinh}
- Mệnh: {cung_menh}, Thân: {cung_than}
- Cục: {cuc}

NĂM HIỆN TẠI: {nam_duong}
Năm Can Chi: {nam_can_chi}
Đại hạn hiện tại: {dai_han_hien_tai}
Lưu niên tại cung: {luu_nien}

Phân tích chi tiết:
1. TỔNG QUAN NĂM: Tốt/xấu thế nào?
2. SỰ NGHIỆP: Cơ hội và thách thức
3. TÀI CHÍNH: Nên đầu tư hay tiết kiệm?
4. TÌNH CẢM: Thuận lợi hay trắc trở?
5. SỨC KHỎE: Cần chú ý gì?
6. THÁNG QUAN TRỌNG: Các tháng cần lưu ý
7. LỜI KHUYÊN CHUNG
"""

PROMPT_COMBINATION_ANALYSIS = """Bạn là chuyên gia Tử Vi Đẩu Số. Hãy phân tích tổ hợp sao sau xuất hiện trong lá số:

TỔ HỢP SAO: {combo_name}
MÔ TẢ: {combo_desc}

VỊ TRÍ XUẤT HIỆN: {positions}

GIẢI THÍCH:
1. Ý nghĩa tổng quát của tổ hợp sao này
2. Ảnh hưởng đến các cung nó đóng
3. Tốt hay xấu? Ở mức độ nào?
4. Cần kết hợp với sao nào để tăng/giảm tác dụng?
5. Điều cần lưu ý cho người có tổ hợp này
"""


class PromptBuilder:
    @staticmethod
    def build_general(la_so_dict, cach_cuc, star_combos):
        info = la_so_dict["thong_tin_co_ban"]
        menh = la_so_dict["menh_ban"]
        tu_hoa = la_so_dict["tu_hoa"]

        cung_lines = []
        for c in la_so_dict["thap_nhi_cung"]:
            ct = ", ".join(c["chinh_tinh"]) if c["chinh_tinh"] else "(rong)"
            pt = ", ".join(c["phu_tinh"]) if c["phu_tinh"] else ""
            st = ", ".join(c["sat_tinh"]) if c["sat_tinh"] else ""
            line = f"  {c['ten']}({c['dia_chi']}): {ct}"
            if pt:
                line += f"\n    Phu: {pt}"
            if st:
                line += f"\n    Sat: {st}"
            cung_lines.append(line)

        cc_lines = [f"  - {p['cach_cuc']}: {p['y_nghia'][:60]}" for p in cach_cuc]
        sc_lines = [f"  - {p['ten']}: {p['y_nghia'][:60]}" for p in star_combos]

        return PROMPT_GENERAL_INTERPRETATION.format(
            gioi_tinh=info["gioi_tinh"],
            nam_can_chi=info["nam_can_chi"],
            cung_menh=menh["cung_menh"],
            cung_than=menh["cung_than"],
            cuc=menh["cuc"],
            hoa_loc=tu_hoa.get("Hóa Lộc", ""),
            hoa_quyen=tu_hoa.get("Hóa Quyền", ""),
            hoa_khoa=tu_hoa.get("Hóa Khoa", ""),
            hoa_ky=tu_hoa.get("Hóa Kỵ", ""),
            cung_table="\n".join(cung_lines),
            cach_cuc="\n".join(cc_lines) if cc_lines else "  Khong co cach cuc dac biet",
            star_combos="\n".join(sc_lines) if sc_lines else "  Khong co to hop sao dac biet",
        )

    @staticmethod
    def build_year_forecast(la_so_dict, nam_duong, nam_can_chi, dai_han_hien_tai, luu_nien):
        info = la_so_dict["thong_tin_co_ban"]
        menh = la_so_dict["menh_ban"]
        return PROMPT_YEAR_FORECAST.format(
            nam_duong=nam_duong,
            nam_can_chi=nam_can_chi,
            gioi_tinh=info["gioi_tinh"],
            cung_menh=menh["cung_menh"],
            cung_than=menh["cung_than"],
            cuc=menh["cuc"],
            dai_han_hien_tai=dai_han_hien_tai,
            luu_nien=luu_nien,
        )
