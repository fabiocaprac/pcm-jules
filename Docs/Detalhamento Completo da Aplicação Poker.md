# Detalhamento Completo da Aplicação Poker Cash Manager

Este documento descreve em detalhes a aplicação "Poker Cash Manager", focando em suas funcionalidades, componentes lógicos, conceitos de negócio, elementos da interface e um esboço de Requisitos de Produto (PRD), com o objetivo de fornecer um guia para sua recriação de forma independente de tecnologias específicas.

## 1. Introdução e Objetivo da Aplicação

O Poker Cash Manager é uma ferramenta projetada para auxiliar organizadores de jogos de poker a gerenciar de forma eficiente todos os aspectos financeiros e operacionais de suas sessões de jogo. Seu principal objetivo é simplificar o controle de entradas e saídas de dinheiro (buy-ins, cashouts), registrar pagamentos, gerenciar jogadores, controlar o fichário e manter um histórico detalhado de todas as operações, substituindo controles manuais propensos a erros.

## 2. Conceitos Fundamentais

A aplicação gira em torno dos seguintes conceitos centrais:

-   Sessão de Jogo (Session): Representa uma partida ou um período contínuo de jogo. É a unidade central onde ocorrem as transações e a participação dos jogadores. Possui um início, um fim (potencial) e um status (ativa ou finalizada).
-   Caixa (Cash Box): Simboliza o "banco" ou o fundo financeiro do organizador/casa. É onde o dinheiro das transações é conceitualmente movimentado e de onde a sessão atual é gerenciada.
-   Jogador na Sessão (Player in Session): Um participante individual dentro de uma sessão de jogo específica. Seu desempenho financeiro (buy-ins, cashouts, pagamentos) é rastreado dentro do contexto dessa sessão.
-   Perfil de Jogador (Player Profile): Um registro persistente e global de um jogador, independente das sessões. Contém informações pessoais (nome, contato), limites de crédito e um histórico financeiro consolidado de todas as suas participações.
-   Transação (Transaction): Qualquer movimentação financeira registrada no sistema. Inclui:
    -   Buy-in: Compra de fichas por um jogador, adicionando dinheiro ao jogo/caixa.
    -   Cashout: Devolução de fichas por um jogador, retirando dinheiro do jogo/caixa.
    -   Pagamento (Payment): Liquidação de dívidas ou créditos entre um jogador e a casa, ou vice-versa.
-   Fichário (Chip Set): O conjunto de fichas físicas usadas no jogo, com seus respectivos valores e quantidades. O sistema permite o controle do valor total em fichas na sessão.
-   Log de Atividades (Activity Log): Um registro cronológico de todas as ações significativas realizadas dentro da aplicação, servindo para auditoria e rastreamento.

## 3. Funcionalidades Principais (Esboço PRD)

### 3.1. Gerenciamento de Sessões

-   Como organizador, eu quero criar uma nova sessão de jogo, para poder iniciar o rastreamento de uma nova partida.
    -   Critérios de Aceitação: Deve ser possível definir um nome para a sessão e registrar a data/hora de início. A nova sessão deve se tornar a "sessão ativa" no Caixa.
-   Como organizador, eu quero continuar uma sessão de jogo anteriormente ativa, para retomar uma partida que não foi finalizada.
    -   Critérios de Aceitação: Ao selecionar uma sessão ativa, o sistema deve carregá-la como a sessão atual em operação.
-   Como organizador, eu quero finalizar uma sessão de jogo ativa, para encerrar formalmente uma partida e consolidar seus resultados.
    -   Critérios de Aceitação: Deve ser possível registrar a data/hora de término. A sessão deve mudar seu status para "finalizada" e deixar de ser a sessão ativa no Caixa.
-   Como organizador, eu quero visualizar uma lista de sessões ativas, para ter uma visão geral das partidas em andamento.
-   Como organizador, eu quero visualizar uma lista de sessões finalizadas, para consultar o histórico de partidas anteriores.

### 3.2. Gerenciamento de Jogadores na Sessão

-   Como organizador, eu quero adicionar um jogador a uma sessão ativa, para incluir participantes na partida.
    -   Critérios de Aceitação: Deve ser possível buscar por um Perfil de Jogador existente ou criar um novo Perfil de Jogador rapidamente caso ele não exista. O jogador adicionado deve aparecer na lista de participantes da sessão.
-   Como organizador, eu quero visualizar a lista de jogadores participantes da sessão ativa, juntamente com seus saldos financeiros atuais (dinheiro em jogo).

### 3.3. Operações Financeiras da Sessão

-   Como organizador, eu quero registrar um buy-in para um jogador, para contabilizar a entrada de dinheiro e a entrega de fichas.
    -   Critérios de Aceitação: Deve ser possível especificar o jogador, o valor do buy-in, o método de pagamento (dinheiro, PIX, cartão, etc.) e se o pagamento foi feito imediatamente ("pago") ou ficou pendente ("crédito" para o jogador pagar depois).
-   Como organizador, eu quero registrar um cashout para um jogador, para contabilizar a devolução de fichas e a saída de dinheiro.
    -   Critérios de Aceitação: Deve ser possível especificar o jogador, o valor do cashout, o método de pagamento e se o pagamento ao jogador foi feito imediatamente ("pago") ou ficou pendente ("dívida" da casa com o jogador).
-   Como organizador, eu quero registrar um pagamento para liquidar pendências de um jogador, para acertar dívidas ou créditos.
    -   Critérios de Aceitação: Deve ser possível especificar o jogador, o valor, o método de pagamento e a direção (jogador pagando à casa ou casa pagando ao jogador). A pendência do jogador deve ser atualizada.

### 3.4. Gerenciamento de Perfis de Jogadores (Global)

-   Como organizador, eu quero cadastrar um novo Perfil de Jogador, para manter um registro persistente dos participantes.
    -   Critérios de Aceitação: Deve ser possível informar nome, apelido (opcional), informações de contato (opcional), chave PIX (opcional) e um limite de crédito (opcional).
-   Como organizador, eu quero editar as informações de um Perfil de Jogador existente, para manter os dados atualizados.
-   Como organizador, eu quero excluir um Perfil de Jogador, (com as devidas confirmações e alertas sobre dados históricos).
-   Como organizador, eu quero visualizar os detalhes e o histórico financeiro global de um Perfil de Jogador.

### 3.5. Controle de Caixa e Fichário

-   Como organizador, eu quero definir e gerenciar os tipos de fichas (valores, cores, quantidades iniciais) para uma sessão, para controlar o fichário.
-   Como organizador, eu quero visualizar um resumo financeiro da sessão ativa, incluindo total de buy-ins, total de cashouts, valor total em fichas em jogo, total de pagamentos recebidos/feitos e pendências.
-   Como organizador, eu quero visualizar um resumo do Caixa, mostrando os saldos por método de pagamento (dinheiro, PIX, cartão).

### 3.6. Segurança e Privacidade

-   Como organizador, eu quero poder ocultar/mostrar os valores financeiros sensíveis na tela (saldos de jogadores, resumos financeiros), para proteger a informação em ambientes compartilhados.
    -   Critérios de Aceitação: A ação de ocultar/mostrar deve ser protegida por uma senha simples definida pelo organizador.

### 3.7. Logs e Auditoria

-   Como organizador, eu quero que todas as ações financeiras e operacionais importantes sejam registradas em um log, para fins de auditoria e rastreamento.
-   Como organizador, eu quero poder visualizar o log de atividades de uma sessão específica, com opções de filtro (por tipo de evento, por jogador).

### 3.8. Impressão de Recibos

-   Como organizador, eu quero poder gerar e imprimir um recibo individual para um jogador, detalhando suas movimentações financeiras (buy-ins, cashouts, pagamentos) e saldo final na sessão.

### 3.9. Reset de Dados (Funcionalidade Administrativa)

-   Como organizador, eu quero poder resetar todos os dados da aplicação (sessões, transações, etc., exceto perfis de jogadores e o próprio usuário organizador), para limpar o ambiente para testes ou um novo começo (com múltiplas confirmações).

## 4. Estrutura de Dados (Abstrata)

-   Caixa (CashBox):
    -   IDCaixa (Identificador Único)
    -   NomeCaixa (Texto)
    -   IDSessaoAtiva (Referência à Sessão)
    -   IDOrganizador (Referência ao Usuário Organizador)

