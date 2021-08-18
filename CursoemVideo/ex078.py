lista01 = []
maior = menor = 0
for pos in range(0, 5):
    lista01.append(int(input(f'Digite um valor para a posição {pos}: ')))
    if pos == 0:
        maior = menor = lista01[pos]
    else:
        if lista01[pos] > maior:
            maior = lista01[pos]
        if lista01[pos] < menor:
            menor = lista01[pos]
print('-=-' * 20)
print(f'Você digitou os valores {lista01}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista01):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista01):
    if v == menor:
        print(f'{i}...', end='')
print()
#print(f'O maior valor digitado foi {max(lista01)} na posição ')
#print(f'O menor valor digitado foi {min(lista01)} na posição ')