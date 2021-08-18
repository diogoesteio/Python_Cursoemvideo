dist = int(input('Qual a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(dist))
if dist > 200:
    print(f'O preço de sua viagem será de R${dist * 0.45:.2f}')
else:
    print(f'O preço de sua viagem será de R${dist * 0.5:.2f}')
