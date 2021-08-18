print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇO'))
print('-' * 40)
materiais = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 15,
             'Estojo', 25,
             'Transferidor', 4.2,
             'Compasso', 9.99,
             'Mochila', 120.32,
             'Canetas', 22.3,
             'Livros', 34.9)
for pos in range(0, len(materiais)):
    if pos % 2 == 0:
        print(f'{materiais[pos]:.<30}', end='')
    else:
        print(f'R${materiais[pos]:>7.2f}')
print('-' * 40)
