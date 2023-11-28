# jogo do par ou impar

from random import randint
print('\033[31;40m-=-\033[m' * 12)
print('\033[36;41m|      Jogo do par ou impar        |\033[m')
print('\033[31;40m-=-\033[m' * 12)
print('''\n\033[33;40m> Lore: Cada jogador escolhe um número
e palpita se a soma entre eles será
impar ou par. Você irá jogar contra mim, \033[31;40mo computador.\033[m''')
print('\n\033[36;40m> Regras:\033[m')
print('\n\033[32;40m* PAR: Se a soma for divisivel por dois.      \033[m')
print('\033[35;40m* ÍMPAR: Se a soma não for divisivel por dois.\033[m')
c = 1
v = 0
while True:
    pc = randint (0, 10)
    print(f'\n\033[36;41m------------| Rodada {c} |------------\n')
    es = str(input('\033[0;0;40m> Você escolhe Par ou ímpar [P/I]?:\033[0;0;31m ')).strip().upper()[0]
    if es == 'P':
        n = int(input('\033[0;0;40m> Digite um número:\033[0;0;31m '))
        if  (n + pc) % 2 == 0:
            v += 1
            print(f'\033[0;0;40m> Você escolheu {n} e \033[31;40mo computador\033[0;0;40m escolheu {pc}, totalizando {n + pc}. \033[36;40mResultado par!\033[m')
            print(f'\033[0;0;40m> \033[34;40mParabéns, você ganhou!\033[0;0;40m Sequência de vitórias: {v}.\033[m')
        else: 
            print(f'\033[0;0;40m> Você escolheu {n} e \033[31;40mo computador\033[0;0;40m escolheu {pc}, totalizando {n + pc}. \033[31;40mResultado impar!\033[m')
            print(f'\033[0;0;40m> \033[31;40mVocê perdeu!\033[0;0;40m Sequência de vitórias: {v}.\033[m')
            break
    elif es == 'I':
        n = int(input('\033[0;0;40m> Digite um número:\033[0;0;31m '))
        if  (n + pc) % 2 != 0:
            v += 1
            print(f'\033[0;0;40m> Você escolheu {n} e \033[31;40mo computador\033[0;0;40m escolheu {pc}, totalizando {n + pc}. \033[36;40mResultado impar!\033[m')
            print(f'\033[0;0;40m> \033[34;40mParabéns, você ganhou!\033[0;0;40m Sequência de vitórias: {v}.\033[m')
        else: 
            print(f'\033[0;0;40m> Você escolheu {n} e \033[31;40mo computador\033[0;0;40m escolheu {pc}, totalizando {n + pc}. \033[31;40mResultado par!\033[m')
            print(f'\033[0;0;40m> \033[31;40mVocê perdeu!\033[0;0;40m Sequência de vitórias: {v}.\033[m')
            break
    else:
        continue
    c += 1
print('\n\033[40m> EU, \033[31;40mKONO COMPUTADOR DA,\033[0;0;40m ganhei novamente!\n> Como você quebrou a sequência de vitórias, o jogo acaba aqui! Beijos bb, chama zap.\033[m\n')
