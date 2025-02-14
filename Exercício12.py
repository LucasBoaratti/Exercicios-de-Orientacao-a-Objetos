class LojaVirtual:
    def __init__(self, nome: str, id: int, categoria: str, produto: str, preco: int):
        self.nome = nome
        self.id = id
        self.categoria = categoria
        self.produto = produto
        self.preco = preco

    def cadastrarProdutos(self):
        print("Olá, seja bem vindo ao MercaLucas! Para continuar, cadastre seu produto aqui.")
        self.nome = input("Digite o nome do produto: ")

        self.id = input("Digite o ID do produto: ")
        self.id = int(self.id)

        self.categoria = input("Digite a categoria do produto: ")

        print("Produto cadastrado com sucesso.")

        self.produto = [
            "Nome do produto: ", self.nome,
            "ID do produto: ", self.id,
            "Categoria do produto: ", self.categoria,
            "Preço do produto: ", self.preco,
        ]
        
        colocar = input(f"Você gostaria de colocar esse(a) {self.nome} no carrinho de compras? (Digite sim ou não): ").lower()

        if colocar == "sim" or colocar == "s":
            print("Beleza! O produto será colocado no carrinho de compras e você será redirecionado para o mesmo.")
            self.carrinhoCompras()
        elif colocar == "nao" or colocar == "não" or colocar == "n":
            print("Ok... Só toma cuidado para não esquecer de comprar o produto 😅.")
        else:
            print("Por favor, digite uma opção válida.")

    def carrinhoCompras(self):
        print("Olá, veio ver seu carrinho? Veja seu produtos realizados abaixo.")

        print(f"Compra 1: {self.produto}")

        comprar = input("Você deseja comprar esse produto? (Digite sim ou não): ").lower()

        if comprar == "sim" or comprar == "s":
            precoLista = self.produto[len(self.produto) - 1]
            
            print(f"Preço do produto: {precoLista} reais")

            desconto = input("Que bom! Você gostaria de aplicar um desconto? (Digite sim ou não): ").lower()

            if desconto == "sim" or desconto == "s":
                print("Muito bem, agora você será redirecionado para aplicar o desconto.")

                self.aplicarDescontos()
            elif desconto == "nao" or desconto == "não" or desconto == "n":
                print("Tudo bem, você será redirecionado para pagar o total da compra.")
                
                self.totalCompra()
            else:
                print("Por favor, digite uma opção válida.")
        elif comprar == "nao" or comprar == "não" or comprar == "n":
            print("Ok... Você será redirecionado para a página de cadastro de produtos.")
            
            self.cadastrarProdutos()
        else:
            print("Por favor, digite uma opção válida.")

    def aplicarDescontos(self):
        print("Olá, vejo que você tem um cupom de desconto, né? 👀 Vamos usá-lo?")
        
        desconto = input("Digite aqui o valor de desconto do cupom em porcentagem (sem usar o %): ")
        desconto = float(desconto)
        
        totalDesconto = desconto / 100
        
        precoLista = self.produto[len(self.produto) - 1]
        
        totalCompra = precoLista * totalDesconto
        totalCompra = float(totalCompra)
        
        print(f"A compra total custou {totalCompra}. Obrigado por comprar no mercadinho do Lucas!")

    def totalCompra(self):
        precoLista = self.produto[len(self.produto) - 1]
        
        print(f"Total da compra: {precoLista}. Obrigado por comprar no mercadinho do Lucas!")
        
produto = LojaVirtual("", 0, "", "", 10)

produto.cadastrarProdutos()