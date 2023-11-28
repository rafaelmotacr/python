# Análise de uma tupla 

lista = ''
tup = (int(input('> Digite o 1º valor: ')),
    int(input('> Digite o 2º valor: ')),
    int(input('> Digite o 3º valor: ')),
    int(input('> Digite o 4º valor: ')),
)
print (f'> Você digitou os números {tup}.')
print(f'> O número 9 apareceu {tup.count(9)} vezes na tupla.')
print(f'> O número 3 apareceu pela primeira vez na posição {tup.index(3) + 1} dentro da tupla.' if 3 in tup else '> O número três não aparece nenhuma vez na tupla.') 
print('> Os números pares são: ', end = '')
for i in range (0, 4):
    if tup[i] % 2 == 0:
        lista += f' {tup[i]}'
lista = lista.split()
l = len(lista)
for i in range (0, l):
    if i == l - 2:
        print(f'{lista[i]} e ', end = '')
    elif i == l - 1:
        print(f'{lista[i]}', end = '.')
    else:
        print(f'{lista[i]}, ', end = '')
