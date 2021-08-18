ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer Continuar [S/N]? '))[0].strip().upper()
    if cont == 'N':
        break
print('=-=' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-' * 25)
while True:
    pergunta = int(input('Mostrar a nota de qual aluno? (999 interrompe):  '))
    if pergunta == 999:
        break
    print(f'Notas de {ficha[pergunta][0]} são {ficha[pergunta][1]}')
    print('-' * 25)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
