print("""Curso Python #10 - Condições Simples e Compostas - Desafio 30

Vou adivinhar se seu número é PAR ou ÍMPAR!
""")

num = int(input("Digite um número inteiro: "))
par = num % 2

if par == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar\.")
