listaj = []

class Jogador:    
    def __init__(self, nome, time, estado, desempenho): 
        self.nome = nome
        self.time = time 
        self.saude = estado
        self.desempenho = desempenho

    def mudar_time(self, time):
        self.time = time

def novo_jogador():
    nome = input("\nNome do jogador: ")
    time = input("Time do jogador: ")
    njogador = Jogador(nome, time, "saudavel", 0)
    listaj.append(njogador)



def inicio():
    print("\nbem vindo ao STM\n")

    print("selecione a opção:")
    print("1 - verificar jogadores")
    print("2 - adicionar jogador")
    print("3 - encerrar")

    escolha = input("sua opção: ")

    if escolha == "1":
        i = 0
        i_max = len(listaj)
        while listaj[i] != i_max:
            print(listaj[i].nome)
            i = i + 1
        inicio()
    elif escolha == "2":
        novo_jogador()
        inicio()
    elif escolha == "3":
        exit()
    else:
        print("opção inválida")
        inicio()

inicio()
