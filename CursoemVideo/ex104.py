def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mERRO! Digite um valor Válido!!!\33[m')
        if ok:
            break
    return valor


n1 = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n1}')
