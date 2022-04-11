print("""Curso Python #10 - Condições Simples e Compostas - Desafio 33

Vamos determinar qual é o maior e qual é o menor número entre três
""")

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

# Primeiro teste, muito mais trabalhoso:
# mai1 = n1 > n2 and n1 > n3
# mai2 = n2 > n1 and n2 > n3
# mai3 = n3 > n1 and n3 > n2
# men1 = n1 < n2 and n1 < n3
# men2 = n2 < n1 and n2 < n3
# men3 = n3 < n1 and n3 < n2

# print("\nO maior número é: ")
# if mai1:
#   print(f"{n1}")
# elif mai2:
#   print(f"{n2}")
# elif mai3:
#   print(f"{n3}")

# print("\nO menor número é:")
# if men1:
#   print(f"{n1}")
# elif men2:
#    print(f"{n2}")
# elif men3:
#    print(f"{n3}")

# outra maneira, bem mais eficiente e consisa:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
print(f"""Entre os números {n1}, {n2} e {n3}:
O menor número é {menor}
O maior número é {maior}""")
