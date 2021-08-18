maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if c > peso:
            maior = peso
        if c < peso:
            menor = peso
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')
