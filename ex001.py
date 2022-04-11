print('\033[1;40mCurso Python Mundo 1 - Aula #4 - Primeiros comandos - Desafio 01\33[m')

# Quando entre aspas, inserir os espaços para que o comando fique mais organizado
nome = str(input("Qual o seu nome? ")).strip().title()
print('Bem vinde, {}!'.format(nome))

# formato anterior, mais manual print('Bem vinde,', nome + '!')
import emoji
print(emoji.emojize("Obrigada por testar comigo! :smiley:", use_aliases=True))
