lista = list()
cadastro = dict()
mulheres = list()
pessoas = cmedia = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Nome: '))
    pessoas += 1
    cadastro['sexo'] = ' '
    while cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('Sexo: [M/F]: '))[0].strip().upper()
        if cadastro['sexo'] not in 'MF':
            print('ERRO! Pro favor, digite apenas M ou F.')
        if cadastro['sexo'] in 'F':
            mulheres.append(cadastro['nome'][:])
    cadastro['idade'] = int(input('Idade: '))
    lista.append(cadastro.copy())
    cmedia += cadastro['idade']
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
        if cont not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if cont == 'N':
        break
media = cmedia / pessoas
print(lista)
print(f'A) Ao todo temos {pessoas} pessoas cadastradas.')
print(f'B) A média de idade é de {media} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista das pessoas que estçao acima da média: ', end='')
for p in lista:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
        print()
