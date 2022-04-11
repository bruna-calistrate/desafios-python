print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for

Vamos determinar a média de idades, o homem mais velho e quantas mulheres têm menos de 20 em um grupo de 4 pessoas""")

homem_nome = []
homem_idade = []
med = 0
menor = 0
for c in range(1, 5):
    print(f'\n----{c}ª PESSOA ----')
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M ou F): ")).strip().upper()
    med += idade
    if sexo == 'M':
        homem_idade.append(idade)
        homem_nome.append(nome)
    elif sexo == "F":
        if idade < 20:
            menor += 1
    else:
        print("Você selecionou a opção errada, tente novamente.")
mais_velho = max(homem_idade)
pos = homem_idade.index(mais_velho)
nome_h = homem_nome[pos]

print(f"\nA média das idades entre as 4 pessoas é {med/4:.1f} anos.\n"
      f"{nome_h} é o homem mais velho com {mais_velho} anos.\n"
      f"Entre as mulheres, {menor} têm menos de 20 anos.")
