print("""Curso Python #10 - Condições Simples e Compostas - Desafio 31

Vamos calcular o preço da sua passagem.
""")
km = float(input("Qual a distância da sua viagem em km? "))

if km <= 200:
    print(f"A sua passagem custará R$ {km*0.5:.2f}!")
else:
    print(f"A sua passagem custará R$ {km*0.45:.2f}!")
print("Boa viagem!!")

#Outra maneira:
if km <= 200:
    preço = km * 0.5
else:
    preço = km * 0.45
print(f"A sua passagem custará R$ {preço:.2f}, boa viagem!")
