import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from src.analytics import COLORS, LABELS


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


def category_bar(data):
    selection = alt.selection_point(name='categorias', fields=['categoria'], clear='dblclick')
    return alt.Chart(data).mark_bar(color='#B20710').encode(
        x=alt.X('titulos:Q', title='Títulos'),
        y=alt.Y('categoria:N', title=None, sort='-x', axis=alt.Axis(labelLimit=230)),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.25)),
        tooltip=[alt.Tooltip('categoria:N', title='Categoria'), alt.Tooltip('titulos:Q', title='Títulos')],
    ).add_params(selection).properties(height=350).configure_view(stroke=None)


def decade_bar(data):
    return alt.Chart(data).mark_bar().encode(
        x=alt.X('decada:O', title='Década de lançamento', axis=alt.Axis(labelAngle=-35)),
        y=alt.Y('titulos:Q', title='Títulos'),
        color=alt.Color('tipo_conteudo:N', title='Tipo', scale=alt.Scale(domain=['Filme', 'Série'], range=[COLORS['Filme'], COLORS['Série']])),
        tooltip=[alt.Tooltip('decada:O', title='Década'), alt.Tooltip('tipo_conteudo:N', title='Tipo'), alt.Tooltip('titulos:Q', title='Títulos')],
    ).properties(height=350).configure_view(stroke=None)
