const TUVIConfig = {
  THIEN_CAN: ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"],
  DIA_CHI: ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"],
  DIA_CHI_INDEX: {Tý:0,Sửu:1,Dần:2,Mão:3,Thìn:4,Tỵ:5,Ngọ:6,Mùi:7,Thân:8,Dậu:9,Tuất:10,Hợi:11},
  TEN_12_CUNG: ["Mệnh","Huynh đệ","Phu thê","Tử tức","Tài bạch","Tật ách","Thiên di","Nô bộc","Quan lộc","Điền trạch","Phúc đức","Phụ mẫu"],
  NGU_HANH: {2:"Thủy nhị cục",3:"Mộc tam cục",4:"Kim tứ cục",5:"Thổ ngũ cục",6:"Hỏa lục cục"},
  NGU_HANH_NAME: {2:"Thủy",3:"Mộc",4:"Kim",5:"Thổ",6:"Hỏa"},
  THOI_GIAN: {23:0,0:0,1:1,2:1,3:2,4:2,5:3,6:3,7:4,8:4,9:5,10:5,11:6,12:6,13:7,14:7,15:8,16:8,17:9,18:9,19:10,20:10,21:11,22:11},
  TU_HOA: {
    Giáp:{Lộc:"Liêm Trinh",Quyền:"Phá Quân",Khoa:"Vũ Khúc",Kỵ:"Thái Dương"},
    Ất:{Lộc:"Thiên Cơ",Quyền:"Thiên Lương",Khoa:"Tử Vi",Kỵ:"Thái Âm"},
    Bính:{Lộc:"Thiên Đồng",Quyền:"Thiên Cơ",Khoa:"Văn Xương",Kỵ:"Liêm Trinh"},
    Đinh:{Lộc:"Thái Âm",Quyền:"Thiên Đồng",Khoa:"Thiên Cơ",Kỵ:"Cự Môn"},
    Mậu:{Lộc:"Tham Lang",Quyền:"Thái Âm",Khoa:"Hữu Bật",Kỵ:"Thiên Cơ"},
    Kỷ:{Lộc:"Vũ Khúc",Quyền:"Tham Lang",Khoa:"Thiên Lương",Kỵ:"Văn Khúc"},
    Canh:{Lộc:"Thái Dương",Quyền:"Vũ Khúc",Khoa:"Thiên Đồng",Kỵ:"Thái Âm"},
    Tân:{Lộc:"Cự Môn",Quyền:"Thái Dương",Khoa:"Văn Khúc",Kỵ:"Văn Xương"},
    Nhâm:{Lộc:"Thiên Lương",Quyền:"Tử Vi",Khoa:"Thiên Phủ",Kỵ:"Vũ Khúc"},
    Quý:{Lộc:"Phá Quân",Quyền:"Cự Môn",Khoa:"Thái Âm",Kỵ:"Tham Lang"},
  },
  DAC_TINH_LABEL: {M:"Miếu",V:"Vượng",Đ:"Đắc",B:"Bình",H:"Hãm"},
  CHINH_TINH: ["Tử Vi","Thiên Cơ","Thái Dương","Vũ Khúc","Thiên Đồng","Liêm Trinh","Thiên Phủ","Thái Âm","Tham Lang","Cự Môn","Thiên Tướng","Thiên Lương","Thất Sát","Phá Quân"],
  PHU_TINH: ["Tả Phụ","Hữu Bật","Văn Xương","Văn Khúc","Thiên Khôi","Thiên Việt","Lộc Tồn","Thiên Mã","Hóa Lộc","Hóa Quyền","Hóa Khoa","Hóa Kỵ","Thiên Hình","Thiên Riêu","Long Trì","Phượng Các","Đào Hoa","Hồng Loan","Thiên Hỷ","Cô Thần","Quả Tú","Thiên Tài","Thiên Thọ","Ân Quang","Thiên Quý","Tuần","Triệt","Trường Sinh","Mộc Dục","Quan Đới","Lâm Quan","Đế Vượng","Suy","Bệnh","Tử","Mộ","Tuyệt","Thai","Dưỡng","Bác Sỹ","Lực Sỹ","Thanh Long","Tiểu Hao","Tướng Quân","Tấu Thư","Phi Liêm","Hỷ Thần","Bệnh Phù","Đại Hao","Phục Binh","Quan Phủ","Phan Án","Tuế Dịch","Tức Thần","Tai Sát","Thiên Sát","Chỉ Bối","Hàm Trì","Nguyệt Sát","Vong Thần","Tuế Kiến","Hối Khí","Tang Môn","Quán Tác","Quan Phù","Long Đức","Bạch Hổ","Thiên Đức","Điếu Khách"],
  SAT_TINH: ["Kình Dương","Đà La","Hỏa Tinh","Linh Tinh","Địa Không","Địa Kiếp","Kiếp Sát","Thiên Không"],
  NATAL_STAR_MATRIX: {
    "Tử Vi":["B","Đ","M","B","V","M","M","Đ","M","B","V","B"],
    "Liêm Trinh":["V","Đ","V","H","M","H","V","Đ","V","H","M","H"],
    "Thiên Đồng":["V","H","M","Đ","H","Đ","H","H","M","H","H","Đ"],
    "Vũ Khúc":["V","M","V","Đ","M","H","V","M","V","Đ","M","H"],
    "Thái Dương":["H","Đ","V","V","V","M","M","Đ","H","H","H","H"],
    "Thiên Cơ":["Đ","Đ","H","M","M","V","Đ","Đ","V","M","M","H"],
    "Thiên Phủ":["Đ","V","Đ","M","B","H","B","Đ","Đ","Đ","Đ","Đ"],
    "Thái Âm":["V","Đ","H","H","H","H","H","Đ","V","M","M","M"],
    "Tham Lang":["H","M","Đ","H","V","H","H","M","Đ","H","V","H"],
    "Cự Môn":["V","H","V","M","H","H","V","H","Đ","M","H","Đ"],
    "Thiên Tướng":["V","Đ","M","H","V","Đ","V","Đ","M","H","V","Đ"],
    "Thiên Lương":["V","Đ","V","V","M","H","M","Đ","V","H","M","H"],
    "Thất Sát":["M","Đ","M","H","H","V","M","Đ","M","H","H","V"],
    "Phá Quân":["M","V","H","H","Đ","H","M","V","H","H","Đ","H"],
    "Văn Xương":["H","Đ","Đ","M","H","Đ","Đ","M","H","Đ","Đ","M"],
    "Văn Khúc":["B","V","Đ","M","H","V","Đ","M","H","V","Đ","M"],
    "Hỏa Tinh":["M","Đ","H","Đ","M","Đ","H","Đ","M","Đ","H","Đ"],
    "Linh Tinh":["M","Đ","H","Đ","M","Đ","H","Đ","M","Đ","H","Đ"],
    "Kình Dương":["","H","M","","H","M","","H","M","","H","M"],
    "Đà La":["H","","M","H","","M","H","","M","H","","M"],
  },
  TUAN_KHONG: {0:[10,11],1:[10,11],2:[8,9],3:[8,9],4:[6,7],5:[6,7],6:[4,5],7:[4,5],8:[2,3],9:[2,3]},
  TRIET_KHONG: {0:[8,9],1:[8,9],2:[6,7],3:[6,7],4:[4,5],5:[4,5],6:[2,3],7:[2,3],8:[0,1],9:[0,1]},
  TRANG_SINH_KHOI_DAU: {2:7,3:11,4:4,5:7,6:2},
  TUONG_QUAN_KHOI_DAU: {2:6,6:6,10:6,0:0,4:0,8:0,3:9,7:9,11:9,1:3,5:3,9:3},
  VONG_TRANG_SINH: ["Trường Sinh","Mộc Dục","Quan Đới","Lâm Quan","Đế Vượng","Suy","Bệnh","Tử","Mộ","Tuyệt","Thai","Dưỡng"],
  BAC_SY_12_THAN: ["Bác Sỹ","Lực Sỹ","Thanh Long","Tiểu Hao","Tướng Quân","Tấu Thư","Phi Liêm","Hỷ Thần","Bệnh Phù","Đại Hao","Phục Binh","Quan Phủ"],
  TUONG_QUAN_12_THAN: ["Tướng Quân","Phan Án","Tuế Dịch","Tức Thần","Hoa Cái","Kiếp Sát","Tai Sát","Thiên Sát","Chỉ Bối","Hàm Trì","Nguyệt Sát","Vong Thần"],
  TUE_PHA_12_THAN: ["Tuế Kiến","Hối Khí","Tang Môn","Quán Tác","Quan Phù","Tiểu Hao","Đại Hao","Long Đức","Bạch Hổ","Thiên Đức","Điếu Khách","Bệnh Phù"],
  NGU_HANH_NAP_AM: {
    "GiápTý":"Hải Trung Kim","ẤtSửu":"Hải Trung Kim","BínhDần":"Lô Trung Hỏa","ĐinhMão":"Lô Trung Hỏa","MậuThìn":"Đại Lâm Mộc","KỷTỵ":"Đại Lâm Mộc",
    "CanhNgọ":"Lộ Bàng Thổ","TânMùi":"Lộ Bàng Thổ","NhâmThân":"Kiếm Phong Kim","QuýDậu":"Kiếm Phong Kim","GiápTuất":"Sơn Đầu Hỏa","ẤtHợi":"Sơn Đầu Hỏa",
    "BínhTý":"Giản Hạ Thủy","ĐinhSửu":"Giản Hạ Thủy","MậuDần":"Thành Đầu Thổ","KỷMão":"Thành Đầu Thổ","CanhThìn":"Bạch Lạp Kim","TânTỵ":"Bạch Lạp Kim",
    "NhâmNgọ":"Dương Liễu Mộc","QuýMùi":"Dương Liễu Mộc","GiápThân":"Tuyền Trung Thủy","ẤtDậu":"Tuyền Trung Thủy","BínhTuất":"Ốc Thượng Thổ","ĐinhHợi":"Ốc Thượng Thổ",
    "MậuTý":"Tích Lịch Hỏa","KỷSửu":"Tích Lịch Hỏa","CanhDần":"Tùng Bách Mộc","TânMão":"Tùng Bách Mộc","NhâmThìn":"Trường Lưu Thủy","QuýTỵ":"Trường Lưu Thủy",
    "GiápNgọ":"Sa Trung Kim","ẤtMùi":"Sa Trung Kim","BínhThân":"Sơn Hạ Hỏa","ĐinhDậu":"Sơn Hạ Hỏa","MậuTuất":"Bình Địa Mộc","KỷHợi":"Bình Địa Mộc",
    "CanhTý":"Bích Thượng Thổ","TânSửu":"Bích Thượng Thổ","NhâmDần":"Kim Bạch Kim","QuýMão":"Kim Bạch Kim","GiápThìn":"Phú Đăng Hỏa","ẤtTỵ":"Phú Đăng Hỏa",
    "BínhNgọ":"Thiên Hà Thủy","ĐinhMùi":"Thiên Hà Thủy","MậuThân":"Đại Dịch Thổ","KỷDậu":"Đại Dịch Thổ","CanhTuất":"Thoa Xuyến Kim","TânHợi":"Thoa Xuyến Kim",
    "NhâmTý":"Tang Đố Mộc","QuýSửu":"Tang Đố Mộc","GiápDần":"Đại Khê Thủy","ẤtMão":"Đại Khê Thủy","BínhThìn":"Sa Trung Thổ","ĐinhTỵ":"Sa Trung Thổ",
    "MậuNgọ":"Thiên Thượng Hỏa","KỷMùi":"Thiên Thượng Hỏa","CanhThân":"Thạch Lựu Mộc","TânDậu":"Thạch Lựu Mộc","NhâmTuất":"Đại Hải Thủy","QuýHợi":"Đại Hải Thủy",
  },
};

