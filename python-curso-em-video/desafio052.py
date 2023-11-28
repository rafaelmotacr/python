# Números primos

p = 0
n = int(input(f'\033[30;40m> Digite o número que deseja saber se é primo ou não: \033[35;40m'))
print('\033[30;40m> Divisores: \033[m', end = '')
for i in range(1, n + 1):
    if n % i == 0:
        p += 1 
        print(f'\033[32;40m{i}\033[40m', end = ' ' )
    else:
        print(f'\033[35;40m{i}\033[40m', end = ' ' )
if p == 2:
    print(f'\n\033[30;40m> O número \033[35;40m{n}\033[36;40m é primo.\033[30;40m Seus únicos divisores são \033[32;40m{n} e 1\033[m.')
else:    
    print(f'\n\033[30;40m> O número \033[35;40m{n}\033[31;40m não é primo.\033[30;40m Ele foi divisível {p} vezes, portanto não é primo.\033[m')
