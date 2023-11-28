# Maior e menor valores numa tupla

from random import randint
tup = (randint (1, 11), randint (1, 11), randint (1, 11), randint (1, 11))
print('> Valors sorteados: ', end = '')
for i in range(0, 4):
    if i == 3:
        print(f'{tup[i]}.', end = '')
    elif i == 2:
        print(f'{tup[i]} e ', end = '')
    else:
        print(f'{tup[i]}, ', end = '')

print(f'\n> O maior valor sorteado foi {max(tup)} e o menor valor sorteado foi {min(tup)}.')
