ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
cont = "S"

while True:
    if cont == "S":
        num = int(input("Digite um número inteiro: "))
        if 0 <= num < len(ext):
            print(f"Você digitou o número {ext[num]}.")
        else:
            print("Tente novamente...")
    if cont == "N":
        break
    cont = str(input("Deseja continuar? [S/N] ")).upper().strip()
    while cont not in "SN":
        cont = str(input("Deseja continuar? [S/N] ")).upper().strip()
