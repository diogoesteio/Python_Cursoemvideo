print('{:=^40}'.format(' DB COMERCIO '))
preco = float(input('Preço das Compras? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/chequ
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pag = int(input('Qual a opção? '))
if pag == 1:
    v1 = preco * 0.9
    print('Pelas compras com valor de R${} voce pagará R${}.'.format(preco, v1))
elif pag == 2:
    v1 = preco * 0.95
    print('Pelas compras com valor de R${} voce pagará R${}.'.format(preco, v1))
elif pag == 3:
    v1 = preco / 2
    print('Pelas compras com valor de R${} voce pagará duas prestações no valor de R${} cada.'.format(preco, v1))
elif pag == 4:
    parc = int(input('Em quantas parcelas deseja fazer? '))
    v1 = preco * 1.2
    prest = v1 / parc
    print('Pelas compras com valor de R${} você pagara {} parcelas no valor de R${} cada.'.format(preco, parc, prest))
else:
    print('Opção Inválida')
