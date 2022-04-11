from emoji import emojize
from time import sleep

print("""Curso Python - Mundo 2 Aula 13 - Estrutura de repetição for - Desafio 46

Contagem regressiva para o ano novo!! \U0001f386
""")

for c in range(10, -1, -1):
    print(f">{c:^53}<")
    sleep(1)
    
print(emojize(f"{':tada::fireworks:' * 5} FELIZ ANO NOVO!! {':tada::fireworks:' * 5}",
              use_aliases=True))
