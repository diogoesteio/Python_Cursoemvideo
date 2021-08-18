tupla = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre zero e 20: '))
    if 0 <= numero <= 20:
        break
    else:
        print('Tente Novamente. ', end='')
print(f'Você digitou o número {tupla[numero]}')
