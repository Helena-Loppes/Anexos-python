import random

def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    while True:
        jogador = input("Olá jogador, vamos jogar Pedra, Papel e Tesoura? \nEscolha (0 = Pedra, 1 = Papel, 2 = Tesoura): ").strip()

        if not jogador.isdigit() or int(jogador) not in range(3):
            print("Opção inválida. Escolha 0, 1 ou 2.")
            continue

        jogador = int(jogador)
        computador = random.randint(0, 2)

        print(f"Você escolheu: {opcoes[jogador]}")
        print(f"O computador escolheu: {opcoes[computador]}")

        if jogador == computador:
            print("Empate!")
        elif (jogador - computador) % 3 == 1:
            print("Você venceu!")
        else:
            print("Computador venceu!")

        if input("Jogar novamente? (Sim/Não): ").strip().lower() != "sim":
            print("Obrigado por jogar! Até a próxima!")
            break

if __name__ == "__main__":
    jogar()
