lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adiconado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitadoes em ordem foram {lista}')
