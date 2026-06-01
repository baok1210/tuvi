from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from .schemas import (ChartRequest, ChartResponse, StarQuery, ChatRequest,
                      LuuNienRequest, RAGQuery, InterpretRequest, AIStreamParams)
from tuvi_engine.lasotuvi_adapter import LaSoTuVi as LaSoTuViNew

try:
    from tuvi_engine.chart import LaSoTuVi as LaSoTuViOld
except ImportError:
    LaSoTuViOld = LaSoTuViNew

LaSoTuVi = LaSoTuViNew
from tuvi_engine.luu_nien import tinh_luu_nien_cho_laso
from tuvi_engine.config import DIA_CHI, THIEN_CAN
from tuvi_engine.can_chi import nam_can_chi
from knowledge.star_knowledge import tra_cuu_sao, danh_sach_sao
from knowledge.palace_meanings import tra_cuu_cung
from knowledge.patterns import nhan_dien_cach_cuc
from knowledge.interpretations import giai_doan_cung, giai_doan_toan_bo
from knowledge.star_combos import phan_tich_to_hop_sao
from knowledge.prompts import PromptBuilder
from knowledge.retriever import truy_xuat
from tuvi_engine.pipeline import Layer2RAG

router = APIRouter(prefix="/api/v1", tags=["Tu Vi"])


