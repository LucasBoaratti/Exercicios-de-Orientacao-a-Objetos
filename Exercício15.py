import random

class JogoCartas:
    def __init__(self, numero: int, jogadas: int):
        self.numero = numero
        self.jogadas = jogadas
    
    def embaralharCartas(self):
        print("Olá, seja bem vindo ao UNO do Lucas, onde serão embaralhadas 7 cartas e o jogador que acabar com as cartas primeiro, vence o jogo.")

        print("As cartas estão sendo embaralhadas para serem distribuidas...")

        self.distribuirCartas()

    def distribuirCartas(self):
        print("Agora as cartas serão distribuidas.")

        nomeJogador1 = input("Digite seu nome, jogador 1: ")

        cartasJogador1 = random.randint(1, 10)

        for i in cartasJogador1:
            print(f"Os números de sua carta, {nomeJogador1}: {cartasJogador1}")

        nomeJogador2 = input("Digite seu nome, jogador 2: ")      

        cartasJogador2 = random.randint(1, 10)

        for i in cartasJogador2:
            print(f"Os número das suas cartas, {nomeJogador2}: {cartasJogador2}.")

        print("Então, vamos para o jogo.")

        nomeJogador1, nomeJogador2 = self.permitirJogadas()

    def permitirJogadas(self):
        print("Vamos começar o jogo, mas será diferente dessa vez, vocês terão no máximo 20 jogadas para terminar o jogo 😈")

        for i in range(1, 20):
            jogada1 = input(f"Digite o número da carta, jogador1: ")
            jogada1 = int(jogada1)

            print(f"Número jogado: {jogada1}")

            jogada2 = input(f"Digite o número da carta, jogador 2: ")
            jogada2 = int(jogada2)

            print(f"Número jogado: {jogada2}")

        print(f"Parabéns, {jogador1}, você venceu o jogo!")

jogador1 = JogoCartas(0, 0)

jogador1.embaralharCartas()