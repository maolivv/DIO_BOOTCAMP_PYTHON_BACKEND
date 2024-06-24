class ContaBanco:
    def __init__(self):
        self.saldo = 0.00
        self.extrato_bancario = '#################EXTRATO################\n'
        self.limite_de_saques = 3
        self.numero_de_saques = 0
        self.limite_por_saque = 500.00


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