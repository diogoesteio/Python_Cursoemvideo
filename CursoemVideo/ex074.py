from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
menor = maior = num[0]
for m in num:
    print(m, end=' ')
    if m < menor:
        menor = m
    if m > maior:
        maior = m
print(f'\nO maior valor sorteado foi o {maior}')
print(f'O menor valor sorteado foi o {menor}')
print(max(num))
print(min(num))
