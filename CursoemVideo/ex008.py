m1 = float(input('Qual a medida em metros? '))
mxkm = m1 / 1000
mxhm = m1 / 100
mxdam = m1 / 10
mxdm = m1 *10
mxc = m1 * 100
mxm = m1 * 1000
print('A medida de {}m corresponde há: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m1, mxkm, mxhm, mxdam, mxdm, mxc, mxm))
