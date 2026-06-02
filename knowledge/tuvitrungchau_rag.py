"""
Trung Châu Phái Tử Vi Đẩu Số — RAG Knowledge Module
Nguồn: https://tuvitrungchau.com/ (Vương Đình Chi / Lục Bân Triệu / Trung Châu Phái)
"""

TRUNG_CHAU_KNOWLEDGE = []

def _add(category, topic, keywords, text):
    TRUNG_CHAU_KNOWLEDGE.append({
        "category": category,
        "topic": topic,
        "keywords": keywords,
        "text": text,
    })

# ===== 14 CHÍNH TINH =====

_add("chinh_tinh", "Tử Vi", ["tử vi", "tử vi tinh", "đế tọa", "bắc đẩu", "chư tinh chi thủ", "âm thổ", "quan lộc chủ"],
    "Tử Vi tinh (紫微星) là Bắc Đẩu tinh hệ chủ tinh, ngũ hành Âm Thổ, là Quan Lộc chủ. Trong hệ thống Tử Vi Đẩu Số, Tử Vi được gọi là 'đế tọa' — ngôi vua, là chư tinh chi thủ. Tử Vi có ba công năng đặc biệt: giải ách — hóa giải tai nạn, diên thọ — kéo dài tuổi thọ, và chế hóa — kiểm soát và chuyển hóa hung tinh. Cổ thư: 'Năng chế Hỏa Linh vi thiện, năng hóa Thất Sát vi quyền.' Cần Tả Phụ Hữu Bật đồng hành, nếu vô Phụ Bật thì là cô quân. Tử Vi không sợ sát tinh bằng thiếu cát tinh. Đắc Phủ Tướng Tả Hữu Xương Khúc cát tập, vô hữu bất quý.")

_add("chinh_tinh", "Tử Vi — 6 tổ hợp", ["tử vi", "tổ hợp", "đồng cung", "tử vi tham lang", "tử vi thiên tướng", "tử vi thất sát", "tử vi phá quân", "tử vi thiên phủ"],
    "Tử Vi có 6 tổ hợp đồng cung: (1) Tử Vi Độc Tọa (Tý/Ngọ) — được Phủ Tướng Triều Viên, Ngọ cung tốt hơn tạo 'Cực Hướng Ly Minh'; (2) Tử Vi Thiên Phủ (Dần/Thân) — Nam Bắc Đẩu tinh chủ hội tụ, chủ vinh hoa nhưng cô độc; (3) Tử Vi Tham Lang (Mão/Dậu) — Tử Vi gặp đào hoa tinh, tính chất phức tạp; (4) Tử Vi Thiên Tướng (Thìn/Tuất) — Tử Vi gặp phúc tinh, tính chất ôn hòa; (5) Tử Vi Thất Sát (Tỵ/Hợi) — 'Hóa sát vi quyền'; (6) Tử Vi Phá Quân (Sửu/Mùi) — phiên phúc, ái tắng quá phân minh.")

_add("chinh_tinh", "Thiên Cơ", ["thiên cơ", "thiên cơ tinh", "mưu tinh", "nam đẩu", "ất âm mộc", "cơ biến", "trí tuệ"],
    "Thiên Cơ tinh (天機星) là Nam Đẩu đệ tam tinh, ngũ hành Ất Âm Mộc, hóa khí vi 'Thiện', là Huynh Đệ chủ. Đại diện Khương Tử Nha. Chủ trí tuệ, mưu lược và cơ biến. Hóa khí vi Thiện — kế mưu cơ biến dùng vào chính đạo thì tốt, dùng vào tà đạo thì thành cơ quan quỷ trá. Bản tính: tư đa hành thiểu — nghĩ nhiều làm ít, du di bất định. Là nhân tài xí họa nghiên cứu. Ba tổ hợp: (1) Cơ Cự đồng lâm (Mão/Dậu); (2) Thiên Cơ Thái Âm (Dần/Thân); (3) Cơ Lương gia hội (Thìn/Tuất).")

_add("chinh_tinh", "Thiên Cơ — Tứ Hóa", ["thiên cơ", "tứ hóa", "hóa lộc", "hóa quyền", "hóa khoa", "hóa kỵ"],
    "Thiên Cơ với Tứ Hóa: Hóa Lộc — lao tâm lao thần, bất đắc an ninh; Hóa Quyền — tốt nhất, quyền biến có lực, mưu lược thành công; Hóa Khoa — thích hợp kế hoạch tài chính, nghiên cứu; Hóa Kỵ — rất bất lợi, lao tâm lao lực, trầm cảm.")

