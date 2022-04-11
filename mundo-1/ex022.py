print("""Curso Python #9 - Manipulando Texto - Desafio 22

>>Vamos formatar o seu nome?<<
""")
nome = str(input('Digite o seu nome completo: ')).strip().title()
div = nome.split()
print(f"""O seu nome é {nome}

Em CapsLOKA: {nome.upper()}
Em minúscula: {nome.lower()}

O seu primeiro nome tem {len(div[0])} letras
O seu nome tem {len(''.join(div))} letras no total""")
