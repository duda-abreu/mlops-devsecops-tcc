# MLOps com DevSecOps - TCC

Projeto para desenvolvimento de pipeline de machine learning (MLOps) integrado a práticas de DevSecOps, com foco em automação, segurança e monitoramento contínuo.

Este pipeline inclui:

- API construída com FastAPI para servir modelos ML containerizados;
- Containerização via Docker;
- Segurança automatizada com Bandit (SAST), Safety (verificação de dependências) e Trivy (scanner de imagens);
- Pipeline CI/CD configurado com GitHub Actions para build, testes, lint e deploy automatizados;
- Planejamento para monitoramento com Prometheus e Grafana.

## Como rodar localmente
1. Treine o modelo:
```bash
python 01_model_training/train_model.py

2. Rodar a API localmente
```bash
uvicorn src.api:app --reload

3. Construir a imagem Docker
```bash
docker build -t mlops-devsecops-api .

4. Executar o container
```bash
docker run -p 8000:8000 mlops-devsecops-api

## Próximos passos
Implementar testes unitários completos e linting automatizado;

Integrar Trivy para análise de vulnerabilidades em imagens Docker;

Implementar Open Policy Agent (OPA) para políticas automatizadas;

Configurar monitoramento com Prometheus e dashboards no Grafana;

Analisar métricas reais de desempenho e segurança do pipeline;

Completar documentação e exemplos de uso.

## Objetivo do projeto
Construir e validar um pipeline MLOps seguro, automatizado e monitorável, integrando DevSecOps para garantir entregas confiáveis e contínuas de modelos de machine learning em ambiente cloud. O projeto serve como referência educacional e técnica, disponibilizando todo o código e documentação abertamente para a comunidade.