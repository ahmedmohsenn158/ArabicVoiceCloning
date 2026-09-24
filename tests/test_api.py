from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "gpu": "Mock RTX 5090",
        "cuda": True,
        "model": "audar_flash",
        "model_loaded": True
    }

def test_status_endpoint():
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert "gpu" in data
    assert "model" in data
    assert data["model"]["name"] == "Audar Flash"
