# Separando digitos de um número

n = int(input('> Digite um número: \033[32m'))
if (n <= 9999):
    print('\033[31m-' * 26)
    print('> Usando números inteiros:')
    print('-' * 26)
    m = n // 1000
    c = n // 100 % 10
    d = n // 10 % 10
    u = n % 10
    print(f'\033[m> Milhar \033[31m{m:2.0f}\033[m.\n> Centena \033[31m{c:0.0f}\033[m.\n> Dezena \033[31m{d:2.0f}\033[m.\n> unidade \033[31m{u:0.0f}\033[m.')
    print('\033[36m-' * 17)
    print('> Usando strings:')
    print('-' * 17)
    ms = str(n)
    print(f'\033[m> Milhar \033[36m{ms[0]:>2}\033[m.\n> Centena \033[36m{ms[1]:0}\033[m.\n> Dezena \033[36m{ms[2]:>2}\033[m.\n> Unidade \033[36m{ms[3]:0}\033[m.\n')    
else:
    print('> O número digitado é inváldio.')
