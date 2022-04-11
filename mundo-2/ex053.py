print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 53

Essa frase é um palíndromo? Vamos descobrir!""")

frase = str(input("Digite uma frase: ")).strip().upper().replace(" ", "")
#pali = frase[::-1]
#print(f"O inverso de {frase} é {pali}")
#if pali == frase:
#    print("Essa frase é um palíndromo!")
#else:
#    print("Essa frase não é um palíndromo!")

inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
print(f"O inverso de {frase} é {inverso}")
if inverso == frase:
    print("Essa frase é um palíndromo!")
else:
    print("Essa frase não é um palíndromo!")
