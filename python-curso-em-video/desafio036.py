# Aprovando empréstimo

c = float(input('\033[m> Diga qual o valor da casa: \033[30m'))
s = float(input('\033[m> Digite o seu salário atual: \033[30m'))
a = int(input('\033[m> Em quantos anos você pretende pagar a casa?: \033[30m'))
p = s * 30 / 100
pm = c / (a * 12)
if pm > p:
    print(f'\033[m> Para pagar uma casa de \033[33mR$ {c:.2f}\033[m em \033[32m{a} anos\033[m, a prestação mensal será de \033[33mR$ {pm:.2f}\033[m, que equivale a \033[31m{pm * 100 / s :.0f}%\033[m do seu salário atual.\n> O seu empréstimo foi \033[4;31mnegado!\033[m')
else:
    print(f'\033[m> Para pagar uma casa de \033[33mR$ {c:.2f}\033[m em \033[32m{a} anos\033[m, a prestação mensal será de \033[33mR$ {pm:.2f}\033[m, que equivale a \033[31m{pm * 100 / s :.0f}%\033[m do seu salário atual.\n> O seu empréstimo foi \033[4;36maprovado!\033[m')