# Sistema de Banco Simples

Este é um sistema de banco simples em Python que permite ao usuário realizar depósitos, saques e visualizar o extrato das transações.

## Funcionalidades

- **Depósito:** Permite ao usuário depositar um valor positivo na conta.
- **Saque:** Permite ao usuário sacar um valor da conta, respeitando o limite de saques diários e o limite de valor por saque.
- **Extrato:** Exibe o histórico de transações e o saldo atual da conta.
- **Sair:** Encerra o programa.

## Como Utilizar

1. **Executar o Programa:**
   Execute o script Python em um terminal ou ambiente de desenvolvimento que suporte entrada de dados pelo teclado.

2. **Menu Principal:**
   Ao iniciar o programa, você verá o menu principal com as seguintes opções:

3. **Depósito:**
- Selecione a opção `1`.
- Insira o valor do depósito.
- O valor será adicionado ao saldo da conta, e a operação será registrada no extrato.

4. **Saque:**
- Selecione a opção `2`.
- Insira o valor do saque.
- O valor será deduzido do saldo da conta, e a operação será registrada no extrato, respeitando os limites estabelecidos:
  - Limite de saques diários: 3 saques.
  - Limite de valor por saque: R$ 500,00.
  - O saque não pode exceder o saldo disponível.

5. **Extrato:**
- Selecione a opção `3`.
- O extrato será exibido, mostrando todas as operações realizadas (depósitos e saques) e o saldo atual da conta.

6. **Sair:**
- Selecione a opção `0` para encerrar o programa.