_add("chinh_tinh", "Thái Dương", ["thái dương", "thái dương tinh", "nhật tinh", "dương hỏa", "quan lộc chủ", "quang minh"],
    "Thái Dương tinh (太阳星) là Trung Thiên tinh chủ, Dương Hỏa, Quan Lộc chủ. Hóa khí vi 'Quý' — chủ quý hơn chủ phú. Đại biểu cho cha, chồng, con trai. Quang minh lỗi lạc, nhiệt tình, hào phóng, lợi tha hơn lợi kỷ. Miếu Vượng: Dần→Mùi (Nhật Xuất Phù Tang tại Mão, Nhật Lệ Trung Thiên tại Ngọ). Lạc Hãm: Thân→Sửu (lao lục bôn ba). Bốn tổ hợp: (1) Độc tọa; (2) Nhật Nguyệt đồng cung (Sửu/Mùi); (3) Cự Nhật đồng cung (Dần/Thân); (4) Dương Lương xương lộc (Mão/Dậu).")

_add("chinh_tinh", "Vũ Khúc", ["vũ khúc", "vũ khúc tinh", "tài tinh", "bắc đẩu", "âm kim", "cương nghị"],
    "Vũ Khúc tinh (武曲星) là Bắc Đẩu đệ lục tinh, Âm Kim, Tài Bạch chủ. Hóa khí vi 'Tài'. Đại diện Chu Vũ Vương. Tính cương quả quyết, tâm tính trực. Cương nghị quả đoán. Vũ Khúc chủ tài nhưng cũng chủ cô khắc lục thân. Năm tổ hợp đồng cung: (1) Vũ Khúc Độc Tọa (Thìn/Tuất) — tốt nhất; (2) Vũ Khúc Thiên Phủ (Tý/Ngọ) — ổn định; (3) Vũ Khúc Tham Lang (Sửu/Mùi) — 'Vũ Tham bất phát, thiếu niên nhân'; (4) Vũ Khúc Thiên Tướng (Dần/Thân); (5) Vũ Khúc Thất Sát (Mão/Dậu); (6) Vũ Khúc Phá Quân (Tỵ/Hợi) — đại khởi đại lạc.")

_add("chinh_tinh", "Thiên Đồng", ["thiên đồng", "thiên đồng tinh", "phúc tinh", "nam đẩu", "dương thủy", "phúc đức chủ"],
    "Thiên Đồng tinh (天同星) là Nam Đẩu đệ tứ tinh, Dương Thủy, hóa khí vi 'Phúc', Phúc Đức chủ. Đại diện Chu Văn Vương. Sao chủ phúc đức, hưởng thụ, an nhàn. 'Phúc bất phúc, yếu xem Tứ Hóa' — miếu vượng + cát tinh = phúc thọ song toàn; lạc hãm + sát tinh + Hóa Kỵ = phúc biến họa. Bản tính: ôn hòa, lương thiện, tùy hòa nhưng thiếu chí tiến thủ, lười biếng, ý chí bạc nhược. Ba tổ hợp: (1) Đồng Âm đồng cung (Tý/Ngọ); (2) Cự Đồng Sửu Mùi, tiên khổ hậu cam; (3) Đồng Lương tại Dần Thân, nhàn du phóng đãng.")

_add("chinh_tinh", "Liêm Trinh", ["liêm trinh", "liêm trinh tinh", "tù tinh", "bắc đẩu", "âm hỏa", "quan lộc", "đào hoa"],
    "Liêm Trinh tinh (廉貞星) là Bắc Đẩu đệ ngũ tinh, Âm Hỏa kiêm Mộc, hóa khí vi 'Tù', Quan Lộc chủ kiêm thứ đào hoa. Đại diện Phí Trọng. Một trong những chính tinh phức tạp nhất. Phân biệt: Liêm Trinh thanh — miếu vượng + cát tinh → thanh liêm chính trực; Liêm Trinh trọc — lạc hãm + sát tinh + đào hoa → tà dâm, tù ngục. Năm tổ hợp: (1) Liêm Trinh Thiên Phủ (Thìn/Tuất) — ổn định nhất; (2) Liêm Trinh Tham Lang (Tỵ/Hợi) — đào hoa nhất; (3) Liêm Trinh Thất Sát (Sửu/Mùi) — hung hiểm nhất 'lộ thượng mai thi'; (4) Liêm Trinh Thiên Tướng (Tý/Ngọ); (5) Liêm Trinh Phá Quân (Mão/Dậu).")

