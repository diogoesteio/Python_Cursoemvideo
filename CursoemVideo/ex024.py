cidade = str(input('Em que cidade você nasceu? ')).strip()
c1 = cidade.lower().split()
print('santo' in c1[0])
#Outra solução
#print(cidade[:5].lower() == 'santo')