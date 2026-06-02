const PALACE_INTERPRETATIONS = {
  "Menh": {
    title: "Cung Mệnh - Bản thân, tính cách, vận mệnh",
    general: "Cung Mệnh là cung quan trọng nhất, đại diện cho bản thân, tính cách cốt lõi, ngoại hình, khí chất và vận mệnh cả đời.",
    stars: {
      "Tử Vi": "Người có tố chất lãnh đạo, uy nghi, độc lập. Nếu Miếu Vượng: địa vị cao. Nếu Hãm: mất uy quyền.",
      "Thiên Cơ": "Thông minh, nhanh trí, giỏi mưu lược. Nếu Miếu Vượng: mưu lược thành công. Nếu Hãm: hay lo lắng.",
      "Thái Dương": "Nhiệt tình, hào phóng, quang minh chính đại. Nếu Miếu Vượng: danh tiếng tốt. Nếu Hãm: hao tài.",
      "Vũ Khúc": "Quyết đoán, thực tế, tài quản lý tài chính. Nếu Miếu Vượng: giàu có. Nếu Hãm: tiền hao hụt.",
      "Thiên Đồng": "Hiền lành, hòa nhã, có phúc. Nếu Miếu Vượng: phúc khí dồi dào. Nếu Hãm: mất phúc.",
      "Liêm Trinh": "Cá tính mạnh, tham vọng, tình cảm mãnh liệt. Nếu Miếu Vượng: thành công sáng tạo. Nếu Hãm: thị phi.",
      "Thiên Phủ": "Ổn định, bảo thủ, giàu có. Nếu Miếu Vượng: kho tàng dồi dào. Nếu Hãm: tiền khó giữ.",
      "Thái Âm": "Nhẹ nhàng, tế nhị, giàu cảm xúc. Nếu Miếu Vượng: tài năng phát triển. Nếu Hãm: u sầu.",
      "Tham Lang": "Đa tài, phóng khoáng, giao tiếp rộng. Nếu Miếu Vượng: tài hoa xuất chúng. Nếu Hãm: dục vọng thấp.",
      "Cự Môn": "Ăn nói lưu loát, tài hùng biện. Nếu Miếu Vượng: danh nhờ tài nói. Nếu Hãm: thị phi.",
      "Thiên Tướng": "Hòa thuận, có tổ chức, biết điều. Nếu Miếu Vượng: quản lý tốt.",
      "Thiên Lương": "Chính trực, nhân từ. Nếu Miếu Vượng: phúc đức dày. Nếu Hãm: bị lợi dụng.",
      "Thất Sát": "Dũng cảm, quyết đoán, thích mạo hiểm. Nếu Miếu Vượng: oai hùng. Nếu Hãm: dễ tai nạn.",
      "Phá Quân": "Phá cách, đổi mới, sáng tạo. Nếu Miếu Vượng: đột phá thành công. Nếu Hãm: phá sản.",
    }
  },
  "Huynh de": {
    title: "Cung Huynh Đệ - Anh chị em, bạn bè thân",
    general: "Cung Huynh Đệ thể hiện mối quan hệ với anh chị em ruột, bạn bè thân thiết.",
    stars: {
      "Tử Vi": "Anh chị em có địa vị, quyền uy.", "Thiên Cơ": "Anh chị em thông minh, mưu lược.",
      "Thái Dương": "Anh chị em nhiệt tình, quan hệ tốt.", "Vũ Khúc": "Anh chị em thực tế, lạnh nhạt.",
      "Thiên Đồng": "Anh chị em hòa thuận, giúp đỡ.", "Liêm Trinh": "Anh chị em cá tính mạnh, phức tạp.",
      "Thiên Phủ": "Anh chị em ổn định, giúp tài chính.", "Thái Âm": "Anh chị em nhẹ nhàng, tình cảm.",
      "Tham Lang": "Anh chị em đa tài, giao tiếp rộng.", "Cự Môn": "Anh chị em hay tranh luận, khẩu thiệt.",
      "Thiên Tướng": "Anh chị em hòa thuận.", "Thiên Lương": "Anh chị em chính trực, giúp đỡ.",
      "Thất Sát": "Anh chị em cá tính mạnh, xung đột.", "Phá Quân": "Anh chị em thay đổi, không ổn định.",
    }
  },
  "Phu the": {
    title: "Cung Phu Thê - Hôn nhân, người bạn đời",
    general: "Cung Phu Thê thể hiện hôn nhân, người bạn đời, quan hệ vợ chồng và tình duyên.",
    stars: {
      "Tử Vi": "Bạn đời có địa vị, hôn nhân ổn định.", "Thiên Cơ": "Bạn đời thông minh, hôn nhân thay đổi.",
      "Thái Dương": "Bạn đời nhiệt tình, nam tốt hơn nữ.", "Vũ Khúc": "Bạn đời thực tế, tình cảm lạnh nhạt.",
      "Thiên Đồng": "Bạn đời hiền lành, hôn nhân hòa thuận.", "Liêm Trinh": "Bạn đời đa tình, hôn nhân sóng gió.",
      "Thiên Phủ": "Bạn đời ổn định, hôn nhân bền vững.", "Thái Âm": "Bạn đời dịu dàng, hôn nhân tốt đẹp.",
      "Tham Lang": "Bạn đời tài hoa, dễ có người thứ ba.", "Cự Môn": "Bạn đời hay xét nét, khẩu thiệt.",
      "Thiên Tướng": "Bạn đời hòa thuận, hôn nhân ổn định.", "Thiên Lương": "Bạn đời chính trực, được chăm sóc.",
      "Thất Sát": "Bạn đời mạnh mẽ, dễ xa cách.", "Phá Quân": "Bạn đời thất thường, dễ đổ vỡ.",
    }
  },
  "Tu tuc": {
    title: "Cung Tử Tức - Con cái, hậu duệ",
    general: "Cung Tử Tức thể hiện con cái, việc sinh nở, quan hệ với con cái.",
    stars: {
      "Tử Vi": "Con cái thành đạt.", "Thiên Cơ": "Con cái thông minh, hiếu động.",
      "Thái Dương": "Con cái hoạt bát, quan hệ tốt.", "Vũ Khúc": "Con cái cứng đầu, cần kỷ luật.",
      "Thiên Đồng": "Con cái hiền lành, nuôi nhàn.", "Liêm Trinh": "Con cái cá tính mạnh, dễ nổi loạn.",
      "Thiên Phủ": "Con cái ổn định, tương lai sáng.", "Thái Âm": "Con cái dịu dàng.",
      "Tham Lang": "Con cái đa tài, nghịch ngợm.", "Cự Môn": "Con cái hay cãi, cần kiên nhẫn.",
      "Thiên Tướng": "Con cái ngoan ngoãn.", "Thiên Lương": "Con cái chính trực, hiếu thảo.",
      "Thất Sát": "Con cái cá tính mạnh.", "Phá Quân": "Con cái thay đổi, khó bảo.",
    }
  },
  "Tai bach": {
    title: "Cung Tài Bạch - Tài chính, tiền bạc",
    general: "Cung Tài Bạch thể hiện khả năng kiếm tiền, quản lý tài chính.",
    stars: {
      "Tử Vi": "Tiền dồi dào, chi tiêu lớn.", "Thiên Cơ": "Tiền từ trí tuệ, không ổn định.",
      "Thái Dương": "Tiền từ danh tiếng, ra nhiều.", "Vũ Khúc": "Chính tài vượng, quản lý tốt.",
      "Thiên Đồng": "Tiền ổn định, không giàu nghèo.", "Liêm Trinh": "Tiền từ nhiều nguồn.",
      "Thiên Phủ": "Kho tàng dồi dào, biết tích lũy.", "Thái Âm": "Tiền chậm nhưng chắc.",
      "Tham Lang": "Tiền từ kinh doanh, nghệ thuật.", "Cự Môn": "Tiền từ tư vấn, luật pháp.",
      "Thiên Tướng": "Tiền từ công việc phụ trợ.", "Thiên Lương": "Tiền từ từ thiện, giáo dục.",
      "Thất Sát": "Tiền nhanh đi nhanh.", "Phá Quân": "Tiền thất thường, hao hụt.",
    }
  },
  "Tat ach": {
    title: "Cung Tật Ách - Sức khỏe, bệnh tật",
    general: "Cung Tật Ách thể hiện tình trạng sức khỏe, bệnh tật dễ mắc.",
    stars: {
      "Tử Vi": "Sức khỏe tốt, chú ý tiêu hóa.", "Thiên Cơ": "Thần kinh nhạy, dễ stress.",
      "Thái Dương": "Chú ý tim mạch, mắt.", "Vũ Khúc": "Chú ý hô hấp, xương khớp.",
      "Thiên Đồng": "Sức khỏe tốt.", "Liêm Trinh": "Chú ý thần kinh, máu huyết.",
      "Thiên Phủ": "Sức khỏe tốt, bệnh giàu sang.", "Thái Âm": "Phụ nữ chú ý phụ khoa.",
      "Tham Lang": "Chú ý gan, thận.", "Cự Môn": "Chú ý họng, tiêu hóa.",
      "Thiên Tướng": "Sức khỏe ổn định.", "Thiên Lương": "Sức khỏe tốt về già.",
      "Thất Sát": "Dễ tai nạn, phẫu thuật.", "Phá Quân": "Dễ tai nạn, chảy máu.",
    }
  },
  "Thien di": {
    title: "Cung Thiên Di - Xuất ngoại, quý nhân, xã hội",
    general: "Cung Thiên Di thể hiện vận mệnh khi ra ngoài, quan hệ xã hội, quý nhân.",
    stars: {
      "Tử Vi": "Ra ngoài được kính trọng.", "Thiên Cơ": "Gặp nhiều cơ hội thay đổi.",
      "Thái Dương": "Quý nhân giúp đỡ.", "Vũ Khúc": "Kiếm tiền xa nhà.",
      "Thiên Đồng": "Gặp nhiều người tốt.", "Liêm Trinh": "Giao thiệp rộng, cẩn thận thị phi.",
      "Thiên Phủ": "Được ủng hộ.", "Thái Âm": "Có quý nhân phù trợ.",
      "Tham Lang": "Giao thiệp rộng.", "Cự Môn": "Dễ gây thị phi.",
      "Thiên Tướng": "Được giúp đỡ.", "Thiên Lương": "Gặp quý nhân.",
      "Thất Sát": "Dễ xung đột.", "Phá Quân": "Nhiều biến động.",
    }
  },
  "No boc": {
    title: "Cung Nô Bộc - Bạn bè, đồng nghiệp, cấp dưới",
    general: "Cung Nô Bộc thể hiện chất lượng bạn bè, đồng nghiệp, cấp dưới.",
    stars: {
      "Tử Vi": "Bạn bè có địa vị.", "Thiên Cơ": "Bạn bè thông minh, khó giữ lâu.",
      "Thái Dương": "Bạn bè nhiệt tình.", "Vũ Khúc": "Bạn bè thực tế, chọn lọc.",
      "Thiên Đồng": "Bạn bè hòa nhã.", "Liêm Trinh": "Bạn bè đa dạng, cẩn thận.",
      "Thiên Phủ": "Bạn bè ổn định, đáng tin.", "Thái Âm": "Bạn bè tế nhị.",
      "Tham Lang": "Bạn bè đa tài.", "Cự Môn": "Bạn bè hay gây thị phi.",
      "Thiên Tướng": "Bạn bè hòa thuận.", "Thiên Lương": "Bạn bè chính trực.",
      "Thất Sát": "Khó kết bạn thân.", "Phá Quân": "Quan hệ không lâu dài.",
    }
  },
  "Quan loc": {
    title: "Cung Quan Lộc - Sự nghiệp, công danh",
    general: "Cung Quan Lộc thể hiện con đường sự nghiệp, công danh, địa vị xã hội.",
    stars: {
      "Tử Vi": "Hợp lãnh đạo, quản lý cấp cao.", "Thiên Cơ": "Hợp nghiên cứu, khoa học.",
      "Thái Dương": "Hợp công chức, giáo dục.", "Vũ Khúc": "Hợp ngân hàng, tài chính.",
      "Thiên Đồng": "Hợp dịch vụ, phúc lợi.", "Liêm Trinh": "Hợp luật pháp, ngoại giao.",
      "Thiên Phủ": "Hợp quản lý, tài chính.", "Thái Âm": "Hợp bất động sản, nghệ thuật.",
      "Tham Lang": "Hợp kinh doanh, giải trí.", "Cự Môn": "Hợp luật sư, tư vấn.",
      "Thiên Tướng": "Hợp công chức, thư ký.", "Thiên Lương": "Hợp giáo dục, y tế.",
      "Thất Sát": "Hợp quân đội, mạo hiểm.", "Phá Quân": "Hợp sáng tạo, xuất nhập khẩu.",
    }
  },
  "Dien trach": {
    title: "Cung Điền Trạch - Nhà cửa, bất động sản",
    general: "Cung Điền Trạch thể hiện vận mệnh về nhà ở, đất đai, bất động sản.",
    stars: {
      "Tử Vi": "Nhà cửa sang trọng.", "Thiên Cơ": "Nhà thay đổi nhiều.",
      "Thái Dương": "Nhà cửa sáng sủa.", "Vũ Khúc": "Nhà cửa chắc chắn.",
      "Thiên Đồng": "Nhà cửa thoải mái.", "Liêm Trinh": "Nhà dễ tranh chấp.",
      "Thiên Phủ": "Nhiều nhà, giàu có.", "Thái Âm": "Nhà yên tĩnh.",
      "Tham Lang": "Nhà cửa đẹp.", "Cự Môn": "Nhà hay thị phi.",
      "Thiên Tướng": "Nhà ổn định.", "Thiên Lương": "Nhà yên bình.",
    }
  },
  "Phuc duc": {
    title: "Cung Phúc Đức - Phúc khí, tinh thần, tổ tiên",
    general: "Cung Phúc Đức thể hiện phúc khí tổ tiên, đời sống tinh thần.",
    stars: {
      "Tử Vi": "Phúc đức dày.", "Thiên Cơ": "Phúc đức thay đổi.",
      "Thái Dương": "Phúc đức sáng sủa.", "Vũ Khúc": "Phúc đức thực tế.",
      "Thiên Đồng": "Phúc đức dồi dào.", "Liêm Trinh": "Phúc đức phức tạp.",
      "Thiên Phủ": "Phúc đức ổn định.", "Thái Âm": "Phúc đức nội tâm.",
      "Tham Lang": "Phúc đức hưởng thụ.", "Cự Môn": "Phúc đức có khẩu nghiệp.",
      "Thiên Tướng": "Phúc đức bình an.", "Thiên Lương": "Phúc đức dày nhất.",
    }
  },
  "Phu mau": {
    title: "Cung Phụ Mẫu - Cha mẹ, gia đình, nguồn gốc",
    general: "Cung Phụ Mẫu thể hiện mối quan hệ với cha mẹ, gia đình.",
    stars: {
      "Tử Vi": "Cha mẹ có địa vị.", "Thiên Cơ": "Cha mẹ thông minh.",
      "Thái Dương": "Cha mẹ nhiệt tình.", "Vũ Khúc": "Cha mẹ nghiêm khắc.",
      "Thiên Đồng": "Cha mẹ hiền lành.", "Liêm Trinh": "Cha mẹ cá tính mạnh.",
      "Thiên Phủ": "Cha mẹ ổn định.", "Thái Âm": "Mẹ hiền dịu.",
      "Tham Lang": "Cha mẹ phóng khoáng.", "Cự Môn": "Cha mẹ hay răn dạy.",
      "Thiên Tướng": "Cha mẹ hòa thuận.", "Thiên Lương": "Cha mẹ nhân hậu.",
    }
  },
};

