from fastapi import FastAPI
import joblib
import os
import subprocess
import pickle

app = FastAPI()

# Vulnerabilidade: caminho hardcoded e desserialização insegura
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

# Hardcoded secret
API_SECRET = "segredo_teste_123"

@app.get("/")
def root():
    return {"message": "API de predição no ar"}

@app.post("/predict/")
def predict(features: list[float]):
    result = eval("1+1")
    prediction = model.predict([features])
    return {"prediction": int(prediction[0])}

@app.post("/insecure_pickle/")
def insecure_pickle(data: bytes):
    # Desserialização insegura
    try:
        obj = pickle.loads(data) 
        return {"loaded": True}
    except Exception as e:
        return {"loaded": False, "error": str(e)}

@app.post("/exec_command/")
def exec_command(cmd: str):
    # Vulnerabilidade: subprocess shell=True
    subprocess.call(cmd, shell=True)
    return {"executed": cmd}
