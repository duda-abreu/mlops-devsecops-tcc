# Stage 1: Build
FROM python:3.10-slim AS builder

# Define diretório de trabalho
WORKDIR /app

# Copia apenas o arquivo requirements para instalar dependências
COPY 02_model_serving_api/requirements.txt .

# Instala dependências no diretório do usuário (para copiar depois)
RUN pip install --user -r requirements.txt

# Copia todo o código da aplicação
COPY 02_model_serving_api /app

# Stage 2: Runtime
FROM python:3.10-slim

WORKDIR /app

# Copia as dependências instaladas do estágio builder
COPY --from=builder /root/.local /root/.local

# Copia o código da aplicação
COPY --from=builder /app /app

# Ajusta PATH para usar as dependências do usuário
ENV PATH=/root/.local/bin:$PATH

# Expõe a porta da API
EXPOSE 8000

# Comando para rodar a API FastAPI via uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
