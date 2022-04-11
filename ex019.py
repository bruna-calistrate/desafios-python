print('Curso Python #8 - Utilizando módulos - Desafio 19\n'
      'Vamos fazer um sorteio?\n')
from random import choice

a1 = str(input('Qual o nome do primeiro aluno? ')).strip().title()
a2 = str(input('Qual o nome do segundo aluno? ')).strip().title()
a3 = str(input('Qual o nome do terceiro aluno? ')).strip().title()
a4 = str(input('Qual o nome do quarto aluno? ')).strip().title()
lista = [a1, a2, a3, a4] # Listas devem estar entre colchetes
print('\nEntre os alunos {}, {}, {} e {}, o sorteado para apagar o quadro é:\n'
      '\033[1;30;42m>>> {} <<<\033[m'.format(a1, a2, a3, a4, choice(lista)))
