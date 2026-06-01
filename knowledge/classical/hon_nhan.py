"""
HÔN NHÂN TỬ VI — Kiến thức hôn nhân & hợp hôn

Nguồn:
  - Ni Hải Hạ (倪海厦) Thiên Kỷ hệ thống
  - Tử Vi Đẩu Số Toàn Thư (紫微斗数全书)
  - Tổng hợp và Việt hóa

Lưu ý: Các luận đoạn cổ điển đã được Việt hóa và điều chỉnh cho phù hợp
với bối cảnh xã hội hiện đại, tránh mê tín cực đoan.
"""

STAR_IN_MARRIAGE_PALACE = {
    "Tử Vi": {
        "summary": "Phối ngẫu có địa vị, kiêu hãnh, nên kết hôn muộn. Tình cảm trên cơ sở tôn trọng.",
        "good": "Có Tả Hữu kèm: vợ/chồng tài giỏi, cưới xong được quý nhân giúp. Có hóa Lộc: tiền tài.",
        "bad": "Không phụ tá: vợ/chồng mạnh mẽ khó gần. Tại Thìn/Tuất: tình cảm nhạt nhòa. Gặp Phá Quân: trước cưới nhiều trở ngại.",
        "spouse": "Phối ngẫu có khí chất cao, tự trọng cao, mạnh mẽ nhưng ít bộc lộ tình cảm.",
        "timing": "Nên cưới muộn (nam >30, nữ >27). Cưới sớm dễ đổ vỡ.",
        "ni_quote": "Tử Vi tại Phu Thê, cô khắc, nên cưới muộn, tình cảm tốt nhưng chi phí giao tiếp cao.",
    },
    "Thiên Cơ": {
        "summary": "Hôn nhân dễ thay đổi, nên chọn người chênh lệch tuổi tác lớn.",
        "good": "Có Lộc Tồn/hóa Lộc: tình cảm tạm ổn. Gặp Thái Âm: thêm dịu dàng tinh tế.",
        "bad": "Hóa Kỵ hoặc nhiều sát tinh: tình cảm thay đổi thất thường, dễ chia ly.",
        "spouse": "Phối ngẫu thông minh, tinh tế, có khi hơi thần kinh, hay thay đổi.",
        "timing": "Nên chênh lệch tuổi ≥6 để giảm xung đột.",
        "ni_quote": "Thiên Cơ thiện biến, bất nghi độc tọa, hôn nhân tràn đầy biến hóa.",
    },
    "Thái Dương": {
        "summary": "Nam mệnh tốt cho vợ, nữ mệnh tốt cho chồng. Nếu Hãm hoặc Hóa Kỵ thì ngược lại.",
        "good": "Miếu Vượng (Mão→Thân): vợ/chồng giỏi giang, hôn nhân tốt.",
        "bad": "Hãm (Dậu→Dần): vợ/chồng yếu, hôn nhân khó khăn. Hóa Kỵ (nữ): chồng gặp tai họa lớn.",
        "spouse": "Phối ngẫu cởi mở, hào phóng, có ý thức công chúng, đôi khi hơi mạnh mẽ quá.",
        "timing": "Tình cảm nóng đầu lạnh cuối, cần giữ khoảng cách để duy trì sự mới mẻ.",
    },
    "Vũ Khúc": {
        "summary": "Sao cô độc, hôn nhân dễ có trở ngại — nên cưới muộn.",
        "good": "Vũ Khúc hóa Lộc: vợ/chồng có tài chính. Có Lộc Tồn kèm: hôn nhân ổn định có của.",
        "bad": "Hóa Kỵ: khó kết hôn hoặc vợ/chồng tàn tật. Gặp Thất Sát (Mão/Dậu): hôn nhân xấu. Gặp 4 sát: ly hôn.",
        "spouse": "Phối ngẫu cứng rắn, độc lập, nói thẳng, ít thể hiện tình cảm, mạnh về tài chính.",
        "timing": "Nhất loạt khuyên cưới sau 30. Sớm quá là tan sớm.",
    },
    "Thiên Đồng": {
        "summary": "Phối ngẫu hiền lành, hưởng thụ. Nên chênh tuổi, cưới muộn tốt.",
        "good": "Có Lộc Tồn/hóa Lộc: vợ/chồng hiền có của, gia đình ấm cúng. Gặp Thái Âm: tình cảm ngọt ngào.",
        "bad": "Hóa Kỵ: tình cảm ban đầu tốt sau nhạt. Nhiều sát: lười biếng thành gánh nặng.",
        "spouse": "Phối ngẫu hiền lành, lạc quan, dễ chịu nhưng có thể hơi lười.",
        "timing": "Nam cưới vợ nhỏ, nữ cưới chồng lớn, chênh ≥8 tuổi là tốt nhất.",
    },
    "Liêm Trinh": {
        "summary": "Sao bất ổn nhất trong hôn nhân, nguy cơ ly biệt cao.",
        "good": "Liêm Trinh + Thiên Phủ (Tý/Ngọ): vợ/chồng hiền, tình cảm tạm ổn.",
        "bad": "Liêm Trinh + Tham Lang: khó sống chung. + Phá Quân: đổ vỡ. + Thất Sát: xa cách. Hóa Kỵ: tình cảm rắc rối.",
        "spouse": "Phối ngẫu hấp dẫn, khéo giao tiếp, cảm xúc mãnh liệt nhưng không ổn định.",
        "timing": "Nam nên cưới vợ trẻ (6-12 tuổi), nữ nên cưới chồng già.",
    },
    "Thiên Phủ": {
        "summary": "Sao hiền, hôn nhân ổn định nhưng có thể hơi nhạt.",
        "good": "Có Lộc Tồn/hóa Lộc: tiền tài + tình cảm ổn định. Không sát: vợ chồng hòa thuận.",
        "bad": "Tả/Hữu đơn tinh: dễ có hôn nhân thứ hai. Gặp sát tinh: tình cảm nhạt nhòa, dễ xa cách.",
        "spouse": "Phối ngẫu ôn hòa, thú vui đa dạng, giữ tiền tốt, hơi bảo thủ.",
        "timing": "Nam vợ lớn tuổi, nữ chồng nhỏ tuổi. Tình cảm ổn định nhưng cần vun đắp.",
    },
    "Thái Âm": {
        "summary": "Phối ngẫu thanh tú. Hãm + sát: tình cảm dễ thay đổi.",
        "good": "Miếu Vượng (Tý→Ngọ): vợ/chồng đẹp, thành đạt.",
        "bad": "Hãm (Mùi→Hợi): tình cảm dễ đổi thay. Hóa Kỵ (nam): mẹ vợ và vợ bất hòa. Gặp Hỏa/Linh: biến cố lớn.",
        "spouse": "Phối ngẫu dịu dàng, tinh tế, giàu cảm xúc, đôi khi hơi thất thường.",
        "timing": "Hãm nên cưới muộn.",
    },
    "Tham Lang": {
        "summary": "Đào hoa nhất, hôn nhân bất ổn, nguy cơ ngoại tình cao.",
        "good": "Hóa Lộc: vợ/chồng tài hoa, tình cảm nồng nhiệt. Có hóa Khoa: giảm ngoại tình.",
        "bad": "Hóa Kỵ: dễ có hôn nhân thứ hai. Gặp Tử Vi (Mão/Dậu): vợ/chồng hay đi ra ngoài. Gặp 4 sát: ly hôn.",
        "spouse": "Phối ngẫu tài hoa, giao tiếp rộng, khác phái tốt, ham muốn mạnh, khó kiềm chế.",
        "timing": "Sớm dễ thay đổi, nên cưới muộn. Trước cưới cần hiểu rõ đối phương.",
    },
    "Cự Môn": {
        "summary": "Khẩu thiệt thị phi, vợ chồng dễ cãi nhau. Cần Thái Dương hóa giải.",
        "good": "Có Thái Dương Miếu Vượng: hôn nhân tốt, cãi nhau hóa thành giao tiếp. Hóa Lộc: vợ/chồng có tài.",
        "bad": "Hóa Kỵ: vợ/chồng hay cằn nhằn, thị phi. Gặp Đà La: tự tìm phiền não.",
        "spouse": "Phối ngẫu ăn nói giỏi, hay ghen, sĩ diện cao, đôi khi khó tính nhưng tình cảm sâu.",
        "timing": "Cần chuẩn bị tâm lý giao tiếp và hòa giải lâu dài.",
    },
    "Thiên Tướng": {
        "summary": "Duyên 'từ từ', tình cảm bền. Vợ chồng hợp tác tốt.",
        "good": "Cả Tả Hữu: chung thủy, hôn nhân vững. Phối ngẫu chính trực.",
        "bad": "Chỉ một Tả/Hữu: dễ tái hôn. Nhiều sát: chịu đựng, ít nói.",
        "spouse": "Phối ngẫu chính trực, đáng tin, không thích xung đột, biết điều hòa.",
        "timing": "Thường quen biết từ trước (bạn học, đồng nghiệp). Hợp làm việc cùng nhau.",
    },
    "Thiên Lương": {
        "summary": "Phối ngẫu có trách nhiệm hoặc lớn tuổi. Trước cưới lận đận.",
        "good": "Có hóa Lộc: vợ/chồng có phúc. Tam phương tốt: tình cảm vững.",
        "bad": "Hóa Kỵ/nhiều sát: hay ca thán, tình cảm xa cách. Dễ thất bại tình đầu.",
        "spouse": "Phối ngẫu có trách nhiệm, chín chắn, thích dạy đời. Hơi già trước tuổi.",
        "timing": "Trước cưới khó khăn là chuyện thường — cưới xong lại tốt.",
    },
    "Thất Sát": {
        "summary": "Xa cách nhiều, nên cưới muộn sau 30.",
        "good": "Miếu Vượng (Dần/Thân): vợ/chồng cứng rắn nhưng chung thủy. Có hóa Lộc: giảm cô độc.",
        "bad": "Nhiều sát: ngoài mặt hòa thuận trong lòng bất mãn. Tại Mão/Dậu (Vũ Khúc + Thất Sát): hôn nhân xấu nhất.",
        "spouse": "Phối ngẫu cứng rắn, cô độc. Yêu nhanh, xa cũng nhanh.",
        "timing": "Cưới sau 30. Sớm quá dễ tan.",
    },
    "Phá Quân": {
        "summary": "Sao phá hoại nhất trong hôn nhân. Thích tự do, không thích ràng buộc.",
        "good": "Hóa Lộc: phá rồi lại lành — có thể đi đến cuối cùng sau nhiều sóng gió.",
        "bad": "Hóa Kỵ: đổ vỡ nặng. Gặp Liêm Trinh: 'thủy trung tác phần'. Gặp Tử Vi (Sửu/Mùi): cũng xấu.",
        "spouse": "Phối ngẫu thích tự do, thay đổi, quan niệm hôn nhân nhẹ nhàng.",
        "timing": "Dễ yêu sớm, yêu vội. Nên kéo dài thời gian tìm hiểu.",
    },
}

