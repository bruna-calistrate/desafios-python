num = []

while True:
    num.append(int(input("Digite um número: ")))
    cont = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if cont not in "SN":
        cont = str(input("Opção errada...\nDeseja continuar? [S/N] ")).strip().upper()
    elif cont == 'N':
        break
num.sort(reverse=True)
print(f"\n{'':-^20}\n"
      f"Foram digitados {len(num)} números.\n"
      f"Segue a lista de valores: {num}")
if 5 in num:
    print(f"O número 5 foi digitado {num.count(5)} vezes.")
else:
    print("O número 5 não foi inserido.")
