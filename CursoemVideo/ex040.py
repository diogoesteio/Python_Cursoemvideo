n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
media = (n1 + n2) / 2
if media < 5:
    print('Você está reprovado com média de {}'.format(media))
elif media >= 5 and media < 7:
    print('Você está em recuperação com a média de {}'.format(media))
elif media >= 7:
    print('Você está aprovado com a média de {}'.format(media))
