from .calendar import solar_to_lunar
from .can_chi import nam_can_chi, gio_can_chi, am_duong_nam, tinh_can_cung
from .config import THIEN_CAN, DIA_CHI, THOI_GIAN, TEN_12_CUNG, DAC_TINH_LABEL, NATAL_STAR_MATRIX
from .palaces import tinh_cung_menh, tinh_cung_than, lap_dia_ban
from .cuc import tinh_cuc
from .stars import (
    an_tu_vi, an_tu_vi_tinh_he, an_thien_phu_tinh_he,
    an_loc_ton, an_kinh_duong_da_la, an_thien_ma,
    an_ta_phu_huu_bat, an_van_xuong_khuc, an_thien_khoi_viet,
    an_hoa_linh, an_dia_khong_kiep, an_thai_tue, an_thien_khong,
    an_dao_hoa_hong_loan_thien_hy, an_co_than_qua_tu,
    an_thien_hinh, an_thien_rieu, an_long_tri_phuong_cac,
    an_am_quang_thien_quy, an_tam_thai_bat_toa,
    an_thien_giai_dia_giai, an_thien_thuong_thien_su,
    an_luu_ha, an_kiep_sat, an_hoa_cai, an_phuc_duc,
    an_tuan, an_triet, an_vong_trang_sinh, an_bac_sy,
    an_tuong_quan, an_tue_pha,
)
from .tu_hoa import tinh_tu_hoa, gan_tu_hoa_vao_cung
from .dai_han import tinh_dai_han


