# Contagem de pares

from random import randint
print('> Aí vai uma lista com todos os números pares entre 1 e 50:\n\033[31;40m> ',end='')
for o in range (1, 51, 2):
    if o %  2 == 0:
        if o == 48:
            print(f'{o} e ', end = '')
        elif o == 50:
            print(f'{o}.\033[m', end = '')
        else:
            print(f'{o}, ', end = '')
