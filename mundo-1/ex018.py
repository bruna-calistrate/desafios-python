from math import sin, tan, cos, radians

print('Curso Python #8 - Utilizando módulos - Desafio 18\n'
      'Vamos calcular o seno, cosseno e tangente?\n')

ang = float(input('Insira um ângulo: '))
rad = radians(ang)

print(f'O ângulo {ang:.2f}° tem como: \n'
      f'seno     {sin(rad):.2f}, \n'
      f'cosseno  {cos(rad):.2f} e \n'
      f'tangente {tan(rad):.2f}.')
