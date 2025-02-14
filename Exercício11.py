import random

class Banco:
    def __init__(self, nome: str, email: str, senha: str, numero: int, cpf: str, saldo: float):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.numero = numero
        self.cpf = cpf
        self.saldo = saldo

    def cadastrarClientes(self):
        print("Olá, seja bem-vindo ao banco do Lucas. Coloque seus dados para abrir uma conta.")

        self.nome = input("Digite seu nome: ")

        self.email = input("Digite seu E-Mail: ")

        self.senha = input("Digite sua senha: ")

        self.cpf = input("Digite seu CPF: ")

        print("Obrigado por se cadastrar no banco do Lucas!")

        self.numero = random.randint(10000, 99999)

        abrirConta = input("Você gostaria de abrir sua conta? (Digite sim ou não): ").lower()

        if abrirConta == "sim" or abrirConta == "s":
            print("Muito bem, agora vamos abrir sua conta!")

            self.abrirConta()
        elif abrirConta == "nao" or abrirConta == "não" or abrirConta == "n":
            print("Tudo bem... Estarei a sua espera.")
            exit
        else:
            print("Por favor, digite uma resposta válida.")
        
    def abrirConta(self):
        print(f"Seu número de conta é: {self.numero}")

        operacoes = input("Você deseja realizar alguma operação? (Digite sim ou não): ").lower()

        if operacoes == "sim" or operacoes == "s":
            tipoOperacao = input("Que bom! Qual operação você deseja realizar? 1 - Saque; 2 - Deposito; 3 - Transferência: ")
            tipoOperacao = int(tipoOperacao)

            if tipoOperacao == 1:
                print("Ok, você será redirecionado para a operação de realizar saque.")

                self.realizarSaque()
            elif tipoOperacao == 2:
                print("Ok, você será redirecionado para a operação de realizar depósito.")

                self.realizarDeposito() 
            elif tipoOperacao == 3:
                print("Ok, você será redirecionado para a operação de realizar transferências.")

                self.realizarTransferencia()
            else:
                print("Por favor, digite uma opção válida.")
        elif operacoes == "não" or operacoes == "nao" or operacoes == "n":
            print("Ok... Até mais.")
            exit
        else:
            print("Por favor, digite um número válida.")

    def realizarSaque(self):
        print("Olá, seja bem vindo a área de saque. Preencha as informações abaixo para realizá-lo.")

        numeroConta = input("Digite o número da sua conta: ")
        numeroConta = int(numeroConta)

        if numeroConta == self.numero:
            saque = input(f"Olá, {self.nome}, o quanto você deseja sacar?: ")
            saque = float(saque)

            retirarDinheiro = self.saldo - saque

            print(f"Foi retirado {saque} da sua conta. Seu saldo agora é de {retirarDinheiro}")
            print("Você será redirecionado para a tela de início.")

            self.abrirConta()
        else:
            print("Desculpe, mas esse número de conta não existe.")
    
    def realizarDeposito(self):
        print("Olá, seja bem vindo a área de depósito. Preencha as informações abaixo para realizá-lo.")

        numeroConta = input("Digite o número da sua conta: ")
        numeroConta = int(numeroConta)

        if numeroConta == self.numero:
            depositar = input(f"Olá, {self.nome}, o quanto você deseja depositar?: ")
            depositar = float(depositar)

            adicionarDinheiro = self.saldo + depositar

            print(f"Foi adicionado {depositar} da sua conta. Seu saldo agora é de {adicionarDinheiro}")
            print("Você será redirecionado para a tela de início.")

            self.abrirConta()
        else:
            print("Desculpe, mas esse número de conta não existe.")

    def realizarTransferencia(self):
        print("Olá, seja bem vindo a área de transferência. Preencha as informações abaixo para realizá-lo.")

        numeroConta = input("Digite o número da sua conta: ")
        numeroConta = int(numeroConta)

        if numeroConta == self.numero:
            transferirConta = input(f"Olá, {self.nome}, Digite o número da conta para qual você queira transferir: ")
            transferirConta = int(transferirConta)

            transferir = input(f"Digite o quanto você deseja transferir para a conta?: ")
            transferir = float(transferir)

            transferirDinheiro = self.saldo - transferir

            print(f"Foi retirado {transferir} da sua conta. Seu saldo agora é de {transferirDinheiro}")
            print("Dinheiro depositado em outra conta com sucesso!")
            print("Você será redirecionado para a tela de início.")

            self.abrirConta()
        else:
            print("Desculpe, mas esse número de conta não existe.")

saldo = Banco("", "", "", 0, "", 10000)

saldo.cadastrarClientes()