MARRIAGE_FOUR_TRANSFORMATIONS = {
    "Hóa Lộc": "Có duyên tiền định với vợ/chồng. Hôn nhân ngọt ngào, ngày càng tốt. Tiền bạc từ hôn nhân.",
    "Hóa Quyền": "Chủ động tìm kiếm hôn nhân. Vợ/chồng nắm quyền. Càng cưỡng cầu càng khó.",
    "Hóa Khoa": "Hòa hợp với vợ/chồng. Có quý nhân. Hôn nhân bền vững.",
    "Hóa Kỵ": "Trả nghiệp hôn nhân. Cưới sớm dễ ly. Khuyên cưới muộn hoặc không cưới.",
}

MARRIAGE_COMPATIBILITY = {
    "Tử Vi + Thiên Phủ": {
        "score": 5,
        "desc": "Hoàng đế gặp kho tàng. Bổ sung cho nhau, ổn định nhất.",
    },
    "Thiên Tướng + Sao khác": {
        "score": 4,
        "desc": "Thiên Tướng thích ứng tốt với hầu hết các sao.",
    },
    "Thiên Lương + Thiên Đồng": {
        "score": 4,
        "desc": "Chín chắn + hiền lành. Bổ sung hoàn hảo, sống đến già.",
    },
    "Thái Dương + Thái Âm": {
        "score": 4,
        "desc": "Mặt trời + mặt trăng. Âm dương hòa hợp. Cổ điển nhất.",
    },
    "Thất Sát + Cơ Nguyệt Đồng Lương": {
        "score": 3,
        "desc": "Động + tĩnh. Cần thời gian hòa hợp. Người mở đất + người giữ nhà.",
    },
    "Thất Sát + Thất Sát": {
        "score": 2,
        "desc": "Hai con hổ. Lửa nhiều, mâu thuẫn nhiều.",
    },
    "Phá Quân + Phá Quân": {
        "score": 2,
        "desc": "Hai người phá — hôn nhân khó bền.",
    },
    "Liêm Trinh + Thất Sát/Phá Quân": {
        "score": 1,
        "desc": "Ba sao xấu về hôn nhân. Nguy cơ ly biệt cao nhất.",
    },
    "Vũ Khúc + Thiên Đồng": {
        "score": 3,
        "desc": "Cứng + mềm bổ sung nhau.",
    },
}

