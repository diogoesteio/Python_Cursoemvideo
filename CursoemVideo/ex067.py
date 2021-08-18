while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 25)
    if valor < 0:
        break
    else:
        for c in range(1, 11):
            mult = valor * c
            print(f'{valor} x {c} = {mult}')
    print('-' * 25)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre. ')
