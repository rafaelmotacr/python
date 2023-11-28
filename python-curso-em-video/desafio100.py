# Funções para sortear e somar

from random import randint
from time import sleep

numeros = list()
def sorteia(x):
    x.clear()
    print('-=-' * 15)
    print('> Sorteando cinco números da lista:', end = '')
    for i in range (0, 5):
        x.append(randint(0, 100))
        sleep(0.5)
        print(f' {x[i]} ', end = '', flush = True)
    print('PRONTO!')

    
def SomaPar(y): 
    soma = 0
    for j in y:
        if j % 2 == 0:
            soma += j
    print(f'> Somando os valores pares de: {y}, temos {soma}.')


sorteia(numeros)
SomaPar(numeros)
sorteia(numeros)
SomaPar(numeros)
