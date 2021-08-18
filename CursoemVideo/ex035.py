print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Essas medidas formam um trinângulo')
else:
    print('Essas medidas não formam um triângulo.')