@router.post("/chart", response_model=ChartResponse)
def create_chart(req: ChartRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        data = la_so.to_dict()
        patterns = nhan_dien_cach_cuc(data)
        star_combos = phan_tich_to_hop_sao(data)
        data["cach_cuc"] = patterns
        data["ket_hop_sao"] = star_combos
        return ChartResponse(success=True, data=data)
    except ValueError as e:
        return ChartResponse(success=False, error=str(e))
    except Exception as e:
        return ChartResponse(success=False, error=f"Loi xu ly: {str(e)}")


@router.post("/chart/interpret", response_model=ChartResponse)
def interpret_chart(req: ChartRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        data = la_so.to_dict()
        patterns = nhan_dien_cach_cuc(data)
        star_combos = phan_tich_to_hop_sao(data)
        data["cach_cuc"] = patterns
        data["ket_hop_sao"] = star_combos

        giai_doan = giai_doan_toan_bo(data)
        luu_giai = []
        for gd in giai_doan:
            entry = {
                "cung": gd["ten"],
                "tieu_de": gd["tieu_de"],
                "phan_tich": gd["sao_phan_tich"],
            }
            luu_giai.append(entry)

        return ChartResponse(success=True, data={
            "thong_tin_co_ban": data["thong_tin_co_ban"],
            "menh_ban": data["menh_ban"],
            "tu_hoa": data["tu_hoa"],
            "cach_cuc": patterns,
            "ket_hop_sao": star_combos,
            "luan_giai": luu_giai,
        })
    except ValueError as e:
        return ChartResponse(success=False, error=str(e))
    except Exception as e:
        return ChartResponse(success=False, error=f"Loi xu ly: {str(e)}")


@router.post("/chart/luu-nien", response_model=ChartResponse)
def annual_flow(req: LuuNienRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        data = la_so.to_dict()
        patterns = nhan_dien_cach_cuc(data)
        combos = phan_tich_to_hop_sao(data)
        luu_nien = tinh_luu_nien_cho_laso(data, req.nam_xem)
        return ChartResponse(success=True, data={
            "thong_tin_co_ban": data["thong_tin_co_ban"],
            "menh_ban": data["menh_ban"],
            "cach_cuc": patterns,
            "ket_hop_sao": combos,
            "luu_nien": luu_nien,
        })
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/stars", response_model=ChartResponse)
def list_stars():
    try:
        return ChartResponse(success=True, data={"cac_sao": danh_sach_sao()})
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.post("/stars/lookup", response_model=ChartResponse)
def lookup_star(req: StarQuery):
    try:
        info = tra_cuu_sao(req.ten_sao.strip())
        if info is None:
            raise HTTPException(status_code=404, detail=f"Khong tim thay sao: {req.ten_sao}")
        return ChartResponse(success=True, data={"sao": req.ten_sao, "thong_tin": info["thong_tin"], "loai": info["loai"]})
    except HTTPException:
        raise
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/palaces/{ten_cung}", response_model=ChartResponse)
def lookup_palace(ten_cung: str):
    try:
        info = tra_cuu_cung(ten_cung.strip())
        if info is None:
            raise HTTPException(status_code=404, detail=f"Khong tim thay cung: {ten_cung}")
        return ChartResponse(success=True, data={"cung": ten_cung, "thong_tin": info})
    except HTTPException:
        raise
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/palaces", response_model=ChartResponse)
def list_palaces():
    from knowledge.palace_meanings import PALACE_MEANINGS
    return ChartResponse(success=True, data={"cac_cung": PALACE_MEANINGS})


@router.get("/patterns", response_model=ChartResponse)
def list_patterns():
    from knowledge.patterns import PATTERNS
    return ChartResponse(success=True, data={"cac_cach_cuc": PATTERNS})


@router.post("/patterns/detect", response_model=ChartResponse)
def detect_patterns(req: ChartRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        data = la_so.to_dict()
        patterns = nhan_dien_cach_cuc(data)
        combos = phan_tich_to_hop_sao(data)
        return ChartResponse(success=True, data={
            "cach_cuc": patterns,
            "ket_hop_sao": combos,
        })
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/knowledge/star-combos", response_model=ChartResponse)
def list_star_combos():
    from knowledge.star_combos import STAR_COMBOS
    result = [{"ten": v["ten"], "mo_ta": v["mo_ta"], "y_nghia": v["y_nghia"]} for v in STAR_COMBOS.values()]
    return ChartResponse(success=True, data={"cac_to_hop_sao": result})


@router.post("/prompt/general", response_model=ChartResponse)
def get_general_prompt(req: ChartRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        data = la_so.to_dict()
        patterns = nhan_dien_cach_cuc(data)
        combos = phan_tich_to_hop_sao(data)
        prompt = PromptBuilder.build_general(data, patterns, combos)
        return ChartResponse(success=True, data={"prompt": prompt, "length": len(prompt)})
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/ai-knowledge", response_model=ChartResponse)
def ai_knowledge():
    ds = danh_sach_sao()
    from knowledge.palace_meanings import PALACE_MEANINGS
    from knowledge.patterns import PATTERNS
    from knowledge.star_combos import STAR_COMBOS
    from knowledge.interpretations import PALACE_INTERPRETATIONS
    return ChartResponse(success=True, data={
        "stars": ds,
        "palaces": PALACE_MEANINGS,
        "patterns": [{"ten": p["ten"], "y_nghia": p["y_nghia"]} for p in PATTERNS],
        "star_combos": [{"ten": v["ten"], "y_nghia": v["y_nghia"]} for v in STAR_COMBOS.values()],
        "interpretations": {k: {"tieu_de": v["title"], "so_cung_cap": len(v["stars"])} for k, v in PALACE_INTERPRETATIONS.items()},
        "usage": {
            "chart": "POST /api/v1/chart",
            "chart_interpret": "POST /api/v1/chart/interpret",
            "luu_nien": "POST /api/v1/chart/luu-nien - Flow stars for a specific year",
            "star_lookup": "POST /api/v1/stars/lookup",
            "palace": "GET /api/v1/palaces/{ten}",
            "patterns_detect": "POST /api/v1/patterns/detect",
            "star_combos": "GET /api/v1/knowledge/star-combos",
            "prompt_general": "POST /api/v1/prompt/general",
            "rag_query": "POST /api/v1/rag/search - Search knowledge base",
            "stream_interpret": "GET /api/v1/stream/interpret - SSE streaming interpretation",
        }
    })


@router.get("/ai/models", response_model=ChartResponse)
def list_ai_models():
    from knowledge.llm.factory import ModelFactory
    return ChartResponse(success=True, data={"models": ModelFactory.list_supported_models()})


@router.post("/ai/interpret", response_model=ChartResponse)
def ai_interpret(req: InterpretRequest):
    try:
        la_so = LaSoTuVi(req.nam, req.thang, req.ngay, req.gio, req.gioi_tinh)
        chart_dict = la_so.to_dict()

        rag = Layer2RAG()
        result = rag.interpret(
            chart_dict,
            model=req.model,
            provider=req.provider,
            base_url=req.base_url,
            api_key=req.api_key,
            temperature=req.temperature,
            max_tokens=req.max_tokens,
            use_cache=req.use_cache,
            refresh=req.refresh,
        )

        return ChartResponse(success=True, data={
            "thong_tin_co_ban": chart_dict["thong_tin_co_ban"],
            "menh_ban": chart_dict["menh_ban"],
            "interpretation": result["interpretation"],
            "model": result["model"],
            "cached": result.get("cached", False),
        })
    except ImportError as e:
        return ChartResponse(success=False, error=f"Thiếu thư viện: {str(e)}. Chạy 'pip install openai anthropic'")
    except Exception as e:
        return ChartResponse(success=False, error=f"Lỗi luận giải AI: {str(e)}")


@router.post("/ai/chat", response_model=ChartResponse)
def ai_chat(req: ChatRequest):
    try:
        from knowledge.llm import ModelFactory
        model = req.chart_data.get("model", "gpt-4o-mini") if req.chart_data else "gpt-4o-mini"
        provider = req.chart_data.get("provider") if req.chart_data else None

        system_prompt = """Bạn là chuyên gia Tử Vi Đẩu Số. Trả lời câu hỏi của người dùng một cách chính xác, hữu ích.
Nếu có dữ liệu lá số, hãy dùng nó để phân tích. Nếu không, trả lời dựa trên kiến thức tử vi tổng quát."""

        user_prompt = req.message
        if req.chart_data and "thong_tin_co_ban" in req.chart_data:
            user_prompt = f"Dữ liệu lá số: {req.chart_data}\n\nCâu hỏi: {req.message}"

        client = ModelFactory.create(model=model, provider=provider)
        reply = client.generate(system_prompt, user_prompt)

        return ChartResponse(success=True, data={
            "reply": reply,
            "model": model,
        })
    except ImportError as e:
        return ChartResponse(success=False, error=f"Thiếu thư viện: {str(e)}")
    except Exception as e:
        return ChartResponse(success=False, error=f"Lỗi chat AI: {str(e)}")


@router.post("/rag/search", response_model=ChartResponse)
def rag_search(req: RAGQuery):
    try:
        results = truy_xuat(req.query, req.top_k)
        return ChartResponse(success=True, data=results)
    except Exception as e:
        return ChartResponse(success=False, error=str(e))


@router.get("/stream/interpret")
async def stream_interpret(
    nam: int = Query(..., ge=1900, le=2100),
    thang: int = Query(..., ge=1, le=12),
    ngay: int = Query(..., ge=1, le=31),
    gio: int = Query(..., ge=0, le=23),
    gioi_tinh: str = Query("Nam"),
):
    import json, asyncio, time

    async def event_stream():
        try:
            yield f"data: {json.dumps({'event': 'start', 'message': 'Dang xu ly la so...'})}\n\n"
            await asyncio.sleep(0.1)

            la_so = LaSoTuVi(nam, thang, ngay, gio, gioi_tinh)
            data = la_so.to_dict()

            yield f"data: {json.dumps({'event': 'chart', 'data': data['thong_tin_co_ban']})}\n\n"
            await asyncio.sleep(0.05)

            yield f"data: {json.dumps({'event': 'menh_ban', 'data': data['menh_ban']})}\n\n"
            await asyncio.sleep(0.05)

            patterns = nhan_dien_cach_cuc(data)
            combos = phan_tich_to_hop_sao(data)

            yield f"data: {json.dumps({'event': 'patterns', 'data': patterns})}\n\n"
            await asyncio.sleep(0.05)

            yield f"data: {json.dumps({'event': 'star_combos', 'data': combos})}\n\n"
            await asyncio.sleep(0.05)

            for i, cung in enumerate(data["thap_nhi_cung"]):
                gd = giai_doan_cung(
                    cung["ten"], cung["chinh_tinh"],
                    cung["phu_tinh"], cung["sat_tinh"],
                    cung.get("dac_tinh", {})
                )
                segment = {
                    "cung": cung["ten"],
                    "dia_chi": cung["dia_chi"],
                    "tieu_de": gd["tieu_de"],
                    "tong_quan": gd["tong_quan"],
                    "so_sao_phan_tich": len(gd["sao_phan_tich"]),
                    "phu_tinh": gd["phu_tinh"],
                    "sat_tinh": gd["sat_tinh"],
                }
                yield f"data: {json.dumps({'event': 'palace', 'index': i, 'data': segment})}\n\n"
                await asyncio.sleep(0.03)

            yield f"data: {json.dumps({'event': 'complete', 'total_palaces': 12})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'event': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )


@router.get("/stream/ai-interpret")
async def stream_ai_interpret(
    nam: int = Query(..., ge=1900, le=2100),
    thang: int = Query(..., ge=1, le=12),
    ngay: int = Query(..., ge=1, le=31),
    gio: int = Query(..., ge=0, le=23),
    gioi_tinh: str = Query("Nam"),
    model: str = Query("gpt-4o-mini"),
    provider: Optional[str] = Query(None),
    base_url: Optional[str] = Query(None),
    api_key: Optional[str] = Query(None),
):
    import json, asyncio

    async def event_stream():
        try:
            la_so = LaSoTuVi(nam, thang, ngay, gio, gioi_tinh)
            chart_dict = la_so.to_dict()

            yield f"data: {json.dumps({'event': 'start', 'data': chart_dict['thong_tin_co_ban']})}\n\n"
            await asyncio.sleep(0.1)

            rag = Layer2RAG()

            collected = []
            async for chunk in rag.interpret_stream(
                chart_dict, model=model, provider=provider,
                base_url=base_url, api_key=api_key,
            ):
                collected.append(chunk)
                yield f"data: {json.dumps({'event': 'token', 'text': chunk})}\n\n"

            full_text = "".join(collected)
            yield f"data: {json.dumps({'event': 'complete', 'text': full_text})}\n\n"

        except ImportError as e:
            yield f"data: {json.dumps({'event': 'error', 'message': f'Thiếu thư viện: {str(e)}'})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'event': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )
