from fastapi import FastAPI

from app.config import settings
from app.routes import register_routes


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="API simples para Android com webview e documentação automática.",
    )
    register_routes(app)
    return app
