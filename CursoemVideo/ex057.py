sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} cadastrado com sucesso!')
