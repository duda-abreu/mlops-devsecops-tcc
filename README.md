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
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows

2. Instalar dependências
```bash
pip install -r requirements.txt

3. Treinar o modelo
```bash
python 01_model_training/train_model.py

4. Rodar a API localmente
```bash
uvicorn src.api:app --reload

5. Construir a imagem Docker
```bash
docker build -t mlops-devsecops-api .

6. Executar o container
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

## Sobre o modelo e o dataset Iris

Este projeto utiliza o dataset Iris, um conjunto e amplamente adotado no ensino e testes de algoritmos de aprendizado de máquina supervisionado. Ele contém 150 amostras de flores da espécie Iris, divididas em três classes (setosa, versicolor, virginica), com quatro características numéricas:

- Comprimento da sépala
- Largura da sépala
- Comprimento da pétala
- Largura da pétala

### Por que o Iris?

A motivação para o uso do dataset Iris está na sua simplicidade e formato estruturado, o que o torna ideal para prototipação rápida de pipelines de ML. Como objetivo deste projeto é testar, validar e demonstrar um pipeline completo com foco em DevSecOps, o Iris permite a construção de um modelo funcional sem a complexidade de pré-processamento ou coleta de dados externos.

### Aplicação

O modelo treinado com o Iris serve como ponto de partida para:

- Implementar a entrega de modelos via API com FastAPI;
- Validar práticas de CI/CD com GitHub Actions;
- Integrar ferramentas automatizadas de segurança;
- Testar monitoramento de métricas operacionais da API;
- Avaliar o comportamento de um pipeline real com métricas de desempenho e segurança coletadas em tempo de execução.

Embora simples, o modelo permite testar todas as etapas do ciclo de vida de machine learning em produção, sendo adequado para uma pesquisa, demonstração e validação prática dos conceitos de MLOps com DevSecOps.
