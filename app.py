"""Aulas 21 a 23: exploração e indicadores da base histórica Netflix."""
# [IA] ChatGPT/Codex - imports e configuração inicial do aplicativo.
import matplotlib.pyplot as plt
import streamlit as st
from src.data_loader import load_data
from src.filters import filter_data
from src.analytics import LABELS, GROUPS, correlation_matrix, calculate_metrics, category_counts, select_categories, category_coverage, rating_summary
from src.charts import heatmap, histogram, category_bar, coverage_bar, rating_boxplot

st.set_page_config(page_title="Netflix | Explorar o catálogo", layout="wide")
VARS_QUANT = list(LABELS)
st.title("Netflix: explorar o catálogo")
st.caption("Filmes e séries · Avaliações IMDb e TMDb · Base histórica com lançamentos até 2021")
try:
    df = load_data()
except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.stop()

# [IA] ChatGPT/Codex - widgets dos filtros gerais e tratamento de valores ausentes.
with st.sidebar:
    st.header("Filtros")
    tipos = st.multiselect("Tipo de conteúdo", ["Filme", "Série"], default=["Filme", "Série"], key="tipos")
    variaveis = st.multiselect(
        "Variáveis quantitativas", VARS_QUANT, default=VARS_QUANT,
        format_func=LABELS.get, key="variaveis",
        help="Escolha as variáveis do Dashboard 1. Os filtros gerais também afetam os indicadores.",
    )
    filtro = st.selectbox(
        "Variável para filtrar por intervalo", VARS_QUANT,
        format_func=LABELS.get, key="filtro",
        help="O intervalo filtra títulos; a seleção acima escolhe as variáveis de análise.",
    )
    valores = df[filtro].dropna()
    if valores.empty:
        intervalo = None
        st.info("Esta variável não tem valores disponíveis.")
    else:
        inteiro = filtro in ("release_year", "imdb_votes")
        converter = int if inteiro else float
        minimo, maximo = converter(valores.min()), converter(valores.max())
        if minimo == maximo:
            intervalo = (minimo, maximo)
            st.caption(f"Valor único: {minimo}")
        else:
            intervalo = st.slider(
                LABELS[filtro], minimo, maximo, (minimo, maximo),
                step=1 if inteiro else 0.01, key=f"intervalo_{filtro}",
            )
    manter_ausentes = st.checkbox(
        "Manter títulos sem valor nessa variável", value=True, key="manter_ausentes",
        help="Preserva títulos sem informação na variável do intervalo. Eles não participam de cálculos que exijam esse valor.",
    )
    separar_por_tipo = st.toggle("Distinguir filmes e séries", key="separar_por_tipo")
    st.caption("Os filtros alteram apenas a visualização; o dataset permanece intacto.")

# [IA] ChatGPT/Codex - aplicação dos filtros e organização das duas abas.
df_filtrado = filter_data(df, tipos, filtro, intervalo, manter_ausentes)
st.caption(f"{len(df_filtrado):,} de {len(df):,} títulos após os filtros.".replace(",", "."))
if df_filtrado.empty:
    st.warning("Nenhum título corresponde aos filtros. Amplie o intervalo ou selecione um tipo de conteúdo.")

tab1, tab2 = st.tabs(["Correlação e distribuição", "Indicadores do catálogo"])

