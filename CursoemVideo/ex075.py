n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}  ', end='')
