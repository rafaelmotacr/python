#  Criando um menu

from interface.interface import *
from arquivos.arquivos import *
from time import sleep 

arq = 'cursoemvideo.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True: 
    resposta = menu(['Ver pessaos cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        leia_arquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\'programa\' está deixando o chat...')
        break
    else:
        cabeçalho('Opção inválida!')
    sleep(1)
