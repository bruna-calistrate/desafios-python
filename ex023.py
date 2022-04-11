print("""Curso Python #9 - Manipulando Texto - Desafio 23
Vamos calcular a unidade, dezena, centena e milhar?""")
num = str(input('Digite um número inteiro de 0 a 9999: '))
form = str(f'{num:0>4}')

print(f"""O seu número é \033[1;30;43m{form}\033[m
Milhar:  \033[1;35m{form[0]}\033[m
Centena: \033[1;34m{form[1]}\033[m
Dezena:  \033[1;32m{form[2]}\033[m
Unidade: \033[1;33m{form[3]}\033[m
""")

# Trabalhando matemagicamente:
# num = int(input('Digite um número inteiro entre 0 e 9999: '))

# print(f"""O seu número é: {num}
# Milhar:  {num // 1000}
# Centena: {num // 100 % 10}
# Dezena:  {num // 10 % 10}
# Unidade: {num // 1 % 10}""")
