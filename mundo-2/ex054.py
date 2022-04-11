print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 54

Teste de maioridade
""")
from datetime import date

maior = 0
menor = 0
for a in range(1, 8):
    ano = int(input(f"Em qual ano a {a}ª pessoa nasceu? "))
    atual = date.today().year
    idade = (atual - ano)
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"Entre as 7 pessoas, {maior} tem mais de 21 anos e {menor} tem menos.")
