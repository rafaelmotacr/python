# Dividindo valores em várias listas
e = 0
par = []
impar = []
lista = []
while True:
    if e == 0:
        n = int(input('> Digite um número: '))
        lista.append(n)
        e += 1
    if e == 1:
        r = str(input('> Deseja continuar? [S/N]: ')).strip().lower()[0]
        print('-=-' * 10)
        if r == 's':
            e = 0
            continue
        elif r == 'n':
            break
        else:
            continue
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'> Os números digitados foram: {lista}.')
print(f'> Deste conjunto, são \033[36mpares\033[m os números: {par}.')
print(f'> Deste conjunto, são \033[31mimpares\033[m os números: {impar}.\n')
print('-=-' * 10)
