class ContaBanco:
    def __init__(self):
        self.saldo = 0.00
        self.extrato_bancario = '#################EXTRATO################\n'
        self.limite_de_saques = 3
        self.numero_de_saques = 0
        self.limite_por_saque = 500.00
        

    def CriarUsuario(nome, data_nascimento, cpf, endereco, lista_usuarios):
        usuario = {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'endereço': endereco,
        }

        if usuario['cpf'].isdigit():
            if lista_usuarios != []:
                for user in lista_usuarios:
                    if user['cpf'] == cpf:
                        print('\nUsuario ja cadastrado.\n')
                        break
                    else:
                        lista_usuarios.append(usuario)
                        print('\nUsuario criado com sucesso!\n')
                        print(f'\nUsuario: {usuario}')
                        break
            else:
                lista_usuarios.append(usuario)
                print('\nUsuario criado com sucesso!\n')
            
        else:
            print('Formato de CPF errado.\n')
            
    

    def CriarConta(nmr_da_conta: str, cpf_usuario, lista_usuarios, lista_contas):
        nova_conta = {
            'agencia': '0001',
            'numero_conta': nmr_da_conta,
            'usuario': dict(),
        }
        iteracao = 1
        for n in nmr_da_conta:
            if n != '1' and iteracao == 1:
                print('\nNumero da conta deve começar com digito 1\n')
                break
            else:
                iteracao += 1
                break
        for user in lista_usuarios:
            if str(cpf_usuario).isdigit():
                if user['cpf'] == cpf_usuario:
                    nova_conta['usuario'] = user
                    iteracao += 1
                    break
            else:
                print('\nFormato de CPF errado.\n')
                break
        if iteracao == 3:
            lista_contas.append(nova_conta)
            print('\nConta criada com sucesso!\n')
            print(f'Conta: {nova_conta}')
        else:
            print('\nErro ao criar usuario.\n')

    def Deposito(self, valor):
        if valor.isdigit():
            v = float(valor)
            if v >= 0.0:
                self.saldo += v
                print('\n########### Deposito realizado com sucesso. ###########')
                self.Extrato(f'Deposito realizado no valor de R$ {v:.2f}\n')
            else:
                print('\nValor negativo é invalido.\n')
        else:
            print('Entrada inválida.')

    def Saque(self, valor):
        if valor.isdigit():
            v = float(valor)
            if self.saldo > v and self.numero_de_saques < self.limite_de_saques:
                if v <= self.limite_por_saque:
                    self.saldo -= v
                    self.numero_de_saques += 1
                    print('\n########### Saque realizado com sucesso. ###########')
                    self.Extrato(f'Saque realizado no valor de R$ {v:.2f}\n')
                else:
                    print(f'Valor muito alto. Seu limite de saque é de R$ {self.limite_por_saque:.2f}')
            else:
                print(f'####\nImpossivel realizar a operação.\nSaldo insuficiente ou o número de saques por dia foi excedido.\nSaques utilizados:{self.numero_de_saques}/{self.limite_de_saques}\n####')
        else:
            print('Operação não pode ser realizada. Valor invalido.')




    def Extrato(self, entrada):
        self.extrato_bancario += entrada
        return (self.extrato_bancario + f'\nSaldo atual: R$ {self.saldo:.2f}\n################EXTRATO#################\n')