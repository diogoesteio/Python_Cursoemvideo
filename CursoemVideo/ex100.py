from random import randint
from time import sleep


def sorteio(lista):
    for c in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.4)
    print('FIM!')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares de {lista} é {soma}')


numeros = list()
sorteio(numeros)
somapar(numeros)
