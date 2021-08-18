km = int(input('Qual sua velocidade atual? '))
if km > 80:
    print('MULTADO! Você excedeu o limite de velocidade de 80km/h.')
    print('Você pagara uma multa de R${}'.format((km - 80)*7))
print('Tenha um bom dia. Dirija com segurança!')
