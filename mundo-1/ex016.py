from math import trunc, floor

print('Curso Python #8 - Utilizando Módulos - Desafio 16\n')

num = float(input('Digite um número com casas decimais: '))

print('O número digitado {} tem a porção inteira {}.\n'
      'Ou, arredondando para baixo: {}'.format(num, trunc(num), floor(num)))
