print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Determinando sexo M ou F
""")

while True:
    sexo = str(input("Insira o seu sexo: [M/F] ")).strip().upper()
    if sexo != "M" and sexo != "F":
        print("Opção inválida, insira seu sexo novamente.")
    elif sexo == "M" or sexo == "F":
        print(f"Sexo {sexo} computado com sucesso.")
        break
print("Fim")

# solução guanaraba
sexo = str(input("Insira o seu sexo: [M/F] ")).strip().upper()
while sexo not in "MF":
    sexo = str(input("Opção inválida, insira o seu sexo novamente: [M/F] ")).strip().upper()
print(f"Sexo {sexo} computado com sucesso.")
