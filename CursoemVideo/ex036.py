valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual seu salário mensal? R$'))
finan = int(input('Em quantos anos pretende financiar? '))
prest = valor / (finan * 12)
max = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(valor, finan), end='')
print('o valor da prestação será de R${:.2f}'.format(prest))
if prest >= max:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')

