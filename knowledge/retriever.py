import re
from collections import Counter

KNOWLEDGE_SOURCES = []

def _build_index():
    global KNOWLEDGE_SOURCES
    if KNOWLEDGE_SOURCES:
        return

    from knowledge.star_knowledge import STAR_KNOWLEDGE
    for ten, info in STAR_KNOWLEDGE.items():
        text = f"{ten}: {info.get('thong_tin', '')}. {info.get('y_nghia', '')} {info.get('giai_doan', '')}"
        if info.get('tot'):
            text += f" Tốt: {info['tot']}."
        if info.get('xau'):
            text += f" Xấu: {info['xau']}."
        KNOWLEDGE_SOURCES.append({"type": "sao", "key": ten, "text": text})

    from knowledge.palace_meanings import PALACE_MEANINGS
    for ten, info in PALACE_MEANINGS.items():
        text = f"Cung {info.get('ten', ten)}: {info.get('y_nghia', '')} {info.get('mo_ta', '')}"
        KNOWLEDGE_SOURCES.append({"type": "cung", "key": ten, "text": text})

    from knowledge.patterns import PATTERNS
    for p in PATTERNS:
        text = f"Cách cục {p['ten']}: {p['mo_ta']}. {p['y_nghia']}."
        KNOWLEDGE_SOURCES.append({"type": "cach_cuc", "key": p["ten"], "text": text})

    from knowledge.star_combos import STAR_COMBOS
    for k, v in STAR_COMBOS.items():
        text = f"Tổ hợp sao {v['ten']}: {v['mo_ta']}. {v['y_nghia']}."
        KNOWLEDGE_SOURCES.append({"type": "to_hop_sao", "key": v["ten"], "text": text})

    from knowledge.classical.cach_cuc import TAT_CA_CACH_CUC
    for pc in TAT_CA_CACH_CUC:
        text = f"[{pc['loai']}] Cách cục {pc['ten']}: {pc['mo_ta']}. {pc['y_nghia']}."
        KNOWLEDGE_SOURCES.append({"type": "phu_quy_cach_cuc", "key": pc["ten"], "text": text})

    from knowledge.interpretations import PALACE_INTERPRETATIONS
    for cung_key, cung_data in PALACE_INTERPRETATIONS.items():
        text = f"Cung {cung_data.get('title', cung_key)}: {cung_data.get('general', '')}"
        KNOWLEDGE_SOURCES.append({"type": "luan_giai", "key": cung_key, "text": text})

    from knowledge.bac_phai_knowledge import BAC_PHAI_KNOWLEDGE, BAC_PHAI_QUY_TAC
    bp = BAC_PHAI_KNOWLEDGE
    gioi_thieu = bp["gioi_thieu"]
    text = f"Bắc phái: {gioi_thieu['ten_day_du']}. {', '.join(gioi_thieu['dac_trung'])}."
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "gioi_thieu", "text": text})

    for ten, info in bp["tu_hoa"]["cac_sao"].items():
        text = f"Tứ hóa {ten}: {info['y_nghia']}. Tính chất: {info['tinh_chat']}. Hạn chế: {info['khi_qua']}."
        KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": f"tu_hoa_{ten}", "text": text})

    text = f"Lai Nhân Cung: {bp['lai_nhan_cung']['y_nghia']}. Cách xác định: {bp['lai_nhan_cung']['cach_xac_dinh']}."
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "lai_nhan_cung", "text": text})

    text = f"Phi cung hóa tượng: {bp['phi_cung_hoa_tuong']['mo_ta']}."
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "phi_cung", "text": text})

    for q_key, qt in BAC_PHAI_QUY_TAC.items():
        text = f"Quy tắc Bắc phái ({q_key}): {qt}"
        KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": f"quy_tac_{q_key}", "text": text})

    for ky_thuat in bp["ky_thuat_co_ban"]:
        text = f"Kỹ thuật {ky_thuat['ten']}: {ky_thuat['mo_ta']}. {ky_thuat['y_nghia']}."
        KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": f"ky_thuat_{ky_thuat['ten']}", "text": text})

    text = f"Ngã cung: {', '.join(bp['nga_cung_tha_cung']['nga_cung'])}. {bp['nga_cung_tha_cung']['nga_cung_y_nghia']}. Tha cung: {', '.join(bp['nga_cung_tha_cung']['tha_cung'])}. {bp['nga_cung_tha_cung']['tha_cung_y_nghia']}."
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "nga_tha_cung", "text": text})

    text = f"Bảng Tứ Hóa 10 can: {str(bp['bang_tu_hoa']['bang'])}"
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "bang_tu_hoa", "text": text})

    text = f"Sao Nam: {', '.join(bp['sao_nam_sao_nu']['sao_nam'])}. Sao Nữ: {', '.join(bp['sao_nam_sao_nu']['sao_nu'])}. Đặc biệt: {bp['sao_nam_sao_nu']['sao_dac_biet']}."
    KNOWLEDGE_SOURCES.append({"type": "bac_phai", "key": "sao_nam_nu", "text": text})

    from knowledge.classical.co_tuy_phu import COT_TUY_PHU, THAI_VI_PHU, NU_MENH_PHU, CAC_SAO_PHU_NI_HAI_XIA

    for ch in COT_TUY_PHU.get("chapters", []):
        for i, paragraph in enumerate(ch.get("viet", ch.get("content", []))):
            text = f"Cốt Tủy Phú - {ch['title']}: {paragraph}"
            KNOWLEDGE_SOURCES.append({"type": "co_thu", "key": f"cot_tuy_{ch['title'][:10]}_{i}", "text": text})

    for rule in COT_TUY_PHU["rules"]:
        text = f"Cốt Tủy Phú - Luận đoán: {rule['rule']}. {rule.get('then', '')}."
        KNOWLEDGE_SOURCES.append({"type": "co_thu", "key": f"cot_tuy_rule_{rule['rule'][:30]}", "text": text})

    for rule in THAI_VI_PHU["rules"]:
        text = f"Thái Vi Phú: {rule}"
        KNOWLEDGE_SOURCES.append({"type": "co_thu", "key": f"thai_vi_{rule[:30]}", "text": text})

    for rule in NU_MENH_PHU["rules"]:
        text = f"Nữ Mệnh Phú: {rule}"
        KNOWLEDGE_SOURCES.append({"type": "co_thu", "key": f"nu_menh_{rule[:30]}", "text": text})

    for ten, y_nghia in CAC_SAO_PHU_NI_HAI_XIA.items():
        text = f"{ten}: {y_nghia}"
        KNOWLEDGE_SOURCES.append({"type": "sao_phu", "key": ten, "text": text})

    from knowledge.classical.tu_vi_toan_thu import ZI_WEI_QUAN_JI, ZI_WEI_QUAN_SHU
    for book in [ZI_WEI_QUAN_JI, ZI_WEI_QUAN_SHU]:
        for ch in book.get("chapters", []):
            for i, paragraph in enumerate(ch.get("viet", ch.get("content", []))):
                text = f"{book['title']} - {ch['title']}: {paragraph}"
                KNOWLEDGE_SOURCES.append({"type": "co_thu", "key": f"toan_thu_{book['slug'] if 'slug' in book else book['title'][:6]}_{ch['title'][:12]}_{i}", "text": text})

    from knowledge.classical.nihaixia import NI_HAIXIA_QUOTES, NI_HAIXIA_TEACHINGS
    for q in NI_HAIXIA_QUOTES:
        text = f"Ni Hải Hạ: {q['viet']} — {q['meaning']}"
        KNOWLEDGE_SOURCES.append({"type": "nihaixia", "key": q["quote"][:30], "text": text})

    for k, v in NI_HAIXIA_TEACHINGS.items():
        if isinstance(v, dict) and "dac_trung" in v:
            for dt in v["dac_trung"]:
                text = f"Ni Hải Hạ - {v.get('ten', k)}: {dt}"
                KNOWLEDGE_SOURCES.append({"type": "nihaixia", "key": f"teaching_{k}", "text": text})

    from knowledge.classical.hon_nhan import STAR_IN_MARRIAGE_PALACE, MARRIAGE_METHODOLOGY
    for ten, info in STAR_IN_MARRIAGE_PALACE.items():
        text = f"Hôn nhân - {ten} tại Phu Thê: {info['summary']}. Tốt: {info['good']}. Xấu: {info['bad']}. Phối ngẫu: {info['spouse']}."
        KNOWLEDGE_SOURCES.append({"type": "hon_nhan", "key": f"hon_nhan_{ten}", "text": text})

    text = f"Phương pháp luận hôn nhân: {MARRIAGE_METHODOLOGY[:500]}"
    KNOWLEDGE_SOURCES.append({"type": "hon_nhan", "key": "marriage_methodology", "text": text})

    from knowledge.classical.hon_nhan import MARRIAGE_STARS, MARRIAGE_SCORE_CRITERIA
    for ten, desc in MARRIAGE_STARS.items():
        text = f"Sao hôn nhân - {ten}: {desc}"
        KNOWLEDGE_SOURCES.append({"type": "hon_nhan", "key": f"star_{ten}", "text": text})
    for level, criteria in MARRIAGE_SCORE_CRITERIA.items():
        text = f"Hôn nhân {level}: {criteria}"
        KNOWLEDGE_SOURCES.append({"type": "hon_nhan", "key": f"score_{level}", "text": text})

    import json, os
    data_dir = os.path.join(os.path.dirname(__file__), "classical", "data")
    for fname in ["gusuifu.json", "quanji.json", "quanshu.json"]:
        fpath = os.path.join(data_dir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, encoding="utf-8") as f:
            book = json.load(f)
        for ch in book.get("chapters", []):
            for para in ch.get("paragraphs", []):
                text = f"{book.get('viet_title', book['title'])} - {ch['title']}: {para.get('text', '')}"
                KNOWLEDGE_SOURCES.append({
                    "type": "co_thu",
                    "key": f"{book['slug']}_{ch['title'][:15]}_{para.get('idx', 0)}",
                    "text": text,
                })

    from knowledge.classical.nihaixia import NI_HAIXIA_QUOTES, NI_HAIXIA_TEACHINGS, TIANJI_MODULES
    for q in NI_HAIXIA_QUOTES:
        text = f"Ni Hải Hạ: {q['viet']} — {q['meaning']}"
        KNOWLEDGE_SOURCES.append({"type": "nihaixia", "key": q.get("quote", q.get("id", ""))[:30], "text": text})

    for mod in TIANJI_MODULES:
        text = f"Ni Hải Hạ - {mod.get('name', '')} ({mod.get('nameEn', '')}): {mod.get('description', '')}"
        KNOWLEDGE_SOURCES.append({"type": "nihaixia", "key": f"module_{mod['id']}", "text": text})
        for ch in mod.get("chapters", []):
            for kp in ch.get("keyPoints", []):
                t = f"Ni Hải Hạ - {mod.get('name', '')}/{ch['title']}: {kp}"
                KNOWLEDGE_SOURCES.append({"type": "nihaixia", "key": f"kp_{mod['id']}_{ch.get('id', '')}", "text": t})


