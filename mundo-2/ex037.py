print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 37

Vamos fazer conversão de base numérica de um número inteiro para binário, octal ou hexadecimal?""")

num = int(input("Digite um número inteiro: "))
conv = int(input("Para qual base numérica você gostaria de converter?\n"
                 "[ 1 ] - binário\n"
                 "[ 2 ] - octal\n"
                 "[ 3 ] - hexadecimal\n"))

if conv == 1:
    print(f"Convertendo {num} para binário: {bin(num)[2:]}")
elif conv == 2:
    print(f"Convertendo {num} para octal: {oct(num)[2:]}")
elif conv == 3:
    print(f"Convertendo {num} para hexadecimal: {hex(num)[2:]}")
else:
    print("Você selecionou a opção errada, tente novamente.")
