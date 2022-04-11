print("""Curso Python #9 - Manipulando textos - Desafio 27
Vamos formatar o seu nome?
""")

nome = str(input('Qual o seu nome completo? ')).strip().title()
lista = nome.split()

print(f"""O seu nome completo é {nome}
O seu primeiro nome é {lista[0]}
O seu  último  nome é {lista[-1]}

Seu nome simplificado é {lista[0]} {lista[-1]}""")
