# Ficha do jogador 

def ficha(name = '< desconhecido >' , gol = 0):
    print(f'> O jogador {name} fez {gol} gol(s) no campeonato.') 


nome = input('> Nome do jogador: ')
gols = input('> Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)
