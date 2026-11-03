# [IA] ChatGPT/Codex - imports para desenhar os gráficos.
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from src.analytics import COLORS, LABELS


# [IA] ChatGPT/Codex - sintaxe e formatação do mapa de calor Seaborn.
def heatmap(matrix):
    """Mesmo tipo de heatmap do notebook da EDA."""
    fig, ax = plt.subplots(figsize=(6, 5))
    labels = [LABELS[column] for column in matrix.columns]
    sns.heatmap(matrix, annot=True, fmt='.2f', cmap='coolwarm',
                vmin=-1, vmax=1, center=0, mask=matrix.isna(),
                xticklabels=labels, yticklabels=labels, ax=ax)
    ax.tick_params(axis='x', rotation=45)
    ax.tick_params(axis='y', rotation=0)
    fig.tight_layout()
    return fig


# [IA] ChatGPT/Codex - histogramas, intervalos comuns e transformação opcional de escala.
def histogram(df, variable, bins=25, split=False, log=False):
    """Seaborn calcula os intervalos e as frequências, como na EDA."""
    data = df[[variable, 'tipo_conteudo']].dropna(subset=[variable]).copy()
    if log:
        data[variable] = np.log1p(data[variable])
    fig, ax = plt.subplots(figsize=(7, 5))
    if split:
        sns.histplot(data=data, x=variable, hue='tipo_conteudo', bins=bins,
                     stat='percent', common_norm=False, common_bins=True,
                     multiple='layer', palette=COLORS, alpha=0.5, ax=ax)
        ax.get_legend().set_title('Tipo de conteúdo')
    else:
        sns.histplot(data=data, x=variable, bins=bins, color=COLORS['Filme'], ax=ax)
    ax.set_xlabel(f'log(1 + {LABELS[variable]})' if log else LABELS[variable])
    ax.set_ylabel('Títulos com valor no grupo (%)' if split else 'Títulos')
    fig.tight_layout()
    return fig


# [IA] ChatGPT/Codex - sintaxe Altair para barras com seleção de categorias.
def category_bar(data):
    selection = alt.selection_point(name='categorias', fields=['categoria'], clear='dblclick')
    return alt.Chart(data).mark_bar(color='#B20710').encode(
        x=alt.X('titulos:Q', title='Títulos'),
        y=alt.Y('categoria:N', title=None, sort='-x', axis=alt.Axis(labelLimit=230)),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.25)),
        tooltip=[alt.Tooltip('categoria:N', title='Categoria'), alt.Tooltip('titulos:Q', title='Títulos')],
    ).add_params(selection).properties(height=350).configure_view(stroke=None)


# [IA] ChatGPT/Codex - barras de cobertura, com percentual e denominadores disponíveis.
def coverage_bar(data):
    base = alt.Chart(data).encode(
        x=alt.X('cobertura:Q', title='Títulos com nota IMDb (%)',
                scale=alt.Scale(domain=[0, 1]), axis=alt.Axis(format='.0%')),
        y=alt.Y('categoria:N', title=None, sort=data['categoria'].tolist(),
                axis=alt.Axis(labelLimit=230)),
        tooltip=[alt.Tooltip('categoria:N', title='Categoria'),
                 alt.Tooltip('avaliados:Q', title='Com nota IMDb'),
                 alt.Tooltip('total:Q', title='Total de títulos'),
                 alt.Tooltip('cobertura:Q', title='Cobertura', format='.1%')],
    )
    bars = base.mark_bar(color=COLORS['Série'])
    labels = base.mark_text(align='left', dx=4).encode(
        text=alt.Text('cobertura:Q', format='.1%'))
    return (bars + labels).properties(height=350).configure_view(stroke=None)


# [IA] ChatGPT/Codex - boxplot com todas as notas disponíveis, sem amostragem ou remoção de extremos.
def rating_boxplot(df):
    data = df[['tipo_conteudo', 'imdb_rating']].dropna(subset=['imdb_rating'])
    # Envia somente duas colunas. Dados explícitos preservam as 5.460 notas da base,
    # inclusive no notebook, cujo limite padrão para DataFrames é de 5.000 linhas.
    source = alt.Data(values=data.to_dict('records'))
    return alt.Chart(source).mark_boxplot(extent=1.5, size=70).encode(
        x=alt.X('tipo_conteudo:N', title='Tipo de conteúdo', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('imdb_rating:Q', title='Nota IMDb', scale=alt.Scale(domain=[0, 10])),
        color=alt.Color('tipo_conteudo:N', title='Tipo', scale=alt.Scale(
            domain=['Filme', 'Série'], range=[COLORS['Filme'], COLORS['Série']])),
    ).properties(height=350).configure_view(stroke=None)
