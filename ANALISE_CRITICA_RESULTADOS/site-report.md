# Relatório: Plataforma de Avaliação de Análise Crítica

**URL:** `https://avaliacao-analise-critica-hmg.aguiabranca.app.br/`
**Empresa:** Grupo Águia Branca / Soluções Digitais (DTI)
**Propósito:** Avaliação psicométrica e cognitiva de motoristas profissionais

---

## 1. Visão Geral da Plataforma

A plataforma **Avaliação de Análise Crítica** é um sistema web corporativo que administra uma bateria de testes cognitivos gamificados para motoristas profissionais. O objetivo é medir tempo de reação, precisão, memória, raciocínio espacial e tomada de decisão sob pressão.

Cada teste resulta em uma classificação binária: **Apto** ou **Inapto**, com base em limites configuráveis por tipo de teste.

---

## 2. Estrutura de Navegação

Barra lateral com três seções principais:

### 2.1. Dashboard (`#/dashboard/lista`)
Resumo executivo com indicadores agregados de todos os testes.

### 2.2. Testes (`#/teste/lista`)
Lista pesquisável e filtrável de registros individuais de teste.

### 2.3. Cadastros (submenu expansível)
- **Parâmetros** (`#/parametro/lista`) — Configuração dos limites de cada teste (rounds, duração máxima, erros)
- **Usuários** (`#/usuario/lista`) — Gestão de usuários do sistema
- **Imagens** (`#/imagem/lista`) — Gestão de imagens usadas nos testes visuais

---

## 3. Dashboard — Detalhamento

### 3.1. Cartões de Resumo (Linha Superior)
- **Data atual** — Exibição da data corrente
- **Motoristas Avaliados** — Número de motoristas únicos avaliados
- **Testes Realizados** — Total de testes completados
- **Dias de Coleta** — Quantos dias com coleta de dados

### 3.2. Tabela "Tempo para Completar Todo o Teste"
Tempo total para finalizar cada tipo de teste:

| Tipo de Teste | Qtd | Média (ms) | Mais Rápido (ms) | Mais Lento (ms) |
|---|---|---|---|---|
| Teste da Bola Caindo | 215 | 21.234,1 | 2.411 | 63.491 |
| Teste do Giroscópio | 49 | 3.797.438,12 | 19.283 | 183.515.795 |
| Teste de Ordem | 346 | 29.943,54 | 873 | 573.632 |
| Teste do Quebra-Cabeça | 80 | 22.948,9 | 3.676 | 310.664 |
| Teste de Pergunta | 392 | 12.814,22 | 1.108 | 441.326 |
| Teste de Mesma Imagem | 202 | 145.032,55 | 1.478 | 23.586.767 |
| Teste da Cobra | 82 | 86.311.038.772,79 | 15.145 | 1.769.433.028.602 |
| Teste de Alvo | 196 | 6.951,61 | 1.893 | 42.936 |

### 3.3. Tabela "Tempo de Cada Clique"
Métrica por clique/ação individual dentro de cada teste:

| Tipo de Teste | Média (ms) | Mais Rápido (ms) | Mais Lento (ms) |
|---|---|---|---|
| Teste da Bola Caindo | 726,96 | 3 | 14.839 |
| Teste do Giroscópio | 378.219,43 | 236 | 183.419.588 |
| Teste de Ordem | 1.722,16 | 52 | 551.871 |
| Teste do Quebra-Cabeça | 5.106,12 | 36 | 305.436 |
| Teste de Pergunta | 1.045,35 | 78 | 438.846 |
| Teste de Mesma Imagem | 5.192,96 | 114 | 2.361.126 |
| Teste da Cobra | 2.967,99 | 507 | 742.403 |
| Teste de Alvo | 695,16 | 106 | 33.178 |

### 3.4. "Testes Realizados por Dia"
Histórico diário de aplicações, paginado (10 por dia, 84 dias de coleta no total). Datas de março a maio de 2026.

### 3.5. Seção de Gráficos e Análise
- **Evolução dos Testes por Dia**
- **Análise por Tipo de Teste** — Seletor para filtrar gráficos por tipo
- **Checkbox "Incluir outliers"** (marcado por padrão)
- **Evolução do Tempo por Clique**
- **Evolução da Média de Tempo por Clique**
- **Histograma**
- **Boxplot de Tempo por Clique**

---

## 4. Página de Testes — Registros Individuais

Formulário de filtros:
- **CPF** — Busca por CPF do motorista
- **Status** — Todos / Apto / Inapto
- **Período** — Seleção de data inicial e final
- **Filtrar** / **Limpar**

