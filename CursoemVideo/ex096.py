def area(a, b):
    calc = a * b
    print(f'A área do Terreno {a}x{b} é de {calc}m² ')


print('Controle de terrenos: ')
print('---' * 15)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area(lar, com)
