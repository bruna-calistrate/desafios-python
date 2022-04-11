print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 42 

Desafio dos triângulos - Com três segmentos de reta podemos formar um triângulo? Qual tipo de triângulo?
""")

r1 = float(input("Insira a medida da primeira reta: "))
r2 = float(input("Insira a medida da segunda reta: "))
r3 = float(input("Insira a medida da terceira reta: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"Com as retas {r1:.2f}, {r2:.2f} e {r3:.2f} podemos formar um triângulo.")
    if r1 == r2 == r3:
        print(f"E é um triângulo EQUILÁTERO.")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f"E é um triângulo ISÓSCELES.")
    else:
        print("E é um triângulo ESCALENO.")
else:
    print(f"Com as retas {r1:.2f}, {r2:.2f} e {r3:.2f} não podemos formar um triângulo.")
