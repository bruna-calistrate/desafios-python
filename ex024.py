print("""Curso Python #9 - Manipulando Texto - Desafio 24
A sua cidade tem Sant(o/a) no nome?
""")

cid = str(input('Qual o nome da sua cidade? ')).strip().title()

print(f"A sua cidade é {cid}."
      f"")
santo = cid.find('Santo' and 'Santa')

if santo >= 0:
    print("E possui a palavra Sant(o/a).\n")
else:
    print("E >>não<< possui a palavra Santo.\n")

# Agora fazendo apenas com a primeira palavra Santo.
print(f"""A sua cidade começa com Santo? {cid[:5] =='Santo'}.
A sua cidade começa com Santa? {cid[:5]=='Santa'}""")
