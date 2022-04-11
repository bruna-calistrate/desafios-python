# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome
print("""Curso Python #9 - Manipulando textos - Desafio 25
Você tem Silva no nome?
""")
nome = str(input('Qual o seu nome? ')).strip().title()

print(f"O seu nome é \033[1;32m{nome}\033[m")
silva = nome.find('Silva')
if silva >= 0:
    print('Você \033[1;30;42mtem\033[m o sobrenome Silva!')
else:
    print('Você \033[1;30;41mnão\033[m tem o sobrenome Silva!')

# outro método:
# silva = 'Silva' in nome
# print(f'Você tem Silva no nome? {silva}')
