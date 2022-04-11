times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
         'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print(f"{'':-^50}\n"
      f"{'Tabela do Brasileirão 2021':^50}\n"
      f"{'':-^50}")
print(f"Os cinco primeiros colocados foram:\n"
      f"{times[:5]}\n"
      f"{'':-^50}")
print(f"Na lanterna, estão:\n"
      f"{times[-4:]}\n"
      f"{'':-^50}")
print(f"Equipes participantes em ordem alfabética:\n"
      f"{sorted(times)}\n"
      f"{'':-^50}")
print(f"A Chapecoense está em {times.index('Chapecoense') + 1}º lugar.\n"
      f"{'':-^50}")
