class Agenda:
     def __init__(self, nome: str, telefone: str, email: str):
          self.nome = nome
          self.telefone = telefone
          self.email = email
          
     def adicionarContato(self):
          print("Olá, tudo bem? Para adicionar um contato, preencha as informações abaixo.")
          
          self.nome = input("Digite um nome: ")
          
          self.telefone = input("Digite um número de telefone: ")
          
          self.email = input("Digite um E-Mail: ")
          
          contatos = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          print(f"Prontinho! Seu contato foi criado. Verifique como ficou: {contatos}")
          
          opcoes = input("Você deseja editar, remover ou buscar algum contato?: ").lower()
          
          if opcoes == "editar":
               print("Ok, você será redirecionado para página de editar contatos.")
               
               self.editarContato()
          elif opcoes == "remover":
               print("Beleza, você será redirecionado para a página de remover esse contato.")
               
               self.removerContato()
          elif opcoes == "buscar":
               print("Ok, você redirecionado para a página de busca de contato.")
               
               self.buscarContato()
          else:
               print("Por favor, digite uma resposta válida.")
          
     def editarContato(self):        
          contatos = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          print("Olá, veio editar o contato? Se sim, fique a vontade 😁")
          
          nomeEditado = input("Digite um nome: ")
          self.nome = nomeEditado
          
          telefoneEditado = input("Digite um número de telefone: ")
          self.telefone = telefoneEditado
          
          emailEditado = input("Digite um E-Mail: ")
          self.email = emailEditado
          
          print("Muito bem, as alterações foram feitas com sucesso.")
          
          print(f"Contato anterior: {contatos}")
          
          contatoEditado = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          print(f"Contato editado: {contatoEditado}")
          
          print("Ok, você será redirecionado para a página de adicionar contatos.")
          
          self.adicionarContato()
          
     def removerContato(self):
          contatos = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          nomeRemovido = input("Digite um nome: ")
          nomeRemovido = self.nome
          self.nome = ""
          
          telefoneRemovido = input("Digite um número de telefone: ")
          telefoneRemovido = self.telefone
          self.telefone = ""
          
          emailRemovido = input("Digite um E-Mail: ")
          emailRemovido = self.email
          self.email = ""
          
          print("As remoção foi realizada com sucesso!")
          
          print(f"Contato antigo: {contatos}")
          
          contatoRemovido = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          print(f"Contado removido: {contatoRemovido}")

          print("Excelente, agora você vai voltar para a página de criar um contato.")

          self.adicionarContato()
          
     def buscarContato(self):
          contatos = {
               "Nome": self.nome,
               "Telefone": self.telefone,
               "E-Mail": self.email,
          }
          
          escolha = input("Você quer procurar uma pessoa pelo nome ou pelo telefone?: ").lower()
          
          if escolha == "nome" :
               print("Olá, tente digitar o nome para procurar um contato.")
          
               buscarNome = input("Digite o nome que você procura: ")
               
               if buscarNome == self.nome:
                    print("Você achou! Esse é contato que você queria?")
               
                    print(contatos)
               else:
                    print("Que pena, parece que esse nome não existe em seus contatos.")
          else:
               print("Esse nome não está em seus contatos.")
                    
          if escolha == "telefone":
               print("Olá, tente digitar um número de telefone para procurar um contato.")
               
               buscarTelefone = input("Digite o telefone que você procura: ")
               
               if buscarTelefone == self.telefone:  
                    print("Você achou! Esse é contato que você queria?")
               
                    print(contatos)
               else:
                    print("Que pena, parece que esse telefone não existe em seus contatos.")
          else:
               print("Que pena, parece que esse telefone não existe em seus contatos.")

contato = Agenda("", "", "")

contato.adicionarContato()