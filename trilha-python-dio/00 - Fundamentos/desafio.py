menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        
        if numero_saques >= LIMITE_SAQUES:
            print("Número de saques diários excedido.")
        elif valor > limite:
            print(f"Valor de saque excede o limite de R$ {limite:.2f}.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        print("Operação finalizada. Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
