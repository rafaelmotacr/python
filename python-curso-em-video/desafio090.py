# Dicionários em Python

aluno = dict()
print('-=-' * 15)
aluno['Nome'] = str(input('> Nome do aluno: ')).strip().title()
aluno['Média'] = float(input(f'> Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[36mAprovado\033[m'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação']= '\033[31mReprovado\033[m'
else:
    aluno['Situação'] = '\033[33mRecuperação\033[m'
print('-=-' * 15)
print(f'> O nome do aluno é {aluno["Nome"]}.')
print(f'> A média de {aluno["Nome"]} é de {aluno["Média"]}')
print(f'> A situação final do aluno é {aluno["Situação"]}.')
print('-=-' * 15,'\n')
