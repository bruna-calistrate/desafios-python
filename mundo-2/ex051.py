print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 51

Progressão Aritmética""")

a1 = int(input("Informe o primeiro termo da PA: "))
r = int(input("Informe a razão da PA: "))
decimo = (a1 + (10 - 1) * r) + r
print("\nSeguem os 10 primeiros termos dessa progressão:")
for n in range(a1, decimo, r):
    print(n, end=' > ')
print("Acabou!!")
