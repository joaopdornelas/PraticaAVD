"""Aula 21: estrutura e filtros do Dashboard 1 da Netflix."""
import streamlit as st
from src.data_loader import load_data
from src.filters import filter_data

st.set_page_config(page_title="Netflix | Explorar o catálogo", layout="wide")
LABELS = {
    "release_year": "Ano de lançamento",
    "imdb_rating": "Nota IMDb",
    "imdb_votes": "Quantidade de votos IMDb",
    "tmdb_rating": "Nota TMDb",
    "tmdb_popularity": "Popularidade TMDb",
}
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
        help="Escolha as variáveis que serão usadas na correlação e na distribuição.",
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

col_correlacao, col_distribuicao = st.columns([1, 1.5])
with col_correlacao:
    with st.container(border=True):
        st.subheader("Correlação")
        if len(variaveis) < 2:
            st.warning("Selecione pelo menos duas variáveis para a correlação.")
        else:
            st.info("Área reservada para a matriz de correlação de Spearman.")
            st.caption("Cada par utilizará os títulos com os dois valores disponíveis.")
        # TODO Aula 22: df_filtrado[variaveis].corr(method="spearman").
        # TODO Aula 22: heatmap com escala fixa de -1 a 1 e quantidade por par.

with col_distribuicao:
    with st.container(border=True):
        st.subheader("Distribuição")
        if variaveis:
            distribuicao = st.selectbox(
                "Variável da distribuição", variaveis, format_func=LABELS.get,
                key="distribuicao",
            )
            n = df_filtrado[distribuicao].notna().sum()
            st.info("Área reservada para o histograma.")
            st.caption(f"{n} títulos com valor disponível para esta variável.")
            if separar_por_tipo:
                st.caption("Comparação planejada: filmes e séries em cores distintas e percentuais por grupo.")
            # TODO Aula 22: histograma usando distribuicao e df_filtrado.
            # Usar intervalos iguais por grupo, ausências excluídas só deste gráfico.
        else:
            st.warning("Selecione uma variável quantitativa para a distribuição.")

with st.expander("Ver os dados filtrados"):
    colunas = ["title", "tipo_conteudo", *variaveis]
    previa = df_filtrado[colunas].head(100).rename(
        columns={"title": "Título", "tipo_conteudo": "Tipo de conteúdo", **LABELS}
    )
    st.dataframe(previa, hide_index=True, width="stretch", alt="Prévia dos títulos da Netflix após os filtros")
    st.caption("Prévia de até 100 títulos. Os filtros consideram a base completa.")
st.caption("Aula 21: layout e filtros. Os gráficos e o Dashboard 2 de indicadores serão desenvolvidos na próxima etapa.")
