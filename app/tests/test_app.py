from fastapi.testclient import TestClient

from app.core.factory import create_app


client = TestClient(create_app())


def test_home_page_renders():
    response = client.get("/")
    assert response.status_code == 200
    assert "ANDROID_API" in response.text


def test_api_page_renders():
    response = client.get("/api")
    assert response.status_code == 200
    assert "/hello" in response.text


def test_get_hello_route():
    response = client.get("/hello")
    assert response.status_code == 200
    body = response.json()
    assert body["method"] == "GET"
    assert body["status"] == "ok"


def test_post_echo_route():
    response = client.post("/echo", json={"message": "teste"})
    assert response.status_code == 200
    body = response.json()
    assert body["received"] == "teste"
    assert body["method"] == "POST"


def test_fastapi_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "Swagger UI" in response.text
