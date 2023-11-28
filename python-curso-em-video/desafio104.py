# Validando entrada de dados em Python

def leiaint(msg):
    valor = 0
    while True:
        num = input(msg)
        if not(num.isnumeric()):
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        else:
            valor = int(num)
            break
    return valor


n = leiaint('> Digite um número: ')
print(f'> Você acabou de digitar o número inteiro {n}.')
