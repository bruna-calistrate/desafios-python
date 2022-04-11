from datetime import date

print(f"""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 39

Você deve se alistar?
""")

ano = int(input("Em qual ano você nasceu? "))
hoje = date.today().year
idade = int(hoje - ano)
sexo = str(input("Informe o seu gênero biológico: \n"
                 "M - Masculino\n"
                 "F - Feminino\n")).strip().upper()

if sexo == "M":
    print("\n"
          "O seu alistamento é obrigatório!")
    if idade > 18:
        print(f"Você tem {idade} anos e está atrasado há {idade - 18} anos.\n"
              f"Seu alistamento foi em {ano + 18}.")
    elif idade == 18:
        print(f"Você completa 18 anos neste ano, você deve se alistar imediatamente!")
    elif idade < 18:
        print(f"Você tem {idade} anos e deverá se alistar em {18 - idade} anos. \n"
              f"Seu alistamento será em {ano + 18}.")
elif sexo == "F":
    print("\n"
          "O seu alistamento não é obrigatório. Caso deseje se alistar:")
    if idade > 18:
        print(f"Você tem {idade} anos e poderia se alistar há {idade - 18} anos.\n"
              f"Seu alistamento foi em {ano + 18}.")
    elif idade == 18:
        print(f"Você completa 18 anos neste ano, você pode se alistar.")
    elif idade < 18:
        print(f"Você tem {idade} anos e poderá se alistar em {18 - idade} anos. \n"
              f"Seu alistamento será em {ano + 18}.")
else:
    print("Por favor, selecione a opção correta. Tente novamente.")
    
