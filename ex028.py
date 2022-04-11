print("""Curso Python #10 - Condições Simples e Compostas

Você consegue me vencer? 

Vou pensar em um número entre 0 e 5, tente adivinhar!""")

from random import randrange, randint
from time import sleep
num = int(randrange(5))
adv = int(input("Digite um número inteiro entre 0 e 5: "))
print("Processando...")
sleep(3)
if num == adv:
    print(f"Eu escolhi \033[1;32m{num}\033[m e você \033[1;32m{adv}\033[m.\033[1;30;42m Parabéns, você venceu!! \033[m")
else:
    print(f"Eu escolhi \033[1;32m{num}\033[m e você \033[1;31m{adv}\033[m.\033[1;30;41m Você errou!! \033[m")
print(f"{'Fim de jogo':-^50}")

# Outra solução:
# comp = randint(0, 5)
# jog = int(input("Em qual número pensei? "))
# if comp == jog:
  #  print(f"Pensei no número {comp}! PARABÉNS, VOCÊ VENCEU!")
# else:
  #  print(f"GANHEI! Eu pensei em {comp} e você em {jog}!")
