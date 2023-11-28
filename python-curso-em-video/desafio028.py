# jogo da advinhação v.1.0

from time import sleep
from random import randint
n = randint(0, 5)
print('-=-' * 24)
print('> O computador irá sortear um número entre 0 e 5. Tente advinhar qual...')
print('-=-' * 24)
c = int(input('> Digite um número entre 0 e 5 e descubra se foi igual ao do computador: \033[30m'))
if c <= 5:
    print('\033[35m> Lidando com dados...')
    sleep(3)
    if c == n:
        print(f'\033[m> O chute do computador foi \033[32m{n}\033[m e o seu foi \033[32m{c}.\n> \033[36mParabéns, você acertou!\033[m\n')
    else:
        print(f'\033[m> O chute do computador foi \033[32m{n}\033[m e o seu foi \033[31m{c}.\n> \033[31mÉ uma pena, você errou!\033[m\n')
else:
    print('> O número digitado foge do limite proposto! Tente novamente.')