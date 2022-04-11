from math import ceil

print("""Curso em Vídeo - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 36
Vamos calcular o seu empréstimo?
""")

casa = float(input("Qual o valor da casa que você deseja comprar? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos = int(input("Em quantos anos você deseja pagar? "))
par = (casa / (12 * anos))

print(f"\n"
      f"Recebendo R$ {salario:.2f} e pagando em {anos} anos, o valor de cada parcela será de R$ {par:.2f}.")
if par / salario <= 0.3:
    print(f"O seu empréstimo foi APROVADO.")
else:
    print(f"O seu empréstimo foi: NEGADO.\n"
          f"Sugerimos pagamento em {ceil(casa / (3.6 * salario))} anos para aprovação.")
    
