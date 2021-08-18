def fatorial(n=1, show=False):
    """-> Calcula o fatorial de um número.
    Para N o número a ser calculado
    Para Show, mostra a conta executada
    return o valor fatorial do número"""
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print((fatorial(8, show=True)))
