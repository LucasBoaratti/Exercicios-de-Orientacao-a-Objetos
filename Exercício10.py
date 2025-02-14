class Livro:
     def __init__(self, titulo: str, autor: str, numeroPaginas: int, emprestimo: True, disponivel = True):
          self.titulo = titulo
          self.autor = autor
          self.numeroPaginas = numeroPaginas
          self.emprestimo = emprestimo
          self.disponivel = disponivel
          
     def emprestar(self):
          emprestar = input(f"Você gostaria de pegar emprestado o livro {self.titulo}? (Digite sim ou não): ").lower()
          
          if emprestar == "sim" or emprestar == "s":
               self.emprestimo = True
               
               print("O livro foi emprestado.")
          elif emprestar == "nao" or emprestar == "não" or emprestar == "n":
               self.emprestimo == False
               
               print("O livro não foi emprestado.")
          else:
               print("Digite uma resposta válida!")
     
     def devolver(self):
          if self.emprestimo == True:
               devolver = input(f"Você gostaria de devolver o livro {self.titulo}? (Digite sim ou não): ").lower()
               
               if devolver == "sim" or devolver == "s":
                    print("O livro foi devolvido.")
                    
                    self.emprestar()
                    
                    self.disponivel = True
               elif devolver == "nao" or devolver == "não" or devolver == "n":
                    self.disponivel = False
     
                    self.emprestar()
               else:
                    print("Digite uma resposta válida!")
                    
     def disponivel(self):
          if self.disponivel == True:
               print("Esse livro está disponível.")
          elif self.disponivel == False:
               print("Esse livro não está disponível.")