# jogo da advinhação v2.0

from time import sleep
from random import randint
t = 1
c = 12
print('-=-' * 25)
print('\033[33m> O computador irá sortear um número entre 0 e 10. Tente advinhar qual...\033[m')
print('-=-' * 25)
n = randint(0, 10)
while c != n:
    c = int(input('> Digite um número entre 0 e 10 e descubra se foi igual ao do computador: \033[30m'))
    print('\033[35m> Lidando com dados...\033[m')
    sleep(0.5)
    if c == n:
        print(f'\033[m> O chute do computador foi \033[32m{n}\033[m e o seu foi \033[32m{c}.\033[m\n> \033[36mParabéns, você acertou!\033[m Foram necessárias {t} tentativas. \n')
    elif c < n:
        print('> Pra \033[31mcima\033[m, meu camarada...\n')
    else:
        print('> Pra \033[36mbaixo\033[m, meu camarada...\n')
    t += 1
