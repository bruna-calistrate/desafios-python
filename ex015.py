print('Curso Python ##Extra - Tratando dados e fazendo contas - Desafio 15\n\n'
      'Calculo de aluguel de carro')
d = int(input('Insira a quantidade de dias que o carro foi alugado: '))
km = float(input('Insira a quantidade de km rodados: '))
print('O carro foi alugado por \033[1;34m{} dias\033[m e rodou \033[1;32m{:.2f} km\033[m.\n'
      'O valor do aluguel será: \033[4;42m>> R$ {:.2f} <<\033[m'
      .format(d, km, d * 60 + km * 0.15))
