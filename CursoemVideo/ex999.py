from random import choice
q1 = int(input('Quantas pessoas vão comer? '))
lista = []
for c in range(0, q1):
    lista.append(str(input(f'Digite o nome da {c + 1}° pessoa:')))
pagador1 = choice(lista)
pagador2 = choice(lista)
while True:
    if pagador1 != pagador2:
        break
    else:
        pagador2 = choice(lista)
print(f'As pessoas que dividiram a conta são: {pagador1} e {pagador2}')
