from .config import TEN_12_CUNG
from .chart import LaSoTuVi
from .phi_tinh import phi_cung_hoa_tuong, tu_hoa_analysis
from .cung_vi_bien_the import (
    thanh_lap_ban_tam_thoi, RELATION_MAP,
)
from .thai_tue_nhap_quai import y_niem_nhap_quai, thai_tue_nhap_quai
from .tam_phuong_tu_chinh import ghep_chuoi_tam_phuong, lay_sao_trong_tam_phuong


class Layer1Algorithm:
    def run(self, nam, thang, ngay, gio, gioi_tinh="Nam",
            doi_tuong=None, nam_sinh_doi_tuong=None, y_niem=None):

        chart_obj = LaSoTuVi(nam, thang, ngay, gio, gioi_tinh)
        la_so_dict = chart_obj.to_dict()
        thap_nhi_cung = la_so_dict["thap_nhi_cung"]

        ctx = {
            "birth": la_so_dict["thong_tin_co_ban"],
            "menh_ban": la_so_dict["menh_ban"],
            "analysis_subject": "Bản Thân",
            "tu_hoa": None,
            "all_palaces": [],
        }

        if doi_tuong and doi_tuong in RELATION_MAP:
            ban = thanh_lap_ban_tam_thoi(la_so_dict, doi_tuong)
            if ban:
                ctx["analysis_subject"] = doi_tuong
                ctx["subject_offset"] = ban["offset_dia_chi"]
                ctx["subject_menh_goc"] = ban["cung_goc_menh"]
                ctx["all_palaces"] = ban["cac_cung"]

        elif y_niem:
            ban = y_niem_nhap_quai(la_so_dict, y_niem)
            if ban:
                ctx["analysis_subject"] = f"Ý niệm: {y_niem}"
                ctx["subject_offset"] = ban["offset_dia_chi"]
                ctx["all_palaces"] = ban["cac_cung"]

        elif nam_sinh_doi_tuong is not None:
            ban = thai_tue_nhap_quai(la_so_dict, nam_sinh_doi_tuong)
            if ban:
                ctx["analysis_subject"] = f"Thái Tuế {ban['doi_tuong_nam_chi']}"
                ctx["subject_offset"] = ban["offset_dia_chi"]
                ctx["all_palaces"] = ban["cac_cung"]

        else:
            ctx["all_palaces"] = [
                {"cung_goc": c["ten"], "cung_tam_thoi": c["ten"],
                 "dia_chi": c["dia_chi"], "dia_chi_index": c["so_thu_tu"],
                 "chinh_tinh": c["chinh_tinh"], "phu_tinh": c["phu_tinh"],
                 "sat_tinh": c["sat_tinh"], "dac_tinh": c.get("dac_tinh", {}),
                 "can_cung": c.get("can_cung", "")}
                for c in thap_nhi_cung
            ]

        pt = phi_cung_hoa_tuong(la_so_dict)
        ctx["tu_hoa"] = pt.get("sinh_nien_tu_hoa")
        ctx["lai_nhan_cung"] = pt.get("lai_nhan_cung")
        ctx["phi_cung"] = pt.get("phi_cung", [])

        if ctx["tu_hoa"]:
            ctx["tu_hoa_analysis"] = tu_hoa_analysis(ctx["tu_hoa"], ctx["phi_cung"])

        if doi_tuong in [None, "Bản Thân"] and not y_niem and nam_sinh_doi_tuong is None:
            ctx["tam_phuong_strings"] = {}
            for pk in TEN_12_CUNG:
                ctx["tam_phuong_strings"][pk] = ghep_chuoi_tam_phuong(la_so_dict, pk)

        return ctx

    def format_context(self, ctx):
        lines = [
            f"THÔNG TIN CƠ BẢN",
            f"  Ngày sinh: {ctx['birth']['duong_lich']}",
            f"  Âm lịch: {ctx['birth']['am_lich']}",
            f"  Giới tính: {ctx['birth']['gioi_tinh']}",
            f"  Năm can chi: {ctx['birth']['nam_can_chi']}",
            f"  Mệnh: {ctx['menh_ban']['cung_menh']} - Thân: {ctx['menh_ban']['cung_than']}",
            f"  Cục: {ctx['menh_ban']['cuc']}",
            f"  Đối tượng PT: {ctx['analysis_subject']}",
            f"",
            f"TỨ HÓA NĂM SINH",
        ]
        if ctx["tu_hoa"]:
            for loai, info in ctx["tu_hoa"].items():
                lines.append(f"  {loai}: {info['sao']} tại {info['cung']} ({info['dia_chi']})")
        if ctx.get("lai_nhan_cung"):
            lines.append(f"  Lai Nhân Cung: {ctx['lai_nhan_cung']}")

        pc = ctx.get("phi_cung", [])
        if pc:
            lines.append(f"PHI CUNG HÓA TƯỢNG ({len(pc)} items)")
            for p in pc[:8]:
                lines.append(f"  {p['cung_goc']} ({p['thien_can']}) -> {p['loai']} {p['sao']} nhập {p['cung_dich']}")
            if len(pc) > 8:
                lines.append(f"  ... +{len(pc)-8} items")

        lines.append(f"LÁ SỐ (xoay theo đối tượng)")
        for c in ctx["all_palaces"]:
            ten = c.get("cung_tam_thoi", "")
            dc = c["dia_chi"]
            stars = c["chinh_tinh"] + c["phu_tinh"] + c["sat_tinh"]
            dc_map = c.get("dac_tinh", {})
            parts = []
            for s in stars:
                base = s.split("(")[0]
                b = dc_map.get(s, "")
                parts.append(f"{s}" + (f"({b})" if b else ""))
            label = f"{ten:10s}({dc})"
            lines.append(f"  {label}: {', '.join(parts) if parts else '(trống)'}")

        tps = ctx.get("tam_phuong_strings", {})
        if tps:
            for k, v in tps.items():
                lines.append(f"  Tam phương {k}: {v[:200]}")

        return "\n".join(lines)


