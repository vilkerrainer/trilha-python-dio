saldo = 0
depositos = []
saques = []
opcao = 99

def deposito(valor):
    global saldo, depositos
    if valor > 0:
        saldo += valor
        depositos += [valor]
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('O valor do depósito deve ser positivo.')

def saque(valor):
    global saldo, saques
    if saldo >= valor and valor <= 500 and len(saques) < 3:
        saldo -= valor
        saques += [valor]
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    elif saldo < valor:
        print('Saldo insuficiente para realizar o saque.')
    elif valor > 500:
        print('O valor do saque deve ser de no máximo R$ 500.00.')
    else:
        print('Limite máximo de saques atingido.')
        
def extrato():
    print('Extrato:')
    if len(depositos) == 0 and len(saques) == 0:
        print('Não foram realizadas movimentações.')
    else:
        for deposito in depositos:
            print(f'Depósito: R$ {deposito:.2f}')
        for saque in saques:
            print(f'Saque: R$ {saque:.2f}')
    print(f'Saldo atual: R$ {saldo:.2f}')

print("\nBem vindo ao Sistema Bancário Dio")
print("Por favor, utilize seguinte o Menu:")
while opcao != 0:
    try:
        opcao = int(input("Menu Bancário Dio:\n[1] Sacar\n[2] Depósito\n[3] Extrato\n[0] Sair\n: "))
        if opcao == 1:
            print('Sacando...')
            valor = float(input('Informe o valor do saque: '))
            saque(valor)
        elif opcao == 3:
            print('Exibindo o extrato...')
            extrato()
        elif opcao == 2:
            print('Realizando depósito...')
            valor = float(input('Informe o valor do depósito: '))
            deposito(valor)
        elif opcao == 0:
            print('Obrigado por usar o sistema bancário DIO. Até logo!')
        else:
            print('Opção inválida. Tente novamente.')
    except ValueError:
        print('Opção inválida. Tente novamente.')
