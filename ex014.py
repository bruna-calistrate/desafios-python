print('Curso Python ##Extra - Tratando dados e fazendo contas - Desafio 14\n'
      'Conversão de escalas termométricas\n')

temp = input("A partir de qual unidade de medida você quer converter? C, F ou K? \n").strip().upper()

if temp == 'C':
      c = float(input('Insira a temperatura em Celsius para conversão: '))
      f = (c * 1.8) + 32
      k = c + 273
      print('A temperatura \033[1;34m{:.1f}°C\033[m corresponde a:\n'
      '\033[1;33m{:.1f}° Fahrenheit\033[m e \033[1;35m{:.1f} Kelvin\033[m.\n'
      '{:-^30}'.format(c, f, k, ''))
if temp == 'F':
      f = float(input('Insira a temperatura em Fahrenheit para conversão: '))
      c = (f - 32) / 1.8
      k = c + 273
      print('A temperatura \033[1;33m{:.1f}°F\033[m corresponde a:\n'
      '\033[1;34m{:.1f}° Celsius\033[m e \033[1;35m{:.1f} Kelvin\033[m.\n'
      '{:-^30}'.format(f, c, k, ''))
if temp == 'K':
      k = float(input('Insira a temperatura em Kelvin para conversão: '))
      c = k - 273
      f = (c * 1.8) + 32
      print('A temperatura \033[1;35m{:.1f} Kelvin\033[m corresponde a:\n'
      '\033[1;34m{:.1f}° Celsius\033[m e \033[1;33m{:.1f}° Fahrenheit\033[m.'.format(k, c, f))
