salario = float(input('Qual o valor do seu salário? '))
if salario > 1250:
    s1 = salario * 1.1
else:
    s1 = salario * 1.15
print('O seu salário de {}, passará a ser de {:.2f}. '.format(salario, s1))
