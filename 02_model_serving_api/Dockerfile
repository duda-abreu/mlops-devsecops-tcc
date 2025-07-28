# Use imagem oficial do Python
FROM python:3.10-slim

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia arquivos necessários para dentro do container
COPY . /app

# Instala dependências (crie um requirements.txt com FastAPI, uvicorn, joblib, scikit-learn etc)
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar a API com reload desabilitado
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
