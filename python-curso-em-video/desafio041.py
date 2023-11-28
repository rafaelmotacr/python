# Analisando atletas

from datetime import date
i = int(input('> Digite o seu ano de nascimento: \033[30m'))
i = date.today().year - i
print(f'\033[m> O atleta tem {i} anos.')
if i <= 9:
    print('\033[m> Sua categoria é: \033[4;31mMirim\033[m.')
elif i <= 14:
    print('\033[m> Sua categoria é: \033[4;32minfantil\033[m.')
elif i <= 19:
    print('\033[m> Sua categoria é: \033[4;33mJunior\033[m.')
elif i <= 25:
    print('\033[m> Sua categoria é: \033[4;34mSênior\033[m.')
else:
    print('\033[m> Sua categoria é: \033[4;35mMaster\033[m.')
