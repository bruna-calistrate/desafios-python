from datetime import datetime

print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 41

Confederação Nacional de Natação - Qual é a sua categoria?""")

nas = int(input("Em qual ano você nasceu? "))
ano_atual = datetime.today().year
idade = ano_atual - nas

print(f"Você tem {idade} anos.")
if idade <= 9:
    print(f"Está na categoria MIRIM.")
elif idade <= 14:
    print(f"Está na categoria INFANTIL.")
elif idade <= 19:
    print(f"Está na categoria JÚNIOR.")
elif idade <= 25:
    print(f"Está na categoria SÊNIOR.")
else:
    print(f"Está na categoria MASTER.")