Tabela de resultados (paginada, 1.564 registros totais):

| Coluna | Descrição |
|---|---|
| CPF | Cadastro de Pessoa Física do motorista |
| Data | Data e hora da realização do teste |
| Tipo de Teste | Qual teste foi aplicado |
| Status | Apto ou Inapto |
| Duração | Tempo total em milissegundos |
| Ação | Visualizar (detalhes) / Deletar |

---

## 5. Seção de Cadastros

### 5.1. Parâmetros — Configuração dos Testes
Cada tipo de teste possui parâmetros ajustáveis:
- **Rounds** — Número de rodadas (ex.: 5, 10, 15, 30)
- **Duração máxima** — Tempo limite em ms (ex.: 30.000, 57.679, 80.000)
- **Erros** — Tolerância a erros (todos configurados como 0)

8 conjuntos de parâmetros configurados de outubro/2025 a fevereiro/2026.

### 5.2. Usuários — Gestão de usuários do sistema
### 5.3. Imagens — Gestão de ativos visuais dos testes

---

## 6. Os 8 Testes Cognitivos

| # | Nome | O que mede |
|---|---|---|
| 1 | **Teste de Alvo** | Tempo de reação e precisão — clicar em alvos na tela |
| 2 | **Teste da Bola Caindo** | Coordenação motora e antecipação — interceptar objeto em queda |
| 3 | **Teste de Ordem** | Sequenciamento e memória operacional |
| 4 | **Teste de Mesma Imagem** | Discriminação visual e atenção aos detalhes |
| 5 | **Teste de Pergunta** | Conhecimento e tomada de decisão sob pressão |
| 6 | **Teste do Quebra-Cabeça** | Raciocínio espacial e resolução de problemas |
| 7 | **Teste da Cobra** | Controle motor fino e rastreamento (similar ao jogo "snake") |
| 8 | **Teste do Giroscópio** | Percepção de equilíbrio e movimento espacial |

---

## 7. Análise sob a Perspectiva do Gestor de Frota

> Persona: Gestor de frota responsável por liberar motoristas para viagens e acompanhar o desempenho da equipe ao longo do tempo.

### 7.1. Cenário Imediato — Decisão Operacional "Quente"

No dia a dia da operação, o gestor recebe um motorista escalado para uma viagem longa — por exemplo, uma rota de 1.200 km até um cliente no Nordeste. Antes de liberar a viagem, o motorista realiza a bateria de testes na plataforma.

**Como o sistema apoia essa decisão:**

- O **Dashboard** mostra na hora se o motorista foi avaliado e qual foi o resultado consolidado. Com um glance, o gestor vê o status geral.
- A página **Testes** permite buscar pelo **CPF** do motorista e ver o histórico completo daquela sessão — quais testes foram feitos, em que ordem, e o status (Apto/Inapto) de cada um.
- Se o motorista foi classificado como **Inapto** em qualquer teste crítico (ex.: Teste de Alvo com tempo de reação muito lento, ou Teste de Pergunta indicando falta de conhecimento), o gestor pode **desqualificar imediatamente** o motorista para aquela viagem.
- Um resultado Inapto pode indicar: fadiga, estresse, problemas de saúde, ou simplesmente um dia ruim. O sistema fornece a **evidência objetiva** para o gestor tomar a decisão sem depender de achismo.
- O motorista é **substituído** por outro da reserva que esteja apto, e a viagem segue sem riscos.

**Exemplo concreto:** Um motorista com CPF `059.258.347-39` realizou 3 testes no dia 05/05/2026 às 17:13:35. Resultado: Inapto no Teste de Alvo (5.385ms), Inapto no Teste da Bola Caindo (23.785ms), Apto no Teste do Quebra-Cabeça (11.054ms). O gestor vê que o motorista apresentou desempenho ruim em duas habilidades críticas para direção (reação e coordenação) e **não libera a viagem**.

### 7.2. Cenário de Longo Prazo — Avaliação de Performance Individual e da Equipe

O gestor também precisa olhar para o **quadro geral** e identificar tendências:

**Indicadores agregados no Dashboard:**
- **Total de motoristas avaliados** (35) — cobertura da frota
- **Total de testes realizados** (1.564) — volume de avaliações
- **Dias de coleta** (84) — consistência do programa
- O gestor pode verificar se a frota toda está sendo avaliada regularmente ou se há motoristas "esquecidos".