const LUNAR_YEAR_INFO = [
  0x04bd8,0x04ae0,0x0a570,0x054d5,0x0d260,0x0d950,0x16554,0x056a0,0x09ad0,0x055d2,
  0x04ae0,0x0a5b6,0x0a4d0,0x0d250,0x1d255,0x0b540,0x0d6a0,0x0ada2,0x095b0,0x14977,
  0x04970,0x0a4b0,0x0b4b5,0x06a50,0x06d40,0x1ab54,0x02b60,0x09570,0x052f2,0x04970,
  0x06566,0x0d4a0,0x0ea50,0x06e95,0x05ad0,0x02b60,0x186e3,0x092e0,0x1c8d7,0x0c950,
  0x0d4a0,0x1d8a6,0x0b550,0x056a0,0x1a5b4,0x025d0,0x092d0,0x0d2b2,0x0a950,0x0b557,
  0x06ca0,0x0b550,0x15355,0x04da0,0x0a5d0,0x14573,0x052d0,0x0a9a8,0x0e950,0x06aa0,
  0x0aea6,0x0ab50,0x04b60,0x0aae4,0x0a570,0x05260,0x0f263,0x0d950,0x05b57,0x056a0,
  0x096d0,0x04dd5,0x04ad0,0x0a4d0,0x0d4d4,0x0d250,0x0d558,0x0b540,0x0b5a0,0x195a6,
  0x095b0,0x049b0,0x0a974,0x0a4b0,0x0b27a,0x06a50,0x06d40,0x0af46,0x0ab60,0x09570,
  0x04af5,0x04970,0x064b0,0x074a3,0x0ea50,0x06b58,0x05ac0,0x0ab60,0x096d5,0x092e0,
  0x0c960,0x0d954,0x0d4a0,0x0da50,0x07552,0x056a0,0x0abb7,0x025d0,0x092d0,0x0cab5,
  0x0a950,0x0b4a0,0x0baa4,0x0ad50,0x055d9,0x04ba0,0x0a5b0,0x15176,0x052b0,0x0a930,
  0x07954,0x06aa0,0x0ad50,0x05b52,0x04b60,0x0a6e6,0x0a4e0,0x0d260,0x0ea65,0x0d530,
  0x05aa0,0x076a3,0x096d0,0x04afb,0x04ad0,0x0a4d0,0x1d0b6,0x0d250,0x0d520,0x0dd45,
  0x0b5a0,0x056d0,0x055b2,0x049b0,0x0a577,0x0a4b0,0x0aa50,0x1b255,0x06d20,0x0ada0,
  0x14b63,0x09370,0x049f8,0x04970,0x064b0,0x168a6,0x0ea50,0x06aa0,0x1a6c4,0x0aae0,
  0x092e0,0x0d2e3,0x0c960,0x0d557,0x0d4a0,0x0da50,0x05d55,0x056a0,0x0a6d0,0x055d4,
  0x052d0,0x0a9b8,0x0a950,0x0b4a0,0x0b6a6,0x0ad50,0x055a0,0x0aba4,0x0a5b0,0x052b0,
  0x0b273,0x06930,0x07337,0x06aa0,0x0ad50,0x14b55,0x04b60,0x0a570,0x054e4,0x0d160,
  0x0e968,0x0d520,0x0daa0,0x16aa6,0x056d0,0x04ae0,0x0a9d4,0x0a2d0,0x0d150,0x0f252,
];

