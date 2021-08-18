resp = 'S'
soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] '))[0].upper()
    soma += num
    quant += 1
    if soma == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print(f'Você digitou {quant} números e a média deles foi {media:.2f}')
print(f'O maior valor foi de {maior} e o menor de {menor}')
