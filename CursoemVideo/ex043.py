from math import pow
peso = float(input('Qual seu peso atual? (Kg): '))
alt = float(input('Qual sua altura atual? (M): '))
imc = peso / pow(alt, 2)
print(f'Com este peso e altura seu IMC atual é {imc:.2f}')
if imc < 18.5:
    print('Atualmente você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Parábens, você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepso.')
elif imc >= 30 and imc < 40:
    print('Você tem obesidade, coma menos.')
else:
    print('Você tem obesidade morbida, cuidado.')
