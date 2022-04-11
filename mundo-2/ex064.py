print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição for

Soma de números""")

soma = 0
cont = 0
n = 1
while n != 999:
    n = int(input("Digite um número [999 para parar]: "))
    if n != 999:
        soma += n
        cont += 1
print(f"Foram digitados {cont} números e a soma entre eles é {soma}.")
