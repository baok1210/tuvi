import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.AmDuong import diaChi, ngayThangNam, ngayThangNamCanChi, timCuc, nguHanh, thienCan
from .config import NGU_HANH, NGU_HANH_NAME, DIA_CHI, TEN_12_CUNG, THIEN_CAN

GIO_MAP = {0: 1, 23: 1, 1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4,
           7: 5, 8: 5, 9: 6, 10: 6, 11: 7, 12: 7, 13: 8, 14: 8,
           15: 9, 16: 9, 17: 10, 18: 10, 19: 11, 20: 11, 21: 12, 22: 12}

DIA_CHI_NUM = {c: i+1 for i, c in enumerate(DIA_CHI)}
DIA_CHI_FROM_NUM = {i+1: c for i, c in enumerate(DIA_CHI)}

STAR_CHINH_TINH = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
STAR_PHU_TINH = {15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
                  43, 44, 45, 46, 47, 48, 49, 50, 57, 58, 59, 60, 61, 62,
                  63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
                  77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                  91, 92, 93, 94}
STAR_SAT_TINH = {51, 52, 53, 54, 55, 56, 95, 96, 97, 98, 99, 100}

TU_HOA_RULES = {
    "Giáp": {"Lộc": "Liêm trinh", "Quyền": "Phá quân", "Khoa": "Vũ khúc", "Kỵ": "Thái Dương"},
    "Ất":  {"Lộc": "Thiên cơ",  "Quyền": "Thiên lương", "Khoa": "Tử vi",     "Kỵ": "Thái âm"},
    "Bính": {"Lộc": "Thiên đồng", "Quyền": "Thiên cơ",  "Khoa": "Văn xương", "Kỵ": "Liêm trinh"},
    "Đinh": {"Lộc": "Thái âm",   "Quyền": "Thiên đồng", "Khoa": "Thiên cơ",  "Kỵ": "Cự môn"},
    "Mậu": {"Lộc": "Tham lang",  "Quyền": "Thái Dương", "Khoa": "Hữu bật",   "Kỵ": "Thiên cơ"},
    "Kỷ":  {"Lộc": "Vũ khúc",    "Quyền": "Tham lang",  "Khoa": "Thiên lương","Kỵ": "Thái âm"},
    "Canh":{"Lộc": "Thái Dương", "Quyền": "Vũ khúc",    "Khoa": "Thái âm",   "Kỵ": "Thiên đồng"},
    "Tân": {"Lộc": "Cự môn",     "Quyền": "Thái âm",    "Khoa": "Văn xương", "Kỵ": "Vũ khúc"},
    "Nhâm":{"Lộc": "Thiên lương","Quyền": "Tử vi",      "Khoa": "Tả phù",    "Kỵ": "Tham lang"},
    "Quý": {"Lộc": "Phá quân",   "Quyền": "Cự môn",     "Khoa": "Thái âm",   "Kỵ": "Tham lang"},
}

PALACE_MAP_1BASED = {
    "Mệnh": 1, "Huynh đệ": 12, "Phu thê": 11, "Tử tức": 10,
    "Tài bạch": 9, "Tật ách": 8, "Thiên di": 7, "Nô bộc": 6,
    "Quan lộc": 5, "Điền trạch": 4, "Phúc đức": 3, "Phụ mẫu": 2,
}

