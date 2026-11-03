"""Cálculos compartilhados entre os dashboards e o notebook de métricas."""
import pandas as pd

# [IA] ChatGPT/Codex - nomes exibidos nos filtros e cores por tipo de conteúdo.
LABELS = {
    'release_year': 'Ano de lançamento', 'imdb_rating': 'Nota IMDb',
    'imdb_votes': 'Votos IMDb', 'tmdb_rating': 'Nota TMDb',
    'tmdb_popularity': 'Popularidade TMDb',
}
GROUPS = {'primary_genre': 'Gênero principal', 'primary_country': 'País principal', 'tipo_conteudo': 'Tipo de conteúdo'}
COLORS = {'Filme': '#B20710', 'Série': '#2563EB', 'Todos': '#B20710'}


# [IA] ChatGPT/Codex - cálculo da correlação usada na EDA.
def correlation_matrix(df, variables):
    """Repete a correlação de Spearman usada na EDA original."""
    return df[variables].corr(method='spearman', min_periods=2)


# [IA] ChatGPT/Codex - cálculo dos indicadores e tratamento de recortes vazios.
def calculate_metrics(df):
    total = len(df)
    notes = df['imdb_rating'].dropna()
    series = int((df['tipo_conteudo'] == 'Série').sum())
    return {
        'total': total, 'avaliados': len(notes),
        'cobertura': len(notes)/total if total else None,
        'mediana': float(notes.median()) if len(notes) else None,
        'series': series,
        'proporcao_series': series / total if total else None,
    }


# [IA] ChatGPT/Codex - contagem de títulos por categoria.
def category_counts(df, group, limit=10):
    values = df[group].fillna('Não informado')
    return (values.value_counts().rename_axis('categoria').reset_index(name='titulos')
            .sort_values(['titulos', 'categoria'], ascending=[False, True]).head(limit).reset_index(drop=True))


# [IA] ChatGPT/Codex - filtro a partir das barras selecionadas.
def select_categories(df, group, selections):
    categories = [item['categoria'] for item in selections if 'categoria' in item]
    return df.loc[df[group].fillna('Não informado').isin(categories)].copy() if categories else df.copy()


# [IA] ChatGPT/Codex - cobertura das notas por categoria, incluindo títulos sem nota no total.
def category_coverage(df, group, limit=10):
    data = df[[group, 'imdb_rating']].copy()
    data[group] = data[group].fillna('Não informado')
    summary = (data.groupby(group, observed=True)['imdb_rating']
               .agg(total='size', avaliados='count').reset_index()
               .rename(columns={group: 'categoria'}))
    summary['cobertura'] = summary['avaliados'] / summary['total']
    return (summary.sort_values(['total', 'categoria'], ascending=[False, True])
            .head(limit).reset_index(drop=True))


# [IA] ChatGPT/Codex - resumo das notas disponíveis, sem substituir ausências por zero.
def rating_summary(df):
    data = (df.groupby('tipo_conteudo', observed=True)['imdb_rating']
            .agg(total='size', avaliados='count', mediana='median').reset_index())
    data['cobertura'] = data['avaliados'] / data['total']
    return data
