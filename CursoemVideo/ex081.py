lista = []
parte = ''
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if 5 in lista:
        parte = 'faz'
    else:
        parte = 'não faz'
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: '))[0].upper().strip()
    if cont in 'N':
        break
print('-=-' * 20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
print(f'O valor 5 {parte} parte da lista.')
