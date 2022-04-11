from random import randrange, randint
from time import sleep

print("""Curso Python #10 - Condições Simples e Compostas

Você consegue me vencer? 
Vou pensar em um número entre 0 e 5, tente adivinhar!""")

num = int(randrange(5))
adv = int(input("Digite um número inteiro entre 0 e 5: "))
print("Processando...")

sleep(3)

if num == adv:
    print(f"Eu escolhi {num} e você {adv}. Parabéns, você venceu!!")
else:
    print(f"Eu escolhi {num} e você {adv}. Você errou!!")
print(f"{'Fim de jogo':-^50}")

# Outra solução:
comp = randint(0, 5)
jog = int(input("Em qual número pensei? "))
if comp == jog:
    print(f"Pensei no número {comp}! PARABÉNS, VOCÊ VENCEU!")
else:
    print(f"GANHEI! Eu pensei em {comp} e você em {jog}!")
