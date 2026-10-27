# Netflix: análise exploratória e Streamlit

Entrega da Aula 21 de Análise e Visualização de Dados (2026.2), baseada no repositório-modelo https://github.com/mfal-school/AVD-20262-pratica-streamlit e no PDF “Aula 21 - Streamlit parte 1”.

## Escopo desta entrega

Conforme as páginas 18, 21 e 22 do PDF: layout, widgets e espaços reservados para os gráficos do Dashboard 1. Heatmap, histograma e Dashboard 2 de KPIs pertencem à próxima etapa. Os filtros já funcionam sobre o CSV tratado.

## Executar no Windows

Use Python 3.12 (versão utilizada na validação).

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m streamlit run app.py
```

No macOS/Linux, use `python3 -m venv .venv`, depois `.venv/bin/python -m pip install -r requirements.txt` e `.venv/bin/python -m streamlit run app.py`.

Para configurar as instruções de IA do Streamlit, execute `python -m streamlit skills --yes` no ambiente do projeto.

## Dados e reprodução

- Entrada: `netflix_content_intelligence_combined.csv`, fornecido pelo aluno, com 7.786 linhas e 40 colunas.
- Bruto local: `data/raw/dataset.csv` (incluído no pacote local, ignorado pelo Git, conforme o modelo).
- Tratado: `data/clean/dataset.csv`, com 7.786 linhas e 42 colunas, incluído no Git.
- Notebook: `notebooks/eda.ipynb`. Execute todas as células usando o ambiente acima. Pode ser aberto localmente no VS Code/Jupyter ou no Colab. No Colab, se o bruto não existir, a célula de carregamento solicita upload do CSV original.
- A última célula de código exporta os dados brutos e tratados. Execute a EDA completa antes de exportar.

Tratamento reproduzido: `type` é mapeado para `tipo_conteudo` (Filme/Série) e `imdb_votes_log = log1p(imdb_votes)`. Não houve remoção de títulos, imputação ou exclusão de extremos. O subconjunto `df_notas` possui 5.331 registros e é usado apenas nas comparações que exigem ambas as notas.

Fonte do notebook: https://colab.research.google.com/drive/1LBwfll2VYpDFk61nXW9KonxWqa0oK7wt

O endereço público original do dataset e sua licença não foram fornecidos. Esses campos devem ser documentados pelo aluno antes de tornar a base pública. Os dados descrevem uma base histórica, com lançamentos até 2021, e não o catálogo atual.

## Organização

| Arquivo | Função |
| --- | --- |
| `app.py` | Layout, widgets, contagem e prévia dos títulos filtrados |
| `src/data_loader.py` | Leitura com cache apenas do CSV tratado |
| `src/filters.py` | Aplicação dos filtros sem alterar o dataset |
| `notebooks/eda.ipynb` | EDA do aluno adaptada com exportação reproduzível |
| `prompts/rascunho_dashboard1.png` | Rascunho de layout criado antes do aplicativo |
| `prompts/layout-skeleton-prompt.md` | Especificação estruturada usada na implementação |
| `prompts/declaracao-uso-ia.md` | Registro do apoio de IA e decisões adotadas |
| `tests/test_app.py` | Verificação de filtros, ausências e estados vazios |

## Decisões sobre os filtros

Selecionar variáveis escolhe o conteúdo dos futuros gráficos. O seletor do intervalo determina qual variável filtra os títulos. Por padrão, o intervalo de ano inclui todos os registros. Ausências são mantidas por padrão e podem ser excluídas explicitamente. A prévia mostra no máximo 100 linhas; a contagem considera todos os títulos filtrados.

## Verificação

Na raiz, execute `python -m unittest discover -s tests -v`.

## Entrega no GitHub

O repositório pessoal de destino ainda não foi informado. A preparação local não representa envio ao GitHub ou entrega no Classroom. O histórico original do modelo foi preservado. `data/raw` fica fora do Git; o notebook, o CSV tratado, o aplicativo, o rascunho e os registros de IA compõem a entrega versionada.

Para publicar quando o destino estiver definido, configure seu repositório pessoal como `origin` e faça push da branch da entrega. Não envie alterações diretamente ao repositório da professora.