_add("chinh_tinh", "Thiên Phủ", ["thiên phủ", "thiên phủ tinh", "nam đẩu tinh chủ", "dương thổ", "khố tinh", "lệnh tinh"],
    "Thiên Phủ tinh (天府星) là Nam Đẩu tinh chủ, Dương Thổ, hóa khí vi 'Hiền Năng', Tài Bạch chủ kiêm Điền Trạch chủ. Đại diện Khương Hoàng Hậu. Biệt danh: 'lệnh tinh', 'tài khố tinh'. Tử Vi là đế tọa, Thiên Phủ là thừa tướng. Ổn trọng, bảo thủ, thiện tích trữ. Bản năng sưu tầm và tích trữ mạnh. Nguyên tắc 'Đắc lộc hiệp' — nếu được Lộc Tồn/Hóa Lộc hội chiếu → kho đầy, giàu bền. Gặp Không Kiếp → 'không kho', tài chính bất ổn. Ba tổ hợp: (1) Tử Phủ đồng cung (Dần/Thân); (2) Vũ Khúc Thiên Phủ (Tý/Ngọ) — đại phú bất động sản; (3) Liêm Trinh Thiên Phủ (Thìn/Tuất). Thiên Phủ không tham gia Tứ Hóa.")

_add("chinh_tinh", "Thái Âm", ["thái âm", "thái âm tinh", "nguyệt tinh", "âm thủy", "phú tinh", "trung thiên"],
    "Thái Âm tinh (太陰星) là Trung Thiên tinh, Âm Thủy, hóa khí vi 'Phú', Tài Bạch chủ kiêm Điền Trạch chủ. Là Mặt Trăng, đại biểu cho mẹ, vợ, con gái. 'Nhật chủ quý, Nguyệt chủ phú.' Miếu Vượng: Dậu, Tuất, Hợi (buổi tối trăng sáng). Hãm Địa: Mão, Thìn, Tỵ (ban ngày trăng mờ). Bản tính: ôn nhu, tinh tế, lãng mạn, cảm tính, giỏi nghệ thuật. Cách cục 'Nguyệt Lãng Thiên Môn' — Thái Âm tại Hợi, một trong những cách cục giàu nhất. Ba tổ hợp: (1) Nhật Nguyệt đồng cung (Sửu/Mùi); (2) Cơ Nguyệt (Dần/Thân); (3) Đồng Âm (Tý/Ngọ).")

_add("chinh_tinh", "Tham Lang", ["tham lang", "tham lang tinh", "đào hoa", "bắc đẩu", "dương mộc", "thiện ác đồng thể"],
    "Tham Lang tinh (貪狼星) là Bắc Đẩu đệ nhất tinh, Dương Mộc kiêm Thủy, đào hoa chủ. Hóa khí vi 'Đào Hoa'. Đại diện Đắc Kỷ. 'Tham Lang vi thiện ác đồng thể' — đa tài đa nghệ, giao tế quảng khoáng (mặt thiện); tham tài, tham sắc, tham danh (mặt ác). Đào hoa có ba tầng nghĩa: (1) nhân duyên đào hoa; (2) nghệ thuật đào hoa; (3) giao tế đào hoa. Cách cục Hỏa Tham/Linh Tham — Tham Lang + Hỏa Tinh/Linh Tinh → đột phát, bất ngờ phát đạt: 'Hỏa Linh Tham hội, danh trấn chư bang.'")

