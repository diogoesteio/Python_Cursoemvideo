mulheres = 0
maior = 0
media = 0
nomemaisvelho = ''
for c in range(1, 5):
    print('{:-^20}'.format(' {}° PESSOA '.format(c)))
    nome = str(input('NOME: ')).strip().capitalize()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    media += idade
    if c == 1 and sexo == 'M':
        maior = idade
        nomemaisvelho = nome
    if sexo == 'M' and idade > maior:
        maior = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print(f'A média de Idade do grupo é {media / 4:.2f} anos')
print(f'O homem mais velho tem idade de {maior} anos e se chama {nomemaisvelho}.')
print(f'O grupo tem {mulheres} mulheres com menos de 20 anos.')
