# Extraindo dados de uma lista

lista = []
e = 0
while True:
    if e == 0:
        n = int(input('> Digite um número: '))
        lista.append(n)
        e += 1
    elif e == 1:
        r = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        print('-=-' * 10)
        if r == 's':
            e = 0
            continue
        elif r == 'n':
            break
        else:
            continue
lista.sort(reverse = True)    
print(f'> Você digitou {len(lista)} números.')
print(f'> Os valores, de forma decrescente, são: {lista}')
print(f'> O valor 5 foi digitado, ele se encontra na posição {lista.index(5)}!\n' if 5 in lista else '> O valor 5 não foi digitado!\n')
