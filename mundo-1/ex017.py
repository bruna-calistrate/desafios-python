from math import hypot

print('Curso Python #8 - Utilizando módulos - Desafio 17\n'
      'Vamos calcular o valor da hipotenusa de um triângulo retângulo?\n')

cat_a = float(input('Insira o valor do cateto oposto: '))
cat_b = float(input('Insira o valor do cateto adjacente: '))
print('A hipotenusa com os catetos {} e {} é igual a {:.3f}.'
      .format(cat_a, cat_b, hypot(cat_a, cat_b)))
