# Maior e menor valores

n1 = int(input('\033[m> Número 1: \033[33m'))
n2 = int(input('\033[m> Número 2: \033[30m'))
n3 = int(input('\033[m> Número 3: \033[31m'))

if max([n1, n2, n3], key = int) == n1:
    print(f'\033[m> O \033[36mmaior\033[m valor digitado foi \033[33m{n1}\033[m.')
elif max([n1, n2, n3], key = int) == n2:
    print(f'\033[m> O \033[36mmaior\033[m valor digitado foi \033[30m{n2}\033[m.')
else:
    print(f'\033[m> O \033[36mmaior\033[m valor digitado foi \033[31m{n3}\033[m.')
if min([n1, n2, n3], key = int) == n1:
    print(f'\033[m> O \033[31mmenor\033[m valor digitado foi \033[33m{n1}\033[m.')
elif min([n1, n2, n3], key = int) == n2:
    print(f'\033[m> O \033[31mmenor\033[m valor digitado foi \033[30m{n2}\033[m.')
else:
    print(f'\033[m> O \033[31mmenor\033[m valor digitado foi \033[31m{n3}\033[m.')

''' Forma menos eficiente de fazer
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
elif n3 > n1 and n3 >n2:
    ma = n3

me = n1
if n2 < n1 and n2 < n3:
    me = n2
elif n3 < n1 and n3 < n2:
    me = n3'''