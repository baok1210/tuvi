from pydantic import BaseModel, Field
from typing import Optional, List


class ChartRequest(BaseModel):
    nam: int = Field(..., ge=1900, le=2100, description="Năm sinh dương lịch")
    thang: int = Field(..., ge=1, le=12, description="Tháng sinh dương lịch")
    ngay: int = Field(..., ge=1, le=31, description="Ngày sinh dương lịch")
    gio: int = Field(..., ge=0, le=23, description="Giờ sinh (0-23)")
    gioi_tinh: str = Field("Nam", description="Giới tính (Nam/Nữ)")


class StarQuery(BaseModel):
    ten_sao: str = Field(..., description="Tên sao cần tra cứu")


class LuuNienRequest(BaseModel):
    nam: int = Field(..., ge=1900, le=2100, description="Năm sinh dương lịch")
    thang: int = Field(..., ge=1, le=12, description="Tháng sinh dương lịch")
    ngay: int = Field(..., ge=1, le=31, description="Ngày sinh dương lịch")
    gio: int = Field(..., ge=0, le=23, description="Giờ sinh (0-23)")
    gioi_tinh: str = Field("Nam", description="Giới tính (Nam/Nữ)")
    nam_xem: int = Field(..., ge=1900, le=2200, description="Năm cần xem lưu niên")


class ChatRequest(BaseModel):
    message: str = Field(..., description="Câu hỏi về tử vi")
    chart_data: Optional[dict] = Field(None, description="Dữ liệu lá số để phân tích cùng")


class RAGQuery(BaseModel):
    query: str = Field(..., description="Câu hỏi về tử vi")
    top_k: int = Field(3, ge=1, le=20, description="Số kết quả trả về")


class ChartResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None


class InterpretRequest(BaseModel):
    nam: int = Field(..., ge=1900, le=2100, description="Năm sinh dương lịch")
    thang: int = Field(..., ge=1, le=12, description="Tháng sinh dương lịch")
    ngay: int = Field(..., ge=1, le=31, description="Ngày sinh dương lịch")
    gio: int = Field(..., ge=0, le=23, description="Giờ sinh (0-23)")
    gioi_tinh: str = Field("Nam", description="Giới tính (Nam/Nữ)")
    model: str = Field("gpt-4o-mini", description="Tên model LLM")
    provider: Optional[str] = Field(None, description="Provider (openai, anthropic, deepseek, openrouter, groq, custom1-3)")
    base_url: Optional[str] = Field(None, description="Custom base URL cho OpenAI-compatible API")
    api_key: Optional[str] = Field(None, description="API key (override .env)")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Nhiệt độ sampling")
    max_tokens: int = Field(4096, ge=256, le=32768, description="Max tokens response")
    use_cache: bool = Field(True, description="Dùng cache nếu có")
    refresh: bool = Field(False, description="Bypass cache")


class AIStreamParams(BaseModel):
    model: str = Field("gpt-4o-mini", description="Tên model")
    provider: Optional[str] = Field(None, description="Provider")
    base_url: Optional[str] = Field(None, description="Custom base URL")
    api_key: Optional[str] = Field(None, description="Override API key")


class ModelsResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[str] = None
