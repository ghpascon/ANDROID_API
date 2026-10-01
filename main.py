import argparse
import threading
import time

import uvicorn

from app.config import settings
from app.core.factory import create_app
from app.webview.launcher import open_app


def run_server(host: str = settings.host, port: int = settings.port):
    uvicorn.run(create_app(), host=host, port=port, reload=False)


def run_webview(host: str = settings.host, port: int = settings.port):
    app = create_app()
    server = uvicorn.Server(
        uvicorn.Config(app, host=host, port=port, log_level="warning")
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    while not server.started:
        time.sleep(0.05)
    open_app(f"http://{host}:{port}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Android API app")
    parser.add_argument("--webview", action="store_true", help="Open the app inside a desktop webview")
    parser.add_argument("--host", default=settings.host, help="Host to bind the server")
    parser.add_argument("--port", type=int, default=settings.port, help="Port to bind the server")
    args = parser.parse_args()

    if args.webview:
        run_webview(host=args.host, port=args.port)
    else:
        run_server(host=args.host, port=args.port)
