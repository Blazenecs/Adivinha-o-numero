import random 

num_min = 1
num_max = 100
random_number = random.randint(num_min, num_max)

def main(random_number):
  chute = 0
  chutes = 0
  while chute != random_number:  
    chute = int(input("Digite um numero entre 1 e 100: "))
    chutes += 1
    dist_chute = calculate_distance(chute, random_number)

    print(results(dist_chute, chutes))
   
def calculate_distance(chute, random_number):
  return abs(random_number - chute) 

def results(dist_chute, chutes):
  if dist_chute == 0:
    return f"Parabens, voce acertou!\nVoce acertou o chute com {chutes} chutes!"
  elif dist_chute <= 10:
    return f"Voce errou por {dist_chute} numeros de distancia para mais ou para menos!"
  else:
    return "Voce errou por muito!"
  
main(random.randint(num_min, num_max))




