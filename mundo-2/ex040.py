print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 40

Vamos calcular a sua média?""")

nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2)/2

if media < 5:
    print(f"Fazendo a média entre as notas {nota1:.2f} e {nota2:.2f}, você atingiu {media:.2f} pontos. "
          f"Estude mais, você foi REPROVADO!")
elif media >= 7:
    print(f"Fazendo a média entre as notas {nota1:.2f} e {nota2:.2f}, você atingiu {media:.2f} pontos. "
          f"Parabéns, você foi APROVADO!")
else:
    print(f"Fazendo a média entre as notas {nota1:.2f} e {nota2:.2f}, você atingiu {media:.2f} pontos. "
          f"Você está de \033[1;33mRECUPERAÇÃO\033[m!")

# REVISÃO: reduzindo um pouco mais o código, evitar as repetições
nota1 = float(input('Qual foi a sua primeira nota? '))
nota2 = float(input('Qual foi a sua segunda nota? '))
media = (nota1 + nota2)/2
print(f"Fazendo a média entre as notas {nota1:.2f} e {nota2:.2f}, você atingiu {media:.2f} pontos.")
if media < 5:
    print("Estude mais, você foi REPROVADO!")
elif media >= 7:
    print("Parabéns, você foi APROVADO!")
else:
    print("Você está de RECUPERAÇÃO!")
