from math import tan, cos, sin, radians
ang = float(input('Qual a medida do ângulo: '))
angrad = radians(ang)
tan = tan(angrad)
cos = cos(angrad)
sin = sin(angrad)
print(f'O cosseno do ângulo {ang}° é {cos:.2f}\nO seno do ângulo {ang}° é {sin:.2f}\nA Tangente do ângulo {ang}° é {tan:.2f}')
