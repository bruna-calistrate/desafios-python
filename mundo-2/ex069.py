mulher_menor = maior = pessoas = homem = 0
while True:
    print(f"{'Cadastro':-^30}")
    sexo = str(input("Insira o seu gênero [M/F]: ")).strip().upper()
    while sexo not in "MF":
        sexo = str(input("Insira o seu gênero [M/F]: ")).strip().upper()
    idade = int(input("Insira a sua idade: "))
    pessoas += 1
    if idade >= 18:
        maior += 1
    if sexo == "M":
        homem += 1
    elif sexo == 'F' and idade <= 20:
        mulher_menor += 1
    r = str(input("Deseja inserir mais dados [S/N]: ")).strip().upper()
    if r == "N":
        break
print(f"\nForam inseridos os dados de {pessoas} pessoas.\n"
      f"{maior} têm mais de 18 anos.\n"
      f"{homem} são homens.\n"
      f"{mulher_menor} são mulheres com menos de 20 anos.")
