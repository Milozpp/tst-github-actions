from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.json["status"] == "ok"


def test_sum():
    client = app.test_client()
    response = client.get("/sum/2/3")
    assert response.json["result"] == 5