const CUNG_KEY_MAP = {"Mệnh":"Menh","Huynh đệ":"Huynh de","Phu thê":"Phu the","Tử tức":"Tu tuc","Tài bạch":"Tai bach","Tật ách":"Tat ach","Thiên di":"Thien di","Nô bộc":"No boc","Quan lộc":"Quan loc","Điền trạch":"Dien trach","Phúc đức":"Phuc duc","Phụ mẫu":"Phu mau"};

function normalizeStarName(name) {
  const map = {"tử vi":"tu vi","thiên cơ":"thien co","thái dương":"thai duong","vũ khúc":"vu khuc","thiên đồng":"thien dong","liêm trinh":"liem trinh","thiên phủ":"thien phu","thái âm":"thai am","tham lang":"tham lang","cự môn":"cu mon","thiên tướng":"thien tuong","thiên lương":"thien luong","thất sát":"that sat","phá quân":"pha quan"};
  const clean = name.replace(/\s/g,"").toLowerCase();
  for (const [vn, ascii] of Object.entries(map)) {
    const vc = vn.replace(/\s/g,"");
    if (vc === clean || vc.includes(clean) || clean.includes(vc)) return ascii.replace(/\s/g,"");
  }
  return clean;
}

function giaiDoanCung(tenCung, chinhTinh, phuTinh, satTinh, dacTinh) {
  const key = CUNG_KEY_MAP[tenCung] || tenCung;
  const data = PALACE_INTERPRETATIONS[key];
  if (!data) return {ten: tenCung, mo_ta: "Chưa có dữ liệu"};

  const result = {ten: tenCung, tieu_de: data.title, tong_quan: data.general, sao_phan_tich: []};
  for (const sao of chinhTinh) {
    const saoGoc = sao.split("(")[0];
    const ns = normalizeStarName(saoGoc);
    for (const [origKey, origVal] of Object.entries(data.stars)) {
      if (normalizeStarName(origKey) === ns) {
        const entry = {sao, giai_doan: origVal};
        if (dacTinh && dacTinh[sao]) entry.dac_tinh = dacTinh[sao];
        result.sao_phan_tich.push(entry);
        break;
      }
    }
  }
  result.phu_tinh = phuTinh;
  result.sat_tinh = satTinh;
  return result;
}

