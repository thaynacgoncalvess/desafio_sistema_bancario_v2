# Sistema Bancário Otimizado

Este projeto é uma versão aprimorada de um sistema bancário simples, implementado em Python. Ele permite ao usuário realizar diversas operações bancárias, incluindo depósito, saque, consulta de extrato, e gerenciamento de usuários e contas correntes. O sistema foi otimizado com o uso de funções Python para facilitar a manutenção e a escalabilidade do código.

## Funcionalidades

- **Saque:** Permite ao usuário sacar um valor da conta, com limite diário de transações e valor máximo por saque.
- **Depósito:** Permite ao usuário depositar um valor na conta, com limite diário de transações.
- **Extrato:** Exibe o histórico de transações e o saldo atual da conta.
- **Cadastro de Usuário:** Permite cadastrar novos usuários, incluindo nome, CPF, data de nascimento e endereço.
- **Consulta de Usuários:** Exibe a lista de usuários cadastrados.
- **Cadastro de Conta Corrente:** Permite criar uma nova conta corrente associada a um usuário previamente cadastrado.
- **Consulta de Contas Correntes:** Exibe a lista de contas correntes cadastradas.

## Como Usar

1. **Inicialização:**
   - Ao iniciar o programa, o usuário é saudado e um menu de opções é exibido.

2. **Menu de Operações:**
   - `[1] - SAQUE`: Realiza um saque da conta corrente, respeitando o limite diário de transações e o limite de valor por saque.
   - `[2] - DEPÓSITO`: Realiza um depósito na conta corrente, respeitando o limite diário de transações.
   - `[3] - EXTRATO`: Exibe o extrato da conta corrente, mostrando todas as transações realizadas e o saldo atual.
   - `[4] - CAD. NOVO USUÁRIO`: Cadastra um novo usuário no sistema.
   - `[5] - VER USUÁRIOS`: Exibe a lista de todos os usuários cadastrados.
   - `[6] - CAD. CONTA CORRENTE`: Cadastra uma nova conta corrente para um usuário existente.
   - `[7] - VER CONTAS CORRENTES`: Exibe a lista de todas as contas correntes cadastradas.
   - `[0] - SAIR`: Encerra o programa.

3. **Interação:**
   - O usuário deve escolher a operação desejada digitando o número correspondente.
   - O sistema continuará a operar até que o usuário escolha a opção `0` para sair.

## Requisitos

- Python 3.x instalado.
- Bibliotecas `datetime` e `pytz` (instaladas por padrão com Python).

## Execução

Para executar o sistema, basta rodar o script Python. O menu será exibido, e você poderá interagir com ele conforme as instruções.
