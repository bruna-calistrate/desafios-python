saque = int(input("Quanto você gostaria de sacar: R$ "))
soma = c50 = c20 = c10 = c01 = 0
print(f"{'':=^20}\n"
      f"{'Banco Pônei':^20}\n"
      f"{'':=^20}\n"
      f"Saque de R$ {saque:.2f}")
while True:
    ced = saque - soma
    if ced >= 50:
        c50 = ced // 50
        soma += (c50 * 50)
        print(f"{c50:2d} cédulas de R$ 50")
    elif ced >= 20:
        c20 = ced // 20
        soma += (c20 * 20)
        print(f"{c20:2d} cédulas de R$ 20")
    elif ced >= 10:
        c10 = ced // 10
        soma += (c10 * 10)
        print(f"{c10:2d} cédulas de R$ 10")
    elif ced >= 1:
        c01 = ced // 1
        soma += c01
        print(f"{c01:2d} cédulas de R$  1")
    elif ced == 0:
        break
print(f"{'':=^20}")
