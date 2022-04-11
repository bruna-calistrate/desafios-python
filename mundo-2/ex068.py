from random import randrange

cont = 0
while True:
    p_ou_i = " "
    computador = randrange(0, 5)
    while p_ou_i not in "PI":
        p_ou_i = str(input("Par ou Ímpar? [P/I] ")).strip().upper()
    jogador = int(input("Escolha um número entre 0 e 5: "))
    soma = computador + jogador
    cont += 1
    if p_ou_i in "P":
        if soma % 2 == 0:
            break
        else:
            print(f"Você jogou {jogador} e eu {computador}, a soma deu {soma}. VENCI!!")
    elif p_ou_i in "I":
        if soma % 2 == 0:
            print(f"Você jogou {jogador} e eu {computador}, a soma deu {soma}. VENCI!!")
        else:
            break
    print("Vamos jogar novamente...")

print(f"\nParabéns, você venceu após {cont} tentativas. Você jogou {jogador} e eu {computador}, a soma deu {soma}")
if p_ou_i == "P":
    pi = "PAR"
elif p_ou_i == "I":
    pi = "ÍMPAR"
print(f"Você escolheu {pi}!")
