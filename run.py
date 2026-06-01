#!/usr/bin/env python3
import sys
import json
import os
from datetime import datetime
from tuvi_engine.chart import LaSoTuVi
from knowledge.patterns import nhan_dien_cach_cuc


def setup_encoding():
    if sys.stdout.encoding and sys.stdout.encoding.lower() not in ('utf-8', 'utf8'):
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass


S = type("S", (), {})()
S = {
    "H1": "=" * 70,
    "H2": "        LA SO TU VI - CONG CU PHAN TICH & AI RESEARCH",
    "LINE": "-" * 70,
    "ARR": "->",
    "SINH": "[Sinh]",
    "AM": "[Am lich]",
    "GT": "[Gioi tinh]",
    "NAM": "[Nam]",
    "GIO": "[Gio]",
    "MENH": "[Menh]",
    "THAN": "[Than]",
    "CUC": "[Cuc]",
    "TU_HOA": "[Tu Hoa]",
    "CACH_CUC": "[Cach cuc]",
    "DAI_HAN": "[Dai han]",
    "CUNG": "Cung",
    "DIA_CHI": "Dia Chi",
    "CHINH_TINH": "Chinh Tinh",
    "TUOI": "Tuoi",
    "PHU": "Phu",
    "SAT": "Sat",
    "API": "[API] uvicorn api.server:app --reload",
    "DOCS": "[Docs] http://localhost:8000/docs",
    "SAVED": "Da luu JSON ra laso_output.json",
}


def print_chart(nam, thang, ngay, gio, gioi_tinh):
    la_so = LaSoTuVi(nam, thang, ngay, gio, gioi_tinh)
    data = la_so.to_dict()
    patterns = nhan_dien_cach_cuc(data)
    data["cach_cuc"] = patterns

    print(S["H1"])
    print(S["H2"])
    print(S["H1"])

    info = data["thong_tin_co_ban"]
    print(f"\n{S['SINH']} {info['duong_lich']}")
    print(f"{S['AM']} {info['am_lich']}")
    print(f"{S['GT']} {info['gioi_tinh']}")
    print(f"{S['NAM']} {info['nam_can_chi']}")
    print(f"{S['GIO']} {info['gio_can_chi']}")

    menh = data["menh_ban"]
    print(f"\n{S['MENH']} {menh['cung_menh']}  |  {S['THAN']} {menh['cung_than']}")
    print(f"{S['CUC']} {menh['cuc']} (Hanh {menh['hanh']})")

    tu_hoa = data["tu_hoa"]
    print(f"\n{S['TU_HOA']} Loc({tu_hoa['Hóa Lộc']})  Quyen({tu_hoa['Hóa Quyền']})  "
          f"Khoa({tu_hoa['Hóa Khoa']})  Ky({tu_hoa['Hóa Kỵ']})")

    if patterns:
        print(f"\n{S['CACH_CUC']}:")
        for p in patterns:
            print(f"   {S['ARR']} {p['cach_cuc']}: {p['y_nghia'][:80]}")

    print(f"\n{S['LINE']}")
    print(f"{S['CUNG']:<12} {S['DIA_CHI']:<8} {S['CHINH_TINH']:<40}")
    print(f"{S['LINE']}")
    for c in data["thap_nhi_cung"]:
        chinh = ", ".join(c["chinh_tinh"]) if c["chinh_tinh"] else "--"
        phu = ", ".join(c["phu_tinh"]) if c["phu_tinh"] else ""
        sat = ", ".join(c["sat_tinh"]) if c["sat_tinh"] else ""
        print(f"{c['ten']:<12} {c['dia_chi']:<8} {chinh:<40}")
        if phu:
            print(f"{'':<21} {S['PHU']}: {phu}")
        if sat:
            print(f"{'':<21} {S['SAT']}: {sat}")
    print(f"{S['LINE']}")

    print(f"\n{S['DAI_HAN']}:")
    print(f"  {S['CUNG']:<12} {S['DIA_CHI']:<8} {S['TUOI']:<12}")
    print(f"  {S['LINE'][:32]}")
    for dh in data["dai_han"]:
        print(f"  {dh['cung']:<12} {dh['dia_chi']:<8} {dh['tuoi']:<12}")

    print(f"\n{S['API']}")
    print(f"{S['DOCS']}")
    print(S["H1"])

    return data


def main():
    if len(sys.argv) >= 6:
        nam = int(sys.argv[1])
        thang = int(sys.argv[2])
        ngay = int(sys.argv[3])
        gio = int(sys.argv[4])
        gioi_tinh = sys.argv[5] if sys.argv[5] in ["Nam", "Nu"] else "Nam"
        data = print_chart(nam, thang, ngay, gio, gioi_tinh)
        with open("laso_output.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"\n{S['SAVED']}")
    elif len(sys.argv) == 2 and sys.argv[1] == "api":
        import uvicorn
        uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)
    else:
        now = datetime.now()
        print("=" * 60)
        print("  TU VI DAU SO - Cong cu Phan tich & AI Research API")
        print("=" * 60)
        print("\n[Usage]:")
        print("  python run.py 1990 8 15 14 Nam    # Lap la so")
        print("  python run.py api                   # Chay API server")
        print("  python run.py 1990 8 15 14 Nu     # Lap la so (Nu)")
        print("\n[API endpoints]:")
        print("  POST /api/v1/chart        - Tao la so")
        print("  GET  /api/v1/ai-knowledge - Tri thuc cho AI")
        print("  POST /api/v1/stars/lookup - Tra cuu sao")
        print("\n[Docs]: http://localhost:8000/docs\n")
        data = print_chart(now.year, now.month, now.day, now.hour, "Nam")


if __name__ == "__main__":
    main()