function lunarYearDays(info) {
  let total = 29 * 12;
  const leap = info & 0xf;
  if (leap) total += 29 + ((info >> 16) & 1);
  for (let m = 1; m <= 12; m++)
    if ((info >> (16 - m)) & 1) total += 1;
  return total;
}

function lunarMonthDays(info, month, leap) {
  if (leap) return (info >> 16) & 1 ? 30 : 29;
  return (info >> (16 - month)) & 1 ? 30 : 29;
}

function solarToLunar(year, month, day) {
  const LUNAR_EPOCH = new Date(1900, 0, 31);
  const dt = new Date(year, month - 1, day);
  let offset = Math.floor((dt - LUNAR_EPOCH) / 86400000);
  if (offset < 0) return [year, month, day, false];

  let lunarYear = 1900, idx = 0;
  while (idx < LUNAR_YEAR_INFO.length) {
    const yd = lunarYearDays(LUNAR_YEAR_INFO[idx]);
    if (offset < yd) break;
    offset -= yd;
    lunarYear++;
    idx++;
  }
  if (idx >= LUNAR_YEAR_INFO.length) return [year, month, day, false];

  const info = LUNAR_YEAR_INFO[idx];
  const leapMonth = info & 0xf;
  for (let m = 1; m <= 12; m++) {
    let md = lunarMonthDays(info, m, false);
    if (offset < md) return [lunarYear, m, offset + 1, false];
    offset -= md;
    if (m === leapMonth) {
      md = lunarMonthDays(info, m, true);
      if (offset < md) return [lunarYear, m, offset + 1, true];
      offset -= md;
    }
  }
  return [lunarYear, 12, 1, false];
}

