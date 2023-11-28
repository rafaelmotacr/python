# Jokenpô virtual

import emoji
from playsound import playsound
from random import randint
from time import sleep
print('\n\033[30;40m> Bem vindo ao jokenpô virtual! Iremos explicar as regras do jogo logo abaixo.\033[m\n')
print(emoji.emojize(f"\033[33;43m{' 1 - Pedra:rock:':^23}\033[m | \033[31;41m{'2 - Papel:newspaper:':^27}\033[m | \033[32;42m{'3 - Tesoura:scissors:':^27}\033[m"))
print(f"{'_' * 18} | {'_' * 18} | {'_' * 18}")
print('{}{}{:<10}{}{}{:^10}{}{:<10}{}{}{:>10}{}{:<7}{}'.format('Ganha de ', '\033[32m','Tesoura','\033[m','|','Ganha de','\033[33m','Pedra','\033[m', '|', 'Ganha de ','\033[31m','Papel','\033[m'))
print('{}{}{:<8}{}{:2}{:^10}{}{:<8}{}{:2}{:>10}{}{:<7}{}'.format('Perde para ', '\033[31m','Papel','\033[m','|','Perde para ','\033[32m','Tesoura','\033[m', '|', 'Perde para ','\033[33m','Pedra','\033[m'))
print('{}{}{:<8}{}{:2}{:^10}{}{:<8}{}{:2}{:>10}{}{:<7}{}'.format('Empata com ', '\033[33m','Pedra','\033[m','|','Empata com ','\033[31m','Papel','\033[m', '|', 'Empata com ','\033[32m','Tesoura','\033[m'))
r = ''
e = v = 0
while True:
    if e == 0:
        j = int(input(f'\n\033[30;40m> Digite 1 para escolher \033[33;43mPedra\033[30;40m, 2 para \033[31;41mPapel\033[30;40m ou 3 para \033[32;42mTesoura\033[m: \033[35m')) -  1
        l = ('\033[33;43mPedra\033[30;40m', '\033[31;41mPapel\033[30;40m', '\033[32;42mTesoura\033[30;40m')
        if j >= 0 and j <= 2:
            p = randint(0, 2)
            sleep(0.5)
            print('\n\033[30;40mPedra...')
            sleep(0.5)
            print('Papel...')
            sleep(0.5)
            print('\033[32;40mE Tesoura!\033[m')
            if j == 0 and p == 2 or j == 1 and p == 0 or j == 2 and p == 1:
                print(f'\n\033[30;40m> Você escolheu {l[j]} e a máquina escolheu {l[p]}. \033[36;40mVitória do jogador!\033[m\n')
                playsound(r'desafio045vitoria.mp3')
            elif j == p:
                print(f'\n\033[30;40m> Você escolheu {l[j]} e a máquina escolheu {l[p]}. \033[35;40mEmpate!\033[m\n')
                playsound(r'desafio045empate.mp3')
            else: 
                print(f'\n\033[30;40m> Você escolheu {l[j]} e a máquina escolheu {l[p]}. \033[31;40mVitória da máquina!\033[m\n')
                playsound(r'desafio045derrota.mp3')
        else:
            print('\n\033[30;40m> O número digitado é \033[4;31;40minválido!\033[0;30;40m Tente novamente!\033[m\n')
        e += 1
    if e == 1:
        r = str(input('\033[30;40m> Deseja jogar novamente? [S/N]\033[m: \033[35m')).upper().strip()[0]
        if r == 'S':
            e = 0
            continue
        elif r == 'N':
            break
        else:
            continue
