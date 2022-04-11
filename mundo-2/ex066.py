print("Soma de vários números com flag\n")

cont = s = 0

while True:
    num = int(input("Digite um número inteiro [999 para parar]: "))
    if num == 999:
        break
    cont += 1
    s += num
print(f"\n"
      f"Foram digitados {cont} números, totalizando {s}")
