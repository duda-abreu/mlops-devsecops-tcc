from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

def train_and_save_model():
    # carrega dados
    X, y = load_iris(return_X_y=True)

    # padroniza dados
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # treina modelo com mais iterações
    model = LogisticRegression(max_iter=1000)
    model.fit(X_scaled, y)

    # salva o modelo e o scaler na pasta da API
    path = "02_model_serving_api"
    joblib.dump(model, os.path.join(path, "model.pkl"))
    joblib.dump(scaler, os.path.join(path, "scaler.pkl"))

if __name__ == "__main__":
    train_and_save_model()
