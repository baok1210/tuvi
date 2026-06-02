"""RAG entries from Bắc Phái Tứ Hóa books (PDF extracts)."""
# Sources:
#   1. Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn (55 trang)
#   2. Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn (134 trang)
#   3. Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa (127 trang)

BAC_PHAI_DATA = [
    # ── 1. THẬP CAN HÓA KHÍ ──────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Thập can hóa khí - Bảng can Lộc Quyền Khoa Kỵ",
        "keywords": ["thập can hóa khí", "bảng can hóa", "can lộc quyền khoa kỵ", "tứ hóa năm sinh", "canh dương vũ âm đồng"],
        "text": "Bảng Thập Can Tứ Hóa theo Khâm Thiên Môn, Trung Châu Vương Đình Chi, Tam Hợp Tử Vân, Hà Lạc Phương Ngoại Nhân, Hà Lạc Bắc Phái, Lương Thị Phi Tinh, Khâm Thiên Vô Cực Môn:\n"
               "Giáp: Liêm Trinh Lộc, Phá Quân Quyền, Vũ Khúc Khoa, Dương Kỵ\n"
               "Ất: Thiên Cơ Lộc, Thiên Lương Quyền, Tử Vi Khoa, Thái Âm Kỵ\n"
               "Bính: Thiên Đồng Lộc, Thiên Cơ Quyền, Văn Xương Khoa, Liêm Trinh Kỵ\n"
               "Đinh: Thái Âm Lộc, Thiên Đồng Quyền, Thiên Cơ Khoa, Cự Môn Kỵ\n"
               "Mậu: Tham Lang Lộc, Thái Âm Quyền, Hữu Bật Khoa, Thiên Cơ Kỵ\n"
               "Kỷ: Vũ Khúc Lộc, Tham Lang Quyền, Thiên Lương Khoa, Văn Khúc Kỵ\n"
               "Canh: Thái Dương Lộc, Vũ Khúc Quyền, Thái Âm Khoa, Thiên Đồng Kỵ\n"
               "Tân: Cự Môn Lộc, Thái Dương Quyền, Văn Khúc Khoa, Văn Xương Kỵ\n"
               "Nhâm: Thiên Lương Lộc, Tử Vi Quyền, Tả Phù Khoa, Vũ Khúc Kỵ\n"
               "Quý: Phá Quân Lộc, Cự Môn Quyền, Thái Âm Khoa, Tham Lang Kỵ\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 4]",
    },
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Can Canh - Sự thống nhất giữa các môn phái",
        "keywords": ["can canh", "canh dương vũ âm đồng", "tứ hóa can canh", "bất đồng can canh", "tam hợp tứ hóa"],
        "text": "Vấn đề can Canh: Nhiều nơi có sự bất đồng về Tứ Hóa của can Canh, nhưng các môn phái lớn như: Khâm Thiên Môn, Trung Châu Vương Đình Chi, Tam Hợp Tử Vân, Hà Lạc Phương Ngoại Nhân, Hà Lạc Bắc Phái đại lục (Sở Thiên Vân Khoát), Lương Thị Phi Tinh, Khâm Thiên Vô Cực Môn (Ông Phúc Dụ) đều dùng: Canh Dương Vũ Âm Đồng (Thái Dương Lộc, Vũ Khúc Quyền, Thái Âm Khoa, Thiên Đồng Kỵ). Cho nên không cần thiết phải tranh luận về vấn đề này.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 4]",
    },
    # ── 2. PHI PHỤC ĐOẠN QUYẾT ──────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Phi Phục đoạn quyết - Phương pháp luận vận hạn",
        "keywords": ["phi phục", "phi hóa", "phi phục đoạn quyết", "tiên thiên phi phục", "đại vận phi phục", "lưu niên phi phục", "ứng kỳ"],
        "text": "Phi phục là phi hóa Lộc Quyền Khoa Kỵ từ tiên thiên (lá số gốc) xuống đại vận, từ đại vận xuống lưu niên, từ lưu niên xuống lưu nguyệt, từ lưu nguyệt xuống lưu nhật, từ lưu nhật xuống lưu thời và chờ đợi thời gian đi qua đó để ứng kỳ. Đây là phương pháp luận vận hạn cốt lõi của Tứ Hóa Bắc Phái: dùng thiên can của từng cung để phi hóa, xem Lộc đến đâu (tốt), Kỵ đến đâu (xấu), và chờ đúng đại vận/lưu niên đến cung đó thì ứng kỳ.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 4-6]",
    },
    # ── 3. NHẤT LỤC CỘNG TÔNG / NHẤT KỴ TAM ĐIỂM ──────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Nhất Lục Cộng Tông và Nhất Kỵ Tam Điểm",
        "keywords": ["nhất lục cộng tông", "nhất kỵ tam điểm", "xung 6 thì 1 chết", "hà đồ lạc thư", "tam điểm", "kỵ phổ"],
        "text": "Nhất Lục Cộng Tông là kiến thức của Hà Đồ Lạc Thư được dùng trong nhiều môn phái Tử Vi. Ứng dụng quan trọng là Nhất Kỵ Tam Điểm (còn gọi là Xung 6 thì 1 chết): Khi một điểm tọa Kỵ sẽ ảnh hưởng tới điểm xung là đối cung (6) và điểm nhất lục cộng tông với nó chính là điểm (1). Do vậy 1 Kỵ sẽ có 3 điểm ảnh hưởng:\n"
               "(1) Điểm tọa Kỵ - mạnh nhất\n"
               "(2) Đối cung (xung) - mạnh thứ hai\n"
               "(3) Nhất Lục Cộng Tông - mạnh thứ ba\n"
               "Ví dụ: Đại vận Tài Bạch can Tân làm Văn Xương hóa Kỵ, theo Nhất Kỵ Tam Điểm làm cung Mùi tụ tập 2 Kỵ (của Tài tiên thiên và Tài đại vận).\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 6-9]",
    },
    # ── 4. TỰ HÓA HƯỚNG TÂM & LY TÂM ────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tự Hóa Ly Tâm",
        "keywords": ["tự hóa ly tâm", "ly tâm", "bài xích", "tự hóa", "nội bộ bài xích"],
        "text": "Tự Hóa Ly Tâm: Can cung làm cho tinh diệu trong chính cung đó tự hóa Lộc/Quyền/Khoa/Kỵ. Lực bài xích đối với các vị trí Lộc Quyền Khoa Kỵ năm sinh và vị trí đối cung của tự hóa đó. Ví dụ: Tự hóa Ly Tâm Khoa tại Mão sẽ có lực bài xích đối với Khoa năm sinh tại Ngọ và đối cung tại Dậu. Nếu Mệnh tại Ngọ, tự hóa ly tâm Khoa tại cung Tử Nữ, thì có thể luận là Tử Nữ (con cái, đối tác) bài xích Mệnh và Điền - con cái rời nhà, học sinh chuyển trường, cổ đông rút vốn.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 4]",
    },
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tự Hóa Hướng Tâm",
        "keywords": ["tự hóa hướng tâm", "hướng tâm", "tụ lực", "tự hóa", "nội bộ tụ hợp"],
        "text": "Tự Hóa Hướng Tâm: Can cung làm cho tinh diệu ở đối cung hóa Lộc/Quyền/Khoa/Kỵ, tức là lực tụ về đối cung. Đây là loại tụ lực đối với các cung vị Lộc Quyền Khoa Kỵ năm sinh và vị trí đối cung của cung tự hóa đó. Ví dụ: cung Dậu có tự hóa hướng tâm Khoa, thì tụ lực đối với Khoa năm sinh tại Ngọ và đối cung Mão. Nếu Ngọ là Mệnh, Điền Trạch nhập Khoa vào Tử Nữ, tụ hợp Mệnh-Điền-Tử 3 cung, có thể luận như đem công ty, phòng ở giao cho tử nữ hoặc cổ đông.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 5]",
    },
    # ── 5. LAI NHÂN CUNG ─────────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Lai Nhân Cung - Khái niệm và ứng dụng",
        "keywords": ["lai nhân cung", "thiên can năm sinh", "nhân duyên quá khứ", "nguyên thần cung", "gen"],
        "text": "Lai Nhân Cung là cung nơi thiên can năm sinh tọa lạc. Đây là đặc trưng riêng của phái Khâm Thiên, khác biệt với các phái khác. Lai Nhân Cung thể hiện nhân duyên chưa hoàn tất từ kiếp trước, là con đường của nhân duyên quá khứ. Ví dụ: mệnh chủ sinh năm Đinh Dậu, Lai Nhân Cung là cung Tài Bạch (Đinh tại Mùi). Nguyên Thần Cung là cung Phu Thê (Kỷ Dậu). Cả hai cung này rất quan trọng, được gọi là vị trí gen.\n\n"
               "Quy tắc chọn: Nếu thiên can giống nhau ở Tý và Dần (ví dụ Nhâm Tý và Nhâm Dần), ưu tiên chọn Dần hoặc Mão (vì Tý khai thiên, Sửu bộc địa, nhân sinh tại Dần).\n\n"
               "Lai Nhân Cung là chốt khởi động trung tâm cuộc đời, những sự kiện để lại ấn tượng sâu sắc thường xuất hiện ở hai cung Lai Nhân và Nguyên Thần.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa, trang 8-9; Khâm Thiên Tứ Hóa Nội Truyền, trang 17]",
    },
    # ── 6. CUNG VỊ HOÁN CHUYỂN ──────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Cung vị hoán chuyển (Lập Thái Cực)",
        "keywords": ["cung vị hoán chuyển", "lập thái cực", "hoán chuyển", "phi cung", "thể dụng"],
        "text": "Cung vị hoán chuyển là kỹ thuật lấy một cung bất kỳ làm trung tâm (lập Thái Cực) để xem xét sự việc liên quan đến cung đó. Ví dụ: để xem kết hôn, lập cực cung Phu Thê - lấy Phu Thê tiên thiên phi phục để xem Lộc/Kỵ. Để xem cha mất, lập cực Phụ Mẫu, xem Tật của Phụ Mẫu. Đây là kỹ thuật căn bản khi luận từng sự kiện cụ thể trong Tứ Hóa Bắc Phái: muốn xem việc gì thì lấy cung đại diện cho việc đó làm Thái Cực, rồi phi hóa từ cung đó.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 19]",
    },
    # ── 7. TỨ HÓA NĂM SINH & PHI CUNG TỨ HÓA ────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tứ Hóa năm sinh và Phi cung tứ hóa",
        "keywords": ["tứ hóa năm sinh", "phi cung tứ hóa", "tiên thiên định số", "hậu thiên biến số", "lai nhân cung phi hóa"],
        "text": "Tứ hóa năm sinh (Sinh niên tứ hóa): Thiên can năm sinh sinh ra hóa khí tác dụng, khiến tính chất của 4 tinh diệu sản sinh biến hóa, tức là tiên thiên định số. Ví dụ: can Đinh tứ hóa: Thái Âm hóa Lộc, Thiên Đồng Quyền, Thiên Cơ Khoa, Cự Môn Kỵ.\n\n"
               "Phi cung tứ hóa: 12 cung đều sở hữu thiên can, cũng có thể dùng các tinh diệu của các cung vị dựa vào thiên can phi hóa mà sản sinh biến hóa, là hậu thiên biến số. Ví dụ: cung Mệnh can Mậu: Tham Lang phi hóa Lộc nhập Tử Nữ; Thái Âm Quyền nhập Tài Bạch; Hữu Bật Khoa nhập Phúc Đức; Thiên Cơ Kỵ nhập Quan Lộc.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 3]",
    },
    # ── 8. LỘC NHÂN KỴ QUẢ ──────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Lộc Nhân Kỵ Quả - Nguyên lý nhân quả trong Tứ Hóa",
        "keywords": ["lộc nhân kỵ quả", "lộc là nhân", "kỵ là quả", "nhân quả tứ hóa", "lộc trước kỵ sau"],
        "text": "Lộc Nhân Kỵ Quả là nguyên lý: Lộc là Nhân (duyên khởi), Kỵ là Quả (kết cục). Trong luận giải: Lộc cho biết duyên lành đến từ đâu (cơ hội, tài lộc, tình duyên), Kỵ cho biết kết quả cuối cùng hoặc vấn đề cần trả giá. Khi xem một cung, nhìn Lộc trước để biết 'nhân', nhìn Kỵ sau để biết 'quả'. Nếu Lộc và Kỵ đồng cung thì hoặc là hưởng Lộc rồi trả Kỵ (tốt hóa xấu) hoặc là trong xấu có tốt.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 115]",
    },
    # ── 9. NAM NỮ TINH ────────────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Nam Nữ Tinh - Phân biệt và ứng dụng",
        "keywords": ["nam tinh", "nữ tinh", "nam nữ tinh", "phân biệt nam nữ", "dương tinh", "âm tinh"],
        "text": "Trong Khâm Thiên Tứ Hóa, các sao được phân làm Nam Tinh và Nữ Tinh để xem xét về hôn nhân, tình cảm, đào hoa. Nam Tinh đại diện cho đàn ông, Nữ Tinh đại diện cho phụ nữ. Khi xem hôn nhân, nếu mệnh chủ nữ có nhiều Nam Tinh nhập mệnh hoặc phu thê thì dễ có duyên với đàn ông, hoặc bản thân có tính cách nam tính. Ngược lại, mệnh chủ nam có nhiều Nữ Tinh thì dễ gần gũi phụ nữ.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 16]",
    },
    # ── 10. PHÁ TƯỢNG THẦN CÔNG ──────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Phá tượng thần công - Phá giải tượng xấu",
        "keywords": ["phá tượng thần công", "phá tượng", "hóa giải", "tượng xấu", "kỵ được hóa giải"],
        "text": "Phá tượng thần công là kỹ thuật phá giải các tượng xấu trên lá số. Khi một cung có Kỵ nhưng có thêm các yếu tố như: Lộc tồn, Kình Dương, Đà La, hoặc Tự Hóa hóa giải, thì tượng Kỵ có thể được phá bớt hoặc chuyển hóa. Có 3 mức độ: (1) Kỵ nhẹ bị hóa giải hoàn toàn, (2) Kỵ trung bình bị giảm, (3) Kỵ nặng không thể phá. Cần xem tinh diệu và tổ hợp sao để đánh giá.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 104]",
    },
    # ── 11. KỴ TINH KỲ PHỔ ──────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Kỵ tinh kỳ phổ - Các cấp độ Kỵ",
        "keywords": ["kỵ tinh kỳ phổ", "kỵ phổ", "kỵ tinh", "phổ kỵ", "cấp độ kỵ"],
        "text": "Kỵ tinh kỳ phổ là lý thuyết phân loại các dạng Kỵ: Kỵ năm sinh, Kỵ phi hóa, Tự Hóa Kỵ, Kỵ trùng điệp, Kỵ song tinh. Mỗi dạng Kỵ có mức độ ảnh hưởng khác nhau:\n"
               "- Kỵ năm sinh: nặng nhất, ảnh hưởng suốt đời\n"
               "- Kỵ phi hóa: xảy ra theo từng cung/vận, nhẹ hơn\n"
               "- Tự Hóa Kỵ: do nội bộ cung gây ra, chủ động hoặc bị động\n"
               "- Kỵ trùng điệp (chồng Kỵ): cung có 2 Kỵ trở lên, rất nặng\n"
               "- Kỵ song tinh: hai sao cùng hóa Kỵ trong một cung\n"
               "Khi có Kỵ trùng điệp cần xem ngay cung đối và cung Nhất Lục để đánh giá toàn diện.\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 107]",
    },
    # ── 12. KÍNH TÂM QUYẾT ──────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Kính Tâm Quyết - Tâm pháp then chốt",
        "keywords": ["kính tâm quyết", "tâm pháp", "kính tâm", "khẩu quyết", "bí quyết tứ hóa"],
        "text": "Kính Tâm Quyết là tâm pháp quan trọng trong Khâm Thiên Tứ Hóa, là khẩu quyết truyền miệng giúp người học nắm bắt nhanh trọng tâm khi luận giải. Nội dung cốt lõi: Lộc định duyên khởi, Kỵ định kết cục; Quyền là quá trình hành động; Khoa là danh nghĩa, kỹ năng. Khi xem một cung, hỏi 4 câu: (1) Duyên từ đâu? (Lộc), (2) Kết cục ra sao? (Kỵ), (3) Hành động thế nào? (Quyền), (4) Danh nghĩa gì? (Khoa).\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn, trang 102]",
    },
    # ── 13. TAM TÀI HỌC ──────────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tam Tài Học - Thiên Địa Nhân trong Tứ Hóa",
        "keywords": ["tam tài", "tam tài học", "thiên địa nhân", "tam bàn", "thiên bàn", "địa bàn", "nhân bàn"],
        "text": "Tam Tài Học (Thiên Địa Nhân) là nguyên lý nền tảng của Tứ Hóa Bắc Phái:\n"
               "- Cách 1: Lá số gốc là Thiên bàn; Đại vận là Địa bàn; Lưu niên là Nhân bàn. Sự kiện phải hội đủ cả 3 bàn (Thiên phi phục xuống Địa, Địa phi phục xuống Nhân) mới ứng.\n"
               "- Cách 2: Cung Lai Nhân là Thiên; cung Mệnh là Nhân; cung...\n"
               "- Cách 3: Phi tinh từ tiên thiên xuống đại vận, từ đại vận xuống lưu niên là quá trình 'Thiên Địa Nhân giao cảm'.\n"
               "Phương pháp ứng kỳ tam bàn: Một sự kiện lớn phải được báo trước từ tiên thiên (Thiên), xác nhận ở đại vận (Địa), và ứng nghiệm ở lưu niên (Nhân).\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa; Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn]",
    },
    # ── 14. TAM TƯỢNG NHẤT VẬT ──────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tam Tượng Nhất Vật - Định cát hung",
        "keywords": ["tam tượng nhất vật", "đơn tượng bất thành vật", "song tượng thành vật", "tam tượng", "cát hung"],
        "text": "Tam Tượng Nhất Vật: Đơn tượng không thành vật (một Lộc/Kỵ đơn lẻ chưa thể luận cát hung); Song tượng thành vật (hai tượng kết hợp mới thành sự). Khi có đủ Tam tượng (Lộc-Quyền-Khoa hoặc Lộc-Quyền-Kỵ...) trên cùng một vật (cùng tinh diệu) mới định được cát hung rõ ràng.\n\n"
               "Ví dụ: Đơn tượng - Lộc năm sinh tọa ở đâu đó nhưng chưa kết luận được; Song tượng - cung Phu Thê có Khoa (C) và tự hóa Khoa (C) - đã có 2 điểm; Tam tượng - Năm sinh Lộc (M) + tự hóa Khoa (C) + vật là Thiên Cơ - lúc này có thể định cát hung.\n\n"
               "Quyền Kỵ xem cát hung: Duyên khởi là bắt đầu (Lộc), duyên diệt là kết thúc (Kỵ). Lộc là duyên, Quyền là nghiệp, Khoa là tình, Kỵ là quả.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa]",
    },
    # ── 15. ĐÀO HOA ──────────────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Đào hoa - Phân tích tình cảm",
        "keywords": ["đào hoa", "tình cảm", "hoa tình", "đào hoa kiếp", "đào hoa sát", "chung thân đào hoa cách"],
        "text": "Đào hoa trong Tứ Hóa:\n"
               "- Các sao đào hoa: Tham Lang, Đào Hoa, Liêm Trinh, Văn Xương, Văn Khúc, Thai Tọa, Hồng Loan, Thiên Hỉ, Thiên Diêu, Hỏa Tinh\n"
               "- Đào Hoa Kiếp (桃花劫): Đào hoa tinh có Hóa Lộc nhưng bị Hóa Kỵ xung; Phụ-Bật ở Phu Thê cung; Đào hoa tinh ở Tử Nữ cung có Hóa Lộc và Hóa Kỵ\n"
               "- Đào Hoa Sát (桃花煞): Tham Lang gặp Kình Dương, Đà La, Thiên Hình, Thiên Khốc, Thiên Hư; Lưu Niên hoặc Đại Hạn Tử Nữ cung xung Mệnh\n"
               "- Chung Thân Đào Hoa Cách (终身桃花格): Đào hoa tinh nhập Mệnh/Phu Thê/Tử Nữ; có sao đào hoa và Hóa Lộc\n"
               "Cung vị liên quan: Tử Nữ làm trung tâm; Tử-Điền tuyến; Nhất Lục cộng tông của Tử Nữ; Quan Lộc cung và Phu-Quan tuyến.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa]",
    },
    # ── 16. BỆNH TẬT ─────────────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Luận bệnh tật qua Tứ Hóa và Ngũ Hành",
        "keywords": ["bệnh tật", "tật ách", "sức khỏe", "ngũ hành bệnh", "bệnh phụ khoa", "bệnh tứ hóa"],
        "text": "Luận bệnh tật trong Khâm Thiên:\n"
               "- Ngũ hành ứng với tạng phủ: Hỏa (Tim, tiểu tràng, thần kinh); Mộc (Gan, nội tiết, mắt); Thổ (Tiêu hóa, tỳ vị); Thủy (Thận, bài tiết, sinh dục); Kim (Phổi, đại tràng, hô hấp)\n"
               "- Địa chi ứng với cơ thể: Tý (bàng quang), Dần (mật), Mão (gan), Tỵ (tim), Ngọ (ruột non), Thân (đại tràng), Tuất (mệnh môn-thận phải), Hợi (đầu)\n"
               "- Các tình huống tai nạn: (1) Tật ách tự hóa Kỵ; (2) Sa xung hướng tâm Kỵ; (3) Song kỵ đồng cung; (4) Tuyến Phá Thể (Kỵ tại Mệnh + Kỵ tại Tật)\n"
               "- Xem bệnh: xem Tật Ách có Kỵ (năm sinh/phi hóa/tự hóa), kết hợp ngũ hành của tinh diệu để luận bệnh. Ví dụ: Tham Lang (Mộc) hóa Kỵ có thể luận bệnh gan; Liêm Trinh (Hỏa) hóa Kỵ luận bệnh tim mạch.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa]",
    },
    # ── 17. 18 SAO CHÍNH KHÂM THIÊN ──────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Hệ thống 18 sao chính của Khâm Thiên",
        "keywords": ["18 sao", "hệ tử vi", "hệ thiên phủ", "tam đẩu", "sao chính khâm thiên"],
        "text": "Khâm Thiên Đẩu Số chỉ dùng 18 sao chính, chia làm hai hệ: Nhật (Mặt Trời) - hệ Tử Vi (6 sao) và hệ Thiên Phủ (8 sao); Nguyệt (Mặt Trăng) - Thập Thiên Can; Ngũ Uẩn Giáp và Trần Sắc Thân do Tả Phù, Hữu Bật, Văn Xương, Văn Khúc tạo ra. Các sao được an vào các cung theo An Tinh Quyết.\n\n"
               "Phân loại sao: (1) Chính tinh 14 sao; (2) Phụ tinh (Tả Hữu, Xương Khúc, Kình Đà, Hỏa Linh, v.v.)\n"
               "Khái niệm Tam Đẩu: (1) Tử Vi Đẩu, (2) Thiên Phủ Đẩu, (3) Thập Thiên Can Đẩu\n\n"
               "Hệ Tử Vi (6 sao): Tử Vi, Thiên Cơ, Thái Dương, Vũ Khúc, Thiên Đồng, Liêm Trinh.\n"
               "Hệ Thiên Phủ (8 sao): Thiên Phủ, Thái Âm, Tham Lang, Cự Môn, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa]",
    },
    # ── 18. SONG TINH TỔ HỢP ────────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Song Tinh tổ hợp trong Tứ Hóa",
        "keywords": ["song tinh", "tổ hợp sao", "sao đồng cung", "tinh diệu tổ hợp"],
        "text": "Song Tinh tổ hợp là hai sao cùng tọa tại một cung, tạo nên ý nghĩa đặc biệt:\n"
               "- Tử Phủ đồng cung: Quyền uy và phúc lộc, nhưng cố chấp\n"
               "- Cơ Nguyệt đồng cung: Mưu lược và tài năng (Cơ Nguyệt đồng lương cách)\n"
               "- Dương Lương đồng cung: Tài năng và phúc đức (Dương Lương Xương Khúc hội)\n"
               "- Đồng Lương đồng cung: Phúc tinh nhưng dễ dựa dẫm\n"
               "- Sát Phá Tham: Cách động, dễ thay đổi (Sát Phá Lang)\n"
               "- Sát Phá đồng cung: Phá cách mạnh, thường có biến cố lớn\n"
               "- Tướng Ấn đồng cung (Thiên Tướng + Tả Hữu): Quyền lực phụ tá\n"
               "- Nhật Nguyệt đồng cung (Thái Dương + Thái Âm): Sáng suốt nhưng dao động\n"
               "[Nguồn: Khâm Thiên Tứ Hóa Nội Truyền Sơ Cấp - Chiến Nguyễn]",
    },
    # ── 19. TỨ HÓA THỰC CHIẾN: MỆNH LỆ KẾT HÔN 1 ─────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Kết hôn (Âm nữ 2/11/1983 giờ Dần)",
        "keywords": ["mệnh lệ kết hôn", "kết hôn tứ hóa", "lập cực phu thê", "phi phục phu thê", "ứng kỳ kết hôn"],
        "text": "Âm nữ sinh 2/11/1983 dương lịch (28/9/1983 âm) giờ Dần. Sự kiện: Kết hôn năm 2020.\n"
               "Luận giải:\n"
               "1. Phu Thê tiên thiên can Mậu → Tham Lang hóa Lộc phi phục tại đại vận 33 tuổi → báo hiệu đại vận này khả năng rất cao có Lộc Phu Thê (có thể kết hôn)\n"
               "2. Phu Thê đại vận 33 can Tân → Cự Môn hóa Lộc phi phục tại Tý → chờ năm Tý tới thì ứng hạn Lộc Phu Thê\n"
               "→ Kết hôn năm 2020 (Canh Tý).\n"
               "Kết luận: Qua việc lập cực Phu Thê tiên thiên ứng xuống Phu Đại vận, Phu Thê đại vận ứng ở Lưu niên, thấy rõ nguyên nhân vì sao cưới năm 2020.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 10-13]",
    },
    # ── 20. TỨ HÓA THỰC CHIẾN: MỆNH LỆ PHÁ TÀI ────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Phá tài (Nam)",
        "keywords": ["mệnh lệ phá tài", "phá tài", "tài bạch kỵ", "thiên cơ kỵ", "nhất kỵ tam điểm tài bạch"],
        "text": "Nam (không rõ năm). Sự kiện: Năm 2019 phá tài.\n"
               "Luận giải:\n"
               "1. Tiên thiên Tài Bạch can Mậu → Thiên Cơ hóa Kỵ → chờ đại hạn 53 tới ứng hạn → báo hiệu đại hạn này dễ có tổn thất về tài\n"
               "2. Đại vận 53 Tài Bạch can Tân → Văn Xương hóa Kỵ → theo Nhất Kỵ Tam Điểm, làm cung Mùi tụ tập 2 Kỵ (của Tài tiên thiên và Tài đại vận)\n"
               "3. Năm 2019 Tài Lưu Niên tại cung Mùi → vừa lúc ứng hạn → phá tài.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 14-18]",
    },
    # ── 21. TỨ HÓA THỰC CHIẾN: MỆNH LỆ BỐ MẤT ─────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Bố mất (giờ Mão 19/6/2020)",
        "keywords": ["mệnh lệ bố mất", "phụ mẫu kỵ", "thiên đồng hóa kỵ", "tật phụ mẫu"],
        "text": "Sự kiện: Bố mất vào giờ Mão ngày 19/06/2020 dương (28/04/2020 âm lịch).\n"
               "Luận giải:\n"
               "1. Phụ Mẫu can Canh → Thiên Đồng hóa Kỵ → phi phục Nhất Kỵ Tam Điểm vào cung Tuất và Hợi → đợi đại vận 15 khi Đại vận tại Tuất và Phụ Mẫu đại vận tại Hợi thì ứng hạn\n"
               "2. Phụ Mẫu đại vận can Tân → Văn Xương hóa Kỵ → phi phục xung vào cung Sửu\n"
               "3. Lưu niên 2020 khi Phụ Mẫu tại Sửu → ứng Kỵ Phụ Mẫu đại vận → ứng kỳ cha mất.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 18-21]",
    },
    # ── 22. TỨ HÓA THỰC CHIẾN: MỆNH LỆ KẾT HÔN 2 ─────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Kết hôn (năm 2019)",
        "keywords": ["mệnh lệ kết hôn 2", "liêm trinh hóa lộc", "thái âm hóa lộc", "phu thê lộc", "kết hôn 2019"],
        "text": "Sự kiện: Kết hôn năm 2019.\n"
               "Luận giải:\n"
               "1. Phu Thê tiên thiên can Giáp → Liêm Trinh hóa Lộc → phi phục Tam Điểm tại đại vận Tỵ\n"
               "2. Đại vận 52 ở Tỵ → nhận Lộc Phu tiên thiên → báo hiệu đại vận này có Lộc Phu Thê\n"
               "3. Phu Thê Đại vận 52 can Đinh → Thái Âm hóa Lộc → phi phục 1 Lộc ở Dậu\n"
               "4. Năm 2019 Phu Lưu niên ở Dậu → ứng kỳ Lộc của Phu Thê Đại vận → kết hôn.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 21-25]",
    },
    # ── 23. TỨ HÓA THỰC CHIẾN: MỆNH LỆ ĐƯƠNG SỐ MẤT ─────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Đương số mất (chết đuối 2020)",
        "keywords": ["mệnh lệ tử vong", "chết đuối", "phúc đức kỵ", "thọ yểu", "tử vong nhìn từ tứ hóa"],
        "text": "Sự kiện: Năm 2020 đương số vì cứu em mà chết đuối.\n"
               "Luận giải:\n"
               "1. Đoán Thọ Yểu: trước tiên cần đoán định cung Phúc Đức. Tất nhiên chỉ mỗi cung Phúc là chưa đủ, nhưng điều tiên quyết để có thể tử vong chắc chắn cung Phúc sẽ xảy ra vấn đề.\n"
               "2. Phúc tiên thiên can Quý → Tham Lang hóa Kỵ → phi phục Tam Điểm tại Tuất → đợi đại vận 14 tuổi đi vào cung Tuất ứng vận → gặp Kỵ của Phúc\n"
               "3. Phúc Đại vận can Nhâm → Vũ Khúc hóa Kỵ → phi phục Tam Điểm tại Dần → đợi lưu niên 2020 tới Tý và Phúc lưu niên tới Dần thì ứng vận.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 25-29]",
    },
    # ── 24. TỨ HÓA THỰC CHIẾN: MỆNH LỆ SINH CON ────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Sinh con (năm 2018)",
        "keywords": ["mệnh lệ sinh con", "tử tức lộc", "thiên cơ hóa lộc", "phá quân hóa lộc", "có con"],
        "text": "Sự kiện: Năm 2018 đương số sinh con vào ngày 26/12/2018 âm lịch.\n"
               "Luận giải:\n"
               "1. Tử Tức tiên thiên can Ất → Thiên Cơ hóa Lộc → phi phục tại Mão\n"
               "2. Đại vận 25 Tử Tức tại Mão → ứng Lộc Tử Tức tiên thiên → đại vận này dễ có lộc về Tử Tức\n"
               "3. Đại vận 25 Tử Tức can Quý → Phá Quân hóa Lộc tại Tuất → đợi lưu niên 2018 đến Tuất → ứng kỳ Lộc Tử Tức → có con.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 29-32]",
    },
    # ── 25. TỨ HÓA THỰC CHIẾN: MỆNH LỆ ĐA BIẾN CỐ ────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Đa biến cố: đổi chỗ ở, ly hôn, đổi việc, bố mất (2019)",
        "keywords": ["mệnh lệ đa biến cố", "đổi chỗ ở", "ly hôn", "đổi việc", "bố qua đời", "điền trạch kỵ", "quan kỵ", "phu thê kỵ"],
        "text": "Sự kiện năm 2019: Đổi chỗ ở, đổi việc, ly hôn, bố qua đời.\n"
               "Luận giải:\n"
               "1. Đổi chỗ ở: không nhất thiết quản bởi tiên thiên, có thể từ đại vận hoặc lưu niên.\n"
               "   a. Đại vận 24 Điền Đại vận can Ất → Thái Âm hóa Kỵ → phi phục Tam Điểm tại Dần\n"
               "   b. Năm 2019 Điền Lưu niên tại Dần → ứng vận Điền có biến động → chuyển nhà\n\n"
               "2. Đổi việc:\n"
               "   a. Đại vận 24 Quan Đại vận can Giáp → Thái Dương hóa Kỵ → phi phục tại Hợi\n"
               "   b. Lưu niên 2019 tại Tuất → nhận Kỵ của Quan Đại vận → có vấn đề về Quan → chuyển việc\n\n"
               "3. Ly hôn (việc lớn, ứng từ tiên thiên xuống):\n"
               "   a. Phu Thê tiên thiên can Nhâm → Vũ Khúc hóa Kỵ → phục tại Tuất\n"
               "   b. Đại vận 24 tại Tuất → gặp Kỵ Phu Thê tiên thiên → xấu về Phu Thê\n"
               "   c. Phu Thê đại vận 24 can Canh → Thiên Đồng hóa Kỵ → phục tại Dậu\n"
               "   d. Lưu niên 2019 Phu Thê Lưu niên tại Dậu → ứng Kỵ Phu Thê đại vận → ly hôn\n\n"
               "4. Cha bệnh mất:\n"
               "   a. Tật Phụ Mẫu tiên thiên ở Thân can Canh → Thiên Đồng hóa Kỵ → phi phục Tam Điểm → báo hiệu Tật cha có vấn đề\n"
               "   b. Đại vận 24 Tật Phụ Mẫu đại vận ở Ngọ can Mậu → Thiên Cơ hóa Kỵ → phi phục Tam Điểm tại Tý-Sửu-Mùi\n"
               "   c. Năm 2019 Phụ Mẫu Lưu niên tại Tý → nhận Kỵ của Tật Phụ Mẫu đại vận → xảy ra vấn đề về Tật với Phụ Mẫu.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 32-42]",
    },
    # ── 26. TỨ HÓA THỰC CHIẾN: MỆNH LỆ GẪY TAY ────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Gẫy tay (năm 2006)",
        "keywords": ["mệnh lệ gẫy tay", "tật ách", "thiên đồng hóa kỵ", "gẫy tay", "tai nạn"],
        "text": "Sự kiện: Năm 2006 đương số gẫy tay.\n"
               "Luận giải:\n"
               "1. Tật tiên thiên và Tật đại vận can Canh → Thiên Đồng hóa Kỵ → phi phục Tam Điểm vào Tỵ và Tuất\n"
               "2. Năm Tuất 2006 Lưu niên tại Tuất, Tật Lưu niên tại Tỵ → vừa lúc ứng kỳ Tật → gẫy tay.\n"
               "Gẫy tay có thể nhìn từ cung Tật Ách của đương số. Tật Ách hóa Kỵ đến đâu là nơi dễ xảy ra tai nạn.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 42-45]",
    },
    # ── 27. TỨ HÓA THỰC CHIẾN: MỆNH LỆ PHỤ MẪU LY HÔN ────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Mệnh lệ - Phụ Mẫu ly hôn nhìn từ lá số con cái",
        "keywords": ["mệnh lệ phụ mẫu ly hôn", "ly hôn phụ mẫu", "phu thê phụ mẫu", "con cái nhìn ly hôn của cha mẹ"],
        "text": "Sự kiện: Phụ Mẫu ly hôn - nhìn từ lá số của con cái.\n"
               "Luận giải: Muốn nhìn chuyện hôn nhân của Phụ Mẫu, nhìn từ Phu Thê của Phụ Mẫu (tức cung Phụ Mẫu lập Thái Cực, rồi lấy cung Phu Thê của Thái Cực đó).\n"
               "1. Phu Thê của Phụ Mẫu tiên thiên ở Dậu can Quý → Tham Lang hóa Kỵ → phi phục Tam Điểm tại Mùi\n"
               "2. Đại vận 26 tuổi Phụ Mẫu đại vận tại Dậu, Phu Thê Phụ Mẫu đại vận tại Mùi → ứng Kỵ Phu Thê Phụ Mẫu tiên thiên\n"
               "3. Phu Thê Phụ Mẫu đại vận 26 ở Mùi can Tân → Văn Xương hóa Kỵ → phi phục Tam Điểm tại Sửu, Mùi (tự xung), Tý\n"
               "4. Lưu niên 2020 ở Tý và Phụ Mẫu lưu niên ở Sửu → ứng kỳ Phụ Mẫu ly hôn.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 45-48]",
    },
    # ── 28. TỔNG KẾT PHƯƠNG PHÁP LUẬN TỨ HÓA ──────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Tổng kết phương pháp luận vận hạn ứng kỳ tam bàn",
        "keywords": ["tổng kết tứ hóa", "khung xương tứ hóa", "phương pháp luận", "tam bàn thiên địa nhân", "sơ cấp tứ hóa", "nhập môn tứ hóa"],
        "text": "Tổng kết phương pháp luận vận hạn ứng kỳ tam bàn Thiên Địa Nhân trong Tứ Hóa Bắc Phái:\n"
               "1. Tiên thiên (Thiên bàn): Lấy Tứ Hóa năm sinh làm gốc, xem Lộc/Kỵ ở cung nào\n"
               "2. Đại vận (Địa bàn): Phi phục từ tiên thiên xuống đại vận, xem đại vận đến cung nào gặp Lộc/Kỵ của tiên thiên\n"
               "3. Lưu niên (Nhân bàn): Đại vận lại phi phục xuống lưu niên, chờ năm đến đúng cung có Lộc/Kỵ\n"
               "4. Nhất Kỵ Tam Điểm: Một Kỵ ảnh hưởng 3 vị trí (tọa, xung, Nhất Lục)\n"
               "5. Lập Thái Cực (Cung vị hoán chuyển): Muốn xem việc gì thì lấy cung tương ứng làm trung tâm\n\n"
               "Lưu ý: Đây chỉ là căn bản Nhập Môn. Thực tế ngoài cuộc sống phức tạp hơn nhiều, cần đọc thêm sách và học nâng cao.\n"
               "[Nguồn: Tứ Hóa Thực Chiến Sơ Cấp - Chiến Nguyễn, trang 51]",
    },
    # ── 29. LỊCH SỬ KHÂM THIÊN ──────────────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Lịch sử Khâm Thiên Giám và nguồn gốc Khâm Thiên Tứ Hóa",
        "keywords": ["khâm thiên giám", "lịch sử tử vi", "nguồn gốc khâm thiên", "tứ hóa bắc phái lịch sử", "hoàng gia chính tông"],
        "text": "Khâm Thiên Tử Vi Đẩu Số bắt nguồn từ Khâm Thiên Giám thời phong kiến Trung Quốc. Tử Vi và các hệ sao là những ngôi sao thực sự tồn tại trong thiên thể. Khâm Thiên Giám thời xưa được lập ra để quan sát thiên tượng, tính toán tiết khí, lập lịch pháp, và khảo sát long mạch cho triều đình.\n\n"
               "Từ thời Tần Hán đến Nam Bắc Triều, Khâm Thiên Giám do Thái Thường quản lý. Qua các thời kỳ: Thời Nguyên đổi thành Tư Thiên Đài; Thời Ngũ Đại đổi thành Tư Thiên Giám, sau thành Thái Sử Cục; Đầu thời Minh chính thức gọi là Khâm Thiên Giám.\n\n"
               "Đẩu Số xuất hiện vào khoảng cuối thời Minh đầu thời Thanh. Khâm Thiên Giám hoạt động theo chế độ thế tập. Dưới chính sách ngu dân thời phong kiến, đây là môn 'tuyệt học cung đình' được giữ kín không truyền ra ngoài. Đến khi chế độ phong kiến sụp đổ, phương pháp quan sát thiên tượng mới lưu lạc dân gian.\n\n"
               "Hiện nay Tứ Hóa Bắc Phái chia làm nhiều môn phái: Khâm Thiên Môn (Thái Minh Hồng), Hà Lạc Phái (Sở Thiên Vân Khoát), Phi Tinh Lương Phái (Lương Nhược Du), Khâm Thiên Vô Cực Môn (Ông Phúc Dụ).\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa, trang 5-6]",
    },
    # ── 30. 4 HỆ THỐNG CỦA KHÂM THIÊN ──────────────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "4 hệ thống của Khâm Thiên: Sao, Cung Vị, Tứ Hóa, Thiên Can Địa Chi",
        "keywords": ["4 hệ thống", "hệ thống khâm thiên", "sao cung vị tứ hóa", "thiên can địa chi", "nạp âm khâm thiên"],
        "text": "Khâm Thiên có 4 hệ thống (không phải 3 như nhiều tác giả khác chia):\n"
               "1. Tinh Thần (Sao): 18 sao chính, hệ Tử Vi và hệ Thiên Phủ\n"
               "2. Cung Vị: 12 cung từ 10 Thiên Can và 12 Địa Chi phối hợp Âm Dương. Cung Vị giống như bình chứa\n"
               "3. Tứ Hóa: Tứ Hóa năm sinh + Tự Hóa + Phi Tinh Tứ Hóa\n"
               "4. Thiên Can Địa Chi: Ngũ hành nạp âm, ứng dụng vào bệnh tật, tạng phủ, cơ thể\n\n"
               "Mệnh bàn được cấu thành từ 4 yếu tố này. Khâm Thiên không chỉ là Khâm Thiên Tứ Hóa, mà còn có Khâm Thiên Phi Tinh.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa, trang 5-7]",
    },
    # ── 31. ĐƠN TƯỢNG - SONG TƯỢNG - TAM TƯỢNG ─────────────────────────
    {
        "category": "Bắc Phái Tứ Hóa",
        "topic": "Đơn tượng, Song tượng, Tam tượng - Nguyên lý hình thành cát hung",
        "keywords": ["đơn tượng", "song tượng", "tam tượng", "tượng pháp", "cát hung tượng", "lộc quyền khoa kỵ tượng"],
        "text": "Nguyên lý Tượng trong Khâm Thiên:\n\n"
               "1. Đơn tượng không thành vật: Một tượng đơn lẻ (ví dụ Lộc năm sinh M tọa ở đâu đó) chưa thể kết luận cát hung.\n\n"
               "2. Song tượng thành vật: Hai tượng kết hợp mới thành sự. Ví dụ: Cung Phu Thê có C (Khoa) và tự hóa C (Khoa) - thành song tượng.\n\n"
               "3. Các trường hợp Song tượng:\n"
               "   - Đồng cung ABD (3 sao trong 1 cung) - Lấy thiên can cung này phi Khoa ra\n"
               "   - Song tượng đồng tổ bất đồng cung: Ví dụ Lộc và Kỵ đồng tổ nhưng khác cung\n"
               "   - Năm sinh M lại tự hóa M (tự hóa Lộc trên cùng tinh diệu có Lộc năm sinh)\n\n"
               "4. Tam tượng nhất vật hình thành cát hung: Ví dụ Năm sinh Lộc (M) + tự hóa Khoa (C) + vật là Thiên Cơ - lúc này có thể định cát hung.\n"
               "[Nguồn: Giáo trình Khâm Thiên Tứ Hóa - Đại Hoa]",
    },
]
