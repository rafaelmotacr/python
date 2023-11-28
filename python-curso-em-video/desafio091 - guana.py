# Jogo de dados em Python

from random import randint as mila 
from time import sleep as amimi
from operator import itemgetter as maio
jogadas = dict()
ranking = list()
jogadas ={'jogador0': mila(1, 6),
           'jogador1': mila(1, 6),
            'jogador2': mila(1, 6),
            'Jogador3': mila(1, 6)}
ranking = sorted(jogadas.items(), key = maio(1), reverse = True)
print('> Os valores sortados foram: ')
for j, n in jogadas.items():
    amimi(0.5)
    print(f'{j:>10}: {n}')
print('\n> Ranking dos jogadores:')
for j, n in enumerate(ranking):
    amimi(0.5)
    print(f'  {j + 1}º lugar: {n[0]} com {n[1]}.')
print()
    