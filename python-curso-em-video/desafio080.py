# lista ordenada sem funções

m = 0
lista = []
for i in range (0, 5):
    n = int(input(f'> Digite o {i}º número: '))
    if i == 0:
        lista.append(n)
        print('> Adicionado ao final da lista.')
    if i > 0:
        for p in range (0, len(lista) + 1):
            if n < lista[p]:
                lista.insert(p, n)
                print(lista)
                print(f'> Mudamos para a posição {lista.index(n)}.')
                break
            elif n > lista[p]:
                if n < max(lista):
                    if n < lista[p + 1] :
                        lista.insert(p + 1, n)
                        print(lista)
                        print(f'> Mudamos para a posição {p + 1}.')
                    elif n < lista[lista.index(max(lista))]:
                        lista.insert(p + 2, n)
                        print(lista)
                        print(f'> Mudamos para a posição {p + 2}.')
                    else:
                        lista.insert(p - 1, n)
                        print(lista)
                        print(f'> Mudamos para a posição {p - 1}.')
                else:
                    lista.append(n)
                    print(lista)
                    print(f'> Mudamos para o fim da lista.')
                break
            else:
                continue
print('-=-' * 20)
print(f'> Os números digitados, em ordem, foram: {lista}.')
'''[0,6,8,5,11]'''