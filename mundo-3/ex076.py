vendinha = ('Refrigerante', 3,
            'Suco', 3,
            'Pastel', 4.5,
            'Pão de Queijo', 2.30,
            'Enrolado', 5.20,
            'Vitamina', 8,
            'Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
print(f"{'':-^50}\n"
      f"{'Vendinha Pônei':^50}\n"
      f"{'':-^50}")
for c in range(0, len(vendinha), 2):
    print(f"{vendinha[c]:.<40} R$ {vendinha[c + 1]:6.2f}")
print(f"{'':-^50}")