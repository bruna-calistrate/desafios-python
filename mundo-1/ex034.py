print("""Curso Python #10 - Condições Simples e Compostas - Desafio 34

Vamos calcular o seu aumento?""")

sal = float(input("Digite o seu salário: R$ "))

if sal > 1250:
    print(f"Com aumento de 10%, o seu salário passará de "
          f"R$ {sal:.2f} para R$ {sal * 1.1:.2f}.")
else:
    print(f"Com aumento de 15%, o seu salário passará de "
          f"R$ {sal:.2f} para R$ {sal * 1.15:.2f}.")
