print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 48

Qual a soma entre todos os números ímpares múltiplos de três entre 1 e 500?
""")

soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1 # contador
        soma += c # acumulador
        
print(f"A soma entre os {cont} números é: {soma}")
