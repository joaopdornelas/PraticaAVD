# Justificativa das métricas — Dashboard 2

## Objetivo e público

Explorar a composição e a disponibilidade de avaliações na base histórica Netflix. Público: estudantes e analistas de curadoria de conteúdo. As decisões apoiadas são comparações exploratórias e priorização de investigação, não compras de direitos ou inferências sobre o catálogo atual.

Um registro corresponde a um título. O total original é de 7.786 títulos; existem 5.460 notas IMDb disponíveis e 2.410 séries. Os resultados a seguir são recalculados com os filtros gerais e a seleção de categorias nas barras. Sem seleção nas barras, todos os títulos dos filtros gerais participam.

## Métrica 1: Títulos no recorte

- **Variável:** `content_id`, uma linha por título.
- **O que mede:** número de registros após os filtros. Fórmula: `len(df_selecionado)`.
- **Por que foi escolhida:** torna explícito o tamanho do recorte que sustenta os demais indicadores.
- **Público-alvo:** estudantes e analistas de curadoria.
- **Qual decisão pode ser apoiada por essa métrica?** Ampliar um recorte pequeno antes de comparar distribuições ou avaliar sua representatividade.
- **O que comunica ao público-alvo:** quantos títulos estão efetivamente incluídos. Base completa: 7.786.

## Métrica 2: Com nota IMDb

- **Variável:** disponibilidade de `imdb_rating`.
- **O que mede:** proporção de títulos com nota. Numerador: notas não ausentes; denominador: todos os títulos do recorte. Fórmula: `imdb_rating.notna().sum() / len(df_selecionado)`.
- **Por que foi escolhida:** há muitas ausências e a cobertura difere entre filmes e séries; a mediana precisa desse contexto.
- **Público-alvo:** analistas que comparam avaliações entre categorias.
- **Qual decisão pode ser apoiada por essa métrica?** Investigar categorias com baixa cobertura e limitar generalizações baseadas apenas nos avaliados.
- **O que comunica ao público-alvo:** quanto do recorte tem informação para comparar notas. Base completa: 5.460 / 7.786 = aproximadamente 70,1%.

## Métrica 3: Nota IMDb mediana

- **Variável:** `imdb_rating`, escala de 0 a 10.
- **O que mede:** valor central das notas disponíveis no recorte. Fórmula: `imdb_rating.dropna().median()`.
- **Por que foi escolhida:** resume as avaliações sem inventar notas ausentes e é menos sensível a valores extremos que a média.
- **Público-alvo:** estudantes e analistas de curadoria interessados nas avaliações típicas.
- **Qual decisão pode ser apoiada por essa métrica?** Selecionar grupos para comparação mais detalhada, considerando simultaneamente cobertura e tamanho do recorte.
- **O que comunica ao público-alvo:** uma avaliação típica entre títulos com nota. Base completa: 6,5, usando 5.460 avaliações. Não é uma medida de qualidade objetiva ou causalidade.

## Métrica 4: Participação de séries

- **Variável:** `tipo_conteudo`.
- **O que mede:** parcela dos títulos classificados como Série. Numerador: quantidade de séries; denominador: total do recorte.
- **Por que foi escolhida:** a composição influencia comparações, porque filmes e séries têm distribuições e cobertura de notas distintas.
- **Público-alvo:** analistas que exploram a composição por gênero, país ou período de lançamento.
- **Qual decisão pode ser apoiada por essa métrica?** Separar filmes e séries antes de comparar avaliações de recortes com composição diferente.
- **O que comunica ao público-alvo:** equilíbrio entre os dois tipos de conteúdo. Base completa: 2.410 / 7.786 = aproximadamente 31,0%. Ao filtrar apenas séries, o indicador será 100% por definição.

## Widgets e interação planejados

1. Filtros gerais: tipos de conteúdo, variável de intervalo, slider e inclusão explícita de títulos sem valor na variável filtrada.
2. Agrupamento no Dashboard 2: gênero principal, país principal ou tipo de conteúdo.
3. Clique em uma barra: filtra os quatro cartões e o gráfico por década. Shift + clique permite selecionar várias categorias. Duplo clique ou o botão limpa a seleção.
4. As barras mantêm o contexto dos filtros gerais. Exibem até dez categorias mais frequentes; a quantidade representada é informada. Sem seleção, os cartões incluem todas as categorias, mesmo as que não estão nas dez barras.
5. Mudar os filtros gerais ou o agrupamento reinicia a seleção das barras para impedir seleções antigas em outro contexto.

## Visuais e identidade

Rascunho: `entregas/rascunho-dashboard2.jpg`, criado antes da implementação do Dashboard 2. Planejamento dos cálculos e visuais: `notebooks/metricas.ipynb`.

Barras por categoria permitem comparar frequências e selecionar recortes. As barras empilhadas por década descrevem a distribuição dos lançamentos por tipo. Décadas não representam crescimento do catálogo, pois não existem snapshots temporais sucessivos.

Vermelho `#B20710` como destaque ligado ao tema Netflix; azul `#2563EB` para distinguir séries; neutros `#202020`, `#FAFAFA` e cinza para texto, fundo e contexto. A matriz usa azul, branco e vermelho para a direção da correlação, com escala fixa de −1 a 1. Legendas e rótulos complementam as cores.

O Dashboard 1 reaproveita os gráficos Seaborn da EDA, exibidos com `st.pyplot` e recalculados pelos filtros. O Dashboard 2 usa Altair para a seleção nas barras, como orienta o roteiro.

## Ausências e limites

- Recorte vazio: contagem 0; proporções e mediana indisponíveis (—).
- Recorte com títulos, mas sem notas: cobertura 0%; mediana indisponível.
- Ausências não são substituídas por zero. Outliers são preservados conforme a EDA.
- País e gênero principais vêm do CSV; títulos não são duplicados para contabilizar múltiplos países/gêneros.
- A mediana depende da disponibilidade das notas e do processo de correspondência entre fontes.
- Não são usados deltas ou taxas de crescimento: não há comparação temporal equivalente definida.
