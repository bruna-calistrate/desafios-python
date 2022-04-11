num = []
par = []
impar = []
while True:
    n = int(input("Digite um número: "))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if cont not in "SN":
        cont = str(input("Opção errada...\nDeseja continuar? [S/N] ")).strip().upper()
    elif cont == 'N':
        break
print(f"Os números são: {num} \n"
      f"Os pares são:   {par} \n"
      f"Os ímpares são: {impar}")
