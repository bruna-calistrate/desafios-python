print('Curso Python #7 - Operadores aritméticos - Desafio 11\n'
      'Quantos litros de tinta preciso para pintar essa parede?')

lar = float(input('Insira a largura da parede em metros: '))
alt = float(input('Insira a altura da parede em metros: '))
area = lar * alt
lit = area / 2

print('Sua parede tem a dimensão de {:.3f} m x {:.3f} m e sua área é de {:.3f} m² \n'
      'Serão necessários {:.3f} l de tinta para pintar essa parede.'
      .format(lar, alt, area, lit))
