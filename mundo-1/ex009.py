print('Curso Python #7 - Operadores aritméticos - Desafio 09\n')
print('Vamos calcular a tabuada?')

num = int(input('Insira um número inteiro: \n'))

print('\n---------Tabuada do {}---------'.format(num))
print("{} x 1 = {:0>2} ~~~~~~ {} x  6 = {:0>2} \n"
      "{} x 2 = {:0>2} ~~~~~~ {} x  7 = {:0>2} \n"
      "{} x 3 = {:0>2} ~~~~~~ {} x  8 = {:0>2} \n"
      "{} x 4 = {:0>2} ~~~~~~ {} x  9 = {:0>2} \n"
      "{} x 5 = {:0>2} ~~~~~~ {} x 10 = {:0>2}"
      .format(num, num*1, num, num*6,
              num, num*2, num, num*7,
              num, num*3, num, num*8,
              num, num*4, num, num*9,
              num, num*5, num, num*10))
print('{:-^30}'.format(''))
