print('Curso Python #7 - Operadores aritméticos - Desafio 12\n\n'
      'PROMOÇÃO!! DESCONTO DE 5%\n')
val = float(input('Qual o valor atual do produto? R$ '))
des = val * .95
print('O produto que custava \033[1;31mR$ {:.2f}\033[m, com desconto de 5%, '
      'agora vale \033[1;32mR$ {:.2f}\033[m!'.format(val, des))
print('Agora vamos calcular o pagamento à vista e à prazo!')
vista = val * 0.9
print('Pagando à vista, o produto custará: \033[1;42mR$ {:.2f}\033[m!\n\n'.format(vista))
n = int(input('Quantas parcelas? '))
par = (val / n) + (n * 0.5)

print('Pagando em \033[1m{}\033[m parcelas, cada uma custará \033[1;35mR$ {:.2f}\033[m, totalizando \033[1;31mR$ {:.2f}\033[m.'
      .format(n, par, n * par))
