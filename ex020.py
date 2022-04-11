print('Curso Python #8 - Utilizando módulos - Desafio 20\n'
      'Vamos sortear a ordem de apresentação?\n')
from random import sample, shuffle

a1 = str(input('Qual o nome do primeiro aluno? ')).strip().title()
a2 = str(input('Qual o nome do segundo aluno? ')).strip().title()
a3 = str(input('Qual o nome do terceiro aluno? ')).strip().title()
a4 = str(input('Qual o nome do quarto aluno? ')).strip().title()
deck = [a1, a2, a3, a4]

print('A ordem de apresentação dos alunos {}, {}, {} e {} será:\n'
      '\033[1;30;44m{}\033[m.\n'.format(a1, a2, a3, a4, sample(deck, k=4)))

shuffle(deck) # Embaralha a lista, não precisa jogar como função
print('Outra maneira é: \n'
      '\033[1;30;45m{}\033[m.'.format(deck))
