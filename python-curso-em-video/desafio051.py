# Progressão aritiméica 

'''p = int(input('> Digite o primeiro termo da sua PA: \033[31m'))
r = int(input('\033[m> Digite a razão da PA: \033[31m'))
print('\033[m> Os dez primeiros termos da PA são:\033[32m', end = ' ')
for i in range(1, 11):
    if i == 9:
        print(f'{p} e ', end = '')
    elif i == 10:
        print(f'{p}.\033[m', end = '')
    else:
        print(f'{p} ➪  ', end = '')
    p += r# Progressão aritiméica '''

p = int(input('> Digite o primeiro termo da sua PA: \033[31m'))
r = int(input('\033[m> Digite a razão da PA: \033[31m'))
print('\033[m> Os dez primeiros termos da PA são:\033[32m', end = ' ')
d = p + (10 - 1) * r
for i in range (p, d + r, r):
    if i == d - r:
        print(f'{i} e ', end = '')
    elif i == d:
        print(f'{i}.\033[m', end = '')
    else:
        print(f'{i} ➪  ', end = '')
        