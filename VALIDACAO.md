# Validação da entrega

Executada em 25/10/2026, com Python 3.12, Streamlit 1.66.1, pandas 2.3.3 e NumPy 2.5.4.

- Notebook `notebooks/eda.ipynb`: todas as células executadas, sem erros. Resultados e gráficos salvos no próprio notebook.
- Exportação bruta: 7.786 linhas e 40 colunas. Comparação com o CSV fornecido pelo aluno aprovada.
- Exportação tratada: 7.786 linhas e 42 colunas. Comparação com o dataset tratado anteriormente aprovada (tolerância numérica de 1e-12 na reexportação).
- Testes automatizados: 3 aprovados, incluindo preservação dos 7.786 títulos e 2.326 ausências IMDb no estado inicial, escolha explícita sobre ausências e interação da interface com seleções vazias, uma variável, mudança de intervalo e nenhum título resultante.
- Rascunho de layout inspecionado visualmente.
- Dados brutos ignorados pelo Git conforme o modelo; CSV tratado incluído no versionamento.

O aplicativo foi testado com AppTest, que executa o Streamlit sem abrir um servidor. Não foi realizado deploy no Streamlit Community Cloud.

As instruções oficiais incluídas no pacote Streamlit foram consultadas diretamente. A instalação automática das skills por symlink não foi concluída devido às permissões do Windows; não foram alteradas configurações do sistema.

## Correspondência com a Aula 21

| Requisito | Evidência |
| --- | --- |
| Utilizar a EDA própria (p. 3) | `notebooks/eda.ipynb`, adaptado do Colab do aluno |
| Planejar o layout (p. 15–16) | `prompts/rascunho_dashboard1.png`, criado antes do app |
| Prompt estruturado (p. 18) | `prompts/layout-skeleton-prompt.md` |
| Seletor de variáveis (p. 21) | Multisseleção de cinco variáveis quantitativas |
| Filtro de intervalo (p. 21) | Seletor de variável e slider |
| Áreas de correlação/distribuição (p. 21) | Dois containers com placeholders e TODOs |
| Exportar bruto e tratado (p. 22) | Célula final de exportação e arquivos em `data/` |
| Commit e push (p. 22) | Commit local preparado; push depende do repositório pessoal |

O aluno ainda deve preencher seu nome e registrar a revisão humana na declaração de IA. O destino GitHub e a fonte pública/licença original do dataset não foram informados.
