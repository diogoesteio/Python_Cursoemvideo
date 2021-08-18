aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('=-=' * 30)
print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["média"]}')
if aluno["média"] >= 7:
    print('- situação é igual a aprovado')
if aluno["média"] >= 5 and aluno["média"] < 7:
    print('- situação é Recuperação')
if aluno["média"] < 5:
    print('- situação é reprovado')
