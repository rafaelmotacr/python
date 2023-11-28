# Sequência de Fibonacci v1.0

l =  int(input('> Digite quantos termos da sequência de Fibos deseja conhecer: \033[31m')) - 1
n1 = 1
n2 = n3 = i = 0
print(f'\033[30;40m> A sequência até o {l + 1}º termo é: ', end = '')
while i <= l:
    if i == l - 1:
        print(f'{n3} e ', end = '')
    elif i == l:
        print(f'{n3}.\033[m')
    else:
        print(f'{n3}, ', end = '')
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    i += 1
