# Ano bissexto

from datetime import date
a = int(input('> Digite um ano: \033[32m'))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'\033[m> O ano \033[32m{a}\033[36m é um ano bissexto\033[m.')
else:
    print(f'\033[m> O ano \033[32m{a}\033[31m não é um ano bissexto\033[m.')
    