import altair as alt
from src.analytics import COLORS, LABELS


def heatmap(data, variables):
    order = [LABELS[v] for v in variables]
    base = alt.Chart(data).encode(
        x=alt.X('x:N', sort=order, title=None, axis=alt.Axis(labelAngle=-35, labelLimit=150)),
        y=alt.Y('y:N', sort=order, title=None, axis=alt.Axis(labelLimit=150)),
        tooltip=[alt.Tooltip('x:N', title='Variável'), alt.Tooltip('y:N', title='Variável'),
                 alt.Tooltip('rho:Q', title='Spearman', format='.3f'), alt.Tooltip('n:Q', title='Pares válidos')],
    )
    background = base.mark_rect(color='#E5E7EB')
    cells = base.transform_filter('isValid(datum.rho)').mark_rect().encode(
        color=alt.Color('rho:Q', title='Spearman', scale=alt.Scale(domain=[-1, 0, 1], range=['#2563EB', '#FFFFFF', '#B20710']))
    )
    text = base.mark_text(fontSize=14).encode(
        text='texto:N', color=alt.when('isValid(datum.rho) && abs(datum.rho) > 0.55').then(alt.value('white')).otherwise(alt.value('#202020')),
    )
    return (background + cells + text).properties(height=340).configure_view(stroke=None)


def histogram(data, variable, split=False, log=False):
    title = f'log(1 + {LABELS[variable]})' if log else LABELS[variable]
    y = alt.Y('percentual:Q', title='Títulos com valor no grupo (%)', stack=None) if split else alt.Y('quantidade:Q', title='Títulos', stack=None)
    return alt.Chart(data).mark_bar(opacity=0.6 if split else 0.95).encode(
        x=alt.X('inicio:Q', title=title, bin='binned'), x2='fim:Q', y=y,
        color=alt.Color('grupo:N', title='Tipo', scale=alt.Scale(domain=list(COLORS), range=list(COLORS.values())), legend=alt.Legend() if split else None),
        tooltip=[alt.Tooltip('grupo:N', title='Grupo'), alt.Tooltip('inicio:Q', title='Início', format='.2f'),
                 alt.Tooltip('fim:Q', title='Fim', format='.2f'), alt.Tooltip('quantidade:Q', title='Títulos no intervalo'),
                 alt.Tooltip('percentual:Q', title='% do grupo', format='.2f'), alt.Tooltip('n_grupo:Q', title='N do grupo')],
    ).properties(height=340).configure_view(stroke=None)


def category_bar(data):
    selection = alt.selection_point(name='categorias', fields=['categoria'], clear='dblclick')
    return alt.Chart(data).mark_bar(color='#B20710').encode(
        x=alt.X('titulos:Q', title='Títulos'),
        y=alt.Y('categoria:N', title=None, sort='-x', axis=alt.Axis(labelLimit=230)),
        opacity=alt.when(selection).then(alt.value(1)).otherwise(alt.value(0.25)),
        tooltip=[alt.Tooltip('categoria:N', title='Categoria'), alt.Tooltip('titulos:Q', title='Títulos')],
    ).add_params(selection).properties(height=350).configure_view(stroke=None)


def decade_bar(data):
    return alt.Chart(data).mark_bar().encode(
        x=alt.X('decada:O', title='Década de lançamento', axis=alt.Axis(labelAngle=-35)),
        y=alt.Y('titulos:Q', title='Títulos'),
        color=alt.Color('tipo_conteudo:N', title='Tipo', scale=alt.Scale(domain=['Filme', 'Série'], range=[COLORS['Filme'], COLORS['Série']])),
        tooltip=[alt.Tooltip('decada:O', title='Década'), alt.Tooltip('tipo_conteudo:N', title='Tipo'), alt.Tooltip('titulos:Q', title='Títulos')],
    ).properties(height=350).configure_view(stroke=None)