function namCanChi(namDuongLich) {
  const offset = namDuongLich - 4;
  return [TUVIConfig.THIEN_CAN[offset % 10], TUVIConfig.DIA_CHI[offset % 12]];
}

function gioCanChi(ngayCan, gioDuong) {
  const gioMap = {0:0,1:1,2:1,3:2,4:2,5:3,6:3,7:4,8:4,9:5,10:5,11:6,12:6,13:7,14:7,15:8,16:8,17:9,18:9,19:10,20:10,21:11,22:11,23:0};
  const chiIdx = gioMap[gioDuong] || 0;
  const canIdx = (TUVIConfig.THIEN_CAN.indexOf(ngayCan) % 5 * 2 + chiIdx) % 10;
  return [TUVIConfig.THIEN_CAN[canIdx], TUVIConfig.DIA_CHI[chiIdx]];
}

function tinhCanCung(namCan, diaChiIndex) {
  const NGU_HO_DON = {Giáp:"Bính",Ất:"Mậu",Bính:"Canh",Đinh:"Nhâm",Mậu:"Giáp",Kỷ:"Bính",Canh:"Mậu",Tân:"Canh",Nhâm:"Nhâm",Quý:"Giáp"};
  const canDan = NGU_HO_DON[namCan] || "Bính";
  const canDanIdx = TUVIConfig.THIEN_CAN.indexOf(canDan);
  const offset = ((diaChiIndex - 2) % 12 + 12) % 12;
  const canIdx = (canDanIdx + offset) % 10;
  return TUVIConfig.THIEN_CAN[canIdx];
}

function tinhCuc(namCanIndex, cungMenhPos) {
  const namCan = TUVIConfig.THIEN_CAN[namCanIndex % 10];
  const canMenh = tinhCanCung(namCan, cungMenhPos % 12);
  const chiMenh = TUVIConfig.DIA_CHI[cungMenhPos % 12];
  const napAm = TUVIConfig.NGU_HANH_NAP_AM[canMenh + chiMenh] || "";
  let ju = 2;
  if (napAm.includes("Thủy")) ju = 2;
  else if (napAm.includes("Mộc")) ju = 3;
  else if (napAm.includes("Kim")) ju = 4;
  else if (napAm.includes("Thổ")) ju = 5;
  else if (napAm.includes("Hỏa")) ju = 6;
  return [ju, TUVIConfig.NGU_HANH[ju], TUVIConfig.NGU_HANH_NAME[ju]];
}

function tinhCungMenh(thangSinh, gioSinhIndex) {
  return ((13 + thangSinh - gioSinhIndex) % 12 + 12) % 12;
}

function tinhCungThan(thangSinh, gioSinhIndex) {
  return ((1 + thangSinh + gioSinhIndex) % 12 + 12) % 12;
}

function anTuVi(ngaySinh, cucSo) {
  if (![2,3,4,5,6].includes(cucSo)) cucSo = 2;
  const k = ((cucSo - (ngaySinh % cucSo)) % cucSo + cucSo) % cucSo;
  const q = Math.floor((ngaySinh + k) / cucSo);
  let pos;
  if (k % 2 === 0) pos = (q + k + 2) % 12;
  else pos = ((q - k + 2) % 12 + 12) % 12;
  return pos;
}

