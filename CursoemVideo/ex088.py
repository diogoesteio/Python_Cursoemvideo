from random import randint
from time import sleep
lista = []
print('-' * 40)
print('         JOGOS DA MEGA SENA:')
print('-' * 40)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=- SORTEANDO {quantidade} JOGOS -=-=-')
for c in range(0, quantidade):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    print(f'Jogo {c+1}: {lista}')
    sleep(1)
    lista.clear()
print('=-=-= BOA SORTE =-=-=')
