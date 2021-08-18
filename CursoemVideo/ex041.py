from datetime import date
ano = date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = ano - nascimento
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFALTIL.')
elif idade <= 19:
    print('Sua categoria é a JUNIOR.')
elif idade <= 25:
    print('Sua categoria é a SÊNIOR.')
elif idade > 25:
    print('Sua categoria é a MASTER.')