function anTuViTinhHe(tuViPos) {
  const ZIWEI_OFFSETS = { "Tử Vi":0, "Thiên Cơ":11, "Thái Dương":9, "Vũ Khúc":8, "Thiên Đồng":7, "Liêm Trinh":4 };
  const stars = {};
  for (const [ten, offset] of Object.entries(ZIWEI_OFFSETS)) {
    const pos = (tuViPos + offset) % 12;
    if (!stars[pos]) stars[pos] = [];
    stars[pos].push(ten);
  }
  return stars;
}

function anThienPhuTinhHe(tuViPos) {
  const ZIWEI_TO_TIANFU = {0:4,1:3,2:2,3:1,4:0,5:11,6:10,7:9,8:8,9:7,10:6,11:5};
  const TIANFU_OFFSETS = {"Thiên Phủ":0,"Thái Âm":1,"Tham Lang":2,"Cự Môn":3,"Thiên Tướng":4,"Thiên Lương":5,"Thất Sát":6,"Phá Quân":10};
  const stars = {};
  const thienPhuPos = ZIWEI_TO_TIANFU[tuViPos % 12];
  for (const [ten, offset] of Object.entries(TIANFU_OFFSETS)) {
    const pos = (thienPhuPos + offset) % 12;
    if (!stars[pos]) stars[pos] = [];
    stars[pos].push(ten);
  }
  return stars;
}

function anLocTon(namCan) {
  const LOC_TON_POS = {Giáp:2,Ất:3,Bính:5,Đinh:6,Mậu:5,Kỷ:6,Canh:8,Tân:9,Nhâm:11,Quý:0};
  return LOC_TON_POS[namCan] !== undefined ? LOC_TON_POS[namCan] : 2;
}

function anKinhDuongDaLa(locTonPos) {
  return {"Kình Dương": (locTonPos + 1) % 12, "Đà La": ((locTonPos - 1) % 12 + 12) % 12};
}

function anThienMa(namChi) {
  const THIEN_MA_POS = {Tý:2,Sửu:2,Dần:8,Mão:8,Thìn:8,Tỵ:11,Ngọ:11,Mùi:11,Thân:5,Dậu:5,Tuất:5,Hợi:2};
  return {"Thiên Mã": THIEN_MA_POS[namChi] || 2};
}

function anTaPhuHuuBat(gioIndex) {
  return {"Tả Phụ": (gioIndex + 4) % 12, "Hữu Bật": ((10 - gioIndex) % 12 + 12) % 12};
}

function anVanXuongKhuc(gioIndex) {
  return {"Văn Xương": ((10 - gioIndex) % 12 + 12) % 12, "Văn Khúc": (4 + gioIndex) % 12};
}

function anThienKhoiViet(namCan) {
  const table = {Giáp:[1,7],Ất:[0,8],Bính:[11,9],Đinh:[9,11],Mậu:[7,1],Kỷ:[0,8],Canh:[7,1],Tân:[6,2],Nhâm:[5,3],Quý:[3,5]};
  const [khoi, viet] = table[namCan] || [1, 7];
  return {"Thiên Khôi": khoi, "Thiên Việt": viet};
}

function anHoaLinh(namChiIndex, gioIndex) {
  const tableH = {0:3,1:4,2:8,3:9,4:2,5:3,6:7,7:8,8:1,9:2,10:6,11:7};
  const tableL = {0:9,1:8,2:5,3:4,4:1,5:0,6:9,7:8,8:5,9:4,10:1,11:0};
  const hoaBase = tableH[namChiIndex] !== undefined ? tableH[namChiIndex] : 3;
  const linhBase = tableL[namChiIndex] !== undefined ? tableL[namChiIndex] : 9;
  return {"Hỏa Tinh": (hoaBase + gioIndex) % 12, "Linh Tinh": (linhBase + gioIndex) % 12};
}

function anDiaKhongKiep(gioIndex) {
  return {"Địa Không": ((11 - gioIndex) % 12 + 12) % 12, "Địa Kiếp": (gioIndex + 11) % 12};
}

function anThaiTue(namChiIndex) { return {"Thái Tuế": namChiIndex}; }
function anThienKhong(namCanIndex) { const t={0:9,1:7,2:9,3:7,4:9,5:7,6:9,7:7,8:9,9:7}; return {"Thiên Không": t[namCanIndex] !== undefined ? t[namCanIndex] : 9}; }

function anDaoHoaHongLoanThienHy(namChiIndex) {
  const dao  = {0:9,1:6,2:3,3:0,4:9,5:6,6:3,7:0,8:9,9:6,10:3,11:0};
  const hong = {0:10,1:9,2:0,3:11,4:2,5:1,6:4,7:3,8:6,9:5,10:8,11:7};
  const hy   = {0:4,1:3,2:6,3:5,4:8,5:7,6:10,7:9,8:0,9:11,10:2,11:1};
  return {"Đào Hoa": dao[namChiIndex]||9, "Hồng Loan": hong[namChiIndex]||10, "Thiên Hỷ": hy[namChiIndex]||4};
}