_add("chinh_tinh", "Cự Môn", ["cự môn", "cự môn tinh", "ám tinh", "bắc đẩu", "âm thủy", "thị phi", "khẩu thiệt"],
    "Cự Môn tinh (巨門星) là Bắc Đẩu đệ nhị tinh, Âm Thủy kiêm Thổ, hóa khí vi 'Ám'. Ám tinh — sao tối, chủ thị phi, khẩu thiệt, nghi ngờ. Đại diện Mã Thiên Quân. 'Cự Môn khai khẩu tiện thị phi' — mở miệng là thị phi. Vừa là nhược điểm (gây mâu thuẫn), vừa là ưu điểm (khẩu tài phi thường). Ba tổ hợp đồng cung: (1) Cơ Cự đồng lâm (Mão/Dậu) — giỏi ăn nói; (2) Cự Nhật đồng cung (Dần/Thân) — 'quan phong tam đại'; (3) Đồng Cự (Sửu/Mùi) — 'tiên khổ hậu cam'. Cách cục Thạch Trung Ẩn Ngọc — Cự Môn tại Tý độc tọa.")

_add("chinh_tinh", "Thiên Tướng", ["thiên tướng", "thiên tướng tinh", "ấn tinh", "nam đẩu", "dương thủy", "phụ trợ"],
    "Thiên Tướng tinh (天相星) là Nam Đẩu đệ ngũ tinh, Dương Thủy, hóa khí vi 'Ấn'. Ấn tinh — sao ấn tín, chủ phụ trợ, quản lý hành chính. Đại diện Văn Trọng. Đặc tính quan trọng nhất: Thụ Hiệp — bị ảnh hưởng mạnh từ hai cung kẹp hai bên, thiếu chủ kiến. Hai cách cục Giáp Ấn: (1) Tài Ấm Giáp Ấn (Đại Cát) — kẹp bởi Thiên Lương + Thiên Đồng → phú quý song toàn; (2) Hình Kỵ Giáp Ấn (Đại Hung) — kẹp bởi Liêm Trinh + Vũ Khúc mang Hóa Kỵ → hình ngục. Nghề: quản lý hành chính, ngân hàng, công chức.")

_add("chinh_tinh", "Thiên Lương", ["thiên lương", "thiên lương tinh", "ấm tinh", "thọ tinh", "nam đẩu", "dương thổ", "giải ách"],
    "Thiên Lương tinh (天梁星) là Nam Đẩu đệ nhị tinh, Dương Thổ, hóa khí vi 'Ấm'. Ấm tinh — sao che chở, bảo vệ, chủ giải ách. Còn gọi là 'Thọ tinh' — trường thọ. 'Phùng hung hóa cát' — gặp ách trước giải sau, 'tiên khổ hậu cam.' Chính trực, cương nghị, ghét tà gian. Tính 'lão' khí — dù trẻ nhưng phong thái già dặn. Thiên Lương tại Ngọ — 'Thiên Lương cư Ngọ vị, quan tư thanh hiển.' Ba tổ hợp: (1) Cơ Lương (Thìn/Tuất) — 'tất hữu cao nghệ tùy thân'; (2) Đồng Lương (Dần/Thân) — phúc ấm rất lớn; (3) Dương Lương (Mão/Dậu) — 'văn tú thiên hạ.'")

_add("chinh_tinh", "Thất Sát", ["thất sát", "thất sát tinh", "tướng tinh", "nam đẩu", "dương kim", "sát phạt", "quyền uy"],
    "Thất Sát tinh (七殺星) là Nam Đẩu đệ lục tinh, Dương Kim kiêm Hỏa, hóa khí vi 'Sát'. Tướng tinh — nguyên soái, chủ quyền uy và chiến đấu. Đại diện Hoàng Phi Hổ. Sát phạt quyết đoán. Kim kiêm Hỏa — vừa sắc bén vừa nóng bỏng. 'Sát vô chế hóa, tất thành hung.' Can đảm, mạo hiểm, thích chinh phục. 'Thất Sát cô tinh, lục thân duyên bạc.' Ba tổ hợp: (1) Tử Vi Thất Sát (Tỵ/Hợi) — 'Hóa sát vi quyền'; (2) Vũ Khúc Thất Sát (Mão/Dậu) — kinh doanh mạo hiểm; (3) Liêm Trinh Thất Sát (Sửu/Mùi) — 'lộ thượng mai thi' hung hiểm nhất.")

