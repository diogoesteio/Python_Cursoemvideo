times = ('Grêmio', 'Inter', 'Flamengo', 'Corinthians', 'Fluminense',
         'Santo', 'Vasco', 'Botafogo', 'Chapecoense', 'Botafogo',
         'Coritiba', 'São Paulo', 'Red Bull', 'Palmeiras', 'Sport'
         'Bahia', 'Vitória', 'Cruzeiro', 'Atlético', 'Juventude')
print('-=-' * 20)
print(f'Lista de times do brasileirão: {times}')
print('-=-' * 20)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=-' * 20)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=-' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}° posição.')
