print('Curso Python #7 - Operadores aritméticos - Desafio 10\n')
print('Conversão de moedas\n')

uss = float(input('Insira a cotação atual do dólar: US$ '))
eu = float(input('Insira a cotação atual do euro: € '))

conv = str(input("""
A partir de qual moeda você quer converter?
Real: rs
Dólar: uss
Euro: eu
""")).strip().lower()

if conv == 'rs':
    rss = float(input('\nInsira quantos reais você quer converter: R$ '))
    print('Conversão em dólar: US$ {:.2f}\n'
          'Conversão em euro: € {:.2f}\n'
          '{:-^30}'.format(rss / uss, rss / eu, ''))
    
if conv == 'uss':
    uss1 = float(input('\nInsira quantos dólares você quer converter: US$ '))
    print('Convertendo em reais: R$ {:.2f}\n'
          'Convertendo em euros: € {:.2f}\n'
          '{:-^30}'.format(uss * uss1, uss * (uss1 / eu), ''))
    
if conv == 'eu':
    eu1 = float(input('\nInsira quandos euros você quer converter: € '))
    print('Convertendo em reais: R$ {:.2f}\n'
          'Convertendo em dólares: US$ {:.2f}\n'
          '{:-^30}'.format(eu * eu1, eu * (eu1 / uss), ''))
