"""Cálculos compartilhados entre os dashboards e o notebook de métricas."""
import numpy as np
import pandas as pd

LABELS = {
    'release_year': 'Ano de lançamento', 'imdb_rating': 'Nota IMDb',
    'imdb_votes': 'Votos IMDb', 'tmdb_rating': 'Nota TMDb',
    'tmdb_popularity': 'Popularidade TMDb',
}
GROUPS = {'primary_genre': 'Gênero principal', 'primary_country': 'País principal', 'tipo_conteudo': 'Tipo de conteúdo'}
COLORS = {'Filme': '#B20710', 'Série': '#2563EB', 'Todos': '#B20710'}


def correlation_data(df, variables):
    matrix = df[variables].corr(method='spearman', min_periods=2)
    valid = df[variables].notna().astype(int)
    counts = valid.T.dot(valid)
    return pd.DataFrame([
        {'x': LABELS[x], 'y': LABELS[y], 'rho': matrix.loc[y, x],
         'n': int(counts.loc[y, x]),
         'texto': f'{matrix.loc[y, x]:.2f}' if pd.notna(matrix.loc[y, x]) else '—'}
        for y in variables for x in variables
    ])


def histogram_data(df, variable, bins=25, split=False, log=False):
    available = df.dropna(subset=[variable]).copy()
    if available.empty:
        return pd.DataFrame(columns=['inicio', 'fim', 'quantidade', 'percentual', 'grupo', 'n_grupo'])
    values = np.log1p(available[variable]) if log else available[variable]
    edges = np.histogram_bin_edges(values, bins=bins)
    groups = available.groupby('tipo_conteudo', observed=True) if split else [('Todos', available)]
    rows = []
    for name, part in groups:
        observations = np.log1p(part[variable]) if log else part[variable]
        counts, _ = np.histogram(observations, bins=edges)
        for left, right, count in zip(edges[:-1], edges[1:], counts):
            rows.append({'inicio': float(left), 'fim': float(right), 'quantidade': int(count),
                         'percentual': float(count / len(part) * 100), 'grupo': name,
                         'n_grupo': len(part)})
    return pd.DataFrame(rows)


def calculate_metrics(df):
    total = len(df)
    notes = df['imdb_rating'].dropna()
    return {
        'total': total, 'avaliados': len(notes),
        'cobertura': len(notes)/total if total else None,
        'mediana': float(notes.median()) if len(notes) else None,
        'series': int(df['tipo_conteudo'].eq('Série').sum()),
        'proporcao_series': float(df['tipo_conteudo'].eq('Série').mean()) if total else None,
    }


def category_counts(df, group, limit=10):
    values = df[group].fillna('Não informado')
    return (values.value_counts().rename_axis('categoria').reset_index(name='titulos')
            .sort_values(['titulos', 'categoria'], ascending=[False, True]).head(limit).reset_index(drop=True))


def select_categories(df, group, selections):
    categories = [item['categoria'] for item in selections if 'categoria' in item]
    return df.loc[df[group].fillna('Não informado').isin(categories)].copy() if categories else df.copy()


def decade_counts(df):
    data = df.dropna(subset=['release_year']).copy()
    data['decada'] = (data['release_year'] // 10 * 10).astype(int).astype(str)
    return data.groupby(['decada', 'tipo_conteudo'], observed=True).size().reset_index(name='titulos')