class LaSoTuVi:
    def __init__(self, nam, thang, ngay, gio, gioi_tinh="Nam"):
        self.nam = nam
        self.thang = thang
        self.ngay = ngay
        self.gio = gio
        self.gioi_tinh = gioi_tinh

        gio_am = GIO_MAP.get(gio, 1)
        gioi_tinh_num = 1 if gioi_tinh in ("Nam", "nam", 1) else -1

        self._db = lapDiaBan(diaBan, ngay, thang, nam, gio_am, gioi_tinh_num, True, 7)

        nn, tt, nnnn, nhuan = ngayThangNam(ngay, thang, nam, True, 7)
        self.nam_am = nnnn
        self.thang_am = tt
        self.ngay_am = nn
        self.nhuan = bool(nhuan)

        can_thang, can_nam, chi_nam = ngayThangNamCanChi(nn, tt, nnnn, False, 7)
        self.can_nam = thienCan[can_nam]["tenCan"] if can_nam else ""
        self.chi_nam = diaChi[chi_nam]["tenChi"] if chi_nam else ""
        self.can_nam_idx = DIA_CHI_NUM.get(self.can_nam, 0)
        self.chi_nam_idx = DIA_CHI_NUM.get(self.chi_nam, 0)

        self.cung_menh_pos = self._db.cungMenh
        self.cung_than_pos = self._db.cungThan

        hanh_cuc = timCuc(self._db.cungMenh, can_nam)
        cuc_info = nguHanh(hanh_cuc)
        self.cuc_so = cuc_info["cuc"]
        self.cuc_ten = cuc_info["tenCuc"]
        self.cuc_hanh = cuc_info["tenHanh"]

        self.palace_data = {}
        self._extract_palaces()
        self._extract_tu_hoa()

    def _extract_palaces(self):
        DAC_MAP = {"M": "Miếu", "V": "Vượng", "Đ": "Đắc", "H": "Hãm"}
        for i in range(1, 13):
            cung = self._db.thapNhiCung[i]
            cung_chu = getattr(cung, "cungChu", "")
            chinh = []
            phu = []
            sat = []
            dac_tinh = {}
            for s in cung.cungSao:
                loai = s.get("saoLoai", 99)
                ten = s.get("saoTen", "")
                dt_raw = s.get("saoDacTinh")
                if dt_raw and dt_raw in DAC_MAP:
                    dac_tinh[ten] = DAC_MAP[dt_raw]
                if loai == 1:
                    chinh.append(ten)
                elif loai in {95}:
                    sat.append(ten)
                elif loai >= 11:
                    sat.append(ten)
                else:
                    phu.append(ten)
            self.palace_data[i] = {
                "ten": cung_chu,
                "dia_chi": diaChi[i]["tenChi"],
                "so_thu_tu": i - 1,
                "chinh_tinh": chinh,
                "phu_tinh": phu,
                "sat_tinh": sat,
                "dac_tinh": dac_tinh,
                "isThan": cung.cungThan,
            }

    def _extract_tu_hoa(self):
        self.tu_hoa = {"Lộc": "", "Quyền": "", "Khoa": "", "Kỵ": ""}
        rules = TU_HOA_RULES.get(self.can_nam, {})
        for loai_key in ("Lộc", "Quyền", "Khoa", "Kỵ"):
            expected = rules.get(loai_key, "")
            if not expected:
                continue
            expected_lower = expected.lower()
            for pos, data in self.palace_data.items():
                all_stars = [s.lower() for s in data["chinh_tinh"] + data["phu_tinh"] + data["sat_tinh"]]
                if expected_lower in all_stars:
                    self.tu_hoa[loai_key] = expected
                    break

    def _tinh_dac_tinh(self, stars):
        from .config import NATAL_STAR_MATRIX, DAC_TINH_LABEL
        result = {}
        for sao in stars:
            base = sao.split("(")[0]
            if base in NATAL_STAR_MATRIX:
                pass
        return result

    def _tinh_can_cung(self, cung_pos_0based):
        from .can_chi import tinh_can_cung
        return tinh_can_cung(self.can_nam, cung_pos_0based)

    def _tinh_dai_han(self):
        from .dai_han import tinh_dai_han as tdh
        can_idx = THIEN_CAN.index(self.can_nam) if self.can_nam in THIEN_CAN else 0
        return tdh(self.cung_menh_pos - 1, self.cuc_so, self.gioi_tinh, can_idx)

    def to_dict(self):
        cung_list = []
        start = self.cung_menh_pos
        for offset in range(12):
            pos_1based = (start - 1 - offset) % 12 + 1
            pos_0based = pos_1based - 1
            data = self.palace_data[pos_1based]
            cung_list.append({
                "ten": data["ten"],
                "dia_chi": data["dia_chi"],
                "so_thu_tu": pos_0based,
                "can_cung": self._tinh_can_cung(pos_0based),
                "is_than": data["isThan"],
                "chinh_tinh": data["chinh_tinh"],
                "phu_tinh": data["phu_tinh"],
                "sat_tinh": data["sat_tinh"],
                "dac_tinh": data["dac_tinh"],
            })

        dai_han_raw = self._tinh_dai_han()
        dai_han_list = []
        for offset, dh in enumerate(dai_han_raw):
            pos_1based = (start - 1 - offset) % 12 + 1
            palace = self.palace_data[pos_1based]
            dai_han_list.append({
                "cung": palace["ten"],
                "dia_chi": dh["dia_chi"],
                "tuoi": dh["tuoi"],
                "start_age": dh["start_age"],
                "end_age": dh["end_age"],
            })

        return {
            "thong_tin_co_ban": {
                "duong_lich": f"{self.nam}-{self.thang:02d}-{self.ngay:02d} {self.gio}h",
                "am_lich": f"{self.nam_am} năm{' nhuận' if self.nhuan else ''} tháng {self.thang_am} ngày {self.ngay_am}",
                "gioi_tinh": self.gioi_tinh,
                "nam_can": self.can_nam,
                "nam_chi": self.chi_nam,
                "nam_can_chi": f"{self.can_nam}{self.chi_nam}",
                "gio_can_chi": "",
            },
            "menh_ban": {
                "cung_menh": DIA_CHI[self.cung_menh_pos - 1],
                "cung_than": DIA_CHI[self.cung_than_pos - 1],
                "cuc": self.cuc_ten,
                "hanh": self.cuc_hanh,
            },
            "tu_hoa": self.tu_hoa,
            "thap_nhi_cung": cung_list,
            "dai_han": dai_han_list,
        }