MARRIAGE_METHODOLOGY = """
## PHƯƠNG PHÁP LUẬN HÔN NHÂN (Ni Hải Hạ + Tử Vi Toàn Thư)

### 1. Nguyên tắc song cung — quan trọng nhất
"Xem hôn nhân, chỉ nhìn Phu Thê là sai to. Phải đồng thời xem Phúc Đức."
- Phu Thê: tính cách vợ/chồng, tương tác vợ chồng
- Phúc Đức: tình cảm sâu xa, hôn nhân có bền không
- Nhiều người Phu Thê tốt nhưng Phúc Đức xấu → vẫn tan.
- Xem hợp hôn phải đồng thời phân tích: Mệnh + Phu Thê + Phúc Đức cả hai bên.

### 2. Tiêu chuẩn trời se duyên
- Cao nhất (thiên tác chi hợp): Mệnh A = Phu Thê B và Mệnh B = Phu Thê A
- Kế: một chiều Phu Thê = Mệnh đối phương
- Mệnh ngũ hành tương sinh (Mộc + Thổ, Thổ + Thủy, v.v.)
- Cả hai đồng thời đi đại vận tốt

### 3. Các mức độ phù hợp
- 5★: Phu Thê đối ứng lẫn nhau, Tứ Hóa bổ sung, đại hạn tốt, Phúc Đức tốt
- 4★: một chiều Phu Thê = Mệnh, Tứ Hóa lộc/khoa chủ đạo
- 3★: tạm ổn, cần vun đắp
- 2★: nhiều sát, nhiều hóa Kỵ, tình cảm sóng gió
- 1★: hung tinh tụ Phu Thê, Liêm Trinh tam hung tổ hợp, nguy cơ ly biệt

### 4. Ngũ bộ hợp hôn hoàn chỉnh
Bước 1 — Đánh giá Mệnh cách nền tảng: Mệnh + Thân + Phúc Đức
Bước 2 — Phu Thê hỗ tham: sao Phu Thê A ↔ Mệnh/tam phương B
Bước 3 — Thái Dương Thái Âm: nữ xem Dương (chồng), nam xem Âm (vợ)
Bước 4 — Tứ Hóa phi hóa hỗ tham: can năm A → sao hóa → cung B
Bước 5 — Đại hạn đồng bộ: đồng vượng = thời cơ tốt nhất

### 5. Luận nam nữ
- Nữ: Thái Dương = chồng. Miếu Vượng = tốt cho chồng. Hóa Kỵ = chồng tai họa.
- Nam: Thái Âm = vợ. Miếu Vượng = vợ đẹp giỏi. Hóa Kỵ = mẹ vợ + vợ bất hòa.

### 6. Thời điểm kết hôn (tam tằng pháp)
Tầng 1 — Bản mệnh: Phu Thê không sát = dễ cưới sớm; có sát = muộn
Tầng 2 — Đại hạn: Phu Thê đại hạn có cát tinh = thập niên đó có cơ hội
Tầng 3 — Lưu niên: Hồng Loan, Thiên Hỷ nhập Mệnh/Phu Thê = năm đó động

### 7. Cung vị kết hôn
- Phu Thê: tình cảm bình thường phát triển → cưới
- Mệnh: tự mình chủ động → cưới
- Tử Nữ: có thai trước → cưới
- Điền Trạch: vì nhà cửa → cưới
- Phụ Mẫu: cha mẹ giới thiệu → cưới

### 8. Dấu hiệu khắc chồng/vợ
- Liêm Trinh + Tham Lang/Phá Quân/Thất Sát tại Phu Thê
- Thái Dương Hóa Kỵ (nữ), Thái Âm Hóa Kỵ (nam)
- Phu Thê tứ sát tụ không cát tinh
- Cô Thần Quả Tú nhập Mệnh/Phu Thê
- Phúc Đức Phá Quân hãm + Liêm Trinh bình (thủy trung tác phần cách)

### 9. Loại hình duyên phận
- Hóa Lộc dẫn động: chánh duyên, chân ái
- Hóa Quyền dẫn động: chủ động tranh thủ
- Hóa Khoa dẫn động: hòa hợp, bạch đầu giai lão
- Hóa Kỵ dẫn động: nghịch duyên/oan gia
- Song phương hỗ Kỵ: oan gia lộ hẹp

### 10. Hợp tác sự nghiệp
- Quan lộc: tương dung
- Huynh đệ (tôi ích): quan hệ hợp tác
- Phúc Đức: đồng cam cộng khổ
"""

