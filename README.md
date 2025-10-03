# 🚀 MLOps com DevSecOps – TCC

Pipeline de Machine Learning com integração de DevSecOps, priorizando automação, segurança e monitoramento contínuo, garantindo qualidade, rastreabilidade e confiabilidade do ciclo de desenvolvimento.

## 🌟 Features Principais

O projeto integra automação, segurança e monitoramento em todo o ciclo MLOps. Entre as funcionalidades destacam-se:

- **API FastAPI** servindo modelo ML (Iris)  
- **Segurança Automatizada**:
  - Bandit – análise estática de código Python
  - Safety – checagem de vulnerabilidades em dependências
  - Trivy – análise de imagens Docker e pacotes de SO
  - OPA – políticas de compliance (ex.: proibir root em containers)  
- **CI/CD com GitHub Actions**:
  - Lint (Flake8)
  - Testes automatizados (Pytest)
  - Build multi-stage e scan de imagens Docker
- **Containerização com Docker** (multi-stage build para reduzir tamanho da imagem)
- **Documentação completa** para reprodutibilidade e contribuições

---

## 🛠️ Como Executar Localmente

```bash
# Clonar o repositório
git clone https://github.com/sua-conta/mlops-devsecops-tcc.git
cd mlops-devsecops-tcc

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar API
uvicorn main:app --reload

A API estará disponível em:
http://127.0.0.1:8000/docs

## 🐳 Execução com Docker (Multi-Stage Build)
O Dockerfile utiliza multi-stage build para:

Stage 1: instalar dependências e compilar o código
Stage 2: criar imagem final leve (apenas binários e libs necessárias)

# Build da imagem
docker build -t mlops-devsecops:latest .

# Rodar container
docker run -p 8000:8000 mlops-devsecops:latest

## Estrutura do Projeto 
mlops-devsecops-tcc/
├── 00_baseline_app/
│   └── tests/
│       └── test_baseline.py      # Testes unitários da versão baseline
├── 01_model_training/
│   └── train_model.py            # Script de treinamento do modelo
├── 02_model_serving_api/
│   └── main.py                   # API FastAPI para servir o modelo
├── Dockerfile                     # Dockerfile para containerização multi-stage
├── metrics_collector.py           # Script para consolidar métricas de segurança e desempenho
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação do projeto

##📬 Exemplos de Requests/Responses
POST /predict

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Response:
{
  "species": "setosa",
  "confidence": 0.98
}

## ✅ Testes e Qualidade de Código
Local:
pytest --maxfail=1 --disable-warnings -q
flake8 .
bandit -r 01_model_training 02_model_serving_api
safety check

CI/CD:
Executa lint, testes unitários, scan de segurança (Bandit, Safety, Trivy) e aplica políticas OPA antes de build e deploy.

## 📥 Diagrama da Pipeline CI/CD

mermaid
graph TD
    A[Push no GitHub] --> B[CI: Flake8]
    B --> C[CI: Testes Unitários]
    C --> D[CI: Bandit]
    D --> E[CI: Trivy]
    E --> F[Build da Imagem Docker]
    F --> G[Deploy Local ou em Cloud]


## 🔒 Segurança Integrada
Bandit: detecta falhas comuns no código Python
Safety: analisa vulnerabilidades conhecidas nas dependências
Trivy: verifica vulnerabilidades em imagens Docker e pacotes OS

## 🌺 Sobre o Modelo e Dataset Iris
Dataset: Iris (flores classificadas em 3 espécies)

Modelo: Classificador treinado com scikit-learn

Entrada esperada:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}