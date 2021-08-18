print('-' * 35)
print('LOJA SUPER BARATÃO')
print('-' * 35)
totalcompra = 0
mais1000 = 0
menorpreco = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço do Produto: R$'))
    cont += 1
    totalcompra += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        menorpreco = preco
        barato = produto
    else:
        if preco < menorpreco:
            menorpreco = preco
            barato = produto
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar? [S/N]'))[0].upper().strip()
    if contin == 'N':
        break
print('FIM DO PROGRAMA')
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${totalcompra:.2f}')
print(f'Temos {mais1000} produto que custa mais de R$1000.00')
print(f'O menor preço é foi do {barato} que custa R${menorpreco}')
