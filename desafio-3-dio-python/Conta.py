from main import Cliente, Historico, Saque, Deposito

class Conta:
    def __init__(self, agencia:str=None, numero:str=None, saldo:float=0.0, cliente:Cliente=None, historico:Historico=None):
        self.historico = historico
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def saldo(self):
        return self.saldo
    
    def nova_conta(self, numero:str, cliente:Cliente):
        return Conta(numero, cliente)
    
    def sacar (self, valor:float):
        if valor > self.saldo:
            print('Saldo insuficiente')
            return False
        else:
            self.saldo -= valor
            Saque(valor).registrar(self)
            return True
        
    def depositar(self, valor:float):
        self.saldo += valor
        Deposito(valor).registrar(self)
        return True
    

class ContaCorrente(Conta):
    def __init__(self, agencia:str=None, numero:str=None, saldo:float=0.0, cliente:Cliente=None, historico:Historico=None, limite:float=0.0, limite_saques:int=0):
        super().__init__(agencia, numero, saldo, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
