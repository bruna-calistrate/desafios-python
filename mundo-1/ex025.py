print("""Curso Python #9 - Manipulando textos - Desafio 25
Você tem Silva no nome?
""")
nome = str(input('Qual o seu nome? ')).strip().title()

print(f"O seu nome é {nome}")
silva = nome.find('Silva')
if silva >= 0:
    print('Você tem o sobrenome Silva!')
else:
    print('Você não tem o sobrenome Silva!')

# outro método:
silva = 'Silva' in nome
print(f'Você tem Silva no nome? {silva}')
