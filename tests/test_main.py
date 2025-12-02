from fastapi.testclient import TestClient
import sys
import os

# adiciona o diretório da API ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../02_model_serving_api')))
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de MLOps com DevSecOps"}

def test_predict_valid():
    payload = [5.1, 3.5, 1.4, 0.2] 
    response = client.post("/predict/", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_predict_missing_field():
    payload = [5.1, 3.5, 1.4]  # falta um valor
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422

def test_predict_wrong_type():
    payload = ["cinco", 3.5, 1.4, 0.2]  # primeiro campo inválido
    response = client.post("/predict/", json=payload)
    assert response.status_code == 422
