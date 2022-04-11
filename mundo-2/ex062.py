print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Quantos termos da PA você quer?
""")


cont = -1
termo = int(input("Informe o primeiro termo da PA: "))
r = int(input("Informe a razão da PA: "))
a = termo
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < (total - 1):
        cont += 1
        print(a + cont * r, end=' > ')
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))
print(f"PA concluída com {total} termos exibidos.")
