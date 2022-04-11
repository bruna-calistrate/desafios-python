from random import randint
from time import sleep

print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 45

Você consegue me vencer?
Vamos jogar pedra, papel ou tesoura!!
""")

print("Vou fazer a minha jogada!\n"
      "Escolhendo...")
itens = ('Teste', 'Pedra', 'Papel', 'Tesoura')
comp = randint(1, 3)
sleep(1)
jock = int(input("Agora é a sua vez!\n"
                 "1 - Pedra\n"
                 "2 - Papel\n"
                 "3 - Tesoura\n"
                 "Escolha a sua jogada: "))

print("\nPEDRA...")
sleep(1)
print("PAPEL...")
sleep(1)
print("TESOURA!!!\n")
sleep(1)

if comp == jock:
    print(f"Escolhemos {itens[jock]}, empatamos!!")
elif comp == 1 and jock == 2 or comp == 2 and jock == 3 or comp == 3 and jock == 1:
    print(f"Escolhi {itens[comp]} e você {itens[jock]}. Parabéns, você venceu!!")
elif jock == 1 and comp == 2 or jock == 2 and comp == 3 or jock == 3 and comp == 1:
    print(f"Escolhi {itens[comp]} e você {itens[jock]}, você perdeu!!")

print("\nFim de jogo.")
