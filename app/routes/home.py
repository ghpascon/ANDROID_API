from fastapi import Request
from fastapi.responses import HTMLResponse

from app.core.templates import templates


def home_page(request: Request):
    return templates.TemplateResponse(
        request,
        "pages/home.html",
        {"title": "ANDROID_API", "message": "Bem-vindo ao app Android com API + WebView."},
    )


def docs_page(request: Request):
    paths = request.app.openapi().get("paths", {})
    routes = []
    for path, operations in paths.items():
        for method, details in operations.items():
            if method == "parameters":
                continue
            routes.append(
                {
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary") or details.get("description") or "Sem descrição",
                }
            )
    return templates.TemplateResponse(
        request,
        "pages/docs.html",
        {"title": "Documentação", "routes": routes},
    )


route_specs = [
    {
        "path": "/",
        "endpoint": home_page,
        "methods": ["GET"],
        "response_class": HTMLResponse,
    },
    {
        "path": "/docs-page",
        "endpoint": docs_page,
        "methods": ["GET"],
        "response_class": HTMLResponse,
    },
]
