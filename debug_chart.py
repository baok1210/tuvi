import sys
sys.path.insert(0, '.')
import json

from tuvi_engine.chart import LaSoTuVi

# Test case: 1996-11-15 6h Nam
ls = LaSoTuVi(1996, 11, 15, 6, 'Nam')
print("=== Internal state ===")
print(f"nam_am: {ls.nam_am}")
print(f"thang_am: {ls.thang_am}")
print(f"ngay_am: {ls.ngay_am}")
print(f"nhuan: {ls.nhuan}")
print(f"nam_can: {ls.nam_can}, nam_chi: {ls.nam_chi}")
print(f"nam_can_index: {ls.nam_can_index}")
print(f"nam_chi_index: {ls.nam_chi_index}")
print(f"gio_index: {ls.gio_index}")
print(f"gio_can: {ls.gio_can}")
print(f"cung_menh_pos: {ls.cung_menh_pos}")
print(f"cung_than_pos: {ls.cung_than_pos}")
print(f"cuc_so: {ls.cuc_so}, cuc_ten: {ls.cuc_ten}, cuc_hanh: {ls.cuc_hanh}")
print(f"tu_vi_pos: {ls.tu_vi_pos}")

print("\n=== Final chart dict ===")
data = ls.to_dict()
print(f"Cuc in dict: {data['menh_ban']['cuc']}")
print(f"Cung Menh in dict: {data['menh_ban']['cung_menh']}")
for cung in data['thap_nhi_cung']:
    if cung['ten'] == 'Mệnh':
        print(f"Mệnh sao chinh: {cung['chinh_tinh']}")
