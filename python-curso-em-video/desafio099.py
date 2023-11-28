# Função que descobre o maior

def maior(* x):
    top = 0
    print('-=-' * 15)
    print('> Analisando os valores passados...')
    for v in range(0, len(x)):
        print(f' {x[v]} ', end = '')
        if x[v] > top or v == 0:
            top = x[v]
    print(f'Foram digitados {len(x)} valores ao todo.')
    print(f'> O maior valor digitado foi {top}.')


maior(5, 3, 7, 10)
maior(4, 7, 63, 1)
maior(0)
maior(- 10, - 7, - 12, - 3)
print('-=-' * 15)
