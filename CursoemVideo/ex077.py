palavras = ('apreder', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for pal in palavras:
    print(f'\nNa palavra {pal.upper()} temos: ', end='')
    for letra in pal:
        if letra in 'aeiou':
            print(letra, end=' ')
