from datetime import date

print("""Curso Python #10 - Condições Simples e Compostas - Desafio 32

É um ano bissexto?
""")

ano = int(input("Digite o ano que quer analizar ou 0 para o ano atual: "))

if ano == 0:
    ano = date.today().year
    
bis = ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0
temp = "será"

if ano == date.today().year:
    temp = "é"
elif ano < date.today().year:
    temp = "foi"

if bis == True:
    print(f"O ano {ano} {temp} bissexto!")
else:
    print(f"O ano {ano} não {temp} bissexto.")
