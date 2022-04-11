# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
# separadamente.
print("""Curso Python #9 - Manipulando textos - Desafio 27
Vamos formatar o seu nome?
""")

nome = str(input('Qual o seu nome completo? ')).strip().title()
lista = nome.split()

print(f"""O seu nome completo é \033[4;32m{nome}\033[m
O seu primeiro nome é \033[1;34m{lista[0]}\033[m 
O seu  último  nome é \033[1;34m{lista[-1]}\033[m

Seu nome simplificado é \033[1;35m{lista[0]} {lista[-1]}\033[m""")
