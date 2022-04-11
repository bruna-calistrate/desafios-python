print("""Curso Python - Mundo 2 Aula 14 - Estrutura de repetição while

Vamos fazer algumas operações
""")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
c = 0
while c != 5:
    c = int(input("\nSelecione uma das opções abaixo: \n"
                  "[1] somar \n"
                  "[2] multiplicar \n"
                  "[3] maior \n"
                  "[4] inserir novos números \n"
                  "[5] sair do programa\n"))
    if c == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif c == 2:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif c == 3:
        print(f"O maior número entre {num1} e {num2} é >>{max(num1, num2)}<<")
    elif c == 4:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    elif c == 5:
        print("Finalizando...")
    else:
        print("Opção inválida, digite novamente.")
print("Fim do programa")
