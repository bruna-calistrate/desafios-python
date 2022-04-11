print("""Curso Python #9 - Manipulando Textos - Desafio 26
Vamos contar quantas vezes alguma letra aparece em uma frase?
""")

frase = str(input('Digite uma frase: ')).strip().upper()
car = str(input('Qual letra você gostaria de identificar? ')).strip().upper()

print(f"""A sua frase é: {frase}.

A sua frase possui {len(frase)} caracteres
A sua frase possui {frase.count(car)} letras >> {car} <<
A letra >> {car} << aparece pela primeira vez na {frase.find(car)+1}ª posição
A letra >> {car} << aparece pela  última  vez na {frase.rfind(car)+1}ª posição""")