# [IA] ChatGPT/Codex - mapa de correlação e um histograma por variável selecionada.
with tab1:
    col_correlacao, col_leitura = st.columns([1.2, 1])
    with col_correlacao:
        st.subheader("Como as variáveis se relacionam?")
        if len(variaveis) < 2:
            st.warning("Selecione pelo menos duas variáveis para a correlação.")
        elif df_filtrado.empty:
            st.info("Sem títulos para calcular a correlação.")
        else:
            correlations = correlation_matrix(df_filtrado, variaveis)
            if correlations.isna().all().all():
                st.info("Não há dados com variação suficiente para calcular a correlação.")
            else:
                fig = heatmap(correlations)
                st.pyplot(fig, width="stretch")
                plt.close(fig)
            st.caption("Spearman, de −1 a 1. Células vazias indicam menos de dois pares válidos ou variável constante.")
            st.caption("Associação não demonstra causalidade. Cada par pode usar um conjunto diferente de títulos.")
    with col_leitura:
        st.subheader("Controles dos histogramas")
        st.write("Cada variável selecionada na lateral aparece em seu próprio histograma abaixo.")
        bins = st.slider("Quantidade de intervalos dos histogramas", 5, 60, 25, key="hist_bins")
        log = st.checkbox("Usar log(1 + valor) em votos e popularidade", value=True, key="hist_log")
        if log:
            st.caption("A transformação afeta somente os histogramas de votos IMDb e popularidade TMDb. Filtros, correlação e indicadores usam os valores originais.")
        if separar_por_tipo:
            st.caption("Filmes e séries usam os mesmos intervalos. Cada grupo soma 100%, permitindo comparar suas distribuições.")
        else:
            st.caption("O eixo vertical informa a quantidade de títulos em cada intervalo.")

    st.subheader("Como os valores se distribuem?")
    if not variaveis:
        st.warning("Selecione uma variável quantitativa para a distribuição.")
    for inicio in range(0, len(variaveis), 2):
        colunas_hist = st.columns(2)
        for coluna, variavel in zip(colunas_hist, variaveis[inicio:inicio + 2]):
            with coluna:
                st.markdown(f"**{LABELS[variavel]}**")
                n = int(df_filtrado[variavel].notna().sum())
                if n == 0:
                    st.info("Não há valores disponíveis para este histograma no recorte.")
                else:
                    usar_log = log and variavel in ("imdb_votes", "tmdb_popularity")
                    fig = histogram(df_filtrado, variavel, bins, separar_por_tipo, usar_log)
                    st.pyplot(fig, width="stretch")
                    plt.close(fig)
                st.caption(f"{n} títulos com valor disponível; {len(df_filtrado) - n} sem valor ficam fora deste gráfico.")

