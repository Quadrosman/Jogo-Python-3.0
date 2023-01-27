def escolha_jogo():
    print("**********************************")
    print("********Escolha o seu jogo!*******")
    print("**********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        import forca
        print("Jogando forca")
        forca.jogar()

    elif(jogo == 2):
        import adivinhacao
        print("Jogando adivinhação")
        adivinhacao.jogar()


if(__name__ == "__main__"):
    escolha_jogo()