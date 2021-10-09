times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
         'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('-=' * 20)
print(f'Lista dos times do Brasileirão em 2018: {times}')
print('-=' * 20)
print(f'Os cinco primeiros times são: {times[0:5]}')
print('-=' * 20)
print(f'Os quatro ultimos times são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')