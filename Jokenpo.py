import random
 

def main():
    while True:
        jogador = input("Vamos jogar jokenpo!! Escolha: pedra, papel ou tesoura? ")
        robo = escolha_aleatoria()

        if jogador != "pedra" and jogador != "tesoura" and jogador != "papel":
            print("Essa escolha e invalida.")
            continue
        if jogador == robo:
            print(f"Deu empate ambos escolheram {jogador}")
        elif vitoria_jogador(jogador, robo):
            print(f"Voce ganhou! Voce escolheu {jogador} e a maquina escolheu {robo}.")
        else:
            input(f"Voce perdeu! Voce escolheu {jogador} e a maquina escolheu {robo}.")
        
        resposta = input("Deseja continuar a jogar?\n Digite Sim para continuar.")

## Continue volta sempre ao ultimo while antes dele. Break sai do loop
        if resposta == "Sim":
            continue
        else:
            break    

def escolha_aleatoria():
    random_jogo = random.randint(1, 3)

    if random_jogo == 1:
        return "pedra"
    elif random_jogo == 2:
        return "papel"
    else:
        return "tesoura"



def vitoria_jogador(jog,rob):
    
    if jog == "pedra" and rob == "tesoura":
        return True
    elif jog == "tesoura" and rob == "papel":
        return True
    elif jog == "papel" and rob == "pedra":
        return True
    else:
        return False

main()
