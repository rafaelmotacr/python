# Criando um menu de opções

n1 = int(input('> Digite um número: '))
n2 = int(input('> Digite outro número: '))
r = 0
while r != 5:
    print('> Qual operação deseja realizar?\033[32m\n\n[1] - Somar\n[2] - Multiplicar\n[3] - Encontrar o maior valor\n[4] - Digitar novos números\n[5] - Sair do programa\n\033[m')
    r = int(input('> Digite sua escolha: '))
    if r == 1:
        print(f'\033[31;40m> A soma entre {n1} e {n2} vale {n1 + n2}.\033[m\n')
    elif r == 2:
        print(f'\033[31;40m> A multiplicação de {n1} por {n2} vale {n1 * n2}.\033[m\n')
    elif r == 3:
        print(f'\033[31;40m> O maior número entre {n1} e {n2} é {max(n1, n2)}.\033[m\n')
    elif r == 4:
        n1 = int(input('> Digite um novo número: '))
        n2 = int(input('> Digite um novo número: '))
    elif r == 5:
        print(f'\033[31;40m> Obrigado por utilizar nosso programa!\033[m\n')
        break
    else:
        print('\033[31;40m> Resposta inválida! Tente novamente!\033[m')
        continue