function anCoThanQuaTu(namChiIndex) {
  const co  = {0:5,1:5,2:8,3:8,4:8,5:11,6:11,7:11,8:2,9:2,10:2,11:5};
  const qua = {0:7,1:7,2:10,3:10,4:10,5:1,6:1,7:1,8:4,9:4,10:4,11:7};
  return {"Cô Thần": co[namChiIndex]||5, "Quả Tú": qua[namChiIndex]||7};
}

function anThienHinh(namChiIndex) { const t={0:10,1:9,2:0,3:0,4:11,5:10,6:10,7:9,8:4,9:4,10:11,11:4}; return {"Thiên Hình": t[namChiIndex]!==undefined?t[namChiIndex]:10}; }
function anThienRieu(namChiIndex) { const t={0:3,1:2,2:1,3:0,4:11,5:10,6:9,7:8,8:7,9:6,10:5,11:4}; return {"Thiên Riêu": t[namChiIndex]!==undefined?t[namChiIndex]:3}; }

function anLongTriPhuongCac(namChiIndex) {
  const lt = {0:2,1:2,2:5,3:5,4:5,5:8,6:8,7:8,8:11,9:11,10:11,11:2};
  const pc = {0:4,1:4,2:7,3:7,4:7,5:10,6:10,7:10,8:1,9:1,10:1,11:4};
  return {"Long Trì": lt[namChiIndex]||2, "Phượng Các": pc[namChiIndex]||4};
}

function anAmQuangThienQuy(namChiIndex) { const t={0:1,1:1,2:10,3:10,4:5,5:5,6:2,7:2,8:5,9:5,10:10,11:10}; const v=t[namChiIndex]!==undefined?t[namChiIndex]:1; return {"Ân Quang":v,"Thiên Quý":v}; }
function anTamThaiBatToa(namChiIndex) { const ta={0:10,1:9,2:8,3:7,4:6,5:5,6:4,7:3,8:2,9:1,10:0,11:11}; const ba={0:2,1:3,2:4,3:5,4:6,5:7,6:8,7:9,8:10,9:11,10:0,11:1}; return {"Tam Thai":ta[namChiIndex]||10,"Bát Tọa":ba[namChiIndex]||2}; }
function anThienGiaiDiaGiai(namChiIndex) { return {"Thiên Giải":(namChiIndex+4)%12,"Địa Giải":(namChiIndex+6)%12}; }
function anThienThuongThienSu(cungNoBoc, cungTatAch) { return {"Thiên Thương":cungNoBoc,"Thiên Sứ":cungTatAch}; }
function anLuuHa(namChiIndex) { const t={0:10,1:9,2:4,3:3,4:10,5:9,6:4,7:3,8:10,9:9,10:4,11:3}; return {"Lưu Hà":t[namChiIndex]!==undefined?t[namChiIndex]:10}; }

function anKiepSat(namChiIndex) { const t={0:5,1:5,2:8,3:8,4:8,5:11,6:11,7:11,8:2,9:2,10:2,11:5}; return {"Kiếp Sát":t[namChiIndex]!==undefined?t[namChiIndex]:5}; }
function anHoaCai(namChiIndex) { const t={0:3,1:3,2:6,3:6,4:6,5:9,6:9,7:9,8:0,9:0,10:0,11:3}; return {"Hoa Cái":t[namChiIndex]!==undefined?t[namChiIndex]:3}; }
function anPhucDuc(namChiIndex) { const t={0:1,1:1,2:4,3:4,4:4,5:7,6:7,7:7,8:10,9:10,10:10,11:1}; return {"Phúc Đức":t[namChiIndex]!==undefined?t[namChiIndex]:1}; }

function anTuan(namCanIndex) { const pos=TUVIConfig.TUAN_KHONG[namCanIndex%10]||[10,11]; return {"Tuần":pos}; }
function anTriet(namCanIndex) { const pos=TUVIConfig.TRIET_KHONG[namCanIndex%10]||[8,9]; return {"Triệt":pos}; }

function anVongTrangSinh(namCanIndex, gioiTinh, cucSo) {
  const start = TUVIConfig.TRANG_SINH_KHOI_DAU[cucSo] || 7;
  const duongNam = namCanIndex % 2 === 0;
  const isMale = gioiTinh === "Nam";
  const thuan = (duongNam && isMale) || (!duongNam && !isMale);
  const result = {};
  for (let i = 0; i < TUVIConfig.VONG_TRANG_SINH.length; i++) {
    const pos = thuan ? (start + i) % 12 : ((start - i) % 12 + 12) % 12;
    result[TUVIConfig.VONG_TRANG_SINH[i]] = pos;
  }
  return result;
}

function anBacSy(locTonPos, namCanIndex, gioiTinh) {
  const duongNam = namCanIndex % 2 === 0;
  const isMale = gioiTinh === "Nam";
  const thuan = (duongNam && isMale) || (!duongNam && !isMale);
  const result = {};
  for (let i = 0; i < TUVIConfig.BAC_SY_12_THAN.length; i++) {
    const pos = thuan ? (locTonPos + i) % 12 : ((locTonPos - i) % 12 + 12) % 12;
    result[TUVIConfig.BAC_SY_12_THAN[i]] = pos;
  }
  return result;
}

