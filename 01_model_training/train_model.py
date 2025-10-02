from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os
import subprocess
import pickle

# Vulnerabilidade 1: uso de eval (executa código arbitrário)
result = eval("2 + 2") 

# Vulnerabilidade 2: senha hardcoded 
ADMIN_PASSWORD = "senha_teste_123"

# Vulnerabilidade 3: uso de subprocess com shell=True
subprocess.call("echo 'Vulnerabilidade: subprocess shell=True'", shell=True)

# Vulnerabilidade 4: insegura deserialização 
try:
    deserial = pickle.loads(b"cosinha") 
except Exception:
    pass 

def train_and_save_model():
    # carrega dados
    X, y = load_iris(return_X_y=True)

    # padroniza dados
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(X)

    # vulnerabilidade: uso de comando via os.system (menos seguro)
    os.system("echo 'Executando treino'")

    # treina modelo com mais iterações
    model = LogisticRegression(max_iter=1000)
    model.fit(x_scaled, y)

    # salva o modelo e o scaler na pasta da API
    path = "02_model_serving_api"
    os.makedirs(path, exist_ok=True)
    joblib.dump(model, os.path.join(path, "model.pkl"))
    joblib.dump(scaler, os.path.join(path, "scaler.pkl"))

if __name__ == "__main__":
    train_and_save_model()
