from datetime import date
ficha = dict()
ficha['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
ficha['idade'] = date.today().year - nascimento
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['Salário'] = float(input('Salário R$: '))
    ficha['Aposentadoria'] = ficha['contratação'] + 35 - nascimento
print('=-=' * 30)
for k, i in ficha.items():
    print(f'{k} tem o valor {i}')
