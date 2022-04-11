print('Curso Python ##Extra - Tratando dados e fazendo contas - Desafio 15\n\n'
      'Calculo de aluguel de carro')

d = int(input('Insira a quantidade de dias que o carro foi alugado: '))
km = float(input('Insira a quantidade de km rodados: '))

print('O carro foi alugado por {} dias e rodou {:.2f} km.\n'
      'O valor do aluguel será: >> R$ {:.2f} <<'
      .format(d, km, d * 60 + km * 0.15))
