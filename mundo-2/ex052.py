print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 52

É um número primo?
""")

div = 0
num = int(input("Informe um número real inteiro: "))
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[1;32m", end='')
        div += 1
    else:
        print("\033[0;31m", end='')
    print(f"{c}", end=' ')
    
print(f"\033[m\nO número {num} é divisível {div} vezes.")
if div == 2:
    print("Portanto, é um número primo!!")
else:
    print("Portanto, não é um número primo.")