function anTuongQuan(namChiIndex) {
  const start = TUVIConfig.TUONG_QUAN_KHOI_DAU[namChiIndex] !== undefined ? TUVIConfig.TUONG_QUAN_KHOI_DAU[namChiIndex] : 6;
  const result = {};
  for (let i = 0; i < TUVIConfig.TUONG_QUAN_12_THAN.length; i++)
    result[TUVIConfig.TUONG_QUAN_12_THAN[i]] = (start + i) % 12;
  return result;
}

function anTuePha(namChiIndex) {
  const result = {};
  for (let i = 0; i < TUVIConfig.TUE_PHA_12_THAN.length; i++)
    result[TUVIConfig.TUE_PHA_12_THAN[i]] = (namChiIndex + i) % 12;
  return result;
}

function tinhTuHoa(namCan) {
  const hoa = TUVIConfig.TU_HOA[namCan] || {};
  return {"Hóa Lộc": hoa["Lộc"] || "", "Hóa Quyền": hoa["Quyền"] || "", "Hóa Khoa": hoa["Khoa"] || "", "Hóa Kỵ": hoa["Kỵ"] || ""};
}

function tinhDaiHan(cungMenhPos, cucSo, gioiTinh, namCanIndex) {
  const amDuong = namCanIndex % 2 === 0 ? "Dương" : "Âm";
  const direction = (amDuong === "Dương" && gioiTinh === "Nam") || (amDuong === "Âm" && gioiTinh === "Nữ") ? 1 : -1;
  const daiHan = [];
  let startAge = cucSo;
  for (let i = 0; i < 12; i++) {
    const cungPos = ((cungMenhPos + i * direction) % 12 + 12) % 12;
    const ageStart = startAge + i * 10;
    daiHan.push({cung: TUVIConfig.TEN_12_CUNG[i], dia_chi: TUVIConfig.DIA_CHI[cungPos], tuoi: `${ageStart}-${ageStart+9}`, start_age: ageStart, end_age: ageStart+9, so_thu_tu: cungPos});
  }
  return daiHan;
}

function ngayCanChi(nam, thang, ngay) {
  const base = new Date(1900, 0, 1);
  const target = new Date(nam, thang - 1, ngay);
  const offset = Math.round((target - base) / 86400000);
  return [TUVIConfig.THIEN_CAN[(offset + 9) % 10], TUVIConfig.DIA_CHI[(offset + 0) % 12]];
}

