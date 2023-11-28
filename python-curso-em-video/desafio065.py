# Maior e menor valores

co = ma = me = ac = 0
r = 's'
while r not in 'nN':
    n = int(input('> Digite um número inteiro: \033[31m'))
    if co == 1:
        me = n
    if n > ma:
        ma = n
    elif  n < me:
        me = n 
    ac += n
    co += 1
    r = str(input('\033[m> Deseja digitar outro número? [S/N]: ')).strip().upper()[0]
    if r not in 'Nn' and r not in 'Ss':
        print('\n\033[36;40m> Resposta inválida! Tente novamente!\033[m')
        break 
md = ac / co
print(f'\n\033[36;40m> Foram digitados {co} valor, onde: \n> {me} foi o menor valor.\n> {ma} foi o maior valor.\n> {ac} foi a soma dos valores.\n> E {ac / co:.2f} é a média dentre eles.\033[m\n')





