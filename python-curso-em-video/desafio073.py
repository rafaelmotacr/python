# Tuplas com times de futebol

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
    'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
    'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
    'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print('-' * 50)
print(f'|\033[36;40m{"Brasileirão do Piton":^48}\033[0m|')
print('-' * 50)
print('\033[30;40m> Os \033[32mprimeiros\033[30m 5 colocados foram:\033[m')
print('-' * 50)
for pos in range (0, 5):
    print (f'| {pos + 1:0>2} - {times[pos]:.<40}.', end =' |\n')
print('-' * 50)
print('\033[30;40m> Os \033[31múltimos\033[30m 4 colocados foram:\033[m')
print('-' * 50)
for pos in range (- 4, 0, + 1):
    print (f'| {times.index(times[pos]) + 1} - {times[pos]:.<40}.', end = ' |\n')
print('-' * 50)
print(f'\033[30;40m> Os times, em \033[33mordem alfabética\033[30m, são:\033[m')
print('-' * 50)
tupla2 = sorted(times)
for pos in range (0, len(tupla2)):
    print(f'| {pos + 1:0>2} - {tupla2[pos]:.<40}. |')
print('-' * 50)
print(f'\033[30;40m> O time \033[35mAvaí\033[30;40m está na {times.index("Avaí") + 1}ª colocação.\033[m')
print('-' * 50)
