from conta import ContaBanco

lista_usuarios = []
lista_contas = []

conta_usuario = ContaBanco()

while True:
    menu = input('''
    O que voce deseja fazer?
        1 - Deposito\n
        2 - Saque\n
        3 - Extrato\n
        4 - Criar usuario\n
        5 - Criar Conta\n
        6 - Sair\n
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
            nome = input('Qual o nome?\n')
            nascimento = input('Qual a data de nascimento?\n')
            cpf_usuario = input('Qual o CPF? (Apenas numeros)\n')
            endereco = input('Endereço: (logradouro, nº casa, bairro/sigla Estado)\n')
            us = ContaBanco.CriarUsuario(nome=nome, data_nascimento=nascimento, cpf=cpf_usuario, endereco=endereco, lista_usuarios=lista_usuarios)
            print(lista_usuarios)
        case '5':
            numero_da_conta = input('Qual o numero da conta que deseja criar? (Precisa começar com o digito 1)\n')
            cpf_conta = input('Qual CPF do usuario que deseja criar conta?\n')
            ContaBanco.CriarConta(numero_da_conta, cpf_conta, lista_usuarios, lista_contas)
        case '6':
            break
        case _:
            print('\nFim.\n')
