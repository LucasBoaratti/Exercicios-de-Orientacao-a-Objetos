class Produto: #Criando a classe do produto
    def __init__(self, nome: str, preco: float, quantidade: int): #Atribuindo os atributos para a classe produto
        self.nome = nome #Atribuindo o valor nome para a instância nome
        self.preco = preco #Atribuindo o valor preco para a instância preco
        self.quantidade = quantidade #Atribuindo o valor quantidade para a instância quantidade

    def valorEstoque(self): #Método de valor do estoque
        self.quantidade = input("Digite o total do estoque inicial: ") #O usuário vai digitar a quantidade do estoque inicial
        self.quantidade = int(self.quantidade) #Transformando a variável self.quantidade em inteiro

        valorCompras = input("Digite o valor de compras obtido durante o período: ") #O usuário vai digitar o valor das compras
        valorCompras = float(valorCompras) #Transformando a variável valorCompras em float

        estoqueFinal = input("Digite o total do estoque final: ") #O usuário vai digitar a quantidade do estoque final
        estoqueFinal = int(estoqueFinal) #Transformando a variável estoqueFinal em inteiro
 
        cmv = self.quantidade + valorCompras - estoqueFinal # CMV: Custo de Mercadoria Vendida

        if cmv > 0: #Se o cmv for maior que 0...
            self.comprar() #Chamando a função de comprar
        else: #Caso o cmv esteja abaixo de 0
            print("O produto não está disponível.") #Exibindo a mensagem de aviso
 
        print(f"O valor do cmv é de: {cmv}") #Exibindo o valor do cmv

    def comprar(self): #Método de comprar produto
        dinheiro = input("Digite a quantidade que deseja pagar: ") #O usuário vai inserir a quantidade que deseja pagar
        dinheiro = float(dinheiro) #Transformando a variável dinheiro em float

        if dinheiro >= self.preco: #Verificando se o usuário tem mais dinheiro que o preço do produto
            valorTotal = dinheiro - self.preco #Calculando o valor total da compra
            
            print(f"Você vai comprar o produto {self.nome} e pagará {valorTotal}. Muito obrigado por comprar na nossa loja!") #Exibindo o produto, e a quantidade que será paga no terminal
        else: #Caso o usuário não tenha dinheiro...
            print("Dinheiro insuficiente.") #Exibindo a mensagem de aviso no terminal

produto = Produto("Chocolate", 10.00, 0) #Nome do produto, preço, quantidade

produto.valorEstoque() #Iniciando a função do valor de estoque