def _tokenize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    tokens = text.split()
    stop_words = {"và", "của", "có", "là", "được", "các", "một", "người", "cung",
                  "sao", "cách", "cục", "tổ", "hợp", "cho", "hoặc", "nhưng",
                  "nhiều", "không", "tại", "với", "trong", "về", "đến", "từ",
                  "ra", "lên", "xuống", "đi", "lại", "này", "kia", "những"}
    return [t for t in tokens if t not in stop_words and len(t) > 1]


def _bm25_score(query_tokens, doc_tokens, doc_len, avg_doc_len, total_docs, doc_freqs):
    k1, b = 1.5, 0.75
    score = 0.0
    for qt in set(query_tokens):
        tf = doc_tokens.count(qt)
        df = doc_freqs.get(qt, 0)
        idf = ((total_docs - df + 0.5) / (df + 0.5) + 1.0)
        if df == 0:
            idf = 1.0
        score += idf * (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * doc_len / avg_doc_len))
    return score


def truy_xuat(query, top_k=5):
    _build_index()

    query_tokens = _tokenize(query)
    if not query_tokens:
        return {"results": [], "query": query}

    total_docs = len(KNOWLEDGE_SOURCES)
    doc_tokens_list = [_tokenize(s["text"]) for s in KNOWLEDGE_SOURCES]
    avg_doc_len = sum(len(t) for t in doc_tokens_list) / max(total_docs, 1)

    doc_freqs = Counter()
    for tokens in doc_tokens_list:
        for t in set(tokens):
            doc_freqs[t] += 1

    scored = []
    for i, source in enumerate(KNOWLEDGE_SOURCES):
        tokens = doc_tokens_list[i]
        score = _bm25_score(query_tokens, tokens, len(tokens), avg_doc_len, total_docs, doc_freqs)
        if score > 0:
            scored.append((score, source))

    scored.sort(key=lambda x: -x[0])
    top = scored[:top_k]

    results = []
    for score, source in top:
        result = {
            "type": source["type"],
            "key": source["key"],
            "text": source["text"][:300],
            "score": round(score, 4),
        }
        results.append(result)

    return {"results": results, "query": query, "total_matched": len(results)}
