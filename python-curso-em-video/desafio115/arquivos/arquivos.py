from interface.interface import *

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
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
        print('Houve um ERRO durante a criação do arquivo!')
    else: 
        cabeçalho(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def leia_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao ler o arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO no abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else: 
            print(f'Novo registro de {nome} adicionado com sucesso!')