class LaSoTuVi:
    def __init__(self, nam, thang, ngay, gio, gioi_tinh="Nam"):
        self.nam = nam
        self.thang = thang
        self.ngay = ngay
        self.gio = gio
        self.gioi_tinh = gioi_tinh

        nam_a, thang_a, ngay_a, nhuan = solar_to_lunar(nam, thang, ngay)
        self.nam_am = nam_a
        self.thang_am = thang_a
        self.ngay_am = ngay_a
        self.nhuan = nhuan

        self.nam_can, self.nam_chi = nam_can_chi(self.nam_am)
        self.nam_can_index = THIEN_CAN.index(self.nam_can)
        self.nam_chi_index = DIA_CHI.index(self.nam_chi)
        self.gio_index = THOI_GIAN.get(gio, 0)
        gio_c, gio_c_idx = gio_can_chi(self.nam_can, gio)
        self.gio_can = gio_c

        self.cung_menh_pos = tinh_cung_menh(self.thang_am, self.gio_index)
        self.cung_than_pos = tinh_cung_than(self.thang_am, self.gio_index)

        cuc_so, cuc_ten, cuc_hanh = tinh_cuc(self.nam_can_index, self.cung_menh_pos)
        self.cuc_so = cuc_so
        self.cuc_ten = cuc_ten
        self.cuc_hanh = cuc_hanh

        self.tu_vi_pos = an_tu_vi(self.ngay_am, self.cuc_so)
        self.dia_ban = lap_dia_ban(self.cung_menh_pos)
        self.all_stars_positions = {}

        self._an_tat_ca_sao()
        self._tinh_dac_tinh()

    def _an_tat_ca_sao(self):
        stars_at_pos = {}

        for pos, saos in an_tu_vi_tinh_he(self.tu_vi_pos).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["chinh"].extend(saos)

        for pos, saos in an_thien_phu_tinh_he(self.tu_vi_pos).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["chinh"].extend(saos)

        loc_ton_pos = an_loc_ton(self.nam_can)
        stars_at_pos.setdefault(loc_ton_pos, {"chinh": [], "phu": [], "sat": []})
        stars_at_pos[loc_ton_pos]["phu"].append("Lộc Tồn")

        kd_dl = an_kinh_duong_da_la(loc_ton_pos)
        for ten, pos in kd_dl.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["sat"].append(ten)

        thien_ma = an_thien_ma(self.nam_chi)
        for ten, pos in thien_ma.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        ta_huu = an_ta_phu_huu_bat(self.gio_index)
        for ten, pos in ta_huu.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        vx_vk = an_van_xuong_khuc(self.gio_index)
        for ten, pos in vx_vk.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tk_tv = an_thien_khoi_viet(self.nam_can)
        for ten, pos in tk_tv.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        hoa_linh = an_hoa_linh(self.nam_chi_index, self.gio_index, self.nam_can_index, self.gioi_tinh)
        for ten, pos in hoa_linh.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["sat"].append(ten)

        dk_dj = an_dia_khong_kiep(self.gio_index)
        for ten, pos in dk_dj.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["sat"].append(ten)

        tt = an_thai_tue(self.nam_chi_index)
        for ten, pos in tt.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tk = an_thien_khong(self.nam_can_index)
        for ten, pos in tk.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["sat"].append(ten)

        dh = an_dao_hoa_hong_loan_thien_hy(self.nam_chi_index)
        for ten, pos in dh.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        ct_qt = an_co_than_qua_tu(self.nam_chi_index)
        for ten, pos in ct_qt.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        th = an_thien_hinh(self.nam_chi_index)
        for ten, pos in th.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tr = an_thien_rieu(self.nam_chi_index)
        for ten, pos in tr.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        lt_pc = an_long_tri_phuong_cac(self.nam_chi_index)
        for ten, pos in lt_pc.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        aq_tq = an_am_quang_thien_quy(self.nam_chi_index)
        for ten, pos in aq_tq.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tt_bt = an_tam_thai_bat_toa(self.nam_chi_index)
        for ten, pos in tt_bt.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tg_dg = an_thien_giai_dia_giai(self.nam_chi_index)
        for ten, pos in tg_dg.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        for ten, pos in an_kiep_sat(self.nam_chi_index).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["sat"].append(ten)
        for ten, pos in an_hoa_cai(self.nam_chi_index).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)
        for ten, pos in an_phuc_duc(self.nam_chi_index).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)
        for ten, pos in an_luu_ha(self.nam_chi_index).items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        cung_no_boc = (self.cung_menh_pos - 5) % 12
        cung_tat_ach = (self.cung_menh_pos - 7) % 12
        ts_tm = an_thien_thuong_thien_su(cung_no_boc, cung_tat_ach)
        for ten, pos in ts_tm.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tuan = an_tuan(self.nam_can_index)
        for ten, pos_pair in tuan.items():
            for p in pos_pair:
                stars_at_pos.setdefault(p, {"chinh": [], "phu": [], "sat": []})
                stars_at_pos[p]["phu"].append(ten)

        triet = an_triet(self.nam_can_index)
        for ten, pos_pair in triet.items():
            for p in pos_pair:
                stars_at_pos.setdefault(p, {"chinh": [], "phu": [], "sat": []})
                stars_at_pos[p]["phu"].append(ten)

        trang_sinh = an_vong_trang_sinh(self.nam_can_index, self.gioi_tinh, self.cuc_so)
        for ten, pos in trang_sinh.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        bac_sy = an_bac_sy(loc_ton_pos, self.nam_can_index, self.gioi_tinh)
        for ten, pos in bac_sy.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tuong_quan = an_tuong_quan(self.nam_chi_index)
        for ten, pos in tuong_quan.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        tue_pha = an_tue_pha(self.nam_chi_index)
        for ten, pos in tue_pha.items():
            stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
            stars_at_pos[pos]["phu"].append(ten)

        self._do_tu_hoa(stars_at_pos)

        self.all_stars_positions = {}
        for pos, sao_list in stars_at_pos.items():
            self.all_stars_positions[pos] = sao_list["chinh"] + sao_list["phu"] + sao_list["sat"]

        for cung_ten, cung_info in self.dia_ban.items():
            pos = cung_info["so_thu_tu"]
            if pos in stars_at_pos:
                cung_info["chinh_tinh"] = stars_at_pos[pos]["chinh"]
                cung_info["phu_tinh"] = stars_at_pos[pos]["phu"]
                cung_info["sat_tinh"] = stars_at_pos[pos]["sat"]

    def _do_tu_hoa(self, stars_at_pos):
        tu_hoa = tinh_tu_hoa(self.nam_can)
        self.tu_hoa = tu_hoa
        for loai, sao in tu_hoa.items():
            if not sao:
                continue
            for pos, data in stars_at_pos.items():
                if sao in data["chinh"]:
                    data["chinh"].append(f"{sao}({loai})")
                    stars_at_pos[pos]["tu_hoa"] = stars_at_pos[pos].get("tu_hoa", []) + [f"{sao}({loai})"]
                    break

    def _tinh_dac_tinh(self):
        for cung_ten, cung_info in self.dia_ban.items():
            pos = cung_info["so_thu_tu"]
            cung_info["dac_tinh"] = {}
            for sao in cung_info["chinh_tinh"] + cung_info["phu_tinh"] + cung_info["sat_tinh"]:
                base_name = sao.split("(")[0]
                if base_name in NATAL_STAR_MATRIX:
                    matrix = NATAL_STAR_MATRIX[base_name]
                    code = matrix[pos]
                    if code:
                        cung_info["dac_tinh"][sao] = DAC_TINH_LABEL.get(code, "")

    def tinh_dai_han(self):
        return tinh_dai_han(self.cung_menh_pos, self.cuc_so, self.gioi_tinh, self.nam_can_index)

    def to_dict(self):
        dai_han_data = self.tinh_dai_han()
        cung_list = []
        for cung_ten in TEN_12_CUNG:
            cung_info = self.dia_ban[cung_ten]
            dia_chi_idx = cung_info["so_thu_tu"]
            cung_list.append({
                "ten": cung_ten,
                "dia_chi": cung_info["dia_chi"],
                "so_thu_tu": dia_chi_idx,
                "can_cung": tinh_can_cung(self.nam_can, dia_chi_idx),
                "chinh_tinh": cung_info["chinh_tinh"],
                "phu_tinh": cung_info["phu_tinh"],
                "sat_tinh": cung_info["sat_tinh"],
                "dac_tinh": cung_info.get("dac_tinh", {}),
            })

        return {
            "thong_tin_co_ban": {
                "duong_lich": f"{self.nam}-{self.thang:02d}-{self.ngay:02d} {self.gio}h",
                "am_lich": f"{self.nam_am} năm {'nhuận' if self.nhuan else ''} tháng {self.thang_am} ngày {self.ngay_am}",
                "gioi_tinh": self.gioi_tinh,
                "nam_can": self.nam_can,
                "nam_chi": self.nam_chi,
                "nam_can_chi": f"{self.nam_can}{self.nam_chi}",
                "gio_can_chi": f"{self.gio_can}",
            },
            "menh_ban": {
                "cung_menh": DIA_CHI[self.cung_menh_pos],
                "cung_than": DIA_CHI[self.cung_than_pos],
                "cuc": self.cuc_ten,
                "hanh": self.cuc_hanh,
            },
            "tu_hoa": self.tu_hoa,
            "thap_nhi_cung": cung_list,
            "dai_han": dai_han_data,
        }