**Análise por tipo de teste:**
- O seletor **"Tipo de teste"** permite filtrar gráficos por teste específico. Ex.: o gestor desconfia que os motoristas estão piorando no Teste de Ordem (sequenciamento). Ele seleciona o teste e vê a **evolução ao longo do tempo** — está melhorando, piorando ou estável?
- O **Histograma** e o **Boxplot** mostram a distribuição dos tempos: onde está a mediana? Há muitos outliers? A equipe é homogênea ou há disparidade grande entre os melhores e piores?

**Comparação entre motoristas:**
- A tabela **"Tempo para Completar Todo o Teste"** permite comparar o desempenho médio da frota com o melhor e o pior caso. Se a média está subindo (tempos maiores), pode ser um sinal de alerta.
- A tabela **"Tempo de Cada Clique"** refina a análise: mesmo que o tempo total esteja bom, o tempo por clique pode revelar hesitação ou falta de prática.

**Identificação de outliers e anomalias:**
- O checkbox **"Incluir outliers"** (ativado por padrão) permite ao gestor decidir se quer ver os dados completos ou apenas a tendência central. Dados como `86 bilhões de ms` no Teste da Cobra sugerem que o motorista pode ter abandonado o teste ou pausado — o gestor pode investigar cada caso individualmente na página de Testes.

**Planejamento de ações corretivas:**
- Se um motorista específico apresenta Inapto recorrente, o gestor pode **acionar o RH ou a área de treinamento** para reciclagem.
- Se a frota toda apresenta desempenho baixo em um teste específico (ex.: Teste de Mesma Imagem), pode ser um indicador de que o treinamento precisa ser revisto ou que há um fator ambiental (ex.: cansaço geral da equipe por excesso de horas).

### 7.3. Gestão de Parâmetros — Ajuste Fino dos Critérios

O gestor (ou o administrador do sistema) pode acessar **Cadastros > Parâmetros** e ajustar os limites de cada teste:

- **Teste de Ordem:** 10 rounds, 57.679ms máx, 0 erros
- **Teste de Pergunta:** 15 rounds, 21.623ms máx, 0 erros
- **Teste da Bola Caindo:** 30 rounds, 30.000ms máx, 0 erros
- **Teste do Giroscópio:** 10 rounds, 80.000ms máx, 0 erros

Esses parâmetros podem ser **calibrados com base nos dados históricos**. Se 90% dos motoristas estão sendo reprovados no Teste do Giroscópio com o limite de 80s, talvez o limite esteja apertado demais — ou talvez os motoristas realmente precisem de treinamento nessa habilidade. O sistema fornece os dados para essa decisão.

### 7.4. Integração com o Fluxo Operacional

A página de Testes funciona como o **"prontuário eletrônico"** do motorista:

1. Motorista chega para a viagem
2. Realiza a bateria de testes (possivelmente em um tablet na garagem)
3. Gestor consulta o CPF no sistema
4. Vê o resultado: **Apto** = libera viagem; **Inapto** = substitui motorista e agenda nova avaliação
5. Ao longo do tempo, o gestor usa os gráficos para **monitorar a saúde cognitiva da frota**

### 7.5. Limitações Atuais para o Gestor

- O Dashboard mostra dados agregados mas **não parece ter um filtro por período** para análise temporal mais refinada nos resumos (apenas nos gráficos)
- **Não há uma comparação explícita "motorista A vs motorista B"** — o gestor precisaria consultar manualmente cada CPF
- A página de Testes estava **sem dados** na segunda navegação (0 de 0 registros), o que pode indicar que a busca precisa de filtros obrigatórios ou que há um problema de carregamento
- **Não há evidência de notificações ou alertas** — o gestor precisa consultar ativamente o sistema em vez de ser notificado quando um motorista é reprovado

---

## 8. Observações Técnicas para o Vídeo de Screencast

- **Esquema de cores:** Tons corporativos navy/azul (consistente com a marca Grupo Águia Branca)
- **SPA (Single Page Application):** A navegação é baseada em hash (`#/dashboard/lista`, `#/teste/lista`, etc.)
- **Tabelas com paginação:** Suportam "Items per page" (10 ou 20), botões de primeira/anterior/próxima/última página
- **Dados reais disponíveis:** 35 motoristas, 1.564 testes, 84 dias de coleta (até maio/2026)
- **A classificação Apto/Inapto** é o principal output de decisão — mostra se o motorista passou ou não em cada dimensão cognitiva
- **O toggle de outliers** demonstra preocupação com qualidade dos dados (alguns testes mostram durações extremas que distorcem as médias)
- **Footer:** "Powered by DevOps" — indica que a plataforma foi desenvolvida internamente pela equipe de DevOps/Soluções Digitais do grupo