function giaiDoanToanBo(data) {
  return (data.thap_nhi_cung || []).map(c =>
    giaiDoanCung(c.ten, c.chinh_tinh, c.phu_tinh, c.sat_tinh, c.dac_tinh)
  );
}

const DIMENSION_MAP = {
  "Sự nghiệp": ["Mệnh","Quan lộc","Thiên di"],
  "Tài chính": ["Tài bạch","Phúc đức","Điền trạch","Mệnh"],
  "Tình cảm": ["Phu thê","Tử tức","Huynh đệ","Mệnh"],
  "Sức khỏe": ["Tật ách","Phụ mẫu","Mệnh"],
};

const STAR_BASE_SCORE = {
  "Tử Vi":18,"Thiên Cơ":10,"Thái Dương":12,"Vũ Khúc":11,"Thiên Đồng":9,"Liêm Trinh":8,
  "Thiên Phủ":16,"Thái Âm":11,"Tham Lang":10,"Cự Môn":6,"Thiên Tướng":12,"Thiên Lương":11,
  "Thất Sát":7,"Phá Quân":6,"Tả Phụ":10,"Hữu Bật":10,"Văn Xương":9,"Văn Khúc":9,
  "Thiên Khôi":11,"Thiên Việt":11,"Lộc Tồn":8,"Thiên Mã":4,
  "Kình Dương":-12,"Đà La":-10,"Hỏa Tinh":-8,"Linh Tinh":-8,"Địa Không":-9,"Địa Kiếp":-9,
  "Thiên Hình":-4,"Thái Tuế":-3,"Cô Thần":-4,"Quả Tú":-4,
};

