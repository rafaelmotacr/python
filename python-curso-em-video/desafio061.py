# Progressão aritimética v2.0

c = 0
i = int(input('> Digite o primeiro termo da sua PA: \033[31m'))
r = int(input('\033[m> Digite a razão da PA: \033[31m'))
print('\033[m> Os dez primeiros termos da PA são:\033[32m', end = ' ')
while c <= 10:
    if c == 9 :
        print(f'{i} e ', end = '')
    elif c == 10:
        print(f'{i}.\033[m', end = '')
    else:
        print(f'{i} ➪  ', end = '')
    i += r
    c += 1