_add("chinh_tinh", "Phá Quân", ["phá quân", "phá quân tinh", "hao tinh", "bắc đẩu", "âm thủy", "phá hoại", "tái tạo"],
    "Phá Quân tinh (破軍星) là Bắc Đẩu đệ thất tinh, Âm Thủy, hóa khí vi 'Hao'. Hao tinh — sao tiêu hao, chủ phá hoại và tái tạo. Đại diện Trụ Vương. 'Tiên phá hậu lập' — cát tinh chế hóa → phá rồi xây; sát tinh → phá rồi trống. Phản nghịch, không chấp nhận hiện trạng. Phá Quân và Thiên Tướng luôn ở đối cung — trục 'phá hoại — ổn định'. Ba tổ hợp: (1) Tử Vi Phá Quân (Sửu/Mùi) — 'Anh tinh nhập miếu'; (2) Vũ Khúc Phá Quân (Tỵ/Hợi) — 'tài lai tài khứ'; (3) Liêm Trinh Phá Quân (Mão/Dậu) — kịch liệt, cuộc đời sóng gió.")

# ===== TỨ HÓA =====

_add("tu_hoa", "Tứ Hóa — Tổng quan", ["tứ hóa", "hóa lộc", "hóa quyền", "hóa khoa", "hóa kỵ", "tổng quan"],
    "Tứ Hóa — Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ — là bốn dạng biến đổi của tinh diệu, phản ánh xu hướng vận hành của mệnh bàn. Trong Trung Châu phái, Tứ Hóa không phải tinh diệu độc lập mà là trạng thái biến đổi của chính tinh — luận đoán phải xem tinh diệu nào mang hóa. Đặc điểm Trung Châu: (1) Tứ Hóa đa tầng — Bản Mệnh, Đại Hạn, Lưu Niên; (2) Tinh hệ hỗ thiệp; (3) Lục Thập Tinh Hệ — 14 chính tinh tạo 60 tổ hợp; (4) Xoay cung và đa tầng cung vị; (5) Phân biệt tiên thiên - hậu thiên.")

_add("tu_hoa", "Tứ Hóa — Bảng Trung Châu", ["tứ hóa", "bảng tứ hóa", "trung châu", "10 can"],
    "Bảng Tứ Hóa Trung Châu Phái: Giáp — Liêm Trinh Lộc, Phá Quân Quyền, Vũ Khúc Khoa, Thái Dương Kỵ. Ất — Thiên Cơ Lộc, Thiên Lương Quyền, Tử Vi Khoa, Thái Âm Kỵ. Bính — Thiên Đồng Lộc, Thiên Cơ Quyền, Văn Xương Khoa, Liêm Trinh Kỵ. Đinh — Thái Âm Lộc, Thiên Đồng Quyền, Thiên Cơ Khoa, Cự Môn Kỵ. Mậu — Tham Lang Lộc, Tham Lang Quyền, Hữu Bật Khoa, Thiên Cơ Kỵ. Kỷ — Vũ Khúc Lộc, Vũ Khúc Quyền, Thiên Lương Khoa, Văn Khúc Kỵ. Canh — Thái Dương Lộc, Thái Dương Quyền, Thiên Phủ Khoa, Thiên Đồng Kỵ. Tân — Cự Môn Lộc, Cự Môn Quyền, Văn Khúc Khoa, Văn Xương Kỵ. Nhâm — Thiên Lương Lộc, Tử Vi Quyền, Thiên Phủ Khoa, Vũ Khúc Kỵ. Quý — Phá Quân Lộc, Cự Môn Quyền, Thái Âm Khoa, Tham Lang Kỵ.")

_add("tu_hoa", "Hóa Lộc", ["hóa lộc", "cát hóa", "tài lộc", "cơ duyên", "hưởng thụ"],
    "Hóa Lộc (化祿) thuộc loại cát hóa — chủ tài lộc, cơ duyên, thuận lợi, hưởng thụ. Là hóa mạnh nhất trong Tứ Hóa. Ba bản chất: (1) Tài lộc — cung nào có Hóa Lộc thì kiếm tiền và giữ tiền lĩnh vực đó; (2) Nhân duyên — mang năng lượng hút người; (3) Hưởng thụ — gắn liền lạc thú, thoải mái. Hóa Lộc kỵ Hóa Kỵ đồng cung — 'Lộc phùng Kỵ, phú nhi bất lâu.' Trung Châu: 'Lộc tùy Kỵ đi' — Lộc đến đâu Kỵ theo đó. Hóa Lộc là lộc động (tiền đến rồi đi); Lộc Tồn là lộc tĩnh (tiền tích lũy).")