const BRIGHTNESS_COEF = {"Miếu":1.5,"Vượng":1.3,"Đắc":1.1,"Bình":1.0,"Hãm":0.5};
const SIHUA_MODIFIER = {"Hóa Lộc":15,"Hóa Quyền":12,"Hóa Khoa":10,"Hóa Kỵ":-18};
const CUNG_MULTIPLIER = {"Mệnh":1.5,"Huynh đệ":0.8,"Phu thê":1.2,"Tử tức":1.0,"Tài bạch":1.3,"Tật ách":1.2,"Thiên di":1.0,"Nô bộc":0.6,"Quan lộc":1.4,"Điền trạch":0.9,"Phúc đức":0.8,"Phụ mẫu":0.7};

function xepLoai(score) {
  if (score >= 85) return "Tốt";
  if (score >= 70) return "Khá";
  if (score >= 50) return "Trung bình";
  if (score >= 30) return "Kém";
  return "Xấu";
}

function tinhDiemCung(cungData, tuHoaMap) {
  let score = 50;
  const allStars = [...(cungData.chinh_tinh||[]), ...(cungData.phu_tinh||[]), ...(cungData.sat_tinh||[])];
  const dt = cungData.dac_tinh || {};
  for (const star of allStars) {
    const base = STAR_BASE_SCORE[star] || 0;
    const coeff = BRIGHTNESS_COEF[dt[star]] || 1.0;
    score += base * coeff;
    if (tuHoaMap[star]) score += SIHUA_MODIFIER[tuHoaMap[star]] || 0;
  }
  const multiplier = CUNG_MULTIPLIER[cungData.ten] || 1.0;
  score = Math.round(Math.max(0, Math.min(100, score * multiplier)));
  return {diem: score, xep_loai: xepLoai(score)};
}

