# Sorteando um item na lista

from random import randrange, choice
n1 = str(input('\033[m> Digite o nome do 1º aluno: \033[31m'))
n2 = str(input('\033[m> Digite o nome do 2º aluno: \033[32m'))
n3 = str(input('\033[m> Digite o nome do 3º aluno: \033[33m'))
n4 = str(input('\033[m> Digite o nome do 4º aluno: \033[34m')) 
sort = [n1, n2, n3, n4]
if sort[randrange(len(sort))] == sort[0]:
    print(f'\033[m> O azarado foi: \033[31m{sort[0]}\033[m.')
elif sort[randrange(len(sort))] == sort[1]:
    print(f'\033[m> O azarado foi: \033[32m{sort[1]}\033[m.')
elif sort[randrange(len(sort))] == sort[2]:
    print(f'\033[m> O azarado foi: \033[33m{sort[2]}\033[m.')
else:
    print(f'\033[m> O azarado foi: \033[34m{sort[3]}\033[m.') 
'''O método choice pode ser usado em alternativa ao randrange
Exemplo de uso de choise:    a = choice(lista)'''
