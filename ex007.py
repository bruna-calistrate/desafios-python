print('Curso Python #7 - Operadores aritméticos - Desafio 07\n')

print('Vamos calcular a média de suas notas?')

n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
m = (n1 + n2) / 2

print('A média das notas é \033[1;35m>>{:.2f}<<\033[m.'.format(m))
