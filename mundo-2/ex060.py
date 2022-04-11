print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Vamos calcular o fatorial de um número inteiro""")

num = int(input("Digite um número inteiro: "))
c = num
fat = 1
print(f"{c}! = ", end='')
while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1
print(f"{fat}")
