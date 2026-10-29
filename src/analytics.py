"""Cálculos compartilhados entre os dashboards e o notebook de métricas."""
import pandas as pd

LABELS = {
    'release_year': 'Ano de lançamento', 'imdb_rating': 'Nota IMDb',
    'imdb_votes': 'Votos IMDb', 'tmdb_rating': 'Nota TMDb',
    'tmdb_popularity': 'Popularidade TMDb',
}
GROUPS = {'primary_genre': 'Gênero principal', 'primary_country': 'País principal', 'tipo_conteudo': 'Tipo de conteúdo'}
COLORS = {'Filme': '#B20710', 'Série': '#2563EB', 'Todos': '#B20710'}


def correlation_matrix(df, variables):
    """Repete a correlação de Spearman usada na EDA original."""
    return df[variables].corr(method='spearman', min_periods=2)


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
