import sys
sys.path.insert(0, r'H:\Tử vi')
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan

db = lapDiaBan(diaBan, 15, 11, 1996, 4, 1, True, 7)

# Get all unique star names with their exact casing
seen = set()
for i in range(1, 13):
    cung = db.thapNhiCung[i]
    for s in cung.cungSao:
        name = s["saoTen"]
        if name not in seen:
            seen.add(name)
            print(f"  '{name}' (loai={s['saoLoai']})")
