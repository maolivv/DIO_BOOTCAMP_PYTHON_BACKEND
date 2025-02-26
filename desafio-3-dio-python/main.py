from abc import ABC, abstractmethod
from datetime import date
import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta:Conta):
        pass


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao:Transacao):
        self.transacoes.append(transacao)


class Deposito(Transacao):
    def __init__(self,valor:float):
        self.valor = valor
        super().__init__()

    def registrar(self, conta:Conta):
        print(f'Deposito de {self.valor} realizado com sucesso')
        conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self,valor:float):
        self.valor = valor
        super().__init__() 

    def registrar(self, conta:Conta):
        print(f'Saque de {self.valor} realizado com sucesso')
        conta.historico.adicionar_transacao(self)


class Cliente:
    def __init__(self):
        self.endereco = ""
        self.contas = []

    def realiza_transacao(self, conta:Conta, transacao:Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta:Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:date):
        super().__init__()
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento