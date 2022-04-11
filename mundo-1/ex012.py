print('Curso Python #7 - Operadores aritméticos - Desafio 12\n\n'
      'PROMOÇÃO!! DESCONTO DE 5%\n')

val = float(input('Qual o valor atual do produto? R$ '))
des = val * .95
print('O produto que custava R$ {:.2f}, com desconto de 5%, '
      'agora vale R$ {:.2f}!'.format(val, des))

print('Agora vamos calcular o pagamento à vista e à prazo!')
vista = val * 0.9
print('Pagando à vista, o produto custará: R$ {:.2f}!\n\n'.format(vista))

n = int(input('Quantas parcelas? '))
par = (val / n) + (n * 0.5)

print('Pagando em {} parcelas, cada uma custará R$ {:.2f}, totalizando R$ {:.2f}.'
      .format(n, par, n * par))
