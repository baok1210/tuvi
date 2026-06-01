import json
import sys
sys.path.insert(0, '.')

from tuvi_engine.chart import LaSoTuVi

ls = LaSoTuVi(nam=2008, thang=8, ngay=8, gio=10)
menh_cung = ls.dia_ban["Mệnh"]

result = {
    "cung_menh": menh_cung["dia_chi"],
    "chinh_tinh": menh_cung["chinh_tinh"],
    "phu_tinh": menh_cung["phu_tinh"],
    "sat_tinh": menh_cung["sat_tinh"]
}

# Write output to UTF-8 file
with open("result.txt", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
