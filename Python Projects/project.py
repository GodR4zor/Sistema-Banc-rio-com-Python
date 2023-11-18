menu = """
Qual ação deseja realizar:

[1] Depoisto
[2] Saque
[3] Extrato
[4] Sair    
    
    """

MAX_VALUE = 500

saldo = 0
valor = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUE = 3

while True:
    print(menu)

    chose = input("Digite o número da ação que deseja realizar: ")

    if chose == 1 or chose == "1":
        valor = input("Digite o valor que deseja depositar: ")
        try:
            valor = float(valor)
            if valor > 0:
                extrato += f"⬆🟢 Deposito Realizado: R$ {valor:.2f}\n"
                saldo += valor
                print(f"Deposito Realizado: R$ {valor:.2f}")
            else:
                print("Valor inválido!")
        except:
            print("\nDigite um valor númerico!")
    elif chose == 2 or chose == "2":
        if saques < LIMITE_SAQUE:
            valor = input("Digite o valor que deseja sacar: ")
            try:
                valor = float(valor)
                if valor > 0 and valor <= MAX_VALUE and valor <= saldo:
                    extrato += f"⬇🔴 Saque Realizado: R$ -{valor:.2f}\n"
                    saldo -= valor
                    saques += 1
                    print(f"Saque Realizado: R$ -{valor:.2f}")
                elif valor > saldo:
                    print("\nSaldo insuficiente!")
                else:
                    print("\nValor digitado inválido!")
            except:
                print("\nDigite um válor válido!")
        else:
            print("Limite de saques diário atingido!")
    elif chose == 3 or chose == "3":
        print("============== EXTRATO ==============")
        print(extrato)
        print(f"💲 Saldo: R$ {saldo:.2f}")
        print("=====================================")
    elif chose == 4 or chose == "4":
        break
    else:
        print("Opção inválida!\nDigite o numero de uma opção valida.")
