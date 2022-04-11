from pygame import mixer

print('Curso Python #8 - Utilizando módulos - Desafio 21\n'
      'Reproduzindo uma música\n\n')

mixer.init()
mixer.music.load('ex021_mus.mp3')
# mus = input('Insira o caminho do arquivo .mp3: ')
# mixer.music.load(mus)
mixer.music.play()
input('Está ouvindo agora?')
