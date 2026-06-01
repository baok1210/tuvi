import sys
sys.path.insert(0, r'H:\Tử vi')
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan

DAC_TINH_MAP = {"M": "Miếu", "V": "Vượng", "Đ": "Đắc", "H": "Hãm", "HĐ": "Hãm/Đắc"}

db = lapDiaBan(diaBan, 15, 11, 1996, 4, 1, True, 7)

for i in range(1, 13):
    cung = db.thapNhiCung[i]
    cung_chu = getattr(cung, "cungChu", "?")
    dac_tinhs = []
    for s in cung.cungSao:
        dt = s.get("saoDacTinh")
        if dt and dt != "Đ" and s["saoTen"] in ("Thiên đồng", "Thiên lương", "Tử vi", "Thái âm", "Thái Dương", "Liêm trinh", "Cự môn", "Thiên tướng", "Vũ khúc", "Thiên cơ", "Tham lang", "Phá quân", "Thất sát", "Thiên phủ"):
            print(f"  {cung_chu:10s} {s['saoTen']:12s} saoDacTinh={dt}")
