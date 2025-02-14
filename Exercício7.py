class Triangulo: #Criando a classe do triângulo
    def __init__(self, lado1: float, lado2: float, lado3: float): #Atribuindo os atributos para a classe triangulo
        self.lado1 = lado1 #Lado1
        self.lado2 = lado2 #Base (lado2)
        self.lado3 = lado3 #Lado3

        #Lados do triângulo: / -> lado1 ; _ -> lado2 ; \ -> lado3

    def area(self): #Método da área
        if self.lado1 != 0 and self.lado2 != 0 and self.lado3 != 0: #Verificando se o usuário não colocou nenhum lado do triângulo como 0
            altura = (3 ** 0.5) * self.lado1 / 2 #Calculando a altura do triângulo
        
            areaTriangulo = (self.lado2 * altura) / 2 #Calculando a área do triângulo

            print(f"A área do triângulo é: {areaTriangulo: .2f}m²") #Exibindo a área do triângulo no terminal

trianguloEquilatero = Triangulo(5, 5, 5) #Todos os lados iguais 
trianguloIsosceles = Triangulo(5, 4, 5) #Dois lados iguais e um diferente
trianguloEscaleno = Triangulo(5, 4, 3) #Todos os lados diferentes
 
trianguloEquilatero.area() #Iniciando a função da área
trianguloIsosceles.area() #Iniciando a função da área
trianguloEscaleno.area() #Iniciando a função da área