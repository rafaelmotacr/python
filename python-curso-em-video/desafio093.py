# Cadastro de um jogador de futebol

from time import sleep 
gol = list ()
jogador = dict ()
print('-=-' * 18)
jogador['nome'] = str(input('> Digite o nome do jogador: '))
l = int(input(f'> Quantas partidas {jogador["nome"]} jogou?: '))
for i in range(0, l):
    gol.append(int(input(f'> Quantos gols na partida {i + 1}?: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-=-' * 18)
print(jogador)
print('-=-' * 18)
for i, j in jogador.items():
    print(f'> O campo {i} tem o valor {j}.')
print('-=-' * 18)
print(f'> O jogador {jogador["nome"]} jogou {l} partidas. Nas quais: ')
for i in range(0, len(gol)):
    sleep(0.5)
    print(f'    ➔  Na partida {i + 1} foram feitos {gol[i]} gols.')
print(f'> Foi um total de {jogador["total"]} gols.\n')
