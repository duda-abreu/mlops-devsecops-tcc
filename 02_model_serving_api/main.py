from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(
    title="API MLOps com FastAPI",
    description="Predição com modelo treinado + scaler",
    version="1.0",
)

# Carrega modelo e scaler treinados
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Define o formato esperado da entrada
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "API de MLOps com DevSecOps"}

@app.post("/predict")
def predict(data: IrisInput):
    # Converte entrada para numpy array
    input_array = np.array([[ 
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    # Aplica o mesmo scaler do treinamento
    input_scaled = scaler.transform(input_array)

    # Realiza predição
    prediction = model.predict(input_scaled)

    return {"classe_predita": int(prediction[0])}