function tinhDiemToanBo(thapNhiCung, tuHoa) {
  const tuHoaMap = {};
  for (const [k, v] of Object.entries(tuHoa)) if (v) tuHoaMap[v] = k;

  const diemCung = {};
  let tong = 0, count = 0;
  for (const c of thapNhiCung) {
    const r = tinhDiemCung(c, tuHoaMap);
    diemCung[c.ten] = {diem: r.diem, xep_loai: r.xep_loai};
    tong += r.diem; count++;
  }
  const diemTB = count ? Math.round(tong / count) : 50;
  const dimensions = {};
  for (const [name, cungList] of Object.entries(DIMENSION_MAP)) {
    const scores = cungList.filter(c => diemCung[c]).map(c => diemCung[c].diem);
    const avg = scores.length ? Math.round(scores.reduce((a,b)=>a+b,0)/scores.length) : 50;
    dimensions[name] = {diem: avg, xep_loai: xepLoai(avg)};
  }
  return {
    diem_trung_binh: diemTB,
    xep_loai_tong_quan: xepLoai(diemTB),
    tung_cung: diemCung,
    cac_khia_canh: dimensions,
  };
}

const PATTERNS_DATA = [
  {ten:"Tử Phủ Tương Hội", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi") && s.includes("Thiên Phủ"); }, y_nghia:"Người có uy quyền, địa vị, phú quý song toàn.", source:"紫微斗数全书·紫府同宫格"},
  {ten:"Tử Vi Độc Tọa", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi") && s.length===1; }, y_nghia:"Cá tính mạnh, độc lập, uy quyền nhưng dễ cô độc."},
  {ten:"Mệnh Vô Chính Diệu", check: (data) => data.thap_nhi_cung[0].chinh_tinh.length===0, y_nghia:"Cuộc đời phải dựa dẫm vào người khác, hay thay đổi.", source:"紫微斗数全书"},
  {ten:"Thất Sát Triều Đẩu", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi")&&s.includes("Thất Sát")&&[2,8].includes(m.so_thu_tu); }, y_nghia:"Quyền uy tột đỉnh, có khả năng chỉ huy.", source:"紫微斗数全书"},
  {ten:"Tử Vi Thất Sát", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi")&&s.includes("Thất Sát"); }, y_nghia:"Uy quyền và dũng mãnh, lãnh đạo, chỉ huy."},
  {ten:"Tử Vi Cư Ngọ", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return m.so_thu_tu===6&&s.includes("Tử Vi"); }, y_nghia:"Đế tinh lâm ngôi chính vị, địa vị cao sang.", source:"紫微斗数全书"},
  {ten:"Cơ Nguyệt Đồng Lương", check: (data) => { const all=new Set; data.thap_nhi_cung.forEach(c=>c.chinh_tinh.forEach(s=>all.add(s.split("(")[0]))); return ["Thiên Cơ","Thái Âm","Thiên Đồng","Thiên Lương"].filter(s=>all.has(s)).length>=3; }, y_nghia:"Tài năng, thông minh, hợp nghiên cứu, giáo dục.", source:"紫微斗数全书·机月同梁格"},
  {ten:"Sát Phá Tham", check: (data) => { const all=new Set; data.thap_nhi_cung.forEach(c=>c.chinh_tinh.forEach(s=>all.add(s.split("(")[0]))); return ["Thất Sát","Phá Quân","Tham Lang"].filter(s=>all.has(s)).length>=2; }, y_nghia:"Cuộc đời nhiều biến động, thăng trầm.", source:"紫微斗数全书·杀破狼"},
  {ten:"Nhật Nguyệt Tịnh Minh", check: (data) => { let dOK=false,aOK=false; data.thap_nhi_cung.forEach(c=>{c.chinh_tinh.forEach(s=>{const b=s.split("(")[0],dt=c.dac_tinh||{};if(b==="Thái Dương"&&["Miếu","Vượng"].includes(dt[s]))dOK=true;if(b==="Thái Âm"&&["Miếu","Vượng"].includes(dt[s]))aOK=true})}); return dOK&&aOK; }, y_nghia:"Tài năng xuất chúng, học rộng, cuộc đời sáng lạn."},
  {ten:"Cự Cơ Đồng Cung", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Cự Môn")&&s.includes("Thiên Cơ"); }, y_nghia:"Tài hùng biện, thông minh, dễ thị phi.", source:"紫微斗数全书"},
  {ten:"Thiên Phủ Thủ Mệnh", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Thiên Phủ"); }, y_nghia:"Ổn định, giàu có, biết tích lũy.", source:"紫微斗数全书"},
  {ten:"Thái Âm Cư Dậu", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return m.so_thu_tu===9&&s.includes("Thái Âm"); }, y_nghia:"Tài năng nghệ thuật, tài chính tốt."},
  {ten:"Thái Dương Cư Ngọ", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return m.so_thu_tu===6&&s.includes("Thái Dương"); }, y_nghia:"Địa vị cao, công danh hiển hách."},
  {ten:"Tham Lang Cư Tỵ Hợi", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return [5,11].includes(m.so_thu_tu)&&s.includes("Tham Lang"); }, y_nghia:"Giàu có, làm ăn phát đạt, tài ngoại giao."},
  {ten:"Tả Hữu Giáp Mệnh", check: (data) => { const m=data.thap_nhi_cung[0],p=m.so_thu_tu; return gC(data,(p-1+12)%12).phu_tinh.includes("Tả Phụ")&&gC(data,(p+1)%12).phu_tinh.includes("Hữu Bật"); }, y_nghia:"Được quý nhân phù trợ.", source:"紫微斗数全书·辅弼夹命"},
  {ten:"Khôi Việt Giáp Mệnh", check: (data) => { const m=data.thap_nhi_cung[0],p=m.so_thu_tu; return gC(data,(p-1+12)%12).phu_tinh.includes("Thiên Khôi")&&gC(data,(p+1)%12).phu_tinh.includes("Thiên Việt"); }, y_nghia:"Khoa bảng, thi cử đỗ đạt cao.", source:"紫微斗数全书·魁钺夹命"},
  {ten:"Xương Khúc Giáp Mệnh", check: (data) => { const m=data.thap_nhi_cung[0],p=m.so_thu_tu; return gC(data,(p-1+12)%12).phu_tinh.includes("Văn Xương")&&gC(data,(p+1)%12).phu_tinh.includes("Văn Khúc"); }, y_nghia:"Học vấn uyên thâm, tài văn chương.", source:"紫微斗数全书·昌曲夹命"},
  {ten:"Hỏa Linh Giáp Mệnh", check: (data) => { const m=data.thap_nhi_cung[0],p=m.so_thu_tu; return gC(data,(p-1+12)%12).sat_tinh.includes("Hỏa Tinh")&&gC(data,(p+1)%12).sat_tinh.includes("Linh Tinh"); }, y_nghia:"Nóng nảy, nhiều thị phi, cẩn thận cháy nổ.", source:"紫微斗数全书·火铃夹命"},
  {ten:"Tam Hóa Gia Hội", check: (data) => { const m=data.thap_nhi_cung[0]; return ["Hóa Lộc","Hóa Quyền","Hóa Khoa"].filter(t=>hasHoa(m,t)).length>=3; }, y_nghia:"Phú quý song toàn hiếm có.", source:"紫微斗数全书·三奇加会"},
  {ten:"Lộc Mã Giao Trì", check: (data) => { for(let i=0;i<12;i++){const c=gC(data,i);if(c.phu_tinh.includes("Lộc Tồn")&&c.phu_tinh.includes("Thiên Mã"))return true}return false; }, y_nghia:"Phát tài nhờ đi xa, buôn bán phương xa."},
  {ten:"Phúc Thọ Song Toàn", check: (data) => { const m=data.thap_nhi_cung[0],f=data.thap_nhi_cung[10],ms=m.chinh_tinh.map(s=>s.split("(")[0]),fs=f.chinh_tinh.map(s=>s.split("(")[0]); return (ms.includes("Thiên Lương")||fs.includes("Thiên Lương"))&&(ms.includes("Thiên Đồng")||fs.includes("Thiên Đồng")); }, y_nghia:"Sống thọ, có phúc, cuộc đời ít sóng gió."},
  {ten:"Hỏa Tham Cách", check: (data) => { for(let i=0;i<12;i++){const c=gC(data,i);if(c.sat_tinh.includes("Hỏa Tinh")&&c.chinh_tinh.map(s=>s.split("(")[0]).includes("Tham Lang"))return true}return false; }, y_nghia:"Phát tài bất ngờ, giàu nhanh nhờ liều lĩnh.", source:"紫微斗数骨髓赋"},
  {ten:"Linh Tham Cách", check: (data) => { for(let i=0;i<12;i++){const c=gC(data,i);if(c.sat_tinh.includes("Linh Tinh")&&c.chinh_tinh.map(s=>s.split("(")[0]).includes("Tham Lang"))return true}return false; }, y_nghia:"Phát đạt bất ngờ, tài kiếm tiền phi thường.", source:"紫微斗数骨髓赋"},
  {ten:"Tử Phủ Triều Viên", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]),dc=gC(data,(m.so_thu_tu+6)%12).chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi")&&dc.includes("Thiên Phủ"); }, y_nghia:"Phú quý, địa vị cao, sự nghiệp viên mãn."},
  {ten:"Phủ Tướng Triều Viên", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Thiên Phủ")&&s.includes("Thiên Tướng"); }, y_nghia:"Khả năng quản lý, tổ chức, sự nghiệp ổn định.", source:"紫微斗数全书·府相朝垣格"},
  {ten:"Song Lộc Triều Viên", check: (data) => { const m=data.thap_nhi_cung[0]; return m.phu_tinh.includes("Lộc Tồn")&&hasHoa(m,"Hóa Lộc"); }, y_nghia:"Đại phú, giàu có bậc nhất."},
  {ten:"Nhật Nguyệt Đồng Cung", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return [1,7].includes(m.so_thu_tu)&&s.includes("Thái Dương")&&s.includes("Thái Âm"); }, y_nghia:"Âm dương hòa hợp, tình duyên tốt, sự nghiệp thuận lợi.", source:"紫微斗数全书·日月同宫"},
  {ten:"Quân Thần Khánh Hội", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Tử Vi")&&(m.phu_tinh.includes("Tả Phụ")||m.phu_tinh.includes("Hữu Bật"))&&(m.phu_tinh.includes("Văn Xương")||m.phu_tinh.includes("Văn Khúc")); }, y_nghia:"Quý nhân phò trợ, quyền lực vững chắc.", source:"紫微斗数全书·君臣庆会格"},
  {ten:"Dương Đà Giáp Kỵ", check: (data) => { for(let p=0;p<12;p++){if(gC(data,(p-1+12)%12).sat_tinh.includes("Kình Dương")&&gC(data,(p+1)%12).sat_tinh.includes("Đà La")&&hasHoa(gC(data,p),"Hóa Kỵ"))return true}return false; }, y_nghia:"Đại hung. Cẩn thận huyết quang, phẫu thuật, kiện tụng.", source:"紫微斗数骨髓赋·羊陀夹忌"},
  {ten:"Không Kiếp Giáp Mệnh", check: (data) => { const p=data.thap_nhi_cung[0].so_thu_tu; return gC(data,(p-1+12)%12).sat_tinh.includes("Địa Không")&&gC(data,(p+1)%12).sat_tinh.includes("Địa Kiếp"); }, y_nghia:"Hợp nghề hư (tâm linh, nghệ thuật). Không hợp kinh doanh.", source:"紫微斗数全书·空劫夹命"},
  {ten:"Cự Nhật Đồng Cung", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]); return [2,8].includes(m.so_thu_tu)&&s.includes("Cự Môn")&&s.includes("Thái Dương"); }, y_nghia:"Tài hùng biện, truyền thông, chuyên môn lập nghiệp.", source:"紫微斗数全书·巨日同宫"},
  {ten:"Vũ Tham Cách", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]),dc=gC(data,(m.so_thu_tu+6)%12).chinh_tinh.map(s=>s.split("(")[0]); return (s.includes("Vũ Khúc")&&s.includes("Tham Lang"))||(dc.includes("Vũ Khúc")&&dc.includes("Tham Lang")); }, y_nghia:"Trước 30 tuổi trầm lắng, sau 30 mới phát. Đại phú đại quý.", source:"紫微斗数骨髓赋·武贪格"},
  {ten:"Cơ Lương Thủ Mệnh", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Thiên Cơ")&&s.includes("Thiên Lương"); }, y_nghia:"Thông minh, có phúc đức, hợp y dược, giáo dục."},
  {ten:"Liêm Trinh Thiên Tướng", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Liêm Trinh")&&s.includes("Thiên Tướng"); }, y_nghia:"Thanh liêm, chính trực, hợp luật pháp."},
  {ten:"Thiên Đồng Thiên Lương", check: (data) => { const m=data.thap_nhi_cung[0],s=m.chinh_tinh.map(s=>s.split("(")[0]),dc=gC(data,(m.so_thu_tu+6)%12).chinh_tinh.map(s=>s.split("(")[0]); return (s.includes("Thiên Đồng")&&s.includes("Thiên Lương"))||(s.includes("Thiên Đồng")&&dc.includes("Thiên Lương")); }, y_nghia:"Phúc thọ song toàn, cuộc đời bình an."},
  {ten:"Hóa Lộc Nhập Mệnh", check: (data) => hasHoa(data.thap_nhi_cung[0],"Hóa Lộc"), y_nghia:"Sinh tài thuận lợi, nhân duyên tốt, cơ duyên nhiều.", source:"紫微斗数全书·四化论"},
  {ten:"Hóa Kỵ Nhập Mệnh", check: (data) => hasHoa(data.thap_nhi_cung[0],"Hóa Kỵ"), y_nghia:"Cố chấp, tâm lý chướng ngại, hoặc tiềm ẩn vấn đề sức khỏe.", source:"紫微斗数全书·四化论"},
  {ten:"Vũ Khúc Thất Sát", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Vũ Khúc")&&s.includes("Thất Sát"); }, y_nghia:"Quả quyết cương nghị, năng lực tài chính mạnh."},
  {ten:"Vũ Khúc Phá Quân", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Vũ Khúc")&&s.includes("Phá Quân"); }, y_nghia:"Cả đời biến động về tài chính, dám liều dám làm."},
  {ten:"Cự Cơ Thủ Mệnh", check: (data) => { const s=data.thap_nhi_cung[0].chinh_tinh.map(s=>s.split("(")[0]); return s.includes("Cự Môn")&&s.includes("Thiên Cơ"); }, y_nghia:"Tài hùng biện, thông minh cơ biến."},
  {ten:"Tử Vi Thủ Mệnh", check: (data) => data.thap_nhi_cung[0].chinh_tinh.some(s=>s.split("(")[0]==="Tử Vi"), y_nghia:"Đế tinh nhập mệnh, chủ uy quyền, lãnh đạo.", source:"紫微斗数全书·紫微入命"},
  {ten:"Hóa Lộc Nhập Tài", check: (data) => hasHoa(data.thap_nhi_cung[4],"Hóa Lộc"), y_nghia:"Tài lộc dồi dào, kiếm tiền thuận lợi.", source:"紫微斗数全书·四化论"},
  {ten:"Hóa Quyền Nhập Quan", check: (data) => hasHoa(data.thap_nhi_cung[8],"Hóa Quyền"), y_nghia:"Quyền lực, thăng tiến trong sự nghiệp.", source:"紫微斗数全书·四化论"},
  {ten:"Hóa Khoa Nhập Mệnh", check: (data) => hasHoa(data.thap_nhi_cung[0],"Hóa Khoa"), y_nghia:"Văn tài, học thức, danh tiếng.", source:"紫微斗数全书·四化论"},
  {ten:"Lộc Tồn Thủ Mệnh", check: (data) => data.thap_nhi_cung[0].phu_tinh.includes("Lộc Tồn"), y_nghia:"Cả đời y thực vô ưu, tài lộc ổn định.", source:"紫微斗数全书·禄存星"},
  {ten:"Thiên Mã Tại Di", check: (data) => { const p=data.thap_nhi_cung[0].so_thu_tu; return gC(data,(p+6)%12).phu_tinh.includes("Thiên Mã"); }, y_nghia:"Xa quê lập nghiệp, phát triển ở ngoại quốc."},
  {ten:"Đào Hoa Phạm Chủ", check: (data) => { const m=data.thap_nhi_cung[0]; let c=0;if(m.phu_tinh.includes("Đào Hoa"))c++;if(m.phu_tinh.includes("Hồng Loan"))c++;if(m.phu_tinh.includes("Thiên Hỷ"))c++;return c>=2&&m.chinh_tinh.some(s=>s.split("(")[0]==="Tham Lang"); }, y_nghia:"Đào hoa quá vượng, dễ vướng tình ái thị phi."},
  {ten:"Hóa Kỵ Nhập Tài", check: (data) => hasHoa(data.thap_nhi_cung[4],"Hóa Kỵ"), y_nghia:"Tài chính có vấn đề, cẩn thận chi tiêu."},
];

function gC(data, pos) { return data.thap_nhi_cung.find(c=>c.so_thu_tu===pos) || {phu_tinh:[],sat_tinh:[],chinh_tinh:[]}; }
function hasHoa(cung, hoaType) { return (cung.tu_hoa||[]).some(s => s.includes(`(${hoaType})`)); }

function nhanDienCachCuc(data) {
  const result = [];
  for (const p of PATTERNS_DATA) {
    try { if (p.check(data)) result.push({cach_cuc: p.ten, y_nghia: p.y_nghia, source: p.source || ""}); } catch(e) {}
  }
  return result;
}
