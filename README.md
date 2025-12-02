# 🚀 MLOps com DevSecOps – TCC

Pipeline completo de Machine Learning integrado a práticas de DevSecOps, unindo automação, segurança contínua, versionamento e monitoramento para garantir qualidade, rastreabilidade e confiabilidade do ciclo de desenvolvimento.

## 🌟 Principais Funcionalidades

Este projeto combina MLOps + DevSecOps em um fluxo automatizado, incluindo:

### 📦 API FastAPI servindo modelo ML
* Modelo **Iris** treinado com `scikit-learn`
* Pré-processamento com `StandardScaler`
* Endpoint `/predict` com validação automática de dados de entrada (`Pydantic`)
### 🔐 Segurança Automatizada (*Shift-Left*)

Ferramentas integradas ao pipeline de CI/CD para detecção proativa de vulnerabilidades:

| Categoria | Ferramenta | Função |
| :--- | :--- | :--- |
| Análise Estática de Código (SAST) | **Bandit** | Identificação de vulnerabilidades comuns em código Python. |
| Análise de Dependências (SCA) | **Safety** | Checagem de CVEs (Common Vulnerabilities and Exposures) em bibliotecas. |
| Análise de Imagens | **Trivy** | Scan de vulnerabilidades em imagens Docker e pacotes do SO base. |
| Compliance e Políticas | **OPA (Rego)** | Políticas de segurança como código (ex.: impedindo execução como `root` no container). |

### ⚙️ CI/CD com GitHub Actions

Pipeline automatizado que executa em cada *push* e *pull request*:

* Linting (`Flake8`)
* Testes unitários (`Pytest`)
* Scans de segurança (Bandit, Safety, Trivy)
* Validação de políticas **OPA**
* Build multi-stage **Docker**

### 🐳 Docker Multi-Stage Build

* Redução significativa do tamanho da imagem final.
* Ambiente isolado e reprodutível para o modelo.

### 📊 Coleta de Métricas

O script `metrics_collector.py` consolida automaticamente:

* Tempo de execução do pipeline e por etapa.
* Vulnerabilidades encontradas (Bandit, Safety, Trivy).
* Métricas de sucesso/erro dos testes.

---

## 🛠️ Como Executar Localmente

### 💻 API Local

```bash
# Clonar o repositório
git clone [https://github.com/duda-abreu/mlops-devsecops-tcc.git](https://github.com/duda-abreu/mlops-devsecops-tcc.git)
cd mlops-devsecops-tcc

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
.\venv\Scripts\activate    # Windows

# Instalar dependências
pip install -r requirements.txt

# Subir API
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
│   └── train_model.py            # Script de treino (com vulnerabilidades intencionais para demonstração)
├── 02_model_serving_api/
│   └── main.py                   # FastAPI + carregamento do modelo
├── 03_security_tests/          # Scripts auxiliares para execução dos scans
├── .github/workflows/          # Definição do pipeline CI/CD
├── opa-policies/               # Políticas Rego para OPA
├── tests/
│   └── test_main.py            # Testes da API
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

Resposta:
{
  "species": "setosa",
  "confidence": 0.98
}

## ✅ Testes e Qualidade de Código
Local:
Para executar localmente as checagens de qualidade e segurança:
```bash
pytest --maxfail=1 --disable-warnings -q
flake8 .
bandit -r 01_model_training 02_model_serving_api
safety check

CI/CD (GitHub Actions):
O pipeline executa automaticamente a suíte completa:

1. Lint

2. Testes unitários

3. Bandit (SAST)

4. Safety (SCA)

5. Trivy (Image Scan)

6. Validação OPA

7. Build da imagem Docker

## 📥 Diagrama da Pipeline CI/CD

mermaid
graph TD
    A[Push no GitHub] --> B(Flake8 - Lint)
    B --> C(Testes Unitários)
    C --> D(Bandit - SAST)
    D --> E(Safety + Trivy - SCA/Image Scan)
    E --> F(Validação com OPA - Compliance)
    F --> G[Build da Imagem Docker Multi-Stage]
    G --> H[Deploy Local/Cloud]


## 🔒 Segurança Integrada
Bandit: detecta falhas comuns no código Python
Safety: analisa vulnerabilidades conhecidas nas dependências
Trivy: verifica vulnerabilidades em imagens Docker
OPA: impede containers inseguros (ex.: rodar como root)

## 🌺 Sobre o Modelo e Dataset Iris
Dataset: Iris, 3 classes de flores

Modelo: LogisticRegression

Recursos de entrada esperados:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
