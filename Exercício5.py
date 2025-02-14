class Funcionario: #Criando a classe funcionário
    def __init__(self, nome: str, salario: float, cargo: str): #Atribuindo os atributos para a classe funcionário
        self.nome = nome #Atribuindo o valor nome para a instância nome
        self.salario = salario #Atribuindo o valor salario para a instância salario
        self.cargo = cargo #Atribuindo o valor cargo para a instância cargo

    def salarioLiquido(self): #Método do salário
        imposto = 5 / 100 #Calculando o imposto do salário

        beneficio = 20 / 100 #Calculando o benefício do salário

        salario = self.salario + beneficio - imposto #Calculando o salário

        print(f"O seu salário final será de: {salario}") #Exibindo o salário no terminal

salarioFuncionario = Funcionario("Lucas", 1520, "Jovem aprendiz de soluções digitais") #Nome, salário, cargo

salarioFuncionario.salarioLiquido() #Iniciando o método de salário