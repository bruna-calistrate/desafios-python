print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 44 

Condições de pagamento, vamos calcular o preço final do produto.
""")

print(f"{'CASAS PÔNEI':-^40}")
valor = float(input("Qual o valor do produto? R$ "))
pag = int(input("Escolha a forma de pagamento:\n"
                "1 - À vista com dinheiro\n"
                "2 - À vista no débito\n"
                "3 - Parcelado no crédito\n"))

if pag == 1:
    print(f"Pagando à vista no dinheiro, o produto de R$ {valor:.2f} "
          f"passará a valer R$ {valor*0.9:.2f}!")
elif pag == 2:
    print(f"Pagando no débito, o produto deR$ {valor:.2f} "
          f"passará a valer \033[1;32mR$ {valor*0.95:.2f}!")
elif pag == 3:
    parc = int(input("Em quantas parcelas você gostaria de pagar? "))
    if parc <= 2:
        print(f"Parcelando em {parc}x de R$ {valor/parc:.2f} "
              f"o produto custará o mesmo.")
    else:
        juros = valor * 1.2
        print(f"Parcelando em {parc}x de R$ {juros/parc:.2f}"
              f"o valor final do produto será R$ {juros:.2f}.")
else:
    print("Você selecionou a opção errada, tente novamente.")
