print("""CursoPython - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 49

Vamos refazer a tabuada??
""")

num = int(input('Informe um número inteiro: '))
tabuada = f" Tabuada do {num} "
print(f"{tabuada:-^22}")
for c in range(1, 11):
    print(f"{'':5}{num:0>2} x {c:0>2} = {num * c:0>2}{'':5}")
