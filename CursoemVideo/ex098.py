from time import sleep


def contagem(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont}', end='')
            sleep(0.25)
            cont += p
        print(' FIM!')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}', end='')
            sleep(0.25)
            cont -= p
        print(' FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem.')
n1 = int(input('Início = '))
n2 = int(input('Fim = '))
n3 = int(input('Passo = '))
contagem(n1, n2, n3)
