"""
Tử Vi Trung Quốc — RAG entries from Chinese ZWDS classical sources
Translated to Vietnamese for Tử Vi Đẩu Số context
Sources: 紫微斗数全书 (诸星问答论, 太微赋, 形性赋, 星垣论, etc.),
         zhunsuan.org, liuyunling.com, iztro.com, gushiwen.cn, zhihu.com
"""

TRUNG_QUOC_DATA = []

def _add(category, topic, keywords, text):
    TRUNG_QUOC_DATA.append({
        "category": category,
        "topic": topic,
        "keywords": keywords,
        "text": text,
    })

# ===== 14 main stars (诸星问答论 classical + modern description) =====

_add("chinh_tinh", "Tử Vi", ["tử vi trung quốc", "tử vi tinh", "tử vi đế tọa", "tử vi vua", "sao tử vi", "tử vi hoàng đế"],
    "Tử Vi — Tinh đế vương, ngôi vua của các sao. Ngũ hành: Kỷ Thổ (Âm Thổ), Hóa Khí: Tôn. "
    "Là Bắc Đẩu chủ tinh, đứng đầu muôn sao, nên gọi là 'Đế Tọa' (ngôi vua). "
    "Chủ tể tạo hóa, nhân sinh chủ tể. Cầm ngũ hành dục vạn vật, chưởng tạo hóa xu cơ. "
    "Người Tử Vi thủ mệnh: khí chất lãnh đạo, uy nghi, tự trọng cao, hành sự trầm ổn. "
    "Nếu cô quân (thiếu Tả Hữu) dễ độc đoán, nội tâm cô độc. "
    "Có thể chế Hỏa Linh thành thiện, hàng Thất Sát thành quyền. "
    "Được Phủ Tướng Tả Hữu Xương Khúc hội nhập, tất đại quý. "
    "Tại Tài Bạch Điền Trạch có Tả Hữu thủ vệ, đồng độ Vũ Khúc Thái Âm, không thấy ác tinh, tất làm quan tài phú. "
    "Cổ văn hỏi đáp: Tử Vi thuộc Thổ, nãi trung thiên chi tôn tinh vi Đế tọa. "
    "Chư cung giáng phúc, năng tiêu bách ác. Vô Phụ Bật đồng hành tắc vi cô quân. "
    "Năng chế Hỏa Linh vi thiện, năng hàng Thất Sát vi quyền. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thiên Cơ", ["thiên cơ trung quốc", "thiên cơ tinh", "sao thiên cơ", "thiên cơ trí tuệ", "thiên cơ mưu"],
    "Thiên Cơ — Sao trí tuệ, mưu thần. Ngũ hành: Ất Mộc (Âm Mộc), Hóa Khí: Thiện. "
    "Nam Đẩu đệ tam tinh, ích toán chi thiện tinh, gia tăng thọ mệnh. "
    "Hóa khí vi thiện, giải chư tinh chi thuận nghịch. "
    "Người Thiên Cơ thủ mệnh: đầu óc nhanh nhạy, đa mưu túc trí, tư duy logic. "
    "Gặp chư cát tắc vạn sự giai thiện. Hay cúng Phật, kính lục thân. "
    "Không có lòng ác, có chí cơ biến. Nữ mệnh ngộ chi vi phúc. "
    "Đồng độ Thiên Lương, tất có cao nghệ tùy thân. "
    "Cổ văn: Thiên Cơ ích thọ chi tinh, nhược thủ thân mệnh, chủ nhân dị thường. "
    "Dữ Thiên Lương, Tả Hữu, Xương Khúc giao hội, văn vi thanh hiển, vũ vi trung lương. "
    "Nhược cư hãm địa, tứ sát xung phá, thị vi hạ cục. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + liuyunling.com/387]")

