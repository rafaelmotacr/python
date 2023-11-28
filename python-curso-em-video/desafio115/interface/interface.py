def leia_int(msg):
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
            return valor


def linha (tam = 42):
    return "-" * tam


def cabeçalho (txt): 
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    i = 1
    for item in lista:
        print(f'\033[33m{i:0>2}\033[m - \033[36m{item}\033[m')
        i += 1
    print(linha())
    opc = leia_int('\033[35mSua opção:\033[m ')
    return opc

