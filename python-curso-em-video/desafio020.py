# Sorteando um item na lista 2 

from random import shuffle
n1 = str(input('\033[m> Digite o nome do 1º aluno: \033[31m'))
n2 = str(input('\033[m> Digite o nome do 2º aluno: \033[32m'))
n3 = str(input('\033[m> Digite o nome do 3º aluno: \033[33m'))
n4 = str(input('\033[m> Digite o nome do 4º aluno: \033[34m')) 
sort = [n1, n2, n3, n4]
shuffle(sort)
print(f'\n\033[m> A ordem de apresentação será: \033[32m{sort}\033[m.')
