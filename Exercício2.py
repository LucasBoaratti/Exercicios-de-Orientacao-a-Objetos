class ContaBancaria: #Criando a classe da conta bancária
    def __init__(self, nome: str, numero: int, saldo: float): #Criando a função para atribuir o nome, número da conta e o saldo
        self.nome = nome #Atribuindo o valor nome para a instância nome
        self.numero = numero #Atribuindo o valor numero para a instância numero 
        self.saldo = saldo #Atribuindo o valor saldo para a instância saldo

    def escolha(self): #Método de escolha do usuário
        escolhaUsuario = input("Você quer depositar ou sacar?: ").lower() #O usuário vai escolher a opção de depositar ou sacar
 
        if escolhaUsuario == "depositar": #Se o usuário escolher depositar...
            self.depositar() #Chama a função depositar para o usuário
        elif escolhaUsuario == "sacar": #Se o usuário escolher sacar...
            self.sacar() #Chama a função sacar para o usuário
        else: #Caso o usuário digite algo errado...
            print("Digite uma opção válida!") #Exibindo uma mensagem de erro

    def depositar(self): #Método de deposito
        deposito = input("Digite a quantidade que deseja depositar: ") #O usuário vai inserir a quantidade que deseja depositar
        deposito = float(deposito) #Transformando a variável deposito em float

        adicionarDinheiro = deposito + self.saldo #Cálculo de adicionar dinheiro a conta

        print(f"Foi depositado {deposito} na sua conta. Seu saldo agora é de {adicionarDinheiro}") #Exibindo a quantidade de dinheiro depositado e o saldo no terminal
    
    def sacar(self): #Método de sacar
        saque = input("Digite a quantidade que deseja sacar: ") #O usuário vai digitar o quanto ele quer sacar
        saque = float(saque) #Transformando a variável saque em float

        retirarDinheiro = self.saldo + saque #Cálculo de retirar dinheiro da conta

        print(f"Foi retirado {saque} da sua conta. Seu saldo agora é de {retirarDinheiro}") #Exibindo a quantidade de dinheiro sacado e o saldo no terminal
    
conta1 = ContaBancaria("Lucas", 82475, 10000) #Nome, numero da conta, saldo

conta1.escolha() #Iniciando o método de escolha