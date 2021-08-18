def analise(* num):
    cont = maior = 0
    print('=-' * 16)
    print('Analisando os valores passados... ')
    for c in num:
        print(f'{c} ', end='')
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


analise(9, -6, -5, 8, 23, 5)
analise(1, 7, 65)
analise(7, -6)
analise(4)
analise()
