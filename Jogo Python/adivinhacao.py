import random

import jogos

print("**********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = random.randrange(1, 101) #isso representa um número aleatório
total_de_tentativas = 3
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Facil (2) Medio (3) Dificil")

nivel = int(input("Define o Nivel: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativas {} de {}".format(rodada, total_de_tentativas)) #faz troca de rodadas automaticamente

    chute_str = input("Digite um número entre 1 à 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 à 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto")

        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


print("Fim do jogo!")


