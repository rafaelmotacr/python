# Ficha do jogador 

def ficha(nome, gols):
    if nome.strip() == '':
        nome = '< desconhecido >'
    if gols.strip() == '' or not(gols.isnumeric()):
        gols = 0
    frase = f'> O jogador {nome} fez {gols} gol(s) no campeonato.'
    return frase 


saída = ficha(input('> Nome do jogador: '),
                input('> Número de gols: '))
print(saída)
