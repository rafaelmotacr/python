# Jogo de dados em Python

from random import randint as mila 
from time import sleep as amimi
jogadas = dict()
lista = list()
nome = list()
jogadas ={'jogador0': mila(1, 6),
           'jogador1': mila(1, 6),
            'jogador2': mila(1, 6),
            'Jogador3': mila(1, 6)}
print('> Os valores sortados foram: ')
for j, n in jogadas.items():
    amimi(0.5)
    print(f'{j:>10}: {n}')
    lista.append(n)
lista.sort(reverse = True)
for i in range(0, len(lista)):
    for j, n in jogadas.items():
        if lista[i] == n and j not in nome:
            nome.append(j)
print('\n> Ranking dos jogadores:')
for i in range (0, len(lista)):
    amimi(0.5)
    if i == len(lista) - 1:
        print(f'{i + 1:>3}º lugar: {nome[i]} com {lista[i]}.\n')
    else:
        print(f'{i + 1:>3}º lugar: {nome[i]} com {lista[i]}.')
