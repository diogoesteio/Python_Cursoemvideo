n1 = int(input('Digite um número inteiro: '))
print('A tabuada do Número {} é: '.format(n1))
for tab in range(1, 11):
    print('{} x {} = {}'.format(tab, n1, (n1 * tab)))
