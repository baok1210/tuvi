import sys
sys.path.insert(0, r'H:\Tử vi')
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan

db = lapDiaBan(diaBan, 15, 11, 1996, 4, 1, True, 7)

for i in range(1, 13):
    cung = db.thapNhiCung[i]
    hoa_stars = [s for s in cung.cungSao if s["saoTen"] in ("H\xf3a l\u1ed9c", "H\xf3a quy\u1ec1n", "H\xf3a khoa", "H\xf3a k\u1ef5")]
    if hoa_stars:
        cung_chu = getattr(cung, "cungChu", "?")
        print(f"Cung {i} ({cung_chu})")
        for s in hoa_stars:
            sao_id = s.get("saoId", "?")
            print(f"  {s['saoTen']}: saoLoai={s['saoLoai']}, saoId={sao_id}")
            # Also show ALL stars at this cung to understand the context
            all_sao = [(ss["saoTen"], ss["saoLoai"]) for ss in cung.cungSao if ss["saoTen"] != s["saoTen"]]
            print(f"     Other stars: {all_sao}")
