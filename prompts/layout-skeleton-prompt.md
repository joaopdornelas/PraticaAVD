# Especificação estruturada: rascunho para esqueleto

Esta especificação foi elaborada pelo assistente a partir do pedido do aluno e usada na implementação; não é apresentada como texto escrito originalmente pelo aluno.

## Contexto

Construir a entrega da Aula 21 da disciplina Análise e Visualização de Dados. Usar a EDA da Netflix do aluno, com 7.786 títulos. O projeto segue o repositório-modelo, com `app.py`, `src/data_loader.py`, `notebooks/` e `data/clean/dataset.csv`.

## Entrada

Rascunho criado antes do app: `entregas/rascunho-dashboard1.png`. Sidebar com tipos de conteúdo, seleção múltipla de variáveis, variável de intervalo, slider e opção de manter ausências. Área principal com Correlação à esquerda e Distribuição à direita. Prévia expansível abaixo.

Variáveis: `release_year`, `imdb_rating`, `imdb_votes`, `tmdb_rating`, `tmdb_popularity`. Classe: `tipo_conteudo`. Perguntas: como os valores se distribuem, como se relacionam e como diferem entre filmes e séries?

## Restrições

Nesta aula, implementar o esqueleto e os widgets mínimos. Manter os gráficos como espaços reservados e comentários TODO para a próxima etapa. Carregar somente dados tratados. Não imputar ausências nem excluir extremos silenciosamente. Tratar seleção vazia, uma única variável e filtros sem resultados. Usar componentes nativos do Streamlit.

## Formato de saída

Um `app.py` executável, com funções auxiliares pequenas em `src/`, CSV tratado, notebook com exportação e registro de uso de IA.
