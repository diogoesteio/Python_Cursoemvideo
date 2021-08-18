listanum = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in listanum:
        listanum.append(n)
        print('Número adicionado com sucesso...')
    else:
        print('Valor duplicado. Não adicionado')
    con = ' '
    while con not in 'SN':
        con = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if con in 'N':
        break
print(f'Você digitou os valores {sorted(listanum)}')
