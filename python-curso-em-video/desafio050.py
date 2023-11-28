# Soma dos pares

c = s = 0
for i in range (1, 7):
    n = int(input(f'\033[30;40m> Digite o {i}º valor a ser somado: \033[36;40m'))
    if n % 2 == 0:
        s += n
        c  += 1
print(f'\033[30;40m> Você digitou {c} números pares e a soma dele é \033[32m{s}\033[m.')
