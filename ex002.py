print('Curso Python #4 - Primeiros comandos - Desafio 02')
print('')
dia = int(input('Em qual dia você nasceu? '))
mes = int(input('Em qual mês você nasceu? '))
ano = int(input('Em qual ano você nasceu? '))
print('')

# Lembrar de sempre por + ou , para conectar todos os elementos do comando
print(f'Você nasceu em \033[7;36;40m{dia:0>2}/{mes:0>2}/{ano}\033[m')
print('')
print('Obrigada!')
