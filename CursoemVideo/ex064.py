num = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = num
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += num
nfinal = soma - 999
print(f'Você digitou {cont} números e a soma deles é {nfinal}.')
