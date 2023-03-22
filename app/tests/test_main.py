from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "Mangkorn"}

def test_write_main():
    name = "Mangkorn"
    response = client.post("/callname", json={"name": name})
    assert response.status_code == 200
    assert response.json() == {"hello": name}