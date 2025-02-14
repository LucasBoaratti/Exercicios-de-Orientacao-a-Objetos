class Paciente:
     def __init__(self, nome: str, idade: int, historico: str):
          self.nome = nome
          self.idade = idade
          self.historico = historico
          
     def adicionarConsulta(self):
          nome = input("Digite seu nome: ")
          
          idade = input("Digite sua idade: ")
          idade = int(idade)

          consulta = input("Digite qual consulta você deseja marcar: ")
          
          print(f"Consulta no nome {nome}, que possui {idade} anos, foi marcada!")
          
          self.historico = {
               "Nome": nome, 
               "Idade": idade,
               "Consulta": consulta,
          }
          
          historico = input("Você deseja consultar seu histórico de consultas? (Digite sim ou não): ")
          
          if historico == "sim" or historico == "s":
               self.exibirConsulta()
          elif historico == "nao" or historico == "não" or historico == "n":
               exit
          else:
               print("Digite uma opção válida!")
          
     def exibirConsulta(self):
          print(f"Consultas já realizadas: {self.historico}")
          
paciente = Paciente("", 0, "")

paciente.adicionarConsulta()