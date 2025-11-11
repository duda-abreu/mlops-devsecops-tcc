from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI(title="API de MLOps com DevSecOps")

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.get("/")
def root():
    return {"message": "API de MLOps com DevSecOps"}

@app.post("/predict/")
def predict(features: Features):
    # Converte Features para lista e aplica scaler
    values = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]
    scaled_values = scaler.transform([values])
    prediction = model.predict(scaled_values)
    return {"classe_predita": int(prediction[0])}
