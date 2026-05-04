import random

class Conta:
    # Método construtor: cria um objeto conforme a necessidade do usuário
    def __init__(self,titular,cpf,limite,chave_pix, senha):
        # Atributos:
        self.titular = titular
        self.cpf = cpf
        self.agencia = 2026
        self.conta = random.randint(100000,999999)
        self.saldo = 0
        self.limite = limite
        self.chave_pix = chave_pix
        self.senha = senha

        
    def mostrar(self):
        print(f'''Titular: {self.titular}
                 \nAgência: {self.agencia} 
                 \nConta: {self.conta}''')                           
