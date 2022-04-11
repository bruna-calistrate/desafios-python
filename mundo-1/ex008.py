print('Curso Python #7 - Operadores aritméticos - Desafio 08\n')
print('Vamos fazer uma conversão de metros para as outras formas de medida\n')

m = float(input('Medida em metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000

print("""A sua medida em metros é {:.3f} m.

      Descendo as casas, a sua medida é:
      Em decímetros {:.3f} dm,
      Em centímetros {:.3f} cm e
      Em milímetros {:.3f} mm.
      
      Subindo as casas, a sua medida é:
      Em decâmetros {:.3f} dam,
      Em hectômetros {:.3f} hm e
      Em quilômetros {:.3f} km."""
      .format(m, dm, cm, mm, dam, hm, km))
