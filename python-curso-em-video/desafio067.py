# Tabuada v3.0

while True:
    n = int(input('\033[0;0;40m> Digite um número e faremos a tabuada dele para ti:\033[32;30m '))
    print('\033[m-' * 54)
    if n < 0:
        break
    for i in range (1, 11):
        print(f'> \033[31m{n}\033[m x \033[34m{i:2}\033[m \033[32m=\033[m \033[35m{n * i}\033[m.')
    print('-' * 54)
print('> Programa de tabuada encerrado com sucesso! Volte sempre.\033[m\n')
