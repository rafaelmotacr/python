# lista ordenada sem funções

lista = []
print('-=-' * 10)
for i in range (0, 5):
    n = int(input(f'> Digite o {i}º número: \033[36m'))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('\033[m> Adicionando ao fim da lista.')
        print('-=-' * 10)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'\033[m> Adicionando à posição {pos} da lista.')
                print('-=-' * 10)
                break
            pos += 1
print(f'> Os valores digitados, em ordem, foram: {lista}.')
