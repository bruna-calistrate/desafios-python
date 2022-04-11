a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))
c = int(input("Digite o 3º número: "))
d = int(input("Digite o 4º número: "))
dados = (a, b, c, d)
print(f"Você imprimiu os números {dados}")
if 9 in dados:
    print(f"O número 9 apareceu {dados.count(9)} vezes.")
else:
    print(f"O número 9 não apareceu")
if 3 in dados:
    print(f"O número 3 apareceu na {dados.index(3) + 1}ª posição pela primeira vez")
else:
    print(f"O número 3 não apareceu")
print("Os números pares são: ", end='')
for num in dados:
    if num % 2 == 0:
        print(num, end=' ')
