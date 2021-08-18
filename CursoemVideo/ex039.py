import datetime
atual = datetime.date.today().year
nascimento = int(input('Qual seu ano de nascimento? '))
idade = atual - nascimento
faltam = 18 - idade
if idade < 18:
    print('Ainda faltam {} anos para seu alistamento.'.format(faltam))
    print('Seu alistamento será em {}.'.format(atual + faltam))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade > 18:
    print('Seu alistamento foi há {} anos.'.format(atual - (atual + faltam)))
    print('Ele ocorreu no ano de {}'.format(atual + faltam))
