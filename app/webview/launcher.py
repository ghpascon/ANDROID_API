import webview


def open_app(url: str = "http://127.0.0.1:8000") -> None:
    webview.create_window("ANDROID_API", url)
    webview.start()
