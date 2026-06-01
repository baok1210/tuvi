import sys, json
sys.path.insert(0, r'H:\Tử vi')
from tuvi_engine.lasotuvi_adapter import LaSoTuVi

la_so = LaSoTuVi(1996, 11, 15, 6, "Nam")
data = la_so.to_dict()
for c in data['thap_nhi_cung']:
    dt = c.get('dac_tinh', {})
    if dt:
        print(f"{c['ten']:10s} {c['dia_chi']:4s}: {dt}")
print(f"\nTu hoa: {data['tu_hoa']}")
print(f"Da han count: {len(data['dai_han'])}")
