print("""Curso Python - mundo 2 Aula 13 - Estrutura de repetição for

Qual o maior e qual o menor peso entre cinco pessoas?
""")
#lista = []
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f"Qual o peso da {c}ª pessoa? (kg) "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O mais pesado entre os 5 tem {maior:.1f} kg, e o menos tem {menor:.1f} kg.")
#    lista.append(peso)
#print(f"O mais pesado entre os 5 tem {max(lista):.1f} kg, e o menos tem {min(lista):.1f} kg.")
