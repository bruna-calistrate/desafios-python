print('Curso Python #7 - Operadores aritméticos - Desafio 06\n')

n1 = float(input('Insira um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print("""O seu número é \033[1;32m{}\033[m, 
o seu dobro é \033[1;31m{}\033[m, 
o seu triplo é \033[1;33m{}\033[m e 
a sua raiz quadrada é \033[1;34m{:.2f}\033[m."""
      .format(n1, dobro, triplo, raiz))
