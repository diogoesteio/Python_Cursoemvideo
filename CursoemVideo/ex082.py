lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: '))[0].upper().strip()
    if cont == 'N':
        break
print('-=-' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpar é {impar}')
