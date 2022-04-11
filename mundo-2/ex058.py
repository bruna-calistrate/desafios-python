print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Vamos jogar! Vou pensar em um número entre 1 e 10, você consegue adivinhar??""")
from random import randrange

comp = randrange(1, 10)
cont = 0
jog = 0
while jog != comp:
    jog = int(input("Digite um número: "))
    cont += 1
    if jog < comp:
        print("Mais... Tente outra vez")
    elif jog > comp:
        print("Menos... Tente outra vez")
print(f"Parabéns, você acertou! Pensei no número {comp} e você acertou após {cont} tentativas.")
