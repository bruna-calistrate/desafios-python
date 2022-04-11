print('Curso Python ##Extra - Tratando dados e fazendo contas - Desafio 14\n'
      'Conversão de escalas termométricas\n')

temp = input("A partir de qual unidade de medida você quer converter? C, F ou K? \n").strip().upper()

if temp == 'C':
      c = float(input('Insira a temperatura em Celsius para conversão: '))
      f = (c * 1.8) + 32
      k = c + 273
      print('A temperatura {:.1f}°C corresponde a:\n'
      '{:.1f}° Fahrenheit e {:.1f} Kelvin.\n'
      '{:-^30}'.format(c, f, k, ''))
if temp == 'F':
      f = float(input('Insira a temperatura em Fahrenheit para conversão: '))
      c = (f - 32) / 1.8
      k = c + 273
      print('A temperatura {:.1f}°F corresponde a:\n'
      '{:.1f}° Celsius e {:.1f} Kelvin.\n'
      '{:-^30}'.format(f, c, k, ''))
if temp == 'K':
      k = float(input('Insira a temperatura em Kelvin para conversão: '))
      c = k - 273
      f = (c * 1.8) + 32
      print('A temperatura {:.1f} Kelvin corresponde a:\n'
      '{:.1f}° Celsius e {:.1f}° Fahrenheit.'.format(k, c, f))
