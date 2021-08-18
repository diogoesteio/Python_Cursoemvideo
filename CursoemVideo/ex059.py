from time import sleep
valor1 = int(input('Primeiro Valor: '))
valor2 = int(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    print('=' * 40)
    opcao = int(input('>>>>>>>> Qual sua Opção? '))
    print('=' * 40)
    if opcao == 1:
        print(f'A soma de {valor1} e {valor2} é igual a {valor2 + valor1}.')
    elif opcao == 2:
        print(f'A multiplicação entre {valor1} e {valor2} é igual a {valor2 * valor1}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2} o maior valor é {valor1}.')
        elif valor2 > valor1:
            print(f'Entre {valor1} e {valor2} o maior valor é {valor2}.')
        elif valor1 == valor2:
            print(f'Os valores são iguais.')
    elif opcao == 4:
        print('Informe os Números novamente: ')
        valor1 = int(input('Primeiro Valor: '))
        valor2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('ANALISANDO...')
        sleep(2)
    else:
        print('Valor inválido, digite novamente.')
print('Fim do programa. Volte sempre.')
