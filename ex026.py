# Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'a'; em que posição ela
# aparece pela primeira vez; em que posição ela aparece pela última vez
print("""Curso Python #9 - Manipulando Textos - Desafio 26
Vamos contar quantas vezes alguma letra aparece em uma frase?
""")
frase = str(input('Digite uma frase: ')).strip().upper()
car = str(input('Qual letra você gostaria de identificar? ')).strip().upper()

print(f"""A sua frase é: \033[1;33m{frase}\033[m.

A sua frase possui \033[1;32m{len(frase)}\033[m caracteres
A sua frase possui \033[1;37m{frase.count(car)}\033[m letras \033[1;30;47m>> {car} <<\033[m
A letra \033[1;30;47m>> {car} <<\033[m aparece pela primeira vez na {frase.find(car)+1}ª posição
A letra \033[1;30;47m>> {car} <<\033[m aparece pela  última  vez na {frase.rfind(car)+1}ª posição""")
