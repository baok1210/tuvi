import sys
sys.path.insert(0, '.')

from tuvi_engine.chart import LaSoTuVi
from tuvi_engine.stars import (
    an_tu_vi_tinh_he, an_thien_phu_tinh_he, an_loc_ton,
    an_kinh_duong_da_la, an_thien_ma, an_ta_phu_huu_bat,
    an_van_xuong_khuc, an_thien_khoi_viet, an_hoa_linh,
    an_dia_khong_kiep, an_thai_tue, an_thien_khong,
    an_dao_hoa_hong_loan_thien_hy, an_co_than_qua_tu,
    an_thien_hinh, an_thien_rieu, an_long_tri_phuong_cac,
    an_am_quang_thien_quy, an_tam_thai_bat_toa,
    an_thien_giai_dia_giai, an_luu_ha, an_kiep_sat,
    an_hoa_cai, an_phuc_duc, an_tuan, an_triet,
    an_vong_trang_sinh, an_bac_sy, an_tuong_quan, an_tue_pha
)
from tuvi_engine.tu_hoa import tinh_tu_hoa, gan_tu_hoa_vao_cung

ls = LaSoTuVi(1996, 11, 15, 6, 'Nam')

print("=== Basic Info ===")
print(f"Nam am: {ls.nam_am}, Thang am: {ls.thang_am}, Ngay am: {ls.ngay_am}")
print(f"Nam can: {ls.nam_can}, Nam chi: {ls.nam_chi}")
print(f"Nam can index: {ls.nam_can_index}")
print(f"Gio index: {ls.gio_index}")
print(f"Cung menh pos: {ls.cung_menh_pos}")
print(f"Cuc so: {ls.cuc_so}")

print("\n=== Tu Vi Position ===")
print(f"Tu vi pos: {ls.tu_vi_pos}")

print("\n=== Star Placement Debug ===")
stars_at_pos = {}

# 1. Tu Vi tinh he
stars = an_tu_vi_tinh_he(ls.tu_vi_pos)
print(f"1. Tu Vi tinh he at Tu Vi pos {ls.tu_vi_pos}: {stars}")
for pos, saos in stars.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["chinh"].extend(saos)

# 2. Thien phu tinh he
stars = an_thien_phu_tinh_he(ls.tu_vi_pos)
print(f"2. Thien phu tinh he at Tu Vi pos {ls.tu_vi_pos}: {stars}")
for pos, saos in stars.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["chinh"].extend(saos)

# 3. Loc ton
loc_ton_pos = an_loc_ton(ls.nam_can)
print(f"3. Loc ton pos: {loc_ton_pos}")
stars_at_pos.setdefault(loc_ton_pos, {"chinh": [], "phu": [], "sat": []})
stars_at_pos[loc_ton_pos]["phu"].append("Lộc Tồn")

# 4. Kinh duong da la
kd_dl = an_kinh_duong_da_la(loc_ton_pos)
print(f"4. Kinh duong da la: {kd_dl}")
for ten, pos in kd_dl.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["sat"].append(ten)

# 5. Thien ma
thien_ma = an_thien_ma(ls.nam_chi)
print(f"5. Thien ma: {thien_ma}")
for ten, pos in thien_ma.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 6. Ta huu
ta_huu = an_ta_phu_huu_bat(ls.gio_index)
print(f"6. Ta huu: {ta_huu}")
for ten, pos in ta_huu.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 7. Van xuong khuc
vx_vk = an_van_xuong_khuc(ls.gio_index)
print(f"7. Van xuong khuc: {vx_vk}")
for ten, pos in vx_vk.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 8. Thien khoi viet
tk_tv = an_thien_khoi_viet(ls.nam_can)
print(f"8. Thien khoi viet: {tk_tv}")
for ten, pos in tk_tv.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 9. Hoa linh
hoa_linh = an_hoa_linh(ls.nam_chi_index, ls.gio_index)
print(f"9. Hoa linh: {hoa_linh}")
for ten, pos in hoa_linh.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["sat"].append(ten)

# 10. Dia khong kiep
dk_dj = an_dia_khong_kiep(ls.gio_index)
print(f"10. Dia khong kiep: {dk_dj}")
for ten, pos in dk_dj.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["sat"].append(ten)

# 11. Thai tue
tt = an_thai_tue(ls.nam_chi_index)
print(f"11. Thai tue: {tt}")
for ten, pos in tt.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 12. Thien khong
tk = an_thien_khong(ls.nam_can_index)
print(f"12. Thien khong: {tk}")
for ten, pos in tk.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["sat"].append(ten)

