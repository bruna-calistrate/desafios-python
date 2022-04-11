print("""Curso Python - Mundo 2 Aula 12 - Condições Aninhadas - Desafio 43

Qual o seu IMC?""")

peso = float(input('Qual o seu peso? (kg) '))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"Com o peso {peso:.2f} kg e altura {altura:.2f} m, o seu IMC é:")

if imc < 18.5:
    print(f"Abaixo do peso - magreza - {imc:.1f}.\n"
          f"O peso ideal para sua altura está entre "
          f"{18.5 * (altura ** 2):.2f} kg e {25 * (altura ** 2):.2f} kg.")
elif imc <= 25:
    print(f"Peso ideal - normal - {imc:.1f}.\n"
          f"O peso ideal para sua altura está entre "
          f"{18.5 * (altura ** 2):.2f} kg e {25 * (altura ** 2):.2f} kg.")
elif imc <= 30:
    print(f"Sobrepeso - grau I - {imc:.1f}.\n"
          f"O peso ideal para sua altura está entre "
          f"{18.5 * (altura ** 2):.2f} kg e {25 * (altura ** 2):.2f} kg.")
elif imc <= 40:
    print(f"Obesidade - grau II - {imc:.1f}.\n"
          f"O peso ideal para sua altura está entre "
          f"{18.5 * (altura ** 2):.2f} kg e {25 * (altura ** 2):.2f} kg.")
else:
    print(f"Obesidade mórbida - grau III - {imc:.1f}.\n"
          f"O peso ideal para sua altura está entre "
          f"{18.5 * (altura ** 2):.2f} kg e {25 * (altura ** 2):.2f} kg.")
