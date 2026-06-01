from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import router


def create_app():
    app = FastAPI(
        title="Tử Vi Đẩu Số - API",
        description="API phân tích lá số tử vi, tra cứu kiến thức sao, AI research endpoints",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)

    @app.get("/")
    def root():
        return {
            "service": "Tử Vi Đẩu Số Engine",
            "version": "1.0.0",
            "docs": "/docs",
            "endpoints": {
                "create_chart": "POST /api/v1/chart",
                "list_stars": "GET /api/v1/stars",
                "lookup_star": "POST /api/v1/stars/lookup",
                "list_palaces": "GET /api/v1/palaces",
                "lookup_palace": "GET /api/v1/palaces/{name}",
                "list_patterns": "GET /api/v1/patterns",
                "ai_knowledge": "GET /api/v1/ai-knowledge",
            }
        }

    return app


app = create_app()
