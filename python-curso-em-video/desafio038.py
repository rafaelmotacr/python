# Comparando números

n1 = int(input('\033[m> Digite o primeiro número: \033[35m'))
n2 = int(input('\033[m> Digite o segundo número: \033[30m'))
if n1 > n2:
    print(f'\033[m> O número \033[4;35m{n1}\033[m é o \033[4;36mmaior\033[m!')
elif n2 > n1:
    print(f'\033[m> O número \033[4;30m{n2}\033[m é o \033[4;36mmaior\033[m!')
else:
    print(f'\033[m> Os números \033[4;35m{n1}\033[m e \033[4;30m{n2}\033[m são \033[4;32miguais\033[m!')
