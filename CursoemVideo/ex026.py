f1 = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezes na frase.'.format(f1.count('a')))
print('A primeira letra A aparece na posição {}'.format(f1.find('a')+1))
print('A última letra A aparece na posição {}'.format(f1.rfind('a')+1))