-   Sessão (Session):
    -   IDSessao (Identificador Único)
    -   IDCaixa (Referência ao Caixa)
    -   NomeSessao (Texto)
    -   DataHoraInicio (Data/Hora)
    -   DataHoraFim (Data/Hora, opcional)
    -   Status (Texto: "Ativa", "Finalizada")
    -   IDOrganizadorCriador (Referência ao Usuário Organizador)
    -   IDOrganizadorFinalizador (Referência ao Usuário Organizador, opcional)
    -   (Implicitamente contém uma lista de JogadoresNaSessao e Transações)

-   JogadorNaSessao (PlayerInSession):
    -   IDJogadorSessao (Identificador Único)
    -   IDSessao (Referência à Sessão)
    -   IDPerfilJogador (Referência ao Perfil de Jogador)
    -   NomeJogadorExibicao (Texto, pode ser o nome ou apelido do perfil)
    -   TotalBuyInsSessao (Numérico, Monetário)
    -   TotalCashoutsSessao (Numérico, Monetário)
    -   TotalPagamentosSessao (Numérico, Monetário, pode ser negativo)
    -   SaldoPendenteSessao (Numérico, Monetário) - Calculado a partir de transações pendentes.
    -   SaldoAtualEmJogo (Numérico, Monetário) - Calculado: TotalBuyInsSessao - TotalCashoutsSessao.

-   PerfilJogador (PlayerProfile):
    -   IDPerfilJogador (Identificador Único)
    -   NomeCompleto (Texto)
    -   Apelido (Texto, opcional)
    -   ContatoWhatsApp (Texto, opcional)
    -   ChavePIX (Texto, opcional)
    -   LimiteCredito (Numérico, Monetário, opcional, default 0)
    -   SaldoGlobalAcumulado (Numérico, Monetário) - Calculado a partir de todas as participações e pagamentos gerais.
    -   IDOrganizador (Referência ao Usuário Organizador que cadastrou)

-   Transação (Transaction):
    -   IDTransacao (Identificador Único)
    -   IDSessao (Referência à Sessão)
    -   IDJogadorSessao (Referência ao JogadorNaSessao)
    -   TipoTransacao (Texto: "BuyIn", "Cashout", "Pagamento")
    -   Valor (Numérico, Monetário)
    -   MetodoPagamento (Texto: "Dinheiro", "PIX", "CartaoCredito", "CartaoDebito", "Nenhum/Pendente")
    -   StatusPagamento (Texto: "Pago", "Pendente")
    -   DirecaoPagamento (Texto: "EntradaCaixa", "SaidaCaixa" - relevante para "Pagamento")
    -   DataHoraTransacao (Data/Hora)
    -   IDOrganizadorExecutor (Referência ao Usuário Organizador)

-   Ficha (ChipDefinition - parte do Fichário da Sessão):
    -   IDFicha (Identificador Único)
    -   IDSessao (Referência à Sessão)
    -   Cor (Texto ou código de cor, opcional)
    -   ValorUnitario (Numérico, Monetário)
    -   QuantidadeInicial (Numérico, Inteiro)
    -   QuantidadeAtual (Numérico, Inteiro) - Pode ser gerenciado ou apenas usado para cálculo do total.

-   LogAtividade (ActivityLog):
    -   IDLog (Identificador Único)
    -   IDSessao (Referência à Sessão, se aplicável)
    -   IDTransacao (Referência à Transação, se aplicável)
    -   IDJogadorSessao (Referência ao Jogador, se aplicável)
    -   NomeJogadorLog (Texto, para manter referência caso jogador seja excluído)
    -   TipoEvento (Texto: "CriacaoSessao", "AddJogador", "RegistroBuyIn", etc.)
    -   Descricao (Texto detalhado do evento)
    -   ValorLog (Numérico, Monetário, se aplicável)
    -   DetalhesAdicionais (Texto, formato livre ou estruturado)
    -   DataHoraEvento (Data/Hora)
    -   IDOrganizadorResponsavel (Referência ao Usuário Organizador)

Relações Chave:

-   Um Caixa pode ter uma Sessao ativa.
-   Uma Sessao tem muitos JogadoresNaSessao e muitas Transacoes.
-   Um JogadorNaSessao está associado a um PerfilJogador.
-   Um JogadorNaSessao pode ter muitas Transacoes dentro de uma Sessao.
-   Logs (LogAtividade) são gerados para a maioria das operações sobre outras entidades.

## 5. Lógicas de Negócio Chave

