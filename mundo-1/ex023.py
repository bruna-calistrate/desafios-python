print("""Curso Python #9 - Manipulando Texto - Desafio 23

Vamos calcular a unidade, dezena, centena e milhar?""")

num = str(input('Digite um número inteiro de 0 a 9999: '))
form = str(f'{num:0>4}')

print(f"""O seu número é {form}
Milhar:  {form[0]}
Centena: {form[1]}
Dezena:  {form[2]}
Unidade: {form[3]}
""")

# Trabalhando matemagicamente:
num = int(input('Digite um número inteiro entre 0 e 9999: '))

print(f"""O seu número é: {num}
Milhar:  {num // 1000}
Centena: {num // 100 % 10}
Dezena:  {num // 10 % 10}
Unidade: {num // 1 % 10}""")
