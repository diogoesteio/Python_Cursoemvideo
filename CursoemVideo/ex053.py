frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos) - 1, -1, -1):
    inverso += juntos[letra]
print(f'O inverso de {juntos} fica escrito {inverso}.')
if juntos == inverso:
    print('Está frase é um Palindromo.')
else:
    print('Está frase não é um Palindromo')
