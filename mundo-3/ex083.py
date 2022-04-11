exp = []
mat = str(input("Digite uma expressão: "))
for c in mat:
    exp.append(c)
abre = exp.count('(')
pabre = exp.index('(')
fecha = exp.count(')')
pfecha = exp.index(')')
tot = abre + fecha
ptot = pabre - pfecha

print(mat)
if tot % 2 == 0 and ptot < 0:
    print("A expressão é válida")
else:
    print("A expressão é inválida")
