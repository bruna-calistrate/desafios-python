print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 50

Soma entre números pares, informe seis números e vamos somar apenas os pares:
""")
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f"Informe o {c}º número: "))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f"Você informou {cont} números pares e a sua soma é: {soma}!!")
