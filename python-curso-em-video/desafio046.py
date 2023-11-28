# Contagem regressiva

from time import sleep
print('\033[31;40m> Jogadores de fogo isento de taxações, se preparem pq ai vão fogos!\033[m')
for c in range(10, -1, - 1):
    sleep(1)
    if c == 0:
        print(f'\033[36m{c}!\033[m')
    else:
        print(f'\033[32m{c}...\033[m')
print('\033[31mKA BUM BUM BUM!\033[m')
