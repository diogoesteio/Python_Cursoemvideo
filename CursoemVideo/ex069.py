homem = maioridade = mulher20 = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: '))[0].strip().upper()
    print('-' * 40)
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer cadastrar outra pessoa? [S/N]: '))[0].upper().strip()
    if resposta == 'N':
        break
print('-' * 35)
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
