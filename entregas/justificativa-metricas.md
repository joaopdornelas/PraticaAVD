# Justificativa das métricas — Dashboard 2

Texto elaborado com apoio de IA. João Pedro Rodrigues confirmou que o público e as justificativas abaixo representam suas escolhas. O histórico desse apoio permanece em `prompts/declaracao-uso-ia.md`.

## Público-alvo

Analistas de conteúdo interessados em conhecer a composição do catálogo e comparar as avaliações dos títulos.

## Métricas

### Total de títulos

- **Variável e cálculo:** registros identificados por `content_id`; quantidade de linhas após os filtros.
- **Justificativa:** mostra o tamanho do grupo analisado após aplicar os filtros.
- **Decisão apoiada:** avaliar quantos títulos sustentam uma comparação.

### Percentual com nota IMDb

- **Variável e cálculo:** `imdb_rating`; títulos com nota divididos pelo total do grupo, multiplicado por 100.
- **Justificativa:** mostra quantos títulos possuem avaliação disponível, ajudando a reconhecer informações ausentes.
- **Decisão apoiada:** identificar grupos que precisam de mais informações antes de comparar avaliações.

### Nota IMDb mediana

- **Variável e cálculo:** mediana dos valores disponíveis de `imdb_rating`.
- **Justificativa:** resume as notas disponíveis e sofre menos influência de valores extremos que a média.
- **Decisão apoiada:** comparar a avaliação central dos grupos, considerando também o tamanho e a cobertura das notas.

### Participação de séries

- **Variável e cálculo:** `tipo_conteudo`; quantidade de séries dividida pelo total do grupo, multiplicado por 100.
- **Justificativa:** mostra quanto do grupo analisado corresponde a séries.
- **Decisão apoiada:** considerar a composição entre filmes e séries ao comparar grupos.

## Gráficos

- **Títulos por categoria:** permite identificar as categorias mais presentes no recorte.
- **Cobertura IMDb por categoria:** permite comparar quais categorias têm maior ou menor disponibilidade de avaliações.
- **Boxplot das notas:** permite comparar a distribuição das avaliações de filmes e séries, mostrando a mediana, a dispersão e os valores extremos.

## Filtros e interação

Os filtros laterais selecionam o tipo de conteúdo e o intervalo de valores. No Dashboard 2, é possível agrupar por gênero principal, país principal ou tipo de conteúdo.

Clicar nas barras de títulos por categoria atualiza as quatro métricas, a cobertura e o boxplot. As barras de contagem mantêm o contexto dos filtros gerais. Shift + clique seleciona várias categorias; duplo clique ou o botão limpa a seleção. As barras exibem até dez categorias, mas, sem seleção, as métricas consideram todo o recorte.

## Cuidados na análise

- A base é histórica, com títulos até 2021; não representa o catálogo atual da Netflix.
- Notas ausentes não recebem zero. A cobertura mede disponibilidade de avaliações.
- Sem títulos, a contagem é zero e as demais métricas ficam indisponíveis. Com títulos, mas sem notas, a cobertura é 0% e não há mediana ou boxplot.
- Os valores extremos permanecem na análise. No boxplot, a caixa representa os 50% centrais e os pontos além dos bigodes também são exibidos.
- Há associações incorretas entre alguns títulos e avaliações, ainda pendentes de correção, que podem afetar as comparações.
- Os indicadores não medem audiência, receita ou sucesso comercial.

## Arquivos relacionados

- Layout: `entregas/rascunho-dashboard2.jpg`.
- Cálculos e gráficos: `notebooks/metricas.ipynb`.
