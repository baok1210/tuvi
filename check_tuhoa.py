import sys
sys.path.insert(0, r'H:\Tử vi')
from tuvi_engine.lasotuvi_adapter import LaSoTuVi

for label, args in [
    ("1996 Bính Tý", (1996, 11, 15, 6, "Nam")),
    ("1988 Mậu Thìn", (1988, 4, 9, 11, "Nam")),
]:
    la_so = LaSoTuVi(*args)
    data = la_so.to_dict()
    print(f"{label}: {data['tu_hoa']}")
