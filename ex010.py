print('Curso Python #7 - Operadores aritméticos - Desafio 10\n')
print('Conversão de moedas\n')
uss = float(input('Insira a cotação atual do dólar: US$ '))
eu = float(input('Insira a cotação atual do euro: € '))
bdm = float(input('Insira a cotação atual do BDM: '))

conv = str(input("""
A partir de qual moeda você quer converter?
Real: rs
Dólar: uss
Euro: eu
BDM: bdm
""")).strip().lower()

if conv == 'rs':
    rss = float(input('\nInsira quantos reais você quer converter: R$ '))
    print('Conversão em dólar: \033[1;34mUS$ {:.2f}\033[m\n'
          'Conversão em euro: \033[1;32m€ {:.2f}\033[m\n'
          'Conversão em BDM: \033[1;33m{:.2f}\033[m\n'
          '{:-^30}'.format(rss / uss, rss / eu, rss / bdm, ''))
if conv == 'uss':
    uss1 = float(input('\nInsira quantos dólares você quer converter: US$ '))
    print('Convertendo em reais: \033[1;31mR$ {:.2f}\033[m\n'
          'Convertendo em euros: \033[1;32m€ {:.2f}\033[m\n'
          'Convertendo em BDM: \033[1;33m{:.2f}\033[m\n'
          '{:-^30}'.format(uss * uss1, uss * (uss1 / eu), uss * (uss1 / bdm), ''))
if conv == 'eu':
    eu1 = float(input('\nInsira quandos euros você quer converter: € '))
    print('Convertendo em reais: \033[1;31mR$ {:.2f}\033[m\n'
          'Convertendo em dólares: \033[1;34mUS$ {:.2f}\033[m\n'
          'Convertendo em BDM: \033[1;33m{:.2f}\033[m\n'
          '{:-^30}'.format(eu * eu1, eu * (eu1 / uss), eu * (eu1 / bdm), ''))
if conv == 'bdm':
    bdm1 = float(input('\nInsira quantos BDMs você quer converter: '))
    print("""Convertendo em reais: \033[1;31mR$ {:.2f}\033[m
          Convertendo em dólares: \033[1;34mUS$ {:.2f}\033[m
          Convertendo em euros: \033[1;32m€ {:.2f}\033[m
          {:-^30}""".format(bdm * bdm1, bdm * (bdm1 / uss), bdm * (bdm1 / eu)))
