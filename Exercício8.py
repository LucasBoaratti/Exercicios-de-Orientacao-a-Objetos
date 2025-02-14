class Carro: #Criando a classe carro
    def __init__(self, marca: str, modelo: str, velocidade: int): #Atribuindo os atributos para a classse carro
        self.marca = marca #Atribuindo o valor marca para a instância marca
        self.modelo = modelo #Atribuindo o valor modelo para a instância modelo
        self.velocidade = velocidade #Atribuindo o valor velocidade para a instância velocidade

    def acelerar(self): #Método de acelerar
        self.velocidade += 1 #Aumentando a velocidade do carro

        print(f"Sua velocidade: {self.velocidade}") #Exibindo a velociade atual no terminal

        self.velocidadeAtual() #Chamando a função da velocidade atual

    def freiar(self): #Método para freiar
        self.velocidade -= 1 #Diminuindo a velocidade do carro

        print(f"Sua velocidade: {self.velocidade}") #Exibindo a velociade atual no terminal

        self.velocidadeAtual() #Chamando a função da velocidade atual

    def velocidadeAtual(self): #Método da velocidade atual
        print(f"Sua velocidade atual: {self.velocidade}km/h") #Exibindo a velociade atual no terminal

        acelerar = input("Você deseja acelerar? (Digite sim ou não): ").lower() #O usuário vai decidir se quer acelerar
 
        if acelerar == "sim" or acelerar == "s": #Verificando se o usuário quer acelerar 
            self.acelerar() #Chamando a função de acelerar
        elif acelerar == "nao" or acelerar == "não" or acelerar == "n": #Se ele não quiser acelerar...
            freiar = input("Então você deseja freiar? (Digite sim ou não): ").lower() #O usuário vai decidir se quer freiar

            if freiar == "sim" or freiar == "s": #Verificando se o usuário quer freiar
                self.freiar() #Chamando a função de freiar
            elif freiar == "nao" or freiar == "não" or freiar == "n": #Se ele não quiser freiar...
                self.velocidadeAtual() #Chamando a função de velocidade atual
            else: #Caso a resposta não sejá válida...
                print("Digite uma resposta válida!") #Exibindo a mensagem de aviso no terminal
        else: #Caso a resposta não sejá válida...
            print("Digite uma resposta válida!") #Exibindo a mensagem de aviso no terminal

carro = Carro("Fiat", "Uno", 300) #Marca, modelo, velocidade

carro.velocidadeAtual() #Iniciando a função de velocidade atual