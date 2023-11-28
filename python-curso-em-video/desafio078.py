# Maior e menor valores numa lista

lista = []
print(f'\033[31;40m{"Viadagem":-^38}\033[m')
for i in range (0, 5):
    lista.append(int(input(f'\033[30;40m> Digite um número para a posição {i}: \033[31m')))
print(f'\033[31;40m{"Viadagem":-^38}\033[m')
print(f'Você digitou os números: {lista}')
ma = max(lista)
me = min(lista)
print(f'> O maior número digitado foi {ma}, nas posições: ', end = '')
for i in range (0, len(lista)):
    if lista[i] == ma:
        print(f'{i}... ', end = '')
print(f'\n> O menor valor digitado foi {me}, nas posições: ', end = '')
for i in range (0, len(lista)):
    if lista[i] == me:
        print(f'{i}... ', end = '')
