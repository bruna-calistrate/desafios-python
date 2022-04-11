print('Curso Python #7 - Operadores aritméticos - Desafio 11\n'
      'Quantos litros de tinta preciso para pintar essa parede?')
lar = float(input('Insira a largura da parede em metros: '))
alt = float(input('Insira a altura da parede em metros: '))
area = lar * alt
lit = area / 2
print('Sua parede tem a dimensão de \033[1;37m{:.3f} m x {:.3f} m\033[m e sua área é de \033[1;32m{:.3f} m²\033[m\n'
      'Serão necessários \033[1;31m{:.3f} l\033[m de tinta para pintar essa parede.'
      .format(lar, alt, area, lit))

