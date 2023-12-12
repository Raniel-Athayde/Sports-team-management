import pickle
import os
import platform

def limpar_terminal():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Jogador:
    def __init__(self, nome, time, estado, desempenho):
        self.nome = nome
        self.time = time
        self.saude = estado
        self.desempenho = desempenho

    def mudar_time(self, time):
        self.time = time

def novo_jogador(lista_jogadores):
    nome = input("\nNome do jogador: ")
    time = input("Time do jogador: ")
    njogador = Jogador(nome, time, "saudavel", 0)
    lista_jogadores.append(njogador)

def verificar_jogadores(lista_jogadores):
    for i, jogador in enumerate(lista_jogadores, start=1):
        print(f"{i} - {jogador.nome}")
    print("\n")

def salvar_jogadores(lista_jogadores):
    with open('dados_jogadores.pkl', 'wb') as file:
        pickle.dump(lista_jogadores, file)

def carregar_jogadores():
    try:
        with open('dados_jogadores.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def inicio():
    listaj = carregar_jogadores()

    while True:
        limpar_terminal()
        print("\nBem-vindo ao STM\n")
        print("Selecione a opção:")
        print("1 - Verificar jogadores")
        print("2 - Adicionar jogador")
        print("3 - Salvar e encerrar")

        escolha = input("Sua opção: ")

        if escolha == "1":
            limpar_terminal()
            print("\nSeus jogadore salvos são:\n")
            verificar_jogadores(listaj)
            print("Secione a opção:\n")
            print("1 - Voltar\n")
            print("2 - Editar jogador\n")
            escolha2 = input("Sua opção: ")
            if escolha2 == 1:
                inicio()
            elif escolha2 == 2:
                editar()
            else:
                print("Opção inválida")

        elif escolha == "2":
            novo_jogador(listaj)
            salvar_jogadores(listaj)
        elif escolha == "3":
            salvar_jogadores(listaj)
            break
        else:
            print("Opção inválida")

def editar():
    limpar_terminal()
    print("Qual jogador deseja editar?")
    verificar_jogadores(listaj)
    input("Digite o número correspondente ao jogador:")
    inicio()

if __name__ == "__main__":
    inicio()
