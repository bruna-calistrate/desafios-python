print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 38 

Vamos comparar dois números e dizer qual o maior, ou se são iguais
""")

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    print(f"O primeiro número, {num1}, é maior que o segundo número, {num2}.")
elif num2 > num1:
    print(f"O segundo número, {num2}, é maior que o primeiro número, {num1}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")
