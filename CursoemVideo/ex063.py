print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)
termos = int(input('Quantos termos você quer mostrar? '))
print('~' * 20)
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= termos:
    t3 = t2 + t1
    print(f'{t3} -> ', end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' -> FIM', end='')
