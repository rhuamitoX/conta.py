import random
class Conta:
    # Método construtor: cria um objeto conforme a necessidade do usuário
    def __init__(self,titular,cpf,limite,chave_pix, senha):
        # Atributos:
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = 2026
        self.__conta = random.randint(100000,999999)
        self.__saldo = 0
        self.__limite = limite
        self.__chave_pix = chave_pix
        self.__senha = senha
        
    # Encapsulamento (getters e setters)
    # getter do titular
    @property
    def titular(self):
        return self.__titular
    #setter do titular
    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome

    # métodos da classe
    def extrato(self):
        print(f'''Titular: {self.__titular}
                 \nAgência: {self.__agencia} 
                 \nConta: {self.__conta}
                 \nSaldo: {self.__saldo}''')

    def sacar(self,valor):
        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            print("Saque efetuado com sucesso!")
        else:
            print("Não foi possível efetuar o saque! Verifique seu saldo.")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito efetuado com sucesso!")
        else:
            print("Não foi possivel realizar o depósito.")

    def transferir(self, valor, conta_destino):
         self.__sacar(valor)
         conta_destino.depositar(valor)                