_add("tu_hoa", "Hóa Quyền", ["hóa quyền", "cát hóa", "quyền lực", "cương quyết", "kiểm soát"],
    "Hóa Quyền (化權) thuộc loại cát hóa — chủ quyền lực, cương quyết, kiểm soát, chủ động. Ba bản chất: (1) Cương quyết — quyết đoán trong lĩnh vực đó; (2) Kiểm soát — nhu cầu nắm giữ, kiểm soát; (3) Tăng cường — tăng lực cho chính tinh — sao mạnh càng oai, sao yếu được cứu. Trung Châu coi Hóa Quyền là phương tiện không phải mục đích. 'Quyền Kỵ giao chiến' — Quyền và Kỵ cùng nhập một cung tạo cục diện vừa mạnh vừa trở ngại. Quyền đơn độc → cương không có nền tảng, dễ phản ứng ngược.")

_add("tu_hoa", "Hóa Khoa", ["hóa khoa", "cát hóa", "danh tiếng", "học vấn", "thanh nhã"],
    "Hóa Khoa (化科) thuộc loại cát hóa — chủ danh tiếng, học vấn, thanh nhã, phong độ. Là hóa 'văn nhã nhất' trong Tứ Hóa. Ba bản chất: (1) Danh tiếng — được biết đến và tôn trọng; (2) Học vấn — trí tuệ, học hành, thi cử; (3) Phong độ — thanh nhã, lịch sự, trí thức. Tam Cát Hóa: Lộc + Quyền + Khoa hội tụ → cách cục cực tốt, phú quý song toàn. Khoa + Lộc → tiền tài đi kèm danh tiếng. Khoa đơn độc → có danh thiếu thực lực. Khoa sợ Hóa Kỵ cùng cung → danh tiếng bị tổn hại.")

_add("tu_hoa", "Hóa Kỵ", ["hóa kỵ", "hung hóa", "trở ngại", "thị phi", "chấp niệm", "tổn thất"],
    "Hóa Kỵ (化忌) là hung hóa — chủ trở ngại, thị phi, chấp niệm, tổn thất. Mang ý nghĩa 'chấp trước' — tập trung quá mức dẫn đến vừa trở ngại vừa chuyên sâu. Bốn bản chất: (1) Chấp niệm — không buông được lĩnh vực đó; (2) Thị phi khẩu thiệt — xung đột, hiểu lầm, kiện tụng; (3) Tổn thất và trì trệ. Trung Châu phân biệt Sinh Niên Tứ Hóa, Đại Vận Tứ Hóa, Lưu Niên Tứ Hóa. Xem Hóa Kỵ là 'trọng điểm' — cung có Kỵ là lĩnh vực cần tập trung xử lý. Tự Hóa Kỵ — chính tinh Hóa Kỵ tại chính cung → 'phá hao tự thân.' Nặng nhất: Bính Liêm Trinh Hóa Kỵ, Đinh Cự Môn Hóa Kỵ.")

# ===== CÁCH CỤC =====

_add("cach_cuc", "Sát Phá Lang", ["sát phá lang", "thất sát", "phá quân", "tham lang", "biến động", "tam hợp"],
    "Sát Phá Lang (杀破狼) là tên gọi chung của ba chủ tinh: Thất Sát, Phá Quân và Tham Lang. Ba sao luôn ở ba cung tam hợp. Được xem là then chốt của sự biến động. Cách cục tốt → 'động trung đắc tài giáng phúc.' Cách cục xấu → 'động trung phùng tai phá tài.' Ba kiểu biến động: Tham Lang — biến đổi trên bề mặt, bát diện linh lung; Thất Sát — biến đổi đột ngột, quật cường; Phá Quân — biến đổi cực đoan, 'tiên phá hậu thành.' Tham Lang hỷ Hóa Lộc, Hóa Quyền → hoành phát. Thất Sát hỷ Tử Vi → 'Hóa sát vi quyền.' Phá Quân hỷ Lộc → 'tiên phá hậu thành' có kết quả.")

_add("cach_cuc", "Tử Phủ Đồng Cung", ["tử phủ đồng cung", "tử vi", "thiên phủ", "dần", "thân", "đế vương"],
    "Tử Phủ Đồng Cung — Tử Vi và Thiên Phủ cùng ngự tại một cung. Chỉ xảy ra tại Dần và Thân. 'Tử Phủ đồng cung, chung thân phúc hậu.' Xếp vào hàng 'đế vương chi mệnh.' Tử Vi = Bắc Đẩu tinh chủ, chủ 'quý' (quyền lực). Thiên Phủ = Nam Đẩu tinh chủ, chủ 'lệnh' (chúng vọng). Mâu thuẫn nội tại: Tử Vi thiên kích tiến mạo hiểm, Thiên Phủ thiên bảo thủ. Phân biệt Dần vs Thân: Tử Phủ tại Dần — Tử Vi và Thiên Phủ hãm dễ nhãn cao thủ đê; Tử Phủ tại Thân — bình hòa hơn, khả tạo chi tài. Cần Tả Hữu thành đôi — nếu không trở thành cô quân.")

_add("cach_cuc", "Cơ Nguyệt Đồng Lương", ["cơ nguyệt đồng lương", "thiên cơ", "thái âm", "thiên đồng", "thiên lương", "lại nhân"],
    "Cơ Nguyệt Đồng Lương tác lại nhân — tính cách giống 'lại nhân', giỏi cơ biến, mưu lược, trường vu kế hoạch. Tổ hợp bốn sao: Thiên Cơ + Thái Âm + Thiên Đồng + Thiên Lương hội chiếu. Cách cục phúc đức điều hòa, thích hợp công việc liên quan kế hoạch, tài chính, nghiên cứu, giáo dục. Nhạy cảm với tác động của sát tinh và Tứ Hóa.")

_add("cach_cuc", "Phủ Tướng Triều Viên", ["phủ tướng triều viên", "thiên phủ", "thiên tướng", "phú quý"],
    "Phủ Tướng Triều Viên — Thiên Phủ và Thiên Tướng hội chiếu vào Mệnh. 'Phủ Tướng đồng lai hội Mệnh cung, toàn gia thực lộc' — phú quý, ổn định, con cháu đông đúc hưởng phúc.")

_add("cach_cuc", "Hỏa Tham Linh Tham", ["hỏa tham", "linh tham", "tham lang", "hỏa tinh", "linh tinh", "đột phát"],
    "Hỏa Tham — Tham Lang + Hỏa Tinh → đột phát, bất ngờ phát đạt. Linh Tham — Tham Lang + Linh Tinh → hoành phát, tài bất ngờ. 'Hỏa Linh Tham hội, danh trấn chư bang.' Thìn Tuất là thượng cách, Sửu Mùi là thứ cách.")

_add("cach_cuc", "Thạch Trung Ẩn Ngọc", ["thạch trung ẩn ngọc", "cự môn", "tý cung", "tiên khổ hậu cam"],
    "Thạch Trung Ẩn Ngọc — Cự Môn tại Tý cung độc tọa. Ngọc ẩn trong đá — tuổi trẻ bôn ba, trung niên bộc phát, về già thành công.")

_add("cach_cuc", "Nguyệt Lãng Thiên Môn", ["nguyệt lãng thiên môn", "thái âm", "hợi cung", "phú quý"],
    "Nguyệt Lãng Thiên Môn — Thái Âm tại Hợi cung. 'Nguyệt Lãng Thiên Môn tấn phú quý.' Một trong những cách cục giàu nhất trong Tử Vi Đẩu Số.")

# ===== CUNG MỆNH & THIÊN DI =====

_add("cung", "Cung Mệnh", ["cung mệnh", "mệnh", "tính cách", "bản thân", "luận đoán"],
    "Cung Mệnh là cung quan trọng nhất trong 12 cung. Đại diện bản thân — tính cách, năng lực, diện mạo, xu hướng cuộc đời. 'Mệnh Cung nãi nhân chi bổn, thập nhị cung chi chủ.' Phương pháp luận đoán: (1) Chính tinh tọa thủ — yếu tố quyết định nhất. Vô chính diệu → xem Thiên Di; (2) Phụ tinh đồng cung — Tả Hữu Khôi Việt Xương Khúc (cát), Kình Đà Hỏa Linh Không Kiếp (sát); (3) Tứ Hóa phi nhập; (4) Tam phương tứ chính: Mệnh + Thiên Di + Tài Bạch + Quan Lộc. Mệnh = bản ngã nội tại. Thiên Di = hình ảnh bên ngoài.")

