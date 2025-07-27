from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

def train_and_save_model():
    X, y = load_iris(return_X_y=True)
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, '02_model_serving_api/model.pkl')

if __name__ == "__main__":
    train_and_save_model()
