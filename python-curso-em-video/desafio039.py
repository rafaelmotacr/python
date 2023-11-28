# Aistamento militar

from datetime import date
s = str(input('> Digite o seu sexo [Homem] ou [Mulher]: ')).strip().lower()
if 'homem' in s:
    i = int(input('> Digite seu ano de nascimento: \033[3;33m'))
    print(f'\033[30;40m> Quem nasceu em {i} tem {date.today().year - i} anos em {date.today().year}.')
    i = date.today().year - i
    if i < 18:
        print(f'\033[m> Você ainda irá se alistar ao serviço militar, faltam \033[36m{18 - i}\033[m anos para o seu alistamento!')
        print(f'> O seu alistamento será em {(date.today().year - i) + 18}'.upper())
    elif i == 18:
        print(f'\033[m> Considerando que você tem \033[32m{i}\033[m anos, está na hora de se alistar, amigão!')
    else:
        print(f'\033[m> Você já passou do tempo do alistamento! Como sua idade é \033[33m{i}\033[m, passaram \033[31m{i - 18}\033[m anos desde a idade de alistamento!')
        print(f'\033[0;0;41m> O seu alistamento foi em {(date.today().year - i) + 18}.'.upper())
elif 'mulher' in s:
    print('> Para as mulheres o alistamento é opcional!')
else: 
    print('> Resposta inválida!')