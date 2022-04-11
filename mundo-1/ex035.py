print("""Curso Python #10 - Condições Simples e Compostas - Desafio 35

Com três segmentos de reta podemos formar um triângulo?
""")

r1 = float(input("Insira a medida da primeira reta: "))
r2 = float(input("Insira a medida da segunda reta: "))
r3 = float(input("Insira a medida da terceira reta: "))

if (r2-r3) < r1 < (r2+r3) and (r1-r3) < r2 < (r1+r3) and (r1-r2) < r3 < (r1+r2):
    print(f"Com as retas {r1:.2f}, {r2:.2f} e {r3:.2f} podemos formar um triângulo.")
else:
    print(f"Com as retas {r1:.2f}, {r2:.2f} e {r3:.2f} >> não << podemos formar um triângulo.")
