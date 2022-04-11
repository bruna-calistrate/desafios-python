print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição for

Sequência de Fibonacci""")
f1 = 0
f2 = 1
n = int(input("Quantos elementos da sequência de Fibonacci você quer ver? "))
print(f1, f2, sep=' - ', end=' - ')
cont = 3
while cont <= n:
    fib = f1 + f2
    f1 = f2
    f2 = fib
    print(fib, end=" - ")
    cont += 1
print("...")

