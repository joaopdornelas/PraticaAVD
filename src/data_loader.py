from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parents[1] / "data/clean/dataset.csv"
REQUIRED = {
    "title", "tipo_conteudo", "release_year", "imdb_rating", "imdb_votes",
    "tmdb_rating", "tmdb_popularity", "imdb_votes_log",
}


@st.cache_data(max_entries=2)
def load_data(path=DATA_PATH):
    """Lê somente o dataset tratado; caminho independente do diretório atual."""
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError("Dataset tratado ausente. Execute notebooks/eda.ipynb para gerar data/clean/dataset.csv.")
    df = pd.read_csv(path)
    faltantes = REQUIRED - set(df.columns)
    if faltantes:
        raise ValueError("Colunas obrigatórias ausentes: " + ", ".join(sorted(faltantes)))
    if df.empty:
        raise ValueError("O dataset tratado está vazio.")
    return df
