print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Média, menores e maiores
""")
r = "S"
media = []
cont = 0
while r == "S":
    num = int(input("Digite um número inteiro: "))
    cont += 1
    media.append(num)
    r = str(input("Deseja continuar? [S/N] ")).strip().upper()
print(f"\nVocê inseriu {cont} números. "
      f"A média entre eles é {sum(media)/len(media)}, o maior é {max(media)} e o menor é {min(media)}.")
