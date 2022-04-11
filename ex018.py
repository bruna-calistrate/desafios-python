print('Curso Python #8 - Utilizando módulos - Desafio 18\n'
      'Vamos calcular o seno, cosseno e tangente?\n')
from math import sin, tan, cos, radians

ang = float(input('Insira um ângulo: '))
rad = radians(ang)
print(f'O ângulo \033[4;47m{ang:.2f}°\033[m tem como: \n'
      f'seno     \033[1;30;42m{sin(rad):.2f}\033[m, \n'
      f'cosseno  \033[1;30;44m{cos(rad):.2f}\033[m e \n'
      f'tangente \033[1;30;45m{tan(rad):.2f}\033[m.')
