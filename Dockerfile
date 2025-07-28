# Use imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para /app no container
COPY requirements.txt .

# Copia todo o código da pasta 02_model_serving_api para dentro do container
COPY 02_model_serving_api/ ./02_model_serving_api/

# Instala as dependências do requirements.txt (está em /app)
RUN pip install --no-cache-dir -r requirements.txt

# Define o diretório de trabalho para rodar a API
WORKDIR /02_model_serving_api

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
