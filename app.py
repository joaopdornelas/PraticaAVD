"""Aulas 21 e 22: exploração e indicadores da base histórica Netflix."""
import matplotlib.pyplot as plt
import streamlit as st
from src.data_loader import load_data
from src.filters import filter_data
from src.analytics import LABELS, GROUPS, correlation_matrix, calculate_metrics, category_counts, select_categories, decade_counts
from src.charts import heatmap, histogram, category_bar, decade_bar

st.set_page_config(page_title="Netflix | Explorar o catálogo", layout="wide")
VARS_QUANT = list(LABELS)
st.title("Netflix: explorar o catálogo")
st.caption("Filmes e séries · Avaliações IMDb e TMDb · Base histórica com lançamentos até 2021")
try:
    df = load_data()
except (FileNotFoundError, ValueError) as error:
    st.error(str(error))
    st.stop()

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

df_filtrado = filter_data(df, tipos, filtro, intervalo, manter_ausentes)
st.caption(f"{len(df_filtrado):,} de {len(df):,} títulos após os filtros.".replace(",", "."))
if df_filtrado.empty:
    st.warning("Nenhum título corresponde aos filtros. Amplie o intervalo ou selecione um tipo de conteúdo.")

tab1, tab2 = st.tabs(["Correlação e distribuição", "Indicadores do catálogo"])

with tab1:
    col_correlacao, col_distribuicao = st.columns([1, 1.35])
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
    with col_distribuicao:
        st.subheader("Como os valores se distribuem?")
        if variaveis:
            distribuicao = st.selectbox("Variável da distribuição", variaveis,
                                       format_func=LABELS.get, key="distribuicao")
            bins = st.slider("Quantidade de intervalos do histograma", 5, 60, 25, key="hist_bins")
            log = st.checkbox("Visualizar em log(1 + valor)", key="hist_log") if distribuicao in ['imdb_votes', 'tmdb_popularity'] else False
            n = int(df_filtrado[distribuicao].notna().sum())
            if n == 0:
                st.info("Não há valores disponíveis para o histograma neste recorte.")
            else:
                fig = histogram(df_filtrado, distribuicao, bins, separar_por_tipo, log)
                st.pyplot(fig, width="stretch")
                plt.close(fig)
                st.caption(f"{n} títulos com valor disponível; {len(df_filtrado)-n} sem valor ficam fora deste gráfico.")
                if separar_por_tipo:
                    st.caption("Mesmos intervalos para os grupos. Cada grupo soma 100%, evitando confundir seu tamanho com o formato da distribuição.")
                if log:
                    st.caption("Somente a escala do histograma foi transformada. Os filtros, os dados e os indicadores continuam nas unidades originais.")
        else:
            st.warning("Selecione uma variável quantitativa para a distribuição.")

with tab2:
    st.subheader("Composição e avaliações do recorte")
    st.caption("Para explorar a composição desta base histórica e avaliar a cobertura das notas.")
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
                                    alt="Barras selecionáveis: clique para filtrar os indicadores e o gráfico por década")
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
        st.markdown("**Títulos por década de lançamento**")
        if selected.empty:
            st.info("Sem títulos para este recorte.")
        else:
            st.altair_chart(decade_bar(decade_counts(selected)), width="stretch",
                            alt="Quantidade de filmes e séries por década no recorte selecionado")
            st.caption("Década do lançamento dos títulos, não crescimento histórico do catálogo.")

with st.expander("Ver os dados dos filtros gerais"):
    colunas = ["title", "tipo_conteudo", *variaveis]
    previa = df_filtrado[colunas].head(100).rename(columns={"title": "Título", "tipo_conteudo": "Tipo de conteúdo", **LABELS})
    st.dataframe(previa, hide_index=True, width="stretch", alt="Prévia dos títulos após os filtros gerais")
    st.caption("Até 100 linhas. A seleção nas barras refina apenas a aba Indicadores do catálogo.")
