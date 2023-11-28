# Cálculo do Fatorial 

f = 1
n = int(input('> Digite o numero do qual deseja saber o fatorial: \033[31m'))
print('\033[m> ', end = '')
c = n
while c > 0:
    print(f'\033[m{c}', end = '')
    print('\033[32m x \033[m' if c > 1 else'\033[m = ', end = '')
    f *= c
    c -= 1
print(f)
print(f'\n> O fatorial deste numero ({n}!) eh igual a: {f}.\n')
