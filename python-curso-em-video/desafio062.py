# Super progressão aritimética v3.0

c = 2
co = 0
i = int(input('> Digite o primeiro termo da sua PA: \033[31m'))
r = int(input('\033[m> Digite a razão da PA: \033[31m'))
print('\033[m> Os dez primeiros termos da PA são:\033[32m', end = ' ')
d = i + (10 - 1) * r
while c != 0:
    while i <= d:
        if i == d - r:
            print(f'{i} e ', end = '')
        elif i == d:
            print(f'{i}.\033[m', end = '')
        else:
            print(f'{i} ➪  ', end = '')
        i += r
        co += 1
    c = int(input('\n\n> Deseja ver mais termos desta PA? Caso sim, digite quantos. Senão, digite zero: '))
    d = i + (c - 1) * r
    print(f'> Aqui estão os {c} próximos termos: \033[32m' if c!= 0 else '\n\033[36;40m> Wakarimasta!\033[m', end = '')
print(f'\n> Ao todo, foram mostrados {co} termos dessa PA com razão {r}.\n\n')
