v1 = int(input('Primeiro Valor: '))
v2 = int(input('Segundo Valor: '))
v3 = int(input('Terceiro Valor: '))
if v1 < v2 and v1 < v3:
    print('O menor número é o {}'.format(v1))
if v2 < v1 and v2 < v3:
    print('O menor número é o {}'.format(v2))
if v3 < v1 and v3 < v2:
    print('O menor número é o {}'.format(v3))
if v1 > v2 and v1 > v3:
    print('O maior número é o {}'.format(v1))
if v2 > v1 and v2 > v3:
    print('O maior número é o {}'.format(v2))
if v3 > v1 and v3 > v2:
    print('O maior número é o {}'.format(v3))
