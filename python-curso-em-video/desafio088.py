# palpites para a mega sena

from random import randint as oli
from time import sleep as amimi
palpite = []
holder = []
print('-=-' * 17 + '=' )
print(f'{"< Jogando na mega >":^47}')
print('-=-' * 17 + '=')
l = int(input('> Digite quantos jogos você deseja gerar: '))
print(f'\n=-=-=-=-=-=-=- < Sorteando {l} jogos > -=-=-=-=-=-=-=')
print('-' * 52)
for i in range(0, l):
    c = 0
    while c < 6: 
        num = oli(1, 60)
        if num not in holder:
            holder.append(f'{num:2}')
            c += 1
    holder.sort()
    palpite.append(holder[:])
    holder.clear()
for i,j in enumerate(palpite):
    print(f'| \033[36;40m> Jogo {i + 1:>2}:\033[m {j:}. |')
    amimi(0.5)
print('-' * 52,'\n> Boa sorte no jogo! Não se esqueça: \033[31mJogos de azar são furada!\033[m\n')
