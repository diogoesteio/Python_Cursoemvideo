from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = {}
print('=-=' * 15)
print('Valores Sorteados: ')
print('=-=' * 15)
for k, v in jogo.items():
    print(f'{k} tirou o número {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-=' * 15)
print('A colocação dos jogadores ficou:')
for k, v in enumerate(ranking):
    print(f'Em {k+1}° lugar ficou o {v[0]} que tirou {v[1]}')
    sleep(1)
