dia = int(input('O veículo foi alugado por quantos dias? '))
km = float(input('Qual a quilometragem que o veículo andou em km? '))
vdia = dia * 60
vkm = km * 0.15
vtotal = vdia + vkm
print('O preço total a ser pago por ter usado o carro {} dias e rodado {}km é de R${}'.format(dia, km, vtotal))
