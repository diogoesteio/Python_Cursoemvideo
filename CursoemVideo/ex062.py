print('GERADOR DE PA')
print('-=-' * 20)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar: '))
print('FIM')
print('Progressão finalizada com um total de {} termos'.format(total))
