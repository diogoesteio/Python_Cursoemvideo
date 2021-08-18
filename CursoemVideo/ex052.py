n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print(c, end=' ')
print(f'\n\33[mO número foi divisível por {tot} vezes.')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
