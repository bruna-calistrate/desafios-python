print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 47

Quais são os números pares entre 1 e 50? Vamos descobrir!!
""")

for c in range(1, 51):
    par = c % 2
    if par == 0:
        print(c, end=', ')
print("Acabou!")
for c in range(2, 51, 2):
    print(c, end=', ')
print("Acabou!")