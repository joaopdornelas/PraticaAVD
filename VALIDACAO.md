# Validação — Aulas 21 e 22

Atualizada em 27/10/2026. Python 3.12, Streamlit 1.66.1, pandas 2.3.3, NumPy 2.5.4 e Altair 6.3.

## Verificações concluídas

- Sete testes automatizados aprovados novamente na pasta do VS Code, com seu próprio ambiente `.venv`: `python -m unittest discover -s tests -v` (5,830 segundos, em 27/10/2026).
- Correlação: pares válidos, relação inversa conhecida e variável constante. Histogramas: intervalos comuns, contagens preservadas e percentuais por grupo, com e sem transformação logarítmica.
- Indicadores: conferência dos totais, seleção de categorias, ausência de notas e recorte vazio.
- AppTest: duas abas, filtros compartilhados, zero/uma/duas variáveis, intervalo, remoção de ausentes, nenhum título, separação por tipo, log, agrupamento e botão de limpeza sem exceções.
- `notebooks/metricas.ipynb` executado integralmente com resultados e gráficos salvos, sem erros. Fórmulas conferidas por cálculos independentes.
- `notebooks/eda.ipynb` preserva exatamente o notebook original do aluno. A versão adaptada e executada na Aula 21 foi mantida em `notebooks/eda-com-downloads.ipynb`.
- Dataset tratado preservado: 7.786 linhas e 42 colunas; 5.460 notas IMDb disponíveis, mediana 6,5 e 2.410 séries. Ausências não foram substituídas por zero.
- Rascunho do Dashboard 2 criado antes da implementação e inspecionado visualmente.
- Servidor local respondeu `ok` na rota de saúde. A conferência visual do aplicativo pelo navegador automatizado não foi concluída porque a ferramenta não respondeu; os testes de interface foram realizados com AppTest. O clique real nas barras ainda deve ser conferido pelo aluno no navegador.

## Correspondência com a Aula 22

| Requisito | Evidência |
| --- | --- |
| Dashboard 1 com gráficos e filtros | Matriz de Spearman e histograma em `app.py` e `src/` |
| Casos de zero, uma e várias variáveis | `tests/test_app.py` |
| Identidade visual | `.streamlit/config.toml`, vermelho, azul e neutros |
| Planejar 3–5 métricas e justificá-las | Quatro métricas em `entregas/justificativa-metricas.md` |
| Experimentar métricas e visuais no notebook | `notebooks/metricas.ipynb` |
| Rascunhar Dashboard 2 | `entregas/rascunho-dashboard2.jpg` |
| Duas abas e agrupamento categórico | Agrupamento por gênero, país ou tipo |
| Interação Altair | Seleção nas barras refina indicadores e gráfico por década |
| Atualizar roteiro e organização | `ROTEIRO.md`, `ALTAIR-CROSSFILTER.md`, `entregas/` e `prompts/` |
| Declarar uso de IA | `prompts/declaracao-uso-ia.md` |

## Pendências para entrega

Repositório: https://github.com/joaopdornelas/PraticaAVD. O aluno autorizou o commit e o push da parte 2 em 27/10/2026. O aluno deve preencher seu nome e registrar sua revisão humana na declaração de IA. A fonte pública e a licença original do dataset também devem ser documentadas. Não foi feito deploy; essa etapa está prevista para a Aula 23.
