import time
import random
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
a1 = int(input('Qual é sua jogada? '))
time.sleep(0.5)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
print('-=-' * 20)
a2 = random.randint(0, 2)
if a1 == 0 and a2 == 1 or a2 == 0 and a1 == 1:
    if a1 == 0:
        print('Jogador Jogou PEDRA')
        print('Computador jogou PAPEL')
        print('-=-' * 20)
        print('COMPUTADOR VENCEU')
    else:
        print('Jogador Jogou PAPEL')
        print('Computador jogou PEDRA')
        print('-=-' * 20)
        print('JOGADOR VENCEU')
elif a1 == 0 and a2 == 2 or a2 == 0 and a1 == 2:
    if a1 == 0:
        print('Jogador Jogou PEDRA')
        print('Computador jogou TESOURA')
        print('-=-' * 20)
        print('JOGADOR VENCEU')
    else:
        print('Jogador Jogou TESOURA')
        print('Computador jogou PEDRA')
        print('-=-' * 20)
        print('COMPUTADOR VENCEU')
elif a1 == 1 and a2 == 2 or a2 == 1 and a1 == 2:
    if a1 == 1:
        print('Jogador Jogou PAPEL')
        print('Computador jogou TESOURA')
        print('-=-' * 20)
        print('COMPUTADOR VENCEU')
    else:
        print('Jogador Jogou TESOURA')
        print('Computador jogou PAPEL')
        print('-=-' * 20)
        print('JOGADOR VENCEU')
else:
    if a1 == 0:
        print('Jogador Jogou PEDRA')
        print('Computador jogou PEDRA')
        print('-=-' * 20)
        print('EMPATE!!!')
    if a1 == 1:
        print('Jogador Jogou PAPEL')
        print('Computador jogou PAPEL')
        print('-=-' * 20)
        print('EMPATE!!!')
    if a1 == 2:
        print('Jogador Jogou TESOURA')
        print('Computador jogou TESOURA')
        print('-=-' * 20)
        print('EMPATE!!!')
