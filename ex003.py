print('Curso Python #4 - Primeiros comandos - Desafio 03')
print('')
print('Vamos fazer uma operação de soma?')

num01 = input('Insira o primeiro número: ')
num02 = input('Insira o segundo número: ')
cores = {'limpa': '\033[m',
         'verm': '\033[1;30;41m',
         'verd': '\033[1;30;42m'}
print('')
print(f"O resultado é: {cores['verm']}{num01+num02}{cores['limpa']}")

# isso apenas junta os dois números, concatenação, é necessária uma nova função para executar o código corretamente
print(f"Ops, algo errado não está certo... vamos tentar novamente?")
print('Processando...')
from time import sleep
sleep(5)

# função int determina que o valor será um número inteiro
print('')
total = int(num01) + int(num02)
# print('O resultado é: {}'.format(total))
print(f"A soma de {num01} e {num02}, é igual a {cores['verd']}{total}{cores['limpa']}!")