-   Cálculo de Saldo do Jogador na Sessão (Dinheiro em Jogo): SaldoAtualEmJogo = Soma(BuyIns_Pagos_Sessao) - Soma(Cashouts_Pagos_Sessao) (Considera apenas o que efetivamente entrou e saiu de fichas/dinheiro com o jogador na mesa). Alternativamente, se TotalBuyInsSessao e TotalCashoutsSessao na entidade JogadorNaSessao já refletem as fichas totais: TotalBuyInsSessao - TotalCashoutsSessao.

-   Cálculo de Pendência do Jogador na Sessão: SaldoPendenteSessao = Soma(BuyIns_Pendentes_Sessao) - Soma(Cashouts_Pendentes_Sessao) Um valor positivo significa que o jogador deve à casa. Um valor negativo significa que a casa deve ao jogador. Os Pagamentos liquidam essas pendências.

-   Cálculo de Saldo do Caixa (por método de pagamento): Para Dinheiro: Soma(BuyIns_Pagos_Dinheiro) + Soma(Pagamentos_Entrada_Dinheiro) - Soma(Cashouts_Pagos_Dinheiro) - Soma(Pagamentos_Saida_Dinheiro) Similar para PIX, Cartão, etc.

-   Impacto das Transações:
    -   Buy-in Pago: Aumenta TotalBuyInsSessao do jogador. Aumenta Saldo do Caixa no método de pagamento correspondente.
    -   Buy-in Pendente: Aumenta TotalBuyInsSessao do jogador. Aumenta SaldoPendenteSessao do jogador (ele deve).
    -   Cashout Pago: Aumenta TotalCashoutsSessao do jogador. Diminui Saldo do Caixa no método de pagamento correspondente.
    -   Cashout Pendente: Aumenta TotalCashoutsSessao do jogador. Diminui SaldoPendenteSessao do jogador (casa deve a ele).
    -   Pagamento de Entrada (Jogador paga à casa): Diminui SaldoPendenteSessao do jogador. Aumenta Saldo do Caixa.
    -   Pagamento de Saída (Casa paga ao jogador): Aumenta SaldoPendenteSessao do jogador. Diminui Saldo do Caixa.

-   Lógica de "Finalizar Sessão":
    -   Atualiza Status da Sessão para "Finalizada".
    -   Registra DataHoraFim.
    -   Remove IDSessaoAtiva do Caixa.
    -   Os SaldosPendenteSessao dos jogadores são transferidos/consolidados para o SaldoGlobalAcumulado em seus PerfisDeJogador.

-   Controle de Fichas em Jogo (Valor Total): ValorTotalFichasEmJogo = Soma(ValorUnitario_Ficha * QuantidadeAtual_Ficha) para todas as definições de fichas da sessão. Este valor deve, idealmente, corresponder à soma dos saldos em jogo de todos os jogadores (Soma(SaldoAtualEmJogo_Jogador)).

-   Validação de Entradas:
    -   Nomes de sessão e jogador são obrigatórios.
    -   Valores monetários devem ser numéricos e positivos.
    -   Um jogador não pode ser adicionado duas vezes à mesma sessão.
    -   Ao registrar transações, o jogador deve ser selecionado.

-   Autenticação/Autorização (Conceitual):
    -   Um sistema de login para o organizador é fundamental.
    -   O organizador só pode ver e gerenciar os dados (Caixas, Sessões, Perfis de Jogadores) que ele criou ou aos quais tem permissão.

## 6. Componentes da Interface e Fluxos de Usuário

### Componente de Layout Principal:

-   UI: Cabeçalho fixo com o nome da aplicação. Menu de navegação principal (ex: Dashboard, Sessão Ativa, Perfis de Jogadores, Configurações). Área de identificação do usuário logado com opção de "Sair".
-   Fluxo: Permite a navegação consistente entre as principais áreas da aplicação.

### Tela: Dashboard (Painel de Controle):

-   UI:
    -   Seção "Sessões Ativas": Lista de sessões com status "Ativa". Cada item mostra nome, data de início. Botões: "Continuar Sessão", "Finalizar Sessão".
    -   Seção "Sessões Finalizadas": Lista de sessões com status "Finalizada". Cada item mostra nome, datas. Botão: "Ver Detalhes".
    -   Botões de Ação Global: "Nova Sessão", "Gerenciar Perfis de Jogadores".
    -   (Opcional) Botão "Resetar Dados da Aplicação".
