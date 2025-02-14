class Aluno: #Criando a classe do aluno
    def __init__(self, nome: str, matricula: int, notas: float): #Atribuindo os atributos para a classe do alunk
        self.nome = nome #Criando o valor nome para a instância nome
        self.matricula = matricula #Criando o valor matricula para a instância matricula
        self.notas = notas #Criando o valor notas para a instância notas

    def notaAluno(self): #Método de nota do aluno
        nota1 = input("Digite a primeira nota: ") #O usuário vai inserir a primeira nota
        nota1 = float(nota1) #Transformando a variável nota1 em float

        nota2 = input("Digite a segunda nota: ") #O usuário vai inserir a segunda nota
        nota2 = float(nota2) #Transformando a variável nota2 em float

        self.notas = (nota1 + nota2) / 2 #Calculando a média das notas

        print(f"Nota final: {self.notas: .2f}") #Exibindo a nota final na tela

        self.situacaoAluno() #Chamando a função da situação do aluno

    def situacaoAluno(self): #Método da situação do aluno
        if self.notas <= 10 and self.notas >= 6: #Se o usuário tirou notas boas...
            print("Parabéns! Você passou de ano!") #Exibindo a mensagem de aviso no terminal
        elif self.notas < 6 and self.notas >= 5: #Se o usuário tirou nota média...
            print("Por pouco! Você irá para a recuperação.") #Exibindo a mensagem de aviso no terminal
        elif self.notas < 5: #Se o usuário tirou nota baixa...
            print("Sinto muito! Você foi reprovado.") #Exibindo a mensagem de aviso no terminal
    
media = Aluno("Lucas", 95385390, 0) #Nome, número da matrícula, notas

media.notaAluno() #Iniciando a função de nota