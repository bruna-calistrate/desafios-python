print('Curso Python #7 - Operadores aritméticos - Desafio 06\n')

n1 = float(input('Insira um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
# Outra forma de se calcular é com o comando: 
# pow(n1, 1/2)

print("""O seu número é {}, 
o seu dobro é {}, 
o seu triplo é {} e 
a sua raiz quadrada é {:.2f}."""
      .format(n1, dobro, triplo, raiz))

# O desafio também pode ser feito sem as variáveis como no anterior