_add("chinh_tinh", "Thái Dương", ["thái dương trung quốc", "thái dương tinh", "mặt trời", "sao thái dương", "thái dương quang minh"],
    "Thái Dương — Sao quang minh, nhật tinh. Ngũ hành: Bính Hỏa (Dương Hỏa), Hóa Khí: Quý. "
    "Trung Thiên chủ tinh, nhật chi tinh dã, đại diện ánh sáng, bác ái. "
    "Chủ quý khí, năng vi văn năng vi vũ. Ở Quan Lộc cung là tốt nhất. "
    "Nam tác phụ tinh (sao cha), nữ vi phu chủ (sao chồng). "
    "Người Thái Dương thủ mệnh: tính cởi mở, nhiệt tình, hào sảng, thích giúp người. "
    "Miếu vượng thì hào quang vạn trượng; hãm địa thì lao nhi vô công. "
    "Ở Dần Mão là sơ thăng (mới mọc), ở Thìn Tỵ là thăng điện, ở Ngọ là nhật lệ trung thiên (đại phú quý). "
    "Ở Thân Dậu là thiên viên (thiên lệch), ở Tuất Hợi Tý là thất huy. "
    "Cổ văn: Thái Dương chu thiên lịch độ, thâu chuyển vô cùng. "
    "Hỉ Phụ Bật nhi tá quân tượng, dĩ Lộc Tồn nhi trợ phúc. "
    "Sở kỵ giả Cự Ám tao phùng. Sở lạc giả Thái Âm tương vượng. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Vũ Khúc", ["vũ khúc trung quốc", "vũ khúc tinh", "sao vũ khúc", "vũ khúc tài", "vũ khúc tài bạch"],
    "Vũ Khúc — Sao tài phú, Tài Bạch chủ. Ngũ hành: Tân Kim (Âm Kim), Hóa Khí: Tài. "
    "Bắc Đẩu đệ lục tinh, tài bạch cung chủ. Đồng cung Thiên Phủ hữu thọ. "
    "Người Vũ Khúc thủ mệnh: tính cương cường, quả đoán, coi trọng hiệu suất. "
    "Nhạy với tiền, quản lý tài chính mạnh. Cơ tính cô khắc, dễ vì quá chuyên sự nghiệp mà lơ là quan hệ. "
    "Nữ mệnh Vũ Khúc mạnh mẽ, 'Quý phụ' nhưng hôn nhân trắc trở. "
    "Người phương Tây Bắc được phúc, phương Đông Nam bình thường. "
    "Cổ văn: Vũ Khúc chúc Kim, Bắc Đẩu đệ lục tinh, vi Tài Bạch chủ. "
    "Dữ Lộc Mã giao trì, phát tài ư viễn quận. "
    "Nhược Tham Lang đồng độ, kiên lận chi nhân. Phá Quân đồng tài hương, tài đáo thủ nhi thành không. "
    "Ngộ Dương Đà tắc cô khắc, ngộ Phá Quân nan hiển quý. "
    "Chủ nhân cương cường quả đoán, Giáp Kỷ sinh nhân phúc hậu, xuất tướng nhập tướng. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thiên Đồng", ["thiên đồng trung quốc", "thiên đồng tinh", "sao thiên đồng", "thiên đồng phước", "thiên đồng phúc"],
    "Thiên Đồng — Sao phúc đức, Phúc tinh. Ngũ hành: Nhâm Thủy (Dương Thủy), Hóa Khí: Phúc. "
    "Nam Đẩu đệ tứ tinh, Phúc Đức cung chi chủ tể. "
    "Hóa phúc, tối hỉ ngộ cát diệu, trợ phúc thiêm tường. "
    "Người Thiên Đồng thủ mệnh: phúc dày, tướng mạo thanh kỳ, tính ôn hòa, khiêm tốn. "
    "Không sợ Thất Sát xâm phạm, không sợ chư sát đồng triền. "
    "Thập nhị cung trung giai viết phúc. Nhược hạn phùng chi, nhất sinh đắc địa. "
    "Gặp Tả Hữu Xương Lương hiển quý. Ất Bính Mậu Kỷ nhân đắc địa. "
    "Nữ mệnh phùng sát xung phá, hình phu khắc tử. Tăng đạo nghi chi, chủ hưởng phúc. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Liêm Trinh", ["liêm trinh trung quốc", "liêm trinh tinh", "sao liêm trinh", "liêm trinh tù", "liêm trinh đào hoa"],
    "Liêm Trinh — Tù tinh, thứ đào hoa. Ngũ hành: Đinh Hỏa (Âm Hỏa), Hóa Khí: Tù. "
    "Bắc Đẩu đệ ngũ tinh, tại Đẩu ti phẩm trật, tại số tư quyền lệnh. "
    "Là sao phức tạp nhất Tử Vi. Biến hóa khôn lường: có thể liêm khiết kỷ luật hoặc phóng đãng tà ác. "
    "Xúc chi bất khả giải kỳ họa, phùng chi bất khả trắc kỳ tường. "
    "Gặp Đế tọa chấp uy quyền, gặp Lộc Tồn chủ phú quý, gặp Văn Xương hiếu lễ nhạc. "
    "Tại thân mệnh vi thứ đào hoa. Tại Quan Lộc hữu uy quyền. "
    "Cổ văn: Liêm Trinh chúc Mộc Hỏa, Bắc Đẩu đệ ngũ tinh, hóa khí vi Tù. "
    "Đồng Vũ Khúc ư thọ chế chi hương, khủng mộc áp xà thương. (đồng Vũ Khúc tại Dần Thân, sợ bị gỗ đè rắn cắn) "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thiên Phủ", ["thiên phủ trung quốc", "thiên phủ tinh", "sao thiên phủ", "thiên phủ kho tàng", "thiên phủ nam diện"],
    "Thiên Phủ — Sao kho tàng, Nam Diện Vương. Ngũ hành: Thổ (Dương Thổ), Hóa Khí: Hiền năng. "
    "Nam Đẩu chủ lệnh đệ nhất tinh, vi Tài Bạch chi chủ tể. "
    "Tại Đẩu tư phúc quyền chi tú, hội cát giai vi phú quý. "
    "Thiên Phủ là Nam Đẩu diên thọ giải ách chi tinh, hựu viết Tư Mệnh. "
    "Năng chế Dương Đà vi tòng, năng hóa Hỏa Linh vi phúc. "
    "Người Thiên Phủ thủ mệnh: tính rộng lượng, bao dung, trầm ổn. "
    "Chủ nhân tướng mạo thanh kỳ, tính ôn lương đoan nhã. "
    "Gặp Xương Khúc tất đăng thủ tuyển. Gặp Lộc Tồn Vũ Khúc, tất hữu cự vạn chi phú. "
    "Không ưa tứ sát xung phá. Thường chủ cát — bất luận chư cung giai cát. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thái Âm", ["thái âm trung quốc", "thái âm tinh", "sao thái âm", "thái âm mặt trăng", "thái âm điền trạch"],
    "Thái Âm — Sao tài phú, điền trạch. Ngũ hành: Quý Thủy (Âm Thủy), Hóa Khí: Phú. "
    "Thủy chi tinh, vi Điền Trạch chủ, hóa phú, dữ Nhật vi phối. "
    "Người Thái Âm thủ mệnh: thông minh tuấn tú, đoan nhã thuần tường. "
    "Nguyệt huy tinh diệu — lấy miếu vượng luận. Tại Dậu Tuất Hợi Tý là đắc viên. "
    "Mão Thìn Tỵ Ngọ là hãm địa. "
    "Hợp Văn Khúc đồng cư thân mệnh, định thị cửu lưu thuật sĩ. "
    "Nam vi thê tú (sao vợ), hựu tác mẫu tinh (sao mẹ). "
    "Cổ văn: Thái Âm hóa lộc dữ nhật vi phối. Dần Mão Thìn Tỵ Ngọ vi hãm địa. "
    "Dậu Tuất Hợi Tý Sửu vi đắc viên. Hiềm Cự Diệu dĩ lai triền, phạ Dương Đà dĩ đồng độ. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Tham Lang", ["tham lang trung quốc", "tham lang tinh", "sao tham lang", "tham lang dục", "tham lang đào hoa", "tham lang bắc đẩu"],
    "Tham Lang — Sao dục vọng, đào hoa. Ngũ hành: Giáp Mộc (Dương Mộc) kiêm Quý Thủy, Hóa Khí: Đào hoa. "
    "Bắc Đẩu đệ nhất tinh, giải ách chi thần. Chủ họa phúc chi thần. "
    "Hóa khí vi đào hoa, vi tiêu chuẩn. Thụ thiện ác định gian trá. "
    "Người Tham Lang thủ mệnh: dục vọng mạnh, thông minh đa tài, giao tiếp thiên phú. "
    "Nhập miếu lạc chi cung, khả vi tường khả vi họa. "
    "Hội Hỏa Linh năng phú quý. Hội Phá Quân mê hoa luyến tửu nhi táng mệnh. "
    "Đồng Vũ Khúc đắc địa, vi nhân siểm nịnh gian tham. "
    "Phạm Đế tọa vô chế, tiện vi vô ích chi nhân. "
    "Cổ văn: Tham Lang vi Bắc Đẩu giải ách chi thần, chức minh chi tinh. "
    "Cư miếu vượng ngộ Hỏa tinh Vũ chức quyền quý. Ngộ Thiên Tướng diên thọ. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Cự Môn", ["cự môn trung quốc", "cự môn tinh", "sao cự môn", "cự môn ám", "cự môn khẩu thiệt", "cự môn thị phi"],
    "Cự Môn — Sao ám, khẩu thiệt. Ngũ hành: Thủy kiêm Kim. "
    "Bắc Đẩu đệ nhị tinh, vi âm tinh chi tinh, hóa khí vi ám. "
    "Tại thân mệnh nhất sinh chiêu khẩu thiệt chi phi. "
    "Tại huynh đệ tắc cốt nhục sâm thương. Tại phu thê chủ vu cách giác, sinh ly tử biệt. "
    "Cự Môn ưa hóa Lộc, hóa Quyền — biến khẩu thiệt thành quyền, thị phi thành tài nguyên. "
    "Người Cự Môn thủ mệnh: tài ăn nói cực tốt nhưng dễ đắc tội người. "
    "Hội Thái Dương tắc cát hung tương bán. Phùng Thất Sát tắc chủ thương sát. "
    "Ngộ Đế tọa tắc chế kỳ cường. Phùng Lộc Tồn tắc giải kỳ ách. "
    "Duy tăng đạo cửu lưu phương miễn lao thần. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thiên Tướng", ["thiên tướng trung quốc", "thiên tướng tinh", "sao thiên tướng", "thiên tướng ấn", "thiên tướng văn thư"],
    "Thiên Tướng — Sao ấn, tước. Ngũ hành: Nhâm Thủy. "
    "Nam Đẩu đệ ngũ tinh, vi Tư Tước chi tú, vi Phúc Thiện. "
    "Hóa khí vi Ấn, thị vi Quan Lộc văn tinh. "
    "Người Thiên Tướng thủ mệnh: ngôn ngữ thành thực, hữu trắc ẩn chi tâm. "
    "Quan Lộc đắc chi tắc hiển vinh, Đế tọa hợp chi tắc tranh quyền. "
    "Sao Thiên Tướng có tính 'bị kẹp': cát tinh kẹp thì cát, hung tinh kẹp thì hung. "
    "Cổ văn: Thiên Tướng Nam Đẩu tư tước chi tinh, hóa khí vi ấn. "
    "Chủ nhân y thực phong túc. Xương Khúc Tả Hữu tương hội, vị chí công khanh. "
    "Hãm địa Tham Liêm Vũ Phá Dương Đà sát tấu, xảo nghệ an thân. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thiên Lương", ["thiên lương trung quốc", "thiên lương tinh", "sao thiên lương", "thiên lương âm", "thiên lương thọ"],
    "Thiên Lương — Sao che chở, thọ tinh. Ngũ hành: Thổ (Dương Thổ), Hóa Khí: Âm. "
    "Nam Đẩu đệ nhị tinh, tư thọ, hóa khí vi âm. "
    "Vi Phúc Thọ, nãi Phụ Mẫu chi chủ. Hóa bạo lệ vi tường hòa. "
    "Người Thiên Lương thủ mệnh: tính tình lạc lạc, dày dặn ôn nhu, cương trực vô tư. "
    "Có khả năng gặp dữ hóa lành. Ấm ư thân, phúc cập tử tôn. "
    "Hội xương hóa lộc tại tài cung, phùng Thái Dương tại Phúc Đức tam hợp. "
    "Cổ văn: Thiên Lương Nam Đẩu tư thọ chi tinh, hóa khí vi âm vi thọ. "
    "Vi Phụ Mẫu chủ. Sinh nhân thanh tú ôn hòa, hình thần ổn trọng. "
    "Đắc Xương Khúc Tả Hữu gia hội, vị chí đài tỉnh. "
    "Hội Thái Dương ư Phúc Đức, cực phẩm chi quý. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Thất Sát", ["thất sát trung quốc", "thất sát tinh", "sao thất sát", "thất sát tướng", "thất sát sát khí", "thất sát nam đẩu"],
    "Thất Sát — Tướng tinh, sát tinh. Ngũ hành: Hỏa kiêm Kim. "
    "Nam Đẩu đệ lục tinh, Đẩu trung chi thượng tướng, thực thành bại chi cô thần. "
    "Chủ phong hiến, uy tác Kim chi linh, kỳ tính nhược thanh lương. "
    "Người Thất Sát thủ mệnh: cương nghị, lãnh khốc, độc lập cực mạnh. "
    "Gặp Tử Vi tắc hóa quyền hàng phúc. Gặp Hỏa Linh tắc trưởng kỳ sát uy. "
    "Cổ văn: Thất Sát Đẩu trung thượng tướng. Ngộ Tử Vi tắc hóa quyền hàng phúc. "
    "Ngộ Hỏa Linh tắc trường kỳ sát uy. Tả Hữu Xương Khúc nhập miếu củng chiếu, chưởng sinh sát chi quyền, phú quý xuất chúng. "
    "Tứ sát kỵ tinh xung phá, xảo nghệ bình thường chi nhân, hãm địa tàn tật. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

_add("chinh_tinh", "Phá Quân", ["phá quân trung quốc", "phá quân tinh", "sao phá quân", "phá quân hao", "phá quân phá hoại", "phá quân bắc đẩu"],
    "Phá Quân — Hao tinh, phá hoại. Ngũ hành: Quý Thủy (Âm Thủy), Hóa Khí: Hao. "
    "Bắc Đẩu đệ thất tinh, tư phu thê, tử tức, nô bộc chi thần. "
    "Cư Tý Ngọ nhập miếu. Tại thiên vi sát khí, tại số vi hao tinh. "
    "Chủ nhân bạo hung giảo trá, kỳ tính gian hoạt. "
    "Người Phá Quân thủ mệnh: ghét sự trì trệ, là nhà cải cách thiên bẩm. "
    "'Tiên phá hậu lập' — phá trước dựng sau. "
    "Cư Tý Ngọ, Tham Lang Thất Sát tương củng tắc uy chấn hoa di. "
    "Đồng Vũ Khúc cư Tỵ, Tham Lang củng diệc cư đài các. "
    "Duy Thiên Lương khả chế kỳ ác, Thiên Lộc khả giải kỳ cuồng. "
    "[Nguồn: 紫微斗数全书 诸星问答论 + zhunsuan.org]")

# ===== Phụ tinh (诸星问答论) =====

_add("phu_tinh", "Văn Xương", ["văn xương trung quốc", "sao văn xương", "văn xương khoa giáp", "văn xương học vấn"],
    "Văn Xương — Sao khoa giáp, chủ văn nghiệp. Văn Xương chủ khoa giáp. "
    "Thủ thân mệnh chủ nhân u nhàn nho nhã, thanh tú khôi ngô, bác văn quảng ký, cơ biến dị thường. "
    "Nhất cử thành danh, phúc thọ song toàn. "
    "Dù tứ sát xung phá bất vi hạ tiện. "
    "Người nữ gia cát đắc địa, y lộc sung túc. "
    "Văn Xương tại Thìn Tỵ là vượng địa, lợi Ngọ, hiềm Mão Dậu. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Văn Khúc", ["văn khúc trung quốc", "sao văn khúc", "văn khúc khoa giáp", "văn khúc tài hoa"],
    "Văn Khúc — Sao tài hoa, khẩu tài. Ngũ hành: Thủy. Bắc Đẩu đệ tứ tinh, chủ khoa giáp văn xa chi tú. "
    "Lâm thân mệnh trung tác khoa đệ chi khách. "
    "Đơn cư thân mệnh, lại phùng hung diệu, diệc tác vô danh thiệt biện chi đồ. "
    "Hợp Liêm Trinh tất tác công lại. Đồng Thái Âm hành tẩu, định hệ cửu lưu thuật sĩ. "
    "Nữ mệnh bất nghi ư phùng — thủy tính dương hoa. "
    "Cư Tỵ Dậu Sửu cung cư hầu bá. Vũ Tham tam hợp đồng viên, tướng tướng chi cách. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Lưu Niên Xương Khúc", ["lưu niên xương khúc", "văn xương văn khúc lưu niên", "khoa giáp", "thi cử trung quốc"],
    "Lưu niên Xương Khúc — Sao khoa giáp lưu niên. Mệnh phùng lưu niên Xương Khúc, vi khoa danh khoa giáp. "
    "Đại tiểu nhị hạn phùng chi, tam hợp củng chiếu Thái Dương, hựu chiếu lưu niên Lộc. "
    "Tiểu hạn Thái Tuế phùng Khôi Việt, Tả Hữu, Đài Tọa, Nhật Nguyệt, Khoa Quyền Lộc Mã tam phương củng chiếu, quyết nhiên cao trung. "
    "Nhị tinh tại Tỵ Dậu đắc địa, bất phú tức quý. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Tả Phụ", ["tả phụ trung quốc", "sao tả phụ", "tả phụ đế cực", "tả hữu phụ tá"],
    "Tả Phụ — Sao phụ tá Đế cực. Tả Phụ Đế cực chủ tể chi tinh, thủ thân mệnh chư cung hàng phúc. "
    "Chủ nhân hình mạo đôn hậu, phong lưu khảng khái. "
    "Tử Phủ Lộc Quyền nhược đắc tam hợp xung chiếu, chủ văn võ đại quý. "
    "Hỏa Kỵ xung phá, tuy phú quý bất cửu. "
    "Tăng đạo thanh nhàn. Nữ nhân hiền lương. "
    "Là 'thất chính' của Tử Vi: Tử Vi vô Tả Hữu như vua mất tay chân. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Hữu Bật", ["hữu bật trung quốc", "sao hữu bật", "hữu bật đế cực", "tả hữu phụ tá 2"],
    "Hữu Bật — Sao phụ tá Đế cực. Hữu Bật Đế cực chủ tể chi tinh, thủ thân mệnh văn mặc tinh thông. "
    "Tử Phủ cát tinh đồng viên, tài quan song mỹ, văn võ song toàn. "
    "Dương Đà Hỏa Kỵ xung phá, hạ cục đoán chi. "
    "Nữ nhân hiền lương hữu chí, dù tứ sát xung phá, bất vi hạ tiện. "
    "Hữu Bật tại phu thê cung, chủ nhân định nhị hôn. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Thiên Khôi Thiên Việt", ["thiên khôi thiên việt trung quốc", "khôi việt trung quốc", "quý nhân tinh", "khoa giáp quý nhân"],
    "Thiên Khôi, Thiên Việt — Sao quý nhân (thiên ất quý nhân). Khôi Việt Đẩu trung tư khoa chi tinh. "
    "Nhập mệnh tọa quý hướng quý, hoặc đắc Tả Hữu cát tụ vô bất phú quý. "
    "Lại vi thượng giới hòa hợp chi thần. Khôi lâm mệnh, Việt thủ thân, cánh điệp tương thủ. "
    "Ngộ Tử Phủ, Nhật Nguyệt, Xương Khúc, Tả Hữu, Quyền Lộc tương tấu, thiếu niên tất tụ mỹ thê. "
    "Ngộ đại nạn, tất đắc quý nhân thành tựu phụ trợ. "
    "Hạn bộ tuần phùng tất chủ nữ tử thiêm hỉ. Hậu học giả hữu công danh. "
    "Thân phùng Khôi Việt, vị cư đài phụ. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Lộc Tồn", ["lộc tồn trung quốc", "sao lộc tồn", "lộc tồn tước lộc", "lộc tồn phú quý"],
    "Lộc Tồn — Sao tước lộc. Bắc Đẩu đệ tam tinh, chân nhân chi tú, chủ nhân quý tước, chưởng nhân thọ cơ. "
    "Là sao tư tước quý tinh. Lão thành trì trọng, tâm từ cánh trực. "
    "Hỉ Tử Phủ Tướng Đồng Lương Nhật Nguyệt cập Vũ Khúc đồng cung. "
    "Đơn thủ thân mệnh — khán tài chi nô (người giữ của). "
    "Phạm không kiếp Hỏa Linh xung chiếu, vi hạ cục, xảo nghệ đa tinh. "
    "Hợp Tử Phủ Liêm Đồng tác Lộc Tồn thượng cục. "
    "Chư cung hàng phúc tiêu tai. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("phu_tinh", "Thiên Mã", ["thiên mã trung quốc", "sao thiên mã", "thiên mã dịch mã", "lộc mã giao trì"],
    "Thiên Mã — Sao dịch mã, chu du. Chư cung các hữu chế hóa. Tại thân mệnh lâm chi vị chi Dịch Mã. "
    "Hỉ Lộc Tồn, Tử Phủ, Xương Khúc thủ chiếu vi cát. "
    "Đồng Lộc Tồn đồng cung, vị chi Lộc Mã giao trì (chiết tiên mã). "
    "Tử Phủ đồng cung vị chi Phù Dư mã (xe ngựa). "
    "Hình sát đồng cung vị chi Phụ Thi mã. Hỏa tinh đồng cung vị chi Chiến mã. "
    "Nhật Nguyệt đồng cung vị chi Hùng thư mã (trống mái). "
    "Phùng không vong vị chi Tử mã, Vong mã (chết). "
    "Ngộ Đà La vị chi Chiết túc mã (què). "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("sat_tinh", "Dương", ["dương trung quốc", "sao dương", "đẩu dương", "hình", "thiên dương"],
    "Dương (Đẩu Dương) — Sao hình, hung tinh. Hỏa Kim, Bắc Đẩu phù tinh, hóa khí vi Hình. "
    "Nhập miếu quyền quý, thân vượng hình thô phá tướng. "
    "Cương cường quả quyết, hiếu dũng đấu hận, cơ mưu giảo trá. "
    "Hợp Tử Phủ tắc phúc lộc gia. Hội Nhật Nguyệt nam khắc thê nhi nữ khắc phu. "
    "Cư Mão Dậu hãm địa tác họa dương tai, tàn tật. "
    "Nữ mệnh nhập miếu quyền quý, hãm địa thương phu khắc tử. "
    "Thần Tuất Sửu Mùi nhập miếu. Tý Ngọ Mão Dậu hãm địa. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("sat_tinh", "Đà La", ["đà la trung quốc", "sao đà la", "đà la kỵ", "đà la bắc đẩu"],
    "Đà La — Sao kỵ, hung tinh. Hỏa Kim, Bắc Đẩu phù tinh, hóa khí vi Kỵ. "
    "Nhập miếu thân hùng hình thô, phú tính cương cường. "
    "Hoành phát hoành phá, bất thủ tổ nghiệp. "
    "Hội Nhật Nguyệt kỵ tú nam khắc thê nhi nữ khắc phu. "
    "Hội Xương Khúc Tả Hữu hữu ám chí ban ngân. "
    "Vô chính tinh nhi độc thủ mệnh giả, cô đơn khí tổ, nhập táng nhị tính. "
    "Nữ mệnh nội ngoan ngoại hư, lăng phu khắc tử. "
    "Thần Tuất Sửu Mùi nhập miếu. Dần Thân Tỵ Hợi hãm địa. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("sat_tinh", "Hỏa Tinh", ["hỏa tinh trung quốc", "sao hỏa tinh", "hỏa tinh nam đẩu", "hỏa tinh sát"],
    "Hỏa Tinh — Nam Đẩu phù tinh, sát tinh. Tính cương cường xuất chúng. "
    "Chư cung bất mỹ, duy Tham Lang miếu vượng đồng độ, chỉ nhật lập biên công. "
    "Lợi Đông Nam sinh nhân, bất lợi Tây Bắc. Hỉ Dần Mão Tỵ Ngọ sinh nhân vi họa giác khinh. "
    "Hợp Đẩu Dương đồng viên, tắc cường bảo tai ách, cô khắc hạ cục. "
    "Nữ mệnh tâm độc nội ngoan ngoại hư giảo trá. "
    "Hợp Tham Lang chủ phú quý — chỉ nhật lập biên công, phong hầu cư thượng tướng. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("sat_tinh", "Linh Tinh", ["linh tinh trung quốc", "sao linh tinh", "linh tinh nam đẩu", "linh tinh sát"],
    "Linh Tinh — Nam Đẩu trợ tinh, hung tinh. Đại sát Linh Tinh tướng, Nam Đẩu vi tòng thần. "
    "Giá trị nhân mệnh giả, tính cách diệc trầm ngâm. "
    "Nhược dữ Tham Lang hội, chỉ nhật lập biên đình. "
    "Miếu địa tài quan quý, hãm địa chủ cô bần. "
    "Dương Đà nhược tấu hợp, kỳ hình đại bất thanh. "
    "Thất Sát chủ trận vong. Phá Quân tài ốc khuynh. "
    "Liêm Túc Dương hình hội, kiếp không chủ đao binh. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("sat_tinh", "Địa Không Địa Kiếp", ["địa không địa kiếp trung quốc", "không kiếp", "sao không kiếp", "không vong"],
    "Địa Không và Địa Kiếp — Sao không vong, hung tinh. Nhị tinh thủ thân mệnh, ngộ cát tắc cát, ngộ hung tắc hung. "
    "Tứ sát xung chiếu, khinh giả hạ tiện, trọng giả lục súc chi mệnh. "
    "Định chủ phá tài, nhị hạn phùng chi tất hung. "
    "Ca: Kiếp không vi hại tối sầu nhân, tài trí anh hùng ngộ nhất thân. "
    "Chỉ hảo vi tăng tịnh học thuật, đôi kim tích ngọc dã tu bần. "
    "Hao tán phúc đức. Đại kỵ Tài Bạch, Quan Lộc cung. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tap_tinh", "Thiên Thương Thiên Sứ", ["thiên thương thiên sứ", "thiên thương", "thiên sứ", "tai họa"],
    "Thiên Thương và Thiên Sứ — Sao tai họa. Thiên Thương nãi thượng thiên hư hao chi thần. "
    "Thiên Sứ nãi thượng thiên truyền sứ chi thần. "
    "Thái tuế nhị hạn phùng chi, bất vấn đắc địa phủ. "
    "Chỉ yếu cát đa vi phúc, kỳ họa siêu khinh. "
    "Như vô cát, trị Cự Môn, Dương Đà, Hỏa Linh, Kỵ, Thiên Cơ, kỳ niên tất chủ quan tai, táng vong, phá bại. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tap_tinh", "Thiên Hình", ["thiên hình trung quốc", "sao thiên hình", "thiên hình tù ngục"],
    "Thiên Hình — Sao hình ngục. Thiên Hình thủ thân mệnh, bất vi tăng đạo định chủ cô hình. "
    "Bất yêu tắc bần. Phụ mẫu huynh đệ bất đắc toàn. "
    "Nhị hạn phùng chi chủ xuất gia, quan sự lao ngục thất tài. "
    "Nhập miếu tắc cát. Ca: Thiên hình vị tất thị hung tinh, nhập miếu danh vi Thiên Hỉ thần. "
    "Hội Xương Khúc cát tinh tất hiến sách đáo vương đình. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tap_tinh", "Thiên Diêu", ["thiên diêu trung quốc", "sao thiên diêu", "thiên diêu đào hoa"],
    "Thiên Diêu — Sao đào hoa. Thiên Diêu thủ thân mệnh, tâm tính âm độc, đa nghi, phong lưu đa tỳ, chủ dâm. "
    "Nhập miếu vượng chủ phú quý đa nô. Cư Hợi hữu học thức. "
    "Hội ác tinh phá gia bại sản, nhân sắc phạm hình. Lục hợp trùng phùng, thiếu niên yêu chiết. "
    "Nhược lâm hạn, bất dụng môi sóc, chiêu thủ thành hôn. "
    "Hội Tử Vi cát tinh gia, cương nhu tương tế, chủ phong tao. "
    "Gia Hồng Loan dâm, gia hình nhận yểu. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tap_tinh", "Thiên Khốc Thiên Hư", ["thiên khốc thiên hư", "thiên khốc", "thiên hư", "tang sự"],
    "Thiên Khốc và Thiên Hư — Sao tang sự, khóc hư. Khốc Hư vi ác diệu, lâm mệnh tối phi thường. "
    "Gia lâm Phụ Mẫu nội, phá đãng mại điền trang. "
    "Nhược giáo thân mệnh hãm, cùng độc đới hình thương. "
    "Lục thân đa bất túc, phiền não quá thời quang. "
    "Sửu Mão Thân cung cát, ngộ Lộc danh hiển dương. "
    "Nhị hạn nhược phùng chi, ai ai khốc đoạn trường. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

# ===== Tứ Hóa (诸星问答论) =====

_add("tu_hoa", "Hóa Lộc", ["hóa lộc trung quốc", "hóa lộc phúc đức", "hóa lộc tứ hóa", "lộc trung quốc"],
    "Hóa Lộc — Sao phúc đức, tài lộc. Lộc vi phúc đức chi thần. "
    "Thủ thân mệnh Quan Lộc chi vị. Khoa Quyền tương phùng, tất tác đại thần chi chức. "
    "Tiểu hạn phùng chi chủ tiến tài nhập sĩ chi hỉ. Đại hạn thập niên kiết khánh vô nghi. "
    "Ác diệu lai lâm tịnh Dương Đà Hỏa Kỵ xung chiếu, diệc bất vi hại. "
    "Nữ nhân cát tấu tác mệnh phụ. Nhị hạn phùng chi, nội ngoại uy nghiêm. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tu_hoa", "Hóa Quyền", ["hóa quyền trung quốc", "hóa quyền quyền lực", "hóa quyền sinh sát", "quyền trung quốc"],
    "Hóa Quyền — Sao quyền lực, sinh sát. Quyền tinh chưởng phán sinh sát chi thần. "
    "Thủ thân mệnh Khoa Lộc tương phùng xuất tướng nhập tướng. "
    "Khoa Quyền tương phùng tất định văn chương quán thế, nhân giai khâm ngưỡng. "
    "Tiểu hạn tương phùng, vô hữu bất cát. Đại hạn thập niên, tất nhiên toại chí. "
    "Như phùng Dương Đà háo sử kiếp không, thính sấm lụy, quan tai biếm trích. "
    "Nữ nhân đắc chi, nội ngoại xưng chí, khả tác mệnh phụ. "
    "Tăng đạo chưởng sơn lâm hữu sư hiệu. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tu_hoa", "Hóa Khoa", ["hóa khoa trung quốc", "hóa khoa văn mặc", "hóa khoa ứng thí", "khoa trung quốc"],
    "Hóa Khoa — Sao văn mặc, khoa cử. Khoa tinh thượng giới ứng thí, chủ chưởng văn mặc chi tinh. "
    "Thủ thân mệnh Quyền Lộc tương phùng tể tướng chi quý. "
    "Như phùng ác diệu diệc vi văn chương tú sĩ, khả tác quần anh sư phạm. "
    "Nữ mệnh cát củng, chủ quý phong tặng. "
    "Tuy tứ sát xung phá, diệc vi phú quý. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

_add("tu_hoa", "Hóa Kỵ", ["hóa kỵ trung quốc", "hóa kỵ đa quản", "hóa kỵ tai họa", "kỵ trung quốc"],
    "Hóa Kỵ — Sao tai họa, đa quản. Kỵ vi đa quản chi thần. "
    "Thủ thân mệnh nhất sinh bất thuận. Tiểu hạn phùng chi nhất niên bất túc. Đại hạn thập niên hối hận. "
    "Nhị hạn Thái Tuế giao lâm, đoạn nhiên trắc đặng. "
    "Văn nhân bất nại cửu, vũ nhân túng hữu quan tai khẩu thiệt bất phòng. "
    "Như hội Tử Phủ, Xương Khúc, Tả Hữu, Khoa Quyền Lộc dữ Kỵ đồng cung, hựu kiêm tứ sát cộng xứ, tức phát tài diệc bất giai. "
    "Như đơn phùng tứ sát, háo sử, kiếp không, chủ bôn ba đới tật. "
    "[Nguồn: 紫微斗数全书 诸星问答论]")

# ===== 形性赋 =====

_add("co_thu", "Hình Tính Phú", ["hình tính phú trung quốc", "hình tính phú", "tướng mạo tính cách tử vi", "hình tính phú cổ văn", "tướng sao"],
    "Hình Tính Phú (紫微斗数全书 quyển 1) — Luận tướng mạo và tính cách qua sao:\n\n"
    "Tử Vi: tướng hậu trọng (đôn hậu, to lớn). Thiên Phủ: thuần hòa.\n"
    "Thái Dương (Kim Ô) viên mãn, Thái Âm (Ngọc Thố) thanh kỳ.\n"
    "Thiên Cơ: không dài không ngắn, tâm hoài hảo thiện.\n"
    "Vũ Khúc: chí yếu chí khẩn chi thao, tâm tính quả quyết.\n"
    "Thiên Đồng: phì mãn, mục tú thanh kỳ.\n"
    "Liêm Trinh: mi khoan, khẩu khoát, diện hoành — tính bạo, hiếu phẫn hiếu tranh.\n"
    "Tham Lang: vi thiện ác chi tinh. Nhập miếu ưng trường tủng (dáng cao), xuất viên tất ngoan tiêu.\n"
    "Cự Môn: thị phi chi diệu. Tại miếu đôn hậu ôn lương.\n"
    "Thiên Tướng: tinh thần. Thiên Lương: ổn trọng, tâm sự ngọc khiết băng thanh.\n"
    "Thất Sát: như Tử Lộ bạo hổ bằng hà (mạnh mẽ liều lĩnh).\n"
    "Hỏa Linh: tự Dự Nhưỡng thôn thán trang ngả.\n"
    "Văn Xương: tuấn nhã, mi thanh mục tú.\n"
    "Văn Khúc: lỗi lạc, khẩu thiệt tiện nịnh. Tại miếu định sinh dị chí, thất hãm tất hữu ban ngân.\n"
    "Tả Phụ Hữu Bật: ôn lương quy mô, đoan trang cao sĩ.\n"
    "Thiên Khôi Thiên Việt: cụ túc uy nghi.\n"
    "Dương Đà La: hình xú mạo thô, hữu kiểu trá thể thái.\n"
    "Phá Quân: bất nhân, bối trọng mi khoan, hành tọa yêu tà, gian trá hiếu hành kinh hiểm.\n"
    "Lộc Tồn: tính mạo như xuân hòa ái.\n"
    "[Nguồn: 紫微斗数全书 形性赋 - gushiwen.cn]")

# ===== 星垣论 =====

_add("co_thu", "Tinh Viên Luận", ["tinh viên luận trung quốc", "tinh viên luận", "ngũ hành cung vị", "sao và cung trung quốc"],
    "Tinh Viên Luận (紫微斗数全书 quyển 1) — Luận ngũ hành tương sinh tương khắc giữa sao và cung:\n\n"
    "Tử Vi Đế tọa dĩ Phụ Bật vi tá nhị, tác số trung chi chủ tinh. "
    "Nam Bắc nhị đẩu tập nhi thành số, vi vạn vật chi linh.\n\n"
    "Quan hệ ngũ hành:\n"
    "Dần (Mộc): tam dương giao thái, thảo mộc manh nha. Tham Lang Thiên Cơ nhập miếu. "
    "Thiên Tướng thủy đáo Dần vi vượng tướng.\n"
    "Mão (Mộc): Cự Môn thủy đắc Mão vi sơ thông.\n"
    "Tỵ (Hỏa): thủy thổ tuyệt chi địa. Liêm Trinh Mộc cư yên.\n"
    "Ngọ (Hỏa): nhật lệ trung thiên, Văn Khúc thủy nhập miếu.\n"
    "Thân Dậu (Kim): Vũ Khúc cư Thân nhi hảo sinh. Dương cư Dậu nhi dụng sát.\n"
    "Hợi (Thủy): Văn Khúc Phá Quân chi miếu địa, văn minh thanh cao chi sĩ.\n"
    "Tý (Thủy): Phá Quân thủy ư Tý vượng chi hương, như cự hải chi lãng.\n\n"
    "Chư sao y ngũ hành suy chi thân mệnh, vô thi bất khả. "
    "[Nguồn: 紫微斗数全书 星垣论 - liuyunling.com/345]")

# ===== 增补太微赋 =====

_add("co_thu", "Tăng Bổ Thái Vi Phú", ["tăng bổ thái vi phú", "bổ sung thái vi phú", "thái vi phú bổ sung", "cổ văn luận đoán"],
    "Tăng Bổ Thái Vi Phú (紫微斗数全书) — Những câu quyết bổ sung:\n\n"
    "- Tiền hậu lưỡng hung thần: lưỡng lân gia vũ thượng khả xanh trì, đồng thất dữ mưu tối nan đề phòng.\n"
    "  (Hung thần trước sau: láng giềng hai bên còn có thể chống đỡ, nhưng trong cùng một nhà thì khó phòng nhất)\n"
    "- Phiến hỏa phần thiên mã, trọng dương trục lộc tồn.\n"
    "  (Lửa nhỏ đốt cháy Thiên Mã, nhiều Dương đuổi Lộc Tồn)\n"
    "- Hung bất giai hung, cát vô thuần cát.\n"
    "  (Hung không hoàn toàn hung, cát không thuần cát)\n"
    "- Chủ cường tân nhược khả bảo vô ngu, chủ nhược tân cường hung nguy lập kiến.\n"
    "  (Chủ mạnh khách yếu thì vô sự; chủ yếu khách mạnh thì nguy hiểm thấy ngay)\n"
    "- Thân mệnh tối hiềm Dương Đà Thất Sát, ngộ chi vị miễn vi hung.\n"
    "  (Thân mệnh kỵ nhất Dương Đà Thất Sát, gặp ắt hung)\n"
    "- Nhị hạn thậm kỵ Tham Phá Cự Liêm, phùng chi định nhiên tác họa.\n"
    "  (Đại tiểu hạn rất kỵ Tham Phá Cự Liêm, gặp ắt có họa)\n"
    "- Phàm quan nữ nhân chi mệnh, tiên quan phu tử nhị cung.\n"
    "  (Xem mệnh nữ trước hết xem Phu Thê và Tử Nữ cung)\n"
    "- Mệnh ngộ Khôi Xương thường đắc quý, hạn phùng Tử Phủ định tài đa.\n"
    "  (Mệnh gặp Khôi Xương thường được quý, hạn gặp Tử Phủ ắt giàu)\n"
    "- Văn Xương Văn Khúc Thiên Khôi tú, bất độc thi thư dã khả nhân.\n"
    "  (Không đọc sách vẫn giỏi nhờ Xương Khúc Khôi)\n"
    "- Long đồ hạn nhược, thủy thượng phù bào; lão nhân hạn suy, phong trung nhiên chúc.\n"
    "  (Trẻ yếu thì như bọt nước; già suy thì như đèn trước gió)\n"
    "Phiến hỏa phần thiên mã — lửa nhỏ đốt cháy Thiên Mã: chuyện nhỏ gây họa lớn. "
    "Hai hung thần kề nhau: láng giềng còn đỡ, đồng cung thì khó phòng. "
    "[Nguồn: 紫微斗数全书 增补太微赋 - liuyunling.com/379]")

# ===== 重补斗数彀率 =====

_add("co_thu", "Trọng Bổ Đẩu Số Cấu Suất", ["trọng bổ đẩu số cấu suất", "cấu suất", "trọng bổ", "câu quyết cổ văn"],
    "Trọng Bổ Đẩu Số Cấu Suất (紫微斗数全书) — Các câu quyết căn bản:\n\n"
    "- Chư tinh cát, đa phùng hung dã cát. Chư tinh ác, đa phùng cát dã hung.\n"
    "  (Sao cát nhiều, gặp hung cũng cát; sao ác nhiều, gặp cát cũng hung)\n"
    "- Đại khái dĩ thân mệnh vi họa phúc chi bính, dĩ căn nguyên vi cùng thông chi cơ.\n"
    "  (Đại khái thân mệnh là then chốt họa phúc, căn nguyên là cơ cùng thông)\n"
    "- Tử Vi tại mệnh Phụ Bật đồng viên, kỳ quý tĩ hĩ.\n"
    "- Tài Ấn giáp mệnh, Nhật Nguyệt giáp tài, kỳ phú hà nghi.\n"
    "  (Tài là Vũ Khúc, Ấn là Thiên Tướng kẹp mệnh; Mặt Trời Mặt Trăng kẹp tài — quý cách)\n"
    "- Âm Phúc lâm bất phạ hung xung, Nhật Nguyệt hội bất như hợp chiếu.\n"
    "  (Thiên Lương Thiên Đồng không sợ hung xung; Nhật Nguyệt đồng cung không bằng hợp chiếu)\n"
    "- Tham Lang cư Tý nãi vi phiếm thủy đào hoa.\n"
    "- Tử Vi tọa mệnh khố tắc viết Kim Dư bổng ngự liễn.\n"
    "- Lộc hợp thủ Điền Tài vi lạn cốt đôi kim.\n"
    "  (Lộc chiếu Điền Tài như kho vàng)\n"
    "- Sát cư tuyệt địa sinh thành tam thập nhị chi Nhan Hồi.\n"
    "  (Sát cư tuyệt địa như Nhan Hồi chết non)\n"
    "- Nhật tại vượng cung khả học bát bách niên chi Bành Tổ.\n"
    "  (Mặt Trời miếu vượng có thể sống như Bành Tổ)\n"
    "Đây là những câu quyết căn bản cần thuộc lòng. "
    "[Nguồn: 紫微斗数全书 重补斗数彀率 - liuyunling.com/377]")

# ===== 斗数发微论 =====

_add("co_thu", "Đẩu Số Phát Vi Luận", ["đẩu số phát vi luận", "phát vi luận", "bạch ngọc thiền", "bạch ngọc thiên"],
    "Đẩu Số Phát Vi Luận (白玉蟾先生) — Bạch Ngọc Thiên nói về Đẩu Số:\n\n"
    "Quan thiên đấu số dữ ngũ tinh bất đồng, án thử tinh thần dữ chư thuật đại dị.\n"
    "Xem Tử Vi khác với Tử Bình (ngũ tinh).\n\n"
    "- Tứ chính cát tinh định vi quý, tam phương sát củng thiếu vi kỳ.\n"
    "  (Tứ chính (tam hợp + xung chiếu) có cát tinh thì quý; tam hợp có sát củng thì hiếm lạ)\n"
    "- Đối chiếu tường tường hung tường cát; hợp chiếu quan tiện quan vinh.\n"
    "  (Xung chiếu thì rõ hung cát; hợp chiếu thì xem sang hèn)\n"
    "- Cát tinh nhập viên tắc vi cát; hung tinh thất địa tắc vi hung.\n"
    "- Mệnh phùng Tử Vi phi đặc thọ nhi thả vinh; thân ngộ sát tinh bất đản bần nhi thả tiện.\n"
    "  (Mệnh có Tử Vi không chỉ thọ mà còn vinh; thân gặp sát tinh chẳng những bần mà còn tiện)\n"
    "- Tả Hữu hội ư Tử Phủ, cực phẩm chi tôn.\n"
    "- Khoa Quyền hãm ư hung hương, công danh trắc đặng.\n"
    "  (Khoa Quyền hãm ở hung địa thì công danh trắc trở)\n"
    "- Dương Đà Thất Sát hạn vận mạc phùng, phùng chi định hữu hình thương.\n"
    "- Nam Đẩu chủ hạn tất sinh nam; Bắc Đẩu gia lâm tiên đắc nữ.\n"
    "  (Đại hạn Nam Đẩu chủ sinh con trai; Bắc Đẩu chủ trước có gái)\n"
    "- Quan Lộc ngộ Tử Phủ, phú nhi thả quý.\n"
    "- Điền Trạch ngộ Phá Quân, tiên phá hậu thành.\n"
    "[Nguồn: 紫微斗数全书 斗数发微论 - liuyunling.com/367]")

# ===== 斗数准绳 =====

_add("co_thu", "Đẩu Số Chuẩn Thằng", ["đẩu số chuẩn thằng", "chuẩn thằng", "đẩu số chuẩn", "câu quyết luận đoán"],
    "Đẩu Số Chuẩn Thằng (紫微斗数全书) — Các câu quyết chuẩn xác:\n\n"
    "- Đấu số chí huyền chí vi, lý chỉ nan minh. Tuy thiết vấn ư các thiên chi trung, do hữu ngôn nhi vị tận.\n"
    "- Tinh hữu đồng triền, số hữu phân định. Tất minh kỳ sinh khắc chi yếu, tất tường hồ đắc viên thất độ chi phân.\n"
    "- Lộc phùng xung phá, cát xứ tàng hung. Mã ngộ không vong, chung thân bôn tẩu.\n"
    "- Nhật Nguyệt tối hiềm phản bối, Lộc Mã tối hỉ giao trì.\n"
    "- Cát tinh gia lâm, phùng hung dã cát. Hung tinh tụ tấu, ngộ cát diệc hung.\n"
    "- Nhất sinh cần lao: Dương Đà cư tật ách. Nhất sinh tao phá: Hỏa Linh cư điền tài.\n"
    "- Cung hảo thân lai tùng, cung hãm thân hậu khứ.\n"
    "  (Cung tốt thì thân đến theo; cung hãm thì thân bỏ đi)\n"
    "- Mệnh tọa không vong, tài nguyên bất tụ. | Mệnh ngồi không vong, tài chẳng tụ.\n"
    "- Đại hạn ngộ Tử: hỉ khí tự nhiên tân. | Đại hạn gặp Tử Vi: hỉ khí tự nhiên mới.\n"
    "[Nguồn: 紫微斗数全书 斗数准绳 - liuyunling.com/346]")

# ===== 谈星要论 =====

_add("co_thu", "Đàm Tinh Yếu Luận", ["đàm tinh yếu luận", "bàn về sao", "yếu luận", "cổ văn luận tinh"],
    "Đàm Tinh Yếu Luận (紫微斗数全书 quyển 3) — Bàn về những điểm chính yếu của tinh diệu:\n\n"
    "Đấu số dĩ thập nhị cung vi kinh, thập tứ chính tinh vi vĩ, tứ hóa vi cơ biến. "
    "Thập nhị chi trung đệ nhất yếu mệnh thân, kế chi tài bạch, quan lộc, điền trạch, phúc đức. "
    "Luận phú quý tiên khán tài bạch điền trạch, luận quý hiển tiên khán quan lộc mệnh thân. "
    "Luận phối ngẫu khán phu thê cung, luận tử tức khán tử nữ cung. "
    "Chư tinh đắc địa vi cát, thất hãm vi hung. Miếu vượng tắc kỳ lực cường, hãm tắc kỳ lực nhược. "
    "Tuy nhiên diệc yếu khán sinh khắc chế hóa. "
    "[Nguồn: 紫微斗数全书 quyển 3 谈星要论]")

# ===== 论男女命同异 =====

_add("co_thu", "Luận Nam Nữ Mệnh Đồng Dị", ["luận nam nữ mệnh", "nam mệnh nữ mệnh", "nam nữ trung quốc", "mệnh nam nữ khác"],
    "Luận Nam Nữ Mệnh Đồng Dị (紫微斗数全书 quyển 3):\n\n"
    "Nam mệnh dĩ sự nghiệp, tài phú vi trọng; nữ mệnh dĩ phu tử, đức hạnh vi tiên.\n"
    "Nam nhi Thất Sát vi tướng tinh; nữ nhi Thất Sát vi khắc tinh.\n"
    "Nam nhi Tham Lang vi tài hoa; nữ nhi Tham Lang vi dâm đãng.\n"
    "Nam nhi Dương Đà vi quyền quý; nữ nhi Dương Đà vi hình khắc.\n"
    "Bất quá tẫn yếu khán cung vị miếu hãm, cát hung chế hóa.\n"
    "Nhập miếu tắc cát, hãm địa tắc hung. Nam giả hữu quyền, nữ giả hữu phúc. "
    "[Nguồn: 紫微斗数全书 quyển 3]")

# ===== 十二宫诸星得地合格诀 =====

_add("cach_cuc", "Thập Nhị Cung Chư Tinh Đắc Địa Hợp Cách", ["thập nhị cung đắc địa", "chư tinh đắc địa", "miếu vượng hợp cách", "đắc địa trung quốc"],
    "Thập Nhị Cung Chư Tinh Đắc Địa Hợp Cách Quyết (紫微斗数全书):\n"
    "Nhất mệnh nhị huynh đệ tam phu thê, tứ tử ngũ tài lục tật ách. "
    "Thất thiên bát nô cửu quan lộc, thập điền thập nhất phúc thập nhị phụ mẫu.\n\n"
    "Đắc địa nhất lãm:\n"
    "- Mệnh: Tử Phủ đồng cung, Nhật Nguyệt đồng cung, Tướng Ấn đồng cung, Thiên Lương nhập miếu\n"
    "- Tài Bạch: Vũ Khúc Thái Âm miếu vượng, Thiên Phủ Lộc Tồn đồng cung\n"
    "- Quan Lộc: Tử Vi Thái Dương miếu vượng, Liêm Trinh nhập miếu cát\n"
    "- Điền Trạch: Tử Phủ miếu vượng, Thiên Phủ Lộc Tồn đồng cung\n"
    "- Phúc Đức: Thiên Đồng miếu vượng, Nhật Nguyệt đồng cung\n"
    "- Phu Thê: Tử Vi miếu vượng cát, Xương Khúc nhập miếu\n"
    "- Tử Nữ: Tử Phủ cát tinh hội, Thiên Tướng đồng cung\n"
    "[Nguồn: 紫微斗数全书 quyển 1]")

_add("cach_cuc", "Thập Nhị Cung Chư Tinh Thất Hãm Phá Cách", ["thập nhị cung thất hãm", "chư tinh thất hãm", "thất hãm phá cách", "hãm địa trung quốc"],
    "Thập Nhị Cung Chư Tinh Thất Hãm Phá Cách Quyết (紫微斗数全书):\n"
    "- Mệnh không chính diệu hựu phùng sát; Thân mệnh sát tinh xung phá\n"
    "- Tài Bạch: thất hãm không kiếp xung; Vũ Khúc hãm phá quân đồng<br>"
    "- Quan Lộc: không kiếp xung phá; Liêm Trinh sát tinh đồng vị<br>"
    "- Điền Trạch: Phá Quân xung phá; Hỏa Linh cư điền trạch<br>"
    "- Phúc Đức: không kiếp đồng cung; Tham Phá hãm thủ phúc<br>"
    "- Phu Thê: Liêm Trinh Thất Sát đồng vị; Cự Môn hãm thủ phu thê<br>"
    "- Tật Ách: Dương Đà hãm thủ; Không kiếp hãm tật ách<br>"
    "Mệnh vô chính diệu hựu phùng sát; Tài Bạch thất hãm gia Không Kiếp; Thân cung nô bộc hữu sát kỵ."
    "[Nguồn: 紫微斗数全书 quyển 1]")

# ===== 羊陀火铃四星总论 + 二星总论 =====

_add("sat_tinh", "Dương Đà Hỏa Linh Tứ Tinh Tổng Luận", ["dương đà hỏa linh", "tứ sát", "dương đà hỏa linh tổng luận", "ngọc thiền dương đà"],
    "Dương Đà Hỏa Linh Tứ Sát Tổng Luận (玉蟾先生):\n"
    "Hỏa Linh Đà La Kim, Dương hình Kỵ quyết. Nhất danh Mã Tảo tinh, hựu danh Đoản Thọ sát.\n"
    "Quân tử thất kỳ quyền, tiểu nhân phạm hình pháp. Cô độc khắc lục thân, tai họa thường bất hát. "
    "Yêu túc thần xỉ thương, lao lộc đa kiển bác. Phá tướng hựu lao tâm, khởi cái điền câu hác. "
    "Vũ Khúc tịnh Tham Lang, nhất thế chiêu hung ác. Tật ách nhược phùng chi, tứ thời bất ly trước. "
    "Chỉ nghi sơn tự tăng, kim cốc thường an lạc.\n\n"
    "Dương Đà nhị tinh tổng luận: Dương hóa khí vi Hình, Đà hóa khí vi Kỵ. "
    "Phạ lâm Huynh Đệ, Điền Trạch, Phụ Mẫu tam cung. "
    "Kỵ tam hợp lâm thân mệnh, hợp Xương Khúc Tả Hữu hữu ám chí nhãn chí. "
    "Kiến Nhật Nguyệt nữ khắc phu nhi phu khắc phụ (đàn bà khắc chồng, đàn ông khắc vợ). "
    "Vi chư cung chi hung thần. "
    "[Nguồn: 紫微斗数全书 诸星问答论 - iztro.com]")

# ===== 定杂局 =====

_add("cach_cuc", "Định Tạp Cục", ["định tạp cục", "tạp cục", "cách cục phụ"],
    "Định Tạp Cục (紫微斗数全书):\n"
    "Tạp cục là những cách cục không thuần phú quý bần tiện:\n"
    "- Tăng đạo cách: Thiên Cơ Thiên Lương đồng cung; Không Kiếp thủ mệnh; Sát tinh nhiều mà có giải\n"
    "- Kỹ nghệ cách: Hỏa Linh Tham Lang hội; Xương Khúc hãm thủ; Cơ Nguyệt đồng cung\n"
    "- Thương cổ cách: Lộc Mã giao trì (xê dịch kiếm tiền); Tử Phủ cư thiên di\n"
    "- Hình ngục cách: Liêm Trinh hãm hội sát tinh; Hình Kỵ đồng cung\n"
    "- Yểu cách (chết non): Sát cư tuyệt địa; Không Kiếp sát tinh giáp mệnh\n"
    "- Tuyệt tự cách (không con): Tử Nữ cung hoàn toàn sát kỵ; không chính diệu\n"
    "[Nguồn: 紫微斗数全书 quyển 1 定杂局]")

# ===== 定富局 定贵局 定贫贱局 =====

_add("cach_cuc", "Định Phú Quý Bần Tiện Cách", ["định phú quý", "định bần tiện", "định phú cục", "định quý cục", "định bần tiện cục"],
    "Định Phú Quý Bần Tiện Cục (紫微斗数全书):\n\n"
    "Định Phú Cục:\n"
    "- Tử Vi Phụ Bật đồng cung phú\n"
    "- Vũ Khúc Thái Âm miếu vượng phú\n"
    "- Thiên Phủ Lộc Tồn đồng cung phú\n"
    "- Nhật Nguyệt giáp tài phú\n"
    "- Lộc Mã giao trì phú\n"
    "- Tài Ấn giáp mệnh phú\n\n"
    "Định Quý Cục:\n"
    "- Tử Vi Khôi Việt đồng cung quý\n"
    "- Nhật Nguyệt thủ chiếu quý\n"
    "- Phụ Bật giáp Đế quý\n"
    "- Khoa Quyền Lộc giáp mệnh quý\n"
    "- Thiên Tướng miếu vượng tại Quan Lộc quý\n\n"
    "Định Bần Tiện Cục:\n"
    "- Mệnh vô chính diệu hựu phùng sát\n"
    "- Tài Bạch thất hãm gia Không Kiếp\n"
    "- Thân cung nô bộc hữu sát kỵ\n"
    "- Liêm Trinh Thất Sát đồng vị (lộ thượng mai thi: chết đường chết chợ)\n"
    "- Phá Quân ám diệu đồng hương (thủy trung tác trủng: chết nước)"
    "[Nguồn: 紫微斗数全书 quyển 1]")

# ===== 杀破狼 =====

_add("cach_cuc", "Sát Phá Lang", ["sát phá lang trung quốc", "thất sát phá quân tham lang", "sát phá lang biến động", "biến động tam giác"],
    "Sát Phá Lang — Bộ ba sao biến động mãnh liệt nhất trong Tử Vi: Thất Sát, Phá Quân, Tham Lang.\n\n"
    "Thất Sát: Nam Đẩu đệ lục tinh, tướng tinh. Đẩu trung chi thượng tướng, thực thành bại chi cô thần. "
    "Có Tử Vi chế hóa thì thành quyền lực, mất chế hóa thì hung. "
    "Gặp Hỏa Linh thì tăng thêm sát uy. Cuộc đời thăng trầm lớn.\n\n"
    "Phá Quân: Bắc Đẩu đệ thất tinh, hao tinh. Tại thiên vi sát khí, tại số vi hao. "
    "'Tiên phá hậu lập' — phá trước xây sau. Cực ghét trì trệ.\n\n"
    "Tham Lang: Bắc Đẩu đệ nhất tinh, đào hoa. Chủ họa phúc. Đa tài đa nghệ, cao thủ giao tiếp.\n\n"
    "Sát Phá Lang luôn ở tam hợp với nhau (Dần Thân Tỵ Hợi), tạo 'biến động thiết tam giác'. "
    "Khi đại hạn hoặc lưu niên kích hoạt, ắt có biến đổi lớn. "
    "[Nguồn: 紫微斗数全书 + zhunsuan.org]")

# ===== 太微赋 =====

_add("co_thu", "Thái Vi Phú", ["thái vi phú", "thái vi phú trung quốc", "thái vi phú đấu số", "cổ văn thái vi phú"],
    "Thái Vi Phú (紫微斗数全书 quyển 1):\n"
    "Đấu số chí huyền chí vi, lý chỉ nan minh. Tuy thiết vấn ư các thiên chi trung, do hữu ngôn nhi vị tận. "
    "Chí như tinh chi phân dã, các hữu sở thuộc, thọ yêu hiền ngu, phú quý bần tiện, bất khả nhất luận nghị.\n\n"
    "**Các câu quyết then chốt:**\n"
    "- Lộc phùng xung phá, cát xứ tàng hung.\n"
    "- Mã ngộ không vong, chung thân bôn tẩu.\n"
    "- Nhật Nguyệt tối hiềm phản bối, Lộc Mã tối hỉ giao trì.\n"
    "- Tử Vi Thiên Phủ toàn y Phụ Bật chi công, Thất Sát Phá Quân chuyên y Dương Linh chi nộ.\n"
    "- Chư tinh cát, phùng hung dã cát. Chư tinh hung, phùng hung dã hung.\n"
    "- Phụ Bật giáp Đế vi thượng phẩm, Đào hoa phạm chủ vi chí dâm.\n"
    "- Quân thần khánh hội, tài thiện kinh bang. Khôi Việt đồng hành, vị cư đài phụ.\n"
    "- Thất Sát Liêm Trinh đồng vị, lộ thượng mai thi.\n"
    "- Phá Quân ám diệu đồng hương, thủy trung tác trủng.\n"
    "- Thái Dương cư Ngọ, vị chi nhật lệ trung thiên, hữu chuyên quyền chi quý, địch quốc chi phú.\n"
    "- Thái Âm cư Tý, hiệu viết thủy trừng quế ngạc, đắc thanh yếu chi chức, trung gián chi tài.\n"
    "[Nguồn: 紫微斗数全书 太微赋]")

_add("phai", "Phân Loại Sao Trung Quốc", ["phân loại sao trung quốc", "bắc đẩu nam đẩu", "chính diệu phụ diệu", "phân loại tinh diệu"],
    "Phân loại sao Tử Vi theo truyền thống Trung Quốc:\n\n"
    "Theo Bắc Đẩu / Nam Đẩu / Trung Thiên:\n"
    "- Bắc Đẩu: Tử Vi, Tham Lang, Vũ Khúc, Cự Môn, Liêm Trinh, Phá Quân, Tả Phụ, Hữu Bật, Lộc Tồn, Văn Khúc, Dương, Đà La\n"
    "- Nam Đẩu: Thiên Phủ, Thiên Cơ, Thiên Tướng, Thiên Lương, Thiên Đồng, Thất Sát, Văn Xương, Thiên Khôi, Thiên Việt, Linh Tinh, Hỏa Tinh\n"
    "- Trung Thiên: Thái Dương, Thái Âm và các sao còn lại\n\n"
    "Theo tính chất:\n"
    "- Chính Diệu (14 chủ tinh): Tử Vi, Vũ Khúc, Thiên Cơ, Tham Lang, Thái Dương, Thiên Đồng, Liêm Trinh, Thiên Phủ, Cự Môn, Thái Âm, Thiên Tướng, Thiên Lương, Thất Sát, Phá Quân\n"
    "- Phụ Diệu: Tả Phụ, Hữu Bật, Thiên Khôi, Thiên Việt\n"
    "- Tá Diệu: Văn Xương, Văn Khúc, Thiên Mã, Lộc Tồn\n"
    "- Sát Diệu: Linh Tinh, Hỏa Tinh, Địa Không, Địa Kiếp, Dương, Đà La\n"
    "- Hóa Diệu: Hóa Lộc, Hóa Khoa, Hóa Quyền, Hóa Kỵ\n"
    "[Nguồn: zhihu.com 紫微斗数知识大全]")