# 13. Dao hoa hong loan thien hy
dh = an_dao_hoa_hong_loan_thien_hy(ls.nam_chi_index)
print(f"13. Dao hoa hong loan thien hy: {dh}")
for ten, pos in dh.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 14. Co than qua tu
ct_qt = an_co_than_qua_tu(ls.nam_chi_index)
print(f"14. Co than qua tu: {ct_qt}")
for ten, pos in ct_qt.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 15. Thien hinh
th = an_thien_hinh(ls.nam_chi_index)
print(f"15. Thien hinh: {th}")
for ten, pos in th.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 16. Thien rieu
tr = an_thien_rieu(ls.nam_chi_index)
print(f"16. Thien rieu: {tr}")
for ten, pos in tr.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 17. Long tri phuong cac
lt_pc = an_long_tri_phuong_cac(ls.nam_chi_index)
print(f"17. Long tri phuong cac: {lt_pc}")
for ten, pos in lt_pc.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 18. Am quyen thien quy
aq_tq = an_am_quang_thien_quy(ls.nam_chi_index)
print(f"18. Am quyen thien quy: {aq_tq}")
for ten, pos in aq_tq.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 19. Tam thai bat toa
tt_bt = an_tam_thai_bat_toa(ls.nam_chi_index)
print(f"19. Tam thai bat toa: {tt_bt}")
for ten, pos in tt_bt.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 20. Thien giai dia giai
tg_dg = an_thien_giai_dia_giai(ls.nam_chi_index)
print(f"20. Thien giai dia giai: {tg_dg}")
for ten, pos in tg_dg.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 21. Kiep sat
for ten, pos in an_kiep_sat(ls.nam_chi_index).items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["sat"].append(ten)

# 22. Hoa cai
for ten, pos in an_hoa_cai(ls.nam_chi_index).items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 23. Phuc duc
for ten, pos in an_phuc_duc(ls.nam_chi_index).items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 24. Tuan
tuan = an_tuan(ls.nam_can_index)
print(f"24. Tuan: {tuan}")
for ten, pos_pair in tuan.items():
    for p in pos_pair:
        stars_at_pos.setdefault(p, {"chinh": [], "phu": [], "sat": []})
        stars_at_pos[p]["phu"].append(ten)

# 25. Triet
triet = an_triet(ls.nam_can_index)
print(f"25. Triet: {triet}")
for ten, pos_pair in triet.items():
    for p in pos_pair:
        stars_at_pos.setdefault(p, {"chinh": [], "phu": [], "sat": []})
        stars_at_pos[p]["phu"].append(ten)

# 26. Vong trang sinh
trang_sinh = an_vong_trang_sinh(ls.nam_can_index, ls.gioi_tinh, ls.cuc_so)
print(f"26. Vong trang sinh: {trang_sinh}")
for ten, pos in trang_sinh.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 27. Bac sy
bac_sy = an_bac_sy(loc_ton_pos, ls.nam_can_index, ls.gioi_tinh)
print(f"27. Bac sy: {bac_sy}")
for ten, pos in bac_sy.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 28. Tuong quan
tuong_quan = an_tuong_quan(ls.nam_chi_index)
print(f"28. Tuong quan: {tuong_quan}")
for ten, pos in tuong_quan.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# 29. Tue pha
tue_pha = an_tue_pha(ls.nam_chi_index)
print(f"29. Tue pha: {tue_pha}")
for ten, pos in tue_pha.items():
    stars_at_pos.setdefault(pos, {"chinh": [], "phu": [], "sat": []})
    stars_at_pos[pos]["phu"].append(ten)

# Apply tu hoa
tu_hoa = tinh_tu_hoa(ls.nam_can)
print(f"\nTu hoa: {tu_hoa}")
for loai, sao in tu_hoa.items():
    if not sao:
        continue
    for pos, data in stars_at_pos.items():
        if sao in data["chinh"]:
            data["chinh"].append(f"{sao}({loai})")
            stars_at_pos[pos]["tu_hoa"] = stars_at_pos[pos].get("tu_hoa", []) + [f"{sao}({loai})"]
            break

print(f"\n=== Final Stars at Position 8 ===")
if 8 in stars_at_pos:
    data = stars_at_pos[8]
    print(f"Chinh: {data['chinh']}")
    print(f"Phu: {data['phu']}")
    print(f"Sat: {data['sat']}")
else:
    print("No stars at position 8")

print(f"\n=== All Stars by Position ===")
for pos in range(12):
    if pos in stars_at_pos:
        data = stars_at_pos[pos]
        chinh = ', '.join(data['chinh']) if data['chinh'] else '--'
        phu = ', '.join(data['phu']) if data['phu'] else '--'
        sat = ', '.join(data['sat']) if data['sat'] else '--'
        print(f"Pos {pos:2d}: Chinh={chinh:<30} | Phu={phu:<30} | Sat={sat}")