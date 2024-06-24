from conta import ContaBanco

conta_usuario = ContaBanco()

while True:
    menu = input('''
    O que voce deseja fazer?
        1 - Deposito\n
        2 - Saque\n
        3 - Extrato\n
        4 - Sair\n
            ''')
    match menu:
        case '1':
            valor = input('Qual valor deseja depositar?\n')
            conta_usuario.Deposito(valor)
        case '2':
            valor = input('Qual valor deseja sacar?\n')
            conta_usuario.Saque(valor)
        case '3':
            extrato = conta_usuario.Extrato('')
            print(extrato)
        case '4':
            break
        case _:
            print('\nFim.\n')

