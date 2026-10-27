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
