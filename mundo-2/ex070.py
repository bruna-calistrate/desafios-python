cont = caro = soma = 0
print(f"{'':-^30}\n"
      f"{'Lojas Pônei':^30}\n"
      f"{'':-^30}")
while True:
    produto = str(input("Digite o nome do produto: ")).capitalize().strip()
    preco = float(input("Digite o valor do produto: R$ "))
    if preco >= 1000:
        caro += 1
    cont += 1
    soma += preco
    if cont == 1:
        barato_prod = produto
        barato_preco = preco
    else:
        if barato_preco > preco:
            barato_preco = preco
            barato_prod = produto
    r = str(input("Deseja inserir mais algum item [S/N]: ")).strip().upper()
    while r not in "NS":
        r = str(input("Deseja inserir mais algum item [S/N]: ")).strip().upper()
    if r in "Nn":
        break
print(f"\nForam comprados {cont} produtos, totalizando R$ {soma:.2f}\n"
      f"{caro} produtos custam mais de R$ 1000.00\n"
      f"{barato_prod} é o produto mais barato, custando R$ {barato_preco:.2f}")