# [IA] ChatGPT/Codex - cartões, gráficos Altair e seleção compartilhada de categorias.
with tab2:
    st.subheader("Composição e avaliações do recorte")
    st.caption("Para analistas de curadoria explorarem a composição da base histórica e a cobertura das avaliações.")
    slots = st.container()
    controls, clear = st.columns([3, 1], vertical_alignment="bottom")
    with controls:
        group = st.selectbox("Agrupar títulos por", list(GROUPS), format_func=GROUPS.get, key="kpi_group")
    with clear:
        if st.button("Limpar seleção das barras", key="clear_categories"):
            st.session_state['selection_version'] = st.session_state.get('selection_version', 0) + 1
    bar_col, detail_col = st.columns([1.3, 1])
    selections = []
    with bar_col:
        st.markdown("**Títulos por categoria**")
        if df_filtrado.empty:
            st.info("Sem títulos para agrupar.")
        else:
            grouped = category_counts(df_filtrado, group)
            # Uma mudança nos filtros cria uma nova seleção, sem carregar cliques antigos.
            chart_key = f"categories_{group}_{tipos}_{filtro}_{intervalo}_{manter_ausentes}_{st.session_state.get('selection_version', 0)}"
            event = st.altair_chart(category_bar(grouped), key=chart_key, on_select="rerun",
                                    selection_mode=['categorias'], width="stretch",
                                    alt="Barras selecionáveis: clique para filtrar os indicadores, a cobertura por categoria e o boxplot de notas")
            selections = event.selection.get('categorias', [])
            st.caption(f"Até 10 maiores categorias: {int(grouped.titulos.sum())} de {len(df_filtrado)} títulos dos filtros gerais. As barras permanecem como contexto durante a seleção.")
            st.caption("Clique para selecionar; Shift + clique para várias categorias; duplo clique ou botão para limpar.")
    selected = select_categories(df_filtrado, group, selections)
    metrics = calculate_metrics(selected)
    with slots:
        cols = st.columns(4)
        cols[0].metric("Títulos no recorte", f"{metrics['total']:,}".replace(',', '.'), border=True)
        cols[1].metric("Com nota IMDb", '—' if metrics['cobertura'] is None else f"{metrics['cobertura']:.1%}".replace('.', ','), border=True,
                       help="Títulos com nota IMDb divididos pelo total do recorte, incluindo os sem nota no denominador.")
        cols[2].metric("Nota IMDb mediana", '—' if metrics['mediana'] is None else f"{metrics['mediana']:.1f}".replace('.', ','), border=True,
                       help="Mediana das notas disponíveis, na escala de 0 a 10. Valores ausentes não recebem zero.")
        cols[3].metric("Participação de séries", '—' if metrics['proporcao_series'] is None else f"{metrics['proporcao_series']:.1%}".replace('.', ','), border=True,
                       help="Quantidade de séries dividida pelo total de títulos do recorte.")
        if selections:
            st.caption("Categorias selecionadas: " + ', '.join(item['categoria'] for item in selections))
        else:
            st.caption("Sem seleção nas barras: indicadores referentes a todos os títulos dos filtros gerais.")
        st.caption(f"A mediana utiliza {metrics['avaliados']} avaliações disponíveis. A cobertura desigual entre grupos limita a comparação.")
    with detail_col:
        st.markdown("**Cobertura IMDb por categoria**")
        if selected.empty:
            st.info("Sem títulos para este recorte.")
        else:
            coverage = category_coverage(selected, group)
            st.altair_chart(coverage_bar(coverage), width="stretch",
                            alt="Percentual de títulos com nota IMDb em cada categoria do recorte selecionado")
            st.caption("Até 10 categorias com mais títulos no recorte. Cobertura = títulos com nota / total da categoria. Passe o cursor para ver as quantidades.")
            st.caption("Cobertura mede a disponibilidade da nota. As associações entre títulos e avaliações da base ainda precisam de revisão.")

    st.markdown("**Distribuição das notas IMDb por tipo de conteúdo**")
    notas_por_tipo = rating_summary(selected)
    if notas_por_tipo.empty or notas_por_tipo['mediana'].isna().all():
        st.info("Sem notas IMDb disponíveis para comparar neste recorte.")
    else:
        st.altair_chart(rating_boxplot(selected), width="stretch",
                        alt="Boxplot das notas IMDb de filmes e séries, com mediana, quartis e valores extremos, na escala de zero a dez")
        sem_notas = notas_por_tipo.loc[notas_por_tipo['avaliados'] == 0, 'tipo_conteudo'].tolist()
        if sem_notas:
            st.caption("Sem notas disponíveis: " + ', '.join(sem_notas) + ". Esses grupos não recebem nota zero.")
        st.caption("A caixa contém os 50% centrais das notas; a linha interna marca a mediana. As hastes vão até os valores dentro de 1,5 vezes a distância entre os quartis. Pontos além das hastes continuam incluídos nos cálculos.")
        for row in notas_por_tipo.itertuples(index=False):
            percentual = f"{row.cobertura:.1%}".replace('.', ',')
            st.caption(f"{row.tipo_conteudo}: {row.avaliados} de {row.total} títulos com nota IMDb ({percentual}).")

# [IA] ChatGPT/Codex - prévia dos dados sem modificar o dataset.
with st.expander("Ver os dados dos filtros gerais"):
    colunas = ["title", "tipo_conteudo", *variaveis]
    previa = df_filtrado[colunas].head(100).rename(columns={"title": "Título", "tipo_conteudo": "Tipo de conteúdo", **LABELS})
    st.dataframe(previa, hide_index=True, width="stretch", alt="Prévia dos títulos após os filtros gerais")
    st.caption("Até 100 linhas. A seleção nas barras refina apenas a aba Indicadores do catálogo.")
