class MaquinasDeVendas:
    def __init__(self, nome: str, id: int, numero: int, tipo: str, preco: float, dinheiro: float, estoque: int):
        self.nome = nome
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.dinheiro = dinheiro
        self.estoque = estoque

    def cadastrarProdutos(self):
        print("Olá, bem vindo a máquina do Lucas! Cadastre seu produto agora para vendê-lo para sempre!")

        self.nome = input("Digite o nome do produto: ")

        self.id = input("Digite o ID do produto: ")
        self.id = int(self.id)

        self.numero = input("Digite o número do produto, correspondente ao número do mesmo, na máquina: ")
        self.numero = int(self.numero)

        self.tipo = input("Digite o tipo do produto: ")

        self.preco = input("Digite o preço do produto: ")
        self.preco = float(self.preco)

        self.estoque = input("Digite a quantidade de estoque do produto: ")
        self.estoque = int(self.estoque)

        print(f"Parabéns! O produto {self.nome}, do número {self.numero} foi cadastrado com sucesso!")

        verEstoque = input("Você quer ver o produto no estoque? (Digite sim ou não): ").lower()

        if verEstoque == "s" or verEstoque == "sim":
            print("Ok, você será redirecionado para o estoque de produtos.")

            self.exibirEstoque()
        elif verEstoque == "n" or verEstoque == "nao" or verEstoque == "não":
            escolher = input("Você quer comprar o produto? (Digite sim ou não): ").lower()

            if escolher == "sim" or escolher == "s":
                print("Beleza, você será redirecionado para a página do produto.")

                self.selecionarProduto()
            elif escolher == "nao" or escolher == "não" or escolher == "n":
                print("Ok, compre na próxima então :)")
            else:
                print("Digite uma opção válida.")

    def selecionarProduto(self):
        print("Olá, que bom que você veio, vamos comprar o produto.")

        produto = {
            "Nome do produto": self.nome,
            "Número do produto": self.numero,
            "Preço do produto": self.preco,
            "Produtos restantes": self.estoque,
        }

        print(f"Produtos disponíveis: {produto}")

        escolherNumero = input("Digite o número do produto que você quer: ")
        escolherNumero = int(escolherNumero)

        if escolherNumero == self.numero and self.estoque > 0: 
            print(f"Você escolheu o produto {self.nome} do número {self.numero}")

            print("Você será redirecionado para a parte de pagamento.")

            self.inserirDinheiro()
        else:
            print("Desculpe, infelizmente o produto acabou ou não temos um produto com esse número.")

            self.selecionarProduto()

    def inserirDinheiro(self):
        print("Olá, vamos concluir seu pagamento.")

        self.dinheiro = input("Digite a quantidade que você irá pagar: ")
        self.dinheiro = float(self.dinheiro)

        if self.dinheiro == self.preco:
            print("Obrigado por comprar na máquina do Lucas! Aproveite seu produto.")

            print(f"Quantidade em estoque: {self.estoque - 1}")
        elif self.dinheiro > self.preco:
            print("Espere um momento, seu troco está sendo calculado.")

            self.retornarTroco()
        elif self.dinheiro < self.preco:
            print("Que pena, parece que seu dinheiro não foi suficiente para pagar o produto. Tente novamente.")

            self.inserirDinheiro()
        else:
            print("Por favor, insira apenas números.")

    def retornarTroco(self):
        calcularTroco = self.dinheiro - self.preco

        print(f"Seu troco total foi de {calcularTroco} reais. Obrigado por comprar na máquina do Lucas!")

        print(f"Quantidade em estoque: {self.estoque - 1}")

    def exibirEstoque(self):
        print(f"Quantidade em estoque: {self.estoque}")

        self.cadastrarProdutos()

vendaProduto = MaquinasDeVendas("", 0, 0, "", 0.0, 0.0, 0)

vendaProduto.cadastrarProdutos()