function createChart(nam, thang, ngay, gio, gioiTinh) {
  const [namAm, thangAm, ngayAm, nhuan] = solarToLunar(nam, thang, ngay);
  const [namCan, namChi] = namCanChi(namAm);
  const namCanIndex = TUVIConfig.THIEN_CAN.indexOf(namCan);
  const namChiIndex = TUVIConfig.DIA_CHI.indexOf(namChi);
  const gioIndex = TUVIConfig.THOI_GIAN[gio] !== undefined ? TUVIConfig.THOI_GIAN[gio] : 0;
  const [ngayCan] = ngayCanChi(nam, thang, ngay);
  const [gioCan, gioChi] = gioCanChi(ngayCan, gio);

  const cungMenhPos = tinhCungMenh(thangAm, gioIndex);
  const cungThanPos = tinhCungThan(thangAm, gioIndex);

  const [cucSo, cucTen, cucHanh] = tinhCuc(namCanIndex, cungMenhPos);
  const tuViPos = anTuVi(ngayAm, cucSo);

  const diaBan = {};
  for (let i = 0; i < 12; i++) {
    const cungPos = ((cungMenhPos - i) % 12 + 12) % 12;
    diaBan[TUVIConfig.TEN_12_CUNG[i]] = {
      ten: TUVIConfig.TEN_12_CUNG[i], dia_chi: TUVIConfig.DIA_CHI[cungPos],
      so_thu_tu: cungPos, chinh_tinh: [], phu_tinh: [], sat_tinh: [], tu_hoa: [], dac_tinh: {}
    };
  }

  const starsAtPos = {};

  function addStars(pos, names, type) {
    if (!starsAtPos[pos]) starsAtPos[pos] = {chinh: [], phu: [], sat: []};
    for (const n of names) starsAtPos[pos][type].push(n);
  }

  // An chinh tinh
  for (const [pos, saos] of Object.entries(anTuViTinhHe(tuViPos))) addStars(Number(pos), saos, "chinh");
  for (const [pos, saos] of Object.entries(anThienPhuTinhHe(tuViPos))) addStars(Number(pos), saos, "chinh");

  const locTonPos = anLocTon(namCan);
  addStars(locTonPos, ["Lộc Tồn"], "phu");

  for (const [ten, pos] of Object.entries(anKinhDuongDaLa(locTonPos))) addStars(pos, [ten], "sat");
  for (const [ten, pos] of Object.entries(anThienMa(namChi))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anTaPhuHuuBat(gioIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anVanXuongKhuc(gioIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anThienKhoiViet(namCan))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anHoaLinh(namChiIndex, gioIndex))) addStars(pos, [ten], "sat");
  for (const [ten, pos] of Object.entries(anDiaKhongKiep(gioIndex))) addStars(pos, [ten], "sat");
  for (const [ten, pos] of Object.entries(anThaiTue(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anThienKhong(namCanIndex))) addStars(pos, [ten], "sat");
  for (const [ten, pos] of Object.entries(anDaoHoaHongLoanThienHy(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anCoThanQuaTu(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anThienHinh(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anThienRieu(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anLongTriPhuongCac(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anAmQuangThienQuy(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anTamThaiBatToa(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anThienGiaiDiaGiai(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anKiepSat(namChiIndex))) addStars(pos, [ten], "sat");
  for (const [ten, pos] of Object.entries(anHoaCai(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anPhucDuc(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anLuuHa(namChiIndex))) addStars(pos, [ten], "phu");

  const cungNoBoc = ((cungMenhPos - 5) % 12 + 12) % 12;
  const cungTatAch = ((cungMenhPos - 7) % 12 + 12) % 12;
  for (const [ten, pos] of Object.entries(anThienThuongThienSu(cungNoBoc, cungTatAch))) addStars(pos, [ten], "phu");

  for (const [ten, pair] of Object.entries(anTuan(namCanIndex))) for (const p of pair) addStars(p, [ten], "phu");
  for (const [ten, pair] of Object.entries(anTriet(namCanIndex))) for (const p of pair) addStars(p, [ten], "phu");

  for (const [ten, pos] of Object.entries(anVongTrangSinh(namCanIndex, gioiTinh, cucSo))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anBacSy(locTonPos, namCanIndex, gioiTinh))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anTuongQuan(namChiIndex))) addStars(pos, [ten], "phu");
  for (const [ten, pos] of Object.entries(anTuePha(namChiIndex))) addStars(pos, [ten], "phu");

  // Tu Hoa
  const tuHoa = tinhTuHoa(namCan);
  for (const [loai, sao] of Object.entries(tuHoa)) {
    if (!sao) continue;
    for (const [pos, data] of Object.entries(starsAtPos)) {
      if (data.chinh.includes(sao)) {
        if (!data.tu_hoa) data.tu_hoa = [];
        data.tu_hoa.push(`${sao}(${loai})`);
        break;
      }
    }
  }

  // Dac tinh
  for (const cungTen of TUVIConfig.TEN_12_CUNG) {
    const cungInfo = diaBan[cungTen];
    const pos = cungInfo.so_thu_tu;
    cungInfo.dac_tinh = {};
    if (starsAtPos[pos]) {
      const all = [...starsAtPos[pos].chinh, ...starsAtPos[pos].phu, ...starsAtPos[pos].sat];
      for (const sao of all) {
        const baseName = sao.split("(")[0];
        const matrix = TUVIConfig.NATAL_STAR_MATRIX[baseName];
        if (matrix && matrix[pos]) {
          cungInfo.dac_tinh[sao] = TUVIConfig.DAC_TINH_LABEL[matrix[pos]];
        }
      }
    }
  }

  // Fill dia ban
  for (const cungTen of TUVIConfig.TEN_12_CUNG) {
    const cungInfo = diaBan[cungTen];
    const pos = cungInfo.so_thu_tu;
    if (starsAtPos[pos]) {
      cungInfo.chinh_tinh = starsAtPos[pos].chinh || [];
      cungInfo.phu_tinh = starsAtPos[pos].phu || [];
      cungInfo.sat_tinh = starsAtPos[pos].sat || [];
      cungInfo.tu_hoa = starsAtPos[pos].tu_hoa || [];
    }
  }

  const cungList = TUVIConfig.TEN_12_CUNG.map(ten => {
    const c = diaBan[ten];
    return {
      ten: c.ten, dia_chi: c.dia_chi, so_thu_tu: c.so_thu_tu,
      can_cung: tinhCanCung(namCan, c.so_thu_tu),
      chinh_tinh: c.chinh_tinh, phu_tinh: c.phu_tinh, sat_tinh: c.sat_tinh,
      dac_tinh: c.dac_tinh, tu_hoa: c.tu_hoa,
      is_than: c.so_thu_tu === cungThanPos,
    };
  });

  const daiHan = tinhDaiHan(cungMenhPos, cucSo, gioiTinh, namCanIndex);

  const chartData = {
    thong_tin_co_ban: {
      duong_lich: `${nam}-${String(thang).padStart(2,'0')}-${String(ngay).padStart(2,'0')} ${gio}h`,
      am_lich: `${namAm} năm${nhuan ? ' nhuận' : ''} tháng ${thangAm} ngày ${ngayAm}`,
      gioi_tinh: gioiTinh, nam_can: namCan, nam_chi: namChi,
      nam_can_chi: `${namCan} ${namChi}`, gio_can_chi: `${gioCan} ${gioChi}`,
    },
    menh_ban: {
      cung_menh: TUVIConfig.DIA_CHI[cungMenhPos],
      cung_than: TUVIConfig.DIA_CHI[cungThanPos],
      cuc: cucTen, hanh: cucHanh,
    },
    tu_hoa: tuHoa,
    thap_nhi_cung: cungList,
    dai_han: daiHan,
  };

  return chartData;
}
