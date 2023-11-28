# Interactive helping system in Python

def boiolagem(cor, text):
    print(f'{cor}', end = '')
    print('~' * (len(text) + 4))
    print(f'  {text}')
    print('~' * (len(text) + 4))
    print('\033[m', end ='')


def ajuda(entrada):
    boiolagem('\033[0;33;40m', f'Acessando o manual do comando \'{entrada}\'')
    print(f'\033[0;31;40m')
    help(entrada)


fun = str()
while True:
    boiolagem('\033[1;36;40m','SISTEMA DE AJUDA PyHELP')
    fun = str(input('\033[mFunção ou biblioteca > ')).lower().strip()
    if fun == 'fim':
        print('> Encerrando o programa...\n')
        break
    elif fun == '':
        continue
    ajuda(fun)
