print("""Curso Python #9 - Manipulando Texto - Desafio 22

>>Vamos formatar o seu nome?<<
""")
nome = str(input('Digite o seu nome completo: ')).strip().title()
div = nome.split()
print(f"""O seu nome é \033[4;37m{nome}\033[m

Em CapsLOKA: \033[1;31m{nome.upper()}\033[m
Em minúscula: \033[1;36m{nome.lower()}\033[m

O seu primeiro nome tem \033[4;35m{len(div[0])}\033[m letras
O seu nome tem \033[4;34m{len(''.join(div))}\033[m letras no total""")
