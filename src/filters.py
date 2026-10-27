def filter_data(df, tipos, variavel, intervalo, manter_ausentes=True):
    """Aplica o intervalo sem remover ausências implicitamente nem editar a base."""
    mask = df["tipo_conteudo"].isin(tipos)
    valores = df[variavel]
    dentro = valores.between(*intervalo) if intervalo is not None else valores.notna()
    if manter_ausentes:
        dentro = dentro | valores.isna()
    return df.loc[mask & dentro].copy()
