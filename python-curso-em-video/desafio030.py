# Par ou impar

n = int(input('> Digite um número e o diremos se é par ou ímpar: \033[35m'))
print('\033[34m> É par!\033[m'if n % 2 == 0 else '\033[31m> É impar!\033[m')
