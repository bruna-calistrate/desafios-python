num = []
for c in range(0, 5):
    num.append(int(input(f"Digite o {c + 1}º valor: ")))
maior = max(num)
menor = min(num)
print(f"O maior valor é {maior} e está na posição {num.index(maior)}, \n"
      f"o menor valor é {menor} e está na posição {num.index(menor)}.")
