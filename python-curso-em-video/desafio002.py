# Respondendo ao usuário

dia = int(input('> Dia: '))
mes = int(input('> Mês: '))
ano = int(input('> Ano: '))
if mes > 12 or dia > 31 or ano < 1900:
    print('> Algum dos valores digitados foi inválido! Tente novamente!')
else:
    mês = ['janeiro', 'fevereio', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    print ('você nasceu no dia {}{}{} de {}{}{} de {}{}{}.'.format('\033[31m',dia,'\033[m','\033[31m',mês[mes-1], '\033[m','\033[31m', ano,'\033[m'))
