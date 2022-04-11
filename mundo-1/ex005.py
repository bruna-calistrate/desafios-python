print('Curso Python #7 - Operadores aritméticos - Desafio 05\n')

n1 = int(input('Insira um número: '))
sus = n1 + 1
ant = n1 - 1

print('\nO número é {}, 
      'seu sucessor é {} e 
      'seu antecessor é {}.'
      .format(n1, sus, ant))

# Outra forma de exibir o resultado seria assim, economizando duas variáveis:
print('O número é {}, '
      'seu sucessor é {} e '
      'seu antecessor é {}'
      .format(n1, (n1 +1), (n1 - 1))
