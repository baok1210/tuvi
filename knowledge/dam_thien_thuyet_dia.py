"""
Đàm thiên thuyết địa thoại Tử Vi (谈天说地话紫微) - Lý Phật (李佛).
Phân tích tổ hợp hai chính tinh đồng cung thủ Mệnh.
"""

LY_PHAT_STAR_PAIRS = {
    "Tử Vi - Thiên Phủ": {
        "cung": "Dần Thân",
        "danh_xung": "Tử Phủ đồng cung cách",
        "phan_tich": "Hai sao Tử vi Thiên phủ chỉ cùng cung tại Dần Thân, đều được coi là vị trí cực tốt. Mệnh được cách này tất có khả năng lãnh đạo, kiến thức, mưu trí, tài năng xuất chúng, phản ứng mẫn tiệp, xử thế hòa hợp mà vẫn giữ khoảng cách với mọi người. Có tinh thần trách nhiệm cao độ, nhiệt tâm phục vụ công ích, bất chấp trở ngại khó khăn. Nhưng vì Tử vi và Thiên Phủ là hai lãnh tụ của hai chùm sao khác nhau, khi cùng cung ví như hai hổ cùng ở một rừng tất phải có xung đột, nên sự tốt đẹp không được hoàn hảo.",
        "xung_dot": "Tử Vi có tính động, Thiên Phủ thiên về tĩnh. Tử Vi có tính khai phá, Thiên Phủ có tính bảo thủ. Tử Vi đại diện ước vọng cao vời, Thiên Phủ đại diện mục đích thực tế.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Tử Vi - Tham Lang": {
        "cung": "Mão Dậu",
        "danh_xung": "Đào hoa phạm Đế tọa",
        "phan_tich": "Mão Dậu là bình địa của Tử Vi, hãm địa của Tham Lang. Tử Vi bình hòa kém thông minh nhưng trọn đời no cơm ấm áo và sống lâu. Tham Lang hãm địa ở Mão Dậu làm việc gì cũng thất bại và hay gặp chẳng lành. Khi Tử Tham đồng cung, người có mệnh này dễ lâm vào cảnh túng thiếu, bần hàn hoặc thất cơ lỡ vận.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Tử Vi - Phá Quân": {
        "cung": "Sửu Mùi",
        "danh_xung": "Tử Phá tương xung",
        "phan_tich": "Tử vi ở Sửu Mùi, Phá quân xung chiếu. Phá quân có ý nghĩa xung phong hãm trận, sau khi nhận lệnh của hoàng đế ở xung cung thì chỉ biết làm theo quân lệnh, không quan tâm đến việc khác. Chủ về hoặc tinh thần bị kích thích, hoặc tâm trạng không khỏe mạnh. Nếu có cát tinh hội chiếu thì cuộc đời ba chìm bảy nổi.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Thiên Đồng - Thiên Lương": {
        "cung": "Dần Thân (Đồng Lương tại Dần, Nhật Nguyệt tại Thìn Tuất đồng luận)",
        "danh_xung": "Đồng Lương cách",
        "phan_tich": "Đồng Lương là sự kết hợp giữa lãng mạn (Thiên Đồng) và nguyên tắc (Thiên Lương). Tại Dần là vị trí cực tốt — 'Đồng Lương đáo Dần chủ bần' là sai: thực ra Đồng Lương tại Dần là cát chi cát. Tại Thân là vượng địa của Thiên Lương. Là người có phúc đức, trí tuệ, sống an nhàn, hay giúp người. Nếu có sát tinh sinh bất đắc chí, hoài tài không gặp thời.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Tử Vi - Thiên Tướng": {
        "cung": "Dần Thân",
        "danh_xung": "Tử Tướng đồng cung",
        "phan_tich": "Tử Tướng đồng cung tại Dần Thân tất có Thiên Phủ ở xa chiếu, lại gặp song Tá Hữu, song Khôi Việt và Xương Khúc, tạo nên thế kiềng ba chân vững vàng. Chủ về uy quyền, có tài lãnh đạo và quản lý, trên thuận dưới hòa.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Vũ Khúc - Tham Lang": {
        "cung": "Mão Dậu (đồng cung), Thìn Tuất Tỵ Hợi (hội chiếu)",
        "phan_tich": "Vũ Tham thủ mệnh chủ về trước nghèo sau giàu. Có sát tinh thì lúc nhỏ nhiều tai nạn, thọ mệnh không dài. (Đây là nhận định từ sách cổ — 'thọ mệnh không dài' cần kết hợp toàn bộ lá số Phúc Đức, Tật Ách, Tứ Hóa mới đánh giá được.) Là người có năng khiếu về kỹ thuật, tài chính, có thể phát triển sự nghiệp từ hai bàn tay trắng.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Liêm Trinh - Thất Sát": {
        "cung": "Tị Hợi",
        "danh_xung": "Liêm Sát đồng cung",
        "phan_tich": "Liêm Trinh Thất Sát đồng cung tại Tị Hợi chủ về lao ngục, huyết quang. Là người can đảm, táo bạo nhưng dễ vướng vòng lao lý. Nếu hội đủ tam hợp Tử Phủ Tướng và Khôi Việt thì hóa dữ thành lành, thành công trong ngành tư pháp hoặc quân đội.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Liêm Trinh - Thiên Phủ": {
        "cung": "Thìn Tuất",
        "phan_tich": "Liêm Trinh Thiên Phủ đồng cung chủ về thông minh, có tài tổ chức, quản lý tiền bạc tốt. Khi gặp cát tinh thì công danh hiển đạt, có lòng trắc ẩn, hay giúp người. Nếu gặp sát tinh thì bị cuốn vào vòng thị phi.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Vũ Khúc - Thiên Phủ": {
        "cung": "Thìn Tuất, Tý Ngọ",
        "phan_tich": "Thiên Phủ Vũ Khúc đồng cung hoặc hội chiếu chủ về tài quản lý, kinh doanh. Thiên Phủ là kho tàng, Vũ Khúc là tài tinh, kết hợp với Miếu Vượng thì phú quý song toàn.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Vũ Khúc - Thiên Tướng": {
        "cung": "Tị Hợi",
        "phan_tich": "Vũ Khúc Thiên Tướng đồng cung tại Tị Hợi chủ về tài năng tổ chức, xây dựng cơ đồ. Là người thực tế, biết vun vén, nếu đắc cát tinh thì làm nên sự nghiệp lớn.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    "Vũ Khúc - Thất Sát": {
        "cung": "Mão Dậu",
        "phan_tich": "Vũ Khúc Thất Sát đồng cung tại Mão Dậu. Vũ khúc thủ mệnh ở Mão là lạc hãm, Thất sát thủ mệnh ở Dậu là miếu địa. Sự kết hợp giữa hãm và miếu tạo nên mâu thuẫn nội tâm, dễ nổi loạn bất cần, tài năng không gặp thời.",
        "nguon": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
}

LY_PHAT_QUOTES = [
    {
        "text": "Khi bàn đến cung Mệnh, tức là cung quan trọng nhất, gần như chẳng thấy sách nào do người Việt biên soạn chú ý đến trường hợp hai chính tinh đứng đồng cung. Ý nghĩa các chính tinh chỉ được trình bày riêng rẽ.",
        "source": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    {
        "text": "Tử vi và Thiên Phủ là hai lãnh tụ của hai chùm sao khác nhau, khi cùng cung ví như hai hổ cùng ở một rừng tất phải có xung đột.",
        "source": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
    {
        "text": "Mão Dậu là bình địa của Tử Vi, hãm địa của Tham Lang.",
        "source": "Đàm thiên thuyết địa thoại Tử Vi – Lý Phật",
    },
]
