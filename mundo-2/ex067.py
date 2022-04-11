while True:
    c = 0
    n = int(input("\nDigite um número inteiro: "))
    if n >= 0:
        print(f"{'':-^15}\n"
              f"Tabuada do {n:>4}\n"
              f"{'':-^15}")
        while c < 10:
            c += 1
            print(f"{n:>3} x {c:2.0f} = {n * c:>4}")
    else:
        break
print("Fim do programa")
