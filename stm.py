import pickle
import os
import platform
from traceback import print_tb

def limpar_terminal():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Jogador:
    def __init__(self, nome, estado,  ocorrencias, desempenho, posicao):
        self.nome = nome
        self.estado = estado
        self.ocorrencias = ocorrencias
        self.desempenho = desempenho
        self.posicao = posicao

    def mudar_nome(self, nome):
        self.nome = nome

def novo_jogador(lista_jogadores):
    nome = input("\nNome do jogador: ")
    ocorrencias = []
    desempenho = []
    estado = True
    njogador = Jogador(nome, estado, ocorrencias, desempenho, "indefinida")
    lista_jogadores.append(njogador)

class Time:
    def __init__(self, nome, jogadores, prox_jogos, vict, derr, em):
        self.nome = nome
        self.jogadores = jogadores
        self.prox_jogos = prox_jogos
        self.vict = vict
        self.derr = derr
        self.em = em

    def novo_nome(self, nome):
        self.nome = nome

def listar(lista):
    for i, elemento in enumerate(lista, start = 1):
        print(f"    {i} - {elemento.nome}")
    print("\n")

def listar_jogos(lista):
    for i, elemento in enumerate(lista, start = 1):
        print(f"    {i} - {elemento}")
    print("\n")

def remover(lista, item):
    print("Qual " + item + " você deseja remover?")
    i_item = input("Escreva o numero do " + item +":" )
    del lista[int(i_item) - 1]

def novo_time(lista_times):
    jogadores = []
    prox_jogos = []
    nome = input("Digite o nome do time: ")
    ntime = Time(nome, jogadores, prox_jogos, 0, 0, 0)
    lista_times.append(ntime)

def salvar_times(lista_times):
    with open('dados_times.pkl', 'wb') as file:
        pickle.dump(lista_times, file)

def carregar_times():
    try:
        with open('dados_times.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
def vizualizar_jogador(jogador):
    while True:
        print("Nome: " + jogador.nome)
        if jogador.estado:
            print("Estado: Apto a jogar")
        else:
            print("Estado: Inapto a jogar")
        print("Posição" + jogador.posicao)
        print("Selecione uma opção: ")
        print(" 1 - Verificar ocorrencias")
        print("2 - verificar desempenho")
        print("3 - voltar")
        escolha = input("Sua opção: ")
        if escolha == "1":
            listar(jogador.ocorrencias)
            print("\n")
            print("Selecione uma opção:")
            print("1 - Adicionar ocorrencia")
            print("2 - Remover ocorrencia")
            print("3 - Voltar")
            escolha2 = input("Sua opção: ")
            if escolha2 == "1":
                nocorrencia = input("Insira a ocorrencia")
                jogador.ocorrencias.append(nocorrencia)
            elif escolha2 == "2":
                iocorrencia = input("Insira o número da ocorrencia que deseja remover: ")
                del jogador.ocorrencias[int(iocorrencia) - 1]
            elif escolha2 == "3":
                pass
            else:
                print("Opção invalida")
                input("Pressione ENTER para continuar")

        elif escolha == "2":
            listar(jogador.desempenho)
            print("\n")
            print("Selecione uma opção:")
            print("1 - Adicionar desempenho em um jogo")
            print("2 - Remover desempenho")
            print("3 - Voltar")
            escolha2 = input("Sua opção: ")
            if escolha2 == "1":
                ndesempenho = input("Insira a descrição")
                jogador.desempenho.append(ndesempenho)
            elif escolha2 == "2":
                idesempenho = input("Insira o número da descrição que deseja remover: ")
                del jogador.ocorrencias[int(idesempenho) - 1]
            elif escolha2 == "3":
                pass
            else:
                print("Opção invalida")
                input("Pressione ENTER para continuar")

        elif escolha == "3":
            break

        else:
            print("Opção invalida")
            input("pressione ENTER para continuar")



    
def vizualizar_time(time, lista):
    while True:
        limpar_terminal()
        print("Time: " + time.nome)
        listar(time.jogadores)
        print("\n")
        print("Selecione a opção:")
        print("1 - Adicionar Jogador")
        print("2 - Vizualizar jogador")
        print("3 - Remover jogador")
        print("4 - vizualizar jogos")
        print("5 - vizualizar resultados")
        print("6 - Editar nome")
        print("7 - voltar")
        print("\n")
        escolha = input("Sua opção: ")

        if escolha == "1":
            novo_jogador(time.jogadores)

        if escolha == "2":
            ijogador = input("Insira o numero do jogador: ")
            vizualizar_jogador(time.jogadores[int(ijogador) - 1])

        elif escolha == "3":
            remover(time.jogadores, "jogador")

        elif escolha == "4":
            limpar_terminal()
            print("Time: " + time.nome)
            print("Seus jogos:\n")
            listar_jogos(time.prox_jogos)
            print("O que deseja fazer?")
            print("1 - Adicionar jogo")
            print("2 - Concluir jogo")
            print("3 - Voltar")

            escolha2 = input("Sua opão: ")

            if escolha2 == "1":
                evento = input("Insira aqui o nome do evento: ")
                time.prox_jogos.append(evento)

            elif escolha2 == "2":
                ievento = input("Escolha o evento que deseja concluir: ")
                del time.prox_jogos[int(ievento) - 1]
                print("Qual foi o resultado do jogo?")
                print("1 - Vitória")
                print("2 - Derrota")
                print("3 - Empate")
                print("4 - Irrelevante")
                resultado = input("Resultado: ")

                if resultado == "1":
                    time.vict += 1

                elif resultado == "2":
                    time.derr += 1
                
                elif resultado == "3":
                    time.em += 1
        elif escolha == "5":
            print("n° de vitorias: " + str(time.vict)) 
            print(" n° de derrotas: " + str(time.derr))
            print(" n° de empates: " + str(time.em))
            total = time.vict + time.derr + time.em
            porcetagem = (time.vict / total) * 100
            print("resultado: " + str(time.vict) +"/" + str(total) + "(" +  str(porcetagem) + "%)\n")
            input("precione enter para continuar")

        elif escolha == "6":
            nome = input("Digite o novo nome: ")
            time.novo_nome(nome)

        elif escolha == "7":
            break

        else:
            print("Opção invalida")
            input("Aperte ENTER para continuar")
        
        salvar_times(lista)

def inicio():
    listat = carregar_times()

    while True:
        limpar_terminal()
        print("\nBem-vindo ao STM\n")
        print("Selecione a opção:")
        print("1 - Verificar times")
        print("2 - Adicionar time")
        print("3 - Salvar e encerrar")

        escolha = input("Sua opção: ")

        if escolha == "1":
            limpar_terminal()
            print("\nSeus times salvos são:\n")
            listar(listat)
            print("Secione a opção:\n")
            print("1 - Vizualizar time\n")
            print("2 - Remover time")
            print("3 - Voltar\n")
            escolha2 = input("Sua opção: ")
            
            if escolha2 == "1":
                print("Qual time deseja vizualizar?")
                escolha3 = input("Escreva o número do time: ")
                vizualizar_time(listat[int(escolha3) - 1], listat)

            elif escolha2 == "2":
                remover(listat, "time")

            elif escolha2 == "3":
                pass

            else:
                print("Opção inválida")

        elif escolha == "2":
            novo_time(listat)
            salvar_times(listat)
        
        elif escolha == "3":
            salvar_times(listat)
            break

        else:
            print("Opção inválida")
            input("Aperte ENTER para continuar")

if __name__ == "__main__":
    inicio()
