class Retangulo: #Criando a classe do retângulo
    def __init__(self, largura: float, altura: float): #Atribuindo os atributos para a classe retângulo
        self.largura = largura #Atribuindo o valor largura para a instância largura
        self.altura = altura #Atribuindo o valor altura para a instância altura
 
    def escolha(self): #Método de escolha 
        escolha = input("Escolha o que você deseja calcular (área ou perímetro): ").lower() #O usuário vai escolher o que quer calcular

        if escolha == "area" or escolha == "área": #Se o usuário quer calcular a área...
            self.area() #Chamando a função de área
        elif escolha == "perimetro" or escolha == "perímetro": #Se o usuário quer calcular o perímetro
            self.perimetro() #Chamando a função do perímetro
        else: #Caso o usuário digite algo errado...
            print("Digite uma opção válida!") #Exibindo a mensagem de erro no terminal

    def area(self): #Método de área
        areaRetangulo = self.largura * self.altura #Calculando a área do retângulo

        print(f"A área do retângulo é: {areaRetangulo}m²") #Exibindo a área do retângulo no terminal 

    def perimetro(self): #Método do perímetro
        perimetro = self.largura + self.altura + self.largura + self.altura #Calculando o perímetro do retângulo

        print(f"O perímetro do retângulo é: {perimetro}m") #Exibindo o perímetro do retângulo no terminal

calculo = Retangulo(15, 10) #Largura, altura

calculo.escolha() #Iniciando o método de escolha