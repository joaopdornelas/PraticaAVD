# Declaração de Uso de Inteligência Artificial Generativa

**RASCUNHO NÃO ASSINADO - NÃO É A ENTREGA FINAL**

Atividade Streamlit AVD - 2026.2 - Dashboards com Streamlit, Aulas 21 a 23.

Preparado em 29/10/2026 e atualizado em 03/11/2026 com informações do histórico. Dados não confirmados, revisão individual e assinatura permanecem pendentes. A entrega final deve ser preenchida, assinada e salva como `prompts/DECLARACAO_IA.pdf`, no repositório e no Classroom.

O registro reúne dúvidas e revisões do aluno, pedidos de implementação e propostas da IA. João Pedro Rodrigues confirmou que o público e as justificativas breves representam suas escolhas; a origem assistida dessas propostas está registrada. O enquadramento dos usos deve ser conferido conforme as diretrizes abaixo.

[Template oficial da professora](https://docs.google.com/document/d/1HJsUJU0cbTouZ2d5vszmFqubbdtfkbObmaEBRI0MvR4/edit)

## 1. Identificação

- **Turma:** 5B (confirmada pelo aluno).
- **Nome completo:** João Pedro Rodrigues.
- **E-mail:** jprda@cesar.school
- **Repositório:** https://github.com/joaopdornelas/PraticaAVD
- **Aplicativo publicado:** https://praticaavd-hkc3krmurmwykzel3f98ae.streamlit.app/
- **Data de entrega:** ____ / ____ / ________

## 2. Diretrizes (leiam antes de usar qualquer ferramenta)

**Permitido, desde que registrado na Seção 5:**

- Usar a Skill oficial do Streamlit (streamlit skills) para orientar a IA a gerar código no padrão correto da biblioteca.
- Gerar o esqueleto do app.py a partir do seu rascunho de layout, usando o Template de Prompt (Contexto, Entrada, Restrições, Formato de saída). Essa etapa faz parte da própria atividade (Aula 21).
- Apoio na criação de identidade visual e/ou apoio na otimização da interface do dashboard.
- Tirar dúvidas conceituais sobre Streamlit, Python, pandas, Git etc., como um tutor.
- Apoio com a sintaxe de bibliotecas de visualização (Altair, Plotly, Seaborn, matplotlib): o código que desenha o gráfico, não a escolha do gráfico nem a interpretação dele.
- Entender mensagens de erro e depurar código (local ou do deploy).
- Revisar ortografia e clareza do README e de textos escritos por você.

**Proibido:**

- Deixar que a IA escolha, proponha ou justifique sozinha as métricas do Dashboard 2. As métricas podem ser calculadas com apoio de IA, mas a escolha de quais usar e por quê precisa ser sua, validada individualmente e consistente com o que você escreveu em entregas/justificativa-metricas.md.
- Pedir que a IA interprete os dados, escreva a justificativa das métricas ou tire conclusões sobre o seu dataset em seu lugar.
- Entregar qualquer trecho de código que você não saiba explicar. Inclusive o esqueleto do app.py gerado via IA/Skill.
- Omitir o uso de IA ou da Skill do Streamlit.

**Obrigatório:**

- Declarar se usou ou não a Skill oficial do Streamlit (streamlit skills), obrigatório mesmo que o único uso de IA tenha sido gerar o esqueleto do app.py com ela.
- Entregar esta declaração preenchida e assinada, mesmo que você não tenha usado IA.
- Marcar no código todo trecho feito com apoio de IA: # [IA] <ferramenta> - <finalidade>.
- Registrar cada uso na Seção 5 OU compartilhar os links das conversas completas com a professora (única forma de dispensar o registro bloco a bloco).

| Situação | Consequência |
|---|---|
| Uso declarado e dentro das diretrizes | Sem desconto. |
| Uso proibido, porém declarado | Itens afetados avaliados como “Não entregue”. |
| Uso não declarado, ou código/análise que o grupo não sabe explicar | Nota ZERO no projeto. |
| Declaração ausente ou sem assinatura de todos | Nota ZERO no projeto. |

Na dúvida sobre se um uso é permitido, perguntem à professora antes de usar. A declaração vale 0,5 ponto na rubrica; o template ressalta a obrigatoriedade da assinatura.

## 3. Declaração geral (marquem uma opção)

- [ ] Não utilizei nenhuma ferramenta de IA generativa em nenhuma etapa do projeto.
- [ ] Utilizei IA generativa, somente nas situações permitidas, e registramos todos os usos nas Seções 4 a 6 (links das conversas ou blocos de registro).

**Nenhuma opção marcada neste rascunho.** Houve uso de IA, inclusive na proposta de métricas e na redação de justificativas. O aluno confirmou posteriormente que as justificativas representam suas escolhas. Antes de preencher esta seção, é necessário esclarecer com a professora o enquadramento desses usos; o rascunho não declara que todos foram permitidos.

## 4. Ferramentas utilizadas

| Ferramenta | Versão / plano | Parte da atividade |
|---|---|---|
| ChatGPT / Codex | A confirmar pelo aluno | Estrutura, código, gráficos, métricas, textos, testes, documentação e orientações |
| Skill oficial do Streamlit | Nome/versão e uso anterior a confirmar | Não utilizada na etapa 3 de 29/10/2026 nem na revisão de 03/11/2026; confirmar consulta ou uso nas etapas anteriores e acrescentar registro específico |
| Ferramentas auxiliares do Codex | Google Drive e habilidade de PDF | Leitura do template oficial, elaboração e conferência deste rascunho |

## 5. Registro de usos

**Formato:** sínteses dos pedidos ao longo da conversa, e não transcrições literais de prompts. O registro inclui dúvidas, revisões, aprovações, pedidos de implementação e propostas analíticas feitas pela IA.

**Forma de registro:** opção B, bloco a bloco. A opção A do template permite usar links das conversas completas; nenhum link foi criado ou publicado automaticamente. Referência dos blocos: conversa deste projeto no Codex; link ou anexo não informado.

**Conferência:** os testes do assistente e as ações confirmadas do aluno são descritos separadamente. Datas antigas, versão/plano da ferramenta e uso anterior da Skill oficial do Streamlit ainda precisam ser conferidos.

### Uso nº 1 - Requisitos, estrutura e dados

- **Data:** Etapas anteriores - datas a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/data_loader.py; data/clean/dataset.csv; README.md; notebooks/eda-com-downloads.ipynb.
- **Finalidade e enquadramento:** Leitura dos requisitos, organização do projeto e implementação.
- **Resumo do que foi pedido:** Forneci os slides, o repositório-modelo, meu Colab e o dataset. Pedi a análise desses materiais, a obtenção da base tratada e a implementação do que a atividade solicitava.
- **O que foi aproveitado e modificado:** Organização dos arquivos, carregamento dos dados com cache e adaptação da exportação. O notebook original foi preservado. O apoio incluiu implementação, além das explicações.
- **Como foi verificado:** O assistente conferiu os arquivos e a base. Minha participação incluiu fornecer os materiais e pedir a comparação com os requisitos; conferências pessoais adicionais ainda precisam ser registradas.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 2 - Filtros e gráficos do Dashboard 1

- **Data:** Etapas anteriores - datas a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/filters.py; src/analytics.py; src/charts.py.
- **Finalidade e enquadramento:** Implementação de filtros, correlação e histogramas conforme a atividade.
- **Resumo do que foi pedido:** Pedi que a aplicação fosse construída a partir da EDA e atendesse aos gráficos e filtros exigidos. Depois solicitei revisão do código e correções conforme o material da professora.
- **O que foi aproveitado e modificado:** O assistente escreveu e ajustou o código dos filtros, do mapa de correlação e dos histogramas, incluindo o tratamento de ausências e de seleções vazias.
- **Como foi verificado:** O assistente realizou testes dos filtros e cálculos. Minha conferência da leitura dos gráficos e da explicação do código ainda deve ser descrita.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 3 - Implementação do Dashboard 2

- **Data:** Etapas anteriores - datas a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/analytics.py; src/charts.py; notebooks/metricas.ipynb; entregas/justificativa-metricas.md.
- **Finalidade e enquadramento:** Código dos indicadores e gráficos, com propostas analíticas e textos elaborados pela IA.
- **Resumo do que foi pedido:** Pedi a implementação da parte 2 no VS Code e solicitei revisar antes do commit. Também pedi para abrir o app no navegador. A IA propôs os indicadores e suas justificativas, além de implementar o painel.
- **O que foi aproveitado e modificado:** Total de títulos, percentual com nota IMDb, nota IMDb mediana e participação de séries. Foram aproveitados cálculos, código e propostas de justificativas. Posteriormente, confirmei que as justificativas breves propostas pela IA representavam minhas escolhas e autorizei incluí-las no arquivo.
- **Como foi verificado:** O assistente conferiu cálculos e testes. Solicitei a revisão antes do envio e depois autorizei o commit; isso não comprova que testei pessoalmente todos os comportamentos.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 4 - Revisão, simplicidade e testes

- **Data:** Etapas anteriores - datas a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/; tests/; notebooks/metricas.ipynb.
- **Finalidade e enquadramento:** Revisão da implementação, depuração e adequação ao conteúdo das aulas.
- **Resumo do que foi pedido:** Pedi para verificar se o código seguia as aulas, sem técnicas desnecessariamente complexas ou não solicitadas. Depois pedi as correções necessárias e testes do aplicativo.
- **O que foi aproveitado e modificado:** Simplificação de cálculos e organização, uso de Seaborn no Dashboard 1 e manutenção de Altair no Dashboard 2. O assistente também escreveu e executou testes.
- **Como foi verificado:** Sete testes haviam passado na etapa anterior; a revisão posterior teve dez testes, registrada no uso 9. Os testes técnicos foram executados pelo assistente.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 5 - Notebooks, rascunhos e organização da entrega

- **Data:** Etapas anteriores e atualização em 29/10/2026; datas anteriores a confirmar.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** notebooks/; entregas/; README.md; VALIDACAO.md local.
- **Finalidade e enquadramento:** Preparação dos entregáveis e explicações sobre a organização do projeto.
- **Resumo do que foi pedido:** Pedi a análise dos materiais e a preparação das partes da atividade. Também perguntei para que serviam ROTEIRO.md e VALIDACAO.md e como manter a validação no VS Code sem enviá-la ao GitHub.
- **O que foi aproveitado e modificado:** Notebooks, desenhos dos dashboards e documentação produzidos com apoio de IA. VALIDACAO.md foi mantido local e fora do versionamento. As justificativas receberam apoio de redação, registrado no uso 3.
- **Como foi verificado:** O assistente executou o notebook de métricas e conferiu os rascunhos. A revisão pessoal dos demais entregáveis ainda deve ser registrada.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 6 - Aprendizado de Git e execução no VS Code

- **Data:** Etapas anteriores - datas a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** Configuração local, Git, .gitignore e orientações no README.md.
- **Finalidade e enquadramento:** Tutoria, explicação de erros e apoio ao versionamento.
- **Resumo do que foi pedido:** Pedi para aprender do zero a instalar e usar o Git. Tirei dúvidas sobre nome e e-mail, commits, conexão ao GitHub, envio dos arquivos e conflito no README. Executei comandos e compartilhei as saídas do terminal para receber orientação.
- **O que foi aproveitado e modificado:** Explicações sobre commit e push, orientação para resolver erros e ações de versionamento autorizadas por mim. Também recebi instruções para executar o app no VS Code.
- **Como foi verificado:** As saídas que enviei mostram execução de git init, git status e tentativas de push, incluindo mensagens de erro e conflito. O aplicativo foi publicado, e o endereço informado foi adicionado ao README. Posteriormente, confirmei na conversa que realizei o teste do app público em janela anônima.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 7 - Conclusão da implementação da parte 3

- **Data:** 29/10/2026 - data histórica registrada; a confirmar pelo aluno.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/; tests/; notebooks/metricas.ipynb; entregas/.
- **Finalidade e enquadramento:** Implementação dos requisitos restantes e propostas de público e visual.
- **Resumo do que foi pedido:** Acrescentei o enunciado completo da atividade e pedi a execução da parte 3 com as melhorias necessárias. Nesse momento, também pedi que o assistente propusesse o público e decidisse o terceiro gráfico.
- **O que foi aproveitado e modificado:** Um histograma para cada variável selecionada e um terceiro visual no Dashboard 2. O assistente propôs o público de analistas de curadoria e o gráfico de medianas, posteriormente substituído no uso 9.
- **Como foi verificado:** O assistente revisou o código e executou testes. A tentativa de controle do navegador foi bloqueada; não foi registrada como teste visual concluído. Minha turma foi confirmada como 5B.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 8 - Organização e revisão da declaração de IA

- **Data:** Adaptação ao template em 29/10/2026; revisão em 03/11/2026. Datas anteriores a confirmar.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** prompts/declaracao-uso-ia.md; prompts/README.md; prompts/DECLARACAO_IA_RASCUNHO.pdf.
- **Finalidade e enquadramento:** Organização e redação do registro de uso de IA.
- **Resumo do que foi pedido:** Pedi uma redação menos genérica que destacasse a colaboração, minhas dúvidas e revisões. Também solicitei uma sugestão breve de reflexão individual.
- **O que foi aproveitado e modificado:** Resumos dos pedidos e reflexão propostos com apoio de IA. Confirmei que a reflexão correspondia à minha experiência e autorizei incluí-la. O assistente organizou o Markdown e o PDF; a assinatura permanece em branco.
- **Como foi verificado:** O assistente conferiu o conteúdo e a apresentação do rascunho. Ainda preciso revisar as informações pessoais, as datas, o registro de uso e o termo antes de assinar.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

### Uso nº 9 - Avaliação dos dados e revisão dos gráficos

- **Data:** 03/11/2026.
- **Ferramenta:** ChatGPT / Codex; versão/plano a confirmar.
- **Parte da atividade:** app.py; src/; tests/; notebooks/metricas.ipynb; README.md; entregas/; prompts/.
- **Finalidade e enquadramento:** Auditoria técnica, interpretação dos dados, propostas analíticas e implementação.
- **Resumo do que foi pedido:** Pedi uma avaliação do atendimento aos requisitos, da qualidade dos dados e da utilidade dos gráficos. Perguntei se as mudanças manteriam as exigências da professora e depois autorizei a implementação. Também solicitei o teste em janela anônima.
- **O que foi aproveitado e modificado:** Logaritmo inicialmente ativado nos histogramas de votos e popularidade. No Dashboard 2, substituição dos gráficos por década e de medianas por cobertura IMDb por categoria e boxplot por tipo. O assistente propôs e implementou essas mudanças; os quatro indicadores e o dataset foram preservados.
- **Como foi verificado:** O assistente executou dez testes com sucesso e oito células do notebook sem erros, com três gráficos. Foram conferidas as 5.460 notas do boxplot e os denominadores da cobertura. A tentativa de teste em janela anônima pelo assistente foi bloqueada. Posteriormente, realizei o teste em janela anônima e confirmei sua realização na conversa. O aplicativo já foi publicado no endereço indicado na identificação. Erros de associação entre títulos e avaliações continuam pendentes.
- **Link ou anexo da conversa:** referência comum indicada no início desta seção.

## 6. Trechos de código feitos com apoio de IA

O esqueleto assistido é previsto na atividade. O detalhamento permanece nas Seções 4 e 5. Todo trecho assistido deve receber comentário `# [IA] <ferramenta> - <finalidade>`.

| Arquivo / parte | Teve apoio de IA? | Tipo de apoio |
|---|---|---|
| app.py (esqueleto) | Sim | Estrutura, componentes, filtros e organização das abas. |
| Dashboard 1 | Sim | Filtros, correlação, histogramas, Seaborn e depuração. |
| Dashboard 2 | Sim | Cálculos, Altair, seleção e propostas analíticas declaradas no registro. |
| Deploy / configuração | Sim, parcial | Configuração e orientação. Aplicativo publicado, com link no README. Teste em janela anônima realizado pelo aluno, conforme confirmação na conversa. |
| Notebooks e testes | Sim | Cálculos explícitos, código de gráficos e verificações automáticas. |
| Skill oficial Streamlit | A confirmar | Não usada nesta etapa; confirmar consulta/uso nas etapas anteriores. |

## 7. Reflexão individual (10 a 15 linhas)

Onde a IA ajudou? Em algum momento ela sugeriu uma métrica, um gráfico ou uma interpretação que você teve que ajustar ou rejeitar? Como você garantiu que as métricas do Dashboard 2 refletem sua própria escolha e validação, e não apenas o que a IA sugeriu?

01. A IA me ajudou a entender Git e organizar o projeto.
02. Também ajudou na implementação dos dashboards.
03. Pedi que o código seguisse os conteúdos das aulas.
04. Solicitei que fossem evitadas técnicas muito complexas.
05. Pedi uma análise dos gráficos e da qualidade dos dados.
06. Perguntei se as mudanças manteriam os requisitos da professora.
07. A IA sugeriu métricas e mudanças nos gráficos.
08. Aprovei as mudanças e confirmei as justificativas apresentadas.
09. Percebi que notas ausentes e erros na base afetam as comparações.
10. Antes de entregar, preciso entender o código e os resultados.

## 8. Termo de responsabilidade

**Texto do termo oficial, reservado para revisão e assinatura do aluno:**

Declaro que as informações deste documento são verdadeiras e completas; que compreendo e sei explicar todo o código, as saídas e as análises entregues, inclusive os trechos feitos com apoio de IA; e que estou ciente de que uso não declarado, uso proibido, Skill não declarada, ou incapacidade de explicar o trabalho resultam nas consequências da Seção 2.

**Nome:** João Pedro Rodrigues
**Assinatura (manuscrita ou gov.br):** ______________________________
**Data:** ____ / ____ / ________

**Rascunho não assinado.** A presença do nome não equivale a assinatura nem a concordância com o termo. Antes da entrega final, preencher as lacunas, confirmar os usos e sua completude, revisar a reflexão e assinar.
