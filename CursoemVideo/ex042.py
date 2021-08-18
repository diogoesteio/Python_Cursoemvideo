print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Essas medidas formam um trinângulo')
    if r1 == r2 and r2 == r3:
        print('E é um triângulo Equilatero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('E é um triângulo Isósceles.')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('E é um triângulo Escaleno')
else:
    print('Essas medidas não formam um triângulo.')
