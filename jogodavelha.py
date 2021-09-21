print("\033[7;40m     Jogo da Velha     \033[m")

def game():
    jogada = 0

    while ganhou() == 0:
        print("\nJogador ", jogada % 2 + 1)
        exibe()
        linha = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if board[linha - 1][coluna - 1] == 0:
            if (jogada % 2 + 1) == 1:
                board[linha - 1][coluna - 1] = 1
            else:
                board[linha - 1][coluna - 1] = -1
        else:
            print("Nâo esta vazio")
            jogada -= 1

        if ganhou():
            print("\033[32mJOGADOR ", jogada % 2 + 1, " VENCEU\033[m")

        jogada += 1


def ganhou():
    # checando linhas
    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]
        if soma == 3 or soma == -3:
            return 1

    # checando colunas
    for i in range(3):
        soma = board[0][i] + board[1][i] + board[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checando diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

def exibe():
    for y in range(3):
        for z in range(3):
            if board[y][z] == 0:
                print(" █ ", end=' ')
            elif board[y][z] == 1:
                print(" X ", end=' ')
            elif board[y][z] == -1:
                print(" O ", end=' ')

        print()


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def menu():
    continuar = 1
    while continuar:
        continuar = int(input("(1). Jogar\n" +
                              "(0). Sair\n"))
        if continuar:
            game()
        else:
            print("Saindo...")

menu()