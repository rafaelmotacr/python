# Análise de dados do grupo

from time import sleep
ab18 = sub20 = i = e = ma = 0 
co = 1
while True:
    if e == 0:
        print(f'\033[32;40m-----| Pessoa {co} |-----\033[m')
        e += 1
    if e == 1:
        i = int(input('> Idade: '))
        if i > 18:
            ab18 += 1 
        e += 1
    if e == 2:
        s = str(input('> Sexo [M/F]: ')).strip().upper()[0]
        if s == 'M':
            ma += 1
        elif s == 'F':
            if i < 20:
                sub20 += 1
        else:
            continue
        e += 1
    if e == 3:
        c = str(input('> Quer continuar? [S/N]:')).strip().upper()[0]
        if c == 'N':
            break
        elif c == 'S':
            print('\n', end = '')
            e = 0
            co += 1
            continue
        else:
            continue
print("> Fim do programa... Compilando resultados.\n")
sleep(2)
print(f'> Ao todo, foram cadastradas {co} pessoas, das quais:\n> {ab18} possuem mais de 18 anos.\n> {ma} foram declaradas homens.\n> E {sub20} são mulheres com menos de 20 anos.\n')
