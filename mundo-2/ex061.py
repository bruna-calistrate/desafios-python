print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Vamos calcular a progressão aritmética de um número inteiro""")

cont = -1
termo = int(input("Informe o primeiro termo da PA: "))
r = int(input("Informe a razão da PA: "))
while cont < 9:
    cont += 1
    print(termo + cont * r, end=' > ')
print("Fim de PA")
