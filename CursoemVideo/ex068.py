from random import randint
print('=-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 20)
vitoria = 0
while True:
    valor = int(input('Diga um valor: '))
    comput = randint(1, 10)
    soma = valor + comput
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]: '))[0].strip().upper()
        print('-' * 30)
    if soma % 2 == 0:
        print(f'Você jogou {valor} e o Computador {comput}. Total de {soma} deu PAR.')
    elif soma % 2 == 1:
        print(f'Você jogou {valor} e o Computador {comput}. Total de {soma} deu IMPAR.')
    if soma % 2 == 0 and escolha in 'P':
        print('Você VENCEU.')
        vitoria += 1
        print('-' * 30)
    elif soma % 2 == 1 and escolha in 'I':
        print('Você VENCEU')
        vitoria += 1
        print('-' * 30)
    else:
        print('Você PERDEU')
        break
print('=-=' * 20)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
