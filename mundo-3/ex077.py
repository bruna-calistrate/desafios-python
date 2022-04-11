palavras = ('batata', 'arroz', 'feijão', 'tomate', 'cebola', 'alface', 'açúcar', 'macarrão', 'coco', 'queijo')
vogal = 'AÁÃÂEÉIÉOÓÕUÚ'

for palavra in palavras:
    palavra = palavra.upper()
    print(f"\nA palavra {palavra} possui as vogais ", end='')
    for letra in palavra:
        if letra in vogal:
            print(letra, end=' ')

