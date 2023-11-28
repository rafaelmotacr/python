# Vários números com flag

c = s = 0
while True:
    n = int(input('\033[33;40m> Digite um número: \033[31m'))
    if n == 999:
        break
    s += n
    c += 1
print(f'\033[33;40m> Foram digitados {c} números e a soma entre eles vale \033[32m{s}\033[m.\n\n ')
