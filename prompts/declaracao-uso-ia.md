# Declaração de Uso de IA

**Nome:** a preencher pelo aluno.
**Data:** 25/10/2026.

## Ferramenta

ChatGPT / Codex. O identificador exato do modelo não foi registrado.

## Pedido do aluno

> a partir dele, analise o pdf dos requisitos, github e faça o que se pede

Contexto fornecido: PDF da Aula 21, repositório-modelo, link do Colab e CSV original da Netflix. A especificação estruturada derivada desse pedido está em `layout-skeleton-prompt.md`.

## Aplicação da IA

Análise dos requisitos, leitura da EDA, reprodução das duas transformações do dataset, planejamento do layout, adaptação do notebook, implementação do esqueleto Streamlit, testes e organização dos arquivos.

## Decisões aplicadas pelo assistente

- **Aceito na implementação:** layout com sidebar e duas áreas de conteúdo, leitura do CSV tratado e preservação das decisões da EDA.
- **Modificado:** variáveis e textos do exemplo Heart Disease foram adaptados à Netflix; o intervalo passou a usar uma variável escolhida pelo usuário; as ausências passaram a ter controle explícito para evitar exclusão automática.
- **Não incorporado nesta etapa:** implementação dos gráficos e KPIs, pois a página 21 do PDF reserva os gráficos à aula seguinte. Não houve imputação ou remoção de extremos.

Estas decisões registram o que o assistente implementou. Não representam aprovação ou revisão humana já realizada pelo aluno. O aluno deve preencher seu nome e registrar o que aceitou, modificou ou rejeitou após revisar a entrega.


## Complemento — Aula 22 (27/10/2026)

**Pedido do aluno:** “analise e vamos seguir”, acompanhado do PDF Aula 22 - Streamlit parte 2.

**Aplicação:** leitura do PDF e do roteiro atualizado; reorganização de entregas; preservação da EDA original; implementação dos gráficos e de quatro métricas, seleção interativa em Altair, notebook de planejamento e testes.

**Aceito na implementação pelo assistente:** Spearman da EDA; gráficos interativos Altair; quatro métricas com denominadores definidos; ausência explícita em resultados indisponíveis.

**Modificado:** rascunhos movidos para `entregas/`; `eda.ipynb` restaurado como cópia exata da EDA original e a versão exportadora colocada em `eda-com-downloads.ipynb`; filtros e barras conectados aos cartões por `on_select`; tema em vermelho, azul e neutros.

**Não incorporado:** taxas de crescimento ou deltas temporais sem uma base comparável; imputação de notas; exclusão automática de outliers. A identidade de origem pública e a licença do CSV não foram inventadas.

Estas decisões descrevem o trabalho do assistente. O aluno ainda deve registrar sua revisão, com o que aceitou, modificou ou rejeitou.

## Aplicação no projeto do VS Code — 27/10/2026

**Pedido do aluno:** “faça a parte 2 no meu vs code e após minha revisao de o commit no repositorio”.

A implementação da Aula 22 foi aplicada na pasta do projeto conectada ao repositório `joaopdornelas/PraticaAVD`. Os sete testes foram executados com o ambiente `.venv` dessa pasta e passaram. O dataset tratado foi conferido por SHA-256 e permaneceu igual. O aluno autorizou o commit e o push desta etapa em 27/10/2026.