class Layer2RAG:
    def __init__(self):
        from knowledge.retriever import truy_xuat
        from knowledge.classical.co_tuy_phu import ClassicalRuleEngine
        self.truy_xuat = truy_xuat
        self.rule_engine = ClassicalRuleEngine()

    def retrieve_relevant(self, context_str, top_k=3):
        results = {}
        keywords = ["Thiên Lương", "Tứ Hóa", "Bắc phái", "cách cục",
                    "Cốt Tủy Phú", "Lộc Tồn", "sao phụ", "tam hợp",
                    "Tử Vi", "Thất Sát", "cung Mệnh"]
        for kw in keywords:
            hits = self.truy_xuat(kw, top_k=1)
            if hits["results"]:
                results[kw] = [r["text"][:200] for r in hits["results"]]
        return results

    def build_prompt(self, context_str, retrieved):
        prompt = f"""Bạn là chuyên gia Tử Vi Đẩu Số. Dưới đây là dữ liệu lá số:

{context_str}

"""
        if retrieved:
            prompt += "KIẾN THỨC THAM KHẢO:\n"
            for topic, texts in retrieved.items():
                for t in texts[:2]:
                    prompt += f"- {t}\n"

        prompt += """
Hãy phân tích theo cấu trúc sau:
1. MỆNH CUNG: Phân tích sao chủ quản, ngũ hành, tính cách cốt lõi
2. TỨ HÓA: Ý nghĩa của Lộc/Quyền/Khoa/Kỵ và vị trí của chúng
3. SỰ NGHIỆP: Tài Bạch + Quan Lộc, tam phương tứ chính
4. TÌNH CẢM: Phu Thê + Phúc Đức
5. TÀI CHÍNH: Tài Bạch + Điền Trạch
6. SỨC KHỎE: Tật Ách
7. KẾT LUẬN: Tổng quan vận mệnh

Dùng ngôn ngữ chuyên môn Tử Vi, nhưng giải thích dễ hiểu."""
        return prompt

    def interpret(self, chart_dict, model="gpt-4o-mini", provider=None,
                  base_url=None, api_key=None, temperature=0.7,
                  max_tokens=4096, use_cache=True, refresh=False):
        from knowledge.llm import ModelFactory, LLMCache
        from tuvi_engine.pipeline import Layer1Algorithm

        l1 = Layer1Algorithm()
        ctx = l1.run(
            nam=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[0]),
            thang=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[1]),
            ngay=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[2].split(" ")[0]),
            gio=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("h")[0].split(" ")[-1]),
            gioi_tinh=chart_dict["thong_tin_co_ban"]["gioi_tinh"],
        )
        context_str = l1.format_context(ctx)
        retrieved = self.retrieve_relevant(context_str)
        user_prompt = self.build_prompt(context_str, retrieved)

        system_prompt = """Bạn là chuyên gia Tử Vi Đẩu Số Bắc Phái với 30 năm kinh nghiệm. Nhiệm vụ của bạn là luận giải lá số tử vi một cách chi tiết, chính xác và hữu ích.

NGUYÊN TẮC LUẬN GIẢI:
1. Phân tích dựa trên vị trí Miếu/Vượng/Đắc/Bình/Hãm của sao
2. Kết hợp Tứ Hóa (Lộc/Quyền/Khoa/Kỵ) và vị trí của chúng
3. Xem xét Ngã cung (Mệnh, Tài, Quan, Tật, Phúc, Điền) vs Tha cung
4. Phân tích Phi Cung Hóa Tượng (48 items)
5. Xem xét tam hợp và xung chiếu giữa các cung

YÊU CẦU ĐẦU RA:
- Luôn bằng tiếng Việt, văn phong chuyên nghiệp, dễ hiểu
- Có cấu trúc rõ ràng với các phần chính
- Nêu cụ thể tên sao, vị trí cung, đặc tính Miếu/Vượng/Hãm
- Kết luận trung thực, tránh tâng bốc hoặc dọa nạt
- Đưa lời khuyên thiết thực dựa trên luận giải"""

        cache = LLMCache()
        import json
        chart_json = json.dumps(chart_dict, ensure_ascii=False, sort_keys=True)

        if use_cache and not refresh:
            cached = cache.get(chart_json, model, user_prompt)
            if cached:
                return {"interpretation": cached, "cached": True, "model": model}

        client = ModelFactory.create(
            model=model, provider=provider,
            base_url=base_url, api_key=api_key,
            temperature=temperature, max_tokens=max_tokens,
        )
        result = client.generate(system_prompt, user_prompt)

        if use_cache:
            cache.set(chart_json, model, user_prompt, result)

        return {"interpretation": result, "cached": False, "model": model,
                "meta": client.get_meta()}

    async def interpret_stream(self, chart_dict, model="gpt-4o-mini", provider=None,
                                base_url=None, api_key=None, temperature=0.7,
                                max_tokens=4096):
        from knowledge.llm import ModelFactory
        from tuvi_engine.pipeline import Layer1Algorithm

        l1 = Layer1Algorithm()
        ctx = l1.run(
            nam=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[0]),
            thang=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[1]),
            ngay=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("-")[2].split(" ")[0]),
            gio=int(chart_dict["thong_tin_co_ban"]["duong_lich"].split("h")[0].split(" ")[-1]),
            gioi_tinh=chart_dict["thong_tin_co_ban"]["gioi_tinh"],
        )
        context_str = l1.format_context(ctx)
        retrieved = self.retrieve_relevant(context_str)
        user_prompt = self.build_prompt(context_str, retrieved)

        system_prompt = """Bạn là chuyên gia Tử Vi Đẩu Số Bắc Phái với 30 năm kinh nghiệm. Hãy luận giải chi tiết lá số này."""

        client = ModelFactory.create(
            model=model, provider=provider,
            base_url=base_url, api_key=api_key,
            temperature=temperature, max_tokens=max_tokens,
        )
        async for chunk in client.generate_stream(system_prompt, user_prompt):
            yield chunk
