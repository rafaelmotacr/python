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
            return valor


def arquivo_existe(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True
    

def criar_arquivo(nome): 
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro durante a criação do arquivo!')
    else: 
        cabeçalho(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def leia_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
        


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
    opc = leiaint('\033[35mSua opção:\033[m ')
    return opc


