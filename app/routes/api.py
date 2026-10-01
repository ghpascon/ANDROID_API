from fastapi import Request
from fastapi.responses import HTMLResponse

from app.api.schemas import ApiResponse, MessagePayload
from app.core.templates import templates


def _api_response(message: str, method: str, received: str | None = None) -> ApiResponse:
    return ApiResponse(
        status="ok",
        method=method,
        message=message,
        received=received,
    )


def get_root(request: Request):
    return templates.TemplateResponse(
        request,
        "pages/api_index.html",
        {
            "title": "API",
            "items": [
                {"label": "GET /hello", "path": "/hello"},
                {"label": "POST /echo", "path": "/echo"},
            ],
        },
    )


def get_hello():
    return _api_response("Olá do GET /hello", "GET")


async def post_echo(payload: MessagePayload):
    return _api_response("Mensagem recebida com sucesso", "POST", payload.message)


route_specs = [
    {
        "path": "/api",
        "endpoint": get_root,
        "methods": ["GET"],
        "response_class": HTMLResponse,
    },
    {
        "path": "/hello",
        "endpoint": get_hello,
        "methods": ["GET"],
    },
    {
        "path": "/echo",
        "endpoint": post_echo,
        "methods": ["POST"],
    },
]
