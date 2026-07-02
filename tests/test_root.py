from fastapi.testclient import TestClient
from app.main import app


def test_root():
    client = TestClient(app)
    res = client.get("/")
    assert res.status_code == 200
    assert 'Welcome to the General API' in res.text or 'message' in res.text