-   Fluxo:
    -   Ao clicar em "Nova Sessão": Abre um diálogo/formulário para inserir o nome da nova sessão. Ao confirmar, a sessão é criada, torna-se a sessão ativa no Caixa, e o usuário é redirecionado para a "Tela de Gerenciamento de Sessão Ativa".
    -   Ao clicar em "Continuar Sessão": A sessão selecionada torna-se a ativa no Caixa, e o usuário é redirecionado para a "Tela de Gerenciamento de Sessão Ativa".
    -   Ao clicar em "Finalizar Sessão": Um diálogo de confirmação aparece. Ao confirmar, a sessão é marcada como finalizada.
    -   Ao clicar em "Gerenciar Perfis de Jogadores": Navega para a "Tela de Gerenciamento de Perfis de Jogadores".

### Tela: Gerenciamento de Sessão Ativa:

-   UI:
    -   Cabeçalho da Sessão: Nome da sessão, data/hora de início.
    -   Área de Ações Rápidas Globais: Botões "Adicionar Jogador à Sessão", "Registrar Buy-in (genérico)", "Registrar Cashout (genérico)", "Registrar Pagamento (genérico)".
    -   Lista de Jogadores na Sessão:
        -   Cada item: Nome do jogador, Saldo Atual em Jogo (pode ser ocultável), Saldo Pendente na Sessão (pode ser ocultável).
        -   Botões de Ação por Jogador: "Buy-in", "Cashout", "Pagamento", "Ver Transações do Jogador", "Imprimir Recibo".
    -   Pé de Página Colapsável (ou seções laterais):
        -   Aba/Seção "Resumo Financeiro da Sessão": Total Buy-ins, Total Cashouts, Dinheiro Total em Jogo, Pendências Totais (a receber vs. a pagar pela casa). Valores ocultáveis.
        -   Aba/Seção "Resumo do Caixa da Sessão": Saldo por método de pagamento (Dinheiro, PIX, Cartão). Valores ocultáveis.
        -   Aba/Seção "Fichário da Sessão": Lista de tipos de fichas com valor e quantidade. Valor total em fichas. Botão "Gerenciar Fichas".
        -   Aba/Seção "Log da Sessão": Botão "Ver Log Completo da Sessão".
    -   Botões de Controle Global da Tela: "Ocultar/Mostrar Todos os Valores" (com senha), "Finalizar Sessão".
-   Fluxo:
    -   "Adicionar Jogador": Abre "Diálogo: Adicionar Jogador".
    -   "Registrar Buy-in/Cashout/Pagamento" (genérico ou por jogador): Abre "Diálogo: Registrar Transação".
    -   "Ver Transações do Jogador": Abre "Diálogo: Histórico de Transações do Jogador na Sessão".
    -   "Gerenciar Fichas": Abre "Diálogo: Gerenciar Fichário".
    -   "Ver Log Completo": Abre "Diálogo: Log de Atividades da Sessão".

### Tela: Gerenciamento de Perfis de Jogadores (Global):

-   UI:
    -   Campo de Busca de Jogadores.
    -   Botão "Cadastrar Novo Perfil de Jogador".
    -   Lista de Perfis de Jogadores:
        -   Cada item: Nome, Apelido, Saldo Global Acumulado.
        -   Botões de Ação: "Editar Perfil", "Excluir Perfil", "Ver Detalhes do Histórico".
-   Fluxo:
    -   "Cadastrar Novo Perfil": Abre "Diálogo: Criar/Editar Perfil de Jogador".
    -   "Editar Perfil": Abre "Diálogo: Criar/Editar Perfil de Jogador" pré-preenchido.
    -   "Excluir Perfil": Diálogo de confirmação.
    -   "Ver Detalhes": Navega para "Tela: Detalhes do Perfil do Jogador".

### Tela: Detalhes do Perfil do Jogador (Histórico Global):

-   UI:
    -   Informações do Perfil: Nome, apelido, contato, PIX, limite de crédito.
    -   Resumo Financeiro Global: Saldo Global Acumulado, Total Buy-ins Histórico, Total Cashouts Histórico.
    -   Lista de Sessões Participadas: Data, nome da sessão, resultado financeiro naquela sessão.
    -   (Opcional) Lista de todas as transações globais do jogador.
    -   Botão "Editar Perfil".
-   Fluxo: Similar à edição da tela anterior.

