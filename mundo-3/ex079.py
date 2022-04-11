num = []
cont = "S"
while True:
    val = int(input("\nDigite um número: "))
    if val in num:
        print("Número repetido... não será adicionado!")
    if val not in num:
        num.append(val)
        print("Número adicionado com sucesso!")
    cont = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if cont not in "SN":
        cont = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if cont == "N":
        break
num.sort()
print(f"{'':-^30} \n"
      f"Os valores são: {num}")
