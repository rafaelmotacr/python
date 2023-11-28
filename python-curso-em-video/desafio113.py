# Funções aprofundadas em python 

def leiaint(msg):
    valor = 0
    while True:
        num = input(msg).strip()
        if num == '':
            print('\033[31m> Usuário preferiu não digitar este número.\033[m')
            break 
        try:
            valor = int(num)
        except Exception as erro: 
            print(f'\033[31m> Tivemos um erro com o valor {erro.__class__}.\033[m')
            continue
        else:
            print('> Deu bom!')
        return valor


def leiafloat(msg =''):
    valor = 0
    while True:
        num = input(msg).strip().replace(',','.')
        if num == '':
            print('\033[31m> Usuário preferiu não digitar este número.\033[m')
            break 
        try:
            float(num)
        except Exception as erro: 
            print(f'\033[31m> Tivemos um erro com o valor {erro.__class__}.\033[m')
            continue
        else:
            print('> Deu bom!')
        return valor


leiaint('> Digite um número inteiro: ')
leiafloat('> Digite um número com ponto flotuante: ')
