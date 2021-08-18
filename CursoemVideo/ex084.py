cadastro = maior = menor = 0
lista = []
while True:
    nome = str(input('Nome: '))
    cadastro += 1
    peso = float(input('Peso: '))
    lista.append([nome, peso])
    if cadastro == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    cont = str(input('Quer continuar? [S/N]? '))
    if cont in 'Nn':
        break
print('-=-' * 20)
print(f'Ao todo você cadastrou {cadastro} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]} ]', end='')
print()
print(f'O menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]} ]', end='')
