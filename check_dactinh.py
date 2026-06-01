import sys
sys.path.insert(0, r'H:\Tử vi')
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan

db = lapDiaBan(diaBan, 15, 11, 1996, 4, 1, True, 7)

for i in range(1, 13):
    cung = db.thapNhiCung[i]
    cung_chu = getattr(cung, "cungChu", "?")
    # Check for any dac_tinh attributes
    attrs = [a for a in dir(cung) if not a.startswith("_") and "dac" in a.lower() or "tinh" in a.lower() or "vi" in a.lower() or "vuong" in a.lower()]
    if attrs:
        print(f"Cung {i} ({cung_chu}): {attrs}")
    # Check cungSao for strength info
    for s in cung.cungSao:
        if any(k for k in s.keys() if k not in ("saoTen", "saoLoai", "saoId")):
            extra = {k: v for k, v in s.items() if k not in ("saoTen", "saoLoai", "saoId")}
            if extra:
                print(f"  {s['saoTen']}: extra keys = {extra}")
                break
