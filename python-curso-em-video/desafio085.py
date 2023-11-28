# Lista com pares e impares

lista = [[], []]
print('-=-' * 17)
for i in range (0, 7):
    n = int(input(f'> Digite o {i + 1}º número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print('-=-' * 17)
print(f'> Os valores \033[34mpares\033[m digitados foram: {lista[0]}.')
print(f'> Os valores \033[31mimpares\033[m digitados foram: {lista[1]}.')
