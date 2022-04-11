num = []
for c in range(0, 5):
    n = int(input(f"Digite o {c + 1}º número: "))
    if n in num:
        print("Número repetido, tente novamente...")
        n = int(input(f"Digite o {c + 1}º número: "))
    if c == 0 or n > num[-1]:
        num.append(n)
        print(f"Número inserido na última posição...")
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f"Número inserido na posição {pos}")
                break
            pos += 1


print('-'*30)
print(num)
for a in range(0, len(num)):
    print(f"Na {a + 1}ª posição: {num[a]}")
