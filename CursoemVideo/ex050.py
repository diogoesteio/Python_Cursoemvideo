soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite {}° valor: '.format(c)))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print(f'Você digitou {cont} Pares e a soma entre eles é: {soma}')