### Diálogos Comuns (Modais/Pop-ups):

-   Diálogo: Nova Sessão:
    -   Campo: Nome da Sessão. Botões: "Criar", "Cancelar".
-   Diálogo: Adicionar Jogador à Sessão:
    -   Abas: "Buscar Jogador Existente", "Criar Novo Perfil Rápido".
    -   Aba Buscar: Campo de busca, lista de resultados (Perfis de Jogador). Botão "Adicionar Selecionado".
    -   Aba Criar Novo: Campo para Nome. Botão "Criar e Adicionar".
-   Diálogo: Registrar Transação (Buy-in / Cashout / Pagamento):
    -   Campo: Selecionar Jogador (se a ação foi genérica, senão já vem preenchido).
    -   Campo: Valor (Numérico).
    -   Campo: Selecionar Método de Pagamento.
    -   Checkbox: "Pagamento Imediato?" (Sim/Não).
    -   (Para Pagamentos): Selecionar Direção (Entrada no Caixa / Saída do Caixa).
    -   Botões: "Confirmar", "Cancelar".
-   Diálogo: Gerenciar Fichário da Sessão:
    -   Lista de tipos de fichas (campos para cor, valor unitário, quantidade inicial, quantidade atual).
    -   Botão "Adicionar Novo Tipo de Ficha". Botão "Salvar Fichário".
-   Diálogo: Histórico de Transações (Jogador na Sessão ou Log Global):
    -   Lista filtrável de transações/logs. Colunas: Data/Hora, Tipo, Descrição, Valor.
    -   Opções de Filtro: Por tipo de evento, por data.
-   Diálogo: Senha para Ocultar/Mostrar Valores:
    -   Campo: Senha. Botões: "Aplicar", "Cancelar".
-   Diálogo: Confirmação (Genérico):
    -   Mensagem de confirmação. Botões: "Confirmar", "Cancelar".
-   Diálogo: Impressão de Recibo do Jogador:
    -   Preview do recibo: Nome do Jogador, Nome da Sessão, Data. Lista de Buy-ins, Cashouts, Pagamentos. Saldo final na sessão.
    -   Botão "Imprimir".

## 7. Elementos de Interface Específicos Notáveis

-   Cartões de Jogador (Player Cards): Usados na tela de sessão ativa para exibir informações de cada jogador de forma concisa, com acesso rápido a ações.
-   Indicadores de Saldo com Cores: Saldos positivos em verde, negativos em vermelho, neutros em cinza/branco.
-   Botões de Ação Rápida com Ícones: Para Buy-in (+), Cashout (-), Pagamento ($), Adicionar Jogador (ícone de usuário+), etc.
-   Pé de Página Colapsável: Maximiza o espaço útil na tela de sessão, mostrando resumos e controles adicionais apenas quando expandido.
-   Abas (Tabs): Para organizar diferentes seções de informação ou formulários complexos (ex: no diálogo de adicionar jogador).
-   Campos de Input com Validação em Tempo Real (ou ao submeter): Fornecem feedback imediato sobre erros de entrada.
-   Notificações/Alertas: Mensagens flutuantes ou fixas para informar sucesso, erro ou avisos.

## 8. Considerações Adicionais para Recriação

-   Persistência de Dados: Definir como e onde os dados (Caixa, Sessões, Perfis, Transações, Logs) serão armazenados de forma duradoura.
-   Gerenciamento de Estado da Interface: Como as informações são mantidas e atualizadas na tela conforme o usuário interage e os dados mudam. Isso inclui o estado local dos componentes e o estado global da aplicação (ex: qual a sessão ativa, quem é o usuário logado).
-   Responsividade: A interface deve ser utilizável em diferentes tamanhos de tela (desktops, tablets, potencialmente celulares).
-   Feedback ao Usuário: O sistema deve fornecer feedback claro para todas as ações:
    -   Indicadores de carregamento para operações demoradas.
    -   Mensagens de sucesso claras após uma operação bem-sucedida.
    -   Mensagens de erro detalhadas e úteis quando algo falha.
-   Tratamento de Erros: Estratégias para lidar com falhas de validação, problemas de comunicação com a persistência de dados, etc.

Este detalhamento visa fornecer uma base sólida e conceitual para a recriação da aplicação Poker Cash Manager, independentemente da pilha tecnológica escolhida.