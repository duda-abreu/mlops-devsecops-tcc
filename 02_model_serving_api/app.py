from fastapi import FastAPI
import joblib
import os
import time
from prometheus_client import Counter, Histogram, generate_latest
from starlette.responses import Response

app = FastAPI()

# Carregando modelo
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Métricas Prometheus
REQUEST_COUNT = Counter('api_request_count', 'Total de requisições à API')
REQUEST_LATENCY = Histogram('api_request_latency_seconds', 'Latência das requisições em segundos')

@app.get("/")
def root():
    return {"message": "API de predição no ar"}

@app.post("/predict/")
def predict(features: list[float]):
    start_time = time.time()
    REQUEST_COUNT.inc()

    prediction = model.predict([features])
    latency = time.time() - start_time
    REQUEST_LATENCY.observe(latency)

    return {"prediction": int(prediction[0]), "latency": latency}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
