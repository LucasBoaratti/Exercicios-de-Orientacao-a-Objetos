class Circulo: #Criando a classe círculo
    def __init__(self, raio: float): #Criando a função com o atributo de raio
        self.raio = raio #Obs: Sempre colocar π = 3 (valor fixo para o pi)
        self.pi = 3 #Definindo o valor de pi

    def area(self): #Criando a função da área que recebe o parâmetro self
        areaCirculo = self.pi * (self.raio ** 2) #Calculando a área do círculo
 
        print(f"A área do círculo é: {areaCirculo}m²") #Exibindo a área do círculo na tela
    
    def perimetro(self): #Criando a função do perímetro que recebe o parâmetro self
        perimetroCirculo = 2 * self.pi * self.raio #Calculando o perímetro do círculo 

        print(f"O perímetro do círculo é: {perimetroCirculo}") #Exibindo o perímetro do círculo na tela
    
raio1 = Circulo(5) #(pi, raio)

raio1.area() #Exibindo a função área na tela
raio1.perimetro() #Exibindo a função área na tela