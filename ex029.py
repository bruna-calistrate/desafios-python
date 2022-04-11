print("""Curso Python #10 - Condições Simples e Compostas

Você vai ser multado? Vamos descobrir
""")

km = float(input('Qual a velocidade atual do seu veículo? '))
multa = (km - 80) * 7

if km > 80:
    print(f"\033[1;30;41m Você está acima do limite de 80 km/h!! Você deverá pagar uma multa de R$ {multa:.2f}!! \033[m")
else:
    print("\033[1;30;42m Tenha um bom dia! Dirija com segurança! \033[m")
