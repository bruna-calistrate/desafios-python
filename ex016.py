print('Curso Python #8 - Utilizando Módulos - Desafio 16\n')
from math import trunc, floor
num = float(input('Digite um número com casas decimais: '))
print('O número digitado \033[1;32m{}\033[m tem a porção inteira \033[1;34m{}\033[m.\n'
      'Ou, arredondando para baixo: \033[1;36m{}\033[m'.format(num, trunc(num), floor(num)))

