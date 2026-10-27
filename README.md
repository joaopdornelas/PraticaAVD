# Netflix: correlação, distribuições e indicadores

Projeto das Aulas 21 e 22 de Análise e Visualização de Dados, 2026.2. Modelo: https://github.com/mfal-school/AVD-20262-pratica-streamlit (atualização consultada: `c8844b4`). Requisitos: PDFs das Aulas 21 e 22 e `ROTEIRO.md`.

## Executar no Windows

Python 3.12 utilizado na validação. Na pasta que contém `app.py`:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

Nas próximas execuções, basta o último comando. No macOS/Linux, use `python3` e `.venv/bin/python` no lugar dos caminhos Windows.

## Os dois dashboards

**Correlação e distribuição:** matriz de Spearman e histogramas interativos em Altair. Os filtros recalculam ambos. A matriz mostra o número de pares válidos no hover e indica coeficientes indefinidos. Na comparação por tipo, os histogramas usam intervalos iguais e percentuais por grupo. Votos e popularidade podem ser visualizados em log(1 + valor), sem modificar os dados.

**Indicadores do catálogo:** quatro cartões (total, cobertura IMDb, mediana IMDb e participação de séries). Barras agrupadas por gênero, país ou tipo permitem selecionar categorias e atualizar os cartões e o gráfico de lançamentos por década. Clique seleciona, Shift + clique seleciona várias categorias, e duplo clique ou o botão limpa. Os filtros gerais afetam as duas abas; seleção das barras refina somente a segunda.

## Notebooks e dados

- `notebooks/eda.ipynb`: cópia exata do Colab original do aluno, preservada conforme o roteiro atualizado. O carregamento original usa upload manual.
- `notebooks/eda-com-downloads.ipynb`: versão adaptada da EDA do aluno para execução local/Colab e exportação. Execute todas as células para gerar `data/raw/dataset.csv` e `data/clean/dataset.csv`.
- `notebooks/arquivo-eda-original.ipynb`: referência da professora, mantida.
- `notebooks/metricas.ipynb`: planejamento, fórmulas, conferências e visuais prévios do Dashboard 2.
- `data/raw/dataset.csv`: original local, incluído no ZIP, ignorado pelo Git como no modelo.
- `data/clean/dataset.csv`: base usada pelo aplicativo e versionada. 7.786 linhas e 42 colunas.

A EDA mantém todos os títulos, ausências e extremos. Acrescenta `tipo_conteudo` (Filme/Série) e `imdb_votes_log`. A base principal é `df`; `df_notas` é apenas o subconjunto de 5.331 títulos com as duas notas.

Fonte do notebook: https://colab.research.google.com/drive/1LBwfll2VYpDFk61nXW9KonxWqa0oK7wt

CSV original fornecido pelo aluno: `netflix_content_intelligence_combined.csv`. Proveniência em `data/proveniencia.json`. A fonte pública original e a licença ainda precisam ser documentadas. Os lançamentos vão até 2021; esta base não descreve o catálogo atual da Netflix.

## Entregáveis e documentação

- `entregas/rascunho-dashboard1.png` e `entregas/rascunho-dashboard2.jpg`.
- `entregas/justificativa-metricas.md`: variáveis, finalidade, público, decisões, fórmulas e limites dos quatro indicadores.
- `prompts/`: somente material relacionado ao uso de IA.
- `ROTEIRO.md` e `ALTAIR-CROSSFILTER.md`: guias atualizados da professora.
- `VALIDACAO.md`: verificações e situação de entrega.

## Testar

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Publicação

Repositório: https://github.com/joaopdornelas/PraticaAVD. O aluno autorizou o commit e o envio da parte 2 ao GitHub em 27/10/2026. O deploy no Streamlit Community Cloud é a etapa da Aula 23. O aluno ainda deve preencher seu nome e registrar sua revisão na declaração de IA.
