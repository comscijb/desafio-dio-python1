menu = """Seja bem-vindo(a)!
Menu princial
Selecione uma opção:
[1]Depósito
[2]Saque
[3]Extrato
[0]Sair\n"""

saldo = 0
limite_por_saque = 500
extrato = []
saques_no_dia = 0
LIMITE_DE_SAQUES = 3

while True:
    option = int(input(menu))
    
    if option == 1:
        valor_deposito = float(input("Qual o valor do depósito? "))
        
        if valor_deposito <= 0:
            print("Operação inválida. Por favor, insira um valor positivo.")
            
        else:
            saldo += valor_deposito
            extrato.append(valor_deposito)
            print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
    
    elif option == 2:
        valor_saque = float(input("Qual o valor do saque? "))
        
        if saques_no_dia >= LIMITE_DE_SAQUES:
            print("Limite de saques diários excedido. Operação cancelada!")
            
        elif valor_saque > limite_por_saque:
            print(f"Saque maior que o valor máximo permitido por saque. Valor maximo: R$ {limite_por_saque}")
            
        elif valor_saque > saldo:
            print(f"Saldo insuficiente. Valor disponível: R$ {saldo}")
            
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato.append(-valor_saque)
            saques_no_dia += 1
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
            
        else:
            print("Operação inválida. O valor informado é inválido!")

    elif option == 3:
        print("\nExtrato:\n")
        
        if len(extrato) == 0:
            print("Nenhuma operação realizada.")
            
        else:
            for operacao in extrato:
                if operacao > 0:
                    print(f"Depósito R$ +{operacao:.2f}")
                else:
                    print(f"Saque R$ {operacao:.2f}")
                    
        print(f"\nSaldo: R$ {saldo:.2f}\n")

    elif option == 0:
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Operação inválida. Por favor, tente novamente.")