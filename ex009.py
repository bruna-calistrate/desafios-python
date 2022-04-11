print('Curso Python #7 - Operadores aritméticos - Desafio 09\n')
print('Vamos calcular a tabuada?')
num = int(input('Insira um número inteiro: \n'))

print('\033[1m---------Tabuada do {}---------\033[m'.format(num))
print("{} x 1 = \033[1;32;40m{:0>2}\033[m \033[1m~~~~~~\033[m {} x  6 = \033[1;32;40m{:0>2}\033[m \n"
      "{} x 2 = \033[1;32;40m{:0>2}\033[m \033[1m~~~~~~\033[m {} x  7 = \033[1;32;40m{:0>2}\033[m \n"
      "{} x 3 = \033[1;32;40m{:0>2}\033[m \033[1m~~~~~~\033[m {} x  8 = \033[1;32;40m{:0>2}\033[m \n"
      "{} x 4 = \033[1;32;40m{:0>2}\033[m \033[1m~~~~~~\033[m {} x  9 = \033[1;32;40m{:0>2}\033[m \n"
      "{} x 5 = \033[1;32;40m{:0>2}\033[m \033[1m~~~~~~\033[m {} x 10 = \033[1;32;40m{:0>2}\033[m".format(num, num*1, num, num*6,
                                                       num, num*2, num, num*7,
                                                       num, num*3, num, num*8,
                                                       num, num*4, num, num*9,
                                                       num, num*5, num, num*10))
print('{:-^30}'.format(''))
