from random import randint
import time
pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente advinhar')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei:  '))
print('-=-' * 20)
print('PROCESSANDO...')
time.sleep(2)
if pc == jogador:
    print('PARABÉNS você Ganhou !!!!!')
else:
    print(f'Que pena, eu pensei no número {pc} e não no {jogador}.')
