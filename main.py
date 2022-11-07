import random

player_1 = input("Insira seu nome\n")
player_2 = "CPU"

while True:
    opcao_player_1 = input('insira:\nsair\npedra\npapel\ntesoura\n')
    opcao_player_2 = random.choice(["pedra", "papel", "tesoura"])

    if opcao_player_1 != "sair" and opcao_player_1 != "pedra" and opcao_player_1 != "papel" and opcao_player_1 != "tesoura":
        print("Opcão inválida.\n")
        break
    elif opcao_player_1 == 'sair':
        print("Obrigado por jogar!\n")
        break
    else:
        print("Opção de", player_1, ":", opcao_player_1)
        print("Opção do", player_2, ":", opcao_player_2)

    if opcao_player_1 == opcao_player_2:
        print("Empatou!\n")
    elif opcao_player_1 == 'pedra':
        if opcao_player_2 == 'tesoura':
            print("Pedra esmaga tesoura!\n", player_1, " venceu!\n")
        else:
            print("Papel cobre a pedra!\n", player_2, " venceu!\n")
    elif opcao_player_1 == 'papel':
        if opcao_player_2 == 'pedra':
            print("Papel cobre a pedra!\n", player_1, " venceu!\n")
        else:
            print("Tesoura corta o papel!\n", player_2, " venceu!\n")
    else:
        if opcao_player_2 == 'papel':
            print("Tesoura corta o papel!\n", player_1, " venceu!\n")
        else:
            print("Pedra esmaga tesoura!\n", player_2, " venceu!\n")