MARRIAGE_SCORE_CRITERIA = {
    "5★": "Phu Thê song phương đối ứng, Tứ Hóa bổ sung, đại hạn đồng vượng, Phúc Đức song cát",
    "4★": "Một chiều Phu Thê = Mệnh, Tứ Hóa lộc/khoa, tình cảm căn bản vững",
    "3★": "Mệnh cách tương phối nhưng có góc cạnh, cần vun đắp",
    "2★": "Phu Thê có sát, Hóa Kỵ xung, tình cảm sóng gió",
    "1★": "Hung tinh tụ Phu Thê, Liêm Trinh tam hung tổ hợp, nguy cơ ly biệt",
}

MARRIAGE_STARS = {
    "Hồng Loan": "Tình duyên chính, nhập Mệnh dễ kết hôn. Năm có Hồng Loan: cưới.",
    "Thiên Hỷ": "Hỷ sự, kết hợp Hồng Loan, chủ tin vui cưới hỏi.",
    "Đào Hoa": "Tình cảm, sắc đẹp. Ngoại tình nếu gặp Tham Lang.",
    "Thiên Riêu": "Tình duyên lãng mạn. Gặp Thái Âm có duyên với người giàu.",
    "Cô Thần": "Cô độc (nam). Nhập Mệnh: khó gần. Nhập Phu Thê: hôn nhân muộn.",
    "Quả Tú": "Cô quả (nữ). Nhập Mệnh/Phu Thê: duyên phận muộn.",
    "Thiên Hình": "Pháp luật, hình phạt. Nhập Phu Thê: dễ kiện tụng ly hôn.",
}