_add("cung", "Cung Thiên Di", ["cung thiên di", "thiên di", "xuất ngoại", "giao tiếp", "xã hội", "đối cung"],
    "Cung Thiên Di chủ quản hoạt động bên ngoài — giao tiếp xã hội, xuất ngoại, di chuyển, cách người khác nhìn nhận. Là cung đối chiếu của Mệnh. Phương pháp luận đoán: (1) Chính tinh tọa thủ; (2) Phụ tinh đồng cung; (3) Tứ Hóa phi nhập; (4) Tam phương tứ chính: Thiên Di + Mệnh + Phu Thê + Phúc Đức. Mối quan hệ Mệnh-Thiên Di: hỗ tương, bổ khuyết (Mệnh vô chính diệu → lấy Thiên Di làm chủ), nội ngoại (Mệnh = bản ngã, Thiên Di = hình ảnh bên ngoài).")

# ===== SO SÁNH TRUNG CHÂU VỚI CÁC PHÁI =====

_add("phai", "Trung Châu vs Tam Hợp vs Phi Tinh", ["trung châu", "tam hợp", "phi tinh", "so sánh", "khác biệt"],
    "Phái Trung Châu (中州派) có hệ thống Tứ Hóa riêng biệt. So sánh: Trung Châu trọng tinh hệ hỗ thiệp + tiên hậu thiên biến hóa, bảng Tứ Hóa khác biệt can Canh/Mậu/Nhâm, chú trọng bản chất tinh diệu. Tam Hợp trọng cung tam hợp + miếu vượng lạc hãm, dễ học nền tảng vững. Phi Tinh trọng phi hóa liên cung, chi tiết quan hệ cung. Tứ Hóa đa tầng là cốt lõi của Trung Châu — kết hợp Tứ Hóa với tinh hệ hỗ thiệp, phân tích Bản Mệnh + Đại Hạn + Lưu Niên. Toàn bộ hệ thống được Vương Đình Chi hệ thống hóa qua Lục Thập Tinh Hệ (60 tổ hợp).")

_add("phai", "Xoay cung Trung Châu", ["xoay cung", "đa tầng cung vị", "trung châu", "phương pháp"],
    "Xoay cung và đa tầng cung vị — lấy một cung bất kỳ làm Mệnh cung mới để phân tích góc nhìn khác. Ví dụ: muốn xem tài chính của vợ/chồng, lấy Phu Thê làm Mệnh rồi xoay tìm Tài Bạch. Đây là kỹ thuật đặc trưng của Trung Châu phái.")

# ===== LỊCH SỬ & PHƯƠNG PHÁP =====

_add("lich_su", "Lịch sử Tử Vi Đẩu Số", ["lịch sử", "nguồn gốc", "trần đoàn", "khâm thiên giám", "trung châu", "vương đình chi"],
    "Tử Vi Đẩu Số do Trần Đoàn (Trần Hy Di) sáng tạo cuối thời Ngũ Đại. Kết hợp và cải tiến từ Cầm Đường Ngũ Tinh thuật và Thập Bát Phi Tinh. Bắc phái dùng thập bát phi tinh + Tử Vi. Nam phái định Tử Vi rồi bố trí Bắc Đẩu thất tinh + Nam Đẩu thất chủ tinh. Du nhập vào Việt Nam khoảng 1257 (thời Trần) qua tiến sĩ Hoàng Bính. Sau 1949 tài liệu theo dòng di cư vào Đài Loan. Thập niên 1970-1980 bùng nổ tại HK và Đài Loan. Hình thành các phái: Tam Hợp, Phi Tinh, Trung Châu (do Vương Đình Chi công khai).")

_add("lich_su", "Phương pháp học Tử Vi", ["phương pháp", "học tập", "lộ trình", "nền tảng"],
    "Phương pháp học Tử Vi — lộ trình: (1) Nền tảng — Âm Dương Ngũ Hành, Thiên Can Địa Chi, 12 cung; (2) Giai đoạn 1 — làm quen lá số, lập lá số, hiểu cấu trúc; (3) Giai đoạn 2 — nghiên cứu 14 chủ tinh (50% nền tảng); (4) Giai đoạn 3 — hiểu Tứ Hóa, linh hồn Tử Vi Đẩu Số; (5) Thực hành — luận đoán lá số người thân; (6) Nâng cao — Tứ Hóa đa tầng, tinh hệ hỗ thiệp, tiên hậu thiên biến hóa.")
