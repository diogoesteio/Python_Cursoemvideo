infos = dict()
partidas = list()
infos['nome'] = str(input('Nome do Jogador: '))
valor = int(input(f'Quantas partidas {infos["nome"]} jogou? '))
total = 0
for c in range(0, valor):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
infos['gols'] = partidas[:]
infos['total'] = sum(partidas)
print('=-=' * 20)
print(infos)
print('=-=' * 20)
for k, v in infos.items():
    print(f'O campo {k} tem o valor {v}')
print('=-=' * 20)
print(f'O jogador {infos["nome"]} jogou {valor} partidas.')
for k, v in enumerate(infos['gols']):
    print(f'   => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {infos["total"]}')
