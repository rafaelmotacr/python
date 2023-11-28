# função de contador

from time import sleep 
def contador(inicio, fim, passo):
    print('-=-' * 15)
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo = abs(passo)
    print(f'> Contagem de {inicio} até {fim} de {passo} em {passo}: ')
    if inicio > fim:
        for i in range (inicio, fim - 1, - passo):
            sleep(0.5)
            print(f' {i} ', end = '', flush = True)
    elif fim > inicio:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(f' {i} ', end = '', flush = True)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0 , - 1)
while True:
    print('-=-' * 15)
    contador(int(input('> Digite o inicio: ')),
            int(input('> Digite o fim: ')),
            int(input('> Digite o passo: '))
            )
