print('Curso Python #8 - Utilizando módulos - Desafio 17\n'
      'Vamos calcular o valor da hipotenusa de um triângulo retângulo?\n')
from math import hypot
cat_a = float(input('Insira o valor do cateto oposto: '))
cat_b = float(input('Insira o valor do cateto adjacente: '))
print('A hipotenusa com os catetos \033[1;32m{}\033[m e \033[1;32m{}\033[m é igual a \033[1;35m{:.3f}\033[m.'
      .format(cat_a, cat_b, hypot(cat_a, cat_b)))

# A soma dos quadrados dos catetos é o quadrado da hipotenusa
