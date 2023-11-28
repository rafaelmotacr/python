# Mais sobre matrizes em Python

print('___' * 20, end ='\n\n')
matriz = [[], [], []]
m2 = s3 = sp = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha].append(int(input(f'> Digite um valor para a posição [{linha}, {coluna}]: ')))
print('___' * 20, end = '\n\n')
for linha in range (0, 3):
    for coluna in range (0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end = '')
        if matriz[coluna][linha] % 2 == 0:
            sp += matriz[coluna][linha]
        if coluna == 2:
            s3 += matriz[linha][coluna] 
    print()
print('___' * 20)
print(f'> A soma dos elementos pares da matriz é: {sp}.')
print(f'> A soma dos elementos da terceira coluna é {s3}.')
print(f'> o maior elemento da segunda linha é {max(matriz[1])}.\n')
