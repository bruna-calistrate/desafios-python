print('Curso Python #6 - Tipos primitivos e saída de dados - Desafio 04')
print('')

info = input('Digite algo: ')
print('')

print('O seu tipo primitivo é', type(info))
print('É um número inteiro?', info.isnumeric())
print('É alfabético?', info.isalpha())
print('É alfanumérico?', info.isalnum())
print('Está em maiúsculas?', info.isupper())
print('Está em minúsculas?', info.islower())
print('Está captalizada?', info.istitle())
print('Só tem espaços?', info.isspace())
print('')

cores = {'amarelo': '\033[1;33m',
         'limpa': '\033[m'}
print(f"""O seu tipo primitivo é {cores['amarelo']}{type(info)}{cores['limpa']}. 
É um número inteiro? {cores['amarelo']}{info.isnumeric()}{cores['limpa']}. 
É alfabético? {cores['amarelo']}{info.isalpha()}{cores['limpa']}. 
É alfanumérico? {cores['amarelo']}{info.isalnum()}{cores['limpa']}. 
Está em maiúsculas? {cores['amarelo']}{info.isupper()}{cores['limpa']}. 
Está em minúsculas? {cores['amarelo']}{info.islower()}{cores['limpa']}. 
Está captalizado? {cores['amarelo']}{info.istitle()}{cores['limpa']}. 
Só tem espaços? {cores['amarelo']}{info.isspace()}{cores['limpa']}""")
