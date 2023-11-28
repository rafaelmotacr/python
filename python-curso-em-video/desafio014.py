# Conversor de temperaturas

c = float(input('> Digite uma temperatura em graus celsius: \033[31m'))
print(f'\033[m> A temperatura digitada (\033[31m{c:.2f}\033[m ºC) em graus farenheint é igual a: \033[32m{c * 9 / 5 + 32:.2f}\033[m ºF')
