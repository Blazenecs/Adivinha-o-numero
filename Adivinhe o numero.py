import random 

num_min = 1
num_max = 100
chutes = 0

def random_number(num_min, num_max):
    while True:
        chute = int(input("Digite um numero de 1 a 100: "))
        chutes + 1
        if chute == (random_number - 10) or chute == (random_number + 10):
            print("Voce esta a 10 numeros de distancia para acertar o numero!")
        elif chute == random_number:
            print(f"Parabens voce acertou o numero! com {chutes} chutes")
        break    