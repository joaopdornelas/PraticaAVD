# Netflix: explorar o catálogo

Aplicação das Aulas 21, 22 e 23 de Análise e Visualização de Dados (2026.2), desenvolvida a partir da EDA da base histórica Netflix. São dois dashboards: um laboratório de distribuição e correlação e um painel de indicadores com a proposta de atender analistas de curadoria de conteúdo. A definição individual do público e das justificativas ainda precisa ser registrada pelo aluno.

## Aplicativo publicado

**Publicação pendente.** O endereço público será incluído aqui após a publicação no Streamlit Community Cloud e a verificação do acesso em janela anônima.

[Repositório do projeto](https://github.com/joaopdornelas/PraticaAVD) · [Modelo da atividade](https://github.com/mfal-school/AVD-20262-pratica-streamlit)

## Os dois dashboards

### 1. Correlação e distribuição

Laboratório para investigar as relações e distribuições de ano de lançamento, nota IMDb, votos IMDb, nota TMDb e popularidade TMDb.

- Mapa de calor da correlação de Spearman, de −1 a 1, entre as variáveis selecionadas.
- **Um histograma para cada variável quantitativa selecionada**, organizado em duas colunas e recalculado pelos filtros.
- Controle da quantidade de intervalos dos histogramas.
- Comparação opcional entre filmes e séries, com os mesmos intervalos e percentuais calculados separadamente para cada grupo.
- Visualização em `log(1 + valor)` inicialmente ativada para votos IMDb e popularidade TMDb, com opção de desativar; as demais variáveis permanecem na escala original. Essa transformação é apenas visual e não modifica o dataset nem os indicadores.

Os gráficos usam Seaborn, seguindo a abordagem da EDA. Uma variável selecionada permite ver seu histograma; a correlação precisa de pelo menos duas. Células vazias da matriz indicam correlações indefinidas. Correlação não demonstra causalidade.

### 2. Indicadores do catálogo

**Público proposto com apoio de IA:** analistas de curadoria de conteúdo que exploram a composição e as avaliações da base histórica. Essa proposta e as justificativas dos indicadores ainda precisam da definição e redação individual exigidas pela professora. A implementação mantém quatro indicadores e não estima audiência, receita ou o catálogo atual da Netflix.

Quatro métricas próprias do recorte:

| Indicador | Interpretação |
|---|---|
| Títulos no recorte | Quantos títulos sustentam a comparação |
| Com nota IMDb | Proporção do recorte com avaliação disponível |
| Nota IMDb mediana | Valor central das notas disponíveis |
| Participação de séries | Proporção de títulos classificados como série |

Três visuais Altair, além das métricas:

1. **Títulos por categoria:** até dez categorias mais frequentes, agrupadas por gênero principal, país principal ou tipo. As barras permitem selecionar categorias.
2. **Cobertura IMDb por categoria:** proporção de títulos com nota IMDb em cada categoria. Exibe até dez categorias com mais títulos no recorte selecionado, usando o mesmo agrupamento do primeiro gráfico. A escala vai de 0% a 100%; o cursor informa títulos avaliados e total de títulos.
3. **Distribuição das notas IMDb por tipo:** boxplot de filmes e séries na escala de 0 a 10. A caixa vai do primeiro ao terceiro quartil (Q1 a Q3), a linha interna indica a mediana e os bigodes alcançam os valores observados até 1,5 vez o intervalo interquartil. Os pontos além dos bigodes continuam representados, sem serem excluídos da base.

O clique em uma barra de contagem atualiza os quatro indicadores, o gráfico de cobertura e o boxplot. `Shift` + clique seleciona várias categorias; duplo clique ou o botão limpa a seleção. As barras de categorias continuam mostrando o contexto dos filtros gerais. Sem seleção, entram todas as categorias do recorte, inclusive as que não estão entre as dez barras.

## Filtros e interpretação

O painel lateral contém seleção de tipos de conteúdo, seleção de variáveis quantitativas, escolha da variável do intervalo e um slider. A opção de manter títulos sem valor na variável filtrada torna explícito o tratamento das ausências.

Os filtros de títulos afetam as duas abas. A seleção de variáveis define os gráficos do Dashboard 1; a seleção nas barras refina apenas o Dashboard 2. Nenhuma interação altera o CSV.

- Ausências não são substituídas por zero; cada gráfico usa os valores disponíveis para a variável necessária.
- Em recorte vazio, a contagem é zero e as métricas sem denominador ou sem notas mostram `—`.
- Um grupo com títulos, mas sem avaliações, tem cobertura 0%; sua mediana e seu boxplot ficam indisponíveis, em vez de receber nota zero.
- A cobertura representa disponibilidade de notas, não avaliação positiva, qualidade do título ou sucesso comercial.
- Os bigodes do boxplot não são necessariamente o mínimo e o máximo: pontos externos são mostrados separadamente e mantidos nos cálculos.
- Os títulos vão até 2021. Esta base **não descreve o catálogo atual da Netflix**.
- As correspondências incorretas entre títulos e avaliações de fontes externas identificadas na revisão não foram corrigidas nesta mudança de gráficos. Elas podem afetar as comparações. O dataset permanece intacto; mudar o visual não valida essas correspondências.

## Executar no Windows

Use Python 3.12. Na pasta que contém `app.py`:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

Nas próximas execuções, basta o último comando. No macOS/Linux, use `python3` e `.venv/bin/python` no lugar dos caminhos Windows. O aplicativo carrega `data/clean/dataset.csv` por caminho relativo ao projeto e usa cache para evitar releituras desnecessárias.

## Notebooks e dados

- `notebooks/eda.ipynb`: cópia do Colab original do aluno, preservada conforme o roteiro. O carregamento original usa upload manual.
- `notebooks/eda-com-downloads.ipynb`: versão adaptada da EDA para execução local/Colab e exportação. Com o CSV original disponível, execute todas as células para gerar `data/raw/dataset.csv` e `data/clean/dataset.csv`.
- `notebooks/arquivo-eda-original.ipynb`: referência da professora.
- `notebooks/metricas.ipynb`: planejamento, cálculos das métricas com pandas e três visuais do Dashboard 2. As escolhas analíticas e suas justificativas ainda precisam da revisão individual.
- `data/raw/dataset.csv`: cópia local da base original, ignorada pelo Git como no modelo da atividade.
- `data/clean/dataset.csv`: base usada pelo aplicativo, versionada, com **7.786 linhas e 42 colunas**.

O tratamento preserva títulos, ausências e extremos. Acrescenta `tipo_conteudo` (Filme/Série) e `imdb_votes_log`. A base principal é `df`; `df_notas` é apenas o subconjunto com as duas notas disponíveis.

[Notebook original do aluno no Colab](https://colab.research.google.com/drive/1LBwfll2VYpDFk61nXW9KonxWqa0oK7wt). CSV fornecido: `netflix_content_intelligence_combined.csv`; proveniência em `data/proveniencia.json`. A fonte pública original e a licença do CSV ainda precisam ser documentadas.

## Entregáveis

- [`entregas/rascunho-dashboard1.png`](entregas/rascunho-dashboard1.png): layout do laboratório com todos os histogramas selecionados.
- [`entregas/rascunho-dashboard2.jpg`](entregas/rascunho-dashboard2.jpg): layout com quatro métricas e três visuais; a justificativa individual das escolhas permanece pendente.
- [`entregas/justificativa-metricas.md`](entregas/justificativa-metricas.md): rascunho anterior preservado, com a revisão individual das escolhas e justificativas pendente.
- [`prompts/declaracao-uso-ia.md`](prompts/declaracao-uso-ia.md): registro editável do apoio de IA, acompanhado do [rascunho em PDF](prompts/DECLARACAO_IA_RASCUNHO.pdf). A entrega oficial exige `prompts/DECLARACAO_IA.pdf`, preenchido e assinado pelo aluno conforme o template da professora, incluindo a reflexão individual. O rascunho não substitui essa versão final.
- `ROTEIRO.md` e `ALTAIR-CROSSFILTER.md`: orientações da professora.

Os rascunhos refletem a revisão gráfica aprovada na conversa: os visuais por década e de mediana por tipo foram substituídos por cobertura IMDb por categoria e boxplot das notas por tipo. O painel mantém quatro indicadores e três visuais. A aprovação da alteração técnica não substitui a redação individual das justificativas e a definição do público exigidas pela atividade. Os gráficos ilustrativos dos desenhos não são resultados da base.

## Testar

```powershell
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Conferência de referência sem filtros adicionais: **7.786 títulos**, **70,1% com nota IMDb**, **mediana 6,5** e **31,0% de séries**. Testar também seleção vazia, uma ou várias variáveis, apenas filmes/séries, intervalo restrito, ausência de notas e seleção/limpeza nas barras.

## Publicação e conferência final

No Streamlit Community Cloud, selecionar o repositório `joaopdornelas/PraticaAVD`, branch `main`, arquivo `app.py` e Python 3.12. Os arquivos devem estar enviados ao GitHub antes da publicação. A aplicação desta atividade deve ser pública; não precisa de login próprio.

Após publicar, conferir:

- [ ] Aplicativo acessível em janela anônima.
- [ ] Todos os widgets respondem e atualizam os resultados.
- [ ] As duas abas carregam.
- [ ] Dashboard 1 mostra um histograma por variável selecionada.
- [ ] Dashboard 2 mostra quatro métricas e três visuais, com seleção das barras funcionando.
- [ ] Repositório e aplicativo não expõem senhas, tokens ou outros dados sensíveis.
- [ ] Link público real incluído no início deste README.
- [ ] Repositório público com notebooks, `app.py`, `entregas/` e `prompts/` completos.
- [ ] Público, métricas, justificativas e terceiro visual definidos pelo aluno.
- [ ] Declaração oficial em PDF preenchida e assinada, com reflexão individual de 10 a 15 linhas e identificação dos blocos de código assistidos por IA.

Os itens de publicação permanecem pendentes até a conferência no endereço público.
