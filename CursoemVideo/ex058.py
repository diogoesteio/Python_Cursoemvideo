from random import randint
computador = randint(0, 10)
tentativa = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu Palpite? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('MENOS...Tente mais uma vez: ')
        elif jogador < computador:
            print('MAIS...Tente mais uma vez: ')
print(f'PARABÉNS! Você acertou em {tentativa} tentativas.')
