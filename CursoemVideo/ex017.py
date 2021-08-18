from math import sqrt, pow
co = float(input('Qual a medida do cateto oposto do triângulo retangulo: '))
ca = float(input('Qual a medida do cateto adjacente do triângulo retangulo: '))
hip = sqrt(pow(co, 2) + pow(ca, 2))
print('A medida da hipotenusa do triangulo de cateto op. {} e cateto adj. {} é {:.2f}!'.format(co, ca, hip))
'''Pode ser usado a função hypot para cáluclo de hipotenusa'''
