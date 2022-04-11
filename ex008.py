print('Curso Python #7 - Operadores aritméticos - Desafio 08\n')
print('Vamos fazer uma conversão de metros para as outras formas de medida\n')
m = float(input('Medida em metros: '))
km = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000

print("""A sua medida em metros é \033[4;31m{:.3f}\033[m m, 
      Descendo as casas, a sua medida é:
      Em decímetros \033[4;33m{:.3f}\033[m dm,
      Em centímetros \033[4;32m{:.3f}\033[m cm e
      Em milímetros \033[4;34m{:.3f}\033[m mm.
      Subindo as casas, a sua medida é:
      Em decâmetros \033[4;36m{:.3f}\033[m dam,
      Em hectômetros \033[4;35m{:.3f}\033[m hm e
      Em quilômetros \033[4;37m{:.3f}\033[m km.""".format(m, dm, cm, mm, dam, hm, km))
