from datetime import date
ano = date.today().year
novo = 0
velho = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = ano - nascimento
    if idade >= 18:
        velho += 1
    else:
        novo += 1
print(f'Ao todo tivemos {velho} pessoas maiores de idade\nE também tivemos {novo} pessoas